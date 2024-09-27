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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fc3b72a-5618-3030-87a7-a2de9f7fe035 | -2.7269 | -46.750599 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc436db-ca8c-3abd-85c2-37aa7bed2563 | -2.7287 | -46.7584 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0b98d48-b91f-396a-b2c7-b7021fbb7b51 | -2.7305 | -46.766102 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b41b65f-a4dc-3992-bb6d-3b8c7fb0875b | -2.7322 | -46.773899 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138744f6-f06d-319a-b29d-040de329ff3d | -3.7503 | -51.2845 | 2024-09-27 00:36:29 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1da959-032b-3942-b9dd-2f299b0e770b | -3.752 | -51.292099 | 2024-09-27 00:36:29 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84a6502-ba23-3776-a609-86972b1f7bef | -2.71 | -46.721802 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee484f82-34be-3bab-86a6-aac138ed8314 | -2.7118 | -46.729599 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90352989-2e6b-357e-a8b1-bc424cdc95b6 | -3.8802 | -51.914299 | 2024-09-27 00:36:29 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d659476-a680-3582-b702-073f727b6344 | -3.569 | -50.5658 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc1f580e-6e33-3489-8d8d-d6d727cd0a09 | -3.5706 | -50.572899 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00e1f24-fb0c-3723-ba63-61eec8f120a9 | -3.5592 | -50.567902 | 2024-09-27 00:36:30 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ececa3e3-e844-34f9-a2ac-a7165ae6694b | -3.288 | -49.497799 | 2024-09-27 00:36:30 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddd4816-d31e-3e93-ba96-b85fbeda1306 | -3.2895 | -49.5047 | 2024-09-27 00:36:30 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1259a037-f82b-35cd-9063-0b56caecbe78 | -4.4828 | -54.931301 | 2024-09-27 00:36:30 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec7bad0-2c69-3c8b-87b5-db543c5acbcf | -4.4855 | -54.943501 | 2024-09-27 00:36:30 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604a5b3c-9978-3846-8bd4-feeb357e620d | -2.9005 | -47.875599 | 2024-09-27 00:36:30 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0647534-ed10-389d-a83e-11cb0354ec0a | -2.8907 | -47.8778 | 2024-09-27 00:36:31 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4336e542-2d0d-3101-b0e8-21e1243f5fba | -3.827 | -52.276402 | 2024-09-27 00:36:31 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85cdcaa-9f39-3dbd-83cb-163091d44ddb | -3.1259 | -49.189899 | 2024-09-27 00:36:32 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669358d7-7929-3936-9136-05e7b9bd47f0 | -3.4783 | -50.803799 | 2024-09-27 00:36:32 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c91e3b9-8f4f-3631-906c-5f7ebbc008e7 | -3.313 | -50.296299 | 2024-09-27 00:36:33 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90825368-b9b5-363c-b553-82d67bb85ce0 | -3.3146 | -50.303299 | 2024-09-27 00:36:33 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c810befb-a5de-3b0f-b950-e9aea7f1cf49 | -2.9492 | -48.727001 | 2024-09-27 00:36:33 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0181cdd7-115f-341d-90dd-84e444d5855b | -2.9507 | -48.733898 | 2024-09-27 00:36:33 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e828d395-b21f-361c-a708-200e860f03a5 | -2.9212 | -48.877102 | 2024-09-27 00:36:34 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c8e0c6-3830-34d6-977a-c97db0449905 | -2.9228 | -48.8839 | 2024-09-27 00:36:34 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11844ed2-eea6-3758-95a2-17b8292fb624 | -3.2232 | -50.308899 | 2024-09-27 00:36:34 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e360f6-cf3c-3ef8-803b-81ddaeea82cd | -3.2247 | -50.3158 | 2024-09-27 00:36:34 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9533bc-f0be-3934-81c0-6e3fdfe16cb2 | -3.3007 | -50.6548 | 2024-09-27 00:36:34 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f9287f-02e4-355b-a30d-e18a3b90fa28 | -2.9459 | -49.351601 | 2024-09-27 00:36:35 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d23739-e61d-3e78-9c5b-9f235b602524 | -2.2612 | -46.380001 | 2024-09-27 00:36:35 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7868d9-ced0-3f0d-864f-69672db6ca83 | -3.1435 | -50.275101 | 2024-09-27 00:36:35 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7694bc-3156-3eb7-9fe5-3c20479ea340 | -2.4563 | -47.825199 | 2024-09-27 00:36:37 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7884cef1-5283-3ce3-b28d-ef3ff4300ab0 | -2.4579 | -47.832401 | 2024-09-27 00:36:37 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 039567b0-b0c4-33e8-a273-453d14df3e5f | -3.1919 | -51.134201 | 2024-09-27 00:36:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e5221b-49ec-386b-9b27-78d511e0688a | -3.1936 | -51.141602 | 2024-09-27 00:36:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68034cee-ce36-3105-93b9-48adfc82244f | -3.1952 | -51.148899 | 2024-09-27 00:36:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ecd752-9e53-3b23-86a1-6f45d34f0692 | -2.3516 | -47.591 | 2024-09-27 00:36:38 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed6d1e7-33da-326c-9b4c-3eefeb978c7a | -2.3532 | -47.598301 | 2024-09-27 00:36:38 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30a72b38-2ccc-3422-89c8-d17c5632582e | -2.3549 | -47.605499 | 2024-09-27 00:36:38 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a60c1d7-a3bd-3d28-9b8e-336589383080 | -2.7995 | -49.570301 | 2024-09-27 00:36:38 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd33ef7a-8c8e-30d8-adb7-11ad5d872d18 | -2.801 | -49.577099 | 2024-09-27 00:36:38 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7669e7ab-1f7d-3609-a55f-c95865a9ed22 | -2.8026 | -49.5839 | 2024-09-27 00:36:38 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0d3102-1f57-37f0-8db9-5f1a591e9ceb | -2.3418 | -47.593201 | 2024-09-27 00:36:38 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4991bf4-100e-3b7e-a62b-84b6c18c7c7b | -2.3434 | -47.600498 | 2024-09-27 00:36:38 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 365cd087-96d9-3137-bde4-61b822bfdcbe | -3.7408 | -53.835701 | 2024-09-27 00:36:38 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a5293e-bae9-37cb-95a9-dbce9f21c77a | -3.743 | -53.845901 | 2024-09-27 00:36:38 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3484ee7b-95de-3abd-858a-8f3486f8f501 | -3.7453 | -53.855999 | 2024-09-27 00:36:38 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa7d7c8-349b-3727-8982-c3fe023cc7fe | -16.7325 | -55.8445 | 2024-09-27 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 1f97e92f-252e-30f2-95e2-3c0f2d44bbe4 | -16.7329 | -55.8237 | 2024-09-27 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| b520cf35-8187-375a-8f6e-8dceaf48478b | -3.223 | -51.825901 | 2024-09-27 00:36:40 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80d1d46a-eef1-3d54-b66f-5de08975658f | -3.0909 | -51.280399 | 2024-09-27 00:36:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55692683-0d2a-356a-9220-02e13e1d1b33 | -3.2132 | -51.828098 | 2024-09-27 00:36:40 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da12e3e-9389-3ab9-aed6-2e0d293d6eb1 | -3.017 | -51.042198 | 2024-09-27 00:36:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22f3b8f-4f90-300e-84ed-28e142a4a535 | -3.0186 | -51.0494 | 2024-09-27 00:36:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0301e9-34f9-3fb1-9928-77ede3e7eda6 | -2.4109 | -48.397701 | 2024-09-27 00:36:40 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67fe5619-c2b6-3fcf-8637-c5f47f6fcf4b | -2.4124 | -48.404598 | 2024-09-27 00:36:40 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b67f0c9-ecd3-38e2-8d89-f8fe8e3f4a05 | -3.0072 | -51.044399 | 2024-09-27 00:36:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7337df-8b1f-3626-a337-9bb683cf2a96 | -3.0088 | -51.051601 | 2024-09-27 00:36:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 654e390e-eb99-33f7-8e12-e4a16709e3a6 | -3.0104 | -51.058899 | 2024-09-27 00:36:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71f29ec6-e0c1-395e-a8dd-35b9b89d9626 | -3.0714 | -51.331501 | 2024-09-27 00:36:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52f98e2e-4915-3608-aa5a-5075c7a1f56c | -1.979 | -46.587601 | 2024-09-27 00:36:41 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1806d0-7654-3558-b599-7a3ba036fdf3 | -2.8009 | -50.263 | 2024-09-27 00:36:41 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54bdded0-dfec-3f2f-9c4d-b44158479ec1 | -2.8025 | -50.27 | 2024-09-27 00:36:41 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da92c14b-a24b-3c36-8492-4aa665976411 | -3.6401 | -54.029499 | 2024-09-27 00:36:41 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 964f788b-877f-32be-a183-f7e57f615751 | -3.6424 | -54.039902 | 2024-09-27 00:36:41 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3068cbaa-513c-3f65-8c77-c0a71e916684 | -3.6303 | -54.031601 | 2024-09-27 00:36:41 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085313e8-580c-3168-b699-abd88cf2aea6 | -3.2871 | -52.7136 | 2024-09-27 00:36:42 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e627edf-f556-39c6-b44d-6d6dfb9e95a2 | -3.289 | -52.722301 | 2024-09-27 00:36:42 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883bdf70-bbec-3773-be0f-d2065b2d6f76 | -2.2179 | -48.228001 | 2024-09-27 00:36:43 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf9d2ad9-23e0-31c4-a475-8e1d7ca7d562 | -2.2195 | -48.235001 | 2024-09-27 00:36:43 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569d9184-7094-3817-873b-161112025a2a | -3.1642 | -52.438499 | 2024-09-27 00:36:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d09289-0b9c-34ed-81d9-ccfb93f43675 | -3.3231 | -53.199699 | 2024-09-27 00:36:43 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a541419a-40ca-3ba1-bc2e-2119641d9356 | -3.3252 | -53.2089 | 2024-09-27 00:36:43 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e038975d-9c94-35c0-8f02-53678d388a89 | -3.2911 | -53.101601 | 2024-09-27 00:36:43 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f4eba0-a8e4-3236-bd85-400c3ecb6e8d | -2.8736 | -51.3671 | 2024-09-27 00:36:44 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5f1388-63a4-350e-a19a-2a5b70396a8c | -3.3933 | -53.701801 | 2024-09-27 00:36:44 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb8f2b7-4778-3420-8002-19f93a469237 | -3.307 | -53.358601 | 2024-09-27 00:36:44 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18eb8344-fd22-34c9-8553-26f3b1f41762 | -2.8754 | -51.651199 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 688cb93e-19a7-3a06-8769-252c37ae5ca8 | -2.8771 | -51.658798 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7cd74c4-25b5-3f75-8cbe-c3a8ebaaec07 | -2.8788 | -51.6665 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcb9d59-8313-3e67-a5b6-54dbac17c43b | -3.3455 | -53.763901 | 2024-09-27 00:36:45 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f07c1ddb-6e88-350a-a26a-ce3f3000942b | -2.8656 | -51.6534 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe1b552-717b-39a3-bd5d-3e79b3887dcb | -2.8673 | -51.660999 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc346169-5b11-3c5a-af47-3b7a35d8e89b | -2.869 | -51.668701 | 2024-09-27 00:36:45 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c0d7c9-b850-3c41-968f-3007db37d58d | -3.3063 | -53.6796 | 2024-09-27 00:36:45 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d23262-4d6b-350a-b7fc-663da1ad12af | -3.2965 | -53.681801 | 2024-09-27 00:36:45 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1609f265-9c98-39b1-ae36-6d9b16d3bccb | -3.2987 | -53.691601 | 2024-09-27 00:36:45 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8f37d2b-1417-3e18-9fd9-dea56b7f5870 | -2.853 | -53.302101 | 2024-09-27 00:36:51 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75829e60-0164-3fa9-8301-b2ea38f657f6 | -2.9366 | -53.678398 | 2024-09-27 00:36:51 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0807123-1a25-346e-be1f-21de962e5a9f | -2.9388 | -53.688099 | 2024-09-27 00:36:51 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91981d2d-4d29-3b84-8e85-3dd3de9f2a34 | -2.3875 | -51.264999 | 2024-09-27 00:36:51 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a99dafb-8c7a-3a57-9451-390405f81143 | -2.3892 | -51.272301 | 2024-09-27 00:36:51 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcec8492-b4d2-370f-beaa-38143a0e0fd2 | -19.6136 | -42.8159 | 2024-09-27 00:36:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| b905e5c6-59cf-3877-a702-a73b5883a279 | -19.5266 | -47.8952 | 2024-09-27 00:36:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3d637f14-e6d7-3bec-81e0-dd9007a7b0ed | -19.5272 | -47.872 | 2024-09-27 00:36:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 2ef1d061-562d-32b2-8e84-b9bdd4c1bfe2 | -19.5476 | -47.8675 | 2024-09-27 00:36:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2cc6e0f6-9319-3bf8-a4d6-fd0f652aa898 | -21.098 | -49.1578 | 2024-09-27 00:37:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| f8c5f804-43ea-3c30-8e6f-7524fae881ef | -21.0986 | -49.1347 | 2024-09-27 00:37:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.9 |


[Clique aqui para ver as próximas entradas](README18.md)
