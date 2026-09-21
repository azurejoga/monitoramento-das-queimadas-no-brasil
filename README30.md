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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b884004-abee-33f9-bc52-0abaf443a188 | -19.4203 | -46.39662 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf4b462d-264a-3454-9f5a-7c27a1d241bf | -14.05578 | -52.11384 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35f8de1b-1270-3060-984b-b6e714e389bb | -17.80465 | -42.54389 | 2026-09-21 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ecf60c7d-48d5-35ef-b6c0-688c5f1f7bbc | -14.17515 | -51.7975 | 2026-09-21 04:04:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba44732e-8512-3154-98bd-bb7262a8ca81 | -15.44498 | -48.45742 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0ff5378-4c67-3eac-8465-7962b2e48943 | -16.01578 | -52.53099 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72ddd28d-b1f2-364d-986d-4fe5c64311f4 | -14.04372 | -52.07224 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fb11b27-9e81-3694-9401-727f16e3fb74 | -16.03282 | -52.52156 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 05c19f91-0294-36c5-8cbe-548ac52e219d | -18.04096 | -50.9303 | 2026-09-21 04:04:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 795bdcf3-1b83-347d-b8a5-64055295fe83 | -15.46133 | -48.43165 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 728dd050-2bc8-3a70-9771-9e5494ff11a2 | -19.41427 | -46.40424 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0705f92f-71c9-3a31-bbb4-1fa81c422682 | -15.45928 | -48.4798 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0edf27cb-1706-3643-8665-97c913f542a6 | -17.57244 | -44.97486 | 2026-09-21 04:04:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4099f74-f9eb-3961-af4e-d2e03ae8f628 | -16.04091 | -52.51715 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 5bb58b82-3232-3fee-9edf-52c8ce78d3f0 | -15.46007 | -48.47602 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bd33ecef-a51f-3d2b-9871-b4aac7f8af22 | -19.41179 | -46.39367 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7330dd14-f20b-3e7b-83bb-2b93112a1e3f | -16.02656 | -52.51432 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cd388c5-6e5e-3a45-83e4-3c52530c817a | -18.97559 | -43.75714 | 2026-09-21 04:04:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbe57319-5818-3d36-8653-ef3f085e6f4c | -15.45561 | -48.47052 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bb3fb344-5b38-3790-95a6-012374f017b6 | -19.67986 | -46.29428 | 2026-09-21 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 69489afb-704b-318f-b5ee-da04ecf9a91b | -14.05182 | -52.06796 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 209d38f8-d91a-305a-b7a5-eed87996cd80 | -15.46065 | -48.43502 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88b78ba6-8a00-33de-bbdd-a211b7521912 | -15.61325 | -47.83732 | 2026-09-21 04:04:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89dfca42-2212-3ebc-831f-647d2d602ea3 | -19.41677 | -46.41478 | 2026-09-21 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17d2eae2-490a-342d-9c11-e2dc5e679f2f | -16.0395 | -52.52335 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 062ad2b1-3a3f-3107-b790-78a755193712 | -17.2211 | -51.76521 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf7ce77-2c0d-3a58-b391-44d73c49d8ac | -18.63085 | -46.85895 | 2026-09-21 04:04:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1483e54d-3c31-358f-a316-c3912a2519b4 | -17.2224 | -51.75939 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82b6223-1d42-314a-9311-df16085d8c12 | -14.06255 | -52.11565 | 2026-09-21 04:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df9a5fea-b8f2-3695-ae36-02fd5430701f | -16.68593 | -47.88844 | 2026-09-21 04:04:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 166704cc-a40f-39fd-987d-80180f85a12a | -16.00909 | -52.52918 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48cc5522-c0b8-3983-b66d-08782dea75ea | -14.75416 | -48.41935 | 2026-09-21 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7dc704d-73d5-3593-b2c6-deaee6827da2 | -15.45995 | -48.43854 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a1c090e-b79d-3fa4-9111-93b1c13d1580 | -18.79161 | -46.46892 | 2026-09-21 04:04:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7acd3245-28e6-3bb2-bbe2-caa391813ac0 | -15.16307 | -48.16723 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 837acf5a-09ff-3dc6-9c92-74dcf2261b69 | -19.86922 | -42.6371 | 2026-09-21 04:04:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e879c622-e62a-30a1-8e48-4515f9c83dc0 | -16.43127 | -42.63468 | 2026-09-21 04:04:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c841509b-8bc7-3a81-b88a-222a37dc646d | -16.02898 | -52.50726 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 43520027-0cb5-3a82-880f-ab7f5cf74367 | -16.0495 | -52.5106 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 273.6 |
| 45ccd2cf-f7cb-3882-8aff-2ac2b7f6bb85 | -7.5703 | -57.6962 | 2026-09-21 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 931f6d39-9bcb-3323-93ab-486452423a24 | -3.0717 | -61.2764 | 2026-09-21 04:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| ab1f70db-2502-3185-ba7c-18744ad83cc3 | -7.5889 | -57.6757 | 2026-09-21 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4efea390-68fb-3291-8968-388835def353 | -16.0491 | -52.532 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| a66c2e18-c910-3699-b6c3-8a9962e4e545 | -9.5593 | -66.0545 | 2026-09-21 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| d623eb7b-32cf-3dea-b764-938f3023d1da | -16.0304 | -52.492 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| eece5e59-3795-3c70-8eeb-6af3f1b4f75a | -7.5704 | -57.6766 | 2026-09-21 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 28a4a9dc-d362-3b5e-a7b1-996993ced7de | -16.0296 | -52.5349 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8fade774-fc3e-34c5-a780-4fb0a2ef6b9b | -16.03 | -52.5135 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 398f9295-e1c8-386c-b4ed-27078be50ae4 | -16.0499 | -52.4892 | 2026-09-21 04:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4bf1d2b3-96d2-314f-8c6c-1d8efcf34580 | -10.8011 | -50.7604 | 2026-09-21 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 008523a1-4b8d-36db-8b7b-c07cb91dd753 | -9.46 | -45.4 | 2026-09-21 04:15:00 | MSG-03 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd22238d-1fc2-38ab-aaad-b553e785fd26 | 1.05547 | -51.19091 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d85083bb-6c77-3ca6-80b9-3b6483924f90 | -1.90739 | -45.81131 | 2026-09-21 04:17:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 2b995239-478e-3724-b7bd-6a70eb7ca4bf | -1.82635 | -45.21674 | 2026-09-21 04:17:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d5576fa-30c0-3000-8721-ebabadfc917c | -1.827 | -45.21268 | 2026-09-21 04:17:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f6382f7-43e0-3618-b41f-f256ebfa0425 | -1.28767 | -46.60863 | 2026-09-21 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3783ab6-c1b4-38fa-be52-d21eedb72ac6 | 1.4354 | -50.83545 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae204ac0-cc2e-381f-b807-fbaf776ade4d | -1.90371 | -45.81074 | 2026-09-21 04:17:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4ceae3a2-da77-33dd-8f50-46c15e871beb | -1.05896 | -48.11243 | 2026-09-21 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1413c4ad-ada1-3a78-a693-2ec7a1f51178 | 1.05987 | -51.18283 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 122e1fe8-a978-321d-8efe-c90ec10c9691 | -1.29157 | -46.60925 | 2026-09-21 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 501d6656-73c5-3d11-bb19-b02159aeedb2 | -1.21884 | -46.01725 | 2026-09-21 04:17:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43051200-5ace-3f62-954e-1db6991286f8 | 1.06042 | -51.18639 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9aaf1aa-a4e4-343b-af43-d156fd6c9a65 | -1.36289 | -49.30776 | 2026-09-21 04:17:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d76b3e7f-6318-36d9-a7fd-5ebc7c5a3c9b | 1.42999 | -50.83631 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43537912-27a0-3ecf-919d-a7a002c23167 | 1.06154 | -51.19366 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55f23119-965b-307d-a187-8d15126c3f39 | 2.12457 | -50.68627 | 2026-09-21 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 758c4f2d-28b3-31d9-804a-493aab060df4 | 1.06098 | -51.19001 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16903a5f-7d94-3816-bd46-475e39c7e8ab | 2.12406 | -50.68282 | 2026-09-21 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 243aa994-667e-3773-9313-bd0d3b81d134 | 1.43593 | -50.8389 | 2026-09-21 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 297f910f-4302-37cb-b2b3-68405f5416de | -1.35824 | -49.30699 | 2026-09-21 04:17:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83ebf3a5-deb2-3a2f-9557-a3d868744400 | -5.00872 | -56.09359 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83c1b52a-2d53-34f9-91b6-24313c7e7059 | -6.90879 | -42.92488 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6f50ebd2-54e6-34cf-a05a-c281ce323041 | -8.30721 | -46.00217 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9323abb-434d-33d8-8d67-114820d114b7 | -9.5939 | -39.00956 | 2026-09-21 04:19:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58078685-b9d9-353e-bed8-cba596ce85e2 | -7.24824 | -55.58834 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f083b739-4d38-32ab-9fdb-aa95dbd5c00b | -9.47401 | -45.41171 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ece95d26-74cc-3b83-8f37-57b0d64745d6 | -9.45498 | -45.40117 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37010270-bcfe-3536-9d76-7fe016066f63 | -7.42006 | -44.77025 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75f87a64-e550-30d7-86a6-4c3c886e4ff6 | -7.5873 | -46.72549 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66ce1154-8734-33a2-9dd6-4a01c6bdb33a | -5.83941 | -53.49235 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174d8a0e-16a8-3c29-81e1-e21ababafec3 | -3.65864 | -54.27226 | 2026-09-21 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0533ef27-b24f-3c53-a968-ed6c2506aae9 | -5.6599 | -42.63889 | 2026-09-21 04:19:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 574a8a1e-8351-3db1-afd8-fdb30ccd9845 | -3.66485 | -54.27352 | 2026-09-21 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b45d1cac-f60c-3930-a4f3-494b459d85c2 | -3.44116 | -50.61026 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11d9a071-96fe-3452-9f27-08cc0a54ec97 | -2.29953 | -48.58571 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54683ed1-671a-30a2-a4b9-47ad9d969b7f | -7.43014 | -44.77185 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc87caf2-215e-32bc-ad7e-658f009e7894 | -7.24239 | -55.59088 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52984605-99ca-3832-a433-15327f25c628 | -9.45656 | -45.41266 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11ad887b-eb57-396d-b6ea-73c84c232627 | -7.29804 | -46.7783 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 557a450c-0514-3840-a9d9-a2acbec0e098 | -5.84676 | -53.55132 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 443eab7b-9bb1-329e-b1ee-93fbb2eefe5a | -7.41335 | -44.76917 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 400bbfb8-7a60-3db6-a0cc-9b0cac684bce | -8.79822 | -48.71277 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98cff5bc-9c09-3eaa-adfc-8be9bd2b87fb | -4.09195 | -52.11853 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bae1697-3a39-39a0-94cc-39fcb52582fe | -8.31414 | -46.00334 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5139a97a-0236-3601-bdcb-b0dd0ddd152c | -6.5605 | -45.55285 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b08e1b6a-f8c0-3c6d-9dcc-3e43b93a3b68 | -4.3416 | -55.66171 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5e276a9-5d6a-3d16-97d8-0844eb8fe532 | -2.82295 | -50.46487 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9348b4d1-30e2-356c-9783-e2bb2d9d452b | -3.38853 | -50.44383 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 433c4438-8d73-31d3-bcdb-61880e6b8655 | -8.13486 | -46.82156 | 2026-09-21 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README31.md)
