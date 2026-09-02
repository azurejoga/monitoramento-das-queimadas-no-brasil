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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe83b721-0332-3024-a34a-90c9b97f9221 | -13.9855 | -58.672 | 2026-09-02 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 611d7aaf-e3ac-3b13-905b-7adf20f39dbc | -4.2383 | -62.2349 | 2026-09-02 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4ae03351-12d7-37f5-89b5-5d496f25857a | -7.4735 | -61.3846 | 2026-09-02 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 020cb87d-f6d0-39d4-857a-600b814ff62f | -12.01 | -60.5345 | 2026-09-02 15:40:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bce407ce-8baf-3f28-832e-34295e657f50 | -7.2931 | -60.6287 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a09a2133-4671-3b70-94b6-3ea9a07e9e79 | -3.2179 | -61.1985 | 2026-09-02 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6775d27b-ab4d-3d3a-b33f-59e8bd8605cc | -13.6233 | -51.8371 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 57893ed8-29c6-397e-8a6f-01dd8ab3b1b0 | -6.6938 | -58.942 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6197d30c-a606-32dd-af37-e4c13e8cac31 | -3.7533 | -59.3231 | 2026-09-02 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c3a4dfb8-cd99-3636-a1f1-38b2b3f20e4c | -3.3688 | -59.3887 | 2026-09-02 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c7cc6463-a20c-36b6-8791-20836790eaf7 | -8.3718 | -62.697 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3fdb64a3-ed4e-3d95-a348-f44e1f7bfc52 | -6.9872 | -59.2582 | 2026-09-02 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| af61e925-8dd7-3dd4-acc1-10782f40a4f2 | -14.2989 | -51.7072 | 2026-09-02 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5e8a28b5-8db4-3053-9967-9a3ede260f3d | -13.681 | -51.8298 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8e2443b6-d1bd-3973-bb98-a777b8625be5 | -3.2178 | -61.2362 | 2026-09-02 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c68d493d-8543-3107-ab86-bbfc41e13d59 | -2.9447 | -60.9002 | 2026-09-02 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| ae620e43-4a41-3721-8a3a-ec842e145788 | -13.6817 | -51.7872 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6e101eb4-fdcd-3e53-8ad2-cc85dcf3e2a7 | -8.8925 | -62.3538 | 2026-09-02 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 172ae237-5973-39f8-be80-af46e7f79081 | -8.5542 | -63.1814 | 2026-09-02 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e2bfa3d3-3369-3d9f-be19-bb6441b12e67 | -7.2007 | -60.6515 | 2026-09-02 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ca7c1dc8-8d52-36ed-b53d-51579eb24905 | -5.5649 | -60.193 | 2026-09-02 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 380c16ef-2a6c-3ebb-89ae-a42256a28593 | -1.5116 | -54.9546 | 2026-09-02 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d8355224-2b03-3b7d-8e57-97c20d8e6914 | -5.565 | -60.1739 | 2026-09-02 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9543a008-a8e8-3cfa-a15f-f5ec601eeeb1 | -13.6813 | -51.8085 | 2026-09-02 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 64819fdd-1041-3cb7-bf1f-a9b34572147e | -10.1538 | -45.6982 | 2026-09-02 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2f29bb47-a1ba-396f-8269-bc2aa247deab | -1.0182 | -53.7189 | 2026-09-02 15:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 692328b3-d847-3668-a878-8aef8794dac9 | -9.8806 | -64.9764 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f3a54553-6f91-31f6-8a14-84353ed4fa4a | -5.975 | -55.7022 | 2026-09-02 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4748dfb3-5022-3b48-8e4c-a2d93cefd1de | -3.3688 | -59.4079 | 2026-09-02 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 60a97587-5916-3540-b01c-753024e838c9 | -10.3769 | -49.9723 | 2026-09-02 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8c457e6f-b437-3493-8ecd-3093d053a088 | -7.3638 | -72.7718 | 2026-09-02 15:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a3f0bad8-55b4-3743-a90c-ae867fc932ed | -5.9451 | -57.6906 | 2026-09-02 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ae72ae44-1aa6-341f-b114-0dd0e14000b6 | -8.3717 | -62.716 | 2026-09-02 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b7a67a07-3c0d-35f1-96c1-57f2cc1dba24 | -3.2361 | -61.2359 | 2026-09-02 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6f057cf6-7249-36f2-914d-160ea55b2198 | -6.1844 | -57.7395 | 2026-09-02 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4d43244d-bd0a-31d6-8ce0-4c3195ac5572 | -14.5758 | -53.5948 | 2026-09-02 15:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a0dfbab5-e030-3e78-bdc7-c6ee957aa2a6 | -8.4296 | -54.7262 | 2026-09-02 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ffa6b216-15a4-3c1e-8349-25218769bd70 | -11.0434 | -49.6851 | 2026-09-02 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7d93f1f3-2162-3ee1-94c1-6562cdfad486 | -5.9635 | -57.6899 | 2026-09-02 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6c704336-5fab-368f-afce-4b12d08c41e7 | -3.1998 | -61.161 | 2026-09-02 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6f41d56c-650c-33bb-ad53-cd6cdc00b88d | -14.2796 | -51.7097 | 2026-09-02 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 99db935d-b325-3f7e-9901-ebcb47fd69b7 | -13.9853 | -58.6919 | 2026-09-02 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 9cf45519-ae1a-391c-acf1-cfba1b90594c | -7.0243 | -59.2181 | 2026-09-02 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d980dc67-5c81-3f4d-ae9a-f8181c445303 | -10.4804 | -64.3313 | 2026-09-02 15:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 68f9aff7-2672-3e3c-af7a-c5e56a5be27f | -8.7628 | -46.4642 | 2026-09-02 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| e7404159-f7d3-38e1-bfbc-301f6d2d3959 | -9.6676 | -47.9429 | 2026-09-02 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3c097016-8014-3c37-b57c-efedf3071097 | -2.9447 | -60.9002 | 2026-09-02 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 57f1b9a6-b355-333d-8edd-127ae3a5ee6a | -6.8019 | -59.4008 | 2026-09-02 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e73e04be-1a39-38a7-8646-e1e06e8ebbc0 | -1.5116 | -54.9546 | 2026-09-02 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9461eb21-2d80-33c5-a291-45845cc358b4 | -12.01 | -60.5345 | 2026-09-02 15:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8721a17f-ad63-37d8-9780-4e55e592f020 | -10.1134 | -45.8621 | 2026-09-02 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0483e0e1-fc97-3d45-ae9e-a106e88cf072 | -5.5833 | -60.1924 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 870980f3-4bcc-3992-a018-b8d63e2ad7bb | -13.681 | -51.8298 | 2026-09-02 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 083d7c53-c660-3af8-807b-5fc338c5835c | -8.8925 | -62.3538 | 2026-09-02 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 173.4 |
| d93b67c0-5edc-3cbf-b781-f1b4b148a57b | -5.2869 | -47.8882 | 2026-09-02 15:50:00 | GOES-19 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 81bbc061-94df-3b5a-82b1-769af86d7c4d | -3.1997 | -61.1988 | 2026-09-02 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 00e4bf99-f808-31b8-ab20-8c54f434b3dd | -9.8434 | -64.9777 | 2026-09-02 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d9cd14aa-10f3-31f5-b21b-db549dc1a337 | -3.6216 | -60.547 | 2026-09-02 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| bf106108-901f-3a46-a3d6-2ad766d019e5 | -3.0347 | -61.4846 | 2026-09-02 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7c6b463d-dcea-3472-8e47-101ce48d167e | -3.3688 | -59.4079 | 2026-09-02 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 19cdef74-3364-3016-85f2-147ee7701749 | -14.2989 | -51.7072 | 2026-09-02 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1fa41a3f-3b32-31d3-a3dc-da358e7f507c | -11.2126 | -46.1066 | 2026-09-02 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a77d689a-c42f-3c13-8040-78f29d9385fb | -3.8446 | -59.3977 | 2026-09-02 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 52b19de6-67ca-3265-859b-cf76f815e5e8 | -5.9451 | -57.6906 | 2026-09-02 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 78b8dc42-efb4-3357-9bdf-d5822d0e037c | -13.9664 | -58.6736 | 2026-09-02 15:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3cb52ce6-5e6f-3d9f-a930-5328cb712bf6 | -11.3579 | -45.4027 | 2026-09-02 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 426.3 |
| f37644c9-552e-32df-9574-88dd6e450047 | -5.5648 | -60.2121 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3628629e-96ee-3593-af47-03b4e2635016 | -6.1844 | -57.7395 | 2026-09-02 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 08f37172-b560-3e93-bb6d-1d4540edbe48 | -11.5479 | -45.4676 | 2026-09-02 15:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 96cde722-9b12-3707-a02a-f1adc4f2376a | -13.6233 | -51.8371 | 2026-09-02 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a265757a-3cda-3b3b-97f3-2c1b40e33418 | -13.5075 | -51.8728 | 2026-09-02 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 03fc0917-0537-39ee-837a-e9fa0cfb8c89 | -1.5805 | -47.7462 | 2026-09-02 15:50:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7f15400b-a6f7-38bf-a4ac-c1959b19188d | -8.4296 | -54.7262 | 2026-09-02 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d08def28-f9cb-3a24-8326-a208d5d0ffb9 | -5.9635 | -57.6899 | 2026-09-02 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2d90aa35-45eb-3124-a89b-26782d438af4 | -5.565 | -60.1739 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b59e8fad-720a-31e9-886b-f3cce1cbb9af | -7.2192 | -60.6507 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 0f95f1ba-6034-3933-b3a7-e14e474e775a | -13.6813 | -51.8085 | 2026-09-02 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f944f63e-69db-313c-b417-3276123706c3 | -1.4761 | -54.2365 | 2026-09-02 15:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 841fdb72-0d18-3200-8d54-80a4bde7807c | -8.5975 | -54.715 | 2026-09-02 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d3eb24bb-efcc-3837-9e6b-42e94efd4606 | -5.9995 | -57.8444 | 2026-09-02 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a693158f-bfc3-3a55-95ea-b117a929f440 | -7.455 | -61.3853 | 2026-09-02 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1bdb0bd2-5cd9-37fb-a79e-ad9a66fe0a18 | -3.4002 | -61.3276 | 2026-09-02 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 076f00e0-54a7-3ea9-8518-9ee56e5e43dc | -1.0182 | -53.7189 | 2026-09-02 15:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5f976bf8-f9b1-39c4-832b-a64c728a090d | -3.3688 | -59.3887 | 2026-09-02 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2a11f39b-b04a-3ae8-ad66-46fbaef9c6ca | -8.3718 | -62.697 | 2026-09-02 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 598d1388-3a93-3c25-953c-d74db749a722 | -7.3302 | -60.589 | 2026-09-02 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f5766d64-9a26-3a88-8dab-ec3c0eae2ca9 | -6.8387 | -59.4186 | 2026-09-02 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 11ba2c94-c377-3469-8c48-325a4a16d582 | -6.6542 | -59.426 | 2026-09-02 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2de01897-016a-33bd-abb2-af22530391ce | -3.7533 | -59.3231 | 2026-09-02 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a721a94f-76c4-3ee2-90a2-ab64103ebc7a | -13.4519 | -57.039 | 2026-09-02 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| ee06d659-305b-3cd0-ae5a-6654c2956985 | -14.5627 | -52.077 | 2026-09-02 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5f9bbc6f-cc3d-3de4-8ecd-f85d0ff26727 | -13.4325 | -57.061 | 2026-09-02 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a93ace8c-da6e-3ec5-ba31-e8aeda1461ed | -7.5668 | -61.2096 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7587a5a4-01e6-3ebc-ba00-8f2903cd8d6a | -3.3871 | -59.3883 | 2026-09-02 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 25d035d9-3af4-334c-9bcd-8220c1ba4728 | -3.8263 | -59.3982 | 2026-09-02 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4fbe6a11-ec2e-3b15-b85c-16c045326299 | -3.218 | -61.1607 | 2026-09-02 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b3d39cf3-cd59-3cc5-9281-299ecc749403 | -6.1426 | -62.5268 | 2026-09-02 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 64a9daed-331b-3352-abf5-3109026ba44c | -2.9326 | -58.3397 | 2026-09-02 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f5d3fefc-18ad-30ef-939a-a50201362007 | -5.5649 | -60.193 | 2026-09-02 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c3ce5b3a-1c02-3eb8-8236-9a364544372f | -13.6817 | -51.7872 | 2026-09-02 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README87.md)
