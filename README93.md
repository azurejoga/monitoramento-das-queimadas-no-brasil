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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f62f332-b9ad-3346-be4d-36bc43368051 | -14.4031 | -51.265 | 2026-10-01 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 29f6af23-bcb0-3934-a2f6-1f9f0305196c | -14.4035 | -51.2435 | 2026-10-01 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| dceb9262-a606-3ca4-83c6-6ddeab0685f6 | -14.3841 | -51.2462 | 2026-10-01 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 19292207-4507-3262-aa2c-d8ed28a7524b | -14.4035 | -51.2435 | 2026-10-01 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1eb719d7-6073-3141-8760-80eb7f2a68e3 | -14.4422 | -51.2382 | 2026-10-01 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4916f032-108e-3ed3-8697-72bb533c176a | -14.4418 | -51.2597 | 2026-10-01 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ea8aa56d-6401-35ad-a22b-498449265054 | -14.3838 | -51.2677 | 2026-10-01 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 03f5649d-3139-3393-9964-3ea70ba46a49 | -4.29 | -50.81 | 2026-10-01 07:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9757c0-4680-376e-8d90-c2b8a232ad33 | -4.26 | -50.75 | 2026-10-01 07:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84961f1f-922a-30a9-9451-20fe64f2e924 | -4.29 | -50.76 | 2026-10-01 07:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b430d5-a3f0-3bc1-bd55-c03f6e667bc5 | -4.26 | -50.81 | 2026-10-01 07:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22702e85-cdbc-3857-82b3-94a23ac8f222 | -14.3841 | -51.2462 | 2026-10-01 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 022ef0fc-4158-387c-bf86-77ba75af8332 | -14.3648 | -51.2488 | 2026-10-01 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| eab24ffa-11ec-32a6-aa50-dc7c7d4579e2 | -14.3838 | -51.2677 | 2026-10-01 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 26c74cfb-7dd8-38af-b2ff-c06fd85338c4 | -14.4418 | -51.2597 | 2026-10-01 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d46ac5ce-9c3f-3ede-af30-4e9dcd53f50f | -14.4035 | -51.2435 | 2026-10-01 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 16334f6a-d80d-3fd1-9183-76f9a00d7baf | -14.4035 | -51.2435 | 2026-10-01 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 3549af6b-5193-34c3-8950-a08fe2547ae6 | -14.3648 | -51.2488 | 2026-10-01 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4f195064-f0f1-35f1-b941-c47c2c88c9db | -14.3838 | -51.2677 | 2026-10-01 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 33c628c9-8cc8-3c58-a32e-6ed49463843b | -14.3841 | -51.2462 | 2026-10-01 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 219.2 |
| eda259ad-b9fb-3f1c-92f9-aa99080b0e26 | -14.3841 | -51.2462 | 2026-10-01 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 3ea43586-a0ae-3fe0-a368-ae519eec8db1 | -14.3648 | -51.2488 | 2026-10-01 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 700ee304-9068-3acf-9fae-79cc9ddb247e | -14.4035 | -51.2435 | 2026-10-01 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2345cd7b-6aa9-3d8d-b6d7-a916282182ca | -14.3841 | -51.2462 | 2026-10-01 07:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1f00b178-781f-3b79-a206-e9f57312103f | -13.0587 | -51.1837 | 2026-10-01 08:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e6283704-fe52-3b5e-8b0a-3d7292e56bb5 | -11.7354 | -50.4015 | 2026-10-01 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c03098d6-6205-31ba-a4bc-b9ab27b1a587 | -11.7164 | -50.4037 | 2026-10-01 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3045e38e-b0b5-3c25-a5ea-4aef54157e4a | -11.2716 | -50.9654 | 2026-10-01 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 4a318d96-3473-3ae6-a0df-6c863fce97ea | -13.0581 | -51.2264 | 2026-10-01 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a4ae6349-bb43-3638-9fa3-fe4d435bc7fa | -13.0584 | -51.205 | 2026-10-01 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5a0d6bff-7534-362c-bfe7-7d50d42285f5 | -14.3845 | -51.2246 | 2026-10-01 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| aa7e6f94-0005-3d8d-afa0-200353904a1a | -14.3841 | -51.2462 | 2026-10-01 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 75cd5ca0-13c7-3041-b3df-a8022a9511a6 | -11.7164 | -50.4037 | 2026-10-01 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| dbace649-1746-3b28-a53e-9caad0e8eba1 | -14.3648 | -51.2488 | 2026-10-01 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 26edf890-d891-3b7e-b1f8-b55e44c0f20c | -11.2716 | -50.9654 | 2026-10-01 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ce41e855-bb66-3a3d-8323-7b335957a827 | -13.0587 | -51.1837 | 2026-10-01 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| ec0bc6a3-10a4-325f-9bde-55c55339094b | -14.3838 | -51.2677 | 2026-10-01 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 2dae23eb-fd7f-37fd-9be0-6aa3c6128a32 | -13.0396 | -51.186 | 2026-10-01 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6025d531-66be-35bd-83af-75fcaeaf592f | -13.255 | -43.6805 | 2026-10-01 10:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a7695153-b1c7-3712-96e1-b3292487d784 | -11.2087 | -45.1939 | 2026-10-01 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ae4782f5-132b-36c5-a2d8-0638b4656069 | -11.2278 | -45.1913 | 2026-10-01 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 71ba3012-be4d-36e1-9fe2-1b512b9fe33f | -11.2278 | -45.1913 | 2026-10-01 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 4dee764e-5caa-3ca7-9ed4-24d71dbc47ac | -11.2087 | -45.1939 | 2026-10-01 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| fb274e35-b3a3-3182-b2b1-54f4ade46dd9 | -6.82012 | -39.75034 | 2026-10-01 11:02:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 875d13e0-26da-351b-8ae7-5a46fdc29fed | -8.33596 | -44.16732 | 2026-10-01 11:04:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c43b49a2-9365-3c7e-895e-a715d6e0badb | -14.66092 | -41.02811 | 2026-10-01 11:04:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| c36a9ea0-a28e-3b31-8cbe-b66c238c94ee | -11.94471 | -37.63796 | 2026-10-01 11:04:00 | TERRA_M-M | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 97ccb91f-5ee7-3992-8885-45ec96b53093 | -15.09951 | -41.18092 | 2026-10-01 11:04:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e1abd7b0-0607-3763-bd77-81cc7f2fe942 | -8.20866 | -45.48545 | 2026-10-01 11:04:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.7 |
| bdf482c3-6a86-315f-b5a7-bd3cd2a7c2a7 | -13.32 | -42.26333 | 2026-10-01 11:04:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b5d87cc9-c88e-38f7-bc54-281238dcef50 | -7.18487 | -41.07579 | 2026-10-01 11:04:00 | TERRA_M-M | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| eda35fc2-7043-3fe1-b752-3814fb3e684a | -16.49967 | -41.20957 | 2026-10-01 11:04:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 3240e50d-0d55-3576-943c-2b54cd1c7483 | -9.36271 | -36.05622 | 2026-10-01 11:04:00 | TERRA_M-M | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 77855f6f-98ab-3b3f-9391-a3de4f6b95d7 | -14.77148 | -41.76518 | 2026-10-01 11:04:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d27d6422-8c60-33fa-8af5-2fd046ba8c42 | -8.00963 | -42.906 | 2026-10-01 11:04:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a3aa3c48-2be0-3696-959f-b1dfebbac610 | -8.20976 | -45.49387 | 2026-10-01 11:04:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 71ab633d-9bd9-3d65-9d61-911161fb5da3 | -15.96247 | -41.89228 | 2026-10-01 11:04:00 | TERRA_M-M | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3492d315-70e0-3412-8bd6-69cd87fbf0ea | -14.37002 | -44.78225 | 2026-10-01 11:04:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| c6a1fb27-9a12-3c31-9ba0-150e6b8a50b5 | -14.44529 | -42.15046 | 2026-10-01 11:04:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8ddfd446-21b4-3091-a5f2-1ad1bb526cfc | -8.34098 | -44.14081 | 2026-10-01 11:04:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 06480ebe-f33d-3d02-b0eb-80118c31928f | -16.62316 | -42.39884 | 2026-10-01 11:04:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ce66d453-4945-31c5-a280-fa6aa7a8c33c | -14.26439 | -41.92944 | 2026-10-01 11:04:00 | TERRA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| d899cd51-b04e-3414-aedb-f178d65b2e53 | -8.01229 | -42.88901 | 2026-10-01 11:04:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| 417da4d2-4fa3-3a0d-aef0-fbbfa64b12c4 | -14.66245 | -41.01813 | 2026-10-01 11:04:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| adaf3789-7a02-3cf2-9d92-0bdfcf4e2f57 | -11.4453 | -43.40915 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 65590026-6aa0-3b3b-8f63-5a593c1f6d0a | -11.21741 | -45.20151 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 561f2d55-5806-30e3-bd3e-1eaafc2a794e | -11.44275 | -43.42507 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| da53e53e-ed44-3fc5-8ebe-44917a8ac48c | -16.50126 | -41.19903 | 2026-10-01 11:04:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| be578419-a64e-3fdd-8f68-913672f0c329 | -11.61654 | -43.56555 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 010822dd-9d91-3ba0-a613-d2f0a3597ec4 | -13.32918 | -42.25858 | 2026-10-01 11:04:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 75b3a9ad-be43-313a-95e0-981f75ea7c3c | -16.66582 | -41.51936 | 2026-10-01 11:04:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fad17ea6-cff7-3dc5-a67b-c835ec112e45 | -7.38327 | -38.04896 | 2026-10-01 11:04:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c5ce1810-b78a-345b-8d7b-1b109923b5a5 | -8.13378 | -43.53011 | 2026-10-01 11:04:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 164aedb5-5636-3770-a352-6f59571fd883 | -11.46328 | -43.44492 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| af3781f6-6223-36d8-a7ad-83b57bd69099 | -8.16703 | -38.69469 | 2026-10-01 11:04:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0b953a6b-b803-345b-a8c5-065b2faf495c | -11.89546 | -43.82421 | 2026-10-01 11:04:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d118514b-5a7d-33cd-9c48-5308f47185fb | -8.30647 | -39.38285 | 2026-10-01 11:04:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| b1fe3bd7-560d-399f-9536-8de759d12354 | -8.33934 | -44.14653 | 2026-10-01 11:04:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5df32ceb-bc34-3e08-bede-c862288ee9e5 | -11.23433 | -45.18247 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 83d1e88a-109a-3a9b-a942-fd9ba371333e | -14.89062 | -41.65532 | 2026-10-01 11:04:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6edf9d7c-1208-3441-8ba6-8db3db02f5d3 | -13.28833 | -42.39948 | 2026-10-01 11:04:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| fc3b1cf6-9b24-33c3-8c50-0344ab0c1f41 | -7.07572 | -42.31643 | 2026-10-01 11:04:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| da925e27-e3e8-3fae-9005-09d987d2d94d | -15.85053 | -41.70176 | 2026-10-01 11:04:00 | TERRA_M-M | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 4a88b861-00e7-3883-8c1b-855793ad4817 | -16.61594 | -42.44526 | 2026-10-01 11:04:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f43bf9c2-7de4-321d-a826-5899748b4b59 | -8.33778 | -44.16152 | 2026-10-01 11:04:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3327cf7d-f9d9-3932-8956-f1dea6bc721b | -15.75976 | -42.27991 | 2026-10-01 11:04:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d0d9aa3f-e679-3382-8553-88484cbbc406 | -11.61913 | -43.54932 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 44beb1f7-e4a8-3d02-a62c-50eadfdc1a48 | -11.20925 | -45.19325 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 16bd24bc-dc9f-3b6f-a66b-25efcc55a995 | -14.26264 | -41.9407 | 2026-10-01 11:04:00 | TERRA_M-M | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 3ac3d815-f874-3bc1-b715-cdfeaf1dc4b3 | -14.88897 | -41.66616 | 2026-10-01 11:04:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| bd0dfa20-fd6d-3b3b-aa82-f676d91969e2 | -15.86002 | -41.70336 | 2026-10-01 11:04:00 | TERRA_M-M | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 91397645-3420-3909-a256-86398b1bf8b9 | -8.30789 | -39.37314 | 2026-10-01 11:04:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a2e667bd-8763-30b8-94df-9a24688a363c | -11.20401 | -45.19954 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b22359cb-41a8-3243-9bf0-16f94bbda2ae | -11.41073 | -43.4035 | 2026-10-01 11:04:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 63ef5ef7-b154-3ae1-a24f-9f0a5e378c6a | -16.62581 | -42.44669 | 2026-10-01 11:04:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| d30b7f1f-f28f-36d2-8c00-9ea766c2745a | -15.17205 | -40.95357 | 2026-10-01 11:04:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f80ebc0d-1089-300e-9972-78be6999aa79 | -11.23078 | -45.20365 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ba335611-5404-3c6d-9aaa-5fd97b433bed | -11.17993 | -45.12133 | 2026-10-01 11:04:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b720ebb9-ef3c-3eed-ad67-f2d3b2228e50 | -19.94558 | -40.63465 | 2026-10-01 11:06:00 | TERRA_M-M | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9ebebbf1-1753-353c-9cd6-58b810e2ba81 | -18.85517 | -41.20684 | 2026-10-01 11:06:00 | TERRA_M-M | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |


[Clique aqui para ver as próximas entradas](README94.md)
