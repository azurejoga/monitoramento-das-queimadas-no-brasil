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
| ea58c5e3-329a-399f-939c-1a574944e60b | -18.889601 | -54.502998 | 2024-10-07 00:25:26 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25296b99-e1ba-368d-846f-725019e256f0 | -18.1126 | -50.1287 | 2024-10-07 00:25:26 | METOP-B | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8c6f41b-0ab7-38c3-b03b-6bd0a00b81e9 | -18.8799 | -54.5047 | 2024-10-07 00:25:26 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bc3245b6-5c9e-365e-ae66-423d3016c0b5 | -18.884001 | -54.529701 | 2024-10-07 00:25:26 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 864edb34-94a1-3aa5-80ef-b28a002726ea | -18.870199 | -54.506302 | 2024-10-07 00:25:26 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e5a9a7dc-33e3-3bd2-bc4f-6feb251cb9db | -18.8743 | -54.5313 | 2024-10-07 00:25:26 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b9d529db-6599-3f6c-96f5-d22a6b8d32b4 | -19.199699 | -46.566601 | 2024-10-07 00:25:28 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 415f7b26-a37f-3324-982b-6dc80a0cf540 | -18.6387 | -43.952499 | 2024-10-07 00:25:28 | METOP-B | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 02c07d9c-044f-3512-a37a-6373eef616f4 | -19.189899 | -46.568802 | 2024-10-07 00:25:28 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7687bf7a-54b9-3b84-9c2b-d5bf452de710 | -18.2365 | -42.200298 | 2024-10-07 00:25:28 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1c2247a-ab55-3a9a-bb9b-c5a89bf479fc | -18.2383 | -42.207901 | 2024-10-07 00:25:28 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 284a01cf-ed9a-3f1f-ba92-aa70501f3608 | -4.2542 | -43.7381 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 63a7253a-ad9e-3304-aa70-f6e6c960a1aa | -4.2728 | -43.7601 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 845e4a7d-4b73-3bf1-a00a-22a8c50c3efe | -4.2729 | -43.737 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 87a108fe-ef2a-3d75-a9c6-856f18fd43fd | -4.2731 | -43.7139 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| a5fc8db2-c0f5-31fa-895a-bcae9aadbb95 | -4.2914 | -43.7591 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| f22146b7-7b07-33b0-be42-fb2380f89989 | -4.2916 | -43.736 | 2024-10-07 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| cccdfd13-102d-3b23-b210-e994d05dec3c | -18.2967 | -43.012699 | 2024-10-07 00:25:30 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c354dad-d3e5-3c51-86f1-e6e8df21bdf1 | -18.298401 | -43.02 | 2024-10-07 00:25:30 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d52d530b-93ad-397d-9060-2c3404416fd6 | -16.9198 | -46.926998 | 2024-10-07 00:25:35 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2779b36e-6b42-343c-a64e-03b997155d64 | -16.921499 | -46.935001 | 2024-10-07 00:25:35 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0ac942-fa8e-3048-b195-5003ef1bb543 | -16.911699 | -46.937199 | 2024-10-07 00:25:36 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eb4ca67f-afbe-359d-b60d-5c4f5234a9a1 | -16.925699 | -47.104198 | 2024-10-07 00:25:36 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af569f76-b16c-3eda-8cb3-72dcb6070c95 | -16.903099 | -47.143501 | 2024-10-07 00:25:36 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fbd56a38-6c60-3c6c-a2be-dc0d9d7947c6 | -16.8916 | -47.137402 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59716ca8-b742-37ab-b558-a1a44ff6673c | -16.893299 | -47.145699 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f315b900-3a34-3c25-8df4-6b93584ba0af | -16.895 | -47.1539 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07bba254-a6e9-374f-8348-a45e7e0b3ba7 | -16.8967 | -47.162102 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d70dd45a-a03d-302e-b301-dee5991c5ad3 | -16.898399 | -47.170399 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 49990ce8-95c7-327b-a9c3-80106c1b9063 | -16.9 | -47.1786 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5f4979-52bf-3334-b744-ec8793df33fc | -16.883499 | -47.1478 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f6d930d4-3f98-39c3-8543-e68b670eb2a1 | -16.885201 | -47.155998 | 2024-10-07 00:25:37 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e5276ac0-4af3-3e44-891a-f4d69bb3a6bb | -15.7845 | -42.270302 | 2024-10-07 00:25:37 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b06fb67-25b1-3b17-8dbc-fdc07578d536 | -17.7763 | -53.061298 | 2024-10-07 00:25:41 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83f0ae14-684b-33c9-87af-c16d29e06165 | -17.7666 | -53.063099 | 2024-10-07 00:25:41 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd1eb67-e3e3-30f2-8a76-b2278599cbcb | -17.8433 | -53.738602 | 2024-10-07 00:25:41 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea393e3-7428-3180-8f11-cb263a8f5ccf | -17.847 | -53.759998 | 2024-10-07 00:25:41 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd589669-4fa3-3185-8d21-792b86c109da | -17.6724 | -53.0411 | 2024-10-07 00:25:42 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91375c59-e20a-348e-83eb-b80d0533b05b | -17.675699 | -53.0602 | 2024-10-07 00:25:42 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd015067-0f47-3f2a-887d-6f96e69c1c12 | -17.6593 | -53.0238 | 2024-10-07 00:25:42 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2125915-090d-3a23-a8da-e2c1fde38e69 | -17.662701 | -53.0429 | 2024-10-07 00:25:42 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1300c70a-bab2-3bfc-9b9c-4c7ddb51cd75 | -17.666 | -53.062 | 2024-10-07 00:25:42 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 157b7d04-4b29-3cd8-a26d-2a81683dee60 | -17.83 | -53.719002 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 013a4c57-260e-30ae-ad70-c69226ffec82 | -17.833599 | -53.740398 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1b10074-bb5b-367f-b8f1-b42b82828a92 | -17.837299 | -53.761799 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d472918-a56d-3e6d-95af-6018e6abb509 | -17.8239 | -53.7421 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fce1741-b3bc-3e9a-a58b-85d0c885de59 | -17.8276 | -53.7635 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36498b71-41a7-3701-9b46-7eabdc7d244a | -17.8106 | -53.7225 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 319f802c-758c-3447-8d8a-5296a9915a2c | -17.814199 | -53.743801 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f921aa06-6242-319f-ab41-32d7b136c9f0 | -17.8009 | -53.7243 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e11e58f1-2698-33ef-b47c-65686aa467f2 | -17.804501 | -53.745602 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d55f5746-879f-36ac-b266-f59245d3a8fe | -17.791201 | -53.726002 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0244a720-1e4d-3b57-accd-a78969ec93f3 | -17.7948 | -53.747299 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a12dd4f0-68ee-38da-9b74-ce7a42f33016 | -17.7985 | -53.7687 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 658f2d8e-6ef8-358a-8b89-08a923f56860 | -17.7778 | -53.706501 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4c34ec7-e670-3de9-ac58-7962c4be1fc5 | -17.7815 | -53.727798 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9323063b-17fe-3577-8eb0-190a68c90ff1 | -17.785101 | -53.7491 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be92af7a-dc3c-3cf5-8ddc-27bf2f0d4e42 | -17.788799 | -53.7705 | 2024-10-07 00:25:42 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33f7020d-2883-3c4c-a101-f72fa0e9994d | -17.649599 | -53.0256 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e557cd8e-e09f-337a-816c-1fb02e9f7518 | -17.653 | -53.044701 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c99fa468-a815-3a27-8ef2-ead7968a0b0f | -17.6563 | -53.063801 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bba2efb-13d2-30cd-bd8a-a2660a852dcd | -17.639799 | -53.027401 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e832736-5e70-301c-8479-0495e714988e | -17.6432 | -53.046501 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ed81361-1447-34ca-a25a-ab971e9db1cf | -17.6465 | -53.065601 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84fc4cf4-86f9-3248-b4d1-91256edb14fc | -17.633499 | -53.048302 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1c7c7cf-ece2-309e-8ac1-a48ed190c173 | -17.636801 | -53.067402 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5fd7480-8e6e-39f6-b822-f36f092fa444 | -17.6238 | -53.050098 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6786d3ca-7f1f-3e61-a720-fde2b33b2786 | -17.6271 | -53.069199 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc3ef4e-01ac-30c6-8838-16bec6d8e575 | -17.630501 | -53.088402 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46e9cdb4-b00a-378c-bf16-8215946974f6 | -17.617399 | -53.070999 | 2024-10-07 00:25:43 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9c75e4-8a13-3170-908e-2632a8183a2a | -17.771799 | -53.729599 | 2024-10-07 00:25:43 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd1a8fb-df33-3c65-aa01-32e001fa04c0 | -17.7754 | -53.7509 | 2024-10-07 00:25:43 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51367bf4-08ba-37e5-bcc7-7bfcf4fbdfb3 | -17.7791 | -53.772301 | 2024-10-07 00:25:43 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 306608d8-2047-30b6-9af0-4a6310519738 | -17.765699 | -53.752701 | 2024-10-07 00:25:43 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad2a20c-781e-3a80-8187-38b82430a9b0 | -17.124599 | -51.672901 | 2024-10-07 00:25:47 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2461c643-3752-3c41-b0d8-c726f030ed92 | -17.127399 | -51.688099 | 2024-10-07 00:25:47 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20849adc-b1f3-3f11-a7a1-0a55b62bcd2f | -16.537701 | -49.024799 | 2024-10-07 00:25:49 | METOP-B | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf5be00b-a0bc-357a-889b-744e53eda550 | -17.084999 | -52.118099 | 2024-10-07 00:25:49 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4614ae9-5cc1-399f-b872-529337e45ed1 | -17.722601 | -57.005199 | 2024-10-07 00:25:52 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 41e21c68-5cca-3b70-8d40-0e444d9c1421 | -17.177299 | -53.881901 | 2024-10-07 00:25:53 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c69732a7-91ad-35a3-963a-d1eecd29c247 | -17.167601 | -53.883701 | 2024-10-07 00:25:53 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3db4bbc-5a3a-3b3e-81bf-bfdfb6071625 | -17.171301 | -53.905102 | 2024-10-07 00:25:53 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3ccf33d-53e1-31d9-b586-af681a8aa110 | -17.315701 | -54.986301 | 2024-10-07 00:25:54 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06f0302c-e0d2-30db-aa6a-aa037b958dcd | -17.306 | -54.987999 | 2024-10-07 00:25:54 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 469676c1-c8b4-3cbb-a7f5-9dc7167c3051 | -17.310301 | -55.0135 | 2024-10-07 00:25:54 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7074843-992e-3301-b791-9435911dd88f | -17.2964 | -54.9897 | 2024-10-07 00:25:54 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29ed4629-01bc-3ef0-a4de-b5886de7dfa4 | -17.300699 | -55.015202 | 2024-10-07 00:25:54 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 126c5b61-f131-335f-bc65-4085b8381065 | -16.3174 | -51.2481 | 2024-10-07 00:25:59 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7b66f9c-1749-3198-964e-4e0ab2b4df4e | -16.32 | -51.261902 | 2024-10-07 00:25:59 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 358a8185-3a3f-3759-a969-b96fd81baa04 | -16.307699 | -51.250099 | 2024-10-07 00:25:59 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14eeab68-6dcb-301f-8b5b-85a074df43a6 | -16.310301 | -51.263901 | 2024-10-07 00:25:59 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7587f7-0b5c-3b97-a5f6-279d21dd30fd | -17.021099 | -55.012199 | 2024-10-07 00:25:59 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60f7081a-6d7a-3553-8785-3c4b0161507b | -17.0114 | -55.013901 | 2024-10-07 00:25:59 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd05a066-6161-3a20-b555-88e86544c69b | -17.0156 | -55.039299 | 2024-10-07 00:25:59 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4c55300-70d6-30c7-90d7-a4c9026f31b1 | -17.006001 | -55.041 | 2024-10-07 00:25:59 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5692b905-9a3f-32f0-bee0-5ce936ad557c | -16.300501 | -51.2658 | 2024-10-07 00:26:00 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 962476cf-604a-36f6-b883-73a6dc98bb83 | -16.180599 | -50.9002 | 2024-10-07 00:26:00 | METOP-B | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa544748-751a-3401-a55b-5c59ce15cbe2 | -16.183001 | -50.9133 | 2024-10-07 00:26:00 | METOP-B | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6a5039d-6aec-3583-af6d-c81367b69825 | -16.173201 | -50.915298 | 2024-10-07 00:26:01 | METOP-B | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f117218-d643-3505-8a08-a3f0440ef9ee | -17.147301 | -56.680401 | 2024-10-07 00:26:01 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README7.md)
