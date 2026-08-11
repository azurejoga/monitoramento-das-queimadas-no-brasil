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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c47e200e-c48a-37c3-bbb7-163aca0b75ed | -2.25461 | -55.07233 | 2026-08-11 12:14:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5fa601e6-502a-3ede-bc63-91a8b71ce14b | -5.80528 | -45.05956 | 2026-08-11 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2bcf9d79-823a-3e1b-adb6-26058c005317 | -2.76519 | -49.46003 | 2026-08-11 12:14:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a4c35397-aef6-37e6-827e-bde3522cb47d | 2.1449 | -50.94345 | 2026-08-11 12:14:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88c20890-d742-30e9-832e-f995c4d3a108 | -2.77566 | -49.46144 | 2026-08-11 12:14:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68962a0f-a1a6-3547-b84b-eb7f0e7be6da | -10.11892 | -46.2126 | 2026-08-11 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 367894ec-53d3-3da9-8e6a-e08ab7a89eb2 | -14.27711 | -45.30626 | 2026-08-11 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5d06b9d4-50c4-3af3-8846-8ed3ef0e0619 | -9.36931 | -48.03114 | 2026-08-11 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 495e857c-f188-3249-9333-09b2db6174a7 | -14.28138 | -45.26492 | 2026-08-11 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 0003a6bc-27ae-3d10-b4c2-86701fc32ea8 | -6.25258 | -55.62014 | 2026-08-11 12:17:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d139d8a7-263f-30e3-9e17-918bd4d6ca88 | -10.72549 | -50.44496 | 2026-08-11 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e6d21287-7bb4-39b6-8df5-1ecb02a01d7e | -11.45309 | -46.69841 | 2026-08-11 12:17:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8301a3a4-2f6c-30ad-bbbf-4e5eda745737 | -8.95141 | -60.53405 | 2026-08-11 12:17:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0a7dc0e3-8a73-3b5b-8bc9-063095eefae8 | -8.948 | -60.50342 | 2026-08-11 12:17:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9ecd1c95-f04d-3d74-8f62-3365abeab2c4 | -12.22249 | -56.55926 | 2026-08-11 12:17:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ec21095-02e1-3fb7-afd9-6b48952e5402 | -9.38158 | -47.47454 | 2026-08-11 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 37689904-fef6-3025-87b5-0ee6c774dd5e | -7.62821 | -47.56534 | 2026-08-11 12:17:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 29bca84c-735b-3b21-b9ee-956829bd33a8 | -9.3747 | -47.4681 | 2026-08-11 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 120b9ea8-1133-3338-8303-311d571b0a63 | -11.66837 | -51.66731 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 3f9304f2-6e2c-3e71-b80c-61fe3f2487ef | -10.72732 | -50.43069 | 2026-08-11 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 13a27b41-632a-3acf-aeaa-ebab4e03acb7 | -13.5508 | -46.28209 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 269349ea-ea95-3994-9771-8661cbb92880 | -10.11621 | -46.21768 | 2026-08-11 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| eb7b5d2f-172f-3a29-aeb5-8b254c29beb5 | -13.54735 | -46.31556 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9f9a62d3-e76b-3efd-9428-2d66a0d75bd9 | -14.46302 | -45.67265 | 2026-08-11 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| be78158b-48cf-3831-9168-17fdeee1d085 | -9.3719 | -48.01003 | 2026-08-11 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| ed13485d-c8f4-3125-a1ed-942c89531da5 | -10.42601 | -46.68392 | 2026-08-11 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 607374ff-4fce-3fce-84c9-182760c3af7f | -9.47936 | -60.52869 | 2026-08-11 12:17:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 14ee95a4-071a-3140-9759-b29b2d2e2b4b | -10.11976 | -46.18659 | 2026-08-11 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2b095bd8-cfa7-39e8-bda6-b2695f444fd2 | -12.49247 | -45.28368 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ef963754-6c33-35c4-8cbf-a59f05af6bc9 | -11.87737 | -48.05802 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 5be46951-a44a-31c0-94c1-b96297908c27 | -6.65741 | -55.43638 | 2026-08-11 12:17:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7623bf6e-1b18-3b41-ba56-6487fa59b33b | -11.66994 | -51.65523 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 89e90394-59aa-3603-a089-c351bca26512 | -11.88059 | -48.07619 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 0240ae9c-a5f0-3c1e-9a36-e80ae327429e | -8.95693 | -60.49816 | 2026-08-11 12:17:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 6bf561ee-e488-30d0-8cba-205a64edfd90 | -11.45636 | -46.66975 | 2026-08-11 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a3e25f41-e25a-3ef2-955f-a53609002316 | -11.65818 | -51.66603 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6e948edc-fade-38bb-8724-ed144a3729c3 | -7.64143 | -47.56693 | 2026-08-11 12:17:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bb66e275-d7f3-31d0-871f-9945a92b09ca | -14.28319 | -45.2721 | 2026-08-11 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 23f033c7-8373-331c-bd1a-386f74909bdf | -6.84649 | -56.41101 | 2026-08-11 12:17:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2bb260fb-527e-3207-8dcd-0510653a4f2e | -11.87479 | -48.08088 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5e3db1c5-c016-37de-a415-9b5fe614ee5f | -12.4961 | -45.29145 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 4a588a6b-690c-3fbd-b3df-9c90c440b42f | -10.42231 | -46.70639 | 2026-08-11 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| bb46e394-4897-3dc0-a7fe-30d72340c674 | -10.42573 | -46.67845 | 2026-08-11 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 70f109dd-e656-39ec-b3a6-6b0670b8a027 | -14.27918 | -45.31353 | 2026-08-11 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 660d3ccd-66b4-3b43-ac51-0511e15a313a | -11.65974 | -51.654 | 2026-08-11 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 26070cd4-ba03-3a4d-a791-71fb0a371411 | -14.45877 | -45.66729 | 2026-08-11 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| dea1902d-0818-30ad-9c52-7338f8f3c21e | -11.48993 | -54.60064 | 2026-08-11 12:17:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 39440974-303e-3a5c-8e53-57498d6b551d | -9.38839 | -47.46988 | 2026-08-11 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 670823dd-2c7d-3260-b275-f9190df9987e | -13.84355 | -53.69233 | 2026-08-11 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d1475b28-db23-330c-bd7a-f70e14f27dd9 | -13.84488 | -53.68232 | 2026-08-11 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1b3e8008-00fa-3ea1-82bb-cb2b22e8873e | -15.15739 | -52.6878 | 2026-08-11 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 627cbe82-a84c-3426-87a1-02fe888c1f16 | -13.85792 | -53.79605 | 2026-08-11 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| fc0a6bb2-d2a6-3e76-b43d-c79309b87314 | -14.2591 | -51.96859 | 2026-08-11 12:19:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8af9ed02-fea2-34e5-9dad-a35285d7d161 | -16.8692 | -48.89597 | 2026-08-11 12:19:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 0990ff22-4b09-31b1-abbd-1e9dc4444393 | -14.50965 | -49.29326 | 2026-08-11 12:19:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c5c975f9-c685-3584-ad25-a5f24a7f71a6 | -13.87637 | -53.79868 | 2026-08-11 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ace679c9-6439-3608-b90b-8ddc44c5cb0c | -15.15758 | -52.68204 | 2026-08-11 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4dd0539a-d398-3118-81b0-a87b7d17f3ad | -16.86253 | -48.90065 | 2026-08-11 12:19:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| cfa618c8-ff33-39fb-a4d2-e8bbd68fd2dc | -14.2877 | -45.2835 | 2026-08-11 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| fe16d9b7-87f3-3d32-8b6f-4f7da1375603 | -13.8608 | -53.8053 | 2026-08-11 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e9501dc5-8504-3e3a-a428-5620f7637e00 | -9.3906 | -47.4878 | 2026-08-11 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2d5cd57d-6209-3fc0-827d-9f3663055393 | -10.4237 | -46.6809 | 2026-08-11 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0113fb1b-43e2-30a0-9815-9bff54f9e34b | -9.3909 | -47.4656 | 2026-08-11 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| a5436431-b0c9-3c12-8561-13b949ca64c6 | -14.2877 | -45.2835 | 2026-08-11 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ee4abd52-c218-37fa-a098-def035fb84ea | -9.3717 | -47.4897 | 2026-08-11 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9d2dace4-3d9f-3c11-b58d-f73e2a8382d9 | -13.8611 | -53.7845 | 2026-08-11 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 37b09e5a-9a5a-382d-90de-9e8ff1f7166b | -9.3909 | -47.4656 | 2026-08-11 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a3a1e08e-9c0c-3132-b5c5-d4eb53c52798 | -9.3906 | -47.4878 | 2026-08-11 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b0d1a541-031e-3de1-872d-0c2c67847aae | -14.2559 | -51.9686 | 2026-08-11 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 9140750c-92cd-3a1c-a2bf-448c7b49ba77 | -14.2877 | -45.2835 | 2026-08-11 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3a47ec0d-2f3f-3864-b903-da35d2912567 | -9.3717 | -47.4897 | 2026-08-11 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f071e591-ec7e-3364-accd-679e2a1f1ab3 | -13.5498 | -46.3074 | 2026-08-11 12:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a102e764-8e0d-3bf8-9e7f-7d8af902e818 | -8.9602 | -60.4973 | 2026-08-11 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4ed0b76a-71db-32b4-adf4-0c99b5e3dd3a | -9.3909 | -47.4656 | 2026-08-11 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1237fb85-40fc-3839-8291-74fe5594739d | -14.2559 | -51.9686 | 2026-08-11 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c44ed164-4a7b-38bc-b518-10f15b971dc7 | -9.3717 | -47.4897 | 2026-08-11 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 70eba81f-34f1-356c-8ebb-9a447f35534a | -14.2877 | -45.2835 | 2026-08-11 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5ba59501-de6b-3a20-a0fa-ca8f0133b5be | -9.3906 | -47.4878 | 2026-08-11 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| abcc77c8-60e7-3e80-a2f6-03b48050496e | -10.2271 | -45.8708 | 2026-08-11 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 008c02db-c515-34a8-89d3-393b34207bc1 | -14.2559 | -51.9686 | 2026-08-11 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c428c5c9-1dd7-312b-937d-822fd653a590 | -9.3909 | -47.4656 | 2026-08-11 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| fbdfd714-62bd-3b04-a23a-27a5eef192d1 | -13.8211 | -53.8931 | 2026-08-11 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e4cdd50f-3ca9-3726-a3c6-927b0f6e00cb | -13.8204 | -53.9347 | 2026-08-11 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5d124f68-b912-37ea-bc13-6c86397a6f58 | -13.5498 | -46.3074 | 2026-08-11 13:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 656af437-1a35-35e6-8ee9-8b2056a329b4 | -14.2877 | -45.2835 | 2026-08-11 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 581335e6-37f0-3976-81e7-422521d34051 | -10.2271 | -45.8708 | 2026-08-11 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 604f0fc4-29de-31bd-b0b3-8eb191949932 | -9.3906 | -47.4878 | 2026-08-11 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 285.2 |
| 9e10d891-f88a-32a8-9fdc-88d1ed2bfcf1 | -9.3717 | -47.4897 | 2026-08-11 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 198.2 |
| c6344b45-b1c2-3cba-916f-4c10870dda83 | -10.4237 | -46.6809 | 2026-08-11 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| d3bb7c27-3283-32b9-ba01-bcf43f5ca951 | -14.2559 | -51.9686 | 2026-08-11 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fa7ebc9f-9748-32f9-86fa-78c7421ce37a | -10.2271 | -45.8708 | 2026-08-11 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 4cffb54b-d62b-389d-828d-fc22e2dde0c3 | -8.96 | -60.5358 | 2026-08-11 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 06bbb0f3-558b-3475-a16e-42b31d9593c2 | -13.5498 | -46.3074 | 2026-08-11 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 046d59d1-124c-33fb-825f-51ebb314257f | -13.8608 | -53.8053 | 2026-08-11 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 835bb1a4-0a6b-3d43-bfd5-a05dbcdd59c6 | -9.3909 | -47.4656 | 2026-08-11 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 2a770817-8619-3e17-8ee6-94890e632153 | -14.2877 | -45.2835 | 2026-08-11 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 2700d54f-e348-3ebf-ab7f-f2e86e19d626 | -10.4237 | -46.6809 | 2026-08-11 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| bac913f8-5248-32c1-9490-78d91144f77f | -9.3906 | -47.4878 | 2026-08-11 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ab789ecf-a652-3dac-8f15-ed4c9e2b9ed7 | -14.6463 | -47.6474 | 2026-08-11 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 289.7 |
| 05c75df7-3049-3716-94db-349f0f15faf9 | -14.6458 | -47.67 | 2026-08-11 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |


[Clique aqui para ver as próximas entradas](README33.md)
