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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e95d0be6-ea73-3e4d-bfae-3efdc7c725e4 | -8.7628 | -46.4642 | 2026-09-02 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| ee4a1730-e6f3-36da-b374-2dad470ed36b | -5.5649 | -60.193 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d9f8fad5-5c5c-3e19-910e-fc30179db5b4 | -7.3487 | -60.5883 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2911a7b9-08f1-3a90-8ed8-93baa3569a6d | -6.6765 | -58.7492 | 2026-09-02 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 04b11c15-78b3-3238-9b2f-3741c5885eeb | -2.8439 | -57.2555 | 2026-09-02 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b8512ccd-9fca-35ce-828b-c5ef3aa80218 | -8.9111 | -62.353 | 2026-09-02 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3674786a-8146-38eb-a9b1-2711a75cb643 | -3.3452 | -42.8067 | 2026-09-02 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9e298afe-e815-3f86-b287-990bef73f181 | -1.0182 | -53.7189 | 2026-09-02 14:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 58ccbfcd-9409-3f58-9007-3807a342433b | -3.3688 | -59.3887 | 2026-09-02 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bdbc72f8-bdd5-3172-bb8b-69a78aaacd17 | -13.5531 | -59.7574 | 2026-09-02 14:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fa3ae1fb-3b0c-3361-af4b-713f85d5580f | -8.7613 | -62.5869 | 2026-09-02 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 439395dc-92d1-37bc-afbe-55bfa864be23 | -10.7242 | -50.8534 | 2026-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1a840150-e02a-352d-b165-485ef035de2e | -6.1928 | -53.4824 | 2026-09-02 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0902e443-36c4-35d0-b295-fa412bf69d5b | -13.9855 | -58.672 | 2026-09-02 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| b1fd70aa-c901-3b5b-8230-d9d4d496bf02 | -12.0936 | -47.0913 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| fe0b117f-68be-3ecf-9560-94c1fc722a33 | -6.7648 | -59.4408 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| efc4b9b2-d5f7-35fc-8ae5-53b1d0afe1fa | -1.4761 | -54.2365 | 2026-09-02 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 432eee61-44e0-37b2-9bd4-2f7a11a39b9e | -7.3118 | -60.5897 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3979ad41-5b3a-32a6-af7b-5e65e0c1fa89 | -7.5326 | -60.7147 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 62b47d14-38eb-35e4-9f99-e705c73df14d | -9.1719 | -59.5017 | 2026-09-02 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 586241c4-237b-394e-8ebf-249d9380e512 | -3.6216 | -60.547 | 2026-09-02 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ce7a5362-a73c-3737-b084-600582a9c5a6 | -7.5139 | -60.7537 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2890b677-b098-3bad-b689-f14db62c7a8e | -10.8815 | -45.3764 | 2026-09-02 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 1589a4d8-1638-3cbe-8da6-6d39ae6e1f4c | -1.5116 | -54.9546 | 2026-09-02 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 48165c66-3925-3755-ba6c-539dd6070119 | -9.139 | -51.1307 | 2026-09-02 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a606278b-67ce-3521-b9cc-4d5912e2991a | -10.5788 | -47.7306 | 2026-09-02 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 991eaf21-6322-3469-adb4-9a21f356abdf | -6.3894 | -45.4664 | 2026-09-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ed5318c5-4fb0-36d6-aa6c-bc0c480b0243 | -17.0878 | -56.8534 | 2026-09-02 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.7 |
| b064e5f9-e7d2-32ab-836a-060925aa5eee | -10.7431 | -50.8514 | 2026-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f612d170-f2a1-3191-8a8f-bcca45986ef6 | -11.1496 | -51.5708 | 2026-09-02 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 25bd7e17-291c-31a5-a7cf-6dbf3ad2743a | -10.746 | -50.6386 | 2026-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9020e901-ec65-3cbc-bd44-bb78c19f22f9 | -5.5648 | -60.2121 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b773bb9f-c5a8-32a4-bf27-752bfbdfd0b8 | -13.9664 | -58.6736 | 2026-09-02 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 0e88c6c0-daf6-3103-b2cc-70c0c740d4e0 | -7.9907 | -46.5177 | 2026-09-02 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 70f81462-5624-3a92-a93d-babb0cd14ad0 | -10.9204 | -45.3253 | 2026-09-02 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 421376b0-a478-39bc-a75f-11c0ceb39292 | -7.0242 | -59.2374 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 66174e6a-7d9a-39b9-bf31-7c234b6a06f2 | -11.5479 | -45.4676 | 2026-09-02 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 47d5a439-ad98-3eba-b2d8-b0e7a174eb88 | -6.6541 | -59.4452 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 74af0914-6dc1-3083-a364-018926c90ce7 | -10.1538 | -45.6982 | 2026-09-02 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e8826b62-4293-38ef-a133-7c3dc68414de | -7.571 | -60.4643 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5b3af0e1-9c75-3389-9256-17396bfd527c | -1.5806 | -47.7245 | 2026-09-02 14:40:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b66c4d8f-9a0e-3aab-b91b-ebb8c9488ee2 | -12.0741 | -47.1164 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| f4a7fa2a-bf4d-340c-bec9-1b660e86f1a2 | -1.959 | -44.7682 | 2026-09-02 14:40:00 | GOES-19 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a1eb1227-7438-34e3-bd8f-107fc6cd3f7f | -9.6633 | -48.2721 | 2026-09-02 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| eadc7c24-8441-3730-ba77-afec3e477ca7 | -3.2455 | -47.9187 | 2026-09-02 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 172bef86-b545-35bd-a5a9-805efca564a9 | -1.5805 | -47.7462 | 2026-09-02 14:40:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| be140190-1784-3bcd-bfb8-83cf2c8a4fb0 | -7.2005 | -60.6897 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| e152dfae-71c1-3274-826e-35e2a1149688 | -9.406 | -60.5711 | 2026-09-02 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3f5f0899-1025-3ee1-8542-33329cf37727 | -7.1123 | -42.7727 | 2026-09-02 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| ae43a9f0-7249-3151-b2ec-bc14510f961f | -8.7615 | -62.5679 | 2026-09-02 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 277487b4-41f4-3aaf-a4f5-d21da4bb4bcc | -8.7817 | -46.4623 | 2026-09-02 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6f53175d-e0f4-307e-8c7a-5831d2900e9c | -12.3622 | -48.1681 | 2026-09-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 5ccfa0ad-2156-3c72-a113-a8a6610809b2 | -6.9115 | -45.6947 | 2026-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f6a2f572-20d7-3439-ba36-80c3fd232900 | -11.0247 | -49.6656 | 2026-09-02 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 100b4d3f-b28c-3ec3-bfbe-db7111a66e6c | -12.1312 | -47.1309 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| ce4978e8-6250-3177-a239-8d35015fe9cf | -11.0437 | -49.6635 | 2026-09-02 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 44519e70-471a-3ca2-ad88-7b10e43440d0 | -6.9113 | -45.7172 | 2026-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 0421fb1b-0ebc-374f-a1c8-733849e01f4c | -6.8756 | -59.4171 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2293a370-4d50-308c-8860-9345393617d1 | -5.9635 | -57.6899 | 2026-09-02 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e3b28de5-72c0-3909-ac54-8e88f89e1d0f | -5.2167 | -60.0507 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 165.0 |
| bd8c17b7-dfa2-3c81-9783-a19e63f4ac5f | -11.3579 | -45.4027 | 2026-09-02 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 3124be45-8248-32e2-901c-ce6b9dff2e4b | -3.2361 | -61.217 | 2026-09-02 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0e0515a8-fdf6-3648-b5aa-7f867d965bbd | -10.0635 | -46.6791 | 2026-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d8893d74-1f4f-3b9d-8bfd-b693ac4dc1e4 | -11.7148 | -50.5109 | 2026-09-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f99958a0-9d6b-36ab-b515-84651f70e5ce | -11.5287 | -45.4703 | 2026-09-02 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 065fca35-12d9-3fc1-824c-3b0eacfa1f33 | -7.3117 | -60.6089 | 2026-09-02 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 65c2dbab-ab65-30b2-9ccf-997783bc485e | -9.6822 | -48.2701 | 2026-09-02 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 05e30504-1b4d-3592-821b-901258e18df5 | -10.1348 | -45.7006 | 2026-09-02 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5c9b88b7-aeed-368d-a163-4f7c839b59a0 | -7.2006 | -60.6706 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 208ae79a-6e77-3015-8634-62ce3afc247e | -3.6215 | -60.566 | 2026-09-02 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| d7894b4f-6164-3091-90a0-eb2395630fcf | -12.1128 | -47.0886 | 2026-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 27a9028a-1f6f-31a5-8b2b-2e5e50e8618e | -12.3814 | -48.1655 | 2026-09-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3f515e3f-a951-3f3e-b8ca-45ab44412a30 | -10.1535 | -45.721 | 2026-09-02 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 64c6da45-62f4-33c0-8488-e95a90114f7d | -13.9853 | -58.6919 | 2026-09-02 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 350e620d-048a-3d06-b891-3fee898615f8 | -6.6883 | -59.9436 | 2026-09-02 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ddd14974-47db-321e-82e5-eecac230cede | -6.93 | -45.7157 | 2026-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| efaa9ca6-6a7e-3098-9862-6fd2c9288569 | -6.6542 | -59.426 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8fafcac0-a6a1-3243-ba10-a8502da1ffdb | -12.1312 | -47.1309 | 2026-09-02 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| b0ead0a3-1908-3b64-84fd-dc12315bae73 | -10.8025 | -50.6539 | 2026-09-02 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fcfeff90-0fbe-3352-9765-fe5f56c2720b | -2.9447 | -60.9002 | 2026-09-02 14:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 9eb7bcb7-5717-3167-8b31-873fff31be76 | -3.3871 | -59.3883 | 2026-09-02 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 36a6cc1e-8fb3-3875-b005-c5fbdae47d09 | -10.6964 | -46.242 | 2026-09-02 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 95e0e95d-ce06-392a-94d1-daad590b8008 | -6.6764 | -58.7686 | 2026-09-02 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0b65b9d6-f293-3369-9b1c-09f5347b5d79 | -12.3818 | -48.1433 | 2026-09-02 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 509f6fd2-79c0-31cb-84df-fd208a15501d | -9.4159 | -45.6271 | 2026-09-02 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ea944608-5708-3ff7-acca-d5432f65acbb | -12.1457 | -44.196 | 2026-09-02 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 57d86e6c-8d73-3bb3-a159-5dd6326ec85a | -9.862 | -64.9771 | 2026-09-02 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 959ed056-5f9c-3554-953a-bfb32ad87210 | -7.3672 | -60.5875 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d84899a1-9e06-397d-86df-9fd970cf9cee | -10.1538 | -45.6982 | 2026-09-02 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a74bc82d-5671-3421-a17b-4019d0259a76 | -10.7641 | -50.7005 | 2026-09-02 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 58fd83f3-e325-309a-b194-c4bc3c9a6248 | -7.571 | -60.4643 | 2026-09-02 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f6d5ab68-9da3-3c96-98e5-feef050eda94 | -11.0437 | -49.6635 | 2026-09-02 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 373431fe-2429-3a32-98c9-4c00fed14314 | -10.7154 | -46.2395 | 2026-09-02 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| bd5c9898-5b19-3695-84a1-1587d7e86c36 | -10.783 | -50.6985 | 2026-09-02 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 16c70721-e99d-3e00-bf3b-75c8699566c2 | -8.7631 | -46.4418 | 2026-09-02 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e7436a4e-b255-3879-a601-b9e6246c757b | -11.1923 | -45.0351 | 2026-09-02 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 7f7120e9-e472-333c-9ae9-5213eedba582 | -3.3265 | -42.8075 | 2026-09-02 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 602509ef-8eab-39a4-9cb4-4fc3bd6a8255 | -11.5483 | -45.4446 | 2026-09-02 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 3fe30c8a-22f9-3e78-9c3e-cbdd06b6a018 | -10.8627 | -45.356 | 2026-09-02 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b3f3cd43-8b99-3ed9-b69f-ce9e4f8077d1 | -10.8891 | -47.294 | 2026-09-02 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |


[Clique aqui para ver as próximas entradas](README81.md)
