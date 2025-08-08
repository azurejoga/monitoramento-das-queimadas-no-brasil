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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259b2c0e-acc2-37c3-8127-8ad7efd776d2 | -7.8915 | -45.3575 | 2025-08-08 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a70d78ee-44fe-3610-b8f3-8bab087c9482 | -10.6247 | -44.767 | 2025-08-08 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 7643f6e5-a331-3ea3-85d9-091f8950fd5c | -7.0616 | -59.1586 | 2025-08-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d707d0df-1e7a-3a00-8124-4ef081feed1e | -7.8918 | -45.3348 | 2025-08-08 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 27d1d388-20e9-33e6-b047-24f6232696b6 | -10.6438 | -44.7645 | 2025-08-08 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7d6d5116-c670-3900-b0a3-2c45ada4df5e | -13.035 | -56.8562 | 2025-08-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 3db6c0c1-6220-366e-9cf6-d014bfe30520 | -8.9399 | -60.7481 | 2025-08-08 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 35b54e74-6cc3-3eaf-b8ac-d8a45ac1ea57 | -7.043 | -59.1787 | 2025-08-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| bb5090dc-1f3b-3fd1-8da5-ca0f43cc6c75 | -13.054 | -56.8545 | 2025-08-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6ed454ec-f69d-320e-9130-5628a97d9a7a | -8.5211 | -43.3063 | 2025-08-08 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e51697f7-38d5-3f12-9609-2abf09ae8cf1 | -10.625 | -44.7439 | 2025-08-08 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4a7e4d04-ba36-3969-9d75-9197ee7cbeae | -22.81446 | -55.59333 | 2025-08-08 01:41:00 | TERRA_M-M | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| 730cffd9-40b5-3dc9-8de5-ce809e94e49d | -13.03893 | -56.88874 | 2025-08-08 01:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 09bc278b-cd06-301d-a763-0a76ad355662 | -13.03408 | -56.86076 | 2025-08-08 01:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 967a6788-847f-3373-b0de-1ef95ecbdf6c | -13.04883 | -56.85821 | 2025-08-08 01:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 5589d081-83c6-30e7-a009-436f582525b8 | -8.89893 | -60.54519 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 30e5ebf0-9ba8-361f-992e-5cad43accb6a | -9.94323 | -60.51415 | 2025-08-08 01:47:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e7063aa3-1967-39b8-bc86-fe554ebaeef7 | -8.90744 | -62.42509 | 2025-08-08 01:47:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 92e335fd-0cbe-35df-8e4b-75c35fd2cab2 | -8.92806 | -60.7288 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 42d26579-2556-313e-b112-d52c8b85de00 | -9.46977 | -57.85856 | 2025-08-08 01:47:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 80120df1-98ba-3af2-a4f1-1d44cf1fc5f6 | -8.91891 | -60.74695 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 00dc0518-2f30-3a80-b2dd-379308be594d | -9.71261 | -62.40802 | 2025-08-08 01:47:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ede323f1-c168-33fe-a845-924efcb92500 | -8.92129 | -60.73619 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e25f3353-b8ed-3cb8-afac-6dd6d7bd4711 | -9.64458 | -62.91389 | 2025-08-08 01:47:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 56b08c13-936a-3aaf-b287-1746f2605426 | -8.92376 | -60.75253 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4aed82a0-d7c8-317f-9d43-cc74e263d4d1 | -9.92631 | -60.48321 | 2025-08-08 01:47:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 09b55115-e7ec-3e80-9823-c095f05a70de | -8.90559 | -62.43219 | 2025-08-08 01:47:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1501bd64-32d2-3502-ad66-c1c89b65871b | -8.90924 | -62.43747 | 2025-08-08 01:47:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 43736c3f-1ad8-3c13-a323-bb092bf97008 | -8.91086 | -60.5433 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 0e54add8-cdae-3983-a147-65924b04d405 | -8.93065 | -60.7451 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 545f286f-cdc5-3f6b-8c4f-c9b9209c1876 | -8.91353 | -60.56021 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 49de2aa1-12ed-30a9-9430-6ed195949e1c | -9.94065 | -60.49769 | 2025-08-08 01:47:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5d7ca763-d79e-3dca-a627-6753ad245218 | -9.7087 | -61.30231 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| f762bea1-7778-327f-be09-13c251e05fd2 | -8.90538 | -60.55053 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 965a2d82-03d6-3bed-ace1-282bd55dffd0 | -9.70648 | -61.28779 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2af842d9-b646-31b9-90db-7154da6a3bc4 | -8.92151 | -60.76328 | 2025-08-08 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 675f038f-1aef-3efc-8e8d-3316c2902e94 | -12.4974 | -54.3048 | 2025-08-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| fb731824-213e-3326-87d8-b54cc755ebb7 | -10.625 | -44.7439 | 2025-08-08 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 22397179-7dbf-380b-b3ca-8611efc31e31 | -7.0429 | -59.198 | 2025-08-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 1dcb857f-f96d-3628-b73f-89c0fa401123 | -10.4784 | -44.3931 | 2025-08-08 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0868837a-86da-3ab5-9566-a7793933601c | -12.4784 | -54.3067 | 2025-08-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e43fd492-c286-39ac-8e77-ef60c827b909 | -10.4787 | -44.3698 | 2025-08-08 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 898449f9-a342-31af-b397-7ddda74c0ce5 | -8.5211 | -43.3063 | 2025-08-08 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c85a901f-2b22-313d-8c3a-2cbad32750b3 | -8.9213 | -60.7489 | 2025-08-08 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| ae654454-4dd3-38db-9991-7674735215dc | -18.688 | -52.7027 | 2025-08-08 01:50:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 512c4fde-39ca-3b95-83e2-06fdcae1545c | -12.4781 | -54.3273 | 2025-08-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 48ea7534-89ca-33a8-bc22-a87930949ea6 | -7.0615 | -59.1779 | 2025-08-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 38c7b370-4431-36bb-821d-227691002b52 | -10.6438 | -44.7645 | 2025-08-08 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ab8cada0-486b-3089-b9d0-3240c5f1ba77 | -7.043 | -59.1787 | 2025-08-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 41b1d3ec-573d-3cba-9380-a7d7df9a8d34 | -7.0616 | -59.1586 | 2025-08-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d9dff76e-f444-35ac-b357-7fba291878da | -13.035 | -56.8562 | 2025-08-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d632a441-8af1-3600-b114-058467e37337 | -7.0614 | -59.1972 | 2025-08-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9c4bfaa5-1db2-3e63-9ec8-78126d2dfdb5 | -10.6247 | -44.767 | 2025-08-08 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 793c9d9a-e6bb-3907-9501-1e323e976f38 | -12.4971 | -54.3254 | 2025-08-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1c190433-bf97-3016-8aa6-be02b0abeeb5 | -13.035 | -56.8562 | 2025-08-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 31a6f4af-379e-3818-87d6-f96d1c131f8d | -10.625 | -44.7439 | 2025-08-08 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4a78d621-5de4-34ab-ae40-802353d05bbb | -7.0616 | -59.1586 | 2025-08-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 08f86e11-d825-3254-a30e-9029382299ef | -12.4971 | -54.3254 | 2025-08-08 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 233.4 |
| e09c90da-0345-3729-99a2-d2c9d18f8c51 | -18.688 | -52.7027 | 2025-08-08 02:00:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c7ce0dc8-8c72-3195-9246-ae5157720670 | -12.4974 | -54.3048 | 2025-08-08 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 207.4 |
| c4bfe242-1e33-3d7b-bebe-ff815c304040 | -12.4784 | -54.3067 | 2025-08-08 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 5290c18b-f58f-3424-903b-af96d581b45e | -21.0227 | -48.9218 | 2025-08-08 02:00:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| f130f808-2256-3be6-b736-9fa13a1d87e0 | -10.6247 | -44.767 | 2025-08-08 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 5017f143-bfd3-3edc-bfc1-b8e4dbd46725 | -21.0234 | -48.8986 | 2025-08-08 02:00:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 9b9df428-d311-3890-9223-5af0373ffeb0 | -7.0615 | -59.1779 | 2025-08-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6650d8c4-8ada-3a1a-9b39-56ec6879aa7c | -8.5211 | -43.3063 | 2025-08-08 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 9d3a2dc2-574d-39f3-80f6-9b321275ba97 | -7.043 | -59.1787 | 2025-08-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0f36c113-3a29-386f-bf1b-d1aa63ebd5b9 | -7.0429 | -59.198 | 2025-08-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 15655f08-7bdf-30d0-9d0a-cafd6955440c | -12.4781 | -54.3273 | 2025-08-08 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 219.5 |
| 4cfdc191-96e4-3960-b624-7ba3b70c8dc0 | -8.9213 | -60.7489 | 2025-08-08 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ad886657-250c-3999-ae2a-23610b11da71 | -12.4778 | -54.3479 | 2025-08-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 267a537a-6eb4-30ed-8518-f56bb0a92e35 | -3.2321 | -46.7836 | 2025-08-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 77616a59-06b0-3495-8177-70797f9afbbf | -25.2955 | -49.4955 | 2025-08-08 02:10:00 | GOES-19 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| c3a4a337-2d1c-316b-939e-70477ba559cb | -25.2739 | -49.5013 | 2025-08-08 02:10:00 | GOES-19 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| 9246d202-9755-3d53-93a5-aacdb9c792da | -12.4974 | -54.3048 | 2025-08-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 69dece9c-4ea0-3957-bef1-e3e3a86f47e8 | -8.9213 | -60.7489 | 2025-08-08 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| cd955f5a-5944-3d4f-83a3-da522e4c138b | -18.6875 | -52.7244 | 2025-08-08 02:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7e0b230b-e7dd-3366-b430-4975eba0397d | -12.4781 | -54.3273 | 2025-08-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 594.7 |
| 079190ca-0ae1-3ebd-ba83-fb46902fc16d | -10.6247 | -44.767 | 2025-08-08 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d56b6470-c236-3ba0-a633-ddd01820a015 | -18.688 | -52.7027 | 2025-08-08 02:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a4c11add-d834-3178-9cbc-46a26722b345 | -12.4784 | -54.3067 | 2025-08-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 192.2 |
| eadf8f1f-4f2c-3df6-8b4e-4832f1c48c50 | -12.4971 | -54.3254 | 2025-08-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 356.7 |
| d0ee6070-cabe-318c-b87b-38704d11689d | -8.9213 | -60.7489 | 2025-08-08 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dc57a295-56c3-3f8f-a6c6-d4be1f189aff | -10.625 | -44.7439 | 2025-08-08 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d983c396-1192-39ec-9741-9c0f874491ec | -3.2321 | -46.7836 | 2025-08-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2a2f2392-6b99-3470-b0ce-ddf349d462f7 | -25.2739 | -49.5013 | 2025-08-08 02:20:00 | GOES-19 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| fda6372f-ab72-3edc-9a57-1f6cf033088a | -10.6247 | -44.767 | 2025-08-08 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 04a3dd2a-d762-33ff-a89a-f9e89f4ff378 | -10.6438 | -44.7645 | 2025-08-08 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 24126a74-8e39-3a7d-b033-335ae302dc54 | -18.688 | -52.7027 | 2025-08-08 02:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9d93b499-f05d-336a-87f8-fe15bc43db41 | -8.9399 | -60.7481 | 2025-08-08 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e4d2ef04-d7c0-3920-8f94-2fe1fba228b0 | -18.6875 | -52.7244 | 2025-08-08 02:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| e994aa58-1dcc-378c-bd0f-8410b8a49060 | -10.6247 | -44.767 | 2025-08-08 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 086ef50c-2fc6-300d-b404-6d4addbf0e41 | -10.6438 | -44.7645 | 2025-08-08 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 26928084-17a0-382f-b3fb-cf5cd857773c | -8.9213 | -60.7489 | 2025-08-08 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 513ea2ad-e867-3ed8-bb21-47d860928dc8 | -3.2321 | -46.7836 | 2025-08-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b4e0efc1-9c1c-378d-bad0-3cba314ef72b | -18.6875 | -52.7244 | 2025-08-08 02:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1ed7c212-70e6-37b1-800a-0bb44942b92d | -8.9213 | -60.7489 | 2025-08-08 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7d3349e3-3d6c-35f1-9c9a-ff4fdd4c791e | -10.6247 | -44.767 | 2025-08-08 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5504cc67-75f2-35c7-8e5c-5ba545946e5e | -8.9042 | -60.5385 | 2025-08-08 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 581e385d-8796-37ce-8d25-5bb1e65d049a | -10.6247 | -44.767 | 2025-08-08 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |


[Clique aqui para ver as próximas entradas](README6.md)
