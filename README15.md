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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634da246-5ef7-3b3a-ab81-687726d86751 | -21.14974 | -48.61104 | 2025-11-30 04:27:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c551333a-b17c-3ec3-9b4e-ea7f2f6bb17e | -19.84065 | -57.77482 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2fa73632-9e3f-377f-9370-b56556cfc8ae | -18.15512 | -47.14156 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6837a3de-377a-38f8-9adb-dbb29c9a35d5 | -17.51381 | -57.15163 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f09cdb3d-2858-383b-b293-710273d3d8b7 | -23.18442 | -45.65909 | 2025-11-30 04:27:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 595d7512-fa39-33ad-b5aa-89af4fb99d51 | -19.09189 | -48.59381 | 2025-11-30 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 424cfa78-2946-30f6-ac26-5643f209cd57 | -18.12016 | -47.15422 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 687ed637-9c61-334c-a0d6-56018735bb6e | -18.3098 | -47.83539 | 2025-11-30 04:27:00 | NPP-375D | TRÊS RANCHOS | GOIÁS | Brasil | 5221304 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41a2d99f-e1ac-3fb5-bca2-2b53e290a08d | -20.59929 | -52.45975 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9d3fbf4-52d2-39d5-bb2b-d645ccb70403 | -20.18593 | -52.38578 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| effd4969-6f24-390f-875d-58db5dfaef31 | -16.76278 | -51.35447 | 2025-11-30 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 886e467e-a878-34aa-bda0-950a176b155e | -22.49217 | -46.93753 | 2025-11-30 04:27:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a361acc-7d37-34b4-a221-6a6ec119714a | -17.56011 | -42.08865 | 2025-11-30 04:27:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b0619a48-a209-38c2-ad12-d4501d6ec11c | -19.86199 | -57.78677 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a30ac570-0ff2-3eb0-857c-011cc5370b5e | -20.92402 | -46.80171 | 2025-11-30 04:27:00 | NPP-375D | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8dbbff5e-3ef9-310f-81b7-4469a63b07cb | -18.1174 | -47.15002 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab971280-e039-389f-9a9d-14b7e7608dc2 | -19.84371 | -57.7605 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aad241d1-a7e9-345e-9546-fe588fb3a320 | -19.65895 | -46.61532 | 2025-11-30 04:27:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b076a8f-08d3-31a0-a249-c69d4b7300a5 | -17.96758 | -48.91048 | 2025-11-30 04:27:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b56e83e-4fc5-3358-91a1-0de1eac796d9 | -18.74643 | -47.06128 | 2025-11-30 04:27:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 394db463-f92f-3505-b718-5d43ff8ddaa6 | -22.29956 | -43.47384 | 2025-11-30 04:27:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6f10f77e-7bab-3b46-b5d0-412024802fba | -19.86125 | -57.7837 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c6e1af4a-12d0-3b72-9fc0-5c8bd5bbfe36 | -23.21959 | -47.43544 | 2025-11-30 04:27:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a5d6323e-95cd-3093-b796-ecd0102ae990 | -19.93476 | -46.72936 | 2025-11-30 04:27:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c5bdf7-8f3b-3aa9-9c1a-672abc1ffe68 | -19.86435 | -57.77604 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a4052612-800f-3626-81d0-f7bb7a9f2fd7 | -18.93585 | -48.48641 | 2025-11-30 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b22e1628-ef87-3693-b286-2be063dade44 | -19.84904 | -57.78823 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1c187cee-94f2-3257-ad9a-22b734143fcf | -19.86811 | -57.77784 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b302f4a7-c2ba-3dc3-a997-67ae7472c86d | -18.13566 | -47.15688 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d93881a-286f-3c57-ada7-d4f976eaa1ce | -23.52099 | -46.97601 | 2025-11-30 04:27:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3a126a7-f9bf-33e9-8dbd-4c5de3622477 | -18.15568 | -47.13793 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd5ecc5c-2280-3293-804e-294633c9967e | -19.85665 | -57.78546 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| f4ec5c94-5a84-3dc8-837f-8b8d418baa77 | -17.49099 | -57.14654 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c62f0b09-65b3-349f-a0c2-003740eaaab2 | -17.49637 | -57.14781 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 37da1729-d3c6-3e94-9cf0-f656da1ca1f2 | -18.1496 | -47.13318 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fea850f0-3422-3226-83ee-822c2506c9e3 | -17.85901 | -44.31449 | 2025-11-30 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efa6fa0d-9d02-35bb-b600-faebe6fe8469 | -20.18017 | -52.37416 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d7f8468-26f6-3f3f-a28d-af93798c3cf0 | -21.62299 | -44.84742 | 2025-11-30 04:27:00 | NPP-375D | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1e8eeee-1e06-3040-9ba3-fb37049dc1a1 | -22.49274 | -46.93362 | 2025-11-30 04:27:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a87996fa-d405-39f5-99dd-112a19fd1ae5 | -20.17766 | -52.37686 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f48e52a2-e0a3-3740-b411-82bcba49c145 | -19.08915 | -48.58949 | 2025-11-30 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4197a734-c3ba-3575-9dbc-b2b4adfa30ea | -19.09249 | -48.59009 | 2025-11-30 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5451959a-5f1e-387e-9348-1101fd7f4d43 | -18.15236 | -47.13737 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85afa426-3773-3b54-856c-c073766b3a0e | -19.84446 | -57.78333 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 495da970-33b4-3494-bb9c-562b250452d2 | -17.50919 | -57.1468 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f7bb25c5-9655-3d9a-8fc3-af16fcbdc462 | -19.92539 | -57.44596 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 64847417-180b-3c4a-889a-ea5cc4048a1a | -17.48767 | -57.1418 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dad034e3-cc4a-3cf6-9a6f-56f2ed438d0a | -22.53989 | -42.11569 | 2025-11-30 04:27:00 | NPP-375D | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcdc2e4d-41d4-3b9c-8558-b842faaf200c | -22.29558 | -43.4733 | 2025-11-30 04:27:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b859da8-1717-3208-8803-39b678e43fdb | -17.50305 | -57.14913 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 23f3f80b-21db-37f1-8538-a3ff054997e9 | -23.18383 | -45.66333 | 2025-11-30 04:27:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a591e346-5c25-306c-9591-fb6100b0c593 | -19.86357 | -57.77962 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 77b69162-4c42-3e96-a4c3-2b5c8c9cc545 | -21.41808 | -46.64175 | 2025-11-30 04:27:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28c1a9b2-1462-32ad-bdd4-44c03e59c7f4 | -19.8666 | -57.78501 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b2b42b01-300d-3d66-960b-5fd9e7a8aa01 | -19.85439 | -57.78955 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2ba678ef-5e74-31f3-9f78-cb21089d86cb | -21.62663 | -44.84801 | 2025-11-30 04:27:00 | NPP-375D | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3fdca2b6-c1e9-3230-8e41-b72b4a2d6d19 | -19.92686 | -57.44673 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1c5ed63e-ba27-30ca-9d69-73a929b6b1fd | -18.13623 | -47.15324 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d86433-e88f-3c88-8d96-3f8423cdee50 | -23.1902 | -46.70947 | 2025-11-30 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6810415c-e19a-30bc-adbf-ed6b7307facf | -21.1758 | -49.18098 | 2025-11-30 04:27:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c53c442c-a89f-3423-a008-1c622d8e69cf | -17.85602 | -44.30975 | 2025-11-30 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96c6f8a7-9a2e-3d83-861b-51f5bf5708aa | -18.6185 | -45.22817 | 2025-11-30 04:27:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b58ddeaf-143b-3be7-8fc0-aa4a84c0cf59 | -20.18147 | -52.37765 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a68327e-df39-3e74-aed7-36adebc3db03 | -23.40754 | -47.39141 | 2025-11-30 04:27:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee8fc60c-5fae-3eb3-b544-d0803a783680 | -23.22297 | -47.43604 | 2025-11-30 04:27:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a8accaf7-80b2-34b2-9119-355b28fd378a | -21.15306 | -48.61165 | 2025-11-30 04:27:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 211d80e4-5315-3e28-bb8f-c05f71f72512 | -19.83989 | -57.77842 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 28d1f7c0-ce9e-328b-815e-725fc50371ce | -17.50175 | -57.14907 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c18421c3-0f26-304c-a49b-b8a7c2c424e7 | -19.93209 | -57.44044 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d03e1579-8966-3785-af09-d72720bdcd27 | -18.12956 | -47.15955 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f867bdf-da16-3e2e-a7ec-bcc0acc2d947 | -19.86278 | -57.7832 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b1a20f21-3209-342a-8fa5-aadc3a4753fd | -19.98015 | -47.83813 | 2025-11-30 04:27:00 | NPP-375D | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dabe6d5-b7a3-3c3e-a534-433d6572b693 | -19.86736 | -57.78142 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ebc06c12-7af0-373b-8d1f-6be7ff290c21 | -23.54943 | -47.20699 | 2025-11-30 04:27:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 65042e94-cd25-381c-a71c-2929ebb5f4e2 | -23.13071 | -54.88099 | 2025-11-30 04:27:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78309a9f-1108-318a-b9fe-5442ff780fca | -17.48543 | -57.11892 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 22cc2b0e-b4d8-335f-a0e7-e4a2c29a0725 | -17.47932 | -57.12123 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ba9ad5cf-38c7-3889-b450-fa5705f24a9e | -18.15293 | -47.13375 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 932aad4e-9be3-3a8d-88b9-5463496e6d97 | -19.85515 | -57.78595 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 46f26277-e3d9-3dfe-8b5d-79073e97d382 | -17.49767 | -57.14788 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c287a51b-6b8b-3218-91d1-6d0784893e44 | -18.12348 | -47.1548 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da840c70-a3f1-3440-bdb1-73e9d1f62c0a | -17.48636 | -57.14168 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ccac46d5-24f7-33c4-969f-e7afda46b42f | -19.92686 | -57.43919 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bd9c3783-3f56-3295-97f2-162980fc92c2 | -21.00354 | -49.30922 | 2025-11-30 04:27:00 | NPP-375D | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3386e820-9ce3-3315-958b-f16930e7d9dc | -22.98039 | -46.24001 | 2025-11-30 04:27:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 53e521fe-e1c9-37fb-aec0-1a6a72643f8f | -21.15247 | -48.61535 | 2025-11-30 04:27:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c05d0451-5e68-3965-8d46-d45985855a2c | -16.22261 | -52.18541 | 2025-11-30 04:27:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc0904d0-4254-3fec-a6df-e7d59f33adc2 | -18.11465 | -47.14582 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bf7465a-3c14-3e47-9ef7-647a23239052 | -17.47858 | -57.1248 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9c0bc5ab-ad19-3577-9cc1-501e54acb4cd | -19.85052 | -57.78774 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| adf85a80-bce5-3339-855a-806875c870ad | -16.79596 | -53.77576 | 2025-11-30 04:27:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57a39639-d121-3214-a0f7-6fecbcb05238 | -19.09442 | -48.58995 | 2025-11-30 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea2d8614-cea9-39bd-ac45-f9941c2e8425 | -19.92614 | -57.45013 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 322d0927-36f9-3659-b3c4-601edfbac4aa | -22.34454 | -43.51611 | 2025-11-30 04:27:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b4329e2-8884-39e7-bd0d-1431da03c2aa | -21.17642 | -49.17722 | 2025-11-30 04:27:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cfaecda2-0793-310c-9631-784c9b699615 | -19.86201 | -57.7801 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 11894b0e-6b8e-3f88-9474-abe14b611a29 | -19.84676 | -57.77255 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 095c02f1-20b8-3d25-b780-0c823eeb1c74 | -19.92613 | -57.44256 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5af70eec-c385-3d65-8dce-c83ba8a986c9 | -19.84295 | -57.76407 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 01de0926-3ee9-3637-9bf9-82b6ad58b604 | -22.48752 | -47.47846 | 2025-11-30 04:27:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
