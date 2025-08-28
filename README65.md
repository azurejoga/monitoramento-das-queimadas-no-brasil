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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cdf219e-2ee8-3088-ab8c-5bd2ef02112f | -13.47654 | -46.8498 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2b91987-a12e-3498-8598-75cf89158814 | -9.46493 | -60.3 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 655bfa45-60b2-3ece-9a5b-c06863f32444 | -11.15371 | -54.30565 | 2025-08-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbf2b03a-4d33-3339-9267-2af502c2db9d | -13.42109 | -47.00093 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44ee14e9-cb42-392f-ac52-d9e86c41bc06 | -13.18109 | -45.28016 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83df3098-d774-3386-b8ce-9c5ff34026f3 | -9.48511 | -62.39478 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb30d76-28d7-3443-8f86-1be3f2e606e1 | -15.67031 | -52.73649 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e19700e-42c6-35e3-94d3-3ef02c593a10 | -11.3257 | -43.54269 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4cfcc86-f9f9-3168-8fa4-e656c2f6bf5d | -12.43992 | -45.96616 | 2025-08-28 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 285d5703-fe5d-3380-b81c-c38c35900512 | -15.61775 | -52.74493 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f203885-d0b2-3fd9-aec5-ae0548e53e7a | -15.19348 | -52.32929 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b09ff4-580f-38b6-885c-620eaff2c8ac | -14.54551 | -48.18472 | 2025-08-28 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 004aa0f7-9d46-3e5e-aa64-dd42d0625f71 | -10.47034 | -57.93859 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e54fad75-5b99-3731-959a-7b3dba66de74 | -11.79593 | -46.79286 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6633c4c-d8bd-3cc9-988f-868543e48220 | -13.63284 | -48.24391 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7148029-4e4c-388a-8835-d6df5b9c3852 | -10.26285 | -64.49673 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56e8d695-c0df-3987-aa1a-02838d661d61 | -15.60919 | -52.72518 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca1c5cf0-8c66-3259-ab17-2807f44d1495 | -12.67555 | -48.18089 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86484562-37b6-341b-96a4-f490e44523aa | -10.81957 | -60.76877 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e3d7147d-9086-3e0a-a2bc-1017e601d723 | -9.80885 | -63.07656 | 2025-08-28 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df1292e8-6c3f-3f44-b0ce-fb492e55402d | -13.45218 | -46.96824 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71c01368-28ac-3b93-b0ee-d16f0fadb133 | -9.4039 | -60.50568 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc07ea6-d406-30e3-ad33-b88d638516d9 | -12.1808 | -47.1845 | 2025-08-28 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d38e088-066a-3c67-9c46-b0b3ea34992c | -10.54576 | -46.6921 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82fe1521-bc17-331b-8bde-72268a30aa4a | -13.52571 | -46.93164 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3edf86f-6fa3-3ef5-a860-88c754cb00e4 | -9.2115 | -60.85843 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d6bd3b6-4e98-3b23-ae80-75124c38ac77 | -10.46297 | -57.96172 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ad56734a-fcaa-3789-8b28-d8ba1df7e76f | -9.18096 | -60.80826 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c24e717b-8c7f-33e7-a033-89b3f96b484f | -13.1411 | -54.92607 | 2025-08-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1cab37c-9a78-312c-b80e-baf6b49984ed | -15.10809 | -48.56282 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23fcc849-90f1-3a62-a73b-0360019253c6 | -10.4788 | -57.93508 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| cfb87a66-8283-3e2f-bdf3-cd62afb616ef | -15.62458 | -52.73888 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf3384b4-a07b-3e87-9830-7ad04e41c121 | -14.53005 | -53.17255 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7fcb2fb-5097-35ea-9460-4acf23d57e72 | -9.47361 | -57.84167 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11ce11fb-eeaa-3298-807d-7c36d57273c8 | -11.57552 | -46.41385 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ec2272f-1ddd-3933-9e15-1830e6061b3a | -14.27599 | -53.06075 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 42a56b74-3e26-3310-a25d-ddf734ed6159 | -14.32018 | -60.37002 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 011d4ede-7903-3042-8f9e-902dbb4eac31 | -14.31856 | -60.35793 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3852f78b-3317-34d1-9684-0c0840c315d6 | -15.09046 | -48.51173 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23ef3ac4-49dd-3dbf-aa3a-c0ed2c6b83c7 | -14.28709 | -53.04765 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0476c8d1-5448-382c-8320-1153d6f6852f | -10.58804 | -54.88752 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9b2ddb4-6d44-3f24-84fb-3c1e5f20d541 | -12.69582 | -48.17406 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9c12d1b-a9e9-39d0-9c45-2e30aa1121cb | -13.17964 | -45.29279 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e06f398a-0f5d-311b-a8cc-cb30c5598a07 | -9.1681 | -59.56261 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05407f24-fb8c-366b-87ad-e71a9258f9b3 | -12.78272 | -48.1805 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29a23ca9-537c-3d66-a87a-d07d236cfbbc | -12.79646 | -48.18729 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb52b339-1751-3fbc-a6d1-074af1140cb0 | -9.41214 | -60.50708 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a66f063a-1249-3245-bdca-09f1761e71e6 | -15.07956 | -48.63929 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b547e43-9db2-3ee5-b40d-bdc5685e03fe | -14.34922 | -53.34997 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9a16d0e-eb70-3947-830b-070462aacd82 | -12.69009 | -45.08844 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a20a6d26-17ed-3b77-8e91-c4479632f682 | -13.51671 | -46.87261 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 708b20cb-9bc8-3de2-bdcb-b26151e86d2a | -9.17313 | -59.46229 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d350c122-e6bf-3666-8f11-446199346071 | -11.2302 | -55.06544 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8c2a83f-7a8f-39ac-a225-751363c40fd6 | -11.74659 | -49.08644 | 2025-08-28 04:59:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e30deab2-9499-3db0-90f8-e3ca4a9d6e19 | -13.42341 | -46.84898 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 105ac8b7-59c3-3815-a902-d3f436a81fd0 | -8.91489 | -60.71416 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8bcb004-dcd0-3478-a058-7ebd2edcf244 | -10.48532 | -57.96083 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1db3aa-7665-32aa-b757-3adca62e88d3 | -9.48791 | -62.39397 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 395d4613-f9d7-3f6b-848d-15ee8bc94042 | -13.00607 | -56.9002 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e8c0772-7f53-3aa1-9417-1ced7c892722 | -9.41405 | -60.56936 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a2c57840-ae8a-383d-80d1-f38c9efc18fc | -10.52925 | -46.69896 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fabe08cf-ed93-3d21-99e2-030314843fb2 | -8.886 | -60.75444 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1651f9-1379-3f03-89c5-a19c6a617b04 | -9.19375 | -59.64876 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b714cd7-57c4-38d9-bd81-734ca21f43cd | -12.40706 | -47.79006 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19f087cc-b105-3b5d-b94d-54ad3392dec8 | -12.79013 | -48.15987 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1abc954-86bc-3674-9fb8-c896d36ad1dc | -14.13384 | -45.41034 | 2025-08-28 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 621cb887-5c8d-33d9-8a35-413ac7be02de | -11.54773 | -46.37743 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0446ee04-29cd-3e08-a254-4aabd3dc295e | -10.47544 | -57.95158 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adc30827-424b-3d2c-ba3f-1a79bf01867b | -9.73236 | -64.89956 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9de7cfa-266b-3ba2-8390-451d08aec455 | -13.00215 | -56.90324 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c20f2c65-e2b4-3ab7-84c0-22976c31ac66 | -8.94484 | -65.95184 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cff19436-79e0-366b-b3a0-df7dc2416c46 | -9.10575 | -61.42536 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5d4d043-c939-38a8-81db-ef81d7529815 | -13.47676 | -46.85101 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e61d123-a491-34c6-8641-486fc07f0ee3 | -10.32617 | -46.77445 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e7214bf-b63b-391d-80f1-4e31cd5f73fa | -13.0094 | -56.90074 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02cf5307-bf71-385d-8aba-4724c029668d | -9.18055 | -60.86116 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c21b368e-3cc2-386e-8148-983d564b1ca0 | -9.57817 | -55.38659 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0ade48e-af8f-344c-813c-46388bab09bf | -13.08554 | -46.33486 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbb5c3ab-c0c7-3c86-b747-129ab5cbe061 | -14.2724 | -53.06021 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 691a1c20-3b1d-3eb9-98b3-465716cf258d | -14.33862 | -53.34912 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a84723e-e2dc-33d8-94ca-095e4830b988 | -15.09948 | -48.39936 | 2025-08-28 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2447642f-826f-320c-bbbd-46e1d713497d | -11.55029 | -46.35675 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 437f4e4d-c8cf-3e48-afdf-74509f79616d | -14.31004 | -60.3831 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e4aa901-f342-3248-aa8e-69084522d7eb | -10.47397 | -57.94241 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91da102f-79f3-3c15-9644-dff54e544ba6 | -12.89916 | -48.10595 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ded8c7f6-80ea-3950-9299-2a3e3cb01fec | -13.47044 | -46.99378 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04bc1a2a-a703-3f2d-9fcb-2f5d70ad0a1b | -11.54284 | -46.37338 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9fc040a-1fe8-384d-9f15-3c2c3e75e46c | -9.40887 | -60.52586 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 780cc52a-4b69-3635-b5fe-3269eb835f8f | -10.4738 | -57.9366 | 2025-08-28 05:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| e78af6ca-0d58-3e4d-8cdc-9dd117f0914a | -9.1154 | -65.7886 | 2025-08-28 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 36f5de26-fdd3-34a2-b291-9accc25d91e3 | -7.3955 | -39.6845 | 2025-08-28 05:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 860c70b6-8661-31fd-82c7-6946ed4c9616 | -10.8047 | -60.7837 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| d98820ae-5def-3535-a415-139c598c61e1 | -8.2893 | -45.1586 | 2025-08-28 05:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 51143e72-c8e7-378f-b092-9dfe9e0ab426 | -6.8772 | -43.6152 | 2025-08-28 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| d966c6ec-3639-3396-aa3a-c42c75c7c9b7 | -10.7862 | -60.7655 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 32f6af13-1d7f-3823-a26d-8719807d1ad9 | -8.2702 | -45.1833 | 2025-08-28 05:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ebd33f70-7eb2-3f69-9e9a-cf8a1740c267 | -10.8051 | -60.745 | 2025-08-28 05:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e32c91cc-ce8f-32e8-8e7d-b3ace2fa022a | -9.1339 | -65.788 | 2025-08-28 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| b9a8a730-45d9-3407-a2fa-06dc26b07378 | -8.289 | -45.1814 | 2025-08-28 05:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 52055ae6-ff7f-357b-984a-0c192df9214f | -14.2958 | -53.042 | 2025-08-28 05:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |


[Clique aqui para ver as próximas entradas](README66.md)
