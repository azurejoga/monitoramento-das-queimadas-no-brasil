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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7cfa7f9-ff22-37b4-aea7-d7f4b290f05d | -5.42756 | -38.56858 | 2024-12-19 11:46:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f961f894-ca9e-30e9-9879-d4bca9092f09 | -6.31259 | -37.56765 | 2024-12-19 11:46:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 40040f96-fd90-328c-a530-4446dd4d62ce | -6.30338 | -37.61034 | 2024-12-19 11:46:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 18.7 |
| ff5330eb-1c7e-3535-aa2f-301fa42d256f | -6.66377 | -37.80427 | 2024-12-19 11:46:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 16f377fb-1bb4-38a3-b835-0db521bca59b | -7.86895 | -37.50225 | 2024-12-19 11:46:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 50bcf7e3-cf14-3d5b-8607-7dbe3c2e610a | -5.49444 | -36.45886 | 2024-12-19 11:46:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e33ad021-6fd7-3f2b-a601-e14b96f3fce3 | -6.29492 | -37.61555 | 2024-12-19 11:46:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 36.0 |
| c2aa4b1a-4f0e-3fcf-b43b-4a32f459cd22 | -6.29677 | -37.60314 | 2024-12-19 11:46:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4358253b-2e55-341e-9e39-90a80d82baf3 | -6.50207 | -35.20876 | 2024-12-19 11:46:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| b907d1b0-fd9d-3031-b3d5-35f75b9d4b71 | -6.31103 | -37.56104 | 2024-12-19 11:46:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2ce91c97-8cfe-3f40-bd4d-9afca76e2f74 | -5.42871 | -38.56281 | 2024-12-19 11:46:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 85c41f45-3ce7-3502-9e24-d385428040c5 | -6.92679 | -35.77172 | 2024-12-19 11:46:00 | TERRA_M-M | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 11.1 |
| dba5d43c-8d11-3534-a855-efb0ae8c67fd | -5.79484 | -38.72644 | 2024-12-19 11:46:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 51b46bd1-9569-311a-b823-5b8ef9b0ca93 | -6.30227 | -37.56612 | 2024-12-19 11:46:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ce024e28-d12d-3f35-a9c1-e0f66cffaf92 | -12.04663 | -45.08715 | 2024-12-19 11:49:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| db8b9c74-79be-36cf-b16e-395730b0c4f9 | -15.74652 | -45.9371 | 2024-12-19 11:49:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 6e65f502-9cd3-38b7-a8aa-e010076f909a | -15.73553 | -45.94078 | 2024-12-19 11:49:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 07dce40d-f8d9-383b-aba4-4bfefeca79f8 | -15.40619 | -43.78921 | 2024-12-19 11:49:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 86a5a587-16a8-30e2-af6c-49a99f02e174 | -15.83 | -43.46 | 2024-12-19 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07396eaf-0c29-3e76-b9b3-2c7fbf9c53d2 | -15.73 | -45.95 | 2024-12-19 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| febee98a-77f1-3884-861d-b9722122b090 | -6.9233 | -42.838 | 2024-12-19 12:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 611e12d4-3228-3904-b2d8-a5c6b2342ee3 | -6.9233 | -42.838 | 2024-12-19 12:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 512bb38a-ea0d-397b-a998-d2020bfb2da0 | -6.9233 | -42.838 | 2024-12-19 12:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 315e170c-e7b1-3d19-90ab-a9f98713db6a | -6.9233 | -42.838 | 2024-12-19 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 420178bf-6a9f-3397-b2db-b8296bb02bfd | -3.0686 | -42.1351 | 2024-12-19 13:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3871eda3-7a93-3c50-a202-beca9535bf5c | -6.686 | -38.8575 | 2024-12-19 13:00:00 | GOES-16 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 108.7 |
| fb7d5ff6-663c-3fcb-89a2-20b38fb5daea | -6.9233 | -42.838 | 2024-12-19 13:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 72b268d6-29b5-38b7-b139-77cbe7618e42 | -6.9233 | -42.838 | 2024-12-19 13:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 64f9a74e-1dbf-3035-9db8-c4e8f5295cf8 | -6.686 | -38.8575 | 2024-12-19 13:10:00 | GOES-16 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 94.8 |
| ed3d4c6c-f279-3d7e-a3c7-aa09c4e555ac | -6.686 | -38.8575 | 2024-12-19 13:20:00 | GOES-16 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 39459222-b44b-39d4-bc9e-6897d6750482 | -3.0131 | -42.0188 | 2024-12-19 13:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 370099d2-1838-3b9e-9994-63cf3150a003 | -3.8044 | -44.0613 | 2024-12-19 13:50:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c8286d76-aa55-3747-ab90-ea555e39c379 | -4.9024 | -42.08 | 2024-12-19 14:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 76ed8032-ec02-39dd-8ca4-36954837a8fc | -6.9233 | -42.838 | 2024-12-19 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| c4404ea2-8dff-369c-acd2-fb771eda623e | -4.9022 | -42.1038 | 2024-12-19 14:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| c47c4810-0df4-315a-a666-811d129234a6 | -6.9424 | -42.8126 | 2024-12-19 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| d88d28c0-0d2f-336f-8e36-5dd63360634b | -6.9613 | -42.8108 | 2024-12-19 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 98942cd7-16f8-3100-9af4-3d6f3200f15f | -6.9422 | -42.8362 | 2024-12-19 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 2037a84f-eae2-34db-9635-8af0a6b7f04c | -6.9613 | -42.8108 | 2024-12-19 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| ac94682d-b77d-33cb-94cc-cd71bbc515af | -6.9233 | -42.838 | 2024-12-19 14:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 2fb45822-313f-3eb1-86d7-abe4b81c986d | -6.9422 | -42.8362 | 2024-12-19 14:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| c522d2bb-eb0e-34db-a7dc-0e1eadd40a79 | -4.718 | -39.3627 | 2024-12-19 14:10:00 | GOES-16 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 148.4 |
| 0706459d-2be8-3f6a-9895-08e66430a040 | -4.7178 | -39.3877 | 2024-12-19 14:10:00 | GOES-16 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 950b96e8-e640-3712-a876-5126d6dbd904 | -3.7859 | -44.0392 | 2024-12-19 14:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 71779f6d-095b-30bb-b3d9-af78ce691276 | -6.9233 | -42.838 | 2024-12-19 14:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 3c419b9c-c953-36fe-9e3e-6cbb3aef1423 | -6.9422 | -42.8362 | 2024-12-19 14:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| c60be7a2-08e3-3985-aec8-4b337c26348b | -3.4645 | -41.5206 | 2024-12-19 14:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 189cdb73-82aa-339c-a8b0-86e6d1e82aca | -3.0122 | -42.2086 | 2024-12-19 14:20:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| ca196a4f-44a1-34b6-acea-62d76227675e | -3.0503 | -42.041 | 2024-12-19 14:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 34e764b0-8e71-308c-a67e-bfb01d265fbf | -3.4645 | -41.5206 | 2024-12-19 14:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 54d3b963-34ca-3371-9767-1cc04b788b4d | -15.1235 | -39.7465 | 2024-12-19 14:40:00 | GOES-16 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 63bdefbd-ce9a-387d-bca9-1883bf7a6c36 | -2.9776 | -41.6389 | 2024-12-19 14:40:00 | GOES-16 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |


