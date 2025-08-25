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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bb498d2-7944-3043-8b93-f69363da2d36 | -6.68718 | -58.86552 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e7f4b78-764b-3906-905a-f46144e2afb5 | -10.60205 | -54.8846 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46107fd6-3ddb-38b1-b038-a6fe4d11e25c | -5.43071 | -60.17844 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8cf389a-336d-3a90-b718-056b14075b2b | -7.90391 | -63.0683 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1dece5fc-f107-34d3-a309-ebf8c9057d08 | -8.91603 | -62.42041 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa22accf-569c-3031-9e07-c0d1e492b292 | -9.22315 | -59.67707 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 859d938d-4883-3423-b633-8f194b99bcbe | -9.81375 | -64.26584 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a923a9e-893a-3419-84e0-6a9273f7c993 | -8.65734 | -68.67929 | 2025-08-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fe509c3-8465-3167-8476-35842610c810 | -8.68809 | -62.87292 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a51489d5-d4bf-368f-b86f-d7c92a5bb13c | -8.2291 | -61.38364 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7059b968-fe97-36f0-bb1c-3fa9a95cdbbf | -8.87898 | -62.43061 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0ef81fb-1052-3672-b205-87a192c89a1f | -8.24414 | -61.46771 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f26d55f-ce9c-34b4-b634-f2f4e762ef5e | -8.11699 | -62.86436 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4232eeba-821f-3f15-a2a5-80d6ea629b6f | -9.64325 | -59.63535 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 919ed1d1-3242-3ec6-a1e2-a2545c32b20f | -9.61349 | -55.35299 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31251333-c983-3b6d-8d6d-d86c1399233c | -9.61574 | -55.3607 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a9afd6c-3844-39d3-a62b-231d10ee69b5 | -9.54737 | -48.1391 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89e4a37b-9b11-3e33-990e-fbb280085973 | -5.42066 | -60.16665 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02941d7d-86e9-3320-835f-07ec34344ff2 | -9.64697 | -59.64619 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32fdf477-35f0-322b-8088-b5911bfc7827 | -5.74128 | -57.57934 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 851613a5-519d-3980-aeef-206cd4df9804 | -11.16783 | -55.02986 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69cc012-5870-33fc-96c2-a0ca2a86b62a | -7.59406 | -46.24231 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a65b1ca-6f8d-3280-bda3-84b602622784 | -6.87374 | -45.65599 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6592d696-7a75-334d-8a4b-1ec9283f239c | -6.82285 | -58.96083 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a995d86-cf43-3474-9232-5cab87539a41 | -9.19878 | -60.83294 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b503eeb-96c3-3c76-919c-0c0f981cf1f5 | -6.88045 | -45.65687 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83c2cf5a-7b1d-37b1-909c-a7460751de3a | -6.78944 | -58.63736 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c86acc3a-add2-3514-abdd-0256c491c6e1 | -8.19653 | -61.40389 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19443e86-8571-3a8a-8472-8f48dd653566 | -9.8795 | -64.28345 | 2025-08-25 05:04:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50dce270-eb33-36e6-bbc6-a8324153fb84 | -6.83069 | -58.9579 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07a4a842-6b14-3b24-bd16-1b5906a62f46 | -9.81562 | -64.28237 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a701700-82f5-3b7d-893b-3c97c9e73807 | -9.19657 | -59.49459 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8d1861c-d862-32e3-9419-ca69bdd7e365 | -8.989 | -63.64735 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d408c959-ac06-3091-8d8e-084f634dd409 | -9.40268 | -60.54299 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16634350-5f89-333d-9f08-8021f5a88bf8 | -11.10279 | -44.78741 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b75058e4-5e74-312a-83fc-b06a6501798c | -8.51405 | -63.87874 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8f3c9f3-318a-31a7-9fe9-819ccb6d1811 | -9.13407 | -60.77185 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbdef497-60f4-3ecc-a625-f75100fe3852 | -8.91105 | -62.42371 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e35843fd-cee8-3f23-9ce0-5251bf3c7f52 | -9.19997 | -59.47402 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3611b8b9-8d00-326a-8748-60b9ab7339fa | -9.61629 | -55.3571 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13eda7a9-c90b-3031-9a39-d98e9ec1bcd0 | -7.65912 | -45.39936 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ecbf2a-ff34-3311-83f4-331db0ecc010 | -9.0049 | -65.37846 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e84ed4a-596c-3e2b-b713-7960e48de804 | -8.97121 | -65.41389 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec1bf6f1-b5f6-38f5-af69-560e301f4b28 | -9.24291 | -60.47699 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c57f1e0-d99f-316a-973e-325882e509e0 | -10.89248 | -55.79738 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cec5c7a-c1c1-35bd-959a-6e32b510f4b5 | -12.93653 | -46.31637 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddefe82b-ea4b-3672-b116-35f84eac9839 | -7.81538 | -46.89162 | 2025-08-25 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 157fb324-177d-309a-b07f-284be136fe03 | -6.81823 | -58.9533 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c172cda-0f66-3f7a-87b9-85c8b1ddf208 | -12.75324 | -48.11963 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77f606b9-458d-3878-a478-690b3aeb7a7d | -9.19875 | -60.92793 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c96926bc-8e4a-39e3-849e-08f2f8a0a5a0 | -9.20037 | -60.9182 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a921ba79-8f6d-3f89-8c69-f1f0a9a60373 | -8.06159 | -49.67124 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85910f93-da5c-38a0-99dd-1d0f016d3a3e | -9.21808 | -60.93135 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b46c3d1-f377-3901-b238-c61d7b9b8eee | -6.67672 | -44.42046 | 2025-08-25 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbe1b302-a31b-3d6f-a7ab-cf21fffd0435 | -11.17922 | -55.02396 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c39fd6f-b8c0-354b-9bf4-aa36c00f32f1 | -8.97064 | -65.41714 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7314cd00-6e0a-30d5-951d-f9ea0648e24d | -8.98216 | -65.41401 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d1e9a992-677b-3178-8cb5-433fb467776d | -9.19436 | -59.48576 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e37988-785e-316e-96f1-e324f5693e0c | -9.20263 | -60.83361 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefb4e40-a923-3ba6-ba3c-f856876f80ac | -8.23072 | -61.39868 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae1627c6-fa84-3766-b196-6295e51110e5 | -8.92248 | -62.43411 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9886e94f-85b0-38bf-acb4-ff9c618532be | -9.00373 | -65.38482 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85a0713b-cd97-3c49-8aea-4fddb33e66e8 | -8.97054 | -65.41844 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb4d063c-69ef-3d52-a582-a803b0407597 | -9.22822 | -60.92511 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e8e104-9a39-3901-95ff-57e60ad1f33b | -8.88541 | -62.44437 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6708238-d75a-3816-b75d-0c6dc72f6b55 | -9.51617 | -60.56021 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b11199d1-ac42-3b79-96b1-f34a7abb6bbb | -16.48484 | -46.76324 | 2025-08-25 05:06:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e35dc81f-e838-3fe2-a158-f74b0fc9ec63 | -14.42865 | -56.46841 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a70ca2ce-91ca-3404-956c-4ef2df706049 | -15.03771 | -48.52533 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7cd48db-2ddc-3d6f-8225-69f462f919e0 | -12.06289 | -63.14972 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2df591b7-636c-3fc2-b6b9-270134d0c1a5 | -13.50984 | -46.89859 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9d8db53-ccc8-3d22-bd1b-5fa63cb410aa | -12.59625 | -60.3642 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d336e51-ca55-32ca-ac73-6fda0815ff76 | -14.20928 | -58.62265 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e5237d4-a78f-38b5-b011-fc6764bfff5a | -13.504 | -46.89812 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a29e0f3-3b35-3632-bfd5-4b403b09e139 | -13.05651 | -56.91969 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26388ef1-060c-3ca9-9c0f-d860952e0122 | -13.42578 | -46.91221 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76a30ecd-3e2d-3978-8451-1d49a0b66d53 | -13.39158 | -51.81036 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae6f9a2-20b0-35f7-bd6c-e15af0ff33b3 | -13.50845 | -46.91036 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60d1b250-9f69-3701-ad3e-e1e0adb91ebb | -12.99962 | -56.89271 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 938be40d-6e85-35e0-9cfc-1cfbe4a8779c | -13.46154 | -47.0095 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 688abac7-4484-3f9d-be28-0365cf620b7a | -13.41733 | -51.77769 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 863e8810-2b81-3572-b0fb-2c9f7958c5ba | -14.11056 | -53.99667 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3909171-d0e4-3126-9f21-81db96ee75c2 | -14.43873 | -56.46998 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19017283-0623-3403-a73d-3890c2b0d65d | -14.30178 | -60.38546 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c99415c-1850-386b-b486-396a52639760 | -15.1477 | -59.59955 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08e87792-ecdd-3be1-a7ee-838e69fac739 | -11.69965 | -60.18154 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2144194b-d033-3d72-a7db-314706547c94 | -14.6731 | -54.8903 | 2025-08-25 05:06:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33733e46-ac6e-3d7b-8eee-ac550112c5ed | -14.23655 | -58.62355 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4f98a96-8913-315e-9677-4a2d3754db61 | -15.03598 | -48.50769 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abdf0f6c-4afd-3652-b932-0e971f35cc4c | -13.43275 | -46.90285 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c3b9f4-1ff7-3cb8-8d00-e7668e78cadf | -13.00791 | -56.88315 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 177413a1-d5d6-377d-a123-17a9e2651865 | -14.76255 | -55.92273 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b4fab23-44db-3965-b254-c2c4d373693a | -16.48526 | -46.75901 | 2025-08-25 05:06:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37d82910-8904-35b4-ac3c-5a967329bbd6 | -15.64961 | -52.72817 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2604a7-ae69-3cb7-967d-c41ccb3e80c0 | -16.23659 | -48.14798 | 2025-08-25 05:06:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1645be3-bc75-30ee-bb92-672d145014cf | -12.22272 | -64.23513 | 2025-08-25 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd361e0f-5374-3642-b01f-f82810c80cdd | -14.27535 | -58.61168 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74fd02b1-f6d2-3f7f-a740-7fb2380a36b5 | -13.50165 | -46.91798 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8141625-a2b4-3f5a-96a4-b825a65bd0eb | -11.70393 | -60.17798 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c7a5bc4-daf1-31c8-92c0-7879ee1ff72f | -11.69605 | -60.18092 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README73.md)
