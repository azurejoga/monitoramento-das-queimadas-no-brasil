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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e173c8-5791-3cb4-9cc4-337d38c4725a | -1.46711 | -52.96785 | 2026-09-15 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be508909-f29a-3417-9852-441fbf363d03 | -3.54316 | -53.99392 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 7b162c87-bcaf-3192-82bf-1d2986fbea32 | -2.92237 | -50.41853 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7605f6a9-8e68-3031-81a4-84e834653f45 | -3.63299 | -58.63966 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1be683d-29d1-3800-b883-1debc475f91b | -2.91335 | -50.41151 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb42383f-9a99-3188-af83-8371213066f4 | -3.42935 | -58.2205 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c8c3bea-e578-3aad-b584-c8628b7e5ba2 | -1.22305 | -54.12483 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa75ff0-a295-39c6-8ad7-226321624af9 | -2.95106 | -50.39473 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ad47ce5-f713-3f84-8d14-f2fb97bb15ed | -3.69712 | -58.88263 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94b84f00-0843-3433-baf3-75a7455d2a7e | -4.54401 | -55.61686 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ebd16a-77a8-3f59-8321-81ed10bd3b73 | -3.37119 | -57.69912 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37252005-f36d-3d8f-a3b6-b9d4617c4202 | -2.91827 | -50.41225 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8766d0fc-e62f-3db4-b8b5-cf37280b7db8 | -3.01551 | -51.21461 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8af18944-c6a2-3fd2-a550-21d10e778018 | -2.78164 | -57.02626 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff7b00d-8552-3737-be15-b1c6eab1d35d | -3.16029 | -58.63965 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 120fc60d-1ab4-30d4-8af0-cdc3915ca609 | -3.41704 | -54.7738 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90204f23-7a94-34fc-9de0-c20314077ae1 | -3.11294 | -53.95214 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60b95716-cdf5-36ef-99e1-715986a5239a | -2.95598 | -50.39547 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8466f48-7333-3293-84dc-c2c4c7215217 | -2.91005 | -50.3997 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7a31a1e-2435-3cdc-9c09-f6c09944963b | -2.97531 | -54.15648 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cefadd3-eb88-3b1c-ae3c-0b2448fbd047 | 0.62453 | -60.15821 | 2026-09-15 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac3250c-333b-3c87-a670-fd197716002f | -2.66544 | -57.55758 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2907efc6-ebfd-306f-9936-da9d77b8ceb1 | -2.66024 | -57.50348 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60cfb929-c23a-3b17-86cb-8df22fa5fb12 | -2.9715 | -54.15583 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a774c1fd-c001-3138-be55-f0933f6883c4 | -3.44826 | -57.99079 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a73a7b3c-cb96-321f-a29c-6a5618f7dc76 | -3.04088 | -59.16206 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa28f51c-0d10-31ed-af49-5497ce1195d0 | -2.6649 | -57.56105 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d3fd4797-e6e7-34f3-a011-21f178ce3b7f | -4.20626 | -50.60916 | 2026-09-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 420de070-12be-3246-85c0-f5393b93c1e1 | -5.41346 | -48.53433 | 2026-09-15 05:16:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d0d9f4fa-641e-35c3-8efa-3e280f0cd498 | -2.04257 | -46.93947 | 2026-09-15 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f31c4fba-2271-30ce-8b6d-75b295ffd412 | -3.33366 | -54.19035 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f27e3e-ca6d-3d41-9341-29786fc383f3 | -3.54897 | -58.67584 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc64d702-c594-3c88-8ca3-e9d17eb0e06a | -3.41007 | -58.21402 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65bb5782-b32b-3718-b2ef-7bc35768b8dc | -2.91504 | -50.4342 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9f96299-1639-301b-8e10-20e7f801190c | 2.58161 | -60.30443 | 2026-09-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44f614ad-44af-3f58-a50d-091aa0ac7c41 | -2.90272 | -50.41549 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13403fc5-9202-3e50-bc90-eaac7f5d7906 | -4.52211 | -54.91814 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33e5fd35-c191-3930-9d70-6dd6f3cb88a6 | -3.36837 | -59.82969 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf90c54-e2bf-36ca-a01a-758908876165 | -2.82379 | -51.33836 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e8914f7-bb8a-3229-81b2-b515053c6f8e | -3.31121 | -57.88844 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee790345-a56b-30d8-aef4-a55cbccef2bb | -4.52154 | -54.97277 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37958d06-f772-37aa-b46e-baed0e5cda51 | -1.93476 | -54.3636 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c70187a-bf71-3027-bb31-a144df53b76b | -2.895 | -50.4193 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee30afca-2c0f-36c5-b2ae-af0b3e91b8a3 | -2.90191 | -50.42101 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a313e20c-489a-306f-81c5-fb717a46107f | 0.00594 | -60.58598 | 2026-09-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ce30ec2-7cdf-3f69-9f42-c3a5871a1b5f | -3.75451 | -59.18882 | 2026-09-15 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9ad347c-380d-3bf2-b812-6599ab9a17be | -4.5185 | -54.9677 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1aa48c5c-789e-3a72-a8d5-c965dc8e023d | -3.17264 | -61.12132 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa45c72-02ec-3225-904b-42f0ed0e0d3a | -3.08206 | -50.57331 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a0d05f0-058b-39d3-9da6-0d233984f240 | -3.43001 | -57.97739 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d75e61d6-db2c-36ed-ae8b-e41b89bd9f38 | -2.71124 | -59.61404 | 2026-09-15 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea56c847-56b8-376d-bae7-0e803cffae13 | -2.97392 | -54.15816 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d0c990f-162b-367f-9e34-add2ff12583f | -3.48764 | -50.37321 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 33c824f4-c62c-33a2-bcd8-865fdfc33cb7 | -2.66145 | -57.53922 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff4918ab-1b03-3555-8595-f4acd992ebef | -3.17803 | -61.11002 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b49f11d7-4666-31ba-981a-0b6a0133e9dd | -3.08326 | -57.25355 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1851ddae-e034-3834-8834-d347f2b68ed7 | -4.54339 | -55.62098 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdb8cc19-5a2d-3e84-af10-0180e11b77b0 | -3.08271 | -57.25708 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14cb0bf0-97d6-3d21-acee-0345795f2b19 | -3.19319 | -61.12859 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dca69590-4df1-3818-9ab7-926251f48178 | -2.88718 | -50.41869 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d00bc8f-53d4-391b-be26-034ff4b45dbc | -3.0772 | -50.57251 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee8c9eb-76c6-3a14-9bcd-e8ff1b8204b2 | -3.49096 | -50.38512 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 450abdcb-e91f-3f44-a3cc-6c9bd388e4c4 | -2.68266 | -57.57799 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 549ba653-e30a-3cd0-8a64-87f339a14058 | -2.8978 | -50.41472 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea940320-326c-3bcd-bc82-f3d31e577768 | -2.69817 | -57.58747 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4238bca7-6ea2-38ab-9cb5-bf998cffde13 | -3.42382 | -58.21262 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538215d6-e31d-35fc-b805-21e24a1c8ccf | -4.13855 | -54.01592 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 306b21a9-b17e-3622-b42e-f85dcc6ff904 | -5.2935 | -49.0922 | 2026-09-15 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da648b44-fa55-3486-bb01-7a6b22319a4b | -3.49261 | -50.37395 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36f34c80-de87-3efe-8cb2-2ea8144a3ef7 | -3.27041 | -57.88923 | 2026-09-15 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 225a9252-9ee0-399c-bc23-72d2a75f2309 | -2.68213 | -57.58145 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58334457-9e5f-34f1-bcb7-ae1fa1b30609 | -4.53979 | -55.62045 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5698f104-9296-321b-9cc7-6bb17dd3045b | -4.38931 | -55.20471 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f0985f-219e-37cd-bace-560c2fceef1c | -3.70857 | -52.09483 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b21c078-0bd0-351f-90bf-f15011c906ef | -3.42275 | -58.21949 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f8f5be2-15a4-3fd6-bac3-1ba790dc9e73 | 2.76689 | -60.21543 | 2026-09-15 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2251fda-2c87-3952-b660-78f78a841da5 | -3.23078 | -50.5864 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f7d10604-9dec-376b-9942-d09e21413c26 | -2.6832 | -57.57452 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59eb68a2-8ff1-3ba9-9a60-c5d3c493831a | -1.46361 | -52.96371 | 2026-09-15 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7804692-e475-34d1-ade6-faa93978efe5 | -3.73356 | -61.7499 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 232733e2-f78e-369a-b8a9-50e0906e75d6 | -2.68544 | -57.58196 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d53d57-eccd-34f2-a668-bda4abc0465a | -3.37842 | -61.31168 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97fcce89-11e9-3618-b993-86cf47b2124b | -3.17903 | -57.86451 | 2026-09-15 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c55dab1-9e99-3316-afa4-143988e8d16d | -4.57644 | -54.91226 | 2026-09-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67a4dba5-65c2-381b-b157-011ab5a661be | -3.18093 | -61.11452 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4f8df7e-75f7-3200-af56-c23cc352a27f | -2.90746 | -54.16553 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acf94448-8b50-329f-8b07-cd4281ed1971 | -3.16636 | -58.64411 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347a0206-008a-3bdd-be73-d27970254a8f | -3.07232 | -50.57177 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38efb2f1-f5d6-341f-b8a9-b3493e0b4dd2 | 0.00238 | -60.58652 | 2026-09-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5da6d273-92cb-39e4-8aef-32f276d7f5d5 | -3.42712 | -58.21312 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ce80d5-a3c1-3828-af4e-9f364d0b33d7 | -2.66929 | -57.55462 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 95d5cfe2-127b-3783-aeff-2489ce9688a6 | -3.10906 | -53.95157 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c32851b-0ce8-309f-8991-086a74f3465f | -1.23055 | -54.12585 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78fa1d2d-cdc1-3ae4-b8da-45268cfd0828 | -5.1973 | -49.33156 | 2026-09-15 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc43a358-56a8-3a83-8037-b7a9e6433028 | -4.53917 | -55.62457 | 2026-09-15 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98cad378-49fa-3fd9-9496-6c6e2e630b75 | -2.65637 | -57.50644 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3db12695-54cb-38ec-8af9-06f7ad834c9c | -2.68383 | -57.59237 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf71fe1f-397c-3840-a898-482aada8cc1c | -3.15699 | -58.63914 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0f07bec-e2e3-39ce-942a-65fd842e83c0 | -3.07761 | -61.0104 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b49dd38b-2e3e-38e3-b8b4-18bb70fd20df | -2.65692 | -57.50297 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README53.md)
