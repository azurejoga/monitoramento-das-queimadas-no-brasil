# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 654aac48-c0a3-328c-b047-576322307419 | -3.99598 | -46.94469 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8927edc6-3c9f-32e7-8909-ff4e15da6e97 | -5.37344 | -44.84789 | 2024-12-28 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1f64e53-a95b-3efa-a672-9856a1784b76 | -3.81736 | -46.0594 | 2024-12-28 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cea73f03-ebaa-33e5-8302-220a7748bdd7 | -4.56331 | -44.12212 | 2024-12-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffe5f2b8-e741-347a-87d6-f0134cf03a38 | -4.4085 | -50.4323 | 2024-12-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6dc2d6-ea01-3548-8d6c-7de38d0d1266 | -3.66711 | -53.84058 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 567c2e38-4e93-3646-afb4-1e43c4614fd9 | -5.63888 | -43.72801 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de0dae66-7869-3894-9b20-260e76782a76 | -3.86671 | -47.02311 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e921fbc4-9093-3183-a703-815445ec99ca | -5.5759 | -46.14335 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4f09588-c16f-31b0-8025-f9bad4ff2e28 | -3.7399 | -47.18508 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41956a48-6a5e-3b59-a863-7e89aea86743 | -3.92853 | -46.98447 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 352c65a6-bae3-3b01-b9ac-a0d73d1f627d | -3.203 | -53.94245 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54af5744-8be0-34e1-aa4a-ffee2b2b901c | -2.57396 | -53.99289 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef75297-fa63-31a2-a443-705dd47df48b | -4.03567 | -47.05738 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15b15eab-4ea5-3cf4-b6c7-d2bea896dc3c | -2.4849 | -54.1711 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 289058be-4b9e-3d4f-a1a9-9efd2a41eff2 | -4.11729 | -46.71228 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0204d726-5a32-322a-9fbb-355777643ed8 | -3.99163 | -46.69361 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ceb5537-7108-3e74-aa1c-1ecce4bea255 | -2.4919 | -54.16898 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 149eaefd-94ee-3608-af31-cf40a990a41c | -5.31031 | -46.06855 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab835284-fed5-3b1b-b8e3-ff3c226caaf4 | -3.86713 | -47.02029 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818ecfcc-038f-3d12-9fc9-37df2c44ca74 | -5.63501 | -43.72381 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bda004c9-7b4f-3fc0-a57b-d782ecbd4dd8 | -4.03689 | -47.049 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c624edb-2063-3e53-9448-5750c002d924 | -2.70238 | -54.06212 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2197fb82-e48a-3cd3-b1ee-baeb346362b2 | -4.08184 | -46.81164 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b88621-fd9b-3915-b7c8-def062f1c460 | -4.11684 | -46.71535 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07d3cb4b-eff4-315a-b6cb-9681e7a51a98 | -5.90511 | -43.48322 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6b0c7b0-9eea-3ffd-b785-1f88b1b3485c | -6.21223 | -46.21964 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0726f02f-e338-39c7-834f-1051b503ac25 | -5.91154 | -43.4845 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd1ae565-0a38-3692-af80-93e903243a71 | -1.94508 | -53.34996 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31b32efa-0cb7-3068-ac96-a0434a3cbc88 | -3.74322 | -47.34908 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6ea6711-1484-3c09-bfa7-4df4f529683f | -4.07723 | -47.0869 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9d54ab28-bd52-390e-a902-20642ab29bfe | -3.73834 | -47.3484 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1d50914-53ee-3f6a-9ceb-156241bb3bde | -2.84679 | -51.87557 | 2024-12-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2de20079-52f5-32e9-91b1-ccd6ed6f8b3b | -2.95507 | -51.76011 | 2024-12-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2f6baa-df01-3261-9e17-c145f692924c | -1.9288 | -53.3438 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 600f8de0-abdc-3046-b533-275e44be7eb8 | -4.04148 | -47.05252 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff36133-7e7b-329f-8dc1-93c48b241d9b | -1.79898 | -53.80075 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8ba8eac-ade9-3ec3-84d4-6e415fec949d | -4.50248 | -44.23923 | 2024-12-28 05:01:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d98d42a3-197c-3fcb-b639-fd7d2ba58dae | -2.2617 | -53.88302 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d47fbfe-3487-314f-ad42-8cdc668a4f62 | -2.41696 | -54.21379 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0e2c8ee-d9e7-3d75-bcfc-4e9a7862c856 | -4.03149 | -47.05101 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aafc8efc-0f44-3bcb-b699-1920e07e105c | -3.76614 | -47.22501 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab3536ab-fdf4-3ded-9e58-b0b45e2771ab | -3.9417 | -46.76436 | 2024-12-28 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ded75ee-bbe0-384f-bbf5-d26b51f13d7f | -4.13198 | -46.68378 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4794175-e540-30f0-ad7e-975e60670520 | -3.73415 | -47.18979 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b9f559-ba74-3b33-a698-b1fe22f0901f | -3.99118 | -46.69668 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03262fe1-50f1-32c8-8373-9ab2d21fe38d | -2.90657 | -54.4923 | 2024-12-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab010be7-4544-3a1b-b707-d0255f400604 | -3.92391 | -46.98098 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39ef5b89-4a45-3e7f-89d6-51c6031e2daa | -2.21712 | -53.6497 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 380b700d-db9b-3a57-aebc-3d8938bd2b74 | -5.57774 | -46.13028 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 40613bf6-7132-39d0-8d43-e742f1d89a5a | -2.65009 | -54.00397 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ffddc9-175c-3fea-9249-036bd95a38e3 | -4.04189 | -47.04971 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ebabe9e-21ef-370f-801e-97a7ecae1198 | -3.53295 | -53.80508 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 931067cd-a477-3019-bb74-925ff4cff56e | -3.95127 | -49.44405 | 2024-12-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9dace873-077b-354a-beec-94831b2d2c9f | -4.08567 | -47.09867 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29508ffd-9878-3897-b500-1903bdab5b70 | -2.72989 | -54.12386 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50e2f84a-0eac-380f-b740-0e59f2f613c1 | -3.75633 | -47.22336 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 164038c7-6195-3d68-a2c3-f6ade6313de0 | -3.8744 | -46.69106 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25c5f350-4590-3f1d-aa76-bd562e591c77 | -2.22047 | -53.65022 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dee41202-8e4d-3029-844f-2d57cf0cc411 | -3.52992 | -53.93531 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa7ab46-d0f3-32b6-bff7-6988d884bf79 | -3.72348 | -47.19382 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee23cdb5-8ba5-379f-ba9a-dcb069f9eaa9 | -3.74481 | -47.18591 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e57cb12-4cd4-3ce9-ac59-d079fa443c9f | -4.00189 | -46.69498 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 643bf35e-1232-31fc-ae29-272ea0fddf28 | -5.64137 | -43.72477 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae95198-0002-34f0-9d8f-fe94afd2ca53 | -2.90711 | -54.48884 | 2024-12-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262b29e8-7227-358e-ab55-e926a35cb124 | -3.74544 | -47.34725 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fc36349-8cfb-3865-a489-f1fe832b1cef | -5.64204 | -43.71978 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eefaf365-b804-3529-88ee-f3a49e521d4c | -2.41865 | -54.2247 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28135767-5949-3947-a66d-ae3ac6542ab7 | -2.47548 | -54.16609 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91570890-550d-3e2f-a204-8ec74163825f | -2.37459 | -53.68138 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dbc824-0e8f-3c5a-802d-9b4646d5cea3 | -3.99631 | -46.69738 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d39ad1c-4fe7-3220-b028-9ba73900ccf0 | -3.89798 | -46.98515 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f287131d-cd48-3b4e-8ab3-bafdbdb11211 | -3.53741 | -53.79849 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f59d5289-6300-32be-a154-9c91836045ed | -4.73765 | -44.65311 | 2024-12-28 05:01:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fb6685-92a7-3f1a-9aa1-56fb9779618b | -2.16913 | -54.42966 | 2024-12-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f29b869c-9ada-3a31-9412-619d35aa40a8 | -3.76123 | -47.22427 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8e004b3-4d1d-334f-80a8-33157382f5f4 | -4.50315 | -44.23459 | 2024-12-28 05:01:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b53d055f-7df9-392a-9cb7-1362ef13cb96 | -2.21657 | -53.65322 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79faccd4-8a4f-31f5-9999-080ac22969ff | -2.88494 | -54.02277 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66083708-44e9-3b4d-9839-909203c50356 | -3.89756 | -46.98796 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f91eb222-2c3c-3231-96c2-dc9d7ab85677 | -4.06726 | -46.7327 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f3d03b-74ba-3017-aea4-05f58f810599 | -4.10311 | -46.80836 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bf8fc32-6c1e-39ea-bc0f-bfb949abfa64 | -2.48804 | -54.17194 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6892bd44-718a-347a-9ac9-bcbd22a9a82b | -16.09446 | -60.1203 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64e9a9af-8c48-3509-8132-8985d70906fe | -11.13308 | -43.30302 | 2024-12-28 05:03:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b98beb07-8a0b-3d12-ac71-b2b4e94fdf1f | -12.59268 | -62.00938 | 2024-12-28 05:03:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b4eb6e2-0db0-3c57-b1c2-0b17748e7451 | -16.09855 | -60.11702 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfd19b6a-fee6-39e5-9123-b2567a9512ea | -15.62865 | -57.28227 | 2024-12-28 05:03:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e67e4593-c149-35b2-abcd-5c5d6a7985f5 | -15.09143 | -59.62791 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b5f1992-b874-3af9-84ae-d4980a1c6b69 | -15.03095 | -59.69591 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37120db0-d3ac-335b-be8b-e432977eb3b1 | -15.28418 | -59.88113 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e188975a-f6ba-330f-96c9-955ccb8bb8e7 | -15.07715 | -59.62932 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61b5af51-231b-3107-b258-69e99c482ab5 | -16.0979 | -60.12092 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69fe4ddd-468b-33e8-815b-8549d90a1f32 | -11.13931 | -43.31049 | 2024-12-28 05:03:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a36b5eba-fd11-3f6e-9a67-22b4c174881d | -15.27386 | -59.8793 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5f368a0-4695-37ed-b891-2258b08dafdd | -16.09939 | -60.06908 | 2024-12-28 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e227144-e36e-3f0b-94f6-4a44431919af | -12.44846 | -64.1513 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc7f458c-8532-3ec0-997a-95b7595006cd | -15.51852 | -59.4209 | 2024-12-28 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67c000d7-fc75-3dd8-8915-e1a3a68e74de | -12.34463 | -64.17741 | 2024-12-28 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c69f944-399b-3317-94bb-e2cb275a6e65 | -11.96975 | -63.51368 | 2024-12-28 05:03:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README23.md)
