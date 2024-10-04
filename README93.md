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
| 5b3ed14a-e290-3d61-9ec0-1f6127e435a7 | -3.97463 | -40.48312 | 2024-10-04 04:29:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a96f787b-66d7-300a-9396-df87e0a93b83 | -4.72031 | -38.45668 | 2024-10-04 04:29:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e1e6c81-791c-37ab-a897-8193da482ce7 | -4.71983 | -38.45988 | 2024-10-04 04:29:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b34b4fd5-f4fa-31d8-a453-62fa7fd6c80b | -2.94672 | -41.74669 | 2024-10-04 04:29:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b80d5dd8-9ea6-339f-9b51-c81792ae486e | -3.37738 | -42.28967 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c1acd4c2-215b-37ce-aa8f-37a2e9cf99d1 | -3.37659 | -42.29481 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d0359256-5da7-352d-98dd-fb538daf3b20 | -3.3726 | -42.29422 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 197e4a58-0b06-3bcb-b6fb-443efdeec312 | -3.36939 | -42.28847 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 110.5 |
| f952cfce-c06a-394c-a151-39375ea73505 | -3.36861 | -42.2936 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 110.5 |
| de95c93d-6b5d-3c44-b4f0-dc8a1987a0c8 | -3.36541 | -42.28783 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52dda298-db4c-3a8c-a748-2604c5f59f7f | -3.41095 | -42.28402 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 663c3f6b-1d3a-3630-91e8-c4a7f859fcfa | -3.40796 | -42.28481 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 93bd7d65-c698-3da0-adec-aab5e50b6b69 | -3.40719 | -42.28997 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dbed681-b9ef-32f7-8ad9-c20790bc3742 | -3.40695 | -42.28344 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a350fd61-af91-3f1e-b718-b4ae9437c4fc | -3.40616 | -42.28859 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 92c7cbfb-8f89-342e-9af7-cf09b0a7ffc0 | -3.40396 | -42.28423 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85fa1512-fd2f-3d12-ae0e-90b7d087d90e | -3.4032 | -42.28939 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 500be544-5842-3d15-8c46-16a3e0a49b1a | -3.37018 | -42.28333 | 2024-10-04 04:29:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b35301ac-e1f9-3a24-b25f-1d9ccc8ded50 | -3.47141 | -43.35714 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9bb91ca-45a4-3183-8412-3a4c7d2bdaa6 | -3.47069 | -43.35944 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d072804-8c9a-31ae-92a1-53c3f3563475 | -3.43462 | -43.34489 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e95eb21-b859-3086-a943-ac8de7bcbb78 | -3.43087 | -43.34432 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a27970-cb96-3a55-afde-c0f17c43085a | -3.43018 | -43.34877 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25199fef-52e4-34d6-8c21-3e132d33dc33 | -3.4285 | -43.33479 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc9b812d-cc54-3ce3-9e3e-9d42e89e68a3 | -3.42476 | -43.3342 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e5835b9-0af3-3999-9cc3-dcca4b3b36e9 | -3.26613 | -43.13836 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbcff33a-3618-3e02-86b4-2f4e82c8721c | -3.26235 | -43.13779 | 2024-10-04 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6566e64-6eca-3094-ba33-5ce69359671b | -4.02992 | -43.23386 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c19d4f0-9089-3c80-83d5-031c7b4a3f95 | -4.02893 | -43.23606 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b3516ca-4305-3640-910e-09dbcdc91a0d | -4.0254 | -43.23793 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a07bb6a-ed5d-34d6-bac4-c270843cea35 | -4.02513 | -43.23547 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb097a09-25bc-30fc-86b6-798e993aa6fd | -4.02444 | -43.24012 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2941b46-a320-3d51-963b-fce7919e4038 | -4.0216 | -43.23735 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 684202e4-0142-3cd4-8ad3-7ee38c7a447d | -4.02064 | -43.23955 | 2024-10-04 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25bca4bc-dadc-3d19-b397-75070974fb3b | -3.05643 | -44.48261 | 2024-10-04 04:29:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24cbb57e-a5f3-32b0-97f3-13d94ea1873d | -1.73114 | -47.12375 | 2024-10-04 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a0cb55f-5ee8-3d0a-8105-3a8f1c017706 | -2.73001 | -46.79541 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76e02e7a-b1bb-37fb-a7da-3b5dff564577 | -2.72947 | -46.79885 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2afc89e-fdf5-3572-a74c-a425710e37eb | -3.31873 | -46.99068 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99721841-2aa0-3272-a355-db40a0af7e6a | -3.31595 | -46.98671 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab28711f-26fc-3365-8d59-0a4955b094f0 | -3.31541 | -46.99017 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71bf843d-9b51-3ead-995b-24816f9b7e6a | -3.31487 | -46.99361 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a2d4523-dbdd-3f27-a414-1d4ae8619e1f | -3.07262 | -46.53383 | 2024-10-04 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b76c020-2f61-3027-8f32-add68668c8ed | -2.73876 | -46.7614 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e026dbff-4cde-33e6-9a4e-9e0bd0f990fc | -2.72615 | -46.79834 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca1690fb-d208-3c39-bd1b-fac401f63095 | -2.72283 | -46.79782 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f2b915d-1306-30c6-9132-edf93e164893 | -2.72228 | -46.80127 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52108888-2764-335e-8f32-7f46a0d7e631 | -2.72005 | -46.79385 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 850cd7c8-9625-3ee9-9f10-4ada1284f8cc | -2.23395 | -46.74648 | 2024-10-04 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7fee3cb-d773-36e5-b74a-732bd7afee01 | -1.58823 | -48.02839 | 2024-10-04 04:29:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2472d0de-58fe-3910-82c6-fd0a5afdcfbe | -1.58766 | -48.03197 | 2024-10-04 04:29:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a7891a1-b3fd-3819-9b51-d87d4ea74248 | -1.49432 | -47.33935 | 2024-10-04 04:29:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2ce8b3e-1b6a-33a8-9e5e-61c93635ca59 | -1.49377 | -47.34282 | 2024-10-04 04:29:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3714b59e-7c16-3250-ad57-1744b161edc5 | -1.03788 | -47.7939 | 2024-10-04 04:29:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1b4c91f-c1aa-3f93-9cba-5537a30cf85c | -1.49098 | -47.33883 | 2024-10-04 04:29:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03b50ea1-cd94-36da-81c9-fc452b9dba97 | -2.3374 | -47.97361 | 2024-10-04 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675a13a7-1460-33a6-9cae-7233c24d15d0 | -2.33684 | -47.97714 | 2024-10-04 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e97eb2d8-74f8-3f99-a3cd-8a1f13078269 | -2.29745 | -47.89166 | 2024-10-04 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef1ed6a1-caf9-3d0c-9f40-f6a0b72d12db | -2.23923 | -48.06402 | 2024-10-04 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71086c90-c652-3610-ae6c-08bd7a56bec3 | -3.41039 | -47.58924 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3472d53-59ee-34ad-b225-cc544b0acfda | -3.40706 | -47.58872 | 2024-10-04 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21084acf-5e1c-3239-878a-7e7fa5d9b80f | -2.43089 | -48.19939 | 2024-10-04 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90494c22-27c2-3680-96e2-89dcd085393d | -2.39369 | -47.66186 | 2024-10-04 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6cdcd3-8071-3288-917d-8c6187c5ad97 | -2.39035 | -47.66133 | 2024-10-04 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f450dd-0851-3717-be80-7b7588a7d1a5 | -2.2941 | -47.89114 | 2024-10-04 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0c4625-cdfd-3aa6-9e6e-09403319d65c | -2.29074 | -47.89061 | 2024-10-04 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 114dd859-8135-387b-b429-f253d0a6d392 | -1.38308 | -48.97755 | 2024-10-04 04:29:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61970229-8ba9-3d19-9745-122235b0d16e | -1.37959 | -48.97701 | 2024-10-04 04:29:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9749338-9beb-336d-ad8a-5f8e3854eb80 | -2.79921 | -50.28858 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b50b8045-41d0-3250-bd23-f685f616c224 | -2.79622 | -50.28375 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aab88c8-a192-3884-8a9b-04089ad1f1c7 | -2.85999 | -50.71445 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80fcb4fb-8f6b-3524-a2b0-6d4bbf963864 | -2.14085 | -50.99149 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2c0c3dd-9f0a-3cc3-b5dc-dc83b285d259 | -2.13701 | -50.99086 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba7493b-85cb-3b18-b504-f403879d253b | -2.13243 | -50.99495 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 335e6091-52d3-3f13-9451-e0676fc510d7 | -2.90204 | -50.73948 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62dd26f0-1da4-337c-ab24-6c2ffd850348 | -2.90133 | -50.74395 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b15a24e4-1753-3111-86b0-10ffe64d3aba | -2.89886 | -50.7115 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f08e5690-962c-3276-82d8-8327fcbafaac | -2.89814 | -50.71596 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b6b1b6a-1357-3c09-9997-b7fc0d00a953 | -2.89758 | -50.74335 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd12a9cf-cc61-3bee-b620-a9d82fce888a | -2.89742 | -50.72042 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52218102-ced3-3c32-870c-975ed8fcc0bd | -2.89686 | -50.74783 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b200224-81a7-3b83-9da0-c012afd96c3d | -2.89368 | -50.71983 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d09c50f-ed4a-3397-8168-2f549372e79e | -2.8908 | -50.73769 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6784d53e-e066-34bf-be71-d2d3ad94bc71 | -2.89065 | -50.71476 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b82a889-ad4d-3725-9e99-e53b03ce9724 | -2.88993 | -50.71923 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5581a2be-7b1e-3c5c-8cb3-fc1a42370c2d | -2.88835 | -50.70525 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1af55f3f-ff01-3627-8689-acb71a826470 | -2.88691 | -50.71416 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73acb6d7-3b90-3482-8741-856f30a9abaf | -2.88317 | -50.71356 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa518970-a195-3a56-b16b-0a105d037fa6 | -2.86602 | -50.72458 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4569e4f-04f4-3999-9a1e-9520a0772949 | -2.86373 | -50.71505 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfcd5149-e388-334b-90b5-1bb555a61b37 | -2.86228 | -50.72398 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51f75793-58a4-3098-a6b2-aaa9c82f9670 | -2.85926 | -50.71891 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb1c0ca7-0a38-3589-a766-d2717b203116 | -2.85853 | -50.72338 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d6274b-e325-365e-a30f-8a0554c928b5 | -2.85624 | -50.71386 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0286cfac-e86d-377f-a8ad-a0bd37adbcd2 | -2.8551 | -50.71562 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c299a5-0c29-37a0-9a26-87993a0cd521 | -2.85229 | -50.73355 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc9a8e5c-19b1-30f8-bcdc-10690fe4e155 | -2.85065 | -50.7195 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba3ca1fc-3d6d-37fb-9218-33c1528be52a | -2.90508 | -50.74454 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ee86af-fcce-3a3c-b4a4-8fd4adfe8e3d | -2.90436 | -50.74903 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f1f11c-bdf0-3dab-aeaa-22cc8e332310 | -2.90188 | -50.71656 | 2024-10-04 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README94.md)
