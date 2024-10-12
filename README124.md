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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17de9565-08f7-3a7c-a88c-4cb243daa1b7 | -17.86869 | -57.32932 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f0f38c99-8fd2-37cc-9251-3c1dd50c8683 | -17.86812 | -57.30091 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 175381d1-5be1-3973-93fe-327b0d1ecb10 | -17.86761 | -57.30489 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 42718947-2ba1-377a-8741-6ee6331f0022 | -17.86709 | -57.30887 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 6a9d2260-2f77-3a2d-a101-d93804c5f50e | -17.86657 | -57.31285 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 4f9daf44-db7e-3a7b-ada8-022b3445a3f4 | -17.86605 | -57.31682 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 493a453a-b30f-3a59-bc6e-45345086019e | -17.86554 | -57.32079 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| fa1fdd87-52c6-35cd-aa4c-46c0a62f2725 | -17.86502 | -57.32476 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 4078f045-3821-36bc-8bc6-106fc5d4a9bb | -17.8645 | -57.32874 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5aa82904-d6bc-3edd-99ab-883293d4a6df | -17.86438 | -57.26378 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 04621e7a-3c67-3bfc-814c-761cc957e25a | -17.86399 | -57.33271 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 20689de1-8e19-3409-921c-891d6d49001a | -17.86393 | -57.30033 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d80076ce-c71f-3b87-ba4d-f748bce82ce9 | -17.86386 | -57.26779 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8652b37f-b656-3e41-8be5-c6f496b6d431 | -17.86341 | -57.30432 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 5ae27af1-4290-3500-bfc4-99160759eedd | -17.86289 | -57.30829 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1457cd1d-7d79-3673-9d90-e9a73c368f6c | -17.86238 | -57.31227 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| f11bd660-02e3-34f9-a3b4-609d842b72c7 | -17.86186 | -57.31623 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 5271dc3f-a8be-37bb-98f1-93ceec801918 | -17.86135 | -57.3202 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 24e5c35d-68e0-311e-881c-04c0a97bc3da | -17.86083 | -57.32418 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 35935ef0-c231-3a8f-a37e-944c62d5a015 | -17.86031 | -57.32816 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8155d93f-2b4d-33a3-9d7d-e692d88515b3 | -17.86024 | -57.29576 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 01b4d5a2-e397-3a84-bbca-91b572172b4d | -17.86017 | -57.26321 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 41b55b3e-3470-3804-abbb-4e8a174017fc | -17.8598 | -57.33213 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4f0681ca-6a67-38d3-95f1-205dbea509cc | -17.85973 | -57.29975 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8637c57c-c757-33f1-b651-23f16b39b718 | -17.85966 | -57.26721 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 49bc2660-1c38-322c-989c-601bb60fb015 | -17.85928 | -57.33611 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3df68359-4cf6-3a21-bce7-1a3ab690a154 | -17.85921 | -57.30373 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 92e5ba7c-2e26-37e8-91a7-54c774390fb4 | -17.8587 | -57.3077 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cf7f12cb-dc08-3a72-aedc-f7b6696e192a | -17.85818 | -57.31168 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| eda60fb1-1d9c-3466-9bd9-0f8c5f898ad8 | -17.85767 | -57.31565 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f0d7de2d-2e2b-31ae-80e3-9c78bfdbe20a | -17.85715 | -57.31962 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 5464667a-3bfb-3b2b-b993-0732ef04d3bb | -17.85708 | -57.2872 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0d06bf19-1387-3180-b95c-d063a9798e8d | -17.85664 | -57.3236 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| b409d79e-7c62-3c49-892e-55ce3846ed3f | -17.85656 | -57.29119 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 48975c70-88f6-31ad-9ded-7838cfc38a65 | -17.85612 | -57.32758 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 2010284e-479c-3110-bf4e-ea55d00ac6ff | -17.85605 | -57.29517 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 161110ab-1c8f-39d4-910e-af9e6c185df4 | -17.85561 | -57.33155 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 649c5957-4e40-3b29-b99a-31c04dea90bd | -17.85553 | -57.29916 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| de0510e8-7877-36ae-a487-d109bddb55a1 | -17.85509 | -57.33553 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fc46d764-7036-37ea-b46f-12e3cc5459a6 | -17.85502 | -57.30313 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| abb85f54-4812-3cec-b540-f2d74857ec1b | -17.8545 | -57.30712 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| dcc3a028-2b44-37b2-afdd-6cfd327b7f5b | -17.85399 | -57.31109 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b7949d47-7ea4-346b-bd1b-ad9fd97c00bb | -17.85348 | -57.31507 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a35456ea-009d-38d4-a916-d1ffe156e9ee | -10.55954 | -57.97259 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca551efd-ad48-3df2-ab19-10107056ae5e | -10.54366 | -57.71983 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 960ea0b3-ad8b-3fc6-a9da-418bb448f329 | -10.54058 | -57.71486 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c95fde4a-efe0-3a16-b54a-875a95f852da | -10.53995 | -57.71926 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0334143b-33eb-39ce-bde7-6ba081a0d8ec | -10.53687 | -57.71431 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5cf40c-bd44-39a4-af34-b4feae0ce0c1 | -10.51189 | -57.78294 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aee0b3c-e7a9-3404-a947-aaafa9c315e2 | -10.42564 | -57.23054 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce3d363d-6b10-3fab-b77f-c37b188d880f | -10.42183 | -57.23001 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 730f472b-b9d2-3ce6-a59a-29ab0da6d0de | -10.41801 | -57.22946 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 635142eb-dcc0-3e88-8b4d-6f1e9d250fce | -10.33178 | -57.50732 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c44559-e3b7-3624-b4ac-261d49527d79 | -10.29325 | -57.71559 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84bab00d-fbd8-3614-8497-eb2a00988724 | -10.29019 | -57.71067 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 423258fb-88a4-3942-9f06-c920e88da96c | -10.28954 | -57.71506 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18609e7a-50d5-3192-9814-f153907c8135 | -10.27777 | -57.7179 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bd40ea1-dce4-3bfb-ae28-2c59c69a8efb | -10.27472 | -57.71298 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a4694c7-0c09-31ba-baeb-712bfb7290e9 | -10.27408 | -57.71732 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0abd4f1-cbd2-3843-bf56-87919e7b9472 | -10.27101 | -57.71243 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 654d94ea-d841-316f-94e8-50317ed67a58 | -10.27038 | -57.71675 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b560fc6-55bf-37b9-abcf-6e7cf08253ec | -10.10446 | -58.00754 | 2024-10-12 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b30f2560-4f1d-34c8-9068-90988d378f80 | -11.23705 | -58.03902 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f3d3259-7c82-37e1-b871-e901b04b5894 | -10.928 | -58.06935 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 498915b1-2f0b-31d8-afe0-a8723a557a43 | -10.92068 | -58.06829 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad5bae1f-0093-3700-83a0-297adba2744f | -10.91702 | -58.06769 | 2024-10-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca2340ae-5398-3ac2-bbf2-a5d1d822eb46 | -10.65049 | -58.76297 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e654198-b553-357c-835d-7c3a32fa074c | -10.64987 | -58.76705 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7b30023-eeb8-3e86-a0bb-15309d921bc3 | -10.64695 | -58.76245 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5aa5a999-e451-3032-bdd2-849acaf0627a | -10.64634 | -58.76655 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b14b354-47a5-3ad4-8ae9-264a2b74b2a0 | -10.64342 | -58.76191 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37c83806-5f3a-37a5-b048-99d71b4edcc8 | -10.62474 | -59.55857 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c794884f-a446-3c95-9119-356d691a4b2a | -10.57886 | -59.40207 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75d48521-4135-3ca8-8886-72a592968ca8 | -10.57828 | -59.40586 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 025e299a-0fe8-3b21-b4a5-bc36bd923920 | -10.53921 | -59.31466 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc17776d-dc36-3415-9a85-1c3b9483f4eb | -10.53863 | -59.31849 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 154ead20-3983-3b62-9947-753f6b65a4d9 | -10.53576 | -59.31412 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b032ce4-9fc7-3ce9-9244-04098c32213e | -10.47726 | -58.76695 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4415cbb-a0e7-3cec-a163-094733681b20 | -10.47668 | -58.7709 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a277f722-b189-32f5-8f51-ebe3e6ec6d72 | -10.47433 | -58.76233 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15a89191-c00e-34c9-a2f5-c816bcb76680 | -10.47424 | -58.7627 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1c3c516-4fbb-3202-98c5-52b670eb9f84 | -10.47141 | -58.75762 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea96f2f4-43ff-3273-a8fc-d2152088ff56 | -10.47136 | -58.75799 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09e73e29-3b1b-36a5-b3cc-2a5f1d0f4f89 | -10.47082 | -58.76168 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fe218f5-7cf7-378d-b834-8362d360c5c6 | -10.47074 | -58.76206 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 564742f3-0def-3b21-bfd5-ef43cd0ebdff | -10.46786 | -58.75731 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a0ec6af-d6ed-3357-9445-ea0496422f95 | -10.46725 | -58.76133 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e01ff2f-d2a5-3570-bddd-64aae9329bbb | -10.41916 | -58.74555 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f1e7afd-67da-3002-a13c-e257338f8191 | -10.41563 | -58.74501 | 2024-10-12 05:25:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8cda7222-c2cc-30e1-a33a-e9dadd0b1c34 | -10.37629 | -58.8887 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c35b92c7-c105-302b-8e94-87a499d27bb8 | -10.37279 | -58.88815 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e41f8180-39d4-307c-b15f-08365309b772 | -10.3722 | -58.89211 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df3c2ebe-8221-3c64-a82a-08462190be99 | -10.35826 | -58.88952 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f69c75c9-574f-3918-b4f1-125b2a5d300b | -10.35708 | -58.89746 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a44315-3764-30b1-bfab-bf12dc340141 | -10.3565 | -58.90138 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf5a0ba7-b822-39f9-bccc-1e6cc74bea95 | -10.35359 | -58.89686 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e0135ad-d68b-3593-a17e-ada701d3dd69 | -10.35301 | -58.90075 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd5d2c52-9e92-314b-88c3-7d33c0ec0b3b | -10.30099 | -59.0764 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c811f025-8455-3f62-a1c0-4c9cb2ecaf9c | -10.30041 | -59.08022 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6cd0433-9693-3707-bc4b-2c52f0321688 | -10.29877 | -58.99707 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README125.md)
