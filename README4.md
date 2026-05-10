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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17e76e49-32b2-3818-b617-1fb85205897a | -9.41151 | -50.69289 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddb5675a-0328-3d54-927b-518c3a0e13de | -11.76785 | -43.64464 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 696c3ee2-eba5-316c-9a3a-a21d26f2b5ce | -12.55643 | -46.67854 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d745d0-b73f-37cd-a17b-da07d8a4c08d | -10.55643 | -56.34371 | 2026-05-10 04:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329334d7-7260-3fcc-99a1-92d63b03e4ba | -14.15102 | -45.42534 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c37e4e-aee8-35a0-9bbf-40425348692a | -11.52829 | -43.32803 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81d0fb35-0af1-33ef-b9d4-61f77d19db10 | -13.40313 | -46.60553 | 2026-05-10 04:29:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c93add60-3cc1-3d3c-b4a7-a18820923bda | -11.52451 | -43.32747 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6abd2fb-51b4-3388-afa0-a37ae80fcdfb | -12.76184 | -46.97449 | 2026-05-10 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d618476-4cb1-38ee-b2dc-f86341475638 | -14.14518 | -45.41627 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7773d585-1c0b-363d-b8b4-53ed426be739 | -11.75668 | -43.64293 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736a1dc3-f3e5-346c-ac72-7604292284bd | -13.40034 | -46.60137 | 2026-05-10 04:29:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 276f2af6-acf6-353d-9520-406b5b458e9d | -10.9417 | -49.44069 | 2026-05-10 04:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ebd631e-9076-37f0-b166-366e8b0d4473 | -8.72686 | -47.98102 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e58a1dde-d627-3aaf-91ce-140df04b8b95 | -12.57033 | -46.67709 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e541edd-a3f3-3c4a-ae14-2bbc0b19ca2e | -13.4143 | -47.51293 | 2026-05-10 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37ce6023-ec59-3db3-af0b-cf03a6d6bf2a | -11.84744 | -43.96722 | 2026-05-10 04:29:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d206f12-08ff-3e56-8f6c-6eee71bc6c51 | -12.55698 | -46.67496 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a868ed1-1202-3d21-8a8e-ce1ba63946b4 | -11.77767 | -43.65541 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8dc7fce-6e14-33c0-afbf-830adc5e997d | -11.84663 | -43.9697 | 2026-05-10 04:29:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4492889-d748-3f3e-a58e-e29476a5f2f5 | -9.70015 | -47.69395 | 2026-05-10 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ab5b2d1-1897-33e1-91e2-ef1b5558d31c | -9.00765 | -47.32896 | 2026-05-10 04:29:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 913bbcfd-0d4a-304e-86bf-d33f1cfe56e2 | -11.47594 | -52.91936 | 2026-05-10 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82020b6e-c0f8-339f-8f6c-183069d5dd42 | -11.48008 | -52.92013 | 2026-05-10 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6583439b-9a57-34fe-a31d-229795709420 | -14.14635 | -45.40826 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7db3f6e9-d3ae-380e-a3f7-73b265ae862b | -12.55309 | -46.67801 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59fe263a-ffe4-3592-a604-a55638681d25 | -8.72801 | -47.97383 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb198b51-f41e-3888-a451-046b7f35fc5c | -14.90105 | -45.18364 | 2026-05-10 04:29:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6716149-cb27-3130-b9c5-212cbbef52cb | -11.76412 | -43.64407 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81bd81e4-3c77-3492-858e-651c0d6bf218 | -10.55112 | -56.34283 | 2026-05-10 04:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c280066-1899-3360-9c9e-a4c7e9882847 | -8.72744 | -47.97743 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c500c58-2947-35bc-b8e8-88b844b7f6c5 | -11.41953 | -47.09172 | 2026-05-10 04:29:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 201d17e0-2758-36c3-9d7d-dc51153454a1 | -13.05056 | -43.86274 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64dffda7-6a66-357b-a569-f2a5df1e622a | -15.47727 | -41.64709 | 2026-05-10 04:29:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 333e25d3-7308-3b1b-85a0-e1ae0f2719bf | -11.78072 | -43.66051 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1186b00-9c5d-3cb8-8695-3e7b745fbdf2 | -11.76346 | -43.6486 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4fca542-000f-35de-a9a0-bc630758932b | -8.73079 | -47.97797 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2866b4d-605b-3e0b-8d73-ff6c58f63d86 | -9.41601 | -50.689 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f979616d-810a-34dc-9212-15c947d4a435 | -12.56365 | -46.67603 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9046cef-1de5-308b-ab4d-1ba4277be331 | -10.93824 | -49.44009 | 2026-05-10 04:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 976c4d87-d986-393f-a069-26f3d9c4f255 | -14.14576 | -45.41227 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53c5fd13-d855-3fb5-b238-ff8a04c87b52 | -14.1481 | -45.42081 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f40c12f5-411e-3645-92dc-405358962943 | -9.41678 | -50.68449 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a941c13c-fe58-31af-90c7-a822bc356907 | -11.92735 | -48.4048 | 2026-05-10 04:29:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75b95b9b-7e3b-374e-8aaf-f4922df6bc0b | -9.57181 | -48.44501 | 2026-05-10 04:29:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1621a60-2c95-30fe-b46a-253653058129 | -9.41228 | -50.68836 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18ae1559-76ee-3f7e-81be-37360199275b | -11.65053 | -52.5638 | 2026-05-10 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8fffac5-526d-3a62-ae90-d3c9fc850204 | -11.41843 | -47.07714 | 2026-05-10 04:29:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edb4c292-cf52-3d16-bdc5-4453e87b2b7f | -13.41486 | -47.50939 | 2026-05-10 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34188c3f-c418-314c-82e7-d22ec89419e2 | -12.5631 | -46.67961 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eeeddd13-86cb-383f-aae2-8364369ff2c9 | -9.41074 | -50.69743 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb54e251-14aa-3be5-8fc6-bdc259ea7e4b | -12.27548 | -44.62971 | 2026-05-10 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81367afa-7578-3eed-a287-8b4abf544a48 | -8.72964 | -47.98518 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa07772d-6469-32e0-801e-98e5c8112fa0 | -12.56699 | -46.67656 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8f22ec0-b40a-3b18-8fbe-34e8e097d2a3 | -8.73022 | -47.98157 | 2026-05-10 04:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c13bb547-77d6-314f-a486-e1f2f909a1c8 | -13.0489 | -43.86518 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c1ee73e-5f03-38c0-be49-847e358647b9 | -11.8229 | -47.33323 | 2026-05-10 04:29:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb1523be-db01-32e0-bb7a-67584de5894a | -12.55976 | -46.67908 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c99b94f-27eb-328d-be82-ae78bbc4f155 | -14.30035 | -49.25085 | 2026-05-10 04:29:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d51ba7b-da91-3980-b051-3ab822080c8a | -14.00107 | -42.53968 | 2026-05-10 04:29:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 449877e8-d11b-3e25-a353-5d22312a6233 | -12.0564 | -49.76241 | 2026-05-10 04:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 610204f8-adb6-3f06-bbd8-828c3335a3a4 | -11.77701 | -43.65993 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 432583c6-9c90-3157-918d-d5e0da8e72bc | -14.14869 | -45.4168 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b493772-151e-3a73-9997-a209639cd274 | -12.05575 | -49.76628 | 2026-05-10 04:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2b5b53db-e824-3bce-bbd1-fd02f910a16f | -11.75296 | -43.64237 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8cb7fff-bbb1-3233-95dc-0bcc6bce1070 | -12.0551 | -49.77016 | 2026-05-10 04:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44941da1-290e-3e3c-8e53-079d3954229f | -13.40257 | -46.60916 | 2026-05-10 04:29:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 297780b1-d5e3-3215-bd48-acfbb59b263a | -19.05235 | -46.9072 | 2026-05-10 04:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e810dd9f-cea6-3f2d-b19e-e8a3ba5a8d55 | -15.4743 | -49.49519 | 2026-05-10 04:32:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3561b560-97e8-3870-a01c-e370cc182352 | -18.08082 | -46.36409 | 2026-05-10 04:32:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bacde560-86c3-32ed-80e5-bdf675490304 | -15.34954 | -44.24425 | 2026-05-10 04:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cbbacc30-98b4-32e2-b3af-d5e866ca8760 | -20.21903 | -46.82528 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 468b3d4d-833d-330e-9bcf-55138fd29ce1 | -16.36656 | -47.1189 | 2026-05-10 04:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bde28ca-c1da-365e-98c1-58ac4e3b347c | -20.21611 | -46.8206 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cdb21c3-0160-3ba2-84f4-ff6e37b94213 | -17.38004 | -42.61472 | 2026-05-10 04:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5d1968b-a55a-3c0f-86ec-4b7554748d46 | -18.07732 | -46.3636 | 2026-05-10 04:32:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e0d7a09a-9d4c-3dbb-b816-28c93306298d | -19.46697 | -44.76485 | 2026-05-10 04:32:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b21c630e-ddf5-3ebc-afe2-89e9c422aaad | -18.08142 | -46.35998 | 2026-05-10 04:32:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9f235ee-eaed-3c02-a14d-57adc91c68e9 | -20.23602 | -46.80648 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff34c11c-0816-3aa3-97fa-37537fccd2f0 | -16.3632 | -47.11834 | 2026-05-10 04:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f70bf639-a8ca-3260-b20a-04b732cbb0de | -18.08023 | -46.36816 | 2026-05-10 04:32:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c17467b-38c3-3470-894e-8f7e0209e7bb | -20.21726 | -46.81248 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8ab6488-67e8-3d53-b173-23432a5021c6 | -14.70827 | -48.89887 | 2026-05-10 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cec5e00-b7dd-3d78-82b8-ba1b70f152b1 | -20.21668 | -46.81655 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab76938d-3cf1-3d96-a275-c098f5f85a6d | -20.21845 | -46.82932 | 2026-05-10 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c9f0a32-3c5b-370c-9ded-44953854f6df | -19.69597 | -43.49899 | 2026-05-10 04:32:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77f172fd-3f65-3cec-b02c-1f706f946a40 | -16.86247 | -44.20546 | 2026-05-10 04:32:00 | NOAA-20 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7147388d-d29a-3b97-9885-800d1d4cd3be | -15.35264 | -44.24949 | 2026-05-10 04:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 341b50d2-bb4f-3163-be4e-39ead5907332 | -22.65803 | -46.82987 | 2026-05-10 04:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a92b5ff-6a3d-39d7-b3cd-ad886c285f20 | -29.47467 | -49.93995 | 2026-05-10 04:34:00 | NOAA-20 | TRÊS CACHOEIRAS | RIO GRANDE DO SUL | Brasil | 4321667 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c856def9-1588-3fa8-8379-3ad9e3ef19bb | -27.65248 | -54.52387 | 2026-05-10 04:34:00 | NOAA-20 | TUPARENDI | RIO GRANDE DO SUL | Brasil | 4322301 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a093db70-12f2-3f16-bf4f-0d9d0eeb345d | -30.08351 | -50.79445 | 2026-05-10 04:36:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 62e19a73-0e5d-3bf1-896d-2d4fb9933e48 | 2.3407 | -60.69446 | 2026-05-10 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 724172c0-b19c-3b3b-b67b-e35361be071b | 1.94094 | -60.84414 | 2026-05-10 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45889b30-ec9c-3290-8617-164b5d5b01d4 | 1.64993 | -60.14669 | 2026-05-10 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cf45a18-13b8-3576-a7a4-19a0647d7763 | 2.34139 | -60.69894 | 2026-05-10 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88c67897-e776-363a-8890-b9c6cb4a5c4f | -10.5587 | -56.34244 | 2026-05-10 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cd7f6eb-9f07-38ed-8498-a80e134e7787 | -9.25012 | -60.33555 | 2026-05-10 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf2bc30-1016-3016-9240-1e42fe55edf3 | -9.41789 | -50.69266 | 2026-05-10 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ab67192-5546-3a0e-bbf4-acdb358e6793 | -7.05828 | -55.42987 | 2026-05-10 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
