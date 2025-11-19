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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 965a859f-b454-32b8-8330-38bf02166c3c | -4.14842 | -46.79114 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 813acf4d-bf45-3a22-8ec1-5e506514bf02 | -5.61527 | -37.80464 | 2025-11-19 04:29:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 28a81f19-ec0c-3488-b096-635fa6a3dba6 | -4.11396 | -49.09584 | 2025-11-19 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fbb3f77c-8e3a-3bca-8da6-ad2206893297 | -7.14284 | -44.92242 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db69ea2-0251-3e97-b319-12a25db2b525 | -5.71439 | -42.73441 | 2025-11-19 04:29:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 251d270a-8a40-31f9-8e3c-974a7918e479 | -4.69425 | -45.88658 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a29506b4-c159-3e5d-94ee-760aba2eb28e | -7.63015 | -42.58132 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48d552a2-99fa-314a-a975-0a82a3821510 | -9.66391 | -43.89606 | 2025-11-19 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a96138d4-02af-39ff-94d0-39401c013ce1 | -4.16217 | -46.84365 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a0cf6b-4859-3a82-82a3-1ba791ba14db | -8.13308 | -47.59198 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6c08246-7948-3903-b9b8-d9e8caefdb2e | -8.31077 | -44.0585 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b182c59-3ec4-3307-8e03-f2e11179b788 | -4.29359 | -48.26346 | 2025-11-19 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c5b3d23-fba8-3e6b-b462-25e9bb6b994e | -6.7225 | -42.12709 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2694629c-45e0-34f2-a027-c651b488dc08 | -10.11439 | -36.3924 | 2025-11-19 04:29:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| db078b15-dcb1-3f0b-a5fb-7ef7e4c8676c | -6.43744 | -39.28022 | 2025-11-19 04:29:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89c6702e-d58e-3f58-ab1b-a33263319c3a | -3.01912 | -49.42492 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63b256b5-ea1a-34dd-8c3a-4f89a21f5559 | -4.5855 | -44.06749 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fac143f-eec1-346c-9afa-3864344866dd | -4.11031 | -49.09524 | 2025-11-19 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ff69c5-6d18-3c49-9e8a-ae0e871bae3f | -8.28477 | -43.94945 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f49280af-55d4-3e2c-84ed-59eadca2de11 | -3.0146 | -49.42886 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07df2e1-7925-3a3b-bc27-a797a546255c | -5.75344 | -45.10757 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c123ab03-5356-3c71-b961-08e874546cfc | -7.45333 | -45.19878 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a180196c-6b72-30a3-bc12-520a6e915b92 | -7.8381 | -42.16087 | 2025-11-19 04:29:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7575ac33-50db-3c99-885a-489ba73cee38 | -4.3663 | -43.61075 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a2e8139-849b-3c39-98c1-88b0905c8d26 | -5.71679 | -42.74321 | 2025-11-19 04:29:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6148bf9-f60f-3c08-bdb9-6aa826d26637 | -4.7253 | -45.66851 | 2025-11-19 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2a2bbf6-4996-3134-8780-0c1d4d9b5342 | -9.1064 | -48.90379 | 2025-11-19 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e60046e-d6a0-321c-8bfa-6c34ecade9ae | -5.6286 | -45.1714 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f6f4cd6-b230-3690-8584-af7f3f4d2b4f | -8.21803 | -50.47696 | 2025-11-19 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8db4a0a1-d2a4-38d7-a547-d2a491762983 | -3.84966 | -43.94857 | 2025-11-19 04:29:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 905c4fea-cea5-3417-b6c0-8fad40893792 | -7.63364 | -42.57923 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 34a90998-26a7-37c4-b86a-f52c0882b566 | -8.3896 | -44.06166 | 2025-11-19 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc2fcd36-4f69-3ce7-b48a-09bdfa6cf839 | -7.27944 | -47.90626 | 2025-11-19 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce8f4529-fe44-3648-b0b1-0629c2b22256 | -3.17653 | -48.61329 | 2025-11-19 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a789987-61ff-31ca-9243-ddf7e8c322d5 | -3.09795 | -49.2706 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f805bef-232e-32cd-9f39-5d470381c4ea | -5.23063 | -49.57796 | 2025-11-19 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae0cad65-a756-3d64-8712-65cc0d296e53 | -7.5856 | -46.8422 | 2025-11-19 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 737cd1f5-c8be-3a4f-a9eb-3d2d32ab1b26 | -8.34376 | -50.58219 | 2025-11-19 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f90592-29fc-3558-9bca-f1e81435f41b | -4.88063 | -45.86259 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61aa8e02-440c-32fc-9d8a-1a2ddbd9cde1 | -8.13421 | -47.5849 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c920c4-606b-3a7a-88d5-0adce86bbecf | -7.44218 | -45.19691 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99d3b237-88fa-3fb0-b1fe-e23b5b5b0366 | -2.28468 | -53.64759 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d534c0dd-e02d-369a-8c5f-e2851baa5134 | -7.55295 | -44.09393 | 2025-11-19 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6415d7b2-104d-32b0-a93c-7883f3cd25d3 | -4.11307 | -49.09855 | 2025-11-19 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1923fff1-4589-3aad-831e-a57249b1bf3c | -7.74053 | -47.25065 | 2025-11-19 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66327efd-af22-35bd-b89b-20672a0c0690 | -6.89878 | -38.91454 | 2025-11-19 04:29:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5c5fae86-abcb-341e-88e2-74193dea1bdf | -3.18014 | -48.61388 | 2025-11-19 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17b2b96-8073-3f7b-9eea-23de72f56e29 | -2.87697 | -52.61852 | 2025-11-19 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cb0e0ce-4db3-3411-989a-ab788bfdc329 | -3.98626 | -47.99863 | 2025-11-19 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e8e46c8-98fa-3591-91cc-2a81e738c2d1 | -4.72138 | -46.37614 | 2025-11-19 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a524f9cd-878d-381c-913e-dadc201daeeb | -7.18236 | -48.68012 | 2025-11-19 04:29:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f77ea3-5964-3e66-a854-76726b91c439 | -6.71613 | -42.12902 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b717e0cd-e902-3d24-bde8-e89f47b87f2b | -7.62056 | -46.85182 | 2025-11-19 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 72534700-4a7a-3e4d-80f9-f7b008daf1a1 | -5.02673 | -45.53503 | 2025-11-19 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15c86372-8957-3c7f-a456-6d094cebd655 | -4.15177 | -46.79166 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae4564a-7e99-36db-8983-7d338cdba9df | -8.87521 | -47.32829 | 2025-11-19 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9e07bdb-c761-3f6f-b283-1f28e8bf021d | -4.14619 | -46.78354 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360d563c-0c0b-3efc-b6b8-fb9757fe55ba | -4.14898 | -46.78761 | 2025-11-19 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a252eb1d-3b8b-3b91-9666-c252182f4868 | -7.1434 | -44.91883 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17a1d87e-9704-3669-8933-3b32e519e8bf | -6.71151 | -47.78967 | 2025-11-19 04:29:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ed699c-2c32-37a5-81fe-0b6af3f43c02 | -6.00242 | -39.51238 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d69a17cb-a222-34c6-8e3c-6e4540aced8c | -5.62525 | -45.17089 | 2025-11-19 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f82a3a58-653b-3831-8192-81524e5a414c | -4.99314 | -44.76161 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b51babbc-16ef-3a63-b6f3-0685c7e48de9 | -4.58266 | -44.06329 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d0b63ab-9ee8-3657-b3c9-4fe88b659185 | -6.2056 | -39.4003 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4818eb67-8e17-30ab-931e-69319addb844 | -9.11297 | -44.68077 | 2025-11-19 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1f4f52b-9fcf-31dd-9bc9-86f49ecff4d5 | -4.98697 | -44.75703 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebafcfee-6a4c-325b-944c-37dd2a43d877 | -6.71209 | -47.78607 | 2025-11-19 04:29:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22aaea82-5653-38dc-8c7a-312f2e4916f3 | -4.42606 | -45.91169 | 2025-11-19 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14340d8b-9839-3b85-9bc7-99bdefa510cb | -4.78655 | -40.25199 | 2025-11-19 04:29:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f886e20d-535b-36f9-b7bb-b3540db24936 | -6.21761 | -39.60279 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8e28999-192c-33b0-a5ca-ba34a6eaa440 | -8.81522 | -37.33751 | 2025-11-19 04:29:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f95a7036-a648-39a9-be8d-6129a99a7dd8 | -8.20369 | -43.02655 | 2025-11-19 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d77413a1-e15f-3da4-ba16-d895c703e938 | -6.71685 | -42.12428 | 2025-11-19 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d3e82117-674a-3e68-9475-344d6c02acad | -3.90253 | -50.66048 | 2025-11-19 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 23ae54c5-cb00-37d9-a21f-6a06010ec210 | -4.58608 | -44.06382 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33a34138-67a0-3f46-bb9b-dc0ac230f4d6 | -8.28742 | -43.94847 | 2025-11-19 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75170956-3d93-3367-9ae0-ef3abf7be339 | -4.6937 | -45.89003 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54ab0b29-158a-34fe-acc5-76ab19e18643 | -5.45693 | -50.74698 | 2025-11-19 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ac0d8b-1bd5-374d-9cca-885a07771f90 | -7.69489 | -38.68546 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7385bc77-318b-344c-8682-d001813cd78b | -8.13365 | -47.58844 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e82116c-7f9d-3a25-a4cc-7c8ee6459d31 | -5.71804 | -42.73499 | 2025-11-19 04:29:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68365e03-e46e-3c20-94e7-e31286626719 | -6.20102 | -39.39968 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 32c81ca2-c8fa-39c8-918a-37395ce21782 | -7.4879 | -47.15582 | 2025-11-19 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6dc79fd-6eb3-369d-a14e-47de419954f7 | -7.63085 | -42.57673 | 2025-11-19 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb23fc76-bc9d-3196-a78c-a97d0cc8c8ee | -6.22146 | -39.60787 | 2025-11-19 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c12fed2-d929-30d4-8d3c-588f865c8b9d | -7.43993 | -45.18924 | 2025-11-19 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c4f0a71-e5bb-3c18-b6c6-0fe6d260094f | -8.12752 | -47.58382 | 2025-11-19 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 359ce8e1-eeb0-3744-be0b-05f65ced106e | -3.01838 | -49.42945 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 978cb7dd-717c-30a0-9864-40b90264e488 | -2.21535 | -53.63656 | 2025-11-19 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd46574-bcda-3e15-9251-b175d9d2f6b3 | -4.76187 | -45.75537 | 2025-11-19 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbd46a8d-a572-3e68-bc21-9f4f87dd75a4 | -5.05086 | -45.12819 | 2025-11-19 04:29:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 974bcac7-d5dd-34fa-8425-937a74bb4dc2 | -4.87903 | -45.8942 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 845c762f-ba51-3f73-bd49-68e655b43a57 | -5.12553 | -44.05026 | 2025-11-19 04:29:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 701fc651-823b-32fc-87ae-9320bc9c49bb | -4.36284 | -43.6102 | 2025-11-19 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47ef231b-b0e1-3eb1-b089-922c0b1338b7 | -7.73997 | -47.25417 | 2025-11-19 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eb8d250-4b7f-35f5-97a8-6c31636f5003 | -5.0542 | -45.1287 | 2025-11-19 04:29:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92ca6df6-eee5-335e-8407-66db2fd335e8 | -7.43311 | -42.76276 | 2025-11-19 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62c84a9c-d940-39e1-80b5-1b1b8369aea4 | -10.11979 | -36.3974 | 2025-11-19 04:29:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34c4f33b-0050-3958-a7cf-4c95272a18bd | -4.98753 | -44.75349 | 2025-11-19 04:29:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README13.md)
