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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 978ee3f1-f3ed-3468-a121-022bced2be40 | -5.25844 | -45.06953 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c29f9a3a-14e2-3a44-9b9a-02386de6addc | -5.23179 | -45.63327 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 535d7b50-5abd-3d5b-b96b-e5482df80e8e | -5.20502 | -44.98484 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13119206-28ce-30cc-b6e6-d9fad19a7f75 | -5.19604 | -44.93998 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a96b6aab-c3c9-3774-90fe-9906e06f391a | -5.19533 | -44.94477 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ad2b83-758c-3117-86e3-0c0448558a79 | -5.19463 | -44.94954 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98e45c7f-7d10-3838-9f7b-a09c185456fa | -5.19462 | -45.48682 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f6c7fa-bed6-325c-bff6-74f406d86fe7 | -5.19222 | -44.93936 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57c24c5d-882e-310f-ae07-14722d2f5c93 | -5.18973 | -45.13979 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4015de30-9e71-3e64-aaca-a6b9c8e4cb83 | -5.16013 | -45.53936 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb8fe15f-11ae-3e37-ae6c-3023d926bf17 | -5.14366 | -45.39705 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e31e2c63-4fed-3455-b089-1053a74cba76 | -5.14061 | -45.39202 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 221fe444-d7e2-3e84-ae2a-36863f9317c0 | -5.13995 | -45.39647 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3703704a-6272-32e8-b526-2ad33bab4f2d | -5.13929 | -45.4009 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bb42bd84-4dc0-3676-a11f-fbb40e3e3531 | -5.13862 | -45.40533 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b229c086-c5b7-3ca0-9501-3028f13680cc | -5.13689 | -45.39146 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c874031a-39f3-31b5-ab16-f45ef135863d | -5.13622 | -45.39592 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea96e5e7-11ff-3ca2-b430-84ddf94fd7a7 | -5.13556 | -45.40037 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 70f5510e-31d4-3326-ac5d-c646b745a579 | -5.1349 | -45.4048 | 2024-10-13 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c26ba8e7-0fb2-3ddf-9cfc-141412811de7 | -5.13316 | -45.39095 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30252474-8fdc-3f20-8cb8-f04f652bf812 | -5.13183 | -45.39988 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0d2f724-b01d-39a8-af09-1d602a81ec66 | -5.09196 | -45.84129 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1a058ea-b9bf-3411-8290-a5cb81f1051c | -5.09132 | -45.84553 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7a121d66-2685-346c-9a52-c8693174c83f | -5.08769 | -45.84499 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17db9505-b500-3889-a585-2ed6e408903a | -5.08706 | -45.84914 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| caf03233-ed21-3e2e-b0f6-eb0bb4bfa9e9 | -5.86818 | -46.45459 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6206d674-2467-3ac9-80d6-77a2586181d3 | -5.84752 | -46.23591 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307aceba-317a-300d-9984-63cc0aa3f2f8 | -5.84688 | -46.24005 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cccbc67c-4d00-37be-8950-2fe6ad3164bf | -5.77458 | -46.11011 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b7ded5f-edbe-349d-b088-e5c1d30a892d | -5.77036 | -46.11367 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97bc0379-8622-3bbb-ae3b-a9790177650f | -5.73391 | -46.47981 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7dfa6ef-cd06-3b51-93d5-fd32a8af8f94 | -5.66947 | -46.35585 | 2024-10-13 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b58d9f-4d3e-3b61-bfde-d7114e7a4a43 | -5.61983 | -46.2791 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36cd0623-ffd4-3a50-a70b-4605e6009eb3 | -5.61626 | -46.27861 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8895cc-3a3e-3ace-8db5-763f6d1d1f9b | -5.57099 | -46.16693 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 60939a3b-1eaa-36e8-a18a-fe89dea33c3d | -5.57037 | -46.17105 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 702f269f-3eca-33bd-8d0b-9b6e3a09335c | -5.54283 | -46.18353 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edafadae-5d9d-3272-a078-062683da9fbe | -5.5142 | -46.18841 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87941d90-b140-3ab6-ba06-54d932c4037d | -5.49853 | -46.29061 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9aeaf75-4e81-367d-842f-ca07008afeda | -5.49653 | -46.23213 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5590d7aa-7686-3721-a900-1b823424aa63 | -5.45271 | -46.3044 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c0e401d-dc7d-3dd1-be7d-3ea3d48a04af | -5.26037 | -46.21202 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd440f79-7f8c-33ea-b27b-651210d34ff8 | -5.22163 | -46.01778 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb4bd390-8291-3e38-a221-c2282cf30d5b | -5.21867 | -46.01305 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66e29f5b-bf32-30ad-a59d-fe8c23ee8946 | -5.21803 | -46.01725 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49fc5be6-7bc1-38dc-a3a1-b64e173f3638 | -5.1909 | -46.19372 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb0bff61-c6c5-335a-b0be-cea8d8d3936e | -5.18518 | -46.15957 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f70ad16-802a-381a-abe3-451e2eb222a4 | -5.18162 | -46.15897 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1ccaddb-d2af-333b-84da-0d5fa3adaef1 | -5.17495 | -46.08265 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23b11b31-d05d-3ed9-bcf8-e67441f95223 | -5.17136 | -46.08213 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b04c91d2-aec9-37b0-8fb8-b1473b77b4ad | -5.16793 | -46.15285 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfecc949-cac9-3c08-9504-6baffb5fda12 | -5.16499 | -46.14819 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24c789bf-9c44-32bf-9877-24fd6f0f9f2c | -5.16436 | -46.15229 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e340a80e-3cf1-3e78-a413-0730952d885a | -6.48127 | -46.06229 | 2024-10-13 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55c4546e-29e6-3060-a378-4872400cb223 | -6.47763 | -46.06171 | 2024-10-13 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eacd229-b327-3cea-b3f3-d59a664b7149 | -6.36185 | -46.58991 | 2024-10-13 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df4914e-7038-3c84-afbf-c407a3952fad | -6.31928 | -45.69461 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2905ae-8071-38b6-a9a5-3b39a7c832c4 | -6.31557 | -45.69404 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9a5a263-a9d5-3de1-9d84-e0c8259680ee | -6.07111 | -45.97614 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c0717ff-f4dc-3b1b-b575-1b22bf89843a | -6.77616 | -46.19376 | 2024-10-13 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee87bb10-0af5-3e40-9b0e-41b5dbf89d1d | -7.70338 | -46.64985 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65750440-26d5-3c3d-9b8c-58d377eccacd | -7.70226 | -46.63286 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 749581c5-a436-365d-99de-0a914ac4171a | -7.56134 | -46.24825 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1ec42e0-fc80-35f5-9794-8a1cbb390501 | -7.5403 | -46.86818 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 278c451d-3375-39c0-967c-234424251149 | -7.53676 | -46.86765 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fd8c499-271c-36aa-97d2-eada3ec435e0 | -7.52424 | -46.59225 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30eb96e0-1a98-3bb9-aa26-7428157333a8 | -7.52065 | -46.5917 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddae0964-39a1-3eab-85f2-5af44e0365fe | -7.49809 | -46.092 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0322516f-e0a4-3068-b8f3-541eaae63651 | -7.49568 | -46.08858 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d02d27dc-8259-32dc-a3ba-84cba23c1220 | -7.4126 | -45.68897 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2090845c-e1f0-3ca3-a022-61272eef152c | -7.39499 | -45.62528 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a613a3c-379f-394f-b2c7-993089e03a70 | -7.39121 | -45.62471 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e89d5cd-cbf9-35e4-af9c-f8b233410263 | -7.24892 | -45.38295 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a932b24-f3a9-3757-9343-8ff6b25a8875 | -7.24822 | -45.38769 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08cd8af1-bf50-3e28-b004-f0ade4759160 | -7.2451 | -45.38234 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1c4e160-69ca-34ec-ad17-835f6ba5f871 | -7.24439 | -45.3871 | 2024-10-13 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7e057fe-60c1-3347-90e6-0830e16a52bb | -6.99208 | -46.30116 | 2024-10-13 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138b239e-bed0-36e6-aaf4-98aa30b73b4e | -6.95274 | -45.52629 | 2024-10-13 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76b08193-bb4b-32fb-8ba3-8594d4133a01 | -6.74599 | -45.22534 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06c83e95-ad08-3112-ad0a-e809756b4f3d | -7.9943 | -46.85819 | 2024-10-13 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72a1c36-e635-3330-a27c-bf9f1ead8d71 | -7.99075 | -46.85762 | 2024-10-13 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fa8b362-e4ca-3dca-9a60-764f253e6a5c | -9.2855 | -46.57998 | 2024-10-13 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07513cac-724e-3f80-be20-76cfd15d0670 | -9.22899 | -46.68409 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa16b629-7715-3cc9-999e-060650951e07 | -9.22598 | -46.67929 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed206632-200d-36e4-a307-0e446fd15dd5 | -9.22534 | -46.68356 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e206e57-817b-3246-abf2-a24c6950c385 | -8.71292 | -46.73846 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fb689c2-5ed7-3a22-94db-1739555ff446 | -8.71146 | -46.73922 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13bdbd0b-6f86-373e-8281-44b36330450c | -8.7093 | -46.73799 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59baeadb-2975-3787-a48b-bb1fbe80bd1e | -8.70869 | -46.7422 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04613296-589d-3c1b-82ab-2d031d0e70ea | -8.70783 | -46.73877 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3cd10bf-73ab-33a5-9b63-460ede83376c | -8.70507 | -46.74173 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc7cc69d-0ed7-37aa-875d-3f043d631f3e | -8.70446 | -46.7459 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e841d17-418b-3f61-bd80-02e053d7a9b8 | -8.70358 | -46.74249 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 393468b8-b566-3c85-a175-9d325cf60a30 | -8.70295 | -46.74664 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caadb3a6-18df-33f5-a006-2d09785e32e8 | -8.70155 | -46.60784 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81ae5d02-76b0-3742-bcdb-f8fbc47ad576 | -8.70091 | -46.61217 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d06c07f-e7af-3d5f-adfb-54e2cee92e42 | -8.6992 | -46.59867 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 448c2c6d-c505-312e-b87e-a2123f94d8bc | -8.69557 | -46.5981 | 2024-10-13 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1aed0c40-6294-3189-a2f4-36b3c632bb3c | -8.27292 | -46.85509 | 2024-10-13 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 770c2934-60fc-38f3-8a2c-87a17f5cd57d | -10.40814 | -47.36702 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
