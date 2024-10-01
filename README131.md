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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73407ff6-99e6-3c51-8b5a-46de464c34fb | -16.83399 | -55.91971 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e986a2c4-5711-377d-90ab-0b82cd5f5f21 | -16.8334 | -55.89947 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 995c7378-d8c1-3081-8b36-1dbb3c420137 | -16.83283 | -55.90341 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a3b63cba-6ecf-3199-9b73-21d9c42c9ca4 | -16.83226 | -55.90736 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f2562982-9520-33a8-b52f-fbc2c5765c5c | -16.83168 | -55.91129 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8b9a65a4-f7c1-3a53-a008-38efebeb6d06 | -16.83111 | -55.91523 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2cc43d06-b0f2-31f0-8c1d-9334261fd3b4 | -16.83054 | -55.91917 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 422d3508-6163-344a-8e85-76c16fda257f | -16.82937 | -55.90287 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4c08de07-8052-3b70-9e79-c9a67fdb3613 | -16.8288 | -55.90681 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a5f3df84-5bdf-31ef-9a64-450cb8e7812c | -16.82823 | -55.91075 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b981f350-7728-3e30-aeed-98fdfcb2950e | -16.82766 | -55.91469 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f2dc8a79-dd8a-35ee-b3a2-f19b0ead0df3 | -16.82709 | -55.91862 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| df4fe681-58c9-36cb-b9f1-c32ccdb7ed90 | -16.82421 | -55.91414 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 100bb380-d23d-3f8a-bbd4-af07a2f4a68f | -16.82363 | -55.91808 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dfe49286-0cf7-3f3d-9a5f-199450ab0683 | -16.85989 | -55.93586 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 27bb06cc-8a84-380a-b21e-ccd4205ad0f7 | -16.85931 | -55.9398 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 47d7101b-a6e5-3456-aa81-84708c4b91ad | -16.85873 | -55.94373 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 21a2ea41-7c8a-3468-8a43-373f4f89f26b | -16.85817 | -55.92352 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7566334f-12c3-301a-828a-2da11c5d9e54 | -16.85586 | -55.93925 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 76588541-a0b2-34a1-b6cc-9deceb480e4a | -16.85528 | -55.94318 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 00b1d299-69a7-3cf8-98fb-bf81941eb2ce | -16.85471 | -55.94711 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 60d960d0-a06e-3631-b307-ff52c94f105c | -16.85471 | -55.92298 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9e6e5b3e-4592-366d-95cb-c03af3824705 | -16.85126 | -55.94657 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 84988a5c-1130-3149-baa8-887427fa67bd | -16.85126 | -55.92243 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fef97a4f-d275-3543-a684-fd741b6d5f26 | -16.84781 | -55.92188 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3471c430-a2fc-305c-bdfe-594d0473b496 | -16.83918 | -55.95671 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1420d522-d03b-3ab2-99f7-cf4bf3fa5cf0 | -16.83687 | -55.92419 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e065dad6-4101-3404-89b4-f3dc09a946f1 | -16.83631 | -55.95224 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a2fcf3dc-fb04-368c-a6a3-1743c260e21d | -16.83574 | -55.95617 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4304c3bd-5ba0-33b3-af66-b6e45d37ddfa | -16.83342 | -55.92364 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e5747f6a-3246-310b-9f52-e1fe7c58fa25 | -16.83285 | -55.92757 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 53a68609-7c95-3f28-a0c0-4dc8ab1bd3c8 | -16.83229 | -55.95562 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 53dfc30d-6603-394c-a756-03690d8ef32f | -16.82997 | -55.9231 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb71b437-f16e-3387-9681-b3de6627c0fd | -16.8294 | -55.92703 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c42084f2-bb2d-3375-8554-294f9c135380 | -16.82884 | -55.95507 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a639820a-0977-3e00-afb6-450622e9c152 | -16.82827 | -55.959 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0b2a0579-b9b5-3d70-9316-683af2ed78db | -16.82769 | -55.96292 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3a75bbb7-acc0-3dd3-94d1-d6748326a2ec | -16.82651 | -55.92256 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d2d35b34-b9a1-3aba-8ab3-21d42aa47714 | -16.82537 | -55.93042 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d1028989-b4f5-38fc-b8db-2c7f966379c0 | -16.82482 | -55.95845 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3e9331e9-22ec-39f9-a152-b5459ce13da8 | -16.8248 | -55.93435 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8fd2463f-d6c8-345c-b2e3-2e5fc7284e3c | -16.82425 | -55.96237 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 25a8daf5-8925-38b8-abaf-161c522e1c90 | -16.82423 | -55.93827 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e7b0e1a1-e823-3111-808e-d5fdf54862cf | -16.82249 | -55.92594 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6d2da2bb-e820-3f73-a237-acba11178d04 | -16.82192 | -55.92987 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fb7864e3-4b67-3fb6-9682-0cc9b9cdbce2 | -16.82023 | -55.96575 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e9bedb93-d16f-3653-a954-4e5b61d8e12e | -17.16065 | -56.20081 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 536a2586-ed5f-3565-9df3-be212431696b | -17.16009 | -56.18086 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 4b791c6b-7657-3004-b60d-49243f3a7115 | -17.16008 | -56.2047 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 5db704b8-20d9-3f7c-8020-047190a20f3b | -17.15952 | -56.18474 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| e8d6d175-bb3f-382d-9a90-a53d4f8862ae | -17.1595 | -56.20857 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| ca12c861-5c09-35d6-8305-73889a0e768f | -17.15895 | -56.18862 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 64d2f905-f8bd-3a60-907f-01c1aa4da4d5 | -17.15837 | -56.1925 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| be70604d-47bd-3fce-a0d4-cb007333378c | -17.15722 | -56.20028 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 61ec4fa6-ee72-317a-bdb4-8044c35903bb | -17.15666 | -56.18031 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| c2810aec-02e7-348b-8cdb-3609b31d2d11 | -17.15665 | -56.20415 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e9f8d00a-44fd-3fb3-a04c-42f03336d997 | -17.15551 | -56.18808 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 672e706b-9c7f-3d7a-b6a4-2c0ab6092700 | -17.15494 | -56.19197 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 89a55c3c-0bba-31fc-9065-73584eeb29b4 | -17.1538 | -56.19973 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 17bf1256-f189-3549-bc4a-9c73bfce481e | -17.15322 | -56.20361 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| f29eae50-a3a4-3c2a-b5fb-61f3cf8b7fda | -17.15266 | -56.18365 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 33f80c73-39fd-3a57-82a4-99aed4a586ce | -17.15265 | -56.20748 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 2c3939c0-988f-3065-8c39-4bad26cc9cf2 | -17.15208 | -56.21135 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 52c495cd-373f-3648-8426-076ed4af5d23 | -17.15094 | -56.1953 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b10a8490-5504-36c9-addf-06e14e1623b5 | -17.15037 | -56.19918 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 53dd2d88-c0ea-36d6-a5aa-f9b135de93cd | -17.14923 | -56.18311 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ee78360c-8e4b-35f3-84b7-c919cac39362 | -17.14866 | -56.187 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4b78a67f-c88a-35d5-97a8-c27eafd6e2fc | -17.14865 | -56.2108 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9695bb85-8b1b-38d7-b866-fc64335cc7e5 | -17.14637 | -56.20251 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8a610117-7fdf-3b18-90cc-6fa903019c10 | -17.1458 | -56.20638 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0a56d3a2-c2f6-3cc3-91f2-94409ba623f0 | -17.1458 | -56.18256 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f1897465-9709-3bb7-99d3-d03ae3de3b78 | -17.14523 | -56.18645 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 75e15586-78cd-32b5-84cc-067d78503307 | -17.14466 | -56.19033 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e9997a67-d721-3edd-826e-a4fb15828740 | -17.14408 | -56.1942 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3961fa1f-26a9-3619-93a2-dcd963b92675 | -17.14351 | -56.19808 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 80bc1326-328c-3f37-b819-5b448bd63e26 | -17.14237 | -56.18201 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cb92ce1b-b110-34d6-8e19-2c08b8bdfed2 | -17.14123 | -56.18979 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ebd8b1ee-b000-33dd-b81d-e0a93bf3201b | -17.14066 | -56.19366 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 90235f18-6cdb-3b7c-ac83-43c87878f93a | -17.13894 | -56.18147 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ecf99591-152c-3a62-867e-b22bafa9a882 | -17.13837 | -56.18536 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d9b2f876-d7bc-32ae-bfaf-ab3e1bb7dc83 | -17.13723 | -56.19312 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ed963ad8-f7ed-33ee-bc7a-93ff7f80a126 | -17.13551 | -56.18093 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a298d462-31f0-3aa7-9c37-665d189ef958 | -17.13494 | -56.18482 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fc88f547-cd65-35b5-9e40-0283c230a3cd | -17.13437 | -56.1887 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d1ac7ff4-f05b-3a01-b937-2d2528e809d6 | -17.13208 | -56.18039 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 732be142-fbe8-380c-bff4-21070915c1a2 | -17.13037 | -56.19203 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c81c555-53bb-3b2c-bb1e-6aebae83c03f | -17.12808 | -56.18373 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 23fd1f44-c5a0-318e-8646-39ce4317544c | -17.18738 | -56.20797 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 656b0510-abbf-3ebe-8be9-6f33badb72d1 | -17.18682 | -56.21186 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 2bf66ff9-f913-3a4a-8062-99d7d3d69208 | -17.18564 | -56.19577 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 68d4b778-8e3e-37ff-93ae-4f98f592a8e1 | -17.18508 | -56.19965 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 201888fc-3eab-349d-918d-73acab6ebfc4 | -17.18452 | -56.20354 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 6f39a706-bde1-3e82-9fbf-c39abf48840b | -17.18395 | -56.20743 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| ef532574-ac48-30a4-b80f-ed7312874aae | -17.18339 | -56.21131 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 51ccde63-beb6-3678-b36b-2901cd41044b | -17.18278 | -56.19133 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| abcfc456-d26f-3944-81e0-b322bf26e32b | -17.18221 | -56.19522 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4d79d669-7999-38f8-b209-f9e916009c2d | -17.18052 | -56.20688 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 137595ca-bb7f-38e1-8270-78ebd237d590 | -17.17766 | -56.20244 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 655e43ab-b0a4-3e28-8804-03af29f77883 | -17.17535 | -56.19413 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7f5f6e90-a91a-3949-a9e8-8073e8d89a87 | -17.17479 | -56.19801 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README132.md)
