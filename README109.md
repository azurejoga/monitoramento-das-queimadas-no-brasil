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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14640a49-97ee-3a8d-aee8-42308b7372e6 | -15.70448 | -50.57886 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 420346d6-7106-36cb-a20b-bd852f6da9d8 | -11.36841 | -59.14308 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44034121-3760-3d72-8381-dcab75926f8f | -16.50559 | -55.157 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2caea926-aafb-3e74-a8de-968618af5968 | -16.55676 | -49.22996 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c52fbbb-beeb-3583-b999-45a688afea26 | -16.36357 | -51.5429 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 624c27e5-8c3a-3c1f-bd6d-8bcfc818af30 | -10.62934 | -63.52248 | 2025-09-13 05:27:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a56c2af7-d67f-36e9-9407-d158f81b8d08 | -16.78988 | -51.36147 | 2025-09-13 05:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6429712f-0874-3198-a1bb-2f5764f34477 | -15.86541 | -49.94477 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2f4a983-d2e7-3763-80ea-88fa1a452a3a | -16.35966 | -51.50829 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be592c01-b2ce-3d34-a43e-b1128122db84 | -15.70393 | -50.58416 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84154e8d-18f6-36ae-a037-b792191bea41 | -15.2181 | -56.69308 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4bd607df-82c1-3ab7-be05-b02ec10642ee | -15.18555 | -56.37677 | 2025-09-13 05:27:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97ec80a7-0496-3059-8891-a21b92035485 | -18.16051 | -49.19798 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4e54958d-6772-3219-af41-87405b4e05b6 | -17.09834 | -48.85723 | 2025-09-13 05:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d226c3c3-4f75-3d3e-8e4c-fb3dc4ca3e71 | -15.20222 | -56.68244 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f723643-dce8-34e7-9653-ddc1e9490a7a | -12.80824 | -47.97029 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4108e8db-07c8-3954-92b5-bfe85e6604e3 | -12.79875 | -47.99117 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3f75760-8819-3915-92dd-08ac719bef6b | -12.95636 | -47.98761 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87be4814-048a-399f-9ce4-626e86af83c0 | -10.15449 | -64.73158 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 370f9cc7-dba6-3856-a23f-f267afad2942 | -15.58313 | -54.7518 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ed223f4-6dfc-3131-b680-fc82ad9d2593 | -15.13087 | -52.49553 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24a64f2c-a903-389b-b7dd-185011e8889b | -17.40895 | -49.23917 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 892b6c3a-88ed-33fc-a45f-76db60702fd4 | -15.86769 | -49.94535 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e91e6468-19e4-3fb0-8b83-f2401c517562 | -13.26507 | -51.71045 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38938bd5-d66a-3635-b2cd-1ee97a8f06f7 | -15.13648 | -52.49623 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3aceda9-c4f7-3fa4-b168-a63470453b1e | -11.77472 | -64.93718 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56913194-1599-3359-9243-03ec48c8e87f | -12.95232 | -48.00072 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 64411550-2124-3a2e-a988-4c3467f7cd6f | -16.36296 | -51.53461 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c00ab8f-77b2-3412-b310-6008e5cb8c4b | -15.87208 | -49.94518 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70f26e64-251d-3b62-83a7-b624f23babe5 | -18.14693 | -49.18926 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 0eabc056-5791-3432-95cb-8ae9b421819a | -15.81331 | -52.21244 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4be64919-23e3-380a-bd83-4b34f0807716 | -16.56404 | -49.23558 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb2ef88a-28db-3854-a8d1-ba05c8e16055 | -18.15053 | -49.19109 | 2025-09-13 05:27:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b6847877-815b-3b1b-831f-798813e249d6 | -12.99953 | -47.99287 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 085aadc1-3da9-3688-8c06-d021c7bcd9f4 | -16.33867 | -51.5323 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea21f9da-85ab-3c13-afd0-abe3c85589a3 | -11.79408 | -62.73728 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bd5038c3-400f-3986-b1c2-88f6299352eb | -15.13182 | -52.48708 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ff66560-d2a5-3f10-b231-af79c8006d29 | -12.93354 | -47.99723 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7679b59e-d95d-313a-9c6f-3ea21332c69f | -12.89244 | -62.09199 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cfb476e-500a-372d-9724-c939deea24ae | -16.55075 | -49.22734 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc282cc5-8bab-3eaf-af87-39aa4c1bf53e | -12.8813 | -62.11924 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03358dbe-7fde-3d08-ab68-38774a1c6063 | -12.95093 | -48.01357 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe708fc3-a24f-3f9f-8c45-6a01f4f3ae58 | -14.46837 | -55.95535 | 2025-09-13 05:27:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c58b0464-4bbb-360f-a023-3e0f41aa718e | -12.15728 | -60.74019 | 2025-09-13 05:27:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c7de8f4-97f6-3d3e-ade6-04b4353a47b2 | -12.85743 | -62.11895 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2623c443-01a8-38f8-b79c-696f80f3a7c6 | -12.95568 | -47.9943 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1857811-9043-310c-bb35-2237f81fbbc7 | -15.2107 | -56.68378 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a861394-895e-3558-ad01-13c2ccb43f91 | -11.58243 | -62.22649 | 2025-09-13 05:27:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a554a02-4e73-3b95-895e-cdaed951fca5 | -17.43139 | -49.22552 | 2025-09-13 05:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07836b71-596d-3011-8cf9-2092ead21ac2 | -15.55112 | -54.79858 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df6d08e5-8ebe-3457-8e7b-8e87eb09c3eb | -14.73964 | -60.22886 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e56f988-3545-3844-814b-6bb60272b7c9 | -10.15156 | -64.72665 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 603216fb-e59e-3aa1-bce1-692c1e27ab42 | -15.06913 | -48.0187 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 754c4ef6-cb73-35db-9a0d-cc8184f1dfc1 | -17.23937 | -50.23338 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ddd037f-069f-3363-85a5-e199cf116f6d | -10.63279 | -63.5231 | 2025-09-13 05:27:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2cf4179-88a3-3dd5-b4e8-a966b6f5d3f4 | -15.77448 | -52.24751 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc94dbac-bc85-3792-b1c8-ff6eaa1a4f54 | -12.41821 | -63.88682 | 2025-09-13 05:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cd40ef8-0167-3727-9fdc-215a75f9073b | -11.38649 | -63.3563 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ef0c7c-0388-35be-ac9e-01437b269112 | -15.16469 | -50.15924 | 2025-09-13 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65ec4b5a-8f97-3fd0-9eec-ba6347f8241d | -15.55047 | -54.80415 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b2009f0-bbd0-3246-9307-f11dd1107d4e | -17.44348 | -49.24945 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85d36f7f-5fb6-39e3-8d22-157af8bb73ac | -12.89577 | -62.09253 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3ffd3d-395a-3f2b-85d5-1baf458bf761 | -17.23331 | -50.22702 | 2025-09-13 05:27:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c537eca3-65cf-3029-866e-d1eacf22fb99 | -12.86405 | -62.14183 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed5ae17-eda2-3135-afa9-44b84d2fa39d | -10.15084 | -64.73096 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9bf0d8a-1efc-36ef-ac49-879c1c927bfe | -16.86573 | -49.33984 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 440cf6f9-85a7-379f-9645-42adb28ec976 | -16.33173 | -51.53991 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3786867-c334-3da5-a0bf-7addcb3cc779 | -16.33914 | -51.52785 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9975749-8bca-3b59-808c-55ee37fa9e2a | -16.41043 | -49.24266 | 2025-09-13 05:27:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 881ea3e9-c2b8-315b-9a94-c02967e8bced | -15.16128 | -52.47858 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e64fa47-053e-34e5-a100-d4bc625fc21c | -13.25881 | -51.7139 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f725b6c-958a-388f-a095-74bb9c933187 | -16.52915 | -51.74442 | 2025-09-13 05:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e79dd0bd-accf-3919-bb21-1021ed00c406 | -13.27096 | -51.70869 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0aeccf2-8c23-33b3-aa73-affa3a8a9d3e | -15.67694 | -49.89644 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7b000106-c670-39cc-915d-3e49e75ba455 | -12.87681 | -62.14756 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 598122df-ff30-3411-a796-753e29fdd1f2 | -15.71098 | -50.59005 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91c443ec-3c46-33dd-b980-c49d1f19fa5e | -17.37564 | -52.91022 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 898c9148-9596-3d0d-8c6c-77182350a3b5 | -17.37318 | -52.90776 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a42eb992-8931-3795-819a-d9f4d16d2691 | -16.33269 | -51.53091 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 066dc1bb-cc08-3923-a69d-16e14153d19c | -12.33362 | -59.93064 | 2025-09-13 05:27:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf615d91-a5bd-3542-b8ee-7548c5a8051c | -11.87343 | -62.76869 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91fc2aef-ceed-3001-9971-67085d24753a | -15.0624 | -48.01136 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d8d75f4-ab16-3805-9610-92a2f7e98b2f | -11.37101 | -63.36518 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb078fff-40bc-3492-878f-ee55e082d64f | -15.58119 | -54.75257 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ff89bd91-de0d-35a5-902b-3f58862dd72c | -14.39129 | -60.28895 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c679df67-b87d-3a1a-8171-b907853248d5 | -17.37007 | -52.90903 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309f7421-9bd7-3a1f-958f-bb28f9af07b9 | -15.71033 | -50.58456 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 988f9dc5-472d-3048-8695-39928fff0477 | -15.31856 | -52.90348 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 115aa9fa-389d-318d-a90f-5fd4bf01b915 | -14.46487 | -55.95615 | 2025-09-13 05:27:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8211db5-236d-3b65-9ab1-40266ecc39de | -15.67636 | -49.90205 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eaad5aea-7e75-3114-9fa7-28cd233a082c | -17.41703 | -49.24763 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0646832-8e99-3f8b-91f3-5a5fc1387d1b | -16.49577 | -55.12623 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3212920b-1934-3fb9-9466-07c3557fcdb5 | -15.59873 | -54.77107 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac14d2e2-ec7f-3146-878c-b0daa581e25d | -15.69116 | -50.58282 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7164fd0-50d9-3211-90cf-71329d9ab693 | -10.58052 | -61.2662 | 2025-09-13 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db04f1b2-ef72-388f-972a-31927f823b47 | -15.05512 | -48.00979 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b37d65fa-af58-3dcb-806f-c2dfeebf7de0 | -16.36199 | -51.54356 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e9c4d7c-c4ee-3201-9986-2f27baa0cf4c | -12.893 | -62.08844 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3aa5667-09de-3793-a7ce-613807a2d818 | -12.12465 | -59.83752 | 2025-09-13 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506d5d76-c2ec-3238-9e91-e80e2c163eac | -11.77181 | -64.9323 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README110.md)
