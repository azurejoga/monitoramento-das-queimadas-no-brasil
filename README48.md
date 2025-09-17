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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cebed781-800b-34da-a1b4-441d2967a287 | -12.69569 | -47.94951 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2d99e7e-2e65-3184-bc37-e5aab34fd3c3 | -15.02508 | -49.2585 | 2025-09-17 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c133174-ef46-3274-8a88-df67e37f41de | -18.54412 | -48.14786 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95e9edf4-da48-3d3e-bffb-98509660b051 | -13.26133 | -54.19462 | 2025-09-17 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6bcbd25-d4b3-3183-9bac-02a2b804d34f | -14.90172 | -51.69346 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd037dbb-0c5b-36e4-8b1a-1e4737911c8f | -12.94967 | -47.95588 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dc10535-36a7-334d-a8b6-752b02311eea | -12.11499 | -44.8112 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 325678d1-7770-3ebb-9f16-bb8495a3e459 | -12.70448 | -45.80721 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06eda074-685e-3ea5-a4ea-954dce48f61b | -14.59868 | -46.37868 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bed1c3fb-3d28-30e4-92ee-3826bb38a202 | -14.18055 | -55.08559 | 2025-09-17 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3149233-3f19-339e-9c23-d8c2d9692aac | -12.72823 | -48.0292 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3d0f609-72bc-31e7-a2bf-78f4ce7890f7 | -15.4113 | -47.33278 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdb7e3a1-6371-34b1-8745-77231d871e50 | -17.96535 | -46.00674 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f46ab3a1-15f1-35e5-b292-382cdc8f5ef4 | -12.94456 | -47.96664 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d24869ca-53b5-3209-999d-55c2d5ac0f5e | -12.71196 | -47.97824 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e3bbffa-aad6-3ddd-b71c-7ceeeaf670a2 | -12.10663 | -44.81472 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47eb46f7-0515-351f-add9-0878be19a591 | -17.96315 | -45.24729 | 2025-09-17 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee755b16-3ef8-306e-983b-d874f36f9dcc | -12.29934 | -50.12614 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ae9ab2e9-2d49-30ad-a740-b8e4144fbda7 | -12.7097 | -47.948 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29b454b8-e5b4-3340-8438-e932e81a5d1e | -11.22428 | -51.43103 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9d52339-6423-37a5-8c70-47b6ab9f8d99 | -12.72374 | -48.01361 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 01d35df0-9e87-35ab-8b2e-7a81c8d1d928 | -12.10261 | -49.1033 | 2025-09-17 04:34:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a36b1eb0-917e-34be-9d96-15bfc7bf791f | -14.63068 | -46.39142 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a74e09e-1b4c-37bb-89d4-de3a8a666020 | -14.90109 | -51.69727 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc8b4274-78f0-3c30-b749-8c54b2d02a61 | -16.61426 | -43.36824 | 2025-09-17 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f79e3f9-1a5a-368a-9f52-a7397a8731ed | -12.69681 | -47.96471 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67b1beac-2011-3ab9-b4d8-ea19fa28de7f | -12.38235 | -51.41702 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 192b86fd-dba9-3f94-bf38-93dcba32e9c6 | -12.11611 | -44.8306 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e646929-3af1-3cb3-a8da-67fc4867b780 | -14.62645 | -46.39505 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ddefa45-8bba-3d55-8180-d4da5342c2cb | -15.40921 | -46.15422 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1926708-1af6-3353-bf8b-6999706dcc84 | -14.93901 | -51.68046 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4eeaa2f-c090-337d-affc-025dc9425072 | -18.3688 | -43.3275 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ab165a4c-fc82-3e9f-82d2-6a20be4dc9d6 | -15.9874 | -46.447 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1c669878-cf4e-39de-9ea9-8ef9f886c51b | -12.7271 | -48.01414 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 878bd067-b895-368a-b429-3050e706560c | -14.83909 | -48.3511 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14277001-5741-3c58-be19-0eff670a2ff6 | -12.69995 | -47.76251 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cb19302-1602-3f6c-bb3a-d42897c6457e | -17.72606 | -43.56215 | 2025-09-17 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e9b6223-cfa5-3654-b65e-1f9a87716747 | -12.70695 | -48.01092 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22ca7371-5e70-3f61-b370-265e58f0403d | -18.16958 | -45.1879 | 2025-09-17 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 354ba961-8dba-30dd-be6b-dc4623556ed0 | -12.44426 | -49.73381 | 2025-09-17 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60ca704e-01a7-3493-bbe5-7847bc3392a1 | -16.64964 | -44.94273 | 2025-09-17 04:34:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b91337f7-8acf-30bb-8d92-391a5b8c036c | -15.42102 | -46.12378 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd9169fc-17b8-3fc4-9689-ea9600a386a9 | -17.34098 | -46.81077 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b441adaf-dc5e-3b6f-84f9-6e4abd923d29 | -12.72543 | -48.02504 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b59cedf-4db5-3ae1-a19d-62d05cfc7564 | -14.99549 | -53.41531 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d238a2f-4786-36e0-9456-f83427e0a5f4 | -14.60474 | -46.39112 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0f0e95b-de49-369b-b862-63903ea1cf38 | -13.22812 | -47.29745 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5bd027a-3d68-3d46-a6c8-f9840c0575bb | -16.70374 | -54.94646 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05298dbd-8712-3a4c-b469-4c33bc0d30ff | -15.4049 | -46.15795 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0405b1d4-548f-3dcc-9a54-9b8f0d8f1e7f | -15.93088 | -42.63646 | 2025-09-17 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 8fbf94c1-b9d1-3ca7-8e82-8c996826f6db | -14.78621 | -51.71303 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d7c3273-460c-33b0-9f43-939399e0d505 | -13.49781 | -43.67097 | 2025-09-17 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1070b51b-ca2c-3e59-bdc0-2a42a7a71c76 | -14.49805 | -47.38363 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a39a8e0-b112-3fe9-8da6-62da5fcc56bd | -12.72486 | -48.00634 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eddb523c-85ff-3319-a604-cc3e07cf18d8 | -17.19563 | -45.91423 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15c212da-b971-3414-b023-9f491338fc0c | -14.50036 | -47.3679 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0383af3-4403-31fd-879f-4915a898bf44 | -12.97256 | -47.95235 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9844e049-fcd8-3c0f-acff-a2310fad8a38 | -17.33301 | -46.81411 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f160b5d-605c-35b9-ad2b-f52eafcd6a37 | -16.84524 | -44.07539 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db20fb7b-1f89-3f4b-991e-a546cc9caa58 | -13.03091 | -47.97688 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83e9ffc5-caf7-366a-93b6-1bd67067ab3a | -18.32341 | -52.05942 | 2025-09-17 04:34:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0f78307-0272-30d0-8755-80301cb61b7e | -14.39376 | -43.53241 | 2025-09-17 04:34:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 527479cb-649a-3310-a29f-6e19ccb2eb01 | -12.44095 | -49.73326 | 2025-09-17 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ea3370-7f2e-36d0-b08d-dc47be6924c6 | -16.031 | -45.16665 | 2025-09-17 04:34:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed682817-1016-3e47-9eb9-1e572510cc04 | -12.70914 | -47.95168 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b779a27e-b7cc-31de-991f-256a6807f327 | -13.22178 | -47.29272 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70de911-bfb8-3fd1-82a5-46892d9685a5 | -14.49919 | -47.37585 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ebf48367-cc87-38d9-b62b-c9c59c21692b | -14.8599 | -50.05029 | 2025-09-17 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a6a0417-dfd3-354d-88e5-f73d8bf4fe70 | -14.49976 | -47.37197 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 537bfb25-fd68-3953-822f-4ce357863461 | -17.32507 | -46.81731 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a369f0ab-6e5a-3ba5-9c8a-2676d13c9723 | -13.62787 | -45.37451 | 2025-09-17 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 559fe2a9-5314-3312-a56d-89423ff8a209 | -13.18002 | -47.31297 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f8909dd-2634-3e9e-8295-7faf742fc912 | -14.31847 | -52.96174 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d67dcee-63a1-3dc8-ab80-7088767322b7 | -16.85507 | -44.05002 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5810b1ea-b0f7-326c-9ebd-5ce9d0772364 | -12.69736 | -47.96107 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4c9e555-2ed0-366e-8bfd-5927973ce8b2 | -15.41785 | -46.14659 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7672ccf-b747-37bf-8148-c6e3c1b9a5b6 | -18.5476 | -48.14849 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9ea26c9-5682-3dbe-9a86-87b707478248 | -13.22758 | -47.30107 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef3e2396-7d06-3ca6-a22c-3c8823bc25ba | -14.8198 | -48.11228 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dd224fe6-2042-33e4-83fd-4a41dadff339 | -14.69915 | -50.39717 | 2025-09-17 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88153b44-5196-3415-a26d-37d1d1de950f | -18.55355 | -49.24401 | 2025-09-17 04:34:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5ab0e90-b172-3f84-bc7a-319919bcf021 | -14.9831 | -53.3993 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f21619d4-ad21-35e8-96dc-e91d4a2863e4 | -12.7546 | -47.9589 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5702e99d-7fb1-3668-bc94-9b7f63081f78 | -12.8637 | -47.14197 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17dce99a-885e-32b3-a892-ffd827906f28 | -12.71645 | -47.99384 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6f5ac88-6fee-3511-a0ce-b1bbc242e55c | -12.72598 | -48.02142 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a9e130f-dc22-3068-8aa0-afa0e6ca5961 | -12.70299 | -47.96936 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37eb8d50-d520-3391-ac4d-7b2d1c3d9248 | -12.11115 | -44.81061 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60445e46-8b8d-3143-8640-6e6f60192dee | -13.91323 | -44.96699 | 2025-09-17 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8993049-0b33-3ee4-a260-d8b4d05953eb | -12.24994 | -46.75691 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b125760-4702-340f-bc9e-98ac76f6fdf5 | -17.20084 | -45.90476 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b654663-ffdf-3631-9182-a464d47082a6 | -12.96415 | -47.96238 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4427c6ae-89c4-3dc6-ae85-68396030a641 | -15.01746 | -49.45812 | 2025-09-17 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9eb4ba31-c338-31c2-a570-b4a266acbf34 | -13.71214 | -49.85593 | 2025-09-17 04:34:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 281c23cc-36b2-37a5-9f78-61443808bb1a | -13.85977 | -44.89224 | 2025-09-17 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6d01851-0872-364b-9713-1b267500751a | -12.35735 | -47.0618 | 2025-09-17 04:34:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e9d9573-f3d9-3a6d-87bc-a5fb15d0a413 | -12.70185 | -47.95428 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 907fa8e9-d3fd-3b80-ba48-ca9e8d8a5319 | -15.5516 | -46.70778 | 2025-09-17 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae1fc2c-519c-3bb7-8fb9-034b2c31259b | -18.19294 | -44.53745 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eeb842ba-14f8-3842-b404-a7603fe2c7dd | -12.70524 | -47.97716 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README49.md)
