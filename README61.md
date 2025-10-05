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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bddf5c0b-4afc-3505-80c8-5bca11141fd3 | -11.83409 | -45.05203 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc3307b-13ab-30ed-a271-a9964ee094ce | -13.37048 | -48.06374 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 114ece30-34c9-38dc-8d10-73462cebf32b | -11.88566 | -44.97775 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf110ff5-c5c5-30bd-bd06-4118acce7fae | -10.03186 | -50.40768 | 2025-10-05 03:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e61b217-bd27-3510-9247-9484edb21387 | -13.91332 | -48.1972 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4a329dc3-6217-385a-b979-6c50ef01c9f6 | -11.80442 | -46.84368 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 857dd86a-be54-3bc5-8055-897775645f46 | -11.84787 | -45.04673 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4723cd2b-46d6-3e06-b56e-b4b4496e07c6 | -14.68649 | -48.27252 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59d404cf-88bd-3c71-a742-185e3523bb9e | -14.32076 | -47.68689 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b3737f4-a27d-3cae-859c-9528ea37c8e0 | -11.47878 | -45.04598 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f30414-434d-3886-96af-e92ddd0b49ea | -12.65097 | -46.98982 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e5e0f99-073a-34ff-b172-23af77667c90 | -11.09744 | -47.744 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 828fc920-fd68-3ce0-84b3-455c02102ec3 | -13.67672 | -47.31224 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 401a163e-0cc6-32e2-a2d7-5b1ec1519a02 | -18.00468 | -45.01825 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c83a5d-b269-3b6a-b52d-b3d5d6e0552f | -15.4272 | -50.20702 | 2025-10-05 03:55:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ada1753-2c7b-30ba-b5b8-25549ebb3dc3 | -13.2488 | -48.47941 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7df144e-84cc-3172-befa-8daa6ac5c793 | -14.67998 | -48.34737 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33414234-db66-321b-ac67-7caef9beee04 | -13.36947 | -47.54877 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a161e8c-81ea-3b2d-b619-a14fde67964b | -10.75198 | -46.61223 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90acf161-b468-3a7a-bb53-ef548da00355 | -13.24856 | -47.22628 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ad65d23-9a30-3361-8aac-621caf2a3c14 | -14.68255 | -48.34406 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01c005d6-a4e8-31a0-b57f-f1e6e9c060de | -13.29698 | -47.62059 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea750b3a-bca3-34d2-a613-73ed80313bf0 | -13.3348 | -47.7862 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c278cde-c6f7-3f30-a132-3f2ae1918a05 | -13.30407 | -48.08533 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cce8f8f-d433-3bd8-beb9-ec3e56692d01 | -13.30749 | -47.79798 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6732e2bc-f68c-35de-9637-58664366a6b8 | -13.30964 | -48.0874 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12b2227c-fb01-354e-a80c-09230601f5aa | -14.87727 | -48.16084 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 103e3649-cb08-3abe-aaf6-c7e8c0b0736e | -13.27622 | -47.18251 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e32ebc10-6afc-377f-9013-2093055127a7 | -14.94464 | -46.84583 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6396b936-2a0e-36b9-8e56-b72699c45411 | -13.23303 | -47.81902 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d828594-839f-3912-85bb-95c5d1695cc5 | -12.89361 | -47.3213 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01662870-453a-3d44-b0e9-6fc71eb5aca7 | -15.35651 | -47.98055 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6f8a11f-542a-3dbc-a639-86d7f724e3c8 | -14.29933 | -52.92768 | 2025-10-05 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2be00ebf-1f55-3068-aba2-1c500560da83 | -16.3873 | -52.1577 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 36392e58-5ade-3724-85bf-72255f836a57 | -13.32988 | -47.7857 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9695be5f-9892-3d3a-b1db-ab942c631298 | -14.66958 | -48.30679 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8abaf5a-82ed-3e33-b54f-76e5c5ae78a5 | -11.1119 | -49.86407 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de3ac4a9-3200-33bd-86c0-e5c3a2912b92 | -12.31291 | -45.36482 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4615d48d-5b5d-388d-b639-fe07152a57fa | -11.09904 | -47.75891 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57cfc3cc-da4b-3e1d-ba7a-3f9a9e2de9e1 | -15.25704 | -47.95845 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac7f6532-9178-31b8-a4db-421c3e4eb823 | -12.91585 | -47.31218 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f864dcf6-e3ae-3a6f-a2d7-a0424f2b4994 | -12.60575 | -48.12007 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e87e35d2-49d0-3dd3-a4f1-9414575a6877 | -11.83157 | -45.09005 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c47cfabf-720c-37e2-8ed5-f46f06faeb8b | -12.46168 | -45.506 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab933530-eaad-372f-b325-c895dd76d78d | -11.09035 | -47.88762 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da52ddb2-b027-3c49-a981-acd53f0f56ae | -11.67033 | -43.89981 | 2025-10-05 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4d961f44-327d-37d2-9c4f-73e3e5494846 | -11.54987 | -47.69382 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56df7def-12c1-35a3-9f02-9cf67e9f8cba | -13.28743 | -47.61856 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e1297e4-b3b5-3e54-a168-2748374068e1 | -11.78075 | -47.55955 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba0cf2ae-6583-367f-a9fe-2485d9fa67fb | -15.7196 | -46.25484 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7032e67-e24f-31bf-ac04-729f384bc9c6 | -15.98863 | -50.92466 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7377384d-398b-35fa-bf96-36aac866e0b4 | -17.25095 | -46.80499 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f645b6cf-dd7a-3df5-a4ec-4874d965b1e5 | -13.23449 | -47.82246 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd188fd0-3ea2-3a54-ad45-e489d2056ddd | -13.12775 | -47.80096 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb882c14-5c55-39cc-aa5f-5d529e383626 | -14.6893 | -48.27142 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5407d26c-f8bd-3451-a213-c5625708e7c4 | -11.81851 | -45.06724 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e391e55b-f294-3024-98a6-2205b8e42921 | -10.84248 | -47.1926 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6968ffce-7919-36ae-b4a0-37d343144f96 | -10.83774 | -47.98158 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 819bc8d2-0e24-347e-8113-e22c3cf95164 | -13.30788 | -48.12284 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ab56a95-0b05-3664-b62a-0470121d0e28 | -13.10651 | -47.87336 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 299b524b-0545-3f0e-91f7-671509ffd581 | -13.72886 | -51.31057 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a235bd5-ccfe-397b-9869-11d12b49adf9 | -12.70358 | -45.85274 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e07c58d-8137-30bf-a4e9-67c7bc646809 | -11.80352 | -46.82278 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a110da1-7b9b-3b8c-a9fb-f969e2257d88 | -18.3294 | -45.88546 | 2025-10-05 03:55:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| cc4585f6-725e-38c4-9c52-82ae3c699e31 | -12.30943 | -45.36012 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3804301-8a1e-310d-81ec-97acc5b74e0c | -15.90686 | -48.82853 | 2025-10-05 03:55:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 413b0420-7de8-34ec-8680-661a27525882 | -14.67348 | -49.61544 | 2025-10-05 03:55:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43acc024-40bd-3026-ab68-8020072d8a32 | -11.52731 | -47.6767 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43afdafd-db2c-38e0-8ee5-264a638ce187 | -11.81504 | -45.08652 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a16bc77d-cf27-36d1-8a77-97a2125752e0 | -10.75428 | -46.6161 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c4400440-5da4-3d43-90d0-d6dbc1ba8638 | -11.1025 | -47.74069 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b2c59b-cd31-3c3b-bed6-3be02226f2fd | -16.12239 | -53.98608 | 2025-10-05 03:55:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dac40904-d80d-3a79-b97e-1741d3d8898d | -11.1301 | -47.92798 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a37e9a0-bec8-3a6a-8035-dcc15ba5de54 | -15.13571 | -45.72873 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 169d6320-f1e1-3712-8993-5753dae57e3f | -12.39197 | -51.10385 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ae5b0e8-e8cb-381d-9c06-86d2262da4b5 | -13.82513 | -48.06269 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de63ac62-34c2-395e-89cc-757edd39ea0f | -15.20831 | -47.19706 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dbdc7fc-0b4e-3be1-bed7-37796071283a | -11.10324 | -47.87498 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e7f0d95-c5a8-3369-8499-8a41ba8ca64f | -13.7414 | -48.0664 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d77d171-e301-3fe8-9387-f85322aae716 | -11.70785 | -44.44546 | 2025-10-05 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 124be189-e087-3156-8296-7f08494ea543 | -13.27553 | -47.60033 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b52a9d51-a2a4-3707-b088-ee42abb243e8 | -11.02573 | -50.70388 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 526e943e-ab90-37b8-a789-3102741c9350 | -13.45042 | -47.27119 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6de30387-d876-3bec-bc38-c15e6b4a59b6 | -12.26987 | -49.1917 | 2025-10-05 03:55:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bcd7632-0570-38fe-93f5-1eb797bc9fe1 | -14.66282 | -48.3409 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ccd5d01-e815-3268-81f6-e499922a1cbe | -17.97591 | -45.00443 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86f2eef1-8a9c-3a0a-9fb3-7a9de10ec6be | -15.5476 | -46.8489 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb28da80-914b-39aa-b149-d67368006055 | -11.10614 | -49.86293 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c16a3bc-a380-334b-8de2-f4d5390d0868 | -11.4836 | -45.04313 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e883dd93-e215-386a-8c48-97bfba8e245c | -13.25455 | -47.20837 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd6d7ef1-d3bf-3071-93d5-dbec6f15ac5e | -15.30714 | -47.32239 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469d11ec-0c11-3748-b818-ab76dbdd2437 | -13.20378 | -48.53402 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a9449d3-0ffc-31eb-aac8-7503109e3759 | -12.45967 | -44.63962 | 2025-10-05 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 46288772-e6bb-3201-a77e-b2b87c4396d8 | -11.67596 | -47.48515 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e496b6c5-d930-3ef1-916f-f02f081986ae | -15.53707 | -46.83268 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78fb8082-eacd-3a1e-8163-cc4988062d97 | -12.59742 | -48.164 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47aed98b-1166-3784-bebd-a500f0093915 | -12.41016 | -51.10774 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 981b2921-dc78-3d93-b38c-d3c0465046b1 | -13.73951 | -51.26013 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8b389b8-3787-3176-bb96-f7b68051e37d | -13.47722 | -47.23039 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1408235c-69ef-3c4e-b549-0867a031e210 | -15.54802 | -46.82257 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
