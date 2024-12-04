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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9babc54c-5fe9-35f3-95ca-639e08a30981 | -2.06947 | -45.49114 | 2024-12-04 00:54:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 55b2350e-bf88-3ed9-9063-0cf6e49a69b2 | -4.19995 | -50.68023 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5631942a-967f-3a56-85bc-2de6346e19b1 | -2.99362 | -54.10097 | 2024-12-04 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| abeed9cd-5a89-32ce-a6de-9ad721fec9c5 | -2.05024 | -46.51368 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53a1e539-0fa6-3bd6-8b8b-e52ee9b1c152 | -2.87934 | -51.79393 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 01626b53-301f-3f40-9f1b-b1fd109f9857 | -3.06855 | -53.28096 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ba3040ff-3246-327f-b7b8-e854a6793304 | -3.00948 | -52.45504 | 2024-12-04 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 43e3552e-a855-34b0-a27f-880222eecaa9 | -4.08027 | -46.19717 | 2024-12-04 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b1cbea95-7f06-3aab-837f-f9fe3d048a6f | -2.64535 | -45.73945 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e85d00b6-deb7-38a5-8528-71ead11f8f51 | -1.70501 | -52.77396 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2edfa1b9-e954-343a-928d-edc936e2c8dc | -4.24765 | -47.57705 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3aafc20d-8b27-3f9b-88d0-94761fa98799 | -3.73342 | -51.23962 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ee351c62-f57f-39e6-8e20-5f638c5a1549 | -5.61806 | -43.94749 | 2024-12-04 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c6a82020-c6f6-3c6f-928c-bb49eccf9b09 | -2.47354 | -46.55055 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f83a553f-454f-3a59-ac07-d954caa055b5 | -4.12456 | -48.53718 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 31f6370c-1af4-382e-8e2c-269ce8f5bd95 | -3.3269 | -50.35158 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af54721e-2304-3f32-bfb5-f745755e0628 | -2.89876 | -51.58097 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a8745896-d3f6-350c-939f-36b59ae27dd6 | -4.11988 | -43.91552 | 2024-12-04 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| dbb1dd39-63db-3431-9983-a555c66db4e3 | -3.56025 | -50.17644 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1754c43d-7979-30e6-af71-59e90e4a4f9a | -3.02886 | -51.5402 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c69e4d6a-3948-3bd0-9c87-fe1f93fd6aa0 | -3.55252 | -50.18678 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ee96d610-fff7-3e2f-8e67-83c9774e2414 | -3.96515 | -52.19773 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| db5f0f8e-ad1a-3d72-be0f-e8cf41c7a36f | -2.63337 | -45.72883 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1824f3d6-3c98-315f-93ab-bbd25ed87672 | -1.75681 | -52.63291 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 95e08e68-a304-3e08-9e40-9da2a790ebb8 | -3.78938 | -50.97403 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b8ac7f7-b4c0-3a27-b3a9-2655f64f8065 | -1.73376 | -52.61308 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| eb99a61c-3f1e-3656-b50c-ad37b99b9f47 | -3.70888 | -50.45259 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 8757dad0-7de0-3774-a3c5-2a4f63b73bad | -3.06347 | -54.50956 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 902c8270-99a9-36dd-b0f8-1b7471dfe9f8 | -1.61728 | -53.53136 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 57151c38-010c-325d-9cc7-ac239a477508 | -1.7167 | -52.7841 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc00dba1-de58-3a4e-8cc6-105e7d5b92b4 | -4.05389 | -46.99664 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 44749840-d4d0-317e-a1ba-7b2dd6b38bbd | -4.3005 | -48.21801 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dc51f41d-d99b-3f39-8fea-32deda4fe7ea | -4.42331 | -46.73592 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2e138a6-ce68-3bf2-b883-cc13ed673248 | -1.48754 | -53.81192 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| dac468cc-837d-335b-bfd5-d716cef8df9b | -0.2627 | -51.49851 | 2024-12-04 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbc3eb9a-eafd-31e9-be8c-265aa251ea18 | -4.09496 | -46.95056 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b0f575c-8bad-306f-bcd6-bf016fc27fa2 | -2.85448 | -49.14209 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6790bad9-4f65-3f47-919d-82ddf1a67a35 | -1.67165 | -52.75513 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c5af241e-ff2b-3771-8286-a8852158a291 | -3.81036 | -46.95862 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91dfb3fe-a482-314f-bbd3-5df4ee81c0a0 | -2.96592 | -45.2144 | 2024-12-04 00:54:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| afed355e-c2f4-3b45-97e0-192cc038d8c8 | -4.07044 | -48.3451 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a36174ac-9bb1-336a-b3c0-96c45f5d6516 | -3.05874 | -54.50454 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 90910514-0d8e-345c-bb4b-54a5611c24da | -3.06687 | -54.04534 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6c51f747-19aa-39f3-bc43-b615cdbff7f2 | -3.27287 | -49.76149 | 2024-12-04 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08ddbdf9-d670-3f63-ba49-5a4bf0675f4d | -3.19099 | -51.16989 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ebfa3ed2-38fb-37fa-8b74-629f30a1abb4 | -2.46906 | -53.62909 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4765658-7cde-3fba-a2ed-5f2b302d51d0 | -1.74684 | -52.6343 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| afeb9d46-8d3e-3417-a742-4b4b37159b47 | -4.04597 | -47.00776 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0ae86795-485b-3f8c-8e8c-54b32dbf4252 | -4.05444 | -46.59561 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 2e83ed73-a09b-38ad-af22-d44df4710a7a | -2.67705 | -46.61838 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e6411368-c8d5-34c1-bf82-2fbc5216ac89 | -3.17235 | -44.43262 | 2024-12-04 00:54:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0a0866f4-ae05-3736-abe4-410a69722c0b | -3.84055 | -52.33241 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 39431876-6695-3d7e-b60d-0e967ec4f1b1 | -1.23599 | -51.60663 | 2024-12-04 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ba683d2-391c-3e1e-8915-4e8baf5ee61c | -1.71126 | -46.21844 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd4b6cd8-b63b-3358-a4be-6c77cf597d6d | -3.06246 | -53.27431 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8333c4b7-3236-3e22-9890-3d5d472756ea | -3.95667 | -52.21027 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dce61954-6c43-3bb2-9bda-21759b9ce4a0 | -2.03274 | -45.53558 | 2024-12-04 00:54:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b5960be-b4f1-3baa-975b-d107189ceadd | -3.97608 | -50.51722 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| efed6ed6-cc31-3f0c-a0d5-8b0432feffcd | -3.30165 | -53.67051 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cd160967-b1ee-3c14-9d61-a1aec3b7e25d | -4.18691 | -45.37945 | 2024-12-04 00:54:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b3269c93-f0b7-30fb-bd39-469b31058fee | -1.87806 | -53.30239 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 534a61e2-0cf7-39bf-9d0e-1e3cb9b24a9e | -2.94572 | -51.39357 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5bc4dbc1-123a-320c-ab35-66b577423c33 | -3.25562 | -53.66217 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 46ece6be-3393-3c35-af6b-42f235b5e767 | -3.45197 | -54.09102 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5871a97b-d9c9-3975-9283-97b868e2328b | -4.00021 | -48.3063 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9296afb5-854d-3ddc-b618-f87a6ce2da6a | -2.82364 | -52.1511 | 2024-12-04 00:54:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 55f9854c-a9f8-3434-a462-76e57d56d4dd | -2.93661 | -45.49746 | 2024-12-04 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74ab817e-c23d-37f6-ad59-4d84576e3ac7 | -4.3226 | -48.10781 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2401fc60-2261-3f4c-beb8-d33828dad348 | -1.70663 | -52.7855 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d64afd71-a012-3f0f-9aa6-10c0587e389c | -3.25363 | -50.61918 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1283091a-fb15-3548-8d48-0b679a2ec533 | -3.52107 | -52.16345 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 90586e5a-ed5b-3ea7-831f-5d24a9c4ecba | -2.72922 | -51.82697 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 52670224-17c2-3aac-9d8a-30273c73fedf | -2.60127 | -46.00579 | 2024-12-04 00:54:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 255a541e-5502-31a0-82e8-8c160031e359 | -4.92451 | -47.86854 | 2024-12-04 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de0076c8-6cf4-351c-b7fb-5f46cab30829 | -2.75502 | -45.29028 | 2024-12-04 00:54:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 56afb96e-5c0e-3e30-88b2-5cf331c08735 | -4.04318 | -46.14714 | 2024-12-04 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 782ac86e-34f2-3cd4-bc16-43c0a8193aef | -2.19739 | -45.6722 | 2024-12-04 00:54:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| bec6788f-294f-340c-bd64-5cde47bd16fa | -5.57717 | -45.15604 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| a8ce5b9e-a394-337d-b36f-ceb1214233b5 | -4.24898 | -47.5864 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 78a23a9b-a13e-3bfc-bbab-5e81e5393664 | -3.05172 | -54.51109 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8607d0d2-2ed7-3cff-aaa9-45a02372cfe4 | -3.06893 | -54.06019 | 2024-12-04 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e8ea854a-66f0-3e31-ba05-8158d279be16 | -3.18733 | -54.51365 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 467ce00e-504e-3e35-a916-f8cef756204b | -3.73012 | -50.20551 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a6d62c3-59dc-3bf4-b6b6-2ecdec9fae15 | -5.58739 | -45.15448 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a4e3ebde-80cc-35f4-9d0e-2ce677e9f434 | -3.60906 | -50.79528 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c33b8af4-65c7-3a27-baf6-3d82f09537f5 | -3.11263 | -50.1987 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fcb0caa-f4fb-394d-891a-88609f508e4b | -2.97832 | -52.97531 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c94d068d-8683-3dec-aaab-c6c9c53de81c | -3.95515 | -52.19898 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 56e5516c-110a-39c1-91f8-189bb11db97e | -4.61649 | -48.03846 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2c89576-18ae-3938-8b37-ddf8e6276724 | -3.66042 | -47.13337 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 5ffd1427-7987-373a-bf81-e0c93a4fa0ef | -2.83052 | -49.82721 | 2024-12-04 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28ac3540-9aa2-399f-93f2-af69ae15e1cf | -3.47424 | -45.47044 | 2024-12-04 00:54:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f459e05f-350b-3633-9d07-ed36aee2057b | -3.24421 | -46.28471 | 2024-12-04 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a70eda70-dc53-3e03-a40f-804cbcafc237 | -2.6907 | -51.85933 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8dc2e887-3683-36b7-b09f-582bffe5c2b9 | -3.96435 | -50.56669 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7d85b3d-9c61-390e-9d83-dc5c0591f695 | -4.05592 | -46.60611 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 12d06ae9-af8b-36ba-a6a7-0348695995b7 | -2.82734 | -53.05835 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 10ce44ff-d826-3485-945e-94c9e220e17f | -3.44886 | -45.85706 | 2024-12-04 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f301138a-78fc-3ecd-8118-e210a5d3b1b5 | -3.21907 | -53.72474 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fd225247-b9ed-3589-acfc-5e79acc4d8e6 | -4.31239 | -48.10008 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README13.md)
