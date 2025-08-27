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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0f86df-66a0-3dcd-9fde-87023f781481 | -8.9295 | -65.9435 | 2025-08-27 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9f39f18f-40f1-31c0-a156-4c1fb8fa3c40 | -8.948 | -65.9429 | 2025-08-27 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 5486bcb3-1e0b-35a2-9e71-c94fcc3b0e83 | -13.6097 | -48.2126 | 2025-08-27 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 5bb14864-6e22-3ced-8d28-ec1b093ad142 | -13.6102 | -48.1903 | 2025-08-27 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a5cb9025-f592-3632-8ceb-96695736dd1c | -10.0977 | -62.9085 | 2025-08-27 13:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 986efebd-050b-3ecd-8f2d-c7654d5d6cf4 | -8.8841 | -60.7699 | 2025-08-27 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 741.8 |
| 37c2f806-8c93-341c-9718-b04ce3cbbe03 | -13.4032 | -46.8987 | 2025-08-27 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2dfb59a6-dee7-3eb9-935d-9a682003729b | -11.5694 | -47.6081 | 2025-08-27 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6603ee2f-e7e5-3d45-8ddb-941dea4107bd | -6.8774 | -43.5919 | 2025-08-27 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 28376909-3cab-3015-9e94-8a8b68f3a434 | -12.7643 | -48.1792 | 2025-08-27 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 7d3d7909-b293-3c0a-b3b9-3fed190b6acc | -9.4183 | -48.2537 | 2025-08-27 13:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 51ad5590-7b51-3c2e-a00f-40709fbe504d | -6.8772 | -43.6152 | 2025-08-27 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 7cf880a9-c3e7-31f0-ac91-a2403bd86057 | -7.4414 | -42.0501 | 2025-08-27 13:00:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| ce01eb18-69c9-3e06-8bd3-83cfe7947784 | -13.6291 | -48.2097 | 2025-08-27 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ef43378d-c7cd-383a-8fc3-7f15ce39812c | -8.9664 | -65.961 | 2025-08-27 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 76df6e78-5165-3d0c-94ee-dad4ee8786de | -6.1783 | -44.0457 | 2025-08-27 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 52182690-d364-30cc-86b4-13c265380601 | -8.2707 | -45.1377 | 2025-08-27 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| bb5f0e8e-8abf-37c7-bd33-24097d8dbac7 | -12.7259 | -48.1846 | 2025-08-27 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0fe1d75f-295e-3eb1-a025-48919439884f | -6.4357 | -44.5535 | 2025-08-27 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8d524489-4334-3dc4-bbf6-81ad8a3be8e7 | -12.7067 | -48.1873 | 2025-08-27 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5a42bdf6-d121-3468-9bba-845a77c1eeb1 | -11.5722 | -46.2844 | 2025-08-27 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8395e935-aa63-386a-b36c-2bb52e1a5113 | -14.1297 | -45.4043 | 2025-08-27 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 5325e33e-ccb1-30f6-a685-659ef36beb21 | -9.4064 | -60.5133 | 2025-08-27 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 265c3f65-1a1a-31ed-96e4-959e348fbdc4 | -12.7843 | -48.1321 | 2025-08-27 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 015fb8b8-db62-3725-9dc6-5911a13cd16c | -9.4062 | -60.5326 | 2025-08-27 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b2fd98f9-0de3-393f-b533-72d7a6f5db07 | -8.9479 | -65.9616 | 2025-08-27 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 465.1 |
| 940c2726-e934-3fcd-85bb-4133a9a76dcd | -6.1783 | -44.0457 | 2025-08-27 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 31349c5a-e8fc-37fa-9909-00e1bcf4c0bc | -13.3838 | -46.9017 | 2025-08-27 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3deb8c36-77ba-3341-8246-60d7f172b0c0 | -11.3146 | -43.5008 | 2025-08-27 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a50e53a7-e1cb-3524-a5af-b4de3dc64f29 | -8.9026 | -60.769 | 2025-08-27 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| aacb6eab-ac5c-3f8a-bb4a-445026f31e71 | -11.3338 | -43.4979 | 2025-08-27 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5efb21e8-8579-38ed-8e2c-8ce1d6e728a9 | -8.4593 | -43.6879 | 2025-08-27 13:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3cdf8786-085c-3bcd-b026-6881f94bd4b0 | -6.8774 | -43.5919 | 2025-08-27 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 275.2 |
| a946ebdc-e68b-3d8c-b397-8223338f6757 | -12.7843 | -48.1321 | 2025-08-27 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 073fc6be-8fc2-33b4-b95c-c7f9e525bb70 | -12.784 | -48.1543 | 2025-08-27 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| de0a7984-8eef-30af-a048-b5206c4e9fa4 | -8.271 | -45.1149 | 2025-08-27 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ac7cfbf6-e958-3609-9ba6-d38771075958 | -8.9028 | -60.7498 | 2025-08-27 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cf02d39c-6723-3aa0-ab23-21637f6d958d | -13.6097 | -48.2126 | 2025-08-27 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| b5ff608e-3159-359e-a4de-d7eb81f18f2a | -8.8841 | -60.7699 | 2025-08-27 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 615.3 |
| cfb5c5f1-1117-3386-bf0c-6cf47b0b98eb | -8.2707 | -45.1377 | 2025-08-27 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d6112f1e-6c0c-3181-a7c3-18fcb573566d | -11.5694 | -47.6081 | 2025-08-27 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 11504692-3ebb-3db1-87d4-0d6a89ba8faf | -12.804 | -48.1072 | 2025-08-27 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 489884ac-35a2-31db-9f86-b8ca529be4e0 | -9.1009 | -49.5621 | 2025-08-27 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b14e4293-db4b-33e7-b9f6-ab49295e0cc1 | -7.6411 | -42.6955 | 2025-08-27 13:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 0c6fcf31-7e39-354b-85af-dd0892f80836 | -8.4596 | -43.6645 | 2025-08-27 13:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e13eb24b-56b1-30d7-aa0e-eb8ec2f95750 | -6.8772 | -43.6152 | 2025-08-27 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 92b220e9-8669-33d7-bc05-04425fca3131 | -8.8842 | -60.7507 | 2025-08-27 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 412.1 |
| f4bc34ee-bf85-34b1-a620-ddbc46b1d7b3 | -7.6414 | -42.6718 | 2025-08-27 13:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 0733e97d-7628-365b-a424-1f54afb6d6f1 | -6.4355 | -44.5764 | 2025-08-27 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 430888f4-19ba-37e5-86f6-87bce58abd52 | -10.4879 | -51.5953 | 2025-08-27 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 41451002-40a4-3ed0-b5ec-de65e3939967 | -8.9664 | -65.961 | 2025-08-27 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| f44f6ffb-cd88-3cd5-9f53-677628c6a26c | -9.9249 | -54.7192 | 2025-08-27 13:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7bc5a566-981b-30aa-be8f-b415d54a6767 | -8.9295 | -65.9435 | 2025-08-27 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9157acca-4976-32af-adea-7b42616bae5d | -8.9479 | -65.9616 | 2025-08-27 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 423.0 |
| fca49b0c-1813-39c2-bd79-100dc22e5629 | -13.6291 | -48.2097 | 2025-08-27 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 0ac49215-9637-3c06-8573-62798c53c120 | -8.9478 | -65.9802 | 2025-08-27 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 31e13a6d-0697-35a8-95e8-1a1ca6cd5088 | -7.4414 | -42.0501 | 2025-08-27 13:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 72295202-6f9c-3c94-a842-913d4a9f2a61 | -8.948 | -65.9429 | 2025-08-27 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 216.2 |
| fdfa27e1-5996-39a3-835f-9bc24ee34c4d | -9.4062 | -60.5326 | 2025-08-27 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| a6fe0584-3163-3f0f-94f0-d40f11d18052 | -9.4064 | -60.5133 | 2025-08-27 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 1fe0813f-a5ed-3981-8022-99b6f7e1c3d1 | -13.4036 | -46.876 | 2025-08-27 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| cbd627d5-1de2-3848-933d-d06246a2a9a6 | -13.4032 | -46.8987 | 2025-08-27 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9f57cfc9-5f56-3f0c-9c69-00d27ac2ed90 | -12.8036 | -48.1294 | 2025-08-27 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 1b1fe707-bdee-3a0d-8f6b-bca531b8b566 | -10.0977 | -62.9085 | 2025-08-27 13:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 11824c79-18a1-3a19-8e84-1dca3da26528 | -12.7843 | -48.1321 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a0076293-21cf-360b-ab20-ce2e796c9e5c | -7.6411 | -42.6955 | 2025-08-27 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 217.6 |
| 72b54151-d1cb-3345-823d-f48b56a3c718 | -8.9294 | -65.9621 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a88e552a-9a10-38cf-a24b-3e8d396dd3f8 | -9.6574 | -64.9845 | 2025-08-27 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 23fab168-092d-39ee-bcce-25b186ac0c42 | -10.4879 | -51.5953 | 2025-08-27 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| dd7f66ec-17c4-3caf-8fc3-a8858cd3bbd2 | -9.9249 | -54.7192 | 2025-08-27 13:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 354bb747-5dcf-3a6b-8ae4-bf4ab948867e | -7.6414 | -42.6718 | 2025-08-27 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 232.3 |
| 2617a144-2b37-3b6b-9fc9-147837c92f3a | -13.3834 | -46.9244 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 02869f8e-4a65-363e-bca7-6e9f0595abac | -10.0977 | -62.9085 | 2025-08-27 13:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 57ed8d9f-e6b0-3c44-8bc0-84388032b296 | -14.3908 | -51.9721 | 2025-08-27 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 57789ac6-c9f2-35ae-8a93-bddbf72055c9 | -8.9479 | -65.9616 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 418.0 |
| 9e8cc50d-f10a-302f-b46e-45932351846b | -9.4183 | -48.2537 | 2025-08-27 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7273b259-c24b-3dc7-a7b5-73dfbac7f9fb | -6.4357 | -44.5535 | 2025-08-27 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 66844707-8442-30a4-809d-039c5b94e266 | -8.4596 | -43.6645 | 2025-08-27 13:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 04ec3b5b-9e7e-32f1-b880-8ae51ca35dd0 | -8.9664 | -65.961 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 06018b8c-e50e-3a7b-a099-5c76464e54fc | -10.7015 | -47.1388 | 2025-08-27 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ede444ab-6d29-3be2-980f-19a004676e9d | -12.7643 | -48.1792 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5127f0cc-fa75-3c6d-b8e4-0fbaa743b4e4 | -13.4032 | -46.8987 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 9268b306-fb3a-386e-887f-d4245b5d4819 | -11.1583 | -44.7859 | 2025-08-27 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 388d8adc-141e-3203-8ec8-be28e9e77a5f | -12.7067 | -48.1873 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 093b3f01-61fc-3b45-b065-a812554045b3 | -11.5694 | -47.6081 | 2025-08-27 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 01698e98-7d59-31fd-9e86-88eb5691bc46 | -8.9478 | -65.9802 | 2025-08-27 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 846a8dfa-0a36-3c82-815b-e5a148dba237 | -13.4027 | -46.9214 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3f13455c-6753-3164-9693-e5a2f29f7a4f | -8.2707 | -45.1377 | 2025-08-27 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a4581340-7358-3e9b-8d63-eb32c7d729af | -6.8774 | -43.5919 | 2025-08-27 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 254.0 |
| ee94f2dc-40c9-3323-b959-4b1bad7faaa3 | -8.9026 | -60.769 | 2025-08-27 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2c07f23c-3f05-323a-9054-70665bb948b6 | -12.784 | -48.1543 | 2025-08-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0cc230a5-c5bb-399a-8d59-675f707f309e | -9.1009 | -49.5621 | 2025-08-27 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c3ac4bb5-36bc-3321-9328-4839ec8cc3a1 | -13.3838 | -46.9017 | 2025-08-27 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f037e185-8c94-3dcc-a300-352e9f8f87a3 | -9.4064 | -60.5133 | 2025-08-27 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| bc7fee4c-e14f-3aa2-80ce-472a5dbc0f5a | -7.4414 | -42.0501 | 2025-08-27 13:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 9a0cc8cd-b080-3631-a082-0a170aa73da8 | -13.0674 | -46.3153 | 2025-08-27 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 271bac9d-b5d0-37ae-873a-ab2ee99c15b9 | -10.6825 | -47.1412 | 2025-08-27 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e8133049-7b01-36f5-a9f0-6d3c99987088 | -8.8855 | -47.1861 | 2025-08-27 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0327a6d4-27e1-3e31-8980-fcbccb70bce5 | -8.271 | -45.1149 | 2025-08-27 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5e6edd8a-4488-3494-a6e9-1432f8144a76 | -9.418 | -48.2756 | 2025-08-27 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |


[Clique aqui para ver as próximas entradas](README94.md)
