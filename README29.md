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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9401d348-2375-3a21-a0f3-fac711e8da23 | -17.95956 | -45.00144 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d03b69-5b77-3132-9b97-37035714f628 | -17.38283 | -46.88182 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd070128-e6e7-3a06-8279-2535d06386d3 | -18.40401 | -45.24746 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dd5428f-8d69-37e1-974d-9e7ef93c62c3 | -19.17776 | -43.52897 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eb9b711-c64e-3407-bde2-2751b64105ab | -19.50208 | -43.83614 | 2025-10-09 04:02:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 480dd2af-8bd8-324d-aad9-12185d9b6a25 | -17.94925 | -44.41516 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50144240-029f-3654-a332-533bda5ff046 | -17.65294 | -44.43946 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b289dc7d-f7f8-3416-92cc-8f06807543d6 | -16.14287 | -47.88293 | 2025-10-09 04:02:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b215f0b4-16ca-3c67-81af-162a35a6fe9b | -18.00541 | -44.98353 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d72d8983-aedd-3692-b8b9-1af3e79055bf | -16.27298 | -47.14252 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43415ddd-ac6f-3d2f-aac6-fb37d7349912 | -17.37679 | -46.65868 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4538c76a-b514-3e9c-a9aa-793ff98ae670 | -17.38782 | -46.87848 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 996a31f2-b76f-3c3d-b6ba-ae1661ef6386 | -18.05218 | -44.95888 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93cd496d-8be3-34d7-9043-054e7f437356 | -16.2773 | -47.14085 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d518632d-2956-3796-8871-e9d4a635f406 | -17.21475 | -47.65504 | 2025-10-09 04:02:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e2bb4a44-1018-375d-9c26-1ee2006c3ec9 | -16.28766 | -47.13404 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2445e3b5-56d7-3ff0-8952-d09baaea68fe | -17.37267 | -46.65772 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4300e773-bf64-399b-a070-865e93cf8eba | -18.0684 | -44.41901 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 098e2533-343e-303d-9684-e0c1acd6d7de | -17.27324 | -46.91042 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88ed8d6c-7112-3e45-b482-2ac344b806f0 | -17.6073 | -47.18337 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ac0bea9-30b4-3628-92d9-59513d487610 | -17.08038 | -43.36768 | 2025-10-09 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb695890-1e9a-39de-97e7-7ca88a370464 | -17.52428 | -46.7492 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| df03bdb6-d1ee-37ba-8dd0-aaf2e6a1ff16 | -16.63074 | -45.4292 | 2025-10-09 04:02:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b86d0a8-3439-33c9-b0a8-27b7369c8818 | -18.05742 | -44.43742 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf3194c3-14c8-3238-ae80-b1d91b993da3 | -19.17431 | -43.52832 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b82d91fd-8780-383c-91b4-187846e9a1be | -18.18578 | -47.42474 | 2025-10-09 04:02:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c08f321-9f1e-3930-9bb2-d3121254c715 | -17.92769 | -44.60521 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7365578e-121b-3a84-a372-c5d56794a05a | -17.26665 | -46.96969 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| c2d5b56c-7e35-3e58-b759-64fa2150c6a5 | -16.61832 | -46.76852 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70f48af9-0e15-3fd4-8ee1-d6c7671de594 | -17.21918 | -47.65602 | 2025-10-09 04:02:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62e6d063-f8ad-35d4-ae3f-143b5cb8dbd0 | -17.46285 | -43.39084 | 2025-10-09 04:02:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f97ae092-6370-3d37-bda7-f248636fbf68 | -18.04181 | -44.95221 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2af8f043-a86c-3a81-b5cb-ebb7f94dc0c5 | -19.40826 | -44.35541 | 2025-10-09 04:02:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23720290-a3cb-3b41-992a-d06faa8e58d2 | -17.95499 | -45.00545 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14b95d87-dd58-3ba8-873d-e716f7a2ec48 | -17.95455 | -44.98596 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1c64ab9-b163-3f5f-bdca-58fc4604a774 | -17.3395 | -42.11441 | 2025-10-09 04:02:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe782cbf-65e2-3206-b2c1-91457fca840b | -18.99289 | -43.08591 | 2025-10-09 04:02:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7bb620e7-7953-3039-b541-8f4724f8f7a4 | -17.95815 | -44.98875 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8184b157-b225-341d-b096-7789a18f1406 | -17.63558 | -47.19804 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3494b567-cbd0-31c2-ac62-72ce59cb081c | -19.87272 | -44.0363 | 2025-10-09 04:02:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56f06ace-d113-3667-9d97-941773a3734b | -17.88601 | -42.87042 | 2025-10-09 04:02:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cfda590b-d266-3235-9fe1-316beaa672ee | -17.89415 | -44.26043 | 2025-10-09 04:02:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01c801c7-7630-3c15-aa61-ff3bbff19049 | -17.95651 | -44.41652 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce9c0c61-2821-3015-9633-c7fd69c360e6 | -17.95474 | -45.00749 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7fac66fb-3786-3601-b45b-b7a589a27487 | -17.56389 | -43.5212 | 2025-10-09 04:02:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8888278e-5841-33ef-b7ee-5721201ed3ee | -16.14743 | -47.88401 | 2025-10-09 04:02:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b9e732-76ad-32ea-a1f6-a8ab9105f82c | -17.98098 | -44.96927 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c734e2d0-521f-3d81-8783-a48a1ff0493c | -17.54139 | -46.06759 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d16d991-a79b-3f9f-83fd-fdc5faf03c9c | -17.26241 | -46.96882 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ec31b06-72da-37c2-a241-3159eb46c2a5 | -20.29945 | -49.69677 | 2025-10-09 04:02:00 | NPP-375D | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b32c4fb7-f824-398b-8c20-c08bdb64d1b2 | -18.61406 | -43.31992 | 2025-10-09 04:02:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9f7a452-a992-314b-bab3-c22a4235dafe | -17.95229 | -44.41921 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f65f81e-96d9-30d2-bd90-9fdc03e91448 | -18.0439 | -44.96216 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7037c827-5857-3af6-8436-18571c3fbcf0 | -18.5412 | -45.06741 | 2025-10-09 04:02:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac43fea-bb0d-31e9-b726-446481bbf08d | -19.7444 | -42.20063 | 2025-10-09 04:02:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d4a28ec-3f75-351c-80c4-55d68b3f0079 | -17.95211 | -44.4203 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae4fba0-8d7f-33c1-9a67-fe07a5b30a5a | -16.28167 | -47.14167 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22ae1b66-a814-3ec0-8e43-3fa7bd8d684e | -17.41433 | -46.54967 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b6df102-3b45-3233-804a-69d26876640c | -18.06857 | -44.41691 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94851e01-3f55-3a28-bc91-7e9e8a4ab793 | -18.30127 | -45.43413 | 2025-10-09 04:02:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42cc6d7e-328e-36cf-bb16-4813ffd695c3 | -19.55214 | -44.05022 | 2025-10-09 04:02:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3221ac2-91a2-3675-ba25-22257dff7578 | -18.41317 | -45.23978 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d63b9379-5328-3ab0-a8e7-5fe6271c3602 | -17.37785 | -46.8851 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c903c09-2e8b-354a-a287-aed5aaeee2d8 | -17.37279 | -46.88884 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 409c1a29-1a44-3631-96e3-f7cca4a8756d | -18.03349 | -44.99918 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 965e406f-e24f-359d-a1f4-0e9851f6ca0a | -18.68538 | -43.70555 | 2025-10-09 04:02:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 118d227d-1d54-3ebb-a75c-512107937afd | -17.53 | -46.05801 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f32e5b40-0bbb-374c-bc5e-e483587874cc | -17.37202 | -46.89297 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 805c768d-5b74-3605-9d6c-d4dab438c5c8 | -16.71484 | -49.75706 | 2025-10-09 04:02:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52e169c6-3d9a-3563-990e-d118cc5c7748 | -17.24098 | -46.94223 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57b1c05a-b134-30c0-b4c8-a2532e60799d | -17.95207 | -45.00012 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e153abdf-d1e8-36b3-b75b-6abce7dda78f | -16.72593 | -47.61771 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 913af7a5-c9b3-3d55-a6de-139087694299 | -16.42291 | -47.82632 | 2025-10-09 04:02:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec284bfa-245a-3d38-9a5f-f5c65b614bcc | -18.05814 | -44.43512 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa80ea58-5481-32a1-ae9b-2b9950a6af77 | -17.26317 | -46.96476 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e81e84-fa1a-3e71-afe5-9150fc303748 | -16.28335 | -47.13293 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b03c3be6-df71-3186-8485-193ab49eb998 | -16.61754 | -46.77269 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20ceed4f-8695-33e1-b00e-1c911827eff1 | -16.71035 | -49.7528 | 2025-10-09 04:02:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b033f2e3-cd73-3ac1-8d3a-3b9e2c3088dc | -17.41845 | -46.55053 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 745190d8-e162-32d2-8fac-88a2545b5f8b | -18.08558 | -44.44767 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df0243e8-81df-3864-95b5-1a1543e31c02 | -17.89056 | -44.25967 | 2025-10-09 04:02:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09aaca80-985c-3f25-ba29-f4beac16e1f8 | -17.38471 | -46.89526 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23e9ba30-4034-3205-9ca1-8bb8ec4e7acd | -18.78582 | -44.61677 | 2025-10-09 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a4783cb-1641-3828-8c0b-c2331f75270a | -17.26481 | -46.90865 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96340d83-9d58-38ce-b1ae-f0656af242a9 | -16.70253 | -47.59439 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d906d94-6c28-34af-bbb2-962a585b3ffd | -17.38708 | -46.88247 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 857974b1-c1a0-3c72-b763-2c6a8ecc4e0f | -17.33249 | -42.13614 | 2025-10-09 04:02:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a3729e5-0258-3673-b5e7-e4672986f325 | -18.08195 | -44.447 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 964dc552-cb54-36d3-96b6-f2d7dc5b5296 | -17.58545 | -46.07544 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb483f7-b58b-333e-bb1d-e287c8785bc4 | -19.71684 | -43.99575 | 2025-10-09 04:02:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fd58c3-9c8f-3f4c-a66c-98eb9e22701b | -17.92845 | -44.60085 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 168ea073-0341-3b2b-8c72-379d7d8ce03e | -17.15942 | -43.43264 | 2025-10-09 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34d7fe00-14a5-3d93-b94a-d8f34a310342 | -17.64929 | -44.43877 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df0e39fc-7d42-3ee1-b605-40ff63399313 | -18.54204 | -45.06274 | 2025-10-09 04:02:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99951ff2-1364-3f6b-b0e9-656befcba018 | -18.03266 | -45.00387 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1e7f8cf-c3cf-3d1c-a87e-d3f4bcbe52e5 | -18.04265 | -44.99098 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb0aa23e-9cfb-31ad-aaf5-b2906e94bf88 | -16.69895 | -45.00658 | 2025-10-09 04:02:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67ec4bcf-96ea-3107-a754-704ad9648441 | -17.95581 | -45.00078 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44e0a8ca-66ca-3bf8-b9e5-70b405cea716 | -17.62971 | -47.20562 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d14956b6-c3ed-3ce7-93f1-7f42c3c256a8 | -18.41403 | -45.23502 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |


[Clique aqui para ver as próximas entradas](README30.md)
