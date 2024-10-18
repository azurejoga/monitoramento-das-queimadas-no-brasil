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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9ffb56b-1e27-31b7-8a1b-de678b4a1144 | -23.369499 | -47.368599 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88f849a5-d602-313a-a029-25472e37e9a8 | -23.371099 | -47.376202 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94af78e6-82a6-3100-942b-9d5e14662d94 | -23.3727 | -47.383801 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c07e0ad-a6d1-33e1-be6d-2f30434345b3 | -23.359699 | -47.370998 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8a477f4-f445-3969-b436-90f9180c1490 | -23.3613 | -47.378601 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29a9fda7-f6d1-322e-b097-b827f36aef3b | -23.3629 | -47.3862 | 2024-10-18 00:50:17 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a875e24-7929-340f-bad9-2d7263012adb | -22.3605 | -43.347599 | 2024-10-18 00:50:19 | METOP-C | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd18882d-d14a-345c-93e0-a6a0900839dc | -22.3626 | -43.3563 | 2024-10-18 00:50:19 | METOP-C | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cb329de-1c40-3e22-8ca5-8695e4aa6eb5 | -22.4035 | -45.444599 | 2024-10-18 00:50:26 | METOP-C | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a680e8cc-7d9d-33e1-b583-6426e14c7a35 | -21.123501 | -44.069599 | 2024-10-18 00:50:41 | METOP-C | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d0cfb2a-b1a7-39ba-944a-f8589da6273a | -21.334499 | -45.876099 | 2024-10-18 00:50:45 | METOP-C | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 372d8b3a-361f-38b8-9436-f01e062870a6 | -21.336201 | -45.883499 | 2024-10-18 00:50:45 | METOP-C | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c7d7aab-dafc-39ad-a15e-3915b208c576 | -21.3379 | -45.890999 | 2024-10-18 00:50:45 | METOP-C | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 825302f1-532b-3f45-8523-2fdcb1ad3d10 | -21.9566 | -49.715401 | 2024-10-18 00:50:48 | METOP-C | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b4379d4-cb1a-37e2-96f8-62b7daf05ed2 | -21.9583 | -49.724098 | 2024-10-18 00:50:48 | METOP-C | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1657862e-14c6-3630-96ef-a02d5aa4e8b0 | -21.9601 | -49.7328 | 2024-10-18 00:50:48 | METOP-C | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ec9cf79-b9e3-3b0f-bdac-59f95bd5e7e1 | -20.9601 | -46.4608 | 2024-10-18 00:50:53 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0aac959-7c2f-3238-b1d9-96f25dec0a37 | -19.3652 | -41.604401 | 2024-10-18 00:51:00 | METOP-C | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8515c541-e093-3bd9-b43f-0f069fb47bdb | -19.368099 | -41.615898 | 2024-10-18 00:51:00 | METOP-C | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f61e730e-bf84-368c-8af4-237cde899f56 | -18.6073 | -40.999699 | 2024-10-18 00:51:10 | METOP-C | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bddb82b8-0176-3663-9267-d6cd4edb3948 | -20.792 | -50.685799 | 2024-10-18 00:51:10 | METOP-C | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6af3df7-c185-3a08-8df8-c219106be3a6 | -20.7939 | -50.695099 | 2024-10-18 00:51:10 | METOP-C | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2154e59c-cfa1-33f2-9848-037fe87d88cc | -19.3325 | -44.637199 | 2024-10-18 00:51:12 | METOP-C | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 93e7e116-b108-302f-802b-f3a788db28ea | -18.403999 | -42.195702 | 2024-10-18 00:51:18 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a831676a-e060-32ae-b834-c96e8760002b | -18.406799 | -42.206699 | 2024-10-18 00:51:18 | METOP-C | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4666df0b-4c41-3fdd-9fd9-65a2f148a66d | -18.3943 | -42.198299 | 2024-10-18 00:51:18 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4933bbba-c5a9-33af-98f5-57e5a7cf34b8 | -18.3971 | -42.209301 | 2024-10-18 00:51:18 | METOP-C | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26e39475-17b0-39b8-85a6-45e09148349c | -18.384501 | -42.201 | 2024-10-18 00:51:18 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a23ab16-e5ee-34ae-8eed-4b622256b025 | -18.3873 | -42.212002 | 2024-10-18 00:51:18 | METOP-C | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f603f719-3b5d-3167-88fb-116085183bf5 | -18.2917 | -42.203098 | 2024-10-18 00:51:20 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7392fc43-d274-3227-98bd-6f7d92cc868c | -18.546 | -43.2244 | 2024-10-18 00:51:20 | METOP-C | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bdcf0a1-700a-3eb1-80bd-94091283cbc8 | -18.548401 | -43.234001 | 2024-10-18 00:51:20 | METOP-C | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ac55c2f-db6b-34f1-a287-cdc203e2b3de | -18.282 | -42.205799 | 2024-10-18 00:51:20 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1175a201-7ec7-32d5-a5ba-18f1ab17f266 | -17.961901 | -42.501099 | 2024-10-18 00:51:26 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7564184-8ada-381b-bb92-6bd2a3f6b863 | -17.9646 | -42.511799 | 2024-10-18 00:51:26 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c75c069-19cf-32c3-ae96-d8949378bbe5 | -17.832701 | -42.3172 | 2024-10-18 00:51:27 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd71dc4c-1497-37a4-b0cc-7a9a4b4a3454 | -17.823 | -42.319901 | 2024-10-18 00:51:28 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ead60cf5-976b-3f91-8b98-aa68c8e90649 | -17.825701 | -42.330799 | 2024-10-18 00:51:28 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e74e8699-27cb-37d9-aa26-85c70cbc3c91 | -18.9979 | -51.409199 | 2024-10-18 00:51:42 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d06990f2-0709-33ae-9d6d-4cd315c6064a | -18.7771 | -50.871101 | 2024-10-18 00:51:44 | METOP-C | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| faa4e0c1-5906-3378-9875-45e649c330bf | -18.778999 | -50.880001 | 2024-10-18 00:51:44 | METOP-C | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e17cf58-3540-3aeb-8d43-aa28e9adb272 | -19.6266 | -56.970402 | 2024-10-18 00:51:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa1cd923-66d8-3b26-9fda-6234d2ce2417 | -19.630301 | -56.992298 | 2024-10-18 00:51:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c37dc08-96fd-304f-ade2-c8f866a26f11 | -19.616899 | -56.972099 | 2024-10-18 00:51:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e8a4cf77-84bb-37ad-912d-fa1f1f7de153 | -19.6206 | -56.993999 | 2024-10-18 00:51:48 | METOP-C | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f7b2f3c2-34b4-37d9-bbe8-ae651bf7fa95 | -19.607201 | -56.9739 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4dfd46aa-1270-3c0e-be64-3a8cb2b93a3f | -19.610901 | -56.9958 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e19e688-5d22-3bd3-9f35-465c5a406de7 | -19.614599 | -57.017799 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58d039d8-acb4-3370-8784-a17112e09a4d | -19.5975 | -56.975601 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 92aabb92-b3ac-3779-bba5-b82e8df3426c | -19.6012 | -56.997501 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1a1de2fd-9e57-360f-ac70-e0476d3e366d | -19.6049 | -57.019501 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8864f389-05d8-3641-9700-b1d0dcd87927 | -19.608601 | -57.041599 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 320c8570-ecb8-3fc6-9ae9-85c39efe5e1e | -19.587799 | -56.977402 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d76efa37-e0c3-3a20-9741-f52c23363d2a | -19.591499 | -56.999298 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca45f9b8-edb2-38b1-819f-b3dfb2bb5537 | -19.5952 | -57.021301 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea02d9b2-da07-3e25-80b0-baad14c6feb6 | -19.5989 | -57.0434 | 2024-10-18 00:51:49 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 45e7b6cc-364e-3860-9146-edd1afc641f1 | -17.187901 | -45.4566 | 2024-10-18 00:51:50 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a6d70a6d-fee5-3334-a103-706ea3d9ceb0 | -17.1898 | -45.4645 | 2024-10-18 00:51:50 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f559ae54-898c-358e-900a-a90b7a7c00fe | -17.191601 | -45.472301 | 2024-10-18 00:51:50 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b557dcc6-4743-3c16-a595-5808f4ef401d | -17.193399 | -45.480099 | 2024-10-18 00:51:50 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a800d2b9-aa56-3786-95af-2f6dc8110d8e | -18.657499 | -57.3274 | 2024-10-18 00:52:05 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10c2ce09-b557-39c6-95be-16c44b61e996 | -18.251101 | -56.600601 | 2024-10-18 00:52:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6ff6c52-a822-3955-8af6-16baadbc7b0b | -18.254601 | -56.620399 | 2024-10-18 00:52:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72d883e6-ebe7-3759-b4cb-5b8842d661b4 | -18.2414 | -56.602501 | 2024-10-18 00:52:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 05e47d0c-2f7d-323f-b960-6575af069ddc | -18.2449 | -56.6222 | 2024-10-18 00:52:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 070a4a92-a148-32f6-a1d0-951bccce0d23 | -18.006399 | -57.263901 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 35b7fdf5-32eb-3fbb-b414-e58523637074 | -17.992901 | -57.244099 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a6e563a-dcf0-3a19-b64d-7b81ca7031bb | -17.9967 | -57.265701 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a113253f-417d-33d7-be58-f9044937aa49 | -18.000401 | -57.287399 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87dc9bbc-9c70-3164-b516-ed00af55f0e8 | -17.983101 | -57.245899 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 523e15b4-27b8-3d8a-bb02-98a33a251f53 | -17.9869 | -57.267502 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98d2dcc0-cc8e-368b-89e3-fd9b0455372a | -17.9907 | -57.2892 | 2024-10-18 00:52:16 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cddfc291-69ff-31e1-b241-eb04e0eed031 | -17.9697 | -57.226101 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ade6812a-7789-37dd-9cab-e41f34ba15e9 | -17.973499 | -57.2477 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f07255ce-53b3-31b8-a764-e4316c534406 | -17.9772 | -57.269299 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 361b4411-f07b-355e-a95b-f24a338ec44e | -17.981001 | -57.291 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 61baef4b-f8f7-3a86-9aab-a47c52ebefcf | -17.959999 | -57.227901 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 19a1637b-39b4-3aa1-aa4b-d43346096fc9 | -17.9638 | -57.249401 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf344f34-3326-34de-946a-247a33bb21a2 | -17.967501 | -57.271099 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e433cbd-4746-3345-bb7c-03a8aa58426a | -17.9713 | -57.292702 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c8ae6bb6-bf8d-331d-8663-ceba5cd82130 | -17.9503 | -57.229599 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b521126d-611b-3a49-85ce-bdec19243077 | -17.9541 | -57.251099 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c29ddac7-528b-3b55-ba01-f22a3249c50b | -17.9578 | -57.2728 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b659c54-9a01-391b-ad9d-150e5d1ef32f | -17.961599 | -57.294399 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dbde6975-3edf-36fb-a947-e9b368fff3c4 | -17.940599 | -57.2314 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c59938a9-a951-315c-8cec-9593b6d8abe0 | -17.944401 | -57.252899 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc4d6dbf-277d-3872-9d51-9f79b575b976 | -17.948099 | -57.274502 | 2024-10-18 00:52:17 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b08cd9d-9de9-3ede-a5c8-af832bee9546 | -17.9457 | -57.4333 | 2024-10-18 00:52:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8fa2a47e-43c6-3edc-852a-4c57a3d20857 | -17.916599 | -57.438599 | 2024-10-18 00:52:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d3d91574-4c04-356c-9705-5a115ca9db81 | -17.8874 | -57.443901 | 2024-10-18 00:52:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e54ef908-3c85-3fee-89bc-bc2fdd66f28f | -17.8293 | -57.454498 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c7f8738-5516-3e85-aea3-83665e33366b | -17.833099 | -57.4767 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b02d7d3f-2bed-336e-8811-656a3752c7b0 | -17.819599 | -57.4562 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f3e63a2-0f98-3f22-8f15-8242e9cf7325 | -17.8234 | -57.478401 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ae6e578-9f12-3ca0-b94c-091585736525 | -17.8099 | -57.458 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9406a164-c7f2-34fb-8579-d49463ef6e61 | -17.796301 | -57.437599 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 073a9b14-babf-3775-b1be-f7d2b5ac8766 | -17.8002 | -57.459702 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5241dba2-ffeb-3be1-9b18-3abf8d010bae | -17.804001 | -57.481998 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2b88ddb-55b1-312c-8e69-a28613ee6597 | -17.782801 | -57.417301 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c7ff454-aca9-39f9-9744-d071d99f207c | -17.7866 | -57.4394 | 2024-10-18 00:52:20 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README9.md)
