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
| 0aaf6813-4ad2-3871-b879-080eb2715c0a | -12.86564 | -44.3434 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6751fe18-8a76-3035-b19f-f99e7f548e2c | -16.39397 | -47.41988 | 2026-07-02 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f71e2357-1f43-393c-93fa-f1b5af7927a1 | -13.56164 | -44.10073 | 2026-07-02 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d5b3ce-9c62-38b1-951e-37f67a9c38b7 | -10.94554 | -43.04747 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0c59233e-5878-3ce4-8a5c-43b7a3f70e60 | -11.41588 | -56.05603 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41df2204-4825-32d6-abf8-3f6e55796343 | -5.80944 | -43.79461 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58d676ef-c2aa-32ff-90f8-ef853561bff9 | -10.4673 | -46.57379 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b382bb3a-8307-33a5-9943-6616c3db244d | -12.86169 | -44.34645 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 954a9211-8fe5-3509-bb8c-f970f3914a49 | -3.50616 | -48.03972 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d6321a3-a566-3f51-8ce4-59bda03f67f9 | -10.1283 | -52.10179 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4751aa30-3667-3bcf-b380-9800873ab7ad | -12.76124 | -44.49079 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e1cf075-f0dd-3367-9749-0a66606d78e5 | -5.12789 | -49.33006 | 2026-07-02 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c2941f0-efd4-36ad-82eb-9ad00afff69c | -12.74161 | -44.4837 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f7955c34-c20c-3fca-86cd-6e7c613d0c08 | -11.40229 | -49.00974 | 2026-07-02 04:19:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a0d1ba6-4a4f-3c75-9057-df485611170c | -3.50154 | -48.03899 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 430bacbb-82bc-3003-8473-229be27bd0ad | -12.84707 | -44.35143 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dcb64604-c252-36c9-b22f-d6c5bd4592bf | -12.76243 | -44.48348 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cae5fabc-e656-3610-a633-aea610e11f80 | -10.12417 | -52.09374 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 404b0092-52fb-3f16-91da-88e312dcf1b2 | -12.84312 | -44.35448 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f366c68a-080e-38d4-8191-8614723db0e8 | -5.56221 | -43.83029 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9008891-5d32-329e-ac1b-d8124cce8835 | -12.86841 | -44.3476 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 01b356e6-3555-3dc6-a89b-4f516194b74b | -11.91222 | -43.39026 | 2026-07-02 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c381d2a0-1fa5-3833-8abb-2611a863d356 | -12.22976 | -47.48467 | 2026-07-02 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43e83217-67dd-3420-b3bb-35a75fc0933b | -5.29326 | -43.7067 | 2026-07-02 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 101fde35-4dda-3252-ac2c-cfb992750c40 | -5.78894 | -45.04501 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29b324a8-1925-3f7c-9f66-82952da540cf | -6.34218 | -43.65348 | 2026-07-02 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5c04a5-9fd9-30d8-993f-ce278e8b4af1 | -5.8123 | -43.79897 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab24dae1-d4af-399d-b33d-d2f6fd21acef | -4.00669 | -48.06701 | 2026-07-02 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27ff0d8b-1a4c-31d6-a4f3-331a5d9b1225 | -11.35161 | -55.43077 | 2026-07-02 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4431cf65-ce9e-38eb-a223-66d3ea680462 | -16.43561 | -43.49011 | 2026-07-02 04:19:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd3a04f1-9db2-3f00-a637-6117de9c95a1 | -12.7771 | -44.50414 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f458da0-76a5-3524-bbed-b0f8f8e8105c | -5.82441 | -47.89228 | 2026-07-02 04:19:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b89b94-6520-3e1d-b79f-27bda12414e1 | -10.1194 | -52.08923 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50759061-a323-33cd-bb9a-73674d460b9f | -12.87059 | -44.35542 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| c9cd34e9-462d-3c5b-9019-6f08466deebc | -4.94673 | -48.24642 | 2026-07-02 04:19:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d395f930-4154-3742-b32f-bfa16de8338d | -10.84607 | -45.05728 | 2026-07-02 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a458b5f-ceda-3559-841a-7a3f7fea75d7 | -4.00749 | -48.06222 | 2026-07-02 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4b7d47f5-3751-3cc9-87b2-48a0768a3141 | -12.76284 | -44.50233 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9058edc9-92a7-3dab-8f05-682af82385fe | -11.91612 | -43.38728 | 2026-07-02 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0130899f-1e37-34a3-b12d-5127f8f27155 | -12.85951 | -44.33864 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 91a43262-3ffe-364e-a928-128b73341022 | -4.28047 | -48.36368 | 2026-07-02 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f2e907-fb3f-3499-824a-9f7df5d58ea2 | -12.85615 | -44.33806 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 03b55250-d2fb-3464-8a3e-530f7dddfc52 | -12.84589 | -44.35868 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6944bf7e-392e-30c2-b481-43c85e8b44cc | -12.77017 | -44.49983 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d38845ae-d327-3c5f-99a0-e26f22b6058f | -11.42134 | -56.06355 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 88c8428e-3458-359c-91b6-8cc7f7d358b9 | -10.84194 | -45.06057 | 2026-07-02 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122bcda2-d870-3ca1-b9d1-bb8eb577f216 | -5.47226 | -45.41604 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0283013b-430a-3eb9-8f0e-a35408ff72a4 | -12.86782 | -44.35122 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e3f5e748-94b9-39f8-9d32-72f80b12ce25 | -11.48783 | -47.38946 | 2026-07-02 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51ddc734-9f6a-3082-88fe-8a1becdce43d | -10.77516 | -53.54443 | 2026-07-02 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015dfff5-dff1-3d8b-a6f2-4ab81ffacd3a | -11.80792 | -57.00893 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6a6668b9-bb96-39dc-93da-a0ec02554f6c | -12.52165 | -48.29322 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fdd29c8-52e7-384b-98eb-5b4ca1379db7 | -12.62186 | -44.65934 | 2026-07-02 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3d6ecc9-9c55-37d8-b437-6bd67fe55ebc | -5.78966 | -45.04069 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a13f729e-8f14-379d-9d51-4212f9697770 | -10.37244 | -46.69701 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 377bd20b-0af7-3ac1-a5f2-ad4f110169b1 | -4.00287 | -48.06168 | 2026-07-02 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 67fbb8e0-6e20-3325-a529-96a537c97519 | -11.91888 | -43.39136 | 2026-07-02 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7eb40e9-4e0e-36ec-b216-2e2786697b91 | -5.47241 | -45.4185 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd00295b-d0b0-3e9c-8c35-43857a2588b6 | -12.87176 | -44.34818 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 31f3e6db-f24f-30f9-8f9a-bb2150b8c835 | -5.46863 | -45.41793 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55298997-d711-3872-bac8-a478dc0883a7 | -14.15491 | -52.87917 | 2026-07-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4279d54-f204-3f3e-8caf-4697831b35bf | -5.47727 | -44.10746 | 2026-07-02 04:19:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ac7887-f3db-3ccc-9231-25ee097d47bf | -12.52229 | -48.28964 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c5201df0-453b-3f64-9f9d-6188fd1bb063 | -12.8443 | -44.34723 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 85903ea0-affd-3ed6-ace6-97dae011e7c6 | -12.86505 | -44.34703 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 51f32526-f7b0-34cf-879e-a6d44f305156 | -17.71605 | -46.79512 | 2026-07-02 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19612b23-6701-3cbf-95ce-d4a0de513907 | -12.85992 | -44.35733 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cff251b2-7faf-34c0-b2d6-90aa3d51071a | -12.76621 | -44.5029 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ed85d6b0-851a-318f-9989-b39cc07012d3 | -9.74463 | -49.02897 | 2026-07-02 04:19:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 925f4c7c-0c50-36ef-a6ce-ba4246531e93 | -14.81139 | -49.00954 | 2026-07-02 04:19:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1768db77-b0e3-35e8-acb7-56fff357b161 | -12.51016 | -48.28738 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9241a834-e4d1-3144-a1b0-907f6af6a5b1 | -10.47032 | -46.57619 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0dd754d-2d86-3eae-a2b3-04e60fcbc2a6 | -12.5108 | -48.28377 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96160a8a-139e-37a8-858b-ee1e47445255 | -10.69707 | -49.61069 | 2026-07-02 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 878ecd4d-23dd-3fc7-9a2b-51b8f33aa5f9 | -12.75113 | -44.48907 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 880223eb-3336-336c-bdba-d40f51327f7e | -5.14456 | -37.91173 | 2026-07-02 04:19:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5603db1-564e-398f-9d49-4dac501e1500 | -5.79262 | -45.04565 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13791d14-f3e1-3d30-97db-5f1eae688872 | -12.76343 | -44.49867 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e0974a3c-8598-3c88-8c5d-f4f0878363d1 | -12.76402 | -44.49502 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a72fce77-3ae5-3e46-b12f-e1d0df1135a0 | -10.38024 | -46.67441 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3385675a-7d27-3803-aed6-72912c078bbd | -12.79336 | -44.51066 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46994268-8ec2-380f-bb73-b95d3f8d2ea8 | -5.34492 | -45.18158 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b8dfe09-3b1f-3835-8c97-1e7df0830a16 | -11.54018 | -47.45883 | 2026-07-02 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afdd8a7f-35cd-3479-916b-b7c08cd8acb7 | -12.51612 | -48.27729 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57b0f4e4-a5ed-3bcc-92b5-fe3ddd634c96 | -17.71744 | -46.78703 | 2026-07-02 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 411a38e2-ce3c-32df-9962-33313b56c2b7 | -12.86446 | -44.35065 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 281d12f7-4cca-3334-9662-5741eb1620f3 | -10.79724 | -48.56524 | 2026-07-02 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfe2b9dc-64fc-37fe-8050-56cfec216e49 | -3.51157 | -48.03557 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| eed4742b-441b-3650-831a-bf8730a41fa1 | -11.49393 | -47.40054 | 2026-07-02 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c3b920f-6cff-395d-b828-8be6f1ab3949 | -5.12202 | -49.33472 | 2026-07-02 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8608bf34-f159-3f2e-972e-36cbe14557cc | -3.51077 | -48.04049 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| fd70d297-e407-31e0-9f80-9c8045775077 | -14.15893 | -52.88676 | 2026-07-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28f1b526-0b93-311f-8511-f79018031343 | -12.86051 | -44.35371 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 96db6e81-0342-314e-afa7-71b33955ddfa | -12.84984 | -44.35562 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c412b6ad-55cb-3ace-8b25-1828987a01ac | -12.74617 | -44.47697 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6616ba35-f57f-341e-9eb4-297ad73c7f8d | -12.86286 | -44.33921 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ab2c3fd4-8f4e-328f-a8d2-684d4356b620 | -5.34792 | -45.18663 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 670a67b3-fff0-37be-acfa-73d38395a554 | -17.71675 | -46.79107 | 2026-07-02 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a694d7-c22a-348d-b114-03777a3974c9 | -3.51442 | -48.03782 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| af587033-7a38-39a1-9bbb-8af4265d6467 | -16.39122 | -47.41681 | 2026-07-02 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
