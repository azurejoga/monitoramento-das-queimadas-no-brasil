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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c629e9a-b73d-33be-82f9-9ff41fbe1419 | -11.59814 | -48.55574 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f58301c9-be79-3e87-8d46-4bdaa38564d4 | -8.41005 | -46.25513 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40368b66-c435-31c1-98ea-485cac0a53fc | -7.50357 | -46.64039 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a39d6314-9f55-337c-899f-fddd744b9bd4 | -7.9505 | -44.13227 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ab4284a-7f9a-37c8-a045-c2f250e14735 | -9.15724 | -46.86716 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8061c013-22fc-3b10-93c3-a79b70519d23 | -7.48299 | -42.75791 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 353f7122-be55-3b49-ab0c-95aee4be9130 | -8.19802 | -47.01257 | 2025-10-16 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02dd7644-b0ef-3ed7-860a-7fe0dfa173c4 | -8.28753 | -43.40127 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e31082ee-23b2-37e6-84c4-0ca940ae2b92 | -10.62693 | -45.251 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0fac993-61f9-38cf-9d63-0b9f0ad0a203 | -10.33324 | -45.17448 | 2025-10-16 05:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95dacb26-c037-3b7f-b7c4-434aeab97f0c | -7.07883 | -44.95028 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89007a5d-f9a2-30a3-9e7f-5101c560670a | -8.28829 | -43.39531 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9194f007-0023-38ab-9afd-0726f9f930a2 | -11.5086 | -44.06757 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86bb58c8-f73f-3b27-b3ca-b8822f8c7a9d | -8.26494 | -43.36134 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 40c03792-4445-34fc-996d-5687e7d05702 | -5.68909 | -45.09565 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5813c498-e26d-3840-af35-bd3d7efbb40d | -8.23938 | -44.03238 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba5f32dc-e9c4-36d3-b267-ae805e06fa42 | -6.5201 | -42.1907 | 2025-10-16 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b622907d-f9ac-3ca1-b616-645fe9878f00 | -10.65637 | -45.25294 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc40ca81-a609-3394-b68c-5e8d3e41c8fd | -7.34802 | -43.85965 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8594e532-baa1-35e5-ab0b-9e4d637192fd | -5.72403 | -44.52578 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c177434f-f6e7-3bcc-819b-f9aff918ece6 | -9.08967 | -47.95166 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 84798a32-3783-3858-b89a-b7194bb9dc1c | -7.17672 | -42.19853 | 2025-10-16 05:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 213723ec-b063-3f26-85ff-790f074f1ec6 | -6.74877 | -44.36995 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a0c5263-224b-3ee3-85fb-ce4da2c82693 | -4.41167 | -50.31664 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c17deca4-26c7-3a0c-b7a8-d36147353fe4 | -7.9318 | -44.12443 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 43247d35-b4f1-3a23-8167-ae51f6dc220c | -7.3473 | -43.86496 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bdc9a865-16e8-36ce-a3bf-d3c8c1164b11 | -10.57687 | -50.90395 | 2025-10-16 05:08:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01a60def-7f32-3d16-a756-2c20258f183d | -8.24063 | -44.02643 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd617fad-9e66-32cb-85e2-d89977c082cf | -5.30488 | -49.57265 | 2025-10-16 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 27fdf92b-d5b5-3d95-aceb-dbc029e7ef2f | -8.39087 | -46.25143 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83016785-aef7-37f8-adcc-996d03436626 | -5.47357 | -42.9326 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 69d8b7e3-1e7b-3784-9b34-e8eb4b082c1c | -7.93036 | -44.13519 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9975f01e-26d6-36b5-8366-9f90c141cd92 | -7.3408 | -43.86386 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d687a534-4a14-371d-840c-160daec34b24 | -10.88637 | -47.93475 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8948420-11a4-3aab-a0fd-5c3db2bb2b4b | -10.6469 | -45.2436 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2145f60-f321-3f64-b337-7e547dd69e5a | -10.0525 | -43.84155 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4109c782-a4b4-3f53-b29a-15a501b0d8ff | -10.80789 | -47.92844 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 648e67e2-858b-30b6-8e6e-649ca7c8a704 | -7.92429 | -44.12885 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 305a9055-185d-397a-87b9-4e6253066430 | -4.84976 | -48.77168 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a67ea3a7-5a8a-358c-bc30-2251bbdd1b88 | -7.60971 | -46.48026 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b48e939b-a321-34fd-a239-01fd9134133e | -8.20388 | -47.00986 | 2025-10-16 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 084671d6-675d-3439-9a99-f30870a58525 | -7.10932 | -44.72605 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20955891-1e8a-3acb-b4e2-6a917a93a2dd | -10.88893 | -47.91497 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3df25f0d-dd4d-37ad-8306-657ef72245a5 | -5.68435 | -45.10571 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6630bae5-dd42-3cfd-8327-479c40625f2d | -7.94903 | -44.14317 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b926a7cd-dce8-363c-b3a2-98591eb2888e | -8.81386 | -47.3056 | 2025-10-16 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 948f6c68-4ff5-379a-b28a-2c02cd45d87f | -5.32757 | -43.94678 | 2025-10-16 05:08:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ab21821-375f-353d-b61d-cb9ea54dcbe6 | -10.6189 | -45.24794 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76742d2b-6845-3358-bea3-97857f87e168 | -6.94737 | -47.74501 | 2025-10-16 05:08:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c68d29cf-7dbf-3341-b80f-361f22bdd6df | -7.39314 | -44.74913 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 522935e9-c65b-317a-8e2f-3e4567729c2b | -11.43538 | -44.15692 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c267bd2-3d33-3d1d-a7c7-84227f53acf3 | -9.6811 | -44.50409 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb2e67db-eca4-3240-a10e-3bf0d55a384f | -8.40709 | -46.23342 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55715117-64af-3f37-887e-bb00e9fe117f | -8.29003 | -44.96824 | 2025-10-16 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 473c7104-c246-32a1-ac1a-71fa625d352e | -7.33957 | -43.86359 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ee5f1ef-0a57-3770-902a-aeea1a84764b | -8.07181 | -45.4344 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fda9080-ed95-3377-9085-3981d6f8a783 | -10.80877 | -43.93951 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b81b8a4-3c81-300a-93c2-b389769849b3 | -5.46884 | -42.93774 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 03f74f1c-7f92-3366-8de1-ddcc63c15c37 | -5.87823 | -42.81591 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23402434-2dc1-385a-b418-189114fdc61a | -8.29065 | -44.96346 | 2025-10-16 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04f5d67a-080d-3b71-9805-fc7a7c7acbfd | -5.68852 | -45.09984 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 92bf5de4-76a6-3315-b0a6-9de3f07bf7b0 | -5.74711 | -44.98249 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e86c11d6-9b03-3fc5-8a3f-bd985585138c | -8.18655 | -43.3196 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 3138bb35-e95b-3d19-b4c1-26cd6ce37e69 | -8.24076 | -43.33328 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90854384-b024-31e8-8d95-ba6116ab8fc7 | -9.69144 | -44.52057 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 517d6569-15ac-373a-88b6-53eab064089e | -5.71556 | -51.12229 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1dda3d-36e6-30d4-95c3-803e5f9c3c56 | -5.87659 | -43.86103 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3480f541-fb83-3e7d-b71e-1f3df9389973 | -6.12852 | -44.29565 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ee9c1c4-accb-3f4d-b2d5-9669144143f8 | -11.49032 | -44.10854 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49133266-81be-3469-9af7-f4813358c8eb | -9.685 | -44.51961 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7db86757-cf1f-30db-af64-80ea11ba360e | -8.39284 | -46.25386 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fc9ccbe-28c4-3b23-87df-5a0b334565db | -10.12796 | -44.55859 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a73a5087-c830-33e2-a5ae-d6ee176ec53e | -5.85371 | -43.87873 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61cca86b-be9f-3ebb-a8d2-feed100d49e0 | -7.16162 | -42.51715 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92d8de77-1b47-32d8-ba8f-bb520703993b | -7.39381 | -44.74422 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cf3b38f-1bbc-32ce-b964-e70b894848d6 | -11.434 | -44.16895 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 406badc5-279f-3fa5-b2ca-091545a1b7b5 | -5.47559 | -42.93862 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2c0a6f6c-883f-3806-a344-83a0d32963d3 | -8.20769 | -43.31686 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0b35b846-6e65-30f3-9cb7-e4870d568a94 | -11.54301 | -49.91976 | 2025-10-16 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7223c37-2f2f-372b-bc2a-54019cf6edec | -6.338 | -44.01927 | 2025-10-16 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53fabfd8-b6b2-3b22-94d9-58284c855c8d | -7.96315 | -44.13372 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ca2f95b-a683-3671-a7a2-8f52844fa9c3 | -7.41011 | -44.75026 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adc5572e-7cdf-3832-a14e-e097637b9dd0 | -9.71916 | -44.5151 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6466b11f-64b6-329c-9628-205bc32b3b91 | -9.81687 | -45.27315 | 2025-10-16 05:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4808f516-96c2-3852-ab3f-0e42083362f4 | -10.05336 | -43.84724 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c63616c-b959-3615-9b1f-9d41f17a3d7d | -4.40759 | -50.31608 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b8a5927-6929-3642-8f53-d2a9e68a7d61 | -6.32548 | -46.32863 | 2025-10-16 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5702925-d937-3e2d-8b6e-c44b355f222e | -11.58254 | -44.08261 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2968dfcd-fa9f-3cc6-9d0d-68196a5cbf0e | -9.16277 | -46.86783 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04614b9a-6f96-3857-b096-e5cd11610fe2 | -9.68435 | -44.53144 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| acbbb168-342f-35ea-8ce6-ca7d1c7dc85b | -7.92533 | -44.12354 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6bf7208-4d6c-3c30-9e94-f2128acac837 | -11.49099 | -44.10247 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a78efbc1-206c-3bbb-b005-4a74da8743b0 | -9.5976 | -63.98958 | 2025-10-16 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34a53ac8-8e98-352e-a948-d762fbf305d9 | -4.30334 | -50.40194 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8fa0f66-a358-3f47-8e04-ba6074db3ce3 | -6.12504 | -44.29059 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73995a73-4c8e-3974-b5e0-74093afa6141 | -11.58183 | -44.08871 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42cc1ca8-751d-3af3-8cd0-2c49708f9b4b | -7.93075 | -44.12976 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| facaa1c8-bbde-3f99-b70a-7098645376c3 | -6.07253 | -47.12986 | 2025-10-16 05:08:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ada043a5-47e1-3b5e-a974-247ba3e316f6 | -11.57227 | -48.55526 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 245ed227-3cad-3837-8111-c4f4b51a1d7f | -11.58525 | -44.07679 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README75.md)
