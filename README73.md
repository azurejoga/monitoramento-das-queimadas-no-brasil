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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99970a0c-d409-3a95-a5d0-7338d6e2e879 | -6.94516 | -71.50008 | 2025-09-14 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca53c69f-c7a2-3706-9f46-dd2bddc00236 | -6.94464 | -71.49867 | 2025-09-14 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8361a668-fa4f-3e83-95b0-ec9c363b22ac | -7.81355 | -72.90983 | 2025-09-14 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b853d81e-1772-3379-a004-10034fff176e | -8.60736 | -72.375 | 2025-09-14 06:22:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a376534-be14-3acb-8ab0-bc1c4702465f | -10.2321 | -67.34765 | 2025-09-14 06:22:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46acba1e-c087-3aac-98fb-68da8f0ce253 | -11.77928 | -64.94321 | 2025-09-14 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f789e13-e115-38ba-84b8-3c95b485819c | -10.89644 | -68.21807 | 2025-09-14 06:22:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef55b6b9-e6b0-3f5f-8a6c-cf9fc837df20 | -11.7732 | -64.94253 | 2025-09-14 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7bbcbde-cd7a-3749-aaea-137acf60c0bf | -12.7871 | -47.9764 | 2025-09-14 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 62324511-4d6d-39eb-85fd-0662b783cae5 | -12.7675 | -48.0013 | 2025-09-14 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 9f7c4ba1-298b-3e8a-903d-a6469cddfdcd | -18.0303 | -50.9385 | 2025-09-14 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b421f198-187c-39bb-9d62-e07d305321f4 | -18.0502 | -50.935 | 2025-09-14 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c6d556bf-8d1b-3d8f-a125-235198f789d0 | -12.9485 | -54.7313 | 2025-09-14 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 2c95ad28-eeb0-38db-b77f-bba0a01a2849 | -12.8063 | -47.9736 | 2025-09-14 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 47645ba7-8e63-33cc-a950-4b8c22a488f4 | -12.8067 | -47.9514 | 2025-09-14 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 946a7af6-25f8-36d5-b307-02b528408a1d | -12.9294 | -54.7333 | 2025-09-14 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 7e01d534-768e-3738-a152-d2e7c88aa2e0 | -12.9292 | -54.7538 | 2025-09-14 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a65dce41-26fc-3ff4-aa5e-b8ba4296f3d7 | -12.7867 | -47.9986 | 2025-09-14 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 03dd5999-ea9d-3d68-b0a6-f427624a230e | -14.2102 | -46.1979 | 2025-09-14 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 05b69d5f-a721-30b3-9b00-268107f32112 | -14.2107 | -46.1749 | 2025-09-14 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9358ab05-0005-3ead-abf7-6f1eef2043e0 | -12.9485 | -54.7313 | 2025-09-14 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 022d3f3e-30ad-3438-811a-fde8f74a88fd | -14.2111 | -46.1518 | 2025-09-14 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 55977a35-7617-3af3-88bc-d386960a016f | -18.0507 | -50.9129 | 2025-09-14 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 1657e2fa-e530-34c7-b4f1-9a0b53127f51 | -12.9292 | -54.7538 | 2025-09-14 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ce82ebbd-a263-371e-a15e-729f761fc5bd | -18.0308 | -50.9164 | 2025-09-14 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5adce116-0613-3266-a957-d96396c87cf4 | -12.7675 | -48.0013 | 2025-09-14 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9a95f828-008d-3e52-bb6a-67a60eefd96a | -18.0502 | -50.935 | 2025-09-14 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f8bf1951-e366-3cfb-b66a-872a5d8e596e | -18.0303 | -50.9385 | 2025-09-14 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3f0885b4-022c-3eee-ab80-09f39e92f505 | -14.2107 | -46.1749 | 2025-09-14 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9b3ce799-47ec-34d1-b197-f7317dd066fa | -12.9294 | -54.7333 | 2025-09-14 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 238cee93-30b9-33dd-85e2-e25a7254f8b3 | -12.6636 | -54.6782 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 3cf1f0f9-c080-32eb-af07-13972d0e4982 | -18.0308 | -50.9164 | 2025-09-14 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 45e930f5-4e64-3867-a813-8b4d004cab40 | -12.6826 | -54.6763 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 7c8bc457-1a1b-3f37-bcf4-225fb1863873 | -14.7529 | -60.2123 | 2025-09-14 06:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8aad43ac-753e-31a3-9d3c-ecebdcc4547c | -14.7723 | -60.191 | 2025-09-14 06:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c4c03839-fc04-3b8c-8ba5-f5a2140bc26b | -12.6824 | -54.6968 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 012f5664-5de5-3dd3-bac8-676804a7f8cb | -14.7721 | -60.2107 | 2025-09-14 06:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 6ec9416a-abb6-3f50-b808-d89cb9b5216b | -12.9485 | -54.7313 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 81a5e815-95c4-3d37-a7d9-67a58952fe07 | -12.7863 | -48.0209 | 2025-09-14 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 096b36d5-3401-3d06-b3bf-14582660864c | -12.7675 | -48.0013 | 2025-09-14 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| bfe15604-4a94-346e-b379-e3a537dea7d5 | -12.7867 | -47.9986 | 2025-09-14 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| cc618828-f488-309f-b2d0-8fe8f655605d | -12.7671 | -48.0236 | 2025-09-14 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2f458440-80c7-36df-bd8a-8746e02e8004 | -12.6829 | -54.6558 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e8070570-f2a6-3628-af88-691d6893d087 | -18.0507 | -50.9129 | 2025-09-14 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 2f052dce-3c5f-3654-b142-8e682d89b674 | -18.0502 | -50.935 | 2025-09-14 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 130.5 |
| bc33af7b-2882-3a19-a278-78b4fb2fc121 | -18.0303 | -50.9385 | 2025-09-14 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 018e4b60-5c7f-3394-b23c-f6f312e19175 | -12.9294 | -54.7333 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 51a0207c-1c14-38dc-a5ba-d4082bef6710 | -12.7014 | -54.6949 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 915ec496-dd89-3db5-8f14-6362c3dc4fb5 | -12.7017 | -54.6744 | 2025-09-14 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 958bc721-dce2-3734-a9d4-303693cecf74 | -14.2107 | -46.1749 | 2025-09-14 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e6597222-7c9f-3320-90f7-804311a992fa | -14.7719 | -60.2305 | 2025-09-14 06:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e7b9e286-15f4-37dc-8330-a0ada84c2639 | -12.9485 | -54.7313 | 2025-09-14 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 352627e0-ff33-35a8-8eba-433ad080950a | -18.0507 | -50.9129 | 2025-09-14 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5d1b9995-4fbe-37e6-b625-20277ba51697 | -12.9294 | -54.7333 | 2025-09-14 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| fb275099-06b4-3fcb-8a15-b3a422f6dbd5 | -15.9032 | -48.154 | 2025-09-14 07:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 47026b60-5893-3bd5-9a80-1491c956c2ca | -15.8836 | -48.1574 | 2025-09-14 07:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 24baf3bd-462c-3a26-b3ea-986fa5670c41 | -12.7671 | -48.0236 | 2025-09-14 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 84decc5d-865c-3fdc-9e58-1760ffbeefa2 | -12.7675 | -48.0013 | 2025-09-14 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 69da96fc-7b3c-3600-b846-96cbac03d35c | -12.7863 | -48.0209 | 2025-09-14 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 98313dab-d9be-37d0-9999-71b28128db88 | -12.7867 | -47.9986 | 2025-09-14 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 9a0ceb20-3b17-3fe5-af25-a939dcfd73f6 | -14.7719 | -60.2305 | 2025-09-14 07:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 813bbac7-e6da-3260-8f2f-2b2eb133e5af | -18.0502 | -50.935 | 2025-09-14 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| db0ed58b-2123-3717-ab9d-a239178bef7a | -18.0303 | -50.9385 | 2025-09-14 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9a346f0a-8c01-3cd2-af2e-fdbe9513bfa5 | -15.9037 | -48.1314 | 2025-09-14 07:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 43.5 |
| d0f519e2-e356-3344-9306-e43ad1c60aaa | -12.9292 | -54.7538 | 2025-09-14 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 36371261-73fa-3b97-87e9-329b19898dca | -12.7478 | -48.0263 | 2025-09-14 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 89b43c00-2c52-34d8-8d08-e345185a0e9c | -14.2107 | -46.1749 | 2025-09-14 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3ec2698f-2e2a-3230-bd0f-ded6f186afe8 | -18.0308 | -50.9164 | 2025-09-14 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 59930c93-3feb-30c5-a5dc-f6516cc08319 | -18.0308 | -50.9164 | 2025-09-14 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e54310f4-dd54-3482-9980-29b328220933 | -15.9037 | -48.1314 | 2025-09-14 07:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 48.7 |
| cdf01ec3-7592-31d4-b30a-8794da757693 | -12.7863 | -48.0209 | 2025-09-14 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 64bed15a-1deb-3e1e-966d-bf2ef4d6cd17 | -12.9485 | -54.7313 | 2025-09-14 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d69d4bf8-338b-35a4-85a3-5fcfe8766aeb | -18.0303 | -50.9385 | 2025-09-14 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f7f13f78-5b97-30b0-a2f0-c54168ffbe09 | -15.8836 | -48.1574 | 2025-09-14 07:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 33c9acf6-61b8-3baa-9c7d-8474ce95d4d5 | -12.9292 | -54.7538 | 2025-09-14 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| f6ee8488-91b8-33f7-b051-1ee60d30705d | -14.2107 | -46.1749 | 2025-09-14 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b4933877-6499-3199-a9cc-e5477124b425 | -18.0502 | -50.935 | 2025-09-14 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| abe497a7-ea1f-36cc-bf5e-a52d23e50407 | -12.9294 | -54.7333 | 2025-09-14 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 5f768d68-c214-3aca-8715-44fa08a39852 | -12.7867 | -47.9986 | 2025-09-14 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 342d0f8a-8069-35b1-a217-a978b1a1d9a8 | -15.9032 | -48.154 | 2025-09-14 07:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 103.6 |
| e6622c38-92b3-3c2d-8749-661586b8f9c9 | -18.0507 | -50.9129 | 2025-09-14 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c1114477-4b7c-30ee-b597-6ff8f639b3da | -14.2102 | -46.1979 | 2025-09-14 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d687d779-0082-3693-8287-3e7dc77aaf7c | -18.0502 | -50.935 | 2025-09-14 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 60171bf6-5023-3cb5-b0e6-5701dfacc779 | -12.9294 | -54.7333 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 198e0903-d329-3ed9-be27-95c0f41db715 | -12.7863 | -48.0209 | 2025-09-14 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ca7224fb-2b44-33b0-8419-51b25d2407fe | -12.9292 | -54.7538 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 041d8fc9-de74-3def-9d38-dc34acb34764 | -11.8294 | -50.4763 | 2025-09-14 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2487eb57-e3a8-37e3-989d-4f0ca2e71797 | -15.9032 | -48.154 | 2025-09-14 07:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 260b22ed-2971-35bf-9fcc-1ea5b6bc0192 | -15.8836 | -48.1574 | 2025-09-14 07:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 44f8193f-e674-3f13-be40-c2feb33c5df7 | -12.9485 | -54.7313 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 31536c21-c720-3f80-83bf-d8d7f1ba4dce | -11.8103 | -50.4785 | 2025-09-14 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d962ea59-2da1-39df-8a11-ef69efa2a23a | -12.6636 | -54.6782 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a7d37146-5529-3397-82fd-38ed2ce8cbaf | -12.6826 | -54.6763 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| f50e75d0-385a-3eeb-8d9a-8f5cab702ffc | -12.6824 | -54.6968 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 22ebf7df-1ac0-3217-961d-e1378fe5d7a6 | -18.0507 | -50.9129 | 2025-09-14 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8f250abc-bfa6-3d87-88c9-164894cebe12 | -18.0303 | -50.9385 | 2025-09-14 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9cc180c5-9f06-36be-816a-a98e87df5567 | -12.7014 | -54.6949 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 806169dd-2919-32b7-901d-6a3f7ecd264b | -12.7017 | -54.6744 | 2025-09-14 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| aa3f37f5-b944-3624-b135-d42e430018df | -14.2107 | -46.1749 | 2025-09-14 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d3337cc3-f3b4-3572-b1ec-cb96d3d8e3c0 | -18.0308 | -50.9164 | 2025-09-14 07:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |


[Clique aqui para ver as próximas entradas](README74.md)
