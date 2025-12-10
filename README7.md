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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ad5e24-4564-3628-bd66-524149bbd182 | -6.47399 | -43.54747 | 2025-12-10 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9e9bccd-2cd0-326d-8e00-ac2b9dabd3a5 | -7.04918 | -45.05132 | 2025-12-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 169a7fbc-0646-3608-b740-93755f7a7337 | -6.76492 | -44.20849 | 2025-12-10 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57795c62-5aaa-31d7-ad03-9ea04bb64cf2 | -5.17032 | -43.11476 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cae49d97-93c3-308e-8bb5-a1e042b5814e | -4.50428 | -40.52159 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be288678-ffaf-381d-839b-ea6ae57c4d60 | -3.69254 | -43.82402 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d410281c-c223-3013-9434-b8baa399e2da | -5.60518 | -40.8111 | 2025-12-10 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2c88794-c8be-3942-aaed-5ec6f87fcb6c | -4.42386 | -43.21612 | 2025-12-10 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 431fa28a-bfc2-3ca8-b1d7-7219c76a6614 | -5.4369 | -41.49536 | 2025-12-10 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d728d886-b0a5-3646-a1d7-5cb200aea4ba | -6.63674 | -39.64198 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc30ac2f-4baa-38cc-a97e-d61896b9566c | -3.70148 | -50.94556 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d1c7275-29e5-3625-a190-7f475a182bb3 | -5.84575 | -42.46241 | 2025-12-10 04:08:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2160aa2-09d2-3c6e-8d40-f4eee67e2af5 | -5.16632 | -43.11793 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b6ab5d36-aabe-3d8e-84ea-e397ef159555 | -4.80907 | -41.83153 | 2025-12-10 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dfbab2dd-95b7-3d0b-8c2e-0c9383e952f2 | -7.06352 | -40.39705 | 2025-12-10 04:08:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 41663018-a7cb-301b-aeb2-0b785b616d19 | -6.54995 | -41.70782 | 2025-12-10 04:08:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83f4444f-0815-3d19-b405-bc2b84d9909c | -8.0378 | -39.0278 | 2025-12-10 04:08:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c207c8d-a3f4-37fd-a56f-8365a91bf483 | -5.74295 | -42.05824 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c87ca774-e4a7-3815-8332-d5c4ef6c3892 | -3.69363 | -43.82106 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05c216d6-1783-318b-a05b-fec5ace43471 | -8.66934 | -44.22007 | 2025-12-10 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5358423b-c592-33df-9c28-ac8c8c68378d | -8.67278 | -44.22066 | 2025-12-10 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cf5eb88-09e9-3e6c-9d37-bd0d1e42883c | -4.29586 | -45.93691 | 2025-12-10 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd1171c9-d99b-3f11-96ee-298e297ca11d | -4.90215 | -42.92261 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 474a13e9-e8d5-352d-9aeb-ec7c3fa645ce | -6.07397 | -41.7697 | 2025-12-10 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2e3822c3-17d9-32d3-9b67-0e24db8534e5 | -7.18053 | -36.00034 | 2025-12-10 04:08:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13b954fb-bb39-36c8-8181-5fdbd4407f0f | -4.5015 | -40.5176 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88240fa8-8eb3-3971-8e3e-b4a47ece3522 | -3.69846 | -43.8135 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de350c04-83ce-3400-bdc4-5ab3739a44a1 | -3.69189 | -43.82804 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4982b92b-6133-34ba-83d4-c5244eb9f374 | -6.89903 | -42.83677 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 819fd289-9598-3376-919e-ba8ab2ca44f3 | -3.01182 | -52.68217 | 2025-12-10 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92deeb49-9d13-3559-8929-e5468c12d1c9 | -6.23185 | -44.16188 | 2025-12-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2d3232f-51c6-3681-8a2b-2dd3398181e3 | -3.8316 | -43.31881 | 2025-12-10 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef67d6bb-f7ec-3a18-9620-85632cd38738 | -5.0061 | -41.29329 | 2025-12-10 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1140a3c-1923-37dd-87a4-d4309d1b922e | -5.74517 | -42.06572 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d4522e0-be02-3c62-90ce-9ead72e84be4 | -3.69553 | -43.80893 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4da8218-330a-395e-8ed0-6c10fa42248e | -6.64862 | -35.10872 | 2025-12-10 04:08:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9f0c078f-ef50-3c07-9846-db372f38088a | -4.78673 | -40.36639 | 2025-12-10 04:08:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85ef37fa-422e-3141-8c00-e8d7ce30ebee | -4.44684 | -42.52509 | 2025-12-10 04:08:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 388d565f-93b7-3a05-9476-f710baec6f32 | -9.03545 | -36.66398 | 2025-12-10 04:08:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4cbc8f29-dcb2-327e-a468-03d13617fe70 | -7.92794 | -43.19152 | 2025-12-10 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a7f57a9-2b8f-3807-ac29-800ba3d7242b | -6.23498 | -40.63112 | 2025-12-10 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fed01d92-f971-3770-a0ae-6d3a12289092 | -8.15726 | -43.17681 | 2025-12-10 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1479122e-8352-3a34-b826-f20290cf62f6 | -6.19872 | -39.82538 | 2025-12-10 04:08:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d166b83-38e1-3dc0-b2e0-ba17706c5285 | -4.49819 | -40.51709 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eaf68013-d84a-3b64-8e10-6717efbbf6b5 | -5.868 | -42.42982 | 2025-12-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7d2f161f-8ecb-3851-bff9-859c13aacc66 | -6.90267 | -38.09923 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cec54e1d-178d-3bfc-aaef-18ec578f4877 | -3.23142 | -47.47813 | 2025-12-10 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af9ca68e-f680-3ca8-b2d5-98f33e9e61d9 | -8.59012 | -38.6744 | 2025-12-10 04:08:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 36ae603e-ef6e-3fa2-81fe-7b6b72276ef4 | -4.50096 | -40.52107 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5715088c-6d14-3e72-9f32-169d6421fb80 | -6.07172 | -40.01352 | 2025-12-10 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60dd33b9-6eb0-3ed0-8f92-88d4e1784ede | -6.89833 | -38.10309 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed2c7d64-c88e-3e62-a048-2fdc641bfeca | -3.84581 | -50.96883 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9814042c-809e-3e3d-96a7-32be60d73702 | -3.6949 | -43.81295 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f94250b-37da-344d-b212-b2d053e804c7 | -3.23214 | -47.47379 | 2025-12-10 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 105868d4-143c-3619-8d48-3d838d37876b | -4.29643 | -45.93342 | 2025-12-10 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ceecfcd-ad70-3454-9ce4-bf1ef7aabe65 | -5.33001 | -43.56593 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9a560193-de6a-3c27-9deb-cff2e394ef1f | -6.86927 | -39.77247 | 2025-12-10 04:08:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75199c79-c144-3ac6-973f-712df45d289e | -3.35524 | -46.86453 | 2025-12-10 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe0431a1-b8e2-3195-840b-f697a6665193 | -5.35613 | -38.06257 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 1fbfea4b-9e42-3564-a369-0ffcac36139b | -6.54223 | -43.60406 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d64265a5-b9d6-37ad-9ef0-a65111175c42 | -6.26989 | -43.68085 | 2025-12-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2149986-6164-326b-87d7-590cd8b6ba05 | -5.13524 | -37.68815 | 2025-12-10 04:08:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a255344-0963-33d4-b345-49d10fdba770 | -4.30038 | -45.93424 | 2025-12-10 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847c7bb4-5f47-3747-b432-66cbbd815e0b | -6.36139 | -39.49332 | 2025-12-10 04:08:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c74eee87-3c6d-32f1-9356-aa0852e0c760 | -4.98465 | -41.30054 | 2025-12-10 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5cabdc61-249a-3d58-82c8-064e5fadeec8 | -9.67365 | -37.09354 | 2025-12-10 04:08:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1784284-e571-3f61-8c43-a40b195b7764 | -5.41486 | -40.6571 | 2025-12-10 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba1bbb49-e686-39a6-8853-eb4948f11696 | -3.69719 | -43.82162 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 990c8368-fb14-3c1e-ad9c-7d143fefc2b9 | -17.18157 | -49.66032 | 2025-12-10 04:10:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5110ee18-897a-3200-8948-f320ddca16e9 | -11.81206 | -44.25474 | 2025-12-10 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d293704c-10d3-39b9-9c15-0beaa4bebfdb | -26.83635 | -48.71788 | 2025-12-10 04:14:00 | NOAA-21 | NAVEGANTES | SANTA CATARINA | Brasil | 4211306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e508372d-d3e5-3a97-811c-598a58db0569 | 3.37706 | -51.26844 | 2025-12-10 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f769eb2-7c6a-3aff-a246-bd3e7413e77b | 3.38066 | -51.26399 | 2025-12-10 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6e75e65-fd66-3ee5-8f9c-5814a95ef2d4 | 3.37764 | -51.27226 | 2025-12-10 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc2e3dec-b522-34bb-83d4-0f6214daddb7 | -2.19838 | -45.07918 | 2025-12-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5ed751e-7edd-374b-893a-1f9eac9746f3 | -4.18578 | -41.94759 | 2025-12-10 04:36:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 948412cc-52e0-30a8-adaa-7d0e0538fcc1 | -6.60964 | -39.53028 | 2025-12-10 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3e68d2fb-d2e9-3464-9d8f-cc5d094c3210 | -5.79431 | -43.738 | 2025-12-10 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7ab0521-91ca-30c7-b4a8-7cd172f6e614 | -1.60122 | -49.92765 | 2025-12-10 04:36:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c76cf613-298e-324d-a34d-b637d68dc78d | -0.97485 | -52.44144 | 2025-12-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ebaa60-4427-35a6-83ee-c9e5345062fe | -4.1078 | -46.48321 | 2025-12-10 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6a9edab-a34e-32e4-b2b2-c02d466a185e | 2.03024 | -55.66976 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b209b41a-1471-3447-bd0a-ea9bbfe9580a | -3.02035 | -52.39476 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ff32be2-efd6-3165-af56-994447ad5838 | -6.60449 | -39.52981 | 2025-12-10 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ea4b396-e911-3983-a147-6b1667b37b7b | -3.74333 | -50.76056 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9434982c-f3e2-3d80-8593-c02bed08301e | -2.06919 | -49.00595 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2db1aba-58f5-3681-85c4-044aecd02b18 | -3.67977 | -52.53167 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 002cae86-701e-36ad-959b-8fb05669443e | -4.98871 | -41.29465 | 2025-12-10 04:36:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 766faff0-700e-3f2a-ad33-3bd0b50363c0 | -2.12657 | -48.73395 | 2025-12-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c7c1bdb-a8e5-3088-9527-ab752587adc9 | -2.82437 | -45.27219 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a36f7f25-7692-3dd6-925a-b6ae19770faf | -3.72258 | -47.12395 | 2025-12-10 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9db3c2a1-3306-3886-9cf3-515956abfa75 | -1.08717 | -47.26467 | 2025-12-10 04:36:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc6ae9c1-ab20-399f-89f7-7b8ce78a40f5 | -1.47768 | -53.53582 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a895ad72-ca93-315f-a929-2c0e98d928a7 | -5.35515 | -38.06336 | 2025-12-10 04:36:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7593b9cf-2dcd-31ce-ad39-938313271885 | -5.85125 | -42.45001 | 2025-12-10 04:36:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8066576e-9629-36a1-8663-ed2534f03daa | -1.34467 | -47.34727 | 2025-12-10 04:36:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cbc63aa-4319-3d8a-9265-d72ea845f9dc | -7.1761 | -35.99892 | 2025-12-10 04:36:00 | NPP-375D | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3d1b3a08-1609-3f23-9c24-08d0ad3a67c9 | -1.68478 | -45.68134 | 2025-12-10 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f66dd109-9652-3f3a-9c51-7f58b3d9919e | -2.81636 | -45.27849 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88aa804c-5786-3d30-a883-ccf22d54c673 | -1.73492 | -46.50813 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
