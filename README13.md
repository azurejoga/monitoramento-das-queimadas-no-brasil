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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e9bffb3-cb93-370c-b7ac-c0a93852cb98 | -6.45133 | -45.75447 | 2024-12-10 03:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d336a70-123c-3195-b48a-99a986792fc0 | -6.89771 | -47.84633 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6be4dfae-e500-3773-8aeb-a5eb012213d4 | -5.91388 | -48.0655 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 25f90be2-3f86-3c92-9e5c-6a4944d95cea | -4.14481 | -49.31426 | 2024-12-10 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a4d104-2162-3339-b333-babc33a17b0b | -6.72618 | -46.28966 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01b1870c-4b18-3b59-afc8-5cca1099e184 | -3.8344 | -52.35394 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e243addc-9b0f-3052-bc8c-87587ed12ba3 | -6.15946 | -35.27523 | 2024-12-10 03:57:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f46ee475-e05f-33ba-ac78-43dba6d35388 | -4.60403 | -48.50169 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8edaf437-b2e6-3f5c-a9f7-c87675a6f76f | -2.91276 | -52.96407 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 29b003aa-e07a-3167-abbe-46588a15d2ca | -5.7677 | -47.87151 | 2024-12-10 03:57:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feebae3d-99ec-3f38-ba0a-10bbeb750145 | -4.88922 | -48.05492 | 2024-12-10 03:57:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 094207e7-6726-3cac-afce-98d5b321e5d1 | -5.62785 | -44.84153 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d339e2d0-5a01-34f7-8a95-98b98ca2b39f | -6.73119 | -46.29242 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac1047a7-347d-3e14-b017-4eda38f9d2e2 | -5.58025 | -45.20688 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8927b775-ad5e-37ba-9136-0743d62007c6 | -2.83956 | -40.30213 | 2024-12-10 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 118509b0-0f23-32e2-b45c-d5cb693e1074 | -4.56185 | -48.92179 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4406487-929d-3d9a-b0dc-ffb958355239 | -5.34232 | -40.8619 | 2024-12-10 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2a4bf69-9b09-3a34-911c-cbe709eeab12 | -5.50934 | -46.25922 | 2024-12-10 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfd11b5c-6c51-3459-963b-e4ec8ef0bea1 | -3.32829 | -45.59727 | 2024-12-10 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec222156-9685-32c0-9468-bfbd942ea1a8 | -6.94686 | -42.84965 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb50382b-8a8a-348a-95ee-c447614382d3 | -8.34696 | -36.05552 | 2024-12-10 03:57:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9c7fb49b-5e4d-3999-8433-e88eb5ef9d3a | -2.90056 | -40.44005 | 2024-12-10 03:57:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79c8d9a5-ad8d-3619-bec2-6643c7db1ece | -6.72542 | -46.29403 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aca1c3a-1e5e-3062-89da-8b54a49f5e97 | -6.72677 | -46.29168 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00f84479-0823-39df-b899-cb0c08e130e6 | -3.7746 | -50.05738 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7dd05489-506d-3193-b555-265e82d0f9dc | -4.49893 | -44.32575 | 2024-12-10 03:57:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 432bd443-f2ed-31d6-8638-64c4be230e8a | -5.76722 | -47.87434 | 2024-12-10 03:57:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e83f9cd-c949-33a0-a2ce-65c8fbac6bba | -5.15625 | -44.09255 | 2024-12-10 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf8ffac2-6489-300f-81bc-4bca9d8beb4e | -6.82825 | -44.38712 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a83c7346-5452-3f40-a629-5d8857bc1667 | -2.98611 | -53.02296 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e88a51f7-76d6-3651-87f6-32808b24db2f | -5.71042 | -46.54803 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 357c3348-d832-3d3a-8973-52e8950ef42e | -2.77617 | -45.00062 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6a08306d-429c-3c56-b39b-d3ab33c741b3 | -3.78055 | -50.05853 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a10f1fc-7dc2-3ea0-a909-2b44fcad36fe | -5.59272 | -50.9857 | 2024-12-10 03:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b31d8eee-7d8f-3050-8277-b26d733301c4 | -5.72988 | -39.03648 | 2024-12-10 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0e3a03b-3503-3f11-abfa-0aa4a88f84eb | -5.91547 | -48.05638 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1c23a903-6e93-386c-8bf0-5889ab272edc | -5.90985 | -48.0587 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c5afd9ce-caca-3459-8773-82a99fdd2412 | -6.30655 | -45.76136 | 2024-12-10 03:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2da06747-fb11-3c1c-9323-ece83b38f4de | -7.07167 | -39.05212 | 2024-12-10 03:57:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 80fabb02-90cc-39a0-b911-5f1eb17b2d5e | -2.98501 | -52.86228 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b0224b61-5aca-3d3f-998b-11d62b31991b | -8.80279 | -35.65549 | 2024-12-10 03:57:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f58781b6-8b51-3553-a004-b5e891184f67 | -2.99183 | -53.02156 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5aeeb04d-f038-31f9-8e59-8beba48ce976 | -4.67383 | -49.49992 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e1ea8d-497d-302a-aab6-85959504b7e3 | -4.47211 | -42.86219 | 2024-12-10 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed4bbd7d-28e9-3c6b-a6cb-708baf46fcd5 | -5.98933 | -46.16249 | 2024-12-10 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ede936d-1c85-35cd-afb5-df65003cfbb2 | -6.7042 | -43.95451 | 2024-12-10 03:57:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f916342b-17de-3088-9b07-c2be4b3c509e | -4.60938 | -48.50248 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be300ed3-99de-38d0-88cf-b93b4ea127a0 | -5.49345 | -43.95366 | 2024-12-10 03:57:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7d7bcb9-6b83-3a65-a505-3ba2c41b5b1d | -7.17202 | -44.99254 | 2024-12-10 03:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75c09772-4d06-34cc-9f86-6f4fcf596b8f | -4.68073 | -49.50578 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbdcc50f-677a-3e94-8694-2164c7059270 | -6.82914 | -44.38419 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df8b8d4c-d87f-31f8-b277-c8e9b35bd387 | -4.60995 | -48.49904 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12572bba-89bf-3486-95c9-c5ade590be70 | -3.85754 | -40.44265 | 2024-12-10 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 769a1d65-055c-3d8e-9508-00ed14746f54 | -5.62845 | -44.83793 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2434c05-0f8c-3934-a0f9-b31cec4001bd | -7.96293 | -40.02005 | 2024-12-10 03:57:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 379e3dd8-2ab9-3120-9ee0-8e33bd4a5011 | -3.83343 | -52.36259 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527c3d17-a01c-313d-9599-a20acaecc9ef | -4.67506 | -49.50472 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33b4e077-32fb-37bc-8273-6e237364cfc6 | -4.8252 | -47.31314 | 2024-12-10 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04679b1c-f5bb-35a1-8fd6-60a46a52b673 | -4.24427 | -41.93232 | 2024-12-10 03:57:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b3fc9e5-9240-3152-a5fb-2eae8c8ec85e | -5.20829 | -44.65418 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d7eccb1-0b76-311c-9790-a011470632ef | -3.37661 | -42.32244 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab41dd3b-9182-39c1-9d28-75157be980ff | -5.63253 | -44.83858 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 51cd54b3-256c-3cf1-a8ca-e3aa4029d47e | -6.97339 | -42.99242 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a96beca3-5706-3059-900a-41149b16b90a | -6.262 | -43.55663 | 2024-12-10 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80006a14-a3c9-3e99-a875-1c439bb14e79 | -1.6982 | -52.61369 | 2024-12-10 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83caa191-966e-300a-abfe-12396218b8a6 | -5.87507 | -40.16425 | 2024-12-10 03:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8206476-dc11-3599-9460-5db35f9a24c4 | -8.3821 | -35.43676 | 2024-12-10 03:57:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60444ca0-d1a2-317a-bc5c-251a8fa6e6c6 | -4.49951 | -44.32225 | 2024-12-10 03:57:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69b11dc7-338d-34c6-bd6e-12e8c35e25e6 | -4.67888 | -49.50468 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f24c8d04-d8e4-3146-8cd6-93a6c5996f1f | -4.7073 | -43.7913 | 2024-12-10 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e0064cb-c1e2-30ae-9441-7d3c4342439b | -3.68355 | -49.5765 | 2024-12-10 03:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9244197-2900-341d-843f-4b2c20dfe115 | -8.11152 | -35.06454 | 2024-12-10 03:57:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 44e661c0-daee-3c3c-85d5-53e8e9181476 | -6.54833 | -41.71204 | 2024-12-10 03:57:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ee56f61-4fcd-32f6-910e-357fb20d1817 | -5.71444 | -46.55188 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a37e7dc8-3a2a-3308-b6dd-67440e9946c5 | -2.98978 | -52.86005 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9caa82aa-3bef-3000-9344-d3a0ad3c40f0 | -2.99216 | -52.86342 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b978fd1d-3e60-3fd1-943d-6c3a61255891 | -4.67821 | -49.50866 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7314df6b-98a5-392d-8362-f1bb5527eabe | -3.73698 | -45.99969 | 2024-12-10 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d09c14e1-1814-3251-bc2a-aed72e362443 | -7.86352 | -35.20197 | 2024-12-10 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c1670322-f9dd-3551-8a23-b4553264a80a | -5.62436 | -44.8373 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 182046a2-f1c7-3924-b7c8-4784b66bc10c | -3.56744 | -53.02935 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab6cc32f-ee79-325d-b389-279dbd95ee5d | -4.55288 | -48.0056 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba41cf49-9baa-30e5-8361-fc726114f5c3 | -6.3372 | -43.4352 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c18f4c6-9a94-399c-ba98-aab031d92196 | -6.34165 | -43.43141 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48e437bc-6fa4-3186-a337-02f164f28f33 | -3.79321 | -50.02006 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c8e508d-fa78-3b57-96fa-9a037410bf48 | -6.8243 | -44.65126 | 2024-12-10 03:57:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f76034f8-8e3e-38bc-ba04-3345d91ddec8 | -4.67953 | -49.50083 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e01d2e4-741a-3ecf-8605-f6f6a289c697 | -3.37196 | -42.32275 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93ec966c-2b26-3fc6-8e28-44fdd69bad7f | -6.90523 | -47.84338 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d51b64d9-40f3-34e4-9925-e0c468bdfb11 | -5.67899 | -46.48267 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6855ba9c-81ac-3940-9ded-f02406792c98 | -5.53762 | -39.22271 | 2024-12-10 03:57:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e3a08d8-728d-34af-a5be-76c198ed1b72 | -3.68433 | -49.5721 | 2024-12-10 03:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcf424b8-2878-360f-a67b-aefa55945b55 | -3.32757 | -45.60167 | 2024-12-10 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ab09952-86df-3767-a39e-1071ad2d00f1 | -6.9172 | -43.51331 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cd37ea50-9604-3cd2-9cbe-f1cc82a5d894 | -4.67573 | -49.50092 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23ed24d3-2823-354c-a3d3-9c12e5406eae | -2.991 | -52.8529 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| def12026-4789-30bb-bee7-374f715561ee | -3.85419 | -40.44212 | 2024-12-10 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2afb5110-d477-3b8d-a35a-2b85e4fd3f7c | -4.54771 | -48.0048 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94e7d000-3bd5-3135-9922-70143fa2f580 | -6.96259 | -42.99071 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3ef1787c-514d-348c-96c3-2b66c76519df | -2.99346 | -52.85614 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |


[Clique aqui para ver as próximas entradas](README14.md)
