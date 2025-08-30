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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0982c808-7db6-32db-8f76-5c55f870c11c | -11.88218 | -46.45028 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33a02c32-06ff-38fd-800d-cbdfca00f6fe | -11.84693 | -46.43729 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5bceb63-63c1-372c-91b6-4565595adc1e | -13.37048 | -51.75594 | 2025-08-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6564174d-2cd5-36c7-956f-72d59dd86e27 | -13.47019 | -46.95 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d3eba1d-884d-3c7a-86ea-f884248c2f13 | -12.84534 | -48.15321 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5eb6fef8-d911-3c28-906a-ceb92fc096e5 | -15.19105 | -53.78246 | 2025-08-30 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b275f36-87df-309c-a81c-e58310c36e6f | -13.4194 | -46.9491 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a46bbaf7-94c5-34ca-b52f-59f5f3b475b1 | -11.29748 | -43.64323 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e622d2af-9d83-3b44-878a-7d161a344914 | -13.55968 | -46.94324 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7957845-0de8-3ba0-98d2-9f990da9be33 | -11.23114 | -45.01655 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55bb5293-95b4-3386-9745-0c138409206a | -11.30958 | -43.6333 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa7c0f10-9115-3447-be54-1245b38c9cc0 | -11.88442 | -46.39301 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9bbbf45-7483-3321-a081-73f6fc18c63c | -14.1544 | -44.74004 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9132ec7e-24f5-36bd-adc1-0b3577aac9b6 | -9.15401 | -59.55802 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0398693f-cdba-3028-a09a-c7c88bde415d | -12.94042 | -48.13032 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9788df68-52b0-3e19-affb-6d769e8d17e8 | -11.86897 | -46.42651 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0140077b-f5f2-39a5-85c1-509c37a80699 | -8.70981 | -50.36348 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 177cd893-158a-3e4e-ad19-e804414dce15 | -13.39048 | -47.00271 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3813f14-f133-3b1f-9dbd-b5ba5e195412 | -16.40697 | -45.65159 | 2025-08-30 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 850243d4-a0aa-3d35-9318-7949707b1ef7 | -12.65329 | -48.19021 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd5bfe0a-f103-3ac1-9f02-ec6eab89504e | -14.32078 | -53.09505 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6583e79-390a-38ef-81cc-bc762939eb69 | -13.55856 | -46.95033 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60e918a3-172c-3e30-af4d-154db0d0a220 | -11.30726 | -43.62498 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59c5faa3-bf70-3ca4-b00d-7fdd00b0ff97 | -12.82308 | -48.11819 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18192c20-d659-3621-8e0c-b4040b9c9e10 | -11.84475 | -46.4297 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 326e10b5-c0cd-37fd-81c8-152005644677 | -11.73935 | -51.76352 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8821957-c8ea-327b-9b89-59b813c8fa4e | -11.29559 | -43.58342 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cef4ea5-1370-30db-9218-5367cb08dff9 | -11.86784 | -46.45515 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c94d84fb-3791-38c8-9cdd-4b40a86adef5 | -13.63881 | -48.16222 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76bb40f7-aee3-3f8a-b333-8cc4bfb45167 | -13.43319 | -46.94778 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddafc8cf-d5ac-3cef-be25-957c2c6a16f5 | -11.30037 | -43.64765 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6d31235-e2eb-3991-83bf-1a3a45ea4949 | -13.56299 | -46.9438 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3de2fe6-ba85-34f6-8d4c-f0f31c42ac6e | -13.37383 | -47.02185 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa4e680d-a820-34ef-86e0-1ccb5f572562 | -13.01147 | -48.72279 | 2025-08-30 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 366a76f0-22ac-3d27-8653-3d04d9b5dc0f | -11.72959 | -51.72193 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1295a2e3-d0a0-356b-9aeb-6cd34f53aa3c | -12.82988 | -48.11932 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71ec8a3f-2952-3c78-b58c-dddad741c314 | -10.16547 | -48.47061 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4733f941-7977-3cfe-8d83-bea70896bd5b | -11.93612 | -46.69061 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e736a4e-249f-33b9-bcfc-1952f447e581 | -11.08114 | -45.13039 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1db916d8-1175-3086-bb1f-5a86272c48d6 | -14.98228 | -48.17587 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 587837af-53f8-3be1-9bc1-baf04c13a437 | -14.04123 | -44.50982 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fa148ea-defa-319b-b020-2ce9623c41ea | -13.75858 | -43.77422 | 2025-08-30 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9766bd63-60f8-39ce-972e-e486d8c66fcb | -8.70583 | -50.36267 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d105d731-a257-3096-b66b-c8803d0f0acd | -13.3866 | -47.00572 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc9db6a5-b6e2-30f3-96ef-766ae566b067 | -13.36873 | -47.01025 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2240e15-f46c-33f9-b288-9847edb2352d | -14.00472 | -44.56687 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07eafb16-ef9c-3a10-88c6-296ae3ac9ae2 | -11.87177 | -46.38731 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| eb7f5498-46cf-35b5-83b2-d1c61d988f84 | -9.76657 | -47.96171 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83745e1c-69c0-382b-89a3-8f3035a973a5 | -13.37509 | -46.88393 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 368b7e6a-071d-3fdf-9173-788abccfbc49 | -12.01273 | -43.99355 | 2025-08-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7053816-81c0-3015-9018-167ec30879d2 | -13.39598 | -47.01091 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6660efc4-15bf-3143-9be0-e8ad5bf7addf | -11.3599 | -43.58131 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2ce8e24a-429c-3ffb-aef4-1fa59c5fa9cc | -13.42326 | -46.94616 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efef431e-74a2-3315-be10-2c78e7e068e5 | -13.38595 | -47.03114 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 824d3c4e-abfe-3ae5-a413-0f5b21ce4858 | -13.38346 | -46.96145 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d5d21c45-327b-316a-9b00-9813af034214 | -15.08624 | -48.16392 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd80b38-d0a2-31b2-84fd-da1781744d19 | -15.08147 | -48.62513 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be8bc70b-d13f-34e7-baa9-8d21c9275f90 | -11.84591 | -46.37946 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19b746a3-9450-3382-953f-6f6b27a7599b | -15.76626 | -47.76758 | 2025-08-30 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7462ed93-a8db-39b5-ba1e-ba0f287416a3 | -8.97224 | -48.19827 | 2025-08-30 04:21:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a5ff39-6ef6-3157-880e-dbde1d656e4c | -11.36107 | -43.57346 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43fc695c-2cfd-39e8-8e55-cb245c6868ed | -12.83143 | -48.08837 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac74d50a-7561-3c9a-ae04-9a7f0442513e | -14.10279 | -43.8938 | 2025-08-30 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af06aec8-b2f7-3074-a818-da0c56e0a58f | -11.29918 | -43.63168 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f437831-5ca2-302b-a281-57a2d4098468 | -9.5847 | -54.46858 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdf0e8e4-d11a-30e9-87f5-a79dad3daa21 | -11.32002 | -43.65865 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9cb6a715-e7e4-35c7-808d-1fda57045ef9 | -13.37884 | -47.01173 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 69a7b2a3-efe5-33d7-b3a5-d6171dd8de58 | -11.33267 | -43.59715 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 50f9345a-a8fb-3ff4-ba52-b4167c95665e | -13.65819 | -46.92336 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 75b386ef-3ee3-3b24-b604-aad842a0f10f | -14.15384 | -44.74089 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 495bcc78-4784-31ce-a132-572c938a3525 | -9.13514 | -49.62311 | 2025-08-30 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79d4c839-67d5-3f72-86a2-1b410303ac19 | -9.80171 | -46.05158 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 044eff26-6fb8-3fb9-ab1d-3ea4f78a554f | -9.65603 | -54.43596 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3c9ed2-f8f9-34cd-bef2-9641ee1509b7 | -13.68358 | -46.91303 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd5e246b-984a-327d-80f6-bdfdcfb6dd8d | -11.92656 | -44.24306 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5568a35d-8bc4-39c7-806d-332661337a52 | -11.33152 | -43.60492 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3731b05b-d582-3279-bb01-3886ee630804 | -13.29114 | -48.84578 | 2025-08-30 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10474d6c-9a84-3ba9-bb7b-d3cac3292c86 | -13.3595 | -54.38775 | 2025-08-30 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04748d25-70ca-3efa-8246-1cea97bb53e1 | -11.57105 | -46.35258 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ef655e2-4048-30d6-a25d-0400d1d95c8b | -12.93764 | -48.12596 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 835fa867-7b89-3795-8692-1e291404f736 | -10.01678 | -48.06903 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e96d049-62f1-3326-a80d-6a8059b511c3 | -14.38779 | -53.22283 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74ce411d-7ca3-3c2d-ac36-abceca961f0b | -11.84974 | -46.39809 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63b44ce2-3dc7-3267-ab65-0acdbefca462 | -10.87989 | -45.13532 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d2cbc1f-884f-3da5-a2ed-585cd4344811 | -12.65204 | -48.19775 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acdbf637-2165-33c2-bba2-e803b182c462 | -13.47237 | -46.95766 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c63e71e-3694-3c99-b429-dfc6a77d3b35 | -11.30369 | -43.57669 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b3f2e4-63bb-3b8a-97a6-ebc65eb6ad02 | -10.45551 | -57.94856 | 2025-08-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10a190f8-4fa3-3811-9433-b834dbb4651a | -11.89905 | -46.70994 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 100c37aa-b75e-3aec-9b3e-13e6b1969211 | -11.41453 | -44.68477 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6ee5b2f-d334-3f4f-87ad-d90a6332d0ab | -11.0064 | -46.86512 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd0388d7-7376-33b3-aad7-7e9af1e1de9d | -11.32229 | -43.61929 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26aca7d1-d977-33a3-b0d6-8f77f95290d9 | -11.31481 | -43.64598 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7fcfc88-e1da-3980-a14f-3a6761fc962c | -11.88273 | -46.44676 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12796b55-80f1-3ab1-aae6-72a2d3b567db | -11.36513 | -43.57008 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 209b1897-d61c-3c41-b045-cc460a52c06a | -14.00821 | -44.59075 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4447701d-529e-3729-9803-f417664f6054 | -11.36165 | -43.56955 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c515fabd-ca46-3bf0-8b0f-812140ed3b6c | -11.84188 | -46.79082 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2985d167-ea78-37e6-82e0-84083b29f715 | -12.62449 | -57.01041 | 2025-08-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95bd44b7-84fa-3809-823e-6b5015de2548 | -13.96854 | -46.33223 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README36.md)
