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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08de78a2-23ab-3345-9011-1766c9711fa0 | -9.9919 | -36.0871 | 2024-10-03 02:36:01 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 93841037-14f9-3bf0-b3fc-8b083edd96a0 | -9.9924 | -36.0599 | 2024-10-03 02:36:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 826cc514-971b-3b44-8f77-27ab7f223a06 | -9.494 | -68.4895 | 2024-10-03 02:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 19b5819e-8788-3ae8-a56b-e5d06f71dfa6 | -10.6505 | -53.6994 | 2024-10-03 02:36:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5e55bb72-4cee-3c87-ae19-18ff2d866602 | -10.8942 | -63.8971 | 2024-10-03 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 39d1d0a5-1ec6-311f-8f5e-89fb181b57dd | -11.2565 | -60.6019 | 2024-10-03 02:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e450a435-d2f3-3755-99d6-f462f35fe72c | -11.2566 | -60.5825 | 2024-10-03 02:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7880cebd-72cc-390f-b1cd-9d26f25dda98 | -11.6742 | -65.0172 | 2024-10-03 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 68ee3d81-86af-311e-925f-9b8703edd06b | -11.6931 | -64.9974 | 2024-10-03 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 060edb71-d4e7-3b44-8fa5-36b2ca606033 | -11.6932 | -64.9785 | 2024-10-03 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c7469cd2-6c87-301a-a2db-5c0938748e42 | -12.404 | -62.9817 | 2024-10-03 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| b2d88e12-9598-37bc-9a90-d4e45124ed0e | -12.3849 | -63.002 | 2024-10-03 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 78312d15-faac-3cde-bb2b-b470a641833b | -12.4227 | -62.9999 | 2024-10-03 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 99af9fec-cb81-370d-b8ed-1210e56af4f2 | -12.4038 | -63.0009 | 2024-10-03 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 15fc64c0-1bcd-3836-8517-074af1282d8c | -12.6484 | -63.1214 | 2024-10-03 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| db6b32d7-5d97-31c4-82ca-e921fa4f0986 | -12.8999 | -62.4527 | 2024-10-03 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 77d73f51-b99b-3400-a092-c83f3d84b239 | -12.8998 | -62.472 | 2024-10-03 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 141.2 |
| b3fb6243-2f2e-3cbf-9cfe-2f2af48fa4d4 | -12.8996 | -62.4913 | 2024-10-03 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 119.7 |
| f4008648-a678-35be-bd89-3705a805a983 | -12.881 | -62.4538 | 2024-10-03 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d9929686-3166-3424-bbed-d34655e60025 | -12.8808 | -62.4731 | 2024-10-03 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 587d7d14-de0e-3239-bd12-0995e34a9b12 | -12.9741 | -62.6409 | 2024-10-03 02:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 526d3529-e4bf-308b-b966-54a164b9aee0 | -12.9167 | -62.7022 | 2024-10-03 02:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6d79881c-9e54-3a60-a874-43a5896d7b87 | -13.5562 | -51.2489 | 2024-10-03 02:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3b0c00a4-51f7-393e-9500-ca6028d4f07c | -13.5195 | -51.1467 | 2024-10-03 02:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 28e2da52-664b-3d33-be58-1c3f00b765cc | -16.7802 | -57.749 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 11e6bcb9-ad99-3a33-be51-f1ae9710c3ba | -16.7793 | -57.8102 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 8282cee3-ea1e-3086-ae4f-8cae0232cfcd | -16.779 | -57.8306 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 0a6ea5d5-484c-3601-a68d-b4cf7db7bb6d | -16.7606 | -57.7512 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| d2e5a787-95e8-3378-a6d7-fa9fede43ccc | -16.7597 | -57.8124 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 014dd53b-2239-31e4-850a-a674f16c6a4e | -16.7594 | -57.8328 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 25849d9e-90ea-30fe-a7e5-0eb3cd130fa3 | -16.6868 | -57.4741 | 2024-10-03 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 5c13eedb-d32b-39a8-8c6c-294eaad70b67 | -16.9179 | -57.6926 | 2024-10-03 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 07c1c987-b7ce-3b15-bdb8-91899ea39e70 | -16.9176 | -57.7131 | 2024-10-03 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| d5848c35-72d1-318b-950f-bb9f1ad9c990 | -16.8983 | -57.6949 | 2024-10-03 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| f8ee55c6-d8fd-34a7-8b86-a540d80106e5 | -16.7985 | -57.8284 | 2024-10-03 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 87559f20-c003-342b-873c-085aa7d9861b | -17.0692 | -56.7939 | 2024-10-03 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 7b380132-7992-3903-aac0-e87c2d579d25 | -18.8927 | -41.2248 | 2024-10-03 02:36:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 87d37efb-952a-3147-b64d-2774045f2d2f | -19.0344 | -43.1944 | 2024-10-03 02:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| b5ad0717-1cf6-3aaf-b314-cfc690ebd98d | -19.9009 | -42.1074 | 2024-10-03 02:36:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| 2611b6ce-4480-3115-89dd-c2184d1d8c54 | -20.6352 | -46.7497 | 2024-10-03 02:37:00 | GOES-16 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0cb1f460-cee5-3008-b563-33eccb155d12 | -21.3675 | -47.6311 | 2024-10-03 02:37:03 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 639001d4-9fb5-3cda-8362-99772c84e3e1 | -21.3875 | -47.6497 | 2024-10-03 02:37:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| fc87de08-1ce9-3ccb-9068-de9b5687e8b1 | -21.3882 | -47.6261 | 2024-10-03 02:37:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d5dcf488-584f-398c-9f0c-e9688034c1de | -11.6823 | -64.977501 | 2024-10-03 02:45:05 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8c60901-0734-3460-b183-8004c0ec35f7 | -11.6727 | -64.980202 | 2024-10-03 02:45:05 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2b4b45f-980e-39c5-a5eb-0c4d81ec6d76 | -11.6811 | -65.010597 | 2024-10-03 02:45:05 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25bf7d61-122f-32c8-8410-34e5420f3144 | -4.0949 | -48.4894 | 2024-10-03 02:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 28b525ff-05fb-3433-b1fc-90f727183d0d | -4.095 | -48.4679 | 2024-10-03 02:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fdfc97a6-e0a5-3e89-b32a-be1c3e3f6529 | -4.4657 | -42.8877 | 2024-10-03 02:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f130f7dc-bc7b-3118-9c09-3a222e4b12dc | -4.4844 | -42.8866 | 2024-10-03 02:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 67eceec0-7f44-35b3-90dc-142ad786cbff | -4.4845 | -42.8631 | 2024-10-03 02:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 678a7dc2-4a11-3de6-9123-fc968c9e9fcf | -4.5031 | -42.8854 | 2024-10-03 02:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c7d9007b-a6b4-32dc-b6c3-bfa6f9c388cf | -4.5373 | -43.3273 | 2024-10-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5a25c8e3-1a62-3374-8460-b15db8957ce0 | -4.5375 | -43.304 | 2024-10-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| af480ba5-ee00-3799-847e-3ab766b7c245 | -4.58 | -48.0132 | 2024-10-03 02:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0e4043ab-b634-323b-8747-917f10485010 | -4.9264 | -43.79 | 2024-10-03 02:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ac35aaa2-b51b-38e3-8310-a779d8ccec04 | -4.9265 | -43.7669 | 2024-10-03 02:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e27ef486-676d-3555-a2df-bcfe4fc69af1 | -4.9451 | -43.7888 | 2024-10-03 02:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 323a6661-ad2b-3a1e-a14e-9359ebb2ccde | -10.5003 | -68.660103 | 2024-10-03 02:45:40 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2a923548-3eda-3731-8715-f47a6a0a2356 | -10.5121 | -69.227997 | 2024-10-03 02:45:42 | METOP-C | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3d768b7e-7019-32cd-bab0-61b4bfe007fe | -9.8963 | -67.3293 | 2024-10-03 02:45:44 | METOP-C | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 94841e59-03b0-3af5-9598-6ec09dc40222 | -6.8777 | -59.0504 | 2024-10-03 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| fa6d7193-199c-3fa5-8086-b10278b4ee4e | -9.8866 | -67.331802 | 2024-10-03 02:45:45 | METOP-C | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ce4ace1a-6c2c-35af-a109-79a6e68ed09d | -9.6254 | -67.4739 | 2024-10-03 02:45:49 | METOP-C | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce3a877-9256-3719-8e79-f030ba262716 | -9.7377 | -68.421898 | 2024-10-03 02:45:52 | METOP-C | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| de101c29-c2b5-3ba1-a982-9eaf1796fee4 | -9.4186 | -67.233902 | 2024-10-03 02:45:52 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56071624-feb8-3393-b132-de61428c75c7 | -8.8506 | -45.5086 | 2024-10-03 02:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| dbf26370-f9ba-3d4a-b169-8418665b9eab | -8.8695 | -45.5066 | 2024-10-03 02:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7fa2acc6-3f02-31d1-a28f-426c2406f567 | -9.4964 | -68.484901 | 2024-10-03 02:45:56 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d82759b2-0b73-3131-91b1-6981040670f5 | -9.5014 | -68.504204 | 2024-10-03 02:45:56 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0b16ba83-7a6b-3e87-886d-8cb3b4e06e11 | -9.4868 | -68.487503 | 2024-10-03 02:45:56 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4eab505b-1c18-3da6-8927-1ecab89059b2 | -9.4917 | -68.506699 | 2024-10-03 02:45:56 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 56284aeb-15c2-3eb3-9512-a4fa2b2133f7 | -8.8926 | -62.3348 | 2024-10-03 02:45:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 52114d58-79df-37f1-98a5-75a2531207a1 | -9.3835 | -68.326599 | 2024-10-03 02:45:57 | METOP-C | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd4e8c4-d7a4-371c-aa46-8381723bd878 | -9.3739 | -68.329102 | 2024-10-03 02:45:57 | METOP-C | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7892d19e-e221-3c37-b4e0-14ada0940f50 | -8.9791 | -67.4099 | 2024-10-03 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b8758c2f-1d5b-3993-948c-0808c74824b8 | -8.9976 | -67.4094 | 2024-10-03 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 55df92a2-0f29-37d9-838b-b326d5f79ee6 | -9.0149 | -67.7423 | 2024-10-03 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2251229d-36ff-32e9-a695-721477fb111f | -9.0515 | -67.871 | 2024-10-03 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7f0de3f0-d69b-36af-b0c8-44310708d98b | -9.1566 | -61.6758 | 2024-10-03 02:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 30dd1e2c-5fe9-3b38-9e14-acce6ec16188 | -9.0918 | -67.518204 | 2024-10-03 02:45:58 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b51f62ee-efb8-3726-86d5-20a4faa91392 | -8.9884 | -67.397697 | 2024-10-03 02:45:59 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e108cf26-681e-323f-a161-a408e65d599c | -9.4865 | -62.4039 | 2024-10-03 02:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9035cd3b-a649-3698-be6f-6f09cad3fb84 | -9.4866 | -62.3849 | 2024-10-03 02:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1e814ed5-951b-3374-b820-71febd6f3cb8 | -8.9788 | -67.4002 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2497e786-6064-361c-8272-6b9d91e96657 | -8.9849 | -67.4235 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76f2d73b-d376-3773-ad7f-3945a7613e2b | -9.0133 | -67.730598 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a65caab8-f756-326f-a0ef-ac820ce95b27 | -9.019 | -67.752701 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d32f4b5-4c16-32ba-a533-2ee1b37e57d5 | -9.0473 | -67.861801 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f56db6a-cfd4-3861-b060-d6de9b15c350 | -9.0529 | -67.883301 | 2024-10-03 02:46:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99079141-6fd1-35e7-91d5-0a3814d5e1ce | -9.0037 | -67.733101 | 2024-10-03 02:46:01 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0e41e79-eead-3146-9246-46231e27ec59 | -9.0377 | -67.864304 | 2024-10-03 02:46:01 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa82adab-77b6-38c5-ae21-9b031f59ba1c | -8.7592 | -67.702103 | 2024-10-03 02:46:04 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba8f5c9b-e1bf-3081-ae51-6fd56c1ea36a | -10.8942 | -63.8971 | 2024-10-03 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ec1b5f00-a8c5-3241-94db-28aa7f9f1e34 | -8.7822 | -68.792 | 2024-10-03 02:46:09 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28d9c0df-070d-3a6c-a9a1-c1f02b05d250 | -11.2565 | -60.6019 | 2024-10-03 02:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 065e055f-6ca5-3ec5-81e0-a194b6078e9a | -11.6932 | -64.9785 | 2024-10-03 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 69efded0-a0fd-3151-9d93-73c5e14d119f | -11.6931 | -64.9974 | 2024-10-03 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8c6c693a-8ea5-3a5d-95fb-f9ce36afd2bc | -11.693 | -65.0163 | 2024-10-03 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2893175a-7343-3927-b626-f0875712ccf3 | -12.3849 | -63.002 | 2024-10-03 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |


[Clique aqui para ver as próximas entradas](README56.md)
