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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec6bb0f-b7f7-3490-8893-31095d606652 | -8.67284 | -62.43356 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff8e7a3-663b-3920-9630-970d0e6d3cc3 | -10.37397 | -57.83764 | 2025-08-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 106c4da4-5204-33e8-a217-a12264c3453a | -8.65702 | -63.29596 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f071a05-04a5-3521-9f16-c4bd7c43243a | -9.45165 | -62.32777 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 09d25814-5040-325f-87c4-3297c66d14bb | -8.44157 | -70.1375 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e38775e2-888e-3acf-b935-fbaab6591d76 | -9.44024 | -62.33547 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fba60186-f43a-35dd-98f3-5459374a5d2d | -11.399 | -63.25883 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1469f8e-3b21-3ca6-90be-d51c49f99e51 | -8.6676 | -62.43293 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f5fa516-5db5-3143-9a01-e205a3b9e705 | -8.24968 | -61.45358 | 2025-08-30 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e61662b5-d98a-37bc-b8b4-afe2d393e9bf | -9.45795 | -60.57387 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbb6bbb4-02a5-3506-9883-e8115b6612bf | -9.11111 | -65.76482 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d22ec7a8-6649-373a-a494-7e4bdbd9e6d6 | -8.65576 | -62.44606 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d146e7f1-6684-3985-a3fc-31f3e4e2264d | -8.88416 | -60.72794 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da4229d4-4665-355c-bf78-7ac848e012ec | -9.15744 | -65.78627 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c599a1-c032-3bdd-b06f-4852bb2bbc2e | -9.44642 | -60.57247 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 289c1687-0366-38cd-a486-ca03575eace3 | -9.45901 | -60.56582 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad6b975f-cd41-37af-9029-30921cfbd8bc | -9.45167 | -62.36811 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eaacbfb-f68c-3159-a6fd-d022c3d542f4 | -9.89563 | -67.01845 | 2025-08-30 06:01:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90126a04-ee6d-3d84-96f4-97615c4f3753 | -9.44694 | -62.32384 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 916be20a-8aa5-300d-9af2-7510931a388b | -10.24064 | -68.09096 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c10db8-8f36-3c3f-92d0-7c4dabe1b277 | -9.33198 | -68.21512 | 2025-08-30 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70f30109-80a7-3b72-bc80-a6bb09e299e2 | -9.4422 | -60.55981 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 74286a91-3bb9-333f-9fc9-106a572ea9f8 | -8.8832 | -60.73565 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a21866d-e066-32fa-bd99-f0fbd6dd0374 | -9.66451 | -65.04611 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd30b6f1-6e5a-340f-8c13-6df78f41a59d | -8.73516 | -70.93511 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2cea66-c6d7-3b4a-a8b8-a666a3a4b34f | -8.59466 | -60.57753 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef00208a-b08f-3dbc-b33c-6799a80193cf | -8.92224 | -64.24156 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63f0d287-a89b-3b57-8e52-da86c12b47b4 | -9.44842 | -60.56415 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c450c7f-8f9f-3e94-b573-b0bb29cb5782 | -9.4493 | -62.34607 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db03f3d5-8bee-32d2-ad0d-a5a82bedbc3b | -9.46135 | -65.42532 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1b1e11f-1c3c-32e2-8484-0f2e5ee422c8 | -8.04386 | -70.09234 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4030ce21-8612-3f3d-98fc-69a7a4f932ff | -9.44614 | -60.53485 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 918d10e5-eba7-3a86-b434-7ed3ec1e981d | -10.3809 | -57.83815 | 2025-08-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef5214e4-d931-37d6-a803-9f2ab9cc49f9 | -8.63976 | -67.25763 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4d0f538-e7db-34a1-bd70-d2fc7b1f7a9c | -8.91369 | -70.60058 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e030494-44e5-353f-a7d4-7faf81a1ee53 | -9.27215 | -65.92467 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49d18034-bfb3-3e92-b95e-d695c8d0e8c3 | -9.44695 | -62.36433 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6d80dd9-958c-38b4-a3e0-c258c8031f71 | -8.91039 | -70.60006 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d756fa09-fc6a-3ae1-8d59-eec3082b947a | -8.92348 | -64.23264 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eb97cb7-b6d9-37aa-8ebc-2fd59dcb6f96 | -9.43665 | -62.34121 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ce8b11c9-4814-3afb-9ba0-541c417cfe0c | -10.18362 | -69.00862 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c00b3974-d23d-3bab-bfe0-e906dca6129a | -8.66781 | -62.4329 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 999a751b-a547-3058-88c1-58b883abdd5b | -9.44326 | -60.5517 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c77591e4-0143-3715-8b94-1c56ac8ca6b3 | -8.59782 | -60.57994 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4145f436-b138-36cd-a329-f966d7c757a5 | -7.99658 | -70.28774 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb0ad548-7a48-3a9d-8727-52ef0f0c9b6c | -8.18294 | -61.38135 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fe6dc92-1e88-3867-9902-778b9799e931 | -9.45061 | -60.54026 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 42f043fc-0c1a-35f1-96ac-20182c3a79f8 | -7.54046 | -63.83939 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b16f6ec7-a204-373d-afdf-cebd8317aea8 | -7.99712 | -70.28427 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56437d2-80e5-35fd-9b73-62d80d630550 | -8.63071 | -67.243 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54a97d21-d490-38fd-9a77-e527942bf67a | -9.17403 | -59.58229 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77f68af3-a164-35e0-bcc8-49c97b6a83f5 | -8.88367 | -60.73182 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad7b8f89-cf8e-3000-ad3e-8431a2e1745c | -8.85172 | -70.6263 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4e57c66-a23e-345c-95bf-6f85c1faaa79 | -9.03286 | -68.33326 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30b5c890-9884-3609-a610-ccb7baecd4da | -8.67787 | -62.43422 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3882db2b-6d3c-37b8-b15a-af317ad38dba | -8.52163 | -70.25717 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ae3382-2b3a-39b7-82cf-e9d6151ecdf8 | -9.11163 | -65.79037 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2e0010c-364e-3bc4-8912-c89e661918b8 | -8.25502 | -61.45433 | 2025-08-30 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4b25e80-60ce-3b14-be66-182e73f24ca5 | -6.56534 | -69.95548 | 2025-08-30 06:01:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a28aee50-4b23-3a6c-801e-5cf809cb4158 | -4.99364 | -67.00332 | 2025-08-30 06:01:00 | NOAA-21 | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5774a9-c51b-3836-aef9-c50d58a43b4e | -10.36522 | -59.21202 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0594d271-d828-36af-8816-881a618dec34 | -9.44341 | -62.3514 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcfadbad-ce04-347f-8e25-963f76edd00a | -9.44578 | -62.37345 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee190f6b-a261-31f0-a241-ac0601b755fd | -8.90631 | -62.10413 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9cc046fb-176c-3f3d-8280-58a5d23b2460 | -11.35721 | -63.25719 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 955d9d58-1145-3e57-a7e0-1b5e3d3a9276 | -8.66457 | -70.03618 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082ac1eb-5581-3390-b9ec-1ed0914ccb27 | -9.1146 | -65.73994 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8b8e30a-e4b9-301d-be00-e4251555fbdb | -7.56997 | -63.85748 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 894e46ab-ef3d-3315-a463-6a6c67fcac32 | -8.85027 | -64.14754 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8fdc74d-b497-3d4b-9591-0f4bcd2e2313 | -9.44464 | -60.54712 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1e80f2a8-7c56-32cd-bc65-10fd4839e210 | -8.29513 | -61.42403 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4bf25c3-5f25-3e14-af30-8314eda0a996 | -9.17836 | -65.55315 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8c1a7ac-7f42-3f7f-9a16-bca1672dd355 | -9.15795 | -65.78271 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9865f491-d845-30d0-b6e3-2dc7ec585670 | -8.71798 | -68.68762 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dde8731-0ac2-3c6a-87e0-f4ed2f19f511 | -9.1101 | -65.77203 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc36ffd2-b8d2-3979-b03e-5f709e6a7f3f | -9.45322 | -60.56521 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 893887a4-3832-3384-b258-7a2d4723e2c0 | -9.4374 | -60.55843 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6b9d083e-d7f5-3a9a-9727-9df891cd1ff6 | -9.73157 | -64.91057 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de7187b6-1b98-3923-b537-1bb537e64e80 | -8.56265 | -63.01539 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aab23ede-9bf8-3b62-a46d-d0b3a8d10337 | -9.45046 | -62.33708 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3e612189-6941-3aad-a4c1-28fba5146c7c | -9.44848 | -60.55661 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5be6d4f3-9ae2-33c6-934d-70763534b415 | -9.44891 | -62.34913 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| feb06d93-3621-31ce-bc7b-3d7473f5ba0b | -10.07428 | -58.36471 | 2025-08-30 06:01:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15a776ee-6625-3de0-8329-494b36534f9e | -9.54389 | -65.70145 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2a40c4-6ad2-3025-8b28-d42e82edcbbf | -8.90714 | -62.09793 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8293b84-33aa-339c-a274-861f86c61daf | -8.67244 | -62.43647 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef09eacc-e92b-3436-bf2d-62f5375d80ce | -10.55986 | -69.2804 | 2025-08-30 06:01:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70d1379f-e847-3eb7-9fc1-b168c148500a | -8.65083 | -69.57137 | 2025-08-30 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4de1c5d3-cb46-3254-ac4d-ff60492443c1 | -8.55638 | -63.0253 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 506cf09a-4371-362d-b0bf-3f2e470243d1 | -9.77849 | -64.24918 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dbcce53-58d4-3e3f-8018-267f495aba3a | -9.17783 | -65.55684 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d7620ef-11b3-3f9c-a2ed-43c9f9b58009 | -8.88689 | -60.7267 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3b986fd-26ab-3717-add2-95b986832d53 | -9.46071 | -62.33842 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4abb0ce5-9b3c-3a38-abc5-c66638fb071f | -9.43624 | -62.34419 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8b87f37-9d38-3860-8c5e-7c723524e8a8 | -6.56865 | -69.95599 | 2025-08-30 06:01:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| affa92e0-a8f4-3c36-8a43-c2b7739ba687 | -7.86853 | -69.95084 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff6d637-f4d5-371a-a731-45bdc3f421fa | -7.90373 | -63.00897 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cebdb5be-0886-3821-9e2e-879a67812e82 | -9.4519 | -60.53569 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11eab855-87da-3236-89dc-7a693f2c86ee | -9.13325 | -65.81169 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63637b62-35a3-3d77-927c-c79775b8967e | -9.44383 | -62.32669 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README82.md)
