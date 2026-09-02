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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b134edda-f1d8-3c23-a74a-d47a6a4a86aa | -3.6215 | -60.566 | 2026-09-02 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| f4e21b7f-5e03-38e5-a450-b6c6876797fb | -14.5948 | -53.6134 | 2026-09-02 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 85bd83a7-4351-3b98-908a-c1d23ce72b7e | -13.5724 | -59.7362 | 2026-09-02 15:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1f15e87d-cbda-334d-b56d-5cdc84edcf0a | -3.6216 | -60.547 | 2026-09-02 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 15771a73-0b47-3b1c-a0a0-49e9d81b37b3 | -8.3717 | -62.716 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 31208acc-3872-33db-8f93-1fc40157468a | -5.9635 | -57.6899 | 2026-09-02 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 42d8673c-8932-3a51-bf7b-0d462e2753e3 | -3.3688 | -59.4079 | 2026-09-02 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| aa86884d-1847-368a-ac5e-cf5189d69dfc | -9.694 | -65.0958 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 347ee5f1-34c6-3820-863d-1350e3edcd19 | -15.3856 | -53.7441 | 2026-09-02 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a0c53c35-bcad-3280-85c8-1f72d6843fd3 | -13.9853 | -58.6919 | 2026-09-02 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e78eb42a-0166-33c9-be42-20f643dda004 | -8.7631 | -46.4418 | 2026-09-02 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7f0d5ba1-e23c-34db-870b-342401ade294 | -7.2006 | -60.6706 | 2026-09-02 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 6f54b383-eec0-345a-93e9-24aba1a5ea18 | -9.8434 | -64.9777 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fc3ab8a1-a060-34b8-8d60-639db9af13da | -13.5533 | -59.7377 | 2026-09-02 15:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6df5d6d4-25ff-30ec-a03a-5061fa977906 | -13.5531 | -59.7574 | 2026-09-02 15:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6192826b-d8a1-35aa-9bed-81b50646fd62 | -9.6941 | -65.077 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0a7ef884-a427-3b21-aea4-6fc66e4d07b9 | -1.0182 | -53.7189 | 2026-09-02 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a2c5d50d-fdb6-3a70-877a-ca76d324975b | -8.7628 | -46.4642 | 2026-09-02 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| dfc6ad41-2cf8-3d52-a2ca-9382274dbbc8 | -8.8589 | -70.6191 | 2026-09-02 15:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e282c955-f2a5-3038-b039-bc36eb0e35f5 | -2.1548 | -47.4735 | 2026-09-02 15:30:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| ae81f570-c635-3f68-af86-6d87fc630bc1 | -7.3672 | -60.5875 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9e43913d-54c2-3d64-a44d-478589b29a78 | -3.3688 | -59.3887 | 2026-09-02 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 0aba45e9-4d8e-3ef3-a9d5-d4a69d547641 | -6.6938 | -58.942 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 51136420-9dbb-33b2-97b6-d6fec130a288 | -11.5479 | -45.4676 | 2026-09-02 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c3b7b847-cbd3-38a5-a30a-6b5db1713550 | -13.5075 | -51.8728 | 2026-09-02 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 714daf72-edde-3831-8893-b1eba16bf303 | -13.9664 | -58.6736 | 2026-09-02 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| dcfd269e-fbbf-3778-b923-e27a1228ff23 | -8.1345 | -45.4923 | 2026-09-02 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 27816bf0-4659-3ee3-8ac4-37d516e64d6b | -15.3654 | -53.7887 | 2026-09-02 15:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6c942a40-4b14-3a85-93cb-b37a0871644d | -8.3718 | -62.697 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e3e31b61-2c65-350d-bc39-6ec7a835e90a | -12.0933 | -47.1138 | 2026-09-02 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 571c833c-8400-30bb-82fb-202ac9b49730 | -8.7814 | -46.4847 | 2026-09-02 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| d0142ca2-76df-33f4-85ad-eb1ef318c2bf | -10.3956 | -49.9918 | 2026-09-02 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 697d1738-c213-376f-a64a-34004f7d1273 | -13.6817 | -51.7872 | 2026-09-02 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 862b4bb7-110f-3213-b6c2-32f3571d8862 | -4.9788 | -55.8417 | 2026-09-02 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 19a4cae7-0672-35eb-a9a5-bb713d0eb515 | -3.8263 | -59.3982 | 2026-09-02 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6027d512-35e5-37c0-8f27-d058f807dd64 | -13.9855 | -58.672 | 2026-09-02 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 68e2844a-4044-3fae-8c52-64cc5339afc7 | -3.7533 | -59.3231 | 2026-09-02 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5e56c606-cc2c-36ca-8b9a-1486df43c079 | -13.8384 | -54.0158 | 2026-09-02 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6852da12-e4d0-30cc-83c3-03fdddcef524 | -5.7937 | -52.2968 | 2026-09-02 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8023a01f-a918-3440-aa5c-3a67ad2bb40c | -8.4089 | -62.6767 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| eee7cdce-0a50-36b3-b216-c4b520014817 | -14.6538 | -53.5433 | 2026-09-02 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cd085641-b1ba-317c-8d4b-5b4d80686ad5 | -3.2361 | -61.217 | 2026-09-02 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| adada687-2d99-3256-8476-d18cbed75d86 | -10.7154 | -46.2395 | 2026-09-02 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4894cdf3-23f4-3f03-96f7-d79a1885caea | -6.7463 | -59.4416 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0d5897cb-0c10-35a8-bb74-1a96ed361835 | -10.4145 | -49.9898 | 2026-09-02 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| f6399b40-b928-30c4-bf03-7209c5642afe | -4.2383 | -62.2349 | 2026-09-02 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c0875aef-cd16-384e-b694-54279f3c42af | -3.6398 | -60.5656 | 2026-09-02 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e016faba-8bef-3c40-b631-63286c26b3c0 | -3.2179 | -61.1985 | 2026-09-02 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e60ae820-1dd2-3360-bceb-bd19f1e49715 | -10.4142 | -50.0112 | 2026-09-02 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7aca83a0-eeff-3c65-bfeb-7efe21b0307c | -9.862 | -64.9771 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a191b36f-5f3e-3597-8939-84bf1868dae0 | -11.8386 | -51.1365 | 2026-09-02 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 80eb7de6-8501-3b4a-8fcd-d7c43526aa9e | -7.2932 | -60.6096 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| be753dd4-e4b0-308e-8398-de2f4246bcae | -7.2933 | -60.5905 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 640091d3-ecb0-30b8-baa0-62e474dcf962 | -7.2007 | -60.6515 | 2026-09-02 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 99387b47-96d7-3a37-b0be-7258bef865d1 | -1.5805 | -47.7462 | 2026-09-02 15:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 9a85e17a-ff9b-3904-aa45-2572dbe578e1 | -3.5161 | -59.0597 | 2026-09-02 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c891b7a2-76e8-3c30-b2e5-932f4d0dd502 | -2.9447 | -60.9002 | 2026-09-02 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cf494659-2db3-363b-898f-76a21fda4f66 | -10.3196 | -50.0211 | 2026-09-02 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| a47729b6-508a-3903-b940-9da9ba2aabfd | -7.0243 | -59.2181 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 30a052e9-d55b-3dcc-8495-637dfbddce37 | -9.8806 | -64.9764 | 2026-09-02 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 896c1c41-8325-3d2e-9a69-c9ddf4ca094b | -13.6233 | -51.8371 | 2026-09-02 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 54c37bd9-7fc1-34e3-9a2f-69b549f575f8 | -3.1998 | -61.161 | 2026-09-02 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9706409f-6307-3b1d-b34a-454ca1525f3d | -6.8203 | -59.4001 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7769a657-31c0-3049-ac45-c1790ccd37b7 | -12.1316 | -47.1084 | 2026-09-02 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 61c3d05a-a574-3155-98bb-1a7b5974ca0c | -7.4735 | -61.3846 | 2026-09-02 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a66d2b33-5f28-3295-9ea8-c02f8fa893c1 | -7.688 | -67.1262 | 2026-09-02 15:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| dbff27c9-aedf-3eab-9da3-c365cde147b2 | -9.043 | -65.4175 | 2026-09-02 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c2d7e6ef-8658-3282-8307-adde984ba014 | -13.8381 | -54.0365 | 2026-09-02 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| d7d9c180-91e6-3afc-8e55-0631a846913a | -7.2005 | -60.6897 | 2026-09-02 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| b731b960-659e-39b6-8b9b-26c39f15226a | -12.1312 | -47.1309 | 2026-09-02 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 3c606763-04a1-3324-a7b1-86fba417562e | -14.6152 | -53.548 | 2026-09-02 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a331b4a7-de73-3df7-80d4-e6e386a707f7 | -6.8757 | -59.3978 | 2026-09-02 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0b32be5d-3c1a-37e8-9ca3-8664c795da66 | -6.1844 | -57.7395 | 2026-09-02 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3fb57a60-ef3d-33da-bc9b-6317353f06ac | -8.7631 | -46.4418 | 2026-09-02 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 5969c7de-c417-3b5f-8922-03f20bc3f44d | -6.6766 | -58.7299 | 2026-09-02 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ece504c0-dcc9-3c36-9c67-1fa63b497855 | -9.6941 | -65.077 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 876a451c-74a3-36ad-a83c-5904bb5f2928 | -9.8434 | -64.9777 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a04d8b02-2c34-342d-aa52-cc815e18e2cd | -3.8263 | -59.3982 | 2026-09-02 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1cc54494-4a55-3512-9826-8d8d98446ddb | -11.5283 | -45.4933 | 2026-09-02 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| aaa4d57a-4380-337b-b8e2-93e2c17ed2c1 | -6.6542 | -59.426 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f88e9370-de7a-30c4-b6b8-2e63d60133fa | -13.5724 | -59.7362 | 2026-09-02 15:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a11d6a92-b903-3e84-b476-c071fea838de | -8.4089 | -62.6767 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e01b49e1-607d-35d3-afdd-53a70b6ce2ac | -13.5533 | -59.7377 | 2026-09-02 15:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e65a4eeb-e73e-3f06-b56f-398ddfb5216b | -7.0057 | -59.2575 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d1d0dea4-36c7-3fdb-b70b-545409f7ab69 | -6.8571 | -59.4179 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0e8cb02c-77f1-31b1-bde1-04586b5a7883 | -7.5326 | -60.7147 | 2026-09-02 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d3a12452-6457-3733-a9f7-5302497e4c1e | -13.8384 | -54.0158 | 2026-09-02 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c5383841-0341-384c-852a-5c55591ea153 | -3.6216 | -60.547 | 2026-09-02 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 00953b55-41c1-31e6-89b7-d07479a0dbca | -13.9664 | -58.6736 | 2026-09-02 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 69da1aa2-534c-3610-8710-e354792f67b7 | -9.862 | -64.9771 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cda34238-2718-30d4-8540-97e7ffe95374 | -13.5075 | -51.8728 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e1fd9f94-9c2a-3b4f-a1e8-5988a62420b4 | -4.9788 | -55.8417 | 2026-09-02 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| a1b4676a-bc7c-316a-b1bc-a829a5ae7b8b | -14.6152 | -53.548 | 2026-09-02 15:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c77fa9b8-7536-30ce-939c-f50a58a4caab | -1.5805 | -47.7462 | 2026-09-02 15:40:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ba613443-420e-3e7f-a6c5-835977c53a71 | -8.7628 | -46.4642 | 2026-09-02 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7ec6b701-767a-35c3-b868-c3599552c547 | -10.3574 | -50.0171 | 2026-09-02 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 49c90610-5588-3795-9778-6b7cd247b397 | -13.6236 | -51.8158 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 025fff1d-a3f8-376f-806f-06689c550c33 | -6.6036 | -58.5972 | 2026-09-02 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4cbd5fdf-ca46-37ed-bb51-6004e0179296 | -6.6358 | -59.4267 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9ee13199-d863-3df2-b271-ca9b273b55d0 | -11.0244 | -49.6872 | 2026-09-02 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |


[Clique aqui para ver as próximas entradas](README86.md)
