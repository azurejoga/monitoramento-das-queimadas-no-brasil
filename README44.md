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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f204595-91f4-3f61-8cc0-309ffbcb8bf2 | -11.25246 | -61.17303 | 2025-10-12 05:55:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 122a4fc2-7b52-30f2-a147-e9fe1d49a4ab | -10.88508 | -69.39198 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c16dda-ba15-324b-9cca-a6e0ecbebc3c | -8.41894 | -70.11414 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69512d3b-2828-31cc-9b44-e344792afc1c | -10.84293 | -69.00608 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e7b8b6-a9e9-3f26-9065-277f3d900830 | -10.63623 | -69.34831 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43281127-e418-3eff-b25d-60291c266bfc | -10.73435 | -69.44309 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 941c85fa-8ad8-3605-932a-9ec8d434047c | -15.15536 | -56.80804 | 2025-10-12 05:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 656b5a7a-b9e9-34ee-9521-12fcf44b09a8 | -10.69558 | -63.47334 | 2025-10-12 05:55:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02b6f65-ecb1-382b-8c62-aaada598a505 | -9.80528 | -64.48648 | 2025-10-12 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9db963ad-ba19-37d1-9f11-49c9c7033e01 | -9.32922 | -68.98256 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03651a07-a8c3-3dda-973f-c6e590cd9dce | -9.41578 | -63.20542 | 2025-10-12 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26bc55d8-d005-34ea-a7ab-44993d91a4a9 | -10.88298 | -68.41573 | 2025-10-12 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f430868d-fdac-3662-b58c-c2a62af99c6c | -9.24099 | -68.67617 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8625e9d5-6d6f-399d-a02c-35368e4e119c | -8.7296 | -67.05848 | 2025-10-12 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 723427f1-71a4-34fe-9b36-7fe1f7b8a61c | -15.28978 | -57.08603 | 2025-10-12 05:55:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f1efc2b-8fed-3ff7-a870-9a18c2d1a250 | -12.21261 | -64.37106 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8db9b189-b033-39a8-9566-5c18bfc19941 | -9.23715 | -68.67914 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec61b29-f0d9-3889-a530-465fa5086e37 | -8.66105 | -70.02597 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff24fd5a-db57-3de8-a333-7f0a96e77a57 | -8.27337 | -70.82832 | 2025-10-12 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49065020-86a1-3fe9-ad1e-1ce369449d55 | -8.7254 | -69.87713 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e954a4f-e9fa-3278-9450-4dd632117388 | -9.01936 | -67.43826 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c7e149c-4e87-3221-ad53-bd0be0efc6a3 | -8.66494 | -70.02296 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 718f9a43-4d36-3a34-9b92-81d40d41fae2 | -10.48868 | -68.08232 | 2025-10-12 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 090c8714-2917-3ffa-899e-d6e9648a8a57 | -9.0233 | -67.43512 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa0fef8d-cec1-3015-bcd6-1cb5fdb07b80 | -9.76277 | -65.05223 | 2025-10-12 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 752ab290-9d0d-3849-959a-16b44c0bfe8a | -9.01881 | -67.4419 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27c1532b-9711-3b38-b125-b5f147d444d6 | -11.25211 | -61.17015 | 2025-10-12 05:55:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 712f119e-2175-3489-b8f6-ce28091f31d0 | -9.02274 | -67.43877 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05a9355a-00b7-313d-827b-74216f23c226 | -9.11681 | -67.32876 | 2025-10-12 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6719f8b5-b8bc-3b83-8dd2-d9013a5ad076 | -9.762 | -65.05396 | 2025-10-12 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ff8cd05-db91-3255-96b9-77474071ec63 | -10.6534 | -69.1081 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c570f74c-bf8b-3e47-b234-c68c621b9166 | -12.20954 | -64.36296 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e598d85-de81-3a6c-b83d-2247f8917eda | -10.89446 | -69.4185 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b57517a2-608f-3d99-bd6c-570fff8e33a3 | -12.29489 | -64.02722 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd2d0259-3385-3229-a9ff-ad7c4258ff00 | -10.72226 | -69.49477 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8890c48-a884-3f7d-9c33-df401d5bdb96 | -8.66438 | -70.0265 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cd5e9d0-1c40-3235-b862-e80a75e4c011 | -12.4324 | -64.37431 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7876884c-85c3-3ba1-bc09-6306cc285f04 | -11.25284 | -61.17012 | 2025-10-12 05:55:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf6c1137-f9bd-3b3e-981b-ca90423a8514 | -12.39697 | -63.87771 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f67a4ba-6875-3c16-a41e-8a3cb7fc6534 | -15.15476 | -56.81446 | 2025-10-12 05:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5d3ce804-2d57-3134-930e-0daebf9b7d3d | -10.63818 | -69.51348 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc681b8d-794a-3567-a9cc-aa8af9bbb242 | -8.43338 | -70.13104 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80d5412-f292-38bf-a316-5e7f2fcda467 | -9.05116 | -69.60338 | 2025-10-12 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 944825b5-ee17-3efa-b607-6bd6588f5538 | -9.90598 | -68.97083 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ca3fbd1-8040-3b69-882c-f5c576664e98 | -8.60591 | -69.75024 | 2025-10-12 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d33469-c3b9-3d6e-9335-63858f1aab80 | -10.73326 | -69.45006 | 2025-10-12 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62f4360b-123c-3711-9a67-77481ed4b003 | -10.48084 | -67.83969 | 2025-10-12 05:55:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 674298bb-2542-375d-bb41-526d28cddbed | -12.21365 | -64.36357 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc08cd4d-b9f3-384f-b34c-df80658a0f16 | -10.64016 | -69.3495 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5ee0ecb-dc7d-3873-b6a0-792618a8996d | -10.79626 | -69.30645 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12449b40-203d-3334-9fcb-87ffc5659c96 | -10.65286 | -69.11158 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51ef1c36-68ef-32b9-8c9b-98cb5d342b3d | -9.24045 | -68.67966 | 2025-10-12 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9872c2a-6ab3-3fe5-a873-70332c8fcfcf | -12.21416 | -64.35983 | 2025-10-12 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f28ef715-3917-3406-88fb-9effec76e9a5 | -10.64147 | -69.51401 | 2025-10-12 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f16ec556-c316-342b-a7c7-79ecad7540ad | -10.88703 | -68.21064 | 2025-10-12 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6fb1d61-cf54-3555-bff2-87dd834b3f25 | -17.83034 | -57.66566 | 2025-10-12 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7a91bbbe-b99a-3a38-b9e3-a727cf78ca16 | -19.04035 | -57.54392 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2e42d8d7-5e4d-33e6-a6ba-3d2567ab6053 | -15.8801 | -56.76318 | 2025-10-12 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c3f1f0-2ff0-3ac1-b788-542eef11ac88 | -19.02646 | -57.5424 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c6f269d8-8eca-3b04-9500-7e70d3e64a58 | -19.02699 | -57.53556 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 22e23d3f-3d24-321a-8c0e-b6070660f4e2 | -19.05423 | -57.54546 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4ed2c301-af5c-3204-a2e5-684dc1499714 | -15.8786 | -56.76019 | 2025-10-12 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e8f05a6-cf52-3b0e-a365-245fbeb22559 | -19.04764 | -57.54716 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8b842b59-6bfe-3a4f-80d3-37980cc43b11 | -19.03432 | -57.53889 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 628c3e7e-052e-3afa-9d8b-8a466428dce6 | -19.02738 | -57.53813 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e198e7ff-213e-326b-85a4-c78b5d9d859b | -19.04127 | -57.53963 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 10c6839c-c0cf-37eb-b17d-e94669cf193b | -17.81499 | -57.66739 | 2025-10-12 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| de45508a-7496-3e29-9985-e6f85007fd31 | -19.02682 | -57.54495 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c00c2905-d8ae-305a-a8e1-27ada743fb69 | -19.05458 | -57.54788 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9151b06b-e941-3f27-aa69-a497af598c2d | -19.0407 | -57.54641 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f9bbd75d-5426-3786-93dd-dc27f2bb67c8 | -15.87155 | -56.7596 | 2025-10-12 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d61ba34-5f7b-3c44-897c-86624d3ab7fb | -17.823 | -57.67101 | 2025-10-12 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| abdc324d-9ec1-3fe9-a8dc-b1e28a61a520 | -17.82344 | -57.6659 | 2025-10-12 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2944ac38-5ff4-33d3-b594-a21c70dce5a4 | -19.04729 | -57.54468 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3955cfd6-cc1a-375b-99d6-0b2095c1e0ee | -15.87305 | -56.76263 | 2025-10-12 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b360487-9536-301b-a6b5-3e896c1d761e | -19.02595 | -57.54921 | 2025-10-12 05:57:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5be07a03-751e-3016-b813-ffaec7b7c53a | -15.88076 | -56.75634 | 2025-10-12 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c5264ee-a015-3938-a817-c009fc91f908 | -17.81653 | -57.6663 | 2025-10-12 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| aaade253-791c-31ff-8768-618a2ca5202a | -10.88411 | -68.41482 | 2025-10-12 06:25:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08df3d1a-200b-3113-a223-557d8ed3e69e | -9.01409 | -67.44216 | 2025-10-12 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7afa281a-e9f7-32cf-85d3-e2c61e6182e7 | -8.66303 | -70.02802 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db9e94d8-a643-3cad-a786-168f9402cdd8 | -8.65889 | -70.0274 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1db1ae0-f114-3ef7-b459-cfaf2fa34817 | -10.72156 | -69.49596 | 2025-10-12 06:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc995a1-729e-3975-8e0d-af6870853a93 | -10.63873 | -69.51262 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61f79bfb-6ee7-33d7-ae3d-eb1b9635d9cb | -8.03591 | -70.13728 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af059716-4d8a-3854-bdee-a7d681f63f2d | -8.65942 | -70.02367 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62b4c932-828a-365b-ac4a-bc8d4b399ba7 | -10.63858 | -69.51073 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| defeabec-41cd-33ea-ad89-9d90916ff95f | -10.63801 | -69.51505 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed081d43-2d06-32ac-8b2f-e989ae40cfed | -8.7264 | -67.05859 | 2025-10-12 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7a28de3-29d4-307f-8abc-4d9d0137ef24 | -9.01484 | -67.43652 | 2025-10-12 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b552288-f765-3246-bea8-f75ac7974a8d | -10.79517 | -69.30733 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a6accb-6dab-3891-8cb0-374d1b4cad33 | -10.73326 | -69.44432 | 2025-10-12 06:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cfdee43-54b4-30f5-b3ad-c68e90b4863e | -10.64313 | -69.51329 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77a2b094-5244-3ac0-bc11-1d5499dfa569 | -10.64299 | -69.51141 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2496756-0661-3093-98d1-9c3149b2edea | -9.0198 | -67.43724 | 2025-10-12 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f345b8ff-d98a-3bfa-b3a5-3ff2e959a3a9 | -8.60266 | -70.19294 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f45c4b0-8e8d-31ea-9eb2-906f3a3aac72 | -9.01905 | -67.44287 | 2025-10-12 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23ac68a3-862e-3f74-b5ab-7d6a1ef0e161 | -10.73265 | -69.44867 | 2025-10-12 06:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b52679ea-2826-3001-acc5-96ad8f1d08cc | -8.60332 | -69.74866 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09141db7-9309-3300-a1b5-f97cef781672 | -8.66355 | -70.0243 | 2025-10-12 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
