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
| 533d6212-1d80-3407-b18a-7b58d09b198d | -4.9361 | -45.5984 | 2025-09-12 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cf49bca-977b-33d5-9d87-9402f9d1fd8d | -6.15297 | -42.60822 | 2025-09-12 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 00c2fcd4-426c-38fb-99ec-28ce7fbcb670 | -7.4417 | -44.43719 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6854c15f-33ea-3c9d-8c14-91111afbe3d3 | -9.05722 | -40.52161 | 2025-09-12 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3139d1a3-18b9-3556-a47d-cdae3b0c4887 | -6.16907 | -43.36449 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90b6cd77-ac53-3a0e-9791-5ed8e3b7d831 | -4.11005 | -38.33323 | 2025-09-12 03:36:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23ea974e-2ea1-38d8-a1a5-bf08d2043150 | -5.65132 | -45.94144 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f5b742-ce41-3c52-9d5a-973459eca210 | -6.40368 | -42.59917 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e314973d-70fd-3db3-823a-183af8265616 | -6.28619 | -42.40169 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9f64e46-172e-3328-867f-50d3e5a5c184 | -5.94815 | -42.78706 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ce4ef3fb-ab9e-3342-9bd5-51008622c32d | -6.88557 | -42.83807 | 2025-09-12 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f277a0b-ff8a-33a3-97d8-865f41cacfee | -6.18243 | -42.62582 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d184b4ac-132f-3c88-be9d-e7e39aae17e1 | -6.82227 | -45.65197 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a9f55bf-b6df-3d93-9cae-e133b641437b | -6.19643 | -42.66846 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 657d159c-1b7f-3564-b093-6c7c33ec8ba0 | -6.1245 | -42.96268 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc360a18-3190-3006-b4b0-35b2654736f9 | -7.31837 | -44.1668 | 2025-09-12 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b23d15c7-c496-3247-8c60-ab5232c49afe | -8.08105 | -42.56794 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6d389af1-9503-3f8b-86fb-fb63e16db906 | -6.47578 | -45.1553 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dd7ad369-e2a1-30a9-ac3a-503d86001641 | -6.65777 | -44.13391 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26fe03b8-94dc-3c83-9ed8-8e99b0122da5 | -7.84961 | -45.39291 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fe8d670-7e29-3c83-af6c-209f7a41c904 | -5.65683 | -45.94819 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3745e1c2-0a6f-37ca-896b-801e1668bfce | -6.21309 | -43.37194 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdf58f32-9d68-39eb-b965-fd44e314d15b | -6.81145 | -45.64007 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a8744f-57d9-302a-8bbe-f2ee9662720c | -6.53883 | -43.11115 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec421fa6-e61f-39c4-af7d-55250a2a423d | -7.56224 | -44.39989 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce5f7679-28b4-3c0d-ac4c-cd95de26db30 | -6.26634 | -43.49026 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 575d3995-2401-353e-a72d-ee954e9dc990 | -7.72957 | -44.8652 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eeb671aa-b40d-300c-8d7c-e46e878fc214 | -7.43777 | -44.98186 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e0c68fd-df34-3dc6-b2fc-c63ce4c43073 | -7.40655 | -44.36399 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44c5ae5d-9785-3071-9e7a-333e5c90bf36 | -6.65836 | -44.13057 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d927350-8e20-3305-82b3-b70e20fdc7a2 | -6.27463 | -43.18199 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a0dac6cb-5b08-33f2-aa74-60d1977035b2 | -8.37357 | -44.84452 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e572e32-81a5-36fa-b683-8d9859e61d85 | -6.30097 | -42.22636 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e2b53a7-ef2e-3dae-8114-558bbbece246 | -6.27403 | -43.18544 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 208eeb75-1e33-3b93-89e9-aaf9f2dae1c3 | -6.29889 | -44.2353 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf990a91-917c-3eab-95d1-acb9dc328ed1 | -6.10767 | -35.54949 | 2025-09-12 03:36:00 | NOAA-21 | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ee1b55e9-ed4c-3724-8d47-8e5afddd9a24 | -9.05424 | -40.5241 | 2025-09-12 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 89adaf27-f423-3d93-98da-b89bf352c340 | -6.82768 | -45.65796 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4eb2ed1d-4790-3cdd-8c59-ea4e88a97dcd | -6.44936 | -41.76508 | 2025-09-12 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 735c88bf-c309-36df-ae4a-8e89680faa2a | -7.84344 | -45.39223 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbbc1d38-7a80-3fcf-a0e9-4bbb1517bde4 | -6.07647 | -43.56585 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1422cb8-459a-30e7-b26d-6b08473bb263 | -7.45316 | -44.99892 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35508804-4bd5-3922-b692-e0bc5abaf5be | -6.12286 | -42.95776 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e5537462-28d8-3ff3-ab16-ae09c4895d29 | -6.96574 | -44.82158 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83699ee9-45b5-30c6-9c3d-2c68dfd9643b | -6.96752 | -44.82887 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7735cb18-a2dd-3821-a997-59cbbff6390c | -7.85474 | -45.39579 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7af4dbd-3604-3096-af93-42a1c0d8ca59 | -6.13911 | -43.37174 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b3be99a-c391-3fae-acef-622bd0a9167d | -8.08159 | -42.56489 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| be077d56-6e7f-3961-b1b5-bc333033bc38 | -6.68006 | -44.1491 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4bf713e-29dc-3402-aeba-33b68412a482 | -5.6 | -42.90768 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f65fc392-cce2-3ccb-90a3-c7ecf3678f6f | -6.40833 | -42.60315 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 40e81802-cdd7-3639-912f-6bf82cf10720 | -5.59657 | -42.91055 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99bb48c0-36ee-341e-a7b2-d98360032632 | -6.07094 | -43.56457 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eca50b7-a1cd-3d2d-945b-21f19115f51e | -8.08712 | -42.56311 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 622c406a-97de-38ab-80b3-a1e23d97b522 | -7.44101 | -44.44099 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a66a82-c442-306d-98ab-bf65ed1e2600 | -6.53944 | -43.10777 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc0b353c-5c2d-34ad-a97e-a1e74630e79f | -6.4083 | -42.59912 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| adc773e4-5ade-3d4a-bae3-a9bd9af8951c | -6.10742 | -45.93762 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa3301d7-7894-3787-afde-5e053970fbc9 | -7.51664 | -44.6841 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 793225e0-7c1d-398c-aa05-455ee30d7a4c | -8.17344 | -46.12187 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e8ea3419-70e1-379a-b81d-8ac5f976d950 | -5.4279 | -42.83075 | 2025-09-12 03:36:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2a0217f8-7816-3daa-9d4a-930705625be7 | -6.71298 | -42.05156 | 2025-09-12 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 31e54781-1247-3d54-9050-eee471e74513 | -6.82855 | -45.65315 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa6c981d-b932-316b-a6f2-060f20b63007 | -4.93703 | -45.59304 | 2025-09-12 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e9b236a-7d74-340a-88d1-148dd5edf86c | -4.48885 | -38.41666 | 2025-09-12 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 35da25d1-d326-3eac-bf7a-ac83d1b7c469 | -6.07875 | -43.26532 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b9c141f-f92a-3f3e-a00c-1c2e10701834 | -7.40076 | -44.3632 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41fd887a-1884-3b65-80c3-4a8c290f2000 | -6.5519 | -43.95847 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4b480ae-b17c-3ed1-81aa-c6268c184cbe | -5.59597 | -42.91393 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5c2b883b-bad2-3f6a-a978-4aebbf1add7d | -5.94874 | -42.78375 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bbbf5998-63cc-3fd0-9b14-476d90528e28 | -6.08422 | -43.26628 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fe2e7cfe-5ac6-384d-9012-5d14b359253c | -6.82634 | -45.64936 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 86fbce9c-e166-309d-89cc-515a15487945 | -9.05498 | -40.51992 | 2025-09-12 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d6143fd6-24ee-39f4-9292-f1eddedacd7a | -6.21862 | -43.37269 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c1526e0-e165-37fa-991c-cf583fd30be4 | -7.18137 | -44.87041 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 170019ef-a083-3b4e-bd7f-c65b4b945dd6 | -6.55764 | -43.95914 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0b54d8a-6271-3e8b-9656-210370864ac7 | -6.65717 | -44.13728 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3b0f72e-8950-35a2-9249-c72b93b34d88 | -6.16191 | -47.27697 | 2025-09-12 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9061c93-61fe-338b-9c24-629b597d24dc | -6.96493 | -44.82608 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 353010b8-c740-3b1b-97ed-0da86d228568 | -5.49825 | -42.67891 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 069e4d72-6696-308e-bfb5-d1e212c76b0c | -6.07714 | -43.56204 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ade8d19a-f8a1-3ed7-b053-9f52991ee71a | -6.08329 | -43.2676 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bbb21d41-e3da-3e80-a949-6ef081205bc8 | -7.32743 | -44.37467 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0539c1c9-c21b-380d-bccd-25f6364e39ca | -6.09998 | -45.94178 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1e8f8b8-ec66-3ba3-b682-2d611367a07d | -3.8987 | -40.92284 | 2025-09-12 03:36:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e126125-453f-3620-b70a-c4a4f2552c67 | -6.54167 | -43.11124 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47397910-bb52-3ba1-9d57-34029cb457a2 | -6.77132 | -41.59316 | 2025-09-12 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d543134-e25b-36e1-8557-34a70b8c4b5d | -7.28954 | -44.48378 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a6bc8d0-2cef-36b2-9458-0dfc045b4ce9 | -6.15241 | -42.61147 | 2025-09-12 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5e0b18eb-bcae-3d4a-b292-ebb09e762256 | -6.67446 | -44.1474 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 24e6c64f-ae6d-3a1a-bfb6-d65b0c6f2cc7 | -6.1251 | -42.95919 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9b2b287-f704-360c-a576-f91680428509 | -5.59717 | -42.90718 | 2025-09-12 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1139bad5-92fb-3ff0-b16c-0a0422cfd4be | -6.60721 | -42.27239 | 2025-09-12 03:36:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1248a136-6fcb-3886-8adf-7d58d711739e | -6.48073 | -43.88316 | 2025-09-12 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2098aac-5884-3850-b88a-b83773c8bb82 | -6.81056 | -45.64497 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 525c9d1b-3c54-369b-8bdf-0785b9ff96b9 | -6.26082 | -43.48919 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cb6b7c3-d325-36bb-92f2-dbf8e49ad4e4 | -6.68567 | -44.15082 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4319ea8-1e5f-3a69-9dbd-6a966926e7e6 | -6.30606 | -42.22725 | 2025-09-12 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 5d9e082e-ed7d-3dc8-9df6-28378b6cf22e | -8.07102 | -42.95101 | 2025-09-12 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88128080-0b75-3622-a758-c613969f7ff0 | -8.18357 | -42.42762 | 2025-09-12 03:36:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README15.md)
