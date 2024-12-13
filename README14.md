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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94527a0f-9702-3cf7-98d5-e572d27f26f7 | -12.76503 | -49.31137 | 2024-12-13 03:57:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dea9ef2b-2169-3b2d-96c7-0d5513fc9d75 | -13.05292 | -52.03771 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ab75c13-719f-3a03-be7f-83433d42b027 | -11.21232 | -53.83323 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8687eebc-d222-3793-9241-df963f68a66d | -11.86347 | -46.94927 | 2024-12-13 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fb06c68-efb2-33e2-8f85-c1d16e0b1484 | -11.20477 | -53.81727 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 37710b8e-64dc-3aab-bc68-72bbba28652f | -11.20189 | -53.83111 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4a6d661c-b9e3-3aa5-b1cb-f18ee4f931f8 | -11.48095 | -48.23196 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b42dd62-ee6a-354e-bfcf-9798d8debd95 | -11.48545 | -48.2312 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7769829f-f5fa-3cfd-80b2-4a01399245b6 | -13.6216 | -44.08687 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c4adb5d-cf5f-38d7-9b8e-8a48fa1312d5 | -11.69059 | -48.07481 | 2024-12-13 03:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8448e3fe-9e2a-3889-b4ee-65bb1dcf71ec | -14.15865 | -39.02129 | 2024-12-13 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0dbcb14c-994b-3176-bf82-be3336a766e6 | -13.57626 | -41.99223 | 2024-12-13 03:57:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be88c1bd-c616-3b85-994c-68363e802266 | -12.05385 | -46.88867 | 2024-12-13 03:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 923546c1-0d98-3350-940e-411e93f2682c | -12.10678 | -44.75662 | 2024-12-13 03:57:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19bb29d1-b4d9-3375-a11c-b4269e6b1aa9 | -11.49135 | -48.20343 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e9da278-ae2e-37f8-9f53-e111f20cfea1 | -9.13851 | -49.48417 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d3c43bca-205b-3a00-8fca-a4f8661807ff | -12.38447 | -51.4535 | 2024-12-13 03:57:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ac1e3cb-5c46-3835-9b66-a155e6c51def | -11.49726 | -52.91876 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92856628-6150-3ca9-b5e6-bc9373e11ba3 | -9.19485 | -49.47802 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c648254-2433-3157-8040-850a13d09567 | -11.24956 | -44.66287 | 2024-12-13 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a315c8da-b099-3525-b793-24f2b753958a | -12.35718 | -44.71112 | 2024-12-13 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99ba2444-1073-3611-bad4-2309e6fa494b | -12.02943 | -49.55123 | 2024-12-13 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5127253-550f-3c26-b9d7-dc9e4c69ae36 | -10.3243 | -42.39581 | 2024-12-13 03:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7cc48a95-ff76-3ad8-af03-4385a05d47d0 | -11.49477 | -52.93094 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a44f0d19-5a91-3476-85a3-1e172440b33e | -11.48043 | -48.23023 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6366707c-871a-3d01-98ec-84a266b5b7f7 | -13.87115 | -42.94759 | 2024-12-13 03:57:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f38be701-536f-3392-b18f-66aad1e6ae0b | -11.49602 | -52.92481 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1162fb4-5114-3f17-a8af-9d009d060e67 | -11.81668 | -46.60993 | 2024-12-13 03:57:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e49bb2dd-2bcd-3cfd-8550-3767c78052e3 | -12.38443 | -51.45083 | 2024-12-13 03:57:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dd63663-0177-3502-912d-f92623dcb3fa | -10.60589 | -37.00591 | 2024-12-13 03:57:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5d1f02cd-9c9b-3e60-ba23-ed6e67ced915 | -13.60972 | -43.97717 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68978c60-fa46-3a58-adf7-a9bbedf165cf | -12.38352 | -51.45542 | 2024-12-13 03:57:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ab183e4-96b8-3352-9057-8319e9c04ad2 | -11.48149 | -48.22898 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d03738a-1bf2-3c88-af55-0338dd578f4b | -9.16342 | -49.47657 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f731e7f-5ed5-351d-8ebc-335db483396e | -9.16269 | -49.48056 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 56f959bc-799f-3ffb-a324-f8e18cef7e99 | -15.5112 | -43.19561 | 2024-12-13 03:57:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8c9ee66b-1242-31ea-9c9a-5b6938888fcb | -9.9024 | -42.11177 | 2024-12-13 03:57:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1b96650-6e75-3948-a31a-c83a3ade2ab2 | -9.16906 | -49.47786 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 014520ac-921b-3571-970a-90d5dfa504d2 | -12.30122 | -50.09115 | 2024-12-13 03:57:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df5d1832-512d-3815-9522-ca560bafbbc0 | -11.47809 | -48.21918 | 2024-12-13 03:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d1eb9fa-91a8-39d4-bb0b-7ad61e95da2a | -11.20668 | -53.82495 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1b135123-0e4a-361f-bd68-8e217686896c | -12.75202 | -48.34636 | 2024-12-13 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aba46726-13c8-3089-a415-c0bf4642dded | -11.20369 | -53.83895 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 419e931a-b15b-315d-8aa5-52bec4962044 | -12.65731 | -46.57738 | 2024-12-13 03:57:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23964925-a94b-3c06-8a54-64c0c27eaf16 | -9.19245 | -49.47838 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12bc1ccf-cf3a-3786-9585-01f0c3746035 | -11.20816 | -53.81807 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d1c8c18-41d0-3714-8e66-c1d254417d79 | -11.21048 | -53.82537 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3dc0078b-d679-3c4b-ba72-bae47dd59bea | -9.19316 | -49.47448 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e02812f3-c5ee-36b8-9532-e617065cf0c4 | -16.923 | -43.59801 | 2024-12-13 03:57:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9150dc22-6b25-3784-9769-34a2e13127f3 | -12.76567 | -49.30803 | 2024-12-13 03:57:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d83e7b90-218d-3a66-8c5d-674cef0e0dca | -11.20519 | -53.83192 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| add15086-e69b-3d67-99e1-5d22690dd4a3 | -11.19619 | -53.82299 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41e0191b-dd5d-3037-9ee9-44aea14ce959 | -11.20044 | -53.83809 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2ad6cc77-fbdb-39d0-adf2-7383850a73d4 | -13.07364 | -52.03135 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5fc5a2c6-6879-3303-ac0d-066ce06e1ad5 | -8.43176 | -49.86901 | 2024-12-13 03:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a74a3980-9e08-3a68-9423-7938d515c987 | -13.07159 | -52.04135 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5212088c-599c-334c-958e-5e46ed4d89fc | -16.18484 | -43.77222 | 2024-12-13 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 726b5b1f-b82b-3334-992c-9d702d79611e | -9.13775 | -49.48821 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6d51d49f-e108-339d-b106-5263b19627ac | -12.1084 | -44.75472 | 2024-12-13 03:57:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 280a0a94-6017-3935-b943-f04f77f2a3ec | -13.70255 | -43.98301 | 2024-12-13 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4616f0f-16ff-36ea-ad7e-8c5203b509c7 | -11.20334 | -53.82415 | 2024-12-13 03:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b847bcd8-24d3-3fbd-9f41-f7576b25a78d | -11.81752 | -46.60534 | 2024-12-13 03:57:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f25da1-ae55-3f31-bf3a-b38e7b0afdfa | -13.06642 | -52.03501 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3f66327e-9fa3-35a9-babe-c24d65c619cf | -9.82738 | -44.1807 | 2024-12-13 03:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a888dd9-546d-3edc-ace3-780a6d65dd17 | -13.0643 | -52.04532 | 2024-12-13 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9aa9e6eb-c559-36ba-bb66-1e5a141f5718 | -9.20055 | -49.47895 | 2024-12-13 03:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 919e717d-6eef-32f2-90a0-83a010e653da | -18.03631 | -44.42536 | 2024-12-13 03:59:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bec34c4-8dac-3c9e-a935-ec443c897aa8 | -12.5497 | -57.7196 | 2024-12-13 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 226f9060-ed8b-3709-a881-2b45872090f3 | -5.211 | -43.2833 | 2024-12-13 04:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 50a8e789-dd78-306a-a3b2-8769bd856386 | -2.4923 | -51.8027 | 2024-12-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 5b7fde0f-8e16-3cca-b837-d854571bdd98 | -6.9156 | -43.5418 | 2024-12-13 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| ab8041af-71c6-3171-9974-cc37fe274b6e | -5.2298 | -43.282 | 2024-12-13 04:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| af6af97f-b321-31ef-bb5b-80456619f301 | -6.9346 | -43.5168 | 2024-12-13 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c74b7f6d-2ab6-3575-94d1-025c6c453645 | -12.5499 | -57.6996 | 2024-12-13 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7d0d7c57-211d-3cec-87c8-f2075387a2c6 | -6.9158 | -43.5185 | 2024-12-13 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d654454e-d2eb-385f-8a25-6905fb213b15 | -11.1959 | -53.8348 | 2024-12-13 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8cdf7d24-9f5b-31cd-b912-a3f8139639a1 | -5.2108 | -43.3067 | 2024-12-13 04:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 9cbbdda4-6b80-31c3-baa4-8ba3d314c679 | -6.9344 | -43.5401 | 2024-12-13 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 13cef2f8-6eeb-3a0c-b4e2-8b2ff432cb2c | -11.1962 | -53.8142 | 2024-12-13 04:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 81623d75-ed82-31b7-879a-122b2811757a | -13.0644 | -52.0326 | 2024-12-13 04:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9398798c-f2ef-306d-b779-1c531f3f5538 | -2.5108 | -51.8023 | 2024-12-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a857a407-378d-3bc7-a343-a59744d69ae4 | -14.7848 | -52.642 | 2024-12-13 04:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fdcc54d5-3441-317c-81b0-70a768a87950 | -29.62437 | -51.97248 | 2024-12-13 04:01:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 00165dd9-1eb9-305b-a679-4a18e2643554 | -29.62202 | -51.9752 | 2024-12-13 04:01:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0a9d41f7-5ab8-31ff-8100-0e9d3e040931 | -28.58488 | -49.44423 | 2024-12-13 04:01:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f0c3c0a-7f88-35cc-8229-2c7efecbf813 | -29.62311 | -51.9701 | 2024-12-13 04:01:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| aa93b70b-4183-3a13-b0b9-057a625ffcbe | -23.33859 | -46.77182 | 2024-12-13 04:01:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1b364bb-8b03-3afa-937c-e724a7c8e19d | -12.5499 | -57.6996 | 2024-12-13 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 78c3e328-5793-30c9-993c-3c696bb9c935 | -11.1962 | -53.8142 | 2024-12-13 04:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 671df114-a874-3a1b-8f19-5c0bf49f454a | -11.1959 | -53.8348 | 2024-12-13 04:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 46e10e60-a092-39a9-803c-3a780e14d0cf | -13.0644 | -52.0326 | 2024-12-13 04:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e1d0db1a-c305-3836-a889-dc1121614b4e | -2.4923 | -51.8027 | 2024-12-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| cd7426a1-c994-3f64-b7f2-212263e79343 | -2.5108 | -51.8023 | 2024-12-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 989d3a16-e948-3c55-ac97-9cff03bcdb33 | -5.211 | -43.2833 | 2024-12-13 04:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ee3faa29-8d15-3760-859b-30efb095bf47 | -5.2108 | -43.3067 | 2024-12-13 04:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| cf9d223c-c1ec-3a0f-aeef-58a59df0e67f | -11.2148 | -53.833 | 2024-12-13 04:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8af937ef-8f44-3ef4-a1e8-916251356139 | -12.5497 | -57.7196 | 2024-12-13 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 00a39522-0667-3cac-bb12-e31bd452f569 | -11.2151 | -53.8125 | 2024-12-13 04:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 1f8d205a-5c35-3e6f-b1b6-331cfdffb495 | -0.7496 | -47.7594 | 2024-12-13 04:18:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02a32b81-6111-3f88-a2b2-9ec0e2a95ebf | -1.57607 | -46.04121 | 2024-12-13 04:18:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
