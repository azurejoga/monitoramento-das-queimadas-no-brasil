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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4058fe20-d94a-3cf2-8cee-83c6e0978161 | -5.71018 | -49.31248 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e043f082-6a5e-3419-ab87-ba374f88c02c | -5.70954 | -49.27335 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062700be-8b12-3c39-8d51-3668408070bc | -5.70899 | -49.27682 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ccaf21d-0e61-348d-9b46-2a66d063f07b | -5.70845 | -49.28028 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec148323-47e4-34eb-b1af-60020f96d73d | -5.70522 | -49.32235 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 354fffbc-8368-3371-a9f6-aea33d7dd7d8 | -5.70467 | -49.32582 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1e45671-5d85-3215-a5f8-2047f4228739 | -5.70237 | -49.95712 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 336201a9-962d-31c7-8775-8ccd88b1c0eb | -5.70181 | -49.96063 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ba1a59f-b4c5-328d-9050-583989f8b476 | -5.69208 | -53.75783 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4b83e5b-96d6-3e0f-84e7-c0ae2d8d9d8a | -5.68813 | -53.75725 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 179bbd8c-3886-3348-a455-79130874a521 | -5.64246 | -50.12856 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0361262e-df1c-3085-89d7-49acf3a31171 | -5.64027 | -51.59133 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 518cbdce-43be-343e-bf73-62a5ded4f754 | -5.63911 | -50.12803 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e8f085a-f6a6-3d74-b11c-99b38de30bca | -5.63676 | -51.59076 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d933fb4-59a9-3711-9472-115968801af5 | -5.62348 | -44.38181 | 2024-10-09 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3f59e7b-4d77-32eb-9025-b2cb7481cd9c | -5.62344 | -44.07214 | 2024-10-09 04:38:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb105f2-65d6-368a-b8ce-7c41bb31867f | -5.61965 | -49.99118 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77f8bb1e-66c0-37e2-a72b-dcabdfb8da9b | -5.6163 | -49.99065 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1b40990-7048-3190-9655-0216869beb7e | -5.60221 | -51.69375 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a42426e-429d-375d-b6fe-29544fa6ce4d | -5.60157 | -51.6977 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fdf4b4a-41bd-39ed-9296-9954825b94b1 | -5.59868 | -51.69318 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3009d1d7-f930-33e0-a7e0-90fd0feeb625 | -5.59501 | -46.37262 | 2024-10-09 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f225d0f-9123-35d4-8c79-f40c7b7aca41 | -5.58639 | -44.87005 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dfdcc049-0d86-3717-85e9-06a16a98dbbf | -5.58567 | -44.87482 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fcba0c3a-3697-3cc8-9864-e9128f1cd2bf | -5.58253 | -44.86951 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b481a597-bfa8-34bd-b434-46d7425b867d | -5.58236 | -46.31295 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 501dcddb-b336-3763-b3b6-61de2b22efa7 | -5.58181 | -44.87428 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 34de9cce-f6e7-3c81-ad63-826b4de2cc2e | -5.5811 | -44.87902 | 2024-10-09 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ecd56f24-59b5-34d0-aac0-26175d2dfcb9 | -5.5788 | -46.31238 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eca3d8b9-95fa-3c4e-ab16-8f0d6f626976 | -5.55811 | -47.03244 | 2024-10-09 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae0cb21a-762e-3593-86c0-fd7a1ab6455b | -5.55466 | -47.0319 | 2024-10-09 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7e55077-eebc-32a2-9e4f-8926a4d417fb | -5.55453 | -47.46437 | 2024-10-09 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40e972c6-006b-3549-94fb-dd0426b31d23 | -5.54557 | -49.58125 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159ef319-e2fa-3ac2-9b78-fb76ce64bfec | -5.53699 | -46.20259 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306a84e9-09d8-30d4-890f-2f48ff8ab0f7 | -5.53005 | -44.11594 | 2024-10-09 04:38:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38dd974d-d207-39bc-8753-aefc9697637d | -5.52735 | -48.36216 | 2024-10-09 04:38:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db35d61-a3fb-32d1-b0e0-ac67fcccdcdd | -5.52172 | -49.98965 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab5be908-f748-3374-9b5b-92b23f8543bd | -5.51918 | -48.98062 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c394874-402c-3d03-9f4b-da1b84d19691 | -5.51248 | -48.95828 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c66dde3b-e5f0-3737-918b-3a372959a889 | -5.50141 | -45.37967 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f657c77e-fc05-3207-ae3b-d93f84e83d36 | -5.49769 | -45.379 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebe8f110-ba79-3e99-b98c-d0e08f9fd2e1 | -5.48129 | -45.51215 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2dd76a6-d886-38fc-b006-8627b747661d | -5.47692 | -45.51597 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdc76b30-5fa4-3640-b0d3-420c8c1c2036 | -5.46291 | -48.28053 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e92a5247-fbbf-3fd1-b686-b8b0ba60e7b1 | -5.4536 | -45.49459 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08fcfb54-52ba-3703-8203-0b8cb08a4e73 | -5.44988 | -45.49406 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f37dbdd-948d-30bd-8fa7-a472e9386d33 | -5.44629 | -45.88836 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95638619-9eec-363b-b01b-ba2bd8540eef | -5.44402 | -49.56192 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3af47235-d7f6-3d77-ac79-075765c670d0 | -5.44347 | -49.5654 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e77b3bfc-8783-3f02-b26d-75789ca7a9b2 | -5.44266 | -45.88778 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2929060-10d8-3ae4-a8f3-3c42423da539 | -5.44069 | -49.5614 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc8b0046-3047-39c9-b302-46ca4e2df680 | -5.44014 | -49.56488 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a3982b66-685f-3da7-860c-982827da262c | -5.43297 | -48.31894 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06284312-ed60-3c9c-9320-cc6d6a8d39c3 | -5.43243 | -48.32244 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf388c5-d924-3b05-896c-988de817a0cf | -5.43201 | -46.00513 | 2024-10-09 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b583e601-2836-3be6-8300-d6e2e5af0756 | -5.43188 | -48.32594 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7060bb4c-0d70-3817-961a-b0af7a74e8ae | -5.43134 | -48.32944 | 2024-10-09 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0115ee1-b053-371e-8214-76e6546964fe | -5.34257 | -44.52522 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9454abd3-6022-340a-a2a2-56d85528571f | -5.34242 | -44.52852 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df71eab-18e9-31dd-99fe-09079e9e9643 | -5.32298 | -46.38251 | 2024-10-09 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695ccbe8-f862-3ea6-a9d2-8cb64b02c385 | -5.32236 | -46.38655 | 2024-10-09 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2656813c-ee81-3283-882e-39c0c8423ec3 | -5.3182 | -45.42266 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c9f7290-32c6-3d45-8a61-425f74a29796 | -5.31777 | -45.47676 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fdf2147-f2b7-3737-8be1-302790e1497d | -5.31711 | -45.48118 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ab1c4c7-e9c5-38f5-86fc-f18601bf8bb1 | -5.31607 | -45.47795 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a3e684b-f99f-3928-84e7-4158a864d7f8 | -5.31539 | -45.48236 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e756d765-ef1c-3f9e-b1c5-461d214763f7 | -5.31001 | -48.13762 | 2024-10-09 04:38:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c4d5cbc-d4f2-3c9a-be79-8a6268ee4479 | -5.30666 | -48.1371 | 2024-10-09 04:38:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a559b36c-443e-36e7-9dae-b525d69c9e36 | -5.28303 | -45.44603 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42636e27-25b8-3d4f-936e-d78762aff593 | -5.2793 | -45.44554 | 2024-10-09 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbe0d550-0d6f-37f2-8eaa-5f6b87c2213a | -5.26389 | -50.88303 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c9cee4-5474-32d8-97c7-32110533ddc2 | -5.26204 | -48.55268 | 2024-10-09 04:38:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e41f8c61-4f74-3b09-a0ff-29e9dac0c8e4 | -5.26189 | -46.14448 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c997672-859f-3a0d-8e52-3834bc63b954 | -5.26127 | -46.14857 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e9d4f6e-1362-3234-8fa7-44fbe33e6280 | -5.25831 | -46.14395 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 506c19e0-ca2b-3241-80aa-a8ccd765d7c2 | -5.25769 | -46.14803 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ecc80ff1-aa6b-33d4-b06b-d673182d3895 | -5.22511 | -45.14191 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bacc538-1639-368f-9a2f-97e56d511c5c | -5.20894 | -52.00396 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f40550b-fe22-3872-96a8-1fd80c92618d | -5.20828 | -52.00804 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da3b5c9-9270-39dc-a996-b426d8366b6f | -5.20663 | -50.60699 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47246435-959b-331e-82a9-78f117ea4cc0 | -5.20323 | -50.60646 | 2024-10-09 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d500b5b-4100-3cd7-916c-938e03d495f9 | -5.20172 | -44.53589 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf174c5-1b3d-3863-bf18-cc8f80c5de2e | -5.19489 | -48.22407 | 2024-10-09 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f10a4799-8ede-395c-b4e3-df63ceea7894 | -5.1733 | -48.27452 | 2024-10-09 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d022136-9a05-360e-8c38-b36d53442cf8 | -5.12996 | -47.52692 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e746f4c-1140-3b47-a62c-2b121c682df9 | -5.09518 | -60.2271 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c2a0fbc-5b74-363c-9926-ef819d0ef088 | -5.09435 | -60.23177 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d13c0f36-1e08-35c5-a0dc-0c417d58200b | -5.09222 | -49.58815 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a40fb120-4042-318b-84b6-33c6600c04f6 | -5.09167 | -49.59164 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7666512f-7774-302b-a9a2-f50aef914cd8 | -5.08989 | -60.22137 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92f1ed78-20ad-31aa-a0ba-48c49500bfe4 | -5.08907 | -60.22601 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9919ab8-53ea-33f7-8bd9-68bdaa55b45e | -5.08378 | -60.22026 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1c9c9af-abcd-32e8-ab8b-8e5c8e44cf0b | -5.08295 | -60.22491 | 2024-10-09 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c3e7c8-33bc-339b-b5fe-43df2208ddae | -5.07873 | -49.47907 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ebccb2-4bdd-3421-86a5-d554bda1a73d | -5.07302 | -46.13442 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 621af171-d61a-3d04-8d01-2fc2b53b693f | -5.06275 | -48.44341 | 2024-10-09 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468f34d7-4d26-3331-867c-6c71acfee885 | -5.06166 | -50.66297 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b95ab6-e6aa-3c7d-8ed1-a59e75ff7e86 | -5.03963 | -49.83437 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dc60d2e-54a5-3c88-bfbb-7faafd727b56 | -5.02092 | -50.87186 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37364c9e-5a9a-3f88-aaa3-633976c04bfe | -5.0151 | -49.77295 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README122.md)
