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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 561a305e-d9b4-3b13-9f4c-639e045c8967 | -11.71473 | -48.86759 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9604157c-84bb-3c86-ab20-ba65fb2a7c17 | -10.85692 | -44.88589 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e428a08-5c39-3252-b1b3-5b6032458858 | -11.71528 | -48.8639 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e1f60406-bb1d-319a-b03b-72a2a1fb1e1c | -9.74681 | -43.96315 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9077b19-505b-3e53-9976-22a12cfb0d66 | -9.99261 | -44.76644 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfaaa903-0c77-3653-98f3-a1a94806c7f7 | -9.87083 | -44.19217 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbadc9e0-4e8e-3aa5-8f7d-cce547733523 | -10.55456 | -47.92899 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e1e9a94-7d51-38fa-85d6-fbfd4f1f21d3 | -11.71078 | -48.87078 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d1c1a57-e515-3d42-8268-7dad3f54ba6f | -10.85207 | -46.75486 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41bef831-0f6f-3118-842a-693b59370c1c | -11.20329 | -46.62372 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f3ca029-b0d8-34a7-b5a4-226801b4dbbe | -9.71593 | -43.96317 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c2ea613-5be5-376b-a7e9-ff122c5854e4 | -9.47582 | -48.74177 | 2025-11-17 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2eb1597-3cac-3d9c-893d-d0da3d4859ea | -9.32423 | -46.57016 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 813dcec3-d0b5-3127-b8a5-e40450849fd3 | -9.85429 | -44.18592 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 758b9957-5472-303a-8afa-bfcfbcfa90e6 | -13.20646 | -53.32949 | 2025-11-17 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f89fa3-89ba-3d05-b8d8-5a059283e9fc | -10.94964 | -48.68366 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 99965969-1eef-352e-9032-52e564a7892b | -12.4429 | -44.74963 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d0f0c09-9bc7-3401-8d0f-5f89b5edd995 | -10.35741 | -47.67183 | 2025-11-17 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52f7d045-3179-3605-9bc1-5c01ec503c52 | -10.96731 | -44.53136 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46a6dc05-db95-3d60-a772-20737ddb4442 | -11.81067 | -45.31261 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 589dcc1e-bf0a-3a9e-b829-f7089a655c83 | -10.14247 | -44.91044 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f9db01-8297-35ab-9e08-fcf700800407 | -12.33921 | -43.65405 | 2025-11-17 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37f707dd-d114-33b7-84a5-bc7059dee047 | -8.86741 | -50.18662 | 2025-11-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095867c1-c991-36fb-9e07-82c838f82b7f | -10.18951 | -44.50779 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27b5483b-b74a-3fe5-8f0a-0ee3950579ab | -10.03396 | -44.06637 | 2025-11-17 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fac61df-d527-3326-a3d4-27399ca22061 | -9.5824 | -49.11226 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3835a33a-6371-3c3e-9ef4-85e73060d2e1 | -12.86806 | -46.03798 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20ce375b-d9e0-3a23-ace5-8b26877778a9 | -10.83715 | -48.03767 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60e639c1-d2e5-3f39-92c0-eb275412fd06 | -11.3404 | -48.90471 | 2025-11-17 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c24efae4-4640-3dde-9c7e-4eb612ecc878 | -9.71649 | -43.95905 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b05555b-1c82-3922-bd59-8a059a92973f | -13.84002 | -41.79265 | 2025-11-17 04:40:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b613821-e4b0-3f18-8989-e05658c615f9 | -13.8387 | -41.79445 | 2025-11-17 04:40:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0536ddef-ff9f-3e53-8c9b-7150bc4bc2a6 | -12.67617 | -47.16508 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b029497-56e6-3eef-8ee7-bce91f5c856d | -10.86136 | -46.74266 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eda3a2d-bdaa-34c5-9aca-cd97e6c46e40 | -12.86735 | -46.03899 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c9812eb-f79b-31ed-ae09-cd92ee3121f6 | -14.43897 | -46.48547 | 2025-11-17 04:40:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 271a79ef-f65e-3638-b259-e0c504f51a92 | -12.89466 | -54.72657 | 2025-11-17 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46d28fb6-953b-3d44-985d-75a721f16416 | -11.13254 | -44.93097 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e15bfdeb-4c32-32e8-8af5-c05f3bd93e07 | -10.16012 | -44.50359 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d31e1185-7dbd-3a1f-bd95-92debc4bb635 | -10.74972 | -45.14523 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f4ab8d6-3449-312e-9593-a5f245444006 | -10.08625 | -44.133 | 2025-11-17 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6994b9cc-956a-3bb5-b2e6-e7ec04ea32db | -12.00671 | -52.46507 | 2025-11-17 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b5266fc-4c2d-3db6-aa3d-8a25c04b5a43 | -12.96808 | -49.9693 | 2025-11-17 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5b1cfb9-5d9c-3f14-a90a-09e71c93fe37 | -12.00071 | -49.27197 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f68df77-07c8-3148-9968-746d915148fc | -9.72404 | -43.96842 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 52fa00f9-5907-3920-b649-ebab3d78c61f | -14.67185 | -46.59691 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6b93fb4-d7eb-3ad6-b7a1-9df5c3c4de69 | -11.40437 | -43.3296 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 261c7463-61a5-3bd1-8bdc-b5e218a4c673 | -12.6712 | -47.17347 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 455931a4-6b1f-3fe1-8ad6-fcf11cfb0f21 | -11.78765 | -45.29853 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fe6fd95-d837-3be8-80ec-fd2ec1666f96 | -10.93607 | -48.68157 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a34526e6-734e-321c-acf0-dfd3e69b90f9 | -11.67471 | -44.72179 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95947426-67e2-3863-b235-d4a537e04453 | -14.66794 | -46.59637 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dd5cf50-db76-39df-ae6e-dbbd78a3f637 | -10.16691 | -44.51673 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 313a1caf-449f-3da8-8bb9-864345e89f59 | -11.68263 | -44.727 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 347036dd-7cda-3e7b-99d0-45bcc403fc77 | -9.74998 | -43.97213 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00f13e0d-43c9-3037-98ed-e3ba11188834 | -10.37145 | -44.25299 | 2025-11-17 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afaf8a03-1620-3727-8804-53699027a2b0 | -12.86485 | -46.03223 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6c9c8c4-7e1b-3d3a-9224-0f798395c2df | -10.80651 | -47.98162 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b184d8-549a-3d42-b27f-30a718f36eb6 | -12.88425 | -46.46447 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f199bf2-d9fb-3ad0-881a-3db7e704ee15 | -11.13616 | -44.93535 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e2831ae-6fae-366d-8faf-fa9bb9cd8e7d | -11.05635 | -45.15115 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11c3e44e-0c34-39f0-9535-9cbf4624b0f7 | -11.3636 | -49.79479 | 2025-11-17 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc2da600-a2e7-3bb1-b105-dd8a222debbb | -12.86733 | -46.41693 | 2025-11-17 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fccf32a-3b3f-352f-909c-7f003c919240 | -10.64125 | -44.61053 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6478bf85-9fae-3ec9-bad0-f6cccce5b566 | -11.11971 | -48.20825 | 2025-11-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b93aa37b-085f-37b5-b247-2759485f1571 | -9.47528 | -48.74536 | 2025-11-17 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c719475b-ebde-3863-a9e1-1d8a8cac3c86 | -10.23274 | -47.5325 | 2025-11-17 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d90c1f91-88fa-3c29-8ea4-ea285316da7a | -13.2732 | -47.29781 | 2025-11-17 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a7cd47b-1e67-35ed-be4b-aed26b2ee09f | -13.81859 | -44.45544 | 2025-11-17 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f86bb6d-35a2-3311-80b4-2e40c2ceed86 | -12.66079 | -47.16731 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb73fbb-081a-35ae-a60b-bc8a8e40d6e3 | -13.32135 | -47.37866 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cc24cd1-f059-3d20-b4b0-860e71bb4663 | -12.04973 | -46.97482 | 2025-11-17 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b688422f-1feb-3247-9a1d-301e15cedac8 | -10.53823 | -44.16061 | 2025-11-17 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11403ae3-c2c8-3398-b2a2-e917d7f870e0 | -11.81164 | -45.3055 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91603364-da91-34fc-aea1-ae82c7d0dfd8 | -10.95753 | -48.70025 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a935a6d-d09a-3f5e-8f5b-5d4f64483d13 | -12.4381 | -44.75304 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85be21c1-57fe-33ea-b802-25ee3d57840e | -13.05059 | -53.9361 | 2025-11-17 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84693893-09b2-305f-b19b-343c1727b8e5 | -9.58185 | -49.1158 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7bf64651-9e95-30cb-bee7-e8dd499bf31f | -10.54316 | -44.92451 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ee7246-9f1c-3bc3-a6a9-ba1224cb65ea | -12.66512 | -47.16341 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad7e3d9c-caac-3680-aac2-baa7bb471a11 | -12.42949 | -43.16926 | 2025-11-17 04:40:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae56415e-9255-3be8-ad52-95550284446b | -12.87591 | -46.46796 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 992c70a5-131c-3b25-b497-b8fa500fea84 | -9.75114 | -43.96373 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738fb40d-0971-37cd-8492-221ee205107a | -12.51072 | -49.4695 | 2025-11-17 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69e8ae45-00dc-3b92-ae03-8ac60901f097 | -11.7085 | -48.86285 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 944114b4-a0bf-335c-a8c0-70da14d778c8 | -10.6382 | -51.7597 | 2025-11-17 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6149f74-c3e4-3f0a-8f13-962a3aeb09a0 | -13.36093 | -48.1987 | 2025-11-17 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a22bcb6f-14df-388a-9634-4d5d7fd2e926 | -11.81673 | -45.29861 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7c8f105-70fc-3623-940d-1cd6f9a98b18 | -10.8692 | -47.88257 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0d1fe0c-deb6-3f6b-b4c6-105fc7f1744d | -12.31481 | -47.90976 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4abd0f21-7060-35a9-a2cb-baa9688bb9f7 | -10.96841 | -44.52332 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35d90da9-3d6b-3976-ae5b-40285d7a9cb6 | -11.70171 | -48.86181 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e755414-4f0f-3e3a-90e6-3df4b9e17782 | -10.18586 | -44.5032 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01d02530-e669-3f06-aec1-83b8e3c8d36d | -10.65327 | -48.16297 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ba62c1d-b4d8-369f-8bdc-21e4089744b9 | -9.84596 | -47.60664 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0e84510-a56b-3e20-8de1-0107a46e62b1 | -12.87061 | -46.04472 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 052d9bc5-ad27-3b84-95d3-2ba34b20f311 | -10.78982 | -47.5338 | 2025-11-17 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc311754-2e75-3b2c-b17a-5af0d8209e98 | -10.31819 | -44.29201 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48fe0598-0f98-3da8-9a7c-3fd5e60b8663 | -13.20712 | -53.32557 | 2025-11-17 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 343d843f-6770-3eb7-a30c-44862a4ef0b9 | -11.409 | -43.33027 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README38.md)
