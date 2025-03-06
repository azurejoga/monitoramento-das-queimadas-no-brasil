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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ddcee2f-efc4-3a4c-9ad8-0ec77a680c27 | -7.47529 | -34.84412 | 2025-03-06 03:23:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b9d4726-e3f8-3273-8084-dc6aa3600a31 | -6.97139 | -43.01061 | 2025-03-06 03:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 991685d0-85f9-3b94-8a01-adde4c8e5960 | -6.97035 | -43.01634 | 2025-03-06 03:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 99aef431-abdf-3fc0-b6d2-fb22159e387a | -10.69546 | -37.04897 | 2025-03-06 03:23:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b360afa8-5905-3d37-b7d2-328592898d43 | -5.46013 | -36.91108 | 2025-03-06 03:23:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 628a6103-6b5d-3ea7-9d4d-ec37dabb63fa | -11.21165 | -37.73053 | 2025-03-06 03:23:00 | NPP-375D | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e2e2e66c-45d3-3661-b453-7ff803dc85f0 | -20.58839 | -45.88531 | 2025-03-06 03:27:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 572d4d2b-5346-35d4-8426-399ede2bc8c7 | -22.90138 | -43.75365 | 2025-03-06 03:27:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1eadc16f-4f50-3d88-ae3f-d6d04d805332 | -20.59431 | -45.88749 | 2025-03-06 03:27:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b882d3e-7968-3fed-93ae-12fcdd32339c | -22.91099 | -42.60799 | 2025-03-06 03:27:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 647d686b-5c16-3a12-980d-bc353f5a3582 | -20.59549 | -45.8824 | 2025-03-06 03:27:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a137c2-3f4b-3c12-acff-0de49d63cc42 | -22.9063 | -42.60646 | 2025-03-06 03:27:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e0c2ca28-aed8-39d4-8850-6a15e898be16 | -27.54543 | -51.10707 | 2025-03-06 03:29:00 | NPP-375D | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7f188acf-5dde-33fa-bfb4-7b4ebf382853 | -27.55222 | -51.10964 | 2025-03-06 03:29:00 | NPP-375D | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a3e2463d-a584-3ebb-8bd9-86695c5faa7d | 1.8504 | -60.5923 | 2025-03-06 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.2 |
| aff8e7bc-2a10-37b8-b8e5-96179592ec92 | 1.8504 | -60.5733 | 2025-03-06 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 6a88707c-2990-3b98-8c93-c52aa70fe012 | 1.8686 | -60.5732 | 2025-03-06 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 63019b70-99a4-3629-a631-02221152fcab | 1.8504 | -60.5923 | 2025-03-06 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| afaa72ee-7938-34e2-b778-6152d5615323 | 1.8504 | -60.5733 | 2025-03-06 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b48528e7-e65d-3c60-8442-e83056655474 | 1.8504 | -60.5733 | 2025-03-06 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c482578d-448b-3020-b2d3-85c6bc62b8fa | 1.8504 | -60.5923 | 2025-03-06 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 144a3fc4-1236-371f-a52b-bad6db9d936e | 1.8504 | -60.5923 | 2025-03-06 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| be719d33-ca8b-3027-8690-c8becf2ed0d9 | 1.8686 | -60.5921 | 2025-03-06 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 89d2ad3b-7ca6-37a0-9fb6-5649705416e6 | 1.8504 | -60.5733 | 2025-03-06 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 526c4e17-d6d3-39f6-af3f-39c7ef00dbec | 2.62326 | -60.41858 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7b63e658-584b-377a-99ba-69712b246f44 | 2.84265 | -60.86004 | 2025-03-06 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 598d1859-3a99-3b24-80c0-e643d1064072 | -6.97071 | -43.01553 | 2025-03-06 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd620293-72d4-317a-a06d-e764673fd478 | 2.30206 | -60.20821 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9aff6f7-5abd-3dac-85f2-10a5486dca45 | 2.63099 | -60.42396 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| aff8f474-4ffa-3242-8cd5-d064035a03ea | 2.3029 | -60.21389 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e516081c-4a52-3c47-8041-dfbd2ff01a9f | 2.85064 | -60.86574 | 2025-03-06 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5f720ca-076f-3e6d-b375-7d4deddda529 | 2.62815 | -60.41591 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 821a22f7-92c8-3055-93db-f601eaf4a09c | 2.63008 | -60.41769 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4d0c08c6-365f-37c6-8856-072da38cd91d | -7.09714 | -44.38763 | 2025-03-06 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 981ab407-a9fa-3b43-9a47-73fde4e42dea | -6.97371 | -43.01442 | 2025-03-06 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db0450e9-d36c-3a62-9ae0-e40c4b9d44aa | -6.97136 | -43.01112 | 2025-03-06 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5afa2ec8-f116-3e5e-ab2c-3452434876f8 | -6.96924 | -43.0138 | 2025-03-06 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2132f955-6d9c-3263-a829-c5ab847c1daa | 2.30586 | -60.2114 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 544b94ab-5210-3c30-9687-074cdbac82ed | 2.62909 | -60.42214 | 2025-03-06 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| fc3aed4b-cc9d-33a6-9e2b-93ce89dadcad | -6.97433 | -43.00999 | 2025-03-06 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b63ab971-2fae-3240-af97-401ba330e1fe | 2.84461 | -60.87342 | 2025-03-06 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fc6edf15-b5de-3d55-a643-3c86c27d439b | 2.6354 | -60.4119 | 2025-03-06 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c004fbea-5ea7-30f1-9a70-dd67aaa51270 | -13.96142 | -48.16835 | 2025-03-06 04:40:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6da50a1-7ec1-3ee8-8ebc-8c8735a978f4 | -13.96372 | -48.15234 | 2025-03-06 04:40:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0de5ba30-a1c1-3303-b805-2140918f906f | -10.66462 | -44.40621 | 2025-03-06 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d77582-dc21-3245-afab-b50fe97b0568 | -11.86255 | -58.06034 | 2025-03-06 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79f3f51-484c-398a-a1ef-ff64b0d8b292 | -9.57886 | -57.39725 | 2025-03-06 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f36bafb2-7cbf-3ef1-be9a-6d28913e88fd | -13.00579 | -46.66224 | 2025-03-06 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8a85644-a856-3868-b9cc-e30fe3f51840 | -10.23187 | -44.76383 | 2025-03-06 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d2f7585-78e1-3fcb-baed-1ee0fb18194a | -13.28873 | -47.0689 | 2025-03-06 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caafa7fd-698e-3f0a-bc4f-2e061432dd6d | -10.66033 | -44.40561 | 2025-03-06 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e67659-9f43-30d1-a395-c115acf7e32e | -13.00511 | -46.66712 | 2025-03-06 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 185708b3-835e-3385-8b82-37d01f8dc318 | -13.35024 | -47.01749 | 2025-03-06 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10ad83e1-7686-38bc-b336-860b522b8ef2 | -13.28498 | -47.06826 | 2025-03-06 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75640333-60d8-3c1a-bed3-a073f931fe48 | -13.23631 | -47.35726 | 2025-03-06 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99335f18-64ad-377c-9417-5081290d8b78 | -11.46104 | -48.01146 | 2025-03-06 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9154006-c909-39c4-ab93-c48fa91c37f7 | -15.56901 | -46.26793 | 2025-03-06 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d6ecda9-dc68-3056-9fb5-cc801540190d | -20.76471 | -46.7692 | 2025-03-06 04:42:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c5a4189-fa20-3380-800a-a98136994680 | -19.22204 | -43.22626 | 2025-03-06 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 79d83864-f714-3446-ae1f-b3aaecacfe35 | -17.98328 | -47.21952 | 2025-03-06 04:42:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc6acd7c-3f61-350a-bb6b-3fbfd055111a | -14.85467 | -46.78915 | 2025-03-06 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6f6fbc5-9c73-385f-a173-a9176a825358 | -16.58965 | -46.79493 | 2025-03-06 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91db08c1-4c26-395e-8f01-c87d2e68efcc | -18.69549 | -48.0179 | 2025-03-06 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1759b536-3434-339f-9c34-c804554d15ba | -19.78156 | -45.39107 | 2025-03-06 04:42:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38d6cf29-ebc7-36b6-a93d-5bd51e6112bd | -20.58013 | -44.57709 | 2025-03-06 04:42:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 43d48f58-9cc9-3357-9d9f-587347308b4e | -15.35101 | -49.61206 | 2025-03-06 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00b5ecb7-ad2d-335d-a6d9-65692ae340b9 | -15.25492 | -45.61449 | 2025-03-06 04:42:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61ee6471-3e3c-3f03-a9a8-01a542b26ed9 | -20.762 | -45.57251 | 2025-03-06 04:42:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ff34ed8-9a48-339b-a066-2c08d8b1c50b | -17.78108 | -42.81037 | 2025-03-06 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01301fb4-9921-38d7-9180-78e8544f8b43 | -16.11176 | -47.98108 | 2025-03-06 04:42:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85cf3124-ad5a-3387-8295-f4c610d4b068 | -14.85362 | -46.79264 | 2025-03-06 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 658472fb-57a8-3e6e-b93c-e4b7181714ad | -20.118 | -47.0415 | 2025-03-06 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 884a4b34-71c9-3725-bddb-3c39723e88da | -15.56851 | -46.27164 | 2025-03-06 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd11bc2d-393e-3f54-9544-644b5e1a3bea | -18.69634 | -48.01661 | 2025-03-06 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c99e86b-7ff0-3271-8248-6be52099d7ee | -19.70335 | -44.77222 | 2025-03-06 04:42:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2a3dc325-0b4b-33c4-b2c3-cbcbbdad2196 | -16.6832 | -43.88651 | 2025-03-06 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20f29991-6a15-345d-9489-6421166aec75 | -15.21075 | -51.17768 | 2025-03-06 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acbcffb7-9bae-3732-8c9a-1ffda00b32c2 | -19.68036 | -45.38103 | 2025-03-06 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4511d44-6fe7-3df0-aa05-8970005ac29e | -20.59175 | -45.88811 | 2025-03-06 04:42:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b97eb7a2-40d9-3d64-88b6-c37103ca9a3c | -16.58781 | -46.79399 | 2025-03-06 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e06c184-964b-3259-a112-8b7378767cfc | -23.40485 | -46.5567 | 2025-03-06 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fee8a2f2-aae8-323d-802f-b0d6b1b62c0d | -21.69827 | -50.35405 | 2025-03-06 04:44:00 | NOAA-21 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8a6d6df3-e469-39f2-a23c-402b1f8130a7 | -23.34073 | -46.7726 | 2025-03-06 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c2205f9-d5ae-332c-a5f2-2c05896cb3e0 | -27.54908 | -51.10826 | 2025-03-06 04:44:00 | NOAA-21 | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 85cd6787-9d47-3a43-8997-dd8cf68f73fa | -20.25987 | -50.65693 | 2025-03-06 04:44:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f07a0afe-66bf-3551-bf0f-39ddcf1fb560 | -21.61583 | -48.47305 | 2025-03-06 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c9b1a5e-8367-3ff6-8a0b-4b4f52bd21d4 | -26.42853 | -49.96572 | 2025-03-06 04:44:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e707bed9-bfe9-3880-9433-930906e0e5e1 | -21.58418 | -57.58402 | 2025-03-06 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e18fc0-060a-3c5c-9e9d-0b1e79e3cd57 | -22.90174 | -43.75183 | 2025-03-06 04:44:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29070e3b-5e25-3d14-9f2e-d83f5f2672ed | -21.61518 | -48.4781 | 2025-03-06 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75da2f72-b7df-353e-8ea0-b5a45ebc40c9 | -23.59402 | -47.43888 | 2025-03-06 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 234ac488-b30b-3d18-9bf6-8d049aa6b1b8 | -21.69768 | -50.35826 | 2025-03-06 04:44:00 | NOAA-21 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 021fe87f-1b6a-3543-8b71-83f59f32831e | -21.69709 | -50.36247 | 2025-03-06 04:44:00 | NOAA-21 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a2bed978-5ca1-35b4-8ba4-e293ac492dc1 | -21.47279 | -48.65544 | 2025-03-06 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2e68b40-b8d2-3c7b-8578-08e6814c0f6a | -20.72484 | -49.43439 | 2025-03-06 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8571a83-4742-3442-a2ab-6300f0751930 | -23.29921 | -49.37486 | 2025-03-06 04:44:00 | NOAA-21 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8aa121bb-7eef-33a4-81be-9b415dc872a9 | -22.53899 | -48.81352 | 2025-03-06 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f0ced30-e5bc-3633-bac9-610532ed070e | -23.13481 | -47.71831 | 2025-03-06 04:44:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dfb1b2af-ace2-3e66-9a9c-c7f9df0c0c6c | -28.58658 | -49.43954 | 2025-03-06 04:46:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e5bbbf4e-884a-3d6d-a19b-4db5efb66899 | -29.58264 | -51.99093 | 2025-03-06 04:46:00 | NOAA-21 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README3.md)
