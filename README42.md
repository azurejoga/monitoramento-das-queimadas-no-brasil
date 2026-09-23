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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41a522cf-b994-3cf1-bc6e-e387cef1e0c0 | -5.997 | -44.26386 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 726b1cce-2c93-3631-8dc5-e49c99f491f3 | -5.77348 | -47.16027 | 2026-09-23 03:42:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3f956d98-610f-328c-b3ed-fe9ed3f1fd03 | -6.57108 | -44.16058 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e9f7ebc-9972-393f-ad76-906d287c4b8f | -5.61674 | -45.25289 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f0dffc62-63c3-3f2f-a8a8-9d72f4ba5996 | -7.41205 | -44.72731 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e257339c-63ab-3c19-91bc-e02e1c826079 | -7.13157 | -43.08184 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8588fec1-5d46-34d2-92ea-1e510db783bd | -6.61507 | -43.75502 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ecf9a2c-6468-327b-a3e7-f616abc2c010 | -7.64965 | -45.45354 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 920fe122-8ec0-3f6d-b255-e74cf13c1f47 | -6.98021 | -42.59188 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 423e8157-5b05-31ae-8427-0817c7393e28 | -7.43828 | -44.74963 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 595123a5-ffb5-3366-9c13-c89597af0270 | -6.51684 | -43.54751 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22111362-da55-3fa9-bc07-2d61fc8f963e | -7.41792 | -44.72842 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 645b7b8e-bf5b-3e58-b95a-d9ae93fb0abf | -6.6018 | -43.73285 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| fe278ff0-f3d4-3dba-a0e1-97ee87a84a49 | -5.34683 | -45.16877 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 50b70266-840e-34ba-b684-e28d673d7f40 | -7.26233 | -39.18169 | 2026-09-23 03:42:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d0d86d0-de3a-34b5-b844-35ddc812d155 | -7.02478 | -44.65887 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9da8ff90-13de-3c36-bcb7-ca5f7f5115e2 | -5.62002 | -43.36089 | 2026-09-23 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52ccbfdd-e26e-3565-948c-88179cc72982 | -6.88792 | -43.75574 | 2026-09-23 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce7ac89b-d89a-34b9-82a3-e99bab6bff74 | -6.37299 | -42.79202 | 2026-09-23 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb29fcc3-ad15-3f9c-8df7-c347ac9e3917 | -7.12823 | -43.09153 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03717530-6307-3cbb-a271-170757353879 | -6.92253 | -46.56268 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9595f569-9f7c-37ae-8de6-4f083a3e29d9 | -6.5223 | -43.54884 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8db2d54-f453-301c-a65d-44c8e628f26a | -7.41333 | -42.64505 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6cc97905-ec68-3147-a871-3a0dc8043676 | -7.45014 | -44.75114 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5356b74a-e120-3676-b07f-fd7cea647317 | -6.62338 | -43.74092 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ca577cb-5705-38a5-89e4-362637033e6f | -6.89375 | -46.57028 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe6cd6e-259f-3b29-acbf-7a92cbb04e1e | -7.13472 | -43.08599 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ed7c5ea-d13e-3ccb-96cb-726b11d885ad | -6.63655 | -38.73416 | 2026-09-23 03:42:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f89452e6-edf3-3b42-a910-516c21a65395 | -6.60112 | -43.73657 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7225cbb7-2f9f-368d-8ae9-74aa026b3ace | -6.52801 | -43.54652 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9390a6b-e396-36d4-9374-2b35e3c306ad | -6.18404 | -45.31709 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5ef2d5cd-0f15-3542-b05c-363f53a6be5c | -5.60415 | -45.95029 | 2026-09-23 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c566219-13b0-3b21-8005-2f99f78b8b22 | -6.60076 | -43.74939 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0d52db4-b0b5-3870-9200-4603712d1598 | -5.76249 | -45.10886 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 4d10cad5-4c62-3762-a310-32aec65b0482 | -5.99769 | -44.26001 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a6ffc62-5f74-3392-819c-dcd5846a088c | -6.13923 | -43.84267 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9c784f0c-e7c2-39cb-9f3f-9a968fdd14d9 | -6.5278 | -43.54995 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5bd13757-b29a-3e73-83bb-a6d329d5c848 | -6.32521 | -43.93962 | 2026-09-23 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c494c528-6cdf-3d08-a40e-a4075570b3dc | -7.97772 | -44.09282 | 2026-09-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89f7e8f7-1e1f-3e2a-ade0-0d20e75c6dc5 | -6.92907 | -46.56433 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 100c4a39-fba8-314e-bbc6-cdd7199a1b63 | -7.40874 | -42.64111 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba0ef7a8-57cb-3dff-9d57-2f3359381737 | -6.1374 | -43.83981 | 2026-09-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb4c17cb-ff6f-302f-8431-3ee0837baa41 | -5.75544 | -45.11263 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d417636a-f2a2-3e4e-8c69-5790db2db8eb | -6.60877 | -43.75792 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b90a674-3a49-32a8-8bdd-f62cc72a557f | -5.99044 | -45.23845 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fea37b76-b90a-324e-941b-8913b7b4ed3b | -6.9346 | -46.55737 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2da121db-a5d4-39fe-98bd-e60fcae6851f | -6.93234 | -46.56921 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54ed301e-0765-3413-926d-a860e2c6f11a | -6.61158 | -43.74244 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 282989ec-ff24-3c5a-afd9-cc8bd5fa079a | -5.28543 | -47.25782 | 2026-09-23 03:42:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 720bf3cd-2e38-37a7-9479-bc5be5b2d1e8 | -6.5725 | -44.15266 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 620c62ac-3917-3f80-a4fb-234d5124d2dc | -5.59531 | -45.3717 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1c18a8-34d3-3de3-ad28-e479ea4d2483 | -6.61428 | -43.7276 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 78372144-265e-39c9-9ffb-fe061c5d18c4 | -6.57323 | -44.14864 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85bfca0e-185d-3adc-880e-b2a830b56786 | -7.34916 | -39.31168 | 2026-09-23 03:42:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dda8c517-34b9-338f-ba9b-67c718025cea | -6.92811 | -46.55553 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7250e1c0-04b9-3bf9-bd80-b5b59108ad07 | -6.90982 | -41.6991 | 2026-09-23 03:42:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8f6596ac-3ade-388e-a6d7-067b1b577e21 | -6.17828 | -45.32297 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70fd01be-98bb-30d0-ad9d-d0a9cad633dc | -5.77564 | -47.15742 | 2026-09-23 03:42:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 49b56eab-43be-3881-a58e-1d01dc37fd41 | -5.57009 | -42.7319 | 2026-09-23 03:42:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa92a515-a787-3eea-8e48-df99163a3ad5 | -6.67059 | -42.57098 | 2026-09-23 03:42:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e6d2d55b-c159-3306-a76c-01a557cd3da6 | -6.1854 | -45.319 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 336770d9-9e30-3425-8db3-0f35222e66a5 | -5.28005 | -47.26423 | 2026-09-23 03:42:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e05fd8fb-4dea-3379-95a1-ab1de4f62d15 | -6.89349 | -43.75673 | 2026-09-23 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff35e85c-c9ec-3725-b34f-330b5160a15a | -5.60404 | -44.02373 | 2026-09-23 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad3fe427-adca-37fb-b2a0-65742e404492 | -6.18936 | -45.32298 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6eb3640-0cdc-316b-af05-6465100935a5 | -5.34237 | -45.1698 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62ea30fd-a871-3197-ac31-112cd3a3111b | -6.1062 | -44.15447 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de403d91-e79f-3601-9055-99d0c36d6fd8 | -7.13627 | -43.08624 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb066f2e-3a75-3eed-87fa-9301fbd39a6f | -6.60462 | -43.74903 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b1d95893-7d2d-380b-8f7c-38b020dd6b0d | -5.24559 | -40.59744 | 2026-09-23 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34a5ffd4-e4fc-3d00-b7d4-475603172336 | -6.61019 | -43.75009 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ceeff051-8215-3bd7-9e88-c4c8583f1c10 | -6.32346 | -43.93839 | 2026-09-23 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f7cffa3d-34f6-3936-9e45-95fe01f0794d | -7.14135 | -42.08381 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57318a36-0715-322d-8b3f-2743fa3cf17e | -5.99663 | -45.2396 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2f00e6-967a-316a-aed0-31e669f8dc02 | -6.20208 | -47.37996 | 2026-09-23 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1198986c-4029-37ec-be1e-b5089c9ae7fe | -6.3386 | -43.37059 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 463d9ac1-fff4-355a-b1f8-0814fbf700cf | -5.61448 | -43.3599 | 2026-09-23 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29882e98-fc58-3801-8569-63d544b335ea | -6.89145 | -46.54596 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a534038f-a065-37c2-a3c5-a8d71762658b | -6.03191 | -44.03657 | 2026-09-23 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17c35578-e226-3726-abc0-aeeed084ff1e | -5.98949 | -45.24353 | 2026-09-23 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d0f4ca6-b6f4-370d-9566-fd4b228cd5a9 | -6.72198 | -44.15051 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8c19f562-37f5-3581-b5d0-8309c575befe | -6.59786 | -43.73305 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be0d6d0b-2125-3b29-a1d8-66f5c162f53f | -7.97205 | -44.09229 | 2026-09-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd45e739-e359-3a88-a34f-90536185de41 | -6.19511 | -47.37844 | 2026-09-23 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49326d89-4400-377f-98d7-1bd356c21b2e | -4.83272 | -42.87415 | 2026-09-23 03:42:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09138fa7-e7a6-3ac3-b707-76beeb4af984 | -7.31537 | -42.26351 | 2026-09-23 03:42:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 591db4ab-4355-3c21-8f08-f6b495fa8b67 | -6.97287 | -42.6035 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba16a3c2-7cef-3608-aada-1ce10362b693 | -7.12629 | -43.08079 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7f5f268f-69f7-387e-abb1-6c6512330886 | -6.41578 | -42.82686 | 2026-09-23 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb4b1c88-cd10-3d44-84b8-b8351c690d0e | -6.60212 | -43.74162 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04dc0e22-7faf-3214-aed8-8f33a3382029 | -6.4257 | -43.48617 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c47c541-402a-3d5b-93af-4e872efe82b1 | -5.76778 | -45.11485 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63cceb70-944c-3177-bdd7-fa9464f795e6 | -5.34324 | -45.16489 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25346086-4344-31cd-ac22-a30cbbd62718 | -7.44499 | -44.74614 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4803b82c-aecb-32aa-8f41-80b9d2da47e2 | -6.60804 | -43.73021 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| aa642361-678c-3656-9c5d-90647883aad3 | -5.61767 | -45.24769 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 55efb8d0-6590-3851-8ed1-1dcb0d795731 | -6.62065 | -43.75607 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 662bad2e-832d-39a0-a52a-10e89a6b654d | -7.40445 | -44.7356 | 2026-09-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbabb0bd-bd7a-3c78-aca0-72538d83987c | -6.72185 | -44.15761 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 16fe8a5f-6ce5-3a5d-beec-7d7c9245a1eb | -6.61993 | -43.76001 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README43.md)
