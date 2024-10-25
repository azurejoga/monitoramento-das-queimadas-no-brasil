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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e8b4582-d86d-35c6-a885-fc181886799d | -5.84581 | -47.2795 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| c741e2af-da89-383d-86b3-df726c70d2f7 | -5.84521 | -46.24018 | 2024-10-25 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 595ab455-6d92-3012-9598-0154b12b2852 | -5.84181 | -46.39134 | 2024-10-25 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d982ac38-fc87-39a0-a303-a0e7add5585a | -5.80969 | -44.49832 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6f43f006-ad07-3f55-919a-dfcca11ed471 | -5.72109 | -44.44886 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b6b1827d-ddf4-38d9-abf0-1dffb45acc0c | -5.71933 | -47.10755 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 55f22ecb-0e12-3749-b7b7-c149082b1094 | -5.7052 | -45.01553 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b1457061-a295-3233-bf18-f6fb1c282b66 | -5.70362 | -45.00372 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b3bd855b-2612-3645-8f1b-1afd9f140783 | -5.69644 | -47.34689 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6347a37-2eb0-30e5-bb56-6fce7a0a8c61 | -5.65709 | -47.9272 | 2024-10-25 00:28:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b836cf8f-41b5-3e2a-adf2-ba4bb46d730e | -5.65449 | -47.90759 | 2024-10-25 00:28:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e780f450-d409-364a-abe0-125bad224a5d | -5.65213 | -46.96324 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| edd02f3b-a9af-30d9-aebb-6cfedfe4779d | -5.64549 | -46.97021 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d3427b70-1b8a-3325-8e5b-fe1ef8133abe | -5.64239 | -46.98122 | 2024-10-25 00:28:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| aa878381-15d4-35c1-a398-23932f236558 | -5.64173 | -47.90943 | 2024-10-25 00:28:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a1070530-099a-363d-95f2-95c2fa577807 | -5.64029 | -46.96476 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d2e46c47-3ed9-3a81-b311-56c1622faaea | -5.63367 | -46.97184 | 2024-10-25 00:28:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fefcd8ff-0384-386d-9b41-75fad5fbe513 | -5.63147 | -46.95548 | 2024-10-25 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d31d8afc-3129-318e-b7bc-6fb1c164b464 | -5.62908 | -44.82892 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| f8ff52cb-de98-3952-a8c1-430942f6c3c6 | -5.61908 | -44.8304 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4a0e08fd-5024-3e4c-9b59-7dd7b398c323 | -5.61182 | -47.26828 | 2024-10-25 00:28:00 | TERRA_M-M | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4041baad-cb54-3c44-a399-105a7c56619f | -5.58671 | -44.42947 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 38437b71-0c04-3782-8464-8dde991080a0 | -5.57508 | -44.88334 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3076027f-31bf-3937-b9f2-c6a694f63a6f | -5.50647 | -44.82872 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 166df697-e002-318c-bddd-25b06c193d2a | -5.45839 | -46.35207 | 2024-10-25 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cbfd52ff-84b6-3188-b55e-93f0d3da7bcc | -5.43928 | -46.29483 | 2024-10-25 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| eab8f448-efa6-3599-80e0-0e75e31b24a2 | -5.41814 | -46.56975 | 2024-10-25 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0a9eb693-168a-3faa-ac00-d14ae672ae65 | -5.41792 | -46.56056 | 2024-10-25 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 2f25bc98-d44f-302f-9d59-34c1475bf53b | -5.41619 | -46.55467 | 2024-10-25 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 586f9543-6129-3222-82eb-bb144210e461 | -5.35589 | -45.44116 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 82175596-604d-3220-9e80-8f408d65a292 | -5.35142 | -45.43586 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| faa63500-8d18-318b-a45b-d00418bebe75 | -5.34548 | -45.44271 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c3ba6a89-255a-3797-9cb9-56340f404d3d | -5.31714 | -48.5066 | 2024-10-25 00:28:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 18.2 |
| af8b3d5d-37fb-35ae-889c-f36cc41cba57 | -5.28073 | -45.51537 | 2024-10-25 00:28:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0a028710-c8be-3cff-adf9-6253d0dba0e1 | -5.15853 | -45.28528 | 2024-10-25 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c71d9e97-0df2-3c43-a1ea-5618deb7ff6b | -5.11593 | -45.18621 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aba9ca4a-da7f-338e-a9aa-e06a1eb08b1e | -5.1143 | -45.17429 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cb0e02dc-f5a6-3aa0-8ac7-39e539adc958 | -5.11227 | -50.72287 | 2024-10-25 00:28:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ddc1622f-dd8a-3cd1-b066-c3fab6ad8037 | -5.10593 | -50.71864 | 2024-10-25 00:28:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 8fb5aaa0-2353-37d4-80bb-fcb8235224b8 | -5.09106 | -45.83715 | 2024-10-25 00:28:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 950272db-0f5a-3ef7-8f10-cad56712fac1 | -5.08931 | -45.82415 | 2024-10-25 00:28:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 07642ace-c3eb-33a9-a96f-54dd28ff1af5 | -4.98434 | -45.49064 | 2024-10-25 00:28:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef162bb2-2477-3e3d-9f2d-29e9d8f0f77a | -4.94946 | -45.54657 | 2024-10-25 00:28:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8f231221-dc95-35a6-8c5d-28c174619b95 | -4.92539 | -48.51485 | 2024-10-25 00:28:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e6650e2c-0e51-3346-9047-b9b4ce522832 | -4.92171 | -49.84406 | 2024-10-25 00:28:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0477022a-ce1f-35cc-8d30-38659bb4c045 | -4.92149 | -49.85069 | 2024-10-25 00:28:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5023aa9a-acfc-3257-93c8-950e199fa6c5 | -4.92149 | -48.50904 | 2024-10-25 00:28:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 80ab8678-3a7e-398c-858b-4c971e92c0e8 | -4.91833 | -49.81718 | 2024-10-25 00:28:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| f24a5038-a637-3353-8975-77a6f907bcdc | -4.9179 | -49.82378 | 2024-10-25 00:28:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ce0cbf17-453b-3362-aae4-5cc68e3b3ef8 | -4.85089 | -45.04265 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 91fc2ec4-13a9-3019-83e0-e0fa592280d9 | -4.84936 | -45.03114 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 736aa0bf-c50b-34b0-a8f0-f718fda695ca | -4.76919 | -46.42752 | 2024-10-25 00:28:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 4f80f3fb-596b-33ef-ab95-d99190096290 | -4.76729 | -46.4131 | 2024-10-25 00:28:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 4e515e1c-4ad3-307d-957f-14d9337bc2ea | -4.73766 | -44.95943 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e786dcc-7ade-3189-b2af-bf08dd593da8 | -4.7365 | -44.95374 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c5f3240d-eb61-38fa-9938-f04d63a4d9f9 | -4.73615 | -44.94806 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| da5bb81b-6303-33b4-9b61-2ba01d530cf9 | -4.72649 | -44.95491 | 2024-10-25 00:28:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fff328f8-d213-375e-83c4-69bd0b88d18d | -4.70445 | -44.63405 | 2024-10-25 00:28:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9623384a-1ffd-33b5-883c-27bf90bb3be3 | -4.67457 | -50.97651 | 2024-10-25 00:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 788ab317-2118-3e96-af6f-81b194c74058 | -4.66398 | -46.07538 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 87f509be-2ab7-3d7c-8ad2-a2cac28af03d | -4.66218 | -46.06207 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d2fb419f-fcb4-3d14-8190-bce16c04508b | -4.61038 | -46.70269 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 466a1d71-dc03-396c-b8f2-bc6d3a9016e1 | -4.23781 | -48.56245 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5e4ba620-4941-357a-b4ac-6aee9c5a4d39 | -4.60692 | -45.81296 | 2024-10-25 00:28:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d1662e82-5afc-377f-9983-54e2fe46c14a | -4.59805 | -45.82742 | 2024-10-25 00:28:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 06df4f8c-17df-3c7f-8a74-38b027f46241 | -4.59631 | -45.81432 | 2024-10-25 00:28:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| f5975cbd-f277-34f1-9585-a26de620e353 | -4.58456 | -48.01564 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 1d35b270-0841-3f2b-9f10-c306b4412131 | -4.58412 | -48.0214 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6af4c241-6dd4-3eb7-bf1c-d24f80b69df5 | -4.5815 | -48.00211 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 901d7213-43de-38a0-923b-24dcc348161d | -4.57145 | -48.02309 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3e1bed8e-0f8f-3999-b654-bb36e9946e25 | -4.55881 | -48.02492 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f22a784c-0f99-3801-b732-b948115934e2 | -4.55622 | -48.00552 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 11d2d6e2-b854-3657-8cbf-6919dd977ca1 | -4.54586 | -46.04337 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 068f2787-c2a4-36e7-b78c-60bb3659c72c | -4.54406 | -46.0299 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 0157ad3e-3ba2-333b-acee-32e43fcb30d8 | -4.53506 | -46.04468 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e5cc4e7f-88ff-31ce-ad42-1c0d2c0e4a11 | -4.53329 | -46.03133 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| de967e0b-8097-3f99-954f-ae33e9fcbf66 | -4.51883 | -48.21583 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| fd759a6e-ba6c-387c-83e3-b8cb37d6a806 | -4.51799 | -48.20939 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| aece538c-b714-3e6b-b823-fc164c2d5d76 | -4.50595 | -48.2174 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 77d68bea-7ff3-3d55-880d-80337a2bc582 | -4.47914 | -47.73855 | 2024-10-25 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b6fc0c15-5f2d-3b0c-a35c-4180a7cb3b03 | -4.46957 | -47.73329 | 2024-10-25 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 6d6be651-b42b-3ce4-9d66-54cdf52bbfb2 | -4.43175 | -45.79629 | 2024-10-25 00:28:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0ed3136a-f4a3-387d-976a-9a4ec88f10f1 | -4.42999 | -45.78329 | 2024-10-25 00:28:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 9c9d54e8-1ad0-3f1c-b2b1-4a99918b4173 | -4.41948 | -45.78498 | 2024-10-25 00:28:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 61a1d9ef-1936-3035-8ac0-4260a73ac034 | -4.39226 | -46.61341 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7dccbc83-eff7-3076-acf6-d62b1004bf8f | -4.35268 | -45.97279 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7ed607c3-5e50-397d-a794-653abadbae7e | -4.25101 | -48.56089 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2211123d-43e7-354c-8f85-a9b63239d6a4 | -4.24958 | -48.35148 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 05903b9f-1b53-3ab4-a8c1-78a38e5f1f20 | -4.24819 | -48.53964 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| f314a603-d6ab-3578-8dca-9c72918244c4 | -4.2468 | -48.33091 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7d7f7317-67de-3956-a0b0-034f59039d58 | -4.23508 | -48.54164 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 19cee980-25ae-3003-a5f4-268705eddf7d | -4.23451 | -50.63637 | 2024-10-25 00:28:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 4be62636-64f6-3bc3-a461-241678fb6e2e | -4.22465 | -48.56427 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| be1946ff-7710-35e4-9a72-5a5aa3a0ecca | -4.14891 | -46.84798 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7d24bac5-1eb0-387f-baa4-590cca8e390a | -4.14675 | -46.83229 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f97c6b15-e868-338f-b22f-7997617fe08f | -4.13986 | -48.41342 | 2024-10-25 00:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 23da0313-7fdf-3c79-9f45-7c3380f2cb13 | -4.09709 | -46.03951 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a129cb74-03a6-3095-9727-4ecfc6dc03e3 | -3.98242 | -45.50092 | 2024-10-25 00:28:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90d197d9-dc2a-36ed-af2a-06dfd8f8e59f | -3.96802 | -44.06331 | 2024-10-25 00:28:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9ec73171-94a2-373f-8d2a-90565bb4d919 | -3.96663 | -44.05333 | 2024-10-25 00:28:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README7.md)
