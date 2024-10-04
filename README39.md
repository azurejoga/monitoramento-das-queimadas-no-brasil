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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd353fd2-f653-3531-9b5c-12bb4579ecfc | -9.8539 | -46.7704 | 2024-10-04 01:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| df09b232-3f2d-32fa-9ffb-0ef3332d280e | -9.8542 | -46.7481 | 2024-10-04 01:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a268ab92-39c7-3f12-b088-1abcc772b494 | -11.0727 | -46.5093 | 2024-10-04 01:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 7e9251b5-68e3-3809-9bd3-a643e42907b8 | -11.6181 | -64.9818 | 2024-10-04 01:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 63d9d735-d046-3d28-994a-4a3b3c90be0a | -11.6369 | -64.981 | 2024-10-04 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ec3261fd-74cb-38bd-83c2-4de40a4c482a | -11.8052 | -56.6024 | 2024-10-04 01:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f7ee3ec5-f7b7-318e-9569-7bc590d8051f | -11.8242 | -56.6009 | 2024-10-04 01:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| e61d866f-f2a6-384a-b43c-f71e15fd005a | -11.8244 | -56.5808 | 2024-10-04 01:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4dcf509a-4692-3e92-9de5-79de1c0c6272 | -11.9147 | -56.9539 | 2024-10-04 01:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b8c3cd39-c744-3237-9898-b9bca98e04c5 | -12.4037 | -63.0201 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| eb06287b-8d5e-3316-b96f-0f406e87eb28 | -12.4038 | -63.0009 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 09d6d568-e8b6-39fd-bb65-e5b8f7310cf2 | -12.4225 | -63.019 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 401c78af-e8ad-390a-99d3-2fb979c5bebb | -12.4227 | -62.9999 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| b7005416-559c-33a2-a554-a923c5e71edb | -12.4414 | -63.018 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ad21620f-aa1d-3b4d-bec9-448df957ade2 | -12.4416 | -62.9988 | 2024-10-04 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b1058b80-2367-34ab-878e-a8d628f7b1e7 | -12.5898 | -53.1359 | 2024-10-04 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 08fee11b-b7b8-354d-ab1b-73fac8b4828c | -12.5901 | -53.115 | 2024-10-04 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 7ecc9766-02e5-3960-ae0f-2eff3fee7da8 | -12.6092 | -53.1129 | 2024-10-04 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d4ca5094-74b5-328f-b194-06e5a37e68b6 | -12.6295 | -63.1225 | 2024-10-04 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8363e436-fd59-3803-9528-1d1485914f06 | -12.6296 | -63.1033 | 2024-10-04 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| fa5adf6f-0242-38ff-a150-602dc48342c9 | -12.6484 | -63.1214 | 2024-10-04 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| efb4bd34-fb98-303c-8297-e49aaf8f1c0b | -12.6486 | -63.1022 | 2024-10-04 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d67ec697-7852-3d93-83d0-e752874c0596 | -12.7256 | -62.925 | 2024-10-04 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| aeaf1951-8063-3f3d-80cf-6f732d92ae0c | -12.9831 | -51.129 | 2024-10-04 01:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 25ec4ed3-6ba6-3f6b-b987-175f32e4a2fb | -13.1166 | -51.1551 | 2024-10-04 01:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a9925407-6544-3959-88ea-a4bb209e28bf | -14.004 | -44.0201 | 2024-10-04 01:46:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1e961d9e-4d36-3f90-be8c-2f2c1ec8d296 | -14.7939 | -48.0275 | 2024-10-04 01:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 61f0db98-ae8f-36e9-86dc-72ba1de9a99a | -16.0933 | -50.2763 | 2024-10-04 01:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9cf5b420-fc96-32f6-83a8-148c4db7c8d1 | -16.1094 | -50.4489 | 2024-10-04 01:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 47c7d0f2-1aba-3f5c-b678-d7d2564de2b9 | -16.4148 | -57.4028 | 2024-10-04 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 92d6ef17-1569-3e3b-8a9a-c15be9be7d8c | -16.4151 | -57.3823 | 2024-10-04 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| af85ea20-95ae-3b7e-805a-dd3b516c12c5 | -16.4554 | -57.2962 | 2024-10-04 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 28e534c1-edc6-3627-bcbe-ff5a1611784a | -16.573 | -57.2624 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| af01ddbe-a9ce-30ec-8983-79a397c8cabb | -16.5733 | -57.2419 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 79664814-597d-37f7-86eb-0830c83b100b | -16.5736 | -57.2215 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| d151e529-54c9-3365-9265-8c3f886526ee | -16.5783 | -58.198 | 2024-10-04 01:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 21278124-74b0-3e24-bde9-4bfffb9c3565 | -16.5925 | -57.2602 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 4990cb68-3301-3d20-a6ec-bdb04477441a | -16.5928 | -57.2397 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| edce034c-d9a9-36fe-be59-3c3e2a9531c9 | -16.5935 | -57.1988 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| acedf5c9-b9a5-3226-a4a8-3c3a7a8147aa | -16.5938 | -57.1783 | 2024-10-04 01:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 61566a11-d10d-319b-aa8d-d5f66bec684b | -16.6133 | -57.176 | 2024-10-04 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 13a699bb-ad54-3b4d-a566-cacd617ca34d | -16.7606 | -57.7512 | 2024-10-04 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 8264b6a3-67ed-3b25-9b69-0ccd468de62c | -16.613 | -57.1965 | 2024-10-04 01:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| e921833e-26bb-324c-9511-765fc0f2ec76 | -16.779 | -57.8306 | 2024-10-04 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 2d16c82b-2261-373d-bc00-bfe0b313b2c0 | -16.7859 | -57.3811 | 2024-10-04 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 6d05490a-b88b-33a4-b40f-4ea6e9bd96ec | -16.7985 | -57.8284 | 2024-10-04 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 69ef246b-2bd0-357a-b378-d5e77618bf08 | -16.8055 | -57.3788 | 2024-10-04 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 939e3398-1573-36cb-9366-98ed6e640e7b | -16.843 | -57.4767 | 2024-10-04 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 0c062bbf-a2df-3b66-8d5b-13522cc21941 | -16.9091 | -55.8222 | 2024-10-04 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 50b7c337-707d-3385-be64-a6ceacecad71 | -16.9087 | -55.843 | 2024-10-04 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 6e07fc11-304a-3bf3-b9f3-05e6c3423f0e | -16.9283 | -55.8405 | 2024-10-04 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 927cffe8-1326-3199-bb59-5451d649a6e8 | -16.9287 | -55.8197 | 2024-10-04 01:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| dfa8a1f9-2ef4-3589-957c-19b9ee99abd7 | -17.3643 | -42.6284 | 2024-10-04 01:46:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2fe0f321-ea5f-3975-b289-d1769cd87461 | -17.3844 | -42.6235 | 2024-10-04 01:46:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 142c5969-411f-361c-a100-06fce7309081 | -17.3851 | -42.5986 | 2024-10-04 01:46:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 831a55f4-881b-38b6-9240-080cf7ac3ccf | -17.5344 | -46.7239 | 2024-10-04 01:46:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2b00c086-5889-3699-9cf3-1bb72bb2570b | -17.1974 | -57.3536 | 2024-10-04 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 6184d53b-36fe-33b7-aa47-ed2d7e679f7c | -18.8413 | -42.8985 | 2024-10-04 01:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| d2022ad9-e3f2-308c-ad88-c6a2f5c6900f | -18.8609 | -42.9182 | 2024-10-04 01:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| ff8b2c87-77bc-38e9-8dcd-041d141e256b | -18.8617 | -42.8932 | 2024-10-04 01:46:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.1 |
| 42a83d97-9331-34b5-953a-e36ebd4063ef | -18.8613 | -43.5837 | 2024-10-04 01:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 1302197b-a630-3d0b-9f6e-e7172ec498c0 | -19.3159 | -42.5976 | 2024-10-04 01:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 152.5 |
| 592e7c99-9b22-3504-97ea-0481aec426b6 | -19.3167 | -42.5724 | 2024-10-04 01:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.1 |
| 5bf0d729-a8cb-3467-bb35-aa2e718c034d | -19.3363 | -42.592 | 2024-10-04 01:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| 52083ac1-442c-3c18-a75c-5f7b77fc33eb | -19.3371 | -42.5668 | 2024-10-04 01:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| b0777b69-088a-33fc-8925-941e49b350aa | -19.8516 | -42.3738 | 2024-10-04 01:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.0 |
| ddf1ebf9-6056-31ea-a7e3-ac2c920af3db | -19.8524 | -42.3484 | 2024-10-04 01:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 15db8cc9-ff50-3d5b-a80b-b1e56818b33c | -19.8721 | -42.368 | 2024-10-04 01:46:55 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| 4574f1db-8f2e-3e8a-bd13-dc061ac69ff8 | -19.873 | -42.3425 | 2024-10-04 01:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| b7fd1e4b-5292-398a-b47a-01f261058ff8 | -19.9901 | -48.7144 | 2024-10-04 01:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4dfda082-513c-38a4-ac8a-8021e11b5f5b | -19.9907 | -48.6913 | 2024-10-04 01:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 126.0 |
| d621b156-ce54-3536-8034-c1c6b1623499 | -20.0104 | -48.71 | 2024-10-04 01:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8b33f3ca-1168-300b-b681-7ff775fce6e3 | -20.0111 | -48.6869 | 2024-10-04 01:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 179.1 |
| f4792813-b27c-3dfc-b2f2-3cc13266de01 | -21.7981 | -48.3926 | 2024-10-04 01:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 66b8612c-931e-3e94-9d1b-f9e0a8be4e0f | -21.7988 | -48.3691 | 2024-10-04 01:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 183.4 |
| c6d2e0f1-1a7e-3388-8bfe-d7353232270b | -21.8175 | -48.4346 | 2024-10-04 01:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| df4b6536-1229-363a-b125-506e6cca67de | -21.8189 | -48.3876 | 2024-10-04 01:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 109.5 |
| fa58a47d-6dd7-31e2-b889-72540379a4ab | -21.8196 | -48.3641 | 2024-10-04 01:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 194c6d4e-b491-30f9-a26f-7df4fbee7a3c | -21.8376 | -48.4531 | 2024-10-04 01:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5d1b21f0-4344-3ab7-8b49-815bf3f563e8 | -21.8383 | -48.4296 | 2024-10-04 01:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5c828c45-2185-3210-acd4-bf7d8fc50085 | -21.8397 | -48.3826 | 2024-10-04 01:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 16fc253c-e05d-3b77-b655-209994dd91c6 | -22.0846 | -48.4865 | 2024-10-04 01:47:07 | GOES-16 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 73ad6664-2759-374a-8aa3-dc6045609f89 | -3.2349 | -50.3695 | 2024-10-04 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 49990d7f-8873-378e-ac86-a2542b48fab3 | -3.4915 | -50.8004 | 2024-10-04 01:55:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2a8524af-53b8-387a-8994-8e2a1a1f74a2 | -4.0949 | -48.4894 | 2024-10-04 01:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a23442a9-f4e9-3d09-9766-f115715260dc | -4.5375 | -43.304 | 2024-10-04 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 828207de-8f4c-38fb-b3c1-8de52f44b993 | -5.8216 | -44.1196 | 2024-10-04 01:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 449ff237-0b5e-36b9-bf90-034718ee8bd5 | -7.4995 | -34.8464 | 2024-10-04 01:55:47 | GOES-16 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| 4ece6e50-ce84-34aa-8646-acccd2827cd7 | -7.8539 | -45.3611 | 2024-10-04 01:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 67ebd3c4-d473-30ca-a1fa-2991fcab9d7f | -7.8164 | -50.543 | 2024-10-04 01:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e68d17a4-cc6b-3e1b-b44b-f0e534c3cd41 | -7.8166 | -50.5219 | 2024-10-04 01:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 76fae794-d49f-3f4b-9989-91a39b456378 | -7.8351 | -50.5416 | 2024-10-04 01:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c4216ea0-0417-347a-a5c5-0952ad6b93fc | -7.8353 | -50.5204 | 2024-10-04 01:55:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6c12a901-d15b-319c-9289-8ef97cab180a | -8.6448 | -50.0518 | 2024-10-04 01:55:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d6098633-9456-3d6d-8fcc-973eca371e74 | -9.1041 | -50.902 | 2024-10-04 01:55:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0db227e0-ccb2-3b9e-9e45-409814a35c3e | -9.0162 | -67.3904 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7641204c-691a-32c7-86a9-13c0eeab50de | -9.0163 | -67.3719 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f6b7ec5d-4c8a-30f2-a8af-0a2614e3e296 | -9.0347 | -67.39 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 450b5786-f5b8-3dfd-9a4b-e1d495aea40c | -9.0348 | -67.3714 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 69e62d1a-bb55-3113-8287-123467adfafb | -9.0898 | -67.5183 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |


[Clique aqui para ver as próximas entradas](README40.md)
