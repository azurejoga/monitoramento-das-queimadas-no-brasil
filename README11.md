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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 797be49c-0171-3957-ae99-881155f5d81a | -9.18792 | -59.46088 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 99f4091b-1a8a-34a1-9f19-81bd92954e00 | -9.01054 | -65.70695 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c331a401-1754-3b5c-b951-89734514ac2a | -9.01929 | -65.69315 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a5510f00-e43d-3763-b0cf-eb8f0a64b91c | -10.0322 | -59.36244 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74cddb71-22e2-3990-98be-5980b3c16d03 | -9.10115 | -61.4318 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1ff263af-e9f7-36b6-bf34-d7bbe91134b1 | -9.14456 | -60.76148 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd6e8d93-9341-333f-a921-44760f33cac3 | -9.17 | -60.80796 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 80b528ad-9a86-35e3-b823-579f43c1df04 | -8.88417 | -62.45929 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 498d07be-84ad-3d57-912a-9b6d75056713 | -9.16425 | -62.35572 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 70346981-2e47-3cea-9c39-50058d27f91e | -8.12293 | -62.8871 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5822f61-a3ae-34b3-b393-8264f1e042a7 | -7.10462 | -59.22138 | 2025-08-25 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5b66262-4ef0-3d08-b55c-b84779556ba3 | -8.98182 | -65.40206 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 17f806d9-a4ed-3240-93a1-43dba57ba5a9 | -8.90188 | -62.45677 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 46b1668e-ab09-36d7-8410-4cf39edb80fe | -9.80993 | -64.25966 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f75b20b9-1b4f-3d15-bbe6-aa30ef7c705e | -10.41263 | -64.39368 | 2025-08-25 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 1a8ce355-76cd-31e8-b517-42a8577d8d74 | -8.1027 | -62.87163 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2d8373d7-14a3-3925-b745-e136d3ce4c87 | -7.49491 | -63.81892 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80ee947e-f805-3c74-ac95-d5f56c035e72 | -10.28537 | -60.55051 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 20713a22-2743-3d6f-a7dd-8384fc149b1c | -9.12267 | -60.73645 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23672ca2-bdc6-3a3a-8c94-99a7ba355698 | -7.9255 | -63.05569 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 220ab188-fa0a-325d-ac67-67bc08e5c025 | -7.67537 | -67.10531 | 2025-08-25 01:28:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3d0d4d51-9eeb-3646-9f9d-57f366490392 | -9.03447 | -65.72925 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3443eef1-376c-3113-9910-cfc7b1bd9ec9 | -8.11281 | -62.87936 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 602d56c2-f956-3783-964b-6f85698d3f30 | -9.19591 | -59.44899 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 56044faa-193c-3e76-9719-e266949ec36b | -9.47605 | -57.82692 | 2025-08-25 01:28:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 2ca8a123-afc0-3d46-a45c-82ec51b26525 | -8.634 | -62.65012 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 92c13902-da1f-3d82-8c55-8f2797de59df | -9.15756 | -59.51859 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 48cc942e-f497-3307-b8d6-71da49fb915e | -9.47405 | -57.8139 | 2025-08-25 01:28:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2b56c98b-6c57-3041-bfc9-f53dfacad4b9 | -8.87409 | -62.45162 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 06e75e9d-1353-3295-829b-722a32277bf7 | -9.19439 | -59.43854 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 058a73d3-8ff1-3506-8d93-cad2e9441e08 | -9.18072 | -59.60989 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 60a752f4-6057-3ea2-95a4-31cc94a91521 | -7.52221 | -63.81513 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7646e370-838e-39a9-8e68-cb69845f5caf | -8.58721 | -62.63849 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 280.5 |
| e910db48-4845-3ff8-923c-ae82e0d845e5 | -9.02089 | -65.70555 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 700f1367-4ab1-3f4b-98de-daf94a7e5912 | -9.08799 | -65.73497 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e09984cd-dc6e-339e-8958-57d9661b254e | -9.17395 | -60.8356 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 584799cc-3e0b-3218-a486-f041aadddef9 | -9.52556 | -60.52238 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| f13e08ee-89b0-373c-886a-8fcc37ab6840 | -9.39998 | -60.54735 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d9fc8de6-59bd-32ff-97f4-9f9040253ce0 | -9.80853 | -64.24925 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aea14f17-7b9e-354a-89c4-e4016e9c7a3d | -11.6988 | -60.18424 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 092c99dc-0ad8-3848-a302-b2d66a782a45 | -8.9849 | -65.42586 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| accbfa16-a476-3644-9c7a-2cbb3be5f302 | -8.24015 | -61.46558 | 2025-08-25 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18740420-d167-33f7-a81e-d99fe8682225 | -9.00206 | -65.39933 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 2f09c762-ba07-3a18-9d8d-78b90bb293bf | -9.09438 | -65.7277 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b30131fe-ceef-3438-bfd4-5ed1e98163ab | -9.14586 | -60.7707 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e7c19e37-3a4b-3fa4-8f2e-fefeaab037f5 | -7.47185 | -61.31841 | 2025-08-25 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c90b1500-3030-3ab1-b609-f7e3335a639a | -8.98336 | -65.41396 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 182.5 |
| ca903b9f-db37-3224-b8a6-f90321408fef | -9.64682 | -59.64446 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 19e18025-41df-3c7e-8916-05920f46788f | -8.91789 | -60.72197 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7571e12c-63be-3804-bab2-86b999c3af48 | -9.80683 | -61.20675 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 934245aa-0745-3e5f-9faf-a954f077cec9 | -9.05519 | -65.72638 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 77a88983-2a42-3028-9588-07711b047faf | -9.26223 | -59.77427 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b8485f69-b188-3422-bbce-c78246b7345b | -12.15628 | -60.7472 | 2025-08-25 01:28:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5286d949-84b1-3965-8fd8-3b6bb835d30a | -9.2439 | -60.48694 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 66454691-0fa4-3b47-bbed-356a8513b2d6 | -8.87287 | -62.44269 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6c21c15b-0f16-3e2e-a42a-b1d01d8e8e1c | -9.81522 | -64.26328 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| dab90c15-6ca5-33cc-8d0f-5716122e353b | -9.20349 | -59.50104 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9e32fbf0-517a-3442-96f6-1709f817eb25 | -12.59939 | -60.35593 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99ef5edf-e721-3b5f-a8d5-c7e4fc981447 | -8.87532 | -62.46055 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 228.1 |
| 2b0b007e-378f-3f37-911b-317166593a01 | -9.64536 | -59.63457 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 29b59d1c-8bbc-31e5-83ac-0c44548d36a4 | -9.06306 | -60.6408 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d32d85a-c39a-32c2-8fb7-890c59543eb2 | -10.41543 | -64.41528 | 2025-08-25 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 651f88c9-5fe9-3cfc-9c40-4c669c6341ea | -9.81657 | -64.27372 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3e55c0f1-e6b4-30e3-a216-ac6f2c423d50 | -8.92695 | -62.42909 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 24ac8663-c883-31b8-8add-450e200ac138 | -9.21944 | -59.67707 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 34ac6f4c-c3f4-354d-9461-d219e71c6136 | -7.65664 | -63.51801 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| efaf2a40-1e66-310e-80d9-fcd48938dc17 | -7.42935 | -60.62538 | 2025-08-25 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d024da18-772e-38ce-84ac-185c555829d1 | -8.62268 | -62.63346 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd293c54-dac9-3016-bf6c-28ef71341293 | -12.85795 | -60.16687 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b3c1e42e-9b12-37f1-b8e5-8bc6f855b0ad | -8.98993 | -63.63992 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 038c30a4-6398-37be-9294-1996cff7b087 | -9.51653 | -60.52371 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4825c4fc-ce9d-3aa2-ae7b-dac4972f7359 | -7.63198 | -62.73135 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| c8413df1-73c3-33ae-b165-017eeff6fb01 | -9.02074 | -65.38479 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 32c77867-1f31-3ee3-add5-706aa0c45da0 | -9.2065 | -59.52175 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39191421-665d-38b2-8139-e0d7083b470e | -7.55567 | -63.86208 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 044bfaf1-979e-3886-a761-dee91c37245d | -9.06173 | -60.6315 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dcbf308c-7fdf-39bb-8985-4c594fa04af1 | -9.21448 | -59.70895 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 80156d65-d338-3856-a2f3-55762c8ad617 | -8.12047 | -62.86911 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 942fc80f-b3c7-3544-94e4-500e3a5d0e77 | -8.13059 | -62.87685 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6a756f1b-4909-346f-af4f-fc658f69ad82 | -10.00919 | -67.86068 | 2025-08-25 01:28:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c674c048-a401-3fcc-8a69-8e37f7aea50f | -7.64888 | -63.52851 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b932623-250a-32b0-b428-adcc64270ac2 | -9.00051 | -65.38747 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| edb4d260-e246-3a2d-8c51-7ee168246fc8 | -8.58599 | -62.62954 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 357.9 |
| 240c8989-90bb-3677-a9b7-2b615564fe28 | -9.00908 | -65.37432 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 24a43bed-d0f6-3086-adae-8c84c8529471 | -10.61396 | -55.04603 | 2025-08-25 01:28:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0abd4e3f-3f20-367e-adc9-a2e216d72986 | -11.69746 | -60.1749 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 90a6b49c-3dbb-316d-8028-834cf8daea2d | -8.23637 | -61.4387 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3583f71-3bda-3356-8690-60bba2231eba | -7.5725 | -63.44172 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 58da936b-d499-3545-b3a4-79d1e81820ab | -9.82473 | -64.26198 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d5f109da-5286-3913-94a0-863f38355d39 | -9.65472 | -59.63302 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 54e3f1ac-3b8b-3b01-afb8-0b71645c16b3 | -10.10123 | -57.76542 | 2025-08-25 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6107c08a-d15e-3c45-8183-42d9fc6af0d9 | -9.2049 | -60.92461 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b0ff9cdb-827d-3577-b199-51f266a3d2d2 | -9.1784 | -59.46231 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 4651eb47-2b04-378e-9d76-258caffdaae1 | -8.10393 | -62.88062 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ed7a8e3a-63a8-38b7-b322-42673e8fd42b | -8.51462 | -63.87337 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 22809aeb-bc97-3d42-ab59-0186e6fa6f64 | -8.89303 | -62.45803 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6920c629-2b00-3f07-9655-9be52ce112d8 | -9.2059 | -60.80264 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb5f7d1c-30bb-38aa-99d6-11aaaaa9f7fe | -9.07737 | -66.06287 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 442edf7f-c513-33dc-9614-54193c6bace7 | -8.22873 | -61.38467 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 4f341383-8d60-3d79-88a6-d20aefa35e31 | -7.36144 | -57.63748 | 2025-08-25 01:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |


[Clique aqui para ver as próximas entradas](README12.md)
