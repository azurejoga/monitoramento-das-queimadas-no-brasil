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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97a9cc52-4fb7-3668-abfe-2dcc979bbd48 | -3.1663 | -50.46016 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7a2f4d3-64c0-3581-a3d4-fae46a2280c0 | -3.0129 | -51.00806 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10d3ae72-21ad-326e-9c0b-0b2426b8ed6b | -3.31258 | -53.86481 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f73185f-f21a-318a-aad2-5ad571eb0633 | -3.18125 | -50.58899 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d44b9105-fefe-338d-ac7e-c6b29e93e9e3 | -4.93343 | -45.72424 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775829b4-99b4-3a0d-ac45-4785214bfecc | -4.82481 | -45.83088 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 39d024c1-3c98-34d8-aa5f-0de9aec4536d | -5.59822 | -47.28014 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbca833b-499c-309c-9f50-e4f179d6cb12 | -3.02407 | -54.05653 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88143691-2b51-308b-b447-c5307c99ddc3 | -4.7703 | -52.77428 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9415af97-db7c-380b-bb63-0e6471e935f9 | -3.56743 | -54.67109 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fd2410e-d967-3ee1-a09c-49aae37322df | -3.25835 | -54.03659 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b73fb1e-5a71-3817-903d-55813be74f12 | -3.01383 | -54.08805 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16be4207-4648-3608-a944-5624b8c7708f | -6.16758 | -39.4502 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 48bd8db3-041f-326d-9d95-06cefd72bff0 | 0.19226 | -51.35446 | 2026-10-09 04:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f249f63c-6a4c-351c-8f16-f6da73931c6b | -2.99073 | -53.8506 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 779a6b45-5d06-30cf-bc31-e9f73f28d85e | -3.74075 | -59.37016 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 799614c9-4bea-3c51-aa27-dd5b694645c3 | -2.91194 | -49.51723 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc44a621-84f2-3c7c-8b37-a37cf3a81309 | -3.29659 | -54.05455 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c036201f-3f00-3805-8c57-d5e21ad16997 | -3.58774 | -54.67762 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f98b9b80-494b-39ab-bd96-ef2f54a59ba1 | -3.00645 | -53.91074 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9003d22a-9d7c-3f53-ad23-8b8803b53d35 | -2.38972 | -57.89581 | 2026-10-09 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9631795b-a5d7-3f69-b887-8066ac1d343f | -3.48736 | -50.48946 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2cc4bbf0-ba92-3076-9f85-598968445d83 | -3.17452 | -49.4505 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b34a61-f782-3d4c-91dd-75235409ca44 | -3.08001 | -53.96366 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea04d8c-007e-32cd-b112-0f64e9c87acb | -5.2649 | -50.1478 | 2026-10-09 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d982010b-de9a-3ab6-93a6-3eae26632123 | -4.45422 | -47.91949 | 2026-10-09 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9e705c0-0c25-35ad-9591-a632e83d014f | -3.11444 | -54.16506 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f34c907c-1383-3990-8e16-79fb34d22698 | -3.57211 | -54.67505 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfea6697-67f8-3115-9544-09e45da2bfb9 | -3.07453 | -53.96572 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 041dc90d-5ea1-3470-8eaf-79eaeb0951b4 | -4.57836 | -55.72496 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19bb21be-27b0-397a-b6b8-514d2f9fd3f8 | -5.37943 | -45.93917 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67c3c695-811e-3eeb-bd5c-14322c8a512d | -6.37207 | -42.5228 | 2026-10-09 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 79d83b1b-3aa1-388b-a87a-2b0ffbe26757 | -6.96195 | -45.27207 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be5ff139-53ee-32f9-b9d1-09e7398a08dc | -6.21721 | -44.83506 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f4c9699-1ce3-3b96-ab43-92a8744ac819 | -2.46915 | -56.05923 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d9b05e6-160b-32a8-a3fc-795247aef725 | -3.0838 | -53.94075 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 505b1994-a537-3bdd-83a2-b4529aa57d6f | -5.7031 | -49.0879 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39bcc90c-f157-33f6-892c-66fccdd28a34 | -3.00371 | -54.08646 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e1aeae-0731-3dae-b21d-c85d61176f32 | -5.35659 | -43.40433 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193a19d3-9dc5-3615-94e7-13ac2f09a60a | -3.58322 | -49.882 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d08989c-b740-3381-8a65-af545a8dd264 | -3.5426 | -59.40835 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6a47e006-44de-3478-8363-439a3062c4ed | -2.94743 | -51.4112 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 684b4a4d-c496-33fb-811c-dee275fa1ba3 | -1.52353 | -54.56834 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac77a31a-8c59-307d-b44d-204998b1313c | -4.63858 | -50.95825 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0d597016-f33d-3bd2-8c0d-c9ae4df4faa0 | -3.30682 | -53.70264 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af5cb70a-f377-3f08-90f3-32bef9c77f5b | -3.00056 | -54.07386 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b01b855-75a7-3103-b0bd-680223414912 | -4.5724 | -55.99207 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5020091-1e3d-303b-9949-2c5f33f8b876 | -3.50468 | -49.93599 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a85ab3a-ee8b-3e58-bbd6-adce7f7c13b3 | -3.52651 | -59.34388 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0edbe3ff-e66a-3003-b94e-402c55325df2 | -4.99243 | -44.99165 | 2026-10-09 04:25:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3dd4f5c-ed2e-3a0e-987e-713bef3c6d6f | -2.75307 | -54.10817 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e90669b-1994-3d6b-8b82-05b66aeb59b8 | -6.60394 | -37.90492 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44597313-f375-3cf8-82ed-f1b10b1678d1 | -5.74807 | -41.62344 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 78a17945-0490-307b-a60c-c7a3322169ce | -3.35792 | -50.41845 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e196c62d-c8b3-3704-ad26-2937a4ad896e | -4.8081 | -56.14344 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a884add-d5e6-3bfa-9a2e-ad24401a8732 | -3.59189 | -54.68479 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4d66f7a-09de-3a4c-89f4-9d0643082c06 | -3.04293 | -54.15642 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d55aa5e0-a2f0-3674-85fa-cb2a37544824 | -3.30588 | -53.69274 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 570eb216-c19a-3f02-8b02-c1c908f7150a | 0.53608 | -50.8963 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33d9bad6-49ef-3ddf-9d25-2e3545e8d4bf | -5.7142 | -53.49049 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ebee1d7-0108-3a9e-a819-25550e4920f2 | -3.58987 | -54.66504 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9c4526a-2378-31b5-be2f-317a99752dc1 | -6.89436 | -45.88922 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d30d4107-5f6e-394a-b92e-5b8a1e87dfba | -5.75292 | -41.67156 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5ef7c4d-c35c-3462-9646-b174eb8d145d | -3.01541 | -54.04607 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91dd0ef0-e410-352c-ab38-92d0bf493036 | -7.19037 | -44.27786 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff29aa58-a1e4-3332-9821-d9aee0b0c467 | -2.88416 | -54.15829 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8216838f-b147-31a8-8002-0bf798a0ac70 | -2.46274 | -56.06139 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dab6ed4-be00-3119-8186-b10b2b6e5612 | -3.00725 | -54.08988 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01c18eae-e80d-3129-9f50-781623fd8fb5 | -1.40913 | -55.41399 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 603fb98e-26bb-3e63-8937-594d95b7c69a | -2.57462 | -56.18149 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65d729d5-3dc5-3110-96c0-1b9d3995927b | -3.81214 | -47.49118 | 2026-10-09 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e03b142c-5ced-3e86-a5d4-63f3a1ffc8e9 | -3.02501 | -54.05067 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41a3b5ad-8e57-3563-89ba-e2b31aa23c9e | -4.1219 | -55.03234 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8213fb99-89e1-311f-9c69-af1dc794e08b | -3.02737 | -54.06283 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d2e8ac-7648-3b83-9488-d3a851507928 | -4.35816 | -44.35643 | 2026-10-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49f55526-9f7f-3467-b841-c348bc08c516 | -1.54237 | -54.55394 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e582cd8f-e54f-33cc-9420-60ff2020ca76 | -3.27911 | -54.06671 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b431d7f7-9d31-3121-8a10-2aaa8b0e09bc | -3.16793 | -50.44727 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93515da0-fed6-351a-b4a4-b283ba3ad692 | -3.30421 | -54.0083 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec7435e0-1091-3cf8-8cd7-11f45eb3eddf | -4.53496 | -47.05122 | 2026-10-09 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65e64441-fcb2-3d41-aeab-3de9ab7fa8eb | -6.70168 | -47.01646 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 610dce7d-67cc-3c98-befc-a307f6d799b7 | -2.51685 | -45.39856 | 2026-10-09 04:25:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3cafedd-83dc-3ec0-9f3a-9f3ccf1c8924 | -4.15732 | -55.13783 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e35c9cdc-3f2b-3258-a14c-dc1068602f4e | -3.00514 | -54.07761 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afbb686a-bc76-3f45-940e-b04c991f6951 | -3.09977 | -53.93722 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c36a836-1834-3135-8766-ffb7dd16d5ad | -1.10885 | -54.17336 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9243d532-68c6-3a1a-ba31-20df9363f2a1 | -3.3109 | -54.03014 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e813f39a-10e7-344f-b696-8c5cc185c0a1 | -3.73468 | -59.45475 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cc5184a-7a4e-341d-8114-0e18fbb97440 | -4.08615 | -48.96302 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e36efd-4456-3fb0-83a5-82d024428650 | -2.54665 | -58.03825 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7664218b-be31-3d70-850b-6db73d8c8b88 | -5.08953 | -46.20679 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84192a6e-5059-3ce9-a0ef-1b7048fbe795 | -3.80282 | -49.94136 | 2026-10-09 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e65e9d30-0e09-31b1-965c-ead4a46b777a | -3.94433 | -56.02269 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ae53651-f096-33d4-a92a-416d37298de1 | -2.57929 | -56.18509 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2cf18ff-9647-3ded-ac0c-2730fb482668 | -5.69667 | -53.46074 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da13f153-365d-3bb8-b014-e2e4a4412d4f | -3.54627 | -55.52502 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba2dee9d-1368-3e17-ba1d-96ceb12fcf96 | -3.20757 | -50.552 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a40f038f-e1f8-31e4-b10f-288465bed8af | -4.37385 | -41.81485 | 2026-10-09 04:25:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1beebb3f-7027-312a-b56e-6e33bd3fa361 | -2.33717 | -48.86369 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d47289f-0f23-3d2e-89ce-45376a3ffc61 | -5.71453 | -41.65925 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README91.md)
