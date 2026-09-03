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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43ac3fdb-17d5-3589-bd30-7b05c1652b5a | -14.95194 | -48.08717 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73022121-bc23-349d-9ed3-e025b38f9b7c | -16.74462 | -47.04248 | 2026-09-03 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa7353cd-3550-3cc1-99de-5e3fb03a9b12 | -11.28469 | -45.17322 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6cfd33e-4c06-3766-8d17-af65684a5e31 | -15.89089 | -47.6828 | 2026-09-03 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb250891-1b3b-3fea-9be4-29d2ca9aeb51 | -12.15227 | -46.66397 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4292cda4-30a6-3ddb-b174-7344e93308ce | -11.31959 | -50.53184 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bfb61b56-42a0-30cf-b3f1-ef123db408c0 | -10.49236 | -48.64579 | 2026-09-03 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5589e500-24fb-342b-adfc-5f135a8ffac9 | -11.6941 | -46.73483 | 2026-09-03 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e240087c-ac4c-3872-b674-fa96133e0d7f | -8.46718 | -54.64798 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 35d6dfc5-b3ae-3cdf-8918-2a789a1d60e8 | -10.24707 | -47.75995 | 2026-09-03 04:40:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3246254-0bb2-340e-94ef-cb43c3187461 | -9.70259 | -57.89053 | 2026-09-03 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96168d8a-09d5-3f1e-b784-baf4ce900571 | -13.58834 | -47.87818 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d4dfc5e-e9e2-3c0f-84e4-c7b2f4d46658 | -8.4464 | -54.74597 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 485d0de7-b7dd-3c42-83e4-c1d174e2dbac | -16.40832 | -48.90407 | 2026-09-03 04:40:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e0c433f-5727-34e6-a783-8d18f64cbddd | -9.60694 | -48.56142 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14b4c3dc-3785-3b3d-99b5-f7029c5f2d72 | -11.30045 | -45.13953 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1be3fa74-027a-3594-919d-4e0055a8d204 | -11.32029 | -50.52767 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c5982fb9-0576-311e-97f8-907bdabe0595 | -14.61 | -48.87432 | 2026-09-03 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b17e8fb7-135d-3b56-a925-e4cd9082c086 | -11.29697 | -45.13896 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7c10453-8153-3fc6-842a-e4619e75e1c5 | -12.08721 | -47.06006 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea2e893c-89b9-3c91-bf16-de4d47b7a323 | -10.24374 | -47.75939 | 2026-09-03 04:40:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07245897-7944-302d-89e7-3a4e8bf19ecc | -8.45753 | -54.68554 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04eacc60-f547-31e1-a078-d9511eadb149 | -13.58778 | -47.88173 | 2026-09-03 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8237e7d-5816-3e62-a6fe-f96559d430ba | -14.04947 | -48.40305 | 2026-09-03 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 450500c9-07bc-32d4-b4d7-3ae08d3625f3 | -8.45573 | -54.68443 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a795c6b5-e484-3bd8-a594-cb7bf25d24c2 | -12.09332 | -47.06469 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 812c14a8-78cc-3041-b7ae-e0654b0b7780 | -15.33311 | -47.04485 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6b5e9cc-c4b6-3555-b800-8b8458f61715 | -15.02756 | -46.8527 | 2026-09-03 04:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e101090-d4bc-3ee8-bdb8-ef24b21a5212 | -13.88325 | -42.43364 | 2026-09-03 04:40:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 958d1a48-c461-3896-a084-be75325f1240 | -12.40699 | -44.81048 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dbf7c56-05be-39fd-a96f-a615d1629a98 | -11.28942 | -45.11786 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08eda5a7-fd01-3198-a42f-678447ffd726 | -8.46923 | -54.67662 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6df0ae2f-4463-3020-bb71-346293aed411 | -11.02406 | -48.38144 | 2026-09-03 04:40:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2efa8b-dd3b-3fa0-94ff-0ce085b0bf45 | -14.02196 | -41.77547 | 2026-09-03 04:40:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d392596d-d219-3996-b76d-6f718c7aeaa8 | -8.46438 | -54.67569 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 982cd251-2069-3330-9519-b9d500b66576 | -11.68585 | -46.94126 | 2026-09-03 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd12c91a-0ceb-33ed-9048-b86f1b601f51 | -15.25667 | -53.83549 | 2026-09-03 04:40:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93e0b4e4-80dd-3e39-961c-dc75ffc509c4 | -8.47019 | -54.67142 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db3e2d96-f75a-302e-af96-86b982364335 | -11.29639 | -45.14281 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ebc995e-2a10-3304-a28e-8a34da9fa93f | -16.94181 | -49.38129 | 2026-09-03 04:40:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a116a5e6-ffb1-3938-8cc6-95a0da4239cc | -11.51819 | -46.90363 | 2026-09-03 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 398b2cd2-aebc-3863-a093-ec20d0357f9c | -8.4663 | -54.66521 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5a6511f-bbc6-34e8-8ce8-3423104970f0 | -10.40009 | -49.95884 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff36aa6-51a6-349b-ac44-8bbb6a9af816 | -13.39489 | -43.00585 | 2026-09-03 04:40:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3db9c9f-72fb-3e47-b3a3-192861ca9189 | -11.30451 | -45.13628 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fde9dbb-1955-352a-9c43-d83721e33c35 | -9.61092 | -48.55834 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa9725d-28f1-3fa1-91ed-f6f353fe9e30 | -10.18414 | -50.26027 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b9a65a2-1d6a-31b2-8a58-66e763478157 | -11.32079 | -45.12309 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c970f3e7-1881-3fed-97a6-551b8fdb2ebf | -12.41057 | -44.81104 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac7c7b5a-fd20-33cc-91ac-e854b691a798 | -10.34011 | -49.9535 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab59f75-db3e-38ca-af28-a5e1e7fe83c3 | -14.95521 | -48.10969 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccb1981e-b01e-34ec-9f48-5e3f4badd9f2 | -10.18427 | -50.28171 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5198d34-2706-3af0-b30a-6273b439e1bd | -10.87876 | -45.30276 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 86e5b341-2719-30d2-a7b2-eaae0e8a0c37 | -8.46136 | -54.65252 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ef8b6e2-dc0c-3455-baaa-da182ccd6de1 | -8.46241 | -54.659 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61ae73fb-2c40-373b-a152-175966e159ed | -12.0911 | -47.05704 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb86b8c7-7ab7-34b1-92ef-cfaee476cb28 | -13.41137 | -42.49476 | 2026-09-03 04:40:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ae0ddf3f-fe5f-3a02-ab66-f4a065b106ce | -11.28707 | -45.15736 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6825f632-07e7-341c-846d-3d79092e19f4 | -9.60974 | -48.56564 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba9b6572-4d2e-3654-836d-817ce81c7dcb | -16.52582 | -49.55985 | 2026-09-03 04:40:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b92f36e-525a-32fe-a9fd-5c95b758aaf6 | -10.48034 | -51.32699 | 2026-09-03 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a716efd2-2286-3af5-acaf-dcc726d331ee | -10.31887 | -49.94985 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabfa5d7-f4e5-3f2e-abda-776255c239b1 | -17.57506 | -44.97243 | 2026-09-03 04:40:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f97e7e-cc26-3f9f-8499-b5865280ac52 | -12.09555 | -47.05048 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b05830a-da02-3d29-87ea-0d77248be061 | -16.07595 | -46.07275 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dc60c98-eb89-3903-9930-2db732be91e9 | -8.46158 | -54.67978 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89c450f2-11b1-3baa-904e-d00dadc3af24 | -10.33944 | -49.95751 | 2026-09-03 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d0a30f5-e41b-3430-9331-b6ca60b6f995 | -16.07537 | -46.07678 | 2026-09-03 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeb2fe3f-c7c9-37a8-bc14-003fc9487811 | -11.24699 | -45.16307 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 653cabc8-bc5c-37e6-990c-7aace47f56a6 | -10.8753 | -45.30224 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5b4b29d1-caba-377a-a164-3dbe88bc52e6 | -12.40639 | -44.81459 | 2026-09-03 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfd8555a-342a-3852-a199-e854dd4de259 | -13.38368 | -51.37824 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1372b1a7-4326-34ca-9326-99b47c89b037 | -10.57223 | -47.71486 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af18e8b1-e573-3d60-8513-964399c98f9b | -8.46624 | -54.65333 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 244ac8eb-59f9-36c4-8fe9-f48cf110f210 | -8.45852 | -54.66861 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cd87b97-d642-3bb9-a1f9-136080fdd0c3 | -12.04665 | -47.07898 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2f49e85-cf7c-3c0f-acc3-d4e8441971b3 | -10.56501 | -47.7173 | 2026-09-03 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a756e2d-0024-3087-81dc-ec1f6fb8e96f | -10.48782 | -51.32883 | 2026-09-03 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81e5ff8e-64fa-3dcc-b0c9-c55b53094b0b | -10.89807 | -45.32831 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e08f04ab-4d25-3cf0-9aa9-64a332af9415 | -15.89423 | -47.68336 | 2026-09-03 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51ae99f1-7ba1-33f0-bfae-8132d676e79c | -10.75966 | -48.97541 | 2026-09-03 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1825e40-a5ea-351a-9ff5-959f1cc0dd63 | -10.99124 | -45.08637 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0025d58e-f8b6-3d20-8dd5-6f61781b05bd | -10.88391 | -45.31528 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfde19d8-93f7-3523-abe1-1b5133c96efa | -10.87526 | -45.32563 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c837becd-df32-32a4-9731-226f5e0e4be6 | -12.06443 | -47.07458 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7446261a-58af-3ee4-8655-e69129c54ace | -10.87355 | -45.31369 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a2933a5-205a-3f44-9f18-f20086c98cfb | -11.32248 | -50.53664 | 2026-09-03 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a0146f3-58f3-3f27-a1e9-6a8915ad503d | -12.08832 | -47.05295 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe295f5-8ae5-30ef-9755-a49d14a1b899 | -11.28534 | -45.12125 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 256af485-7e82-3d55-b925-1d36dc7c887a | -10.87588 | -45.29843 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fc99ac34-a160-3b4a-a641-829f67fe0a73 | -9.6028 | -48.58701 | 2026-09-03 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efc6b374-dd52-329a-b7ca-bc955d2cdfcd | -11.52195 | -49.20824 | 2026-09-03 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c3d30bd-4923-3e04-bd04-d9b196ec1d10 | -13.38734 | -51.3789 | 2026-09-03 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b14df6ae-70b3-3e66-a02b-5f5109336dcd | -10.89864 | -45.32447 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b38fb91-3cc2-33d0-ac68-92151b54cc29 | -15.33367 | -47.04118 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90ca89bf-f624-3d63-b5b4-3076089dd08f | -8.45948 | -54.67493 | 2026-09-03 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74499bbb-66e7-3444-a1a7-660dd58e9ec3 | -12.05887 | -47.06639 | 2026-09-03 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb7fa16-ea33-34d9-a411-03a9ffccb39e | -14.95797 | -48.11382 | 2026-09-03 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b144e0f8-cfad-3c01-9f15-c69b7d844496 | -11.24149 | -45.16719 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff331d2b-7777-38e6-afc9-f26765fa354a | -10.89141 | -45.3125 | 2026-09-03 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README30.md)
