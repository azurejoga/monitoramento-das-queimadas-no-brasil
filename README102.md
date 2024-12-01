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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7fa2e67-16da-3aa6-a765-a1a3b07987d1 | -4.88331 | -41.33787 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| ed1b6ac8-aac7-3b2f-8f85-2f675515d044 | -3.85416 | -46.54112 | 2024-12-01 12:55:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bf781afc-5e5f-3448-b10b-aa0175ad0ad9 | -2.41108 | -56.42447 | 2024-12-01 12:55:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| aca580eb-7a9b-38a5-bc49-22e6f9e87a76 | -2.90459 | -42.13728 | 2024-12-01 12:55:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 57c4c3ec-ef11-383e-8d6d-47f90f130448 | -4.69669 | -42.38756 | 2024-12-01 12:55:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 7f4113fb-af47-303c-a12a-b6339aea03ad | -3.26238 | -53.63897 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ba7a7198-23cd-3119-9b81-286fa28862ac | -2.59458 | -53.98726 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8edd393f-84e1-3c4d-ab18-8045de5ec875 | 2.81343 | -51.07431 | 2024-12-01 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 34ebed9f-1a23-3e2b-950d-648086529874 | -2.87203 | -42.05238 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e23f85ba-e87c-33f1-a179-edc1ce63827d | -4.25989 | -50.83996 | 2024-12-01 12:55:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 12b2b75b-0d2a-3b34-86cc-05b8ed038adb | -3.17276 | -42.19824 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 8ad97ef7-ec32-3291-a29b-51cb5afded26 | -2.66354 | -48.7876 | 2024-12-01 12:55:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8ea5fdb9-2b64-31fe-bad1-9152fee0925b | -2.87575 | -42.02563 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4579a44e-d549-3ce8-9815-62c30762b5a3 | -2.90109 | -44.01357 | 2024-12-01 12:55:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 61429f63-19f1-3efe-84ce-99069c7bebe3 | -4.89665 | -41.30996 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 37.8 |
| a3745db5-f994-3a78-bd76-0d684c49c6c6 | -1.37793 | -47.19918 | 2024-12-01 12:55:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e9dc5aa3-2011-3ce0-89ee-35b8af2638f5 | -1.64774 | -52.4881 | 2024-12-01 12:55:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 370ab899-afb9-3a4b-8356-63f8149f8b37 | -4.43552 | -42.89161 | 2024-12-01 12:55:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 8f41b212-381e-31a4-bd55-7bc93de8d4cd | -3.53482 | -42.10792 | 2024-12-01 12:55:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 538bad9d-ca86-3940-a0a5-3377d33598b0 | -2.11891 | -47.10346 | 2024-12-01 12:55:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 174.7 |
| e962af13-8d29-35a6-b28a-b69b5d242f47 | -3.21188 | -54.17327 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e4f48812-b4a2-33a3-8851-16ef71838666 | 1.19247 | -50.88533 | 2024-12-01 12:55:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 29b03c4a-b53b-3de6-b8cd-27c1bc9582bc | -2.44068 | -48.28377 | 2024-12-01 12:55:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0f426084-bcc6-36cd-980c-bae4c18bda29 | -2.92089 | -54.12553 | 2024-12-01 12:55:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 651ab885-a474-397b-8bf4-af70dbb1aa77 | -3.53421 | -42.10212 | 2024-12-01 12:55:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 1e5f719c-fa40-3f30-8cf5-3e28f14690ed | -1.82242 | -50.90273 | 2024-12-01 12:55:00 | TERRA_M-T | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5f9e4391-d63a-3638-8446-536b3db3b30c | 1.18333 | -50.88662 | 2024-12-01 12:55:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 23.5 |
| e0c15633-d538-345d-8789-c1fc246bec0e | -2.83787 | -54.10098 | 2024-12-01 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 33fe3e3e-20da-3345-b791-ebd69a6507d5 | -3.95202 | -43.2005 | 2024-12-01 12:55:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 16588e21-e180-3035-8e6f-e4db5daadb74 | -2.89039 | -42.02758 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 1e4a314a-fc8d-3762-9cca-cca33858b06a | 3.55332 | -51.40208 | 2024-12-01 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cd76ec8a-046a-375b-9fcd-9206aacaf122 | 2.81483 | -51.08434 | 2024-12-01 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eaf4e1e9-e26c-3e4e-877a-6ee428e94f5a | -2.89635 | -44.02615 | 2024-12-01 12:55:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| b319de19-b2a8-30af-a407-6284be76d486 | -3.04891 | -49.37693 | 2024-12-01 12:55:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9ef0efc5-c1b5-3a65-a18d-ecb739bd374e | -4.69754 | -42.39466 | 2024-12-01 12:55:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 09255c7e-2512-33d9-a8e0-15ce68f6c42d | -2.99816 | -42.02693 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cd8c4014-05f8-37a1-afd4-d30d9f7aede1 | -2.63273 | -54.20081 | 2024-12-01 12:55:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 66eb2ff5-9d42-37bb-94ae-e8179ef5796c | -1.56642 | -48.65342 | 2024-12-01 12:55:00 | TERRA_M-T | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c43a8d1b-eb9f-3bf1-b72d-f47da51ed79a | -2.12043 | -47.09265 | 2024-12-01 12:55:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6bc578b4-bd72-30fa-b363-bd7eaf565585 | -1.72019 | -52.62458 | 2024-12-01 12:55:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 53ddd43b-efa9-34c7-80b7-a7b0e98962a7 | -3.31129 | -53.86353 | 2024-12-01 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 07aec4f2-9b92-30ca-af36-e802b03a9a54 | -0.841 | -51.75765 | 2024-12-01 12:55:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 31b03743-59ee-34d7-9a34-4bc9d137f26b | -2.99735 | -42.02169 | 2024-12-01 12:55:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d0834272-beb4-3f66-b3d6-fa9ac4633a3a | -4.10785 | -48.88045 | 2024-12-01 12:55:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fdd82116-9636-35c1-acff-f53ed8df0587 | -4.0373 | -46.92021 | 2024-12-01 12:55:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 66658914-a01a-3121-9a31-5cc3db55a906 | -4.54345 | -43.29243 | 2024-12-01 12:55:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 19b79c34-06dd-3d0e-b4ea-69b278fa446a | -1.94317 | -47.89408 | 2024-12-01 12:55:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a6fd70a0-956b-36bc-bffb-5ec084eac6aa | -2.66222 | -48.79671 | 2024-12-01 12:55:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f700e40-43ce-3f73-8eed-8b4f303eca6a | -3.97975 | -46.74988 | 2024-12-01 12:55:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 03aab855-ed57-334d-8510-93d4899d553e | -2.00252 | -48.82838 | 2024-12-01 12:55:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c45fd856-5bf0-3481-9f2e-2e2fa4337f15 | -3.02405 | -42.27161 | 2024-12-01 12:55:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 95737756-0749-33fe-adbe-e86319a2c306 | -4.56254 | -45.72338 | 2024-12-01 12:55:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d6cd61f9-7d82-373a-b569-a4466fe0ce28 | -12.77537 | -45.55291 | 2024-12-01 12:57:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d7b719b5-aee8-396f-b15b-6bd2e0bdb308 | -8.38865 | -44.14115 | 2024-12-01 12:57:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 191ca642-37eb-35fb-877c-c65fa4c6053a | -11.68967 | -54.32572 | 2024-12-01 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f6abdb27-f837-3ca0-939e-5dfdc5ef8227 | -12.12186 | -54.16589 | 2024-12-01 12:57:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1772270d-1b76-3aea-9a2a-c558b7d17ed7 | -12.25016 | -52.68397 | 2024-12-01 12:57:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 4fe032f6-4eaf-31eb-8ea2-3f604bf36796 | -11.16516 | -44.74293 | 2024-12-01 12:57:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| f44b8486-e80c-387d-987a-bc17f88e9ffe | -9.17272 | -47.62906 | 2024-12-01 12:57:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c10fcb6-a68b-3945-a899-758ececec30e | -7.94374 | -48.25531 | 2024-12-01 12:57:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 849ad707-12f0-3bf3-8e0b-0e8f21783ef3 | -12.25148 | -52.6749 | 2024-12-01 12:57:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 306e87a2-ff25-3d7e-96b1-2dce32d85ad2 | -10.66274 | -44.4876 | 2024-12-01 12:57:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 625ea255-f0da-3720-b9aa-9b3d70b9ffbe | -10.65995 | -44.5106 | 2024-12-01 12:57:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| a84d9e26-a6c2-344b-a501-a363e84a78e8 | -11.18231 | -45.25012 | 2024-12-01 12:57:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a1e6bd3a-6908-3b60-bb18-246f77c24137 | -11.78705 | -54.23059 | 2024-12-01 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 59ca4056-d82e-33bb-8be9-1074f988f739 | -11.72857 | -54.86547 | 2024-12-01 12:57:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1d317eaa-56d6-3695-9242-43e6da01254e | -12.46963 | -51.93197 | 2024-12-01 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6246355b-5884-3102-beae-7fc73bccb1c5 | -11.08321 | -44.02043 | 2024-12-01 12:57:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c651589b-7b6e-32e8-83c2-ae7dd34c3ced | -13.46285 | -52.08107 | 2024-12-01 12:57:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 405c3623-f479-3887-928b-1ddaf6541f16 | -9.08215 | -46.67844 | 2024-12-01 12:57:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2f26a470-56df-3b25-aeb8-0d6d7ba33049 | -8.38326 | -44.14605 | 2024-12-01 12:57:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 15f6c918-b21a-3ad7-81ac-81ca9a8300ac | -19.93792 | -48.6575 | 2024-12-01 12:59:00 | TERRA_M-T | PIRAJUBA | MINAS GERAIS | Brasil | 3150703 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 534d84ce-965e-39c3-b51a-156ba57a70aa | -21.369 | -47.24114 | 2024-12-01 12:59:00 | TERRA_M-T | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 67a7ab95-d05b-35cc-94cc-af2a5d21a8ba | -4.8899 | -41.3143 | 2024-12-01 13:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 5e29dfdf-0abf-3147-86e1-63b7820ea7b7 | -1.663 | -52.4131 | 2024-12-01 13:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7136d36f-264c-3589-9f27-b48ae0825d74 | -4.5562 | -43.3028 | 2024-12-01 13:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d034f6c2-f15f-3f8b-a951-bfd7b8600d7b | -4.8709 | -41.3398 | 2024-12-01 13:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 73cfe75b-5c1b-3259-9f5d-2facc2a5ebee | -4.8899 | -41.3143 | 2024-12-01 13:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 072396a7-269a-3dcc-8607-5ef2f28bed39 | -4.8711 | -41.3157 | 2024-12-01 13:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| cb28cfce-80a5-3650-b1cb-8dbb55dc256f | -4.8709 | -41.3398 | 2024-12-01 13:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 5a740d43-8750-3aae-bb6b-e26fde333fe3 | -4.9087 | -41.313 | 2024-12-01 13:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 6c042104-8ddc-3705-b691-1dafb9feca12 | 1.4918 | -55.9443 | 2024-12-01 13:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 891b3caf-f838-30cf-bfcb-415f9268949c | -3.913 | -41.6167 | 2024-12-01 13:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 7386667f-9848-3785-ae0e-4f0bbabdf909 | -4.9087 | -41.313 | 2024-12-01 13:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 80adb2ba-48e5-31b8-a5ab-6b92efef6c90 | -4.5562 | -43.3028 | 2024-12-01 13:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5e208669-f8a9-3dc9-816d-fb5bd1f20b5a | -4.8709 | -41.3398 | 2024-12-01 13:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 57bec791-6d02-3d82-a3f1-b486562c6afe | -4.8899 | -41.3143 | 2024-12-01 13:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 4bee8518-f779-314e-90c5-b4fb1e6d9068 | -4.8899 | -41.3143 | 2024-12-01 13:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 224.0 |
| a9d6036f-3475-367b-9ecc-3c6f86870f6a | -4.8711 | -41.3157 | 2024-12-01 13:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 81030b48-5771-3aac-8634-a15796153de6 | -2.7217 | -49.372 | 2024-12-01 13:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5c6a953b-9d05-39f2-957f-3384b84177e1 | -4.5375 | -43.304 | 2024-12-01 13:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 638d36f2-e303-3b0a-9556-8b41f3832565 | -4.8901 | -41.2902 | 2024-12-01 13:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| b9ab9bc2-df01-3279-af40-6234784cc4a7 | -2.9572 | -41.9974 | 2024-12-01 13:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 3ca105ac-bb68-3fad-b704-c5b44db3d6d5 | -10.6674 | -44.4835 | 2024-12-01 14:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 14e7167e-67be-37c5-8cd3-25c0c4697c11 | -4.9087 | -41.313 | 2024-12-01 14:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| 2c3b08c1-a6d1-33a9-90a5-acb24dacf814 | -1.6444 | -52.4951 | 2024-12-01 14:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0abbd862-84c9-3b84-8563-0a58a14507cc | -4.8899 | -41.3143 | 2024-12-01 14:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 198.5 |
| 5e799f55-2e12-3f19-920e-d4d88e9f58a4 | -1.6261 | -52.475 | 2024-12-01 14:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9c57bf3f-7949-3076-a56d-d3ba66290922 | -4.5562 | -43.3028 | 2024-12-01 14:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 16b588f3-478a-3e53-8dfd-98012360ce23 | -10.6483 | -44.4861 | 2024-12-01 14:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |


[Clique aqui para ver as próximas entradas](README103.md)
