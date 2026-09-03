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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2458dcc0-bde9-3423-b277-1b96275734c3 | -7.2932 | -60.6096 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3a3e837f-b4a0-3b42-b9d2-ca5668f11138 | -7.2006 | -60.6706 | 2026-09-03 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d728d911-9268-31c4-9fdc-fb3c95e50d53 | -3.7828 | -61.7545 | 2026-09-03 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 892841a7-8333-3afe-a511-854073558a1b | -6.7094 | -59.443 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| fc443af2-cc86-37b3-84ba-305e6c157615 | -14.6535 | -53.5642 | 2026-09-03 16:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e56513e4-56a5-3681-990a-0f5cc2ba581d | -7.0242 | -59.2374 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1169b1be-918a-324e-8635-ec4fba768818 | -20.8174 | -57.6709 | 2026-09-03 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 217.8 |
| 28ee37aa-5eae-3d82-8bb3-4ee3bae58928 | -6.8386 | -59.4379 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1309b7d4-d268-355f-95ad-941022f7a245 | -6.8203 | -59.4001 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ca137cc8-8de9-379e-9f2a-949e2d3b8c5d | -3.0164 | -61.4848 | 2026-09-03 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 183.8 |
| cd6fef15-db69-3aea-a5c1-8d148b725101 | -20.8377 | -57.6681 | 2026-09-03 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 159.3 |
| 19fee657-c298-35a9-a08c-f32c90732157 | -11.2292 | -51.2879 | 2026-09-03 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d97c8a20-87a6-3584-b346-a58d5d5ff243 | -3.3321 | -59.4469 | 2026-09-03 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 13749944-9d1c-3619-975d-2faa6b4ef8e7 | -7.2933 | -60.5905 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 4d9bde69-4481-3f1c-9ddd-bc8579749712 | -3.7645 | -61.7548 | 2026-09-03 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d68fe49e-02cf-3411-b858-1f8ea8ab7973 | -14.5627 | -52.077 | 2026-09-03 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 82527d00-935f-3bb7-8a25-bc66171b5ec5 | -8.6854 | -62.9118 | 2026-09-03 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d8d43822-46b8-3839-9c3d-9786230e250d | -8.4677 | -54.6429 | 2026-09-03 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 4607be7f-c049-3f21-81b2-fd2fcedbdd07 | -6.7692 | -58.6679 | 2026-09-03 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 41b2066f-3b7c-3be3-8fab-076b3cbff89c | -3.4002 | -61.3276 | 2026-09-03 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b964d3a6-c5f5-3447-8a95-e7f3b70fb7ca | -6.6015 | -58.9651 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1a90ca49-2701-3783-98cc-b1253b85ec3e | -7.3118 | -60.5897 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 95521ad1-0a05-3d4c-9f91-72af91490ab7 | -3.0347 | -61.4657 | 2026-09-03 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 581a7da5-95c9-3a89-bfc5-96aa154c1683 | -8.7599 | -62.8332 | 2026-09-03 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| db091c2d-4a05-35b7-b4e2-d40d00ec4c77 | -9.4816 | -60.4131 | 2026-09-03 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ba73a491-be4f-35fc-ba72-c98d1e872421 | -10.1321 | -45.8825 | 2026-09-03 16:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 9c4dad95-14fc-3fbc-b568-7e472f5a1750 | -3.1449 | -61.1808 | 2026-09-03 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 373779a4-7252-366a-bde0-75ee3c1ebb74 | -17.0881 | -56.8328 | 2026-09-03 16:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| b13808ad-753a-31ec-b323-6d7d7c5eac0b | -3.1267 | -61.1811 | 2026-09-03 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 746dc4fb-30b0-3968-992d-d1c5c233d40c | -6.6226 | -58.4995 | 2026-09-03 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 1a868d2c-9d65-3844-a4cd-bc687b1d0759 | -3.1266 | -61.2 | 2026-09-03 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0f4b234d-75c4-3041-9ea7-16a4b7dc2dd4 | -10.6473 | -61.7549 | 2026-09-03 16:00:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a06b71f1-e832-3899-a564-acde265ed9fa | -10.5467 | -49.9973 | 2026-09-03 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8419b4f7-718b-30b7-95dd-c2ca52cbd783 | -14.2989 | -51.7072 | 2026-09-03 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f5c9bce2-6491-34e1-b5ce-488205a90d7d | -13.8384 | -54.0158 | 2026-09-03 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6c7bdf34-bc63-3a4f-9c80-ca54e271f0ac | -9.4812 | -60.4709 | 2026-09-03 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| b371911e-4812-376a-91b9-1e0caeff07e9 | -14.5631 | -52.0557 | 2026-09-03 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4ba38391-6fc4-3012-9594-1e1ed65d4cdf | -6.1294 | -57.6833 | 2026-09-03 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3d283e85-8f56-3139-83f9-b9bf94eb8c3b | -6.8599 | -58.9351 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3b417996-720d-3ca1-b3e3-923ff7e2fd9b | -6.654 | -59.4645 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| a98d290c-1fff-379c-a6b1-a8a9ddefaf37 | -3.0347 | -61.4846 | 2026-09-03 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| dd98903f-d82f-3690-906d-8e2362c10cce | -3.4003 | -61.3087 | 2026-09-03 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9207f472-0be0-3387-b93c-cdd73443d620 | -13.4005 | -51.3756 | 2026-09-03 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 04f131f1-8be4-3187-8687-e887a0c089e8 | -11.5373 | -50.9576 | 2026-09-03 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6bc62cff-4e1a-38a7-9c12-6827bd8ac80f | -17.0875 | -56.874 | 2026-09-03 16:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| dfc201b5-d0b4-31ef-b35d-4da38fcbd30e | -14.6728 | -53.5618 | 2026-09-03 16:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 072430ba-b3a0-32f1-bb53-fffd9973779a | -8.5728 | -63.1807 | 2026-09-03 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b08ffcad-3683-31d5-82d7-49fc75c4d125 | -17.1227 | -55.9402 | 2026-09-03 16:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| bdbdf973-988d-3b3e-a737-18db5617652c | -3.6215 | -60.585 | 2026-09-03 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| cde237c7-fbc0-3f87-bb8e-c3ac8ab531ae | -10.2915 | -68.8411 | 2026-09-03 16:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9756962e-99aa-3e35-a73b-1ff3ba65871d | -10.1134 | -45.8621 | 2026-09-03 16:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6b97e47a-dee0-353f-ae3f-2d93e985aa4d | -7.5326 | -60.7147 | 2026-09-03 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ebb87d78-f808-3e48-9a08-62ea94c01e95 | -7.0243 | -59.2181 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 818d2839-48d1-3e22-86d9-451f8c4807c5 | -6.7453 | -59.6341 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 4e0bcd3c-645e-381a-a85e-791c19522e26 | -10.8028 | -50.6326 | 2026-09-03 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cf0e6a16-ead1-33ff-bcf7-624bbe9d5afb | -10.6472 | -61.7741 | 2026-09-03 16:00:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 754d899a-35f6-3740-b14f-f7cc0737463b | -6.6937 | -58.9613 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 76884bbf-360a-3232-acb0-0fea25792a3b | -7.0428 | -59.2173 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3a4eda7b-9937-3374-bc80-c7517286f9dd | -9.4814 | -60.4324 | 2026-09-03 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f40a0376-06f9-3897-82c0-3cb1a1434474 | -10.547 | -49.9758 | 2026-09-03 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| cf089be8-90ef-3186-8f14-a1ec6656a311 | -8.3718 | -62.697 | 2026-09-03 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 6ac8488f-6e64-31f1-bd66-51f1180986c7 | -9.4813 | -60.4516 | 2026-09-03 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9ac23e01-2abc-3e8b-9e19-2d2ace581b74 | -14.4846 | -52.1299 | 2026-09-03 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1a5d0ee7-5815-30c5-b285-495a9ad89d8b | -7.3117 | -60.6089 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8c14a960-5e57-3cef-832f-d2434de07dcb | -3.0721 | -61.0685 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 524e16cb-8b8a-3d5a-8e02-502d99836eb4 | -7.5326 | -60.7147 | 2026-09-03 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| afbd7735-0687-3094-8aec-55557525336b | -7.0243 | -59.2181 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e449d255-dadc-3eac-870c-0815337bdc51 | -3.1267 | -61.1811 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 10817fd1-85b2-3a10-b56f-fb60be5aa75a | -3.1084 | -61.1814 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 083f089b-63d8-3e3b-a2f5-39e8a1bc98e5 | -10.2915 | -68.8411 | 2026-09-03 16:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 3c878c83-a140-32c8-8647-2d1ca8ace682 | -3.4003 | -61.3087 | 2026-09-03 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8ad01e21-2933-3217-806a-e061c732985e | -5.78 | -57.5605 | 2026-09-03 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6e0291cf-b815-34fc-b936-6094f938042f | -8.5542 | -63.1814 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3b876a85-9fe0-3241-97ca-ea64ff4cf0ce | -3.6398 | -60.5656 | 2026-09-03 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ec5b3757-5c77-325b-bf84-7ec9c9fe9442 | -7.2932 | -60.6096 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 064e6a19-c374-36a6-ba32-b182a218b243 | -8.6854 | -62.9118 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a855a9c0-4a04-33b4-95da-2bfe6c3d28d8 | -10.651 | -50.6697 | 2026-09-03 16:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 97e468b7-0681-3b9e-b915-2646610d2b41 | -15.287 | -53.8407 | 2026-09-03 16:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 8f58324d-9457-3f4f-b502-b6410eb49c61 | -9.4813 | -60.4516 | 2026-09-03 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 2c2abb30-27eb-3ebe-b400-4ea66ddf1bcd | -7.3118 | -60.5897 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6f0e6f78-2520-30d7-8994-7da91d24cec7 | -10.1653 | -50.2719 | 2026-09-03 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3fb55db1-ce9f-3306-b7b7-9e4b4718fa9e | -9.4812 | -60.4709 | 2026-09-03 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f64a2f3f-e108-3d06-a8cc-95ebd80451a7 | -3.7645 | -61.7548 | 2026-09-03 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fbbe2f20-ea6e-32c4-9337-a5fbf566000f | -6.6357 | -59.4459 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 227.2 |
| b204ef73-4d47-3d0c-a741-cccdb082ad18 | -3.3321 | -59.4469 | 2026-09-03 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 7a1bef21-0103-39c4-8602-5f6bec331273 | -8.6853 | -62.9307 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3120dedb-b1e2-3d48-b067-f89ceb203bfb | -6.7463 | -59.4416 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 212.3 |
| e5bc1277-c611-39e6-9c87-0018abb57484 | -17.1227 | -55.9402 | 2026-09-03 16:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 57843ae8-08ac-35cc-bc9e-088e0fdbd550 | -10.1273 | -50.2971 | 2026-09-03 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 995f20be-3b86-3ef7-a748-4094ec2759f6 | -7.0058 | -59.2382 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a5107b2d-0af4-32d4-82f8-7f786d3098a7 | -14.3818 | -52.5039 | 2026-09-03 16:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1eebe328-f591-399e-b29f-58399a09e833 | -15.2866 | -53.8617 | 2026-09-03 16:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b964065b-66da-3ee3-8f24-4c277b0d37b9 | -3.7828 | -61.7545 | 2026-09-03 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8fefc786-e5f2-3c07-b692-72a8bcd17f01 | -15.3061 | -53.8592 | 2026-09-03 16:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 70496660-3d0b-3a9d-9736-23bc1f7169bf | -8.5728 | -63.1807 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4065b969-d6dd-3254-a111-9918752954b5 | -5.9451 | -57.6906 | 2026-09-03 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8dbbccbe-781c-326b-a06f-5ce1c09b7507 | -17.0878 | -56.8534 | 2026-09-03 16:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 217.2 |
| 8b52985b-0a37-38be-9e51-c5d455f0427e | -3.4002 | -61.3276 | 2026-09-03 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| fef4b5cd-1bae-3038-bda3-a9d5419d632d | -14.5623 | -52.0984 | 2026-09-03 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 849d85f9-040f-3616-8bbc-e6d9b5f90ec5 | -6.6727 | -59.4252 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README70.md)
