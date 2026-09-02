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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d59c408-f402-3353-8d6d-af9b020c43b3 | -9.0191 | -65.4534 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 909c76c9-39cd-3323-99b1-9357ae09968c | -6.7578 | -59.439899 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8b4275-7c21-34d9-9069-b7c1db5d94da | -6.5878 | -59.115101 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1047a120-bbde-3c15-a8bc-9cbe49ed8ac8 | -5.5437 | -60.228699 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a094fdb2-8609-3ac1-902f-87d9957db4c6 | -9.4475 | -64.558296 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9253bb5-1be5-3e22-9201-9496952a15af | -7.3531 | -60.6045 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78e59d32-4851-390e-8c08-0c918275e74e | -8.1158 | -54.9491 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cea22f9-3a09-316d-b48c-017951ba8898 | -8.2659 | -54.933399 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ed16f0-f30d-35c4-bb07-777211e7fe25 | -9.0834 | -65.372498 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3bf4a4-cb0a-3bf7-8cdf-079ed3e08ea3 | -9.0273 | -65.444199 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 797ce068-fb97-3545-9d7f-f96927d5df82 | -8.4298 | -54.729599 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4ca6fc-7771-3af0-84b8-24780aa25830 | -4.2378 | -62.229099 | 2026-09-02 01:10:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8efb21fd-fa26-3357-b441-927989f6ac64 | -7.5345 | -60.7183 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 764bdb2d-2df8-30cb-897b-c22aa5d15d19 | -9.8795 | -64.973099 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 08f0a4ab-7526-355b-958e-0f5c54148f0f | -9.5552 | -67.484596 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7d4eea-4e98-3cd2-afd0-78362f347198 | -6.6805 | -59.938801 | 2026-09-02 01:10:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3787a8af-c9ae-351e-a4be-75d761bd8028 | -9.018 | -65.401901 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3011c081-9ce8-3402-a3dc-36462fcd7539 | -8.763 | -62.5858 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b144679c-2cdc-342d-89ae-dc3084160c5f | -3.746 | -59.3209 | 2026-09-02 01:10:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf672ba7-005c-3977-bb39-7ca69db0cef2 | -6.6808 | -58.772301 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13f521e3-6c4a-362c-9cb0-b0a2e8f66b4c | -7.6897 | -67.116699 | 2026-09-02 01:10:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3d8bbb9-f9ae-34b6-bc2c-c8dfbae70c22 | -17.084299 | -56.8451 | 2026-09-02 01:10:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81eca017-f9be-3f13-9be9-cb89270b8028 | -8.9079 | -62.363899 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7b2d456-8d2d-380a-90cb-d8d8bc4c8650 | -9.0058 | -67.789299 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b025d5b2-f4ac-30c9-af3b-bf5f3a83be32 | -9.4473 | -67.412003 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8ac790-4eb1-31b9-86e4-b26e9344b285 | -9.1473 | -60.953701 | 2026-09-02 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46a49f46-ac76-3346-924a-919a0560607d | -8.7498 | -62.5732 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76d45b48-0b8e-3e28-9a29-8d67eb6d904b | -3.1923 | -61.136101 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d878375-c65c-3ce0-82f7-db108324434b | -10.4904 | -59.6091 | 2026-09-02 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c817d8c-a8d8-3c7f-8f23-7fd449c32e19 | -10.4847 | -64.316704 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aeb4686c-f25c-33b3-b2c5-dc78b65de0fb | -7.4407 | -61.418499 | 2026-09-02 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5bb81db-1397-3832-8a40-71d978e87c32 | -9.8403 | -64.981903 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc1738a8-103c-3f59-a82c-5a74b8487874 | -8.4531 | -54.7001 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c51cad-5bdd-34a4-a5c9-4c05f6f9098e | -8.4089 | -54.688 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64b4c616-3975-3be5-9433-865e1bb5caec | -8.4378 | -54.6805 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85610bc0-2032-366e-8466-386743e4e759 | -6.6846 | -58.744999 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd22c57c-1213-3b25-b7a8-191766b7dcf7 | -9.0905 | -65.497002 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d247d8f4-7b58-347b-9d8b-c64f06983ade | -4.1399 | -60.696499 | 2026-09-02 01:10:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0251e6-80b8-316d-83c5-0ce1c9d2420e | -7.6995 | -67.114502 | 2026-09-02 01:10:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2652f8-b984-3dae-b3f9-fdae921bdb09 | -7.9391 | -63.445 | 2026-09-02 01:10:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb59ecc5-2119-3b3c-9f54-aee8c7598ce4 | -8.4339 | -54.705101 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d621389-0dae-3d96-9f96-e96427b5d8e2 | -9.4393 | -64.567596 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 033adfa0-14fd-30f0-8471-5b233b0797d9 | -8.7549 | -62.595402 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9dbc8f60-2e54-3837-b3a5-4d4556837577 | -9.0932 | -65.3703 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54568de6-945b-31fc-84cf-b527e51e95ac | -8.78 | -62.480202 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5ec2463-f10a-3810-880e-e99be0b04b7c | -7.749 | -61.1931 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0dfd32-abb5-3f17-a14e-024014289d42 | -8.445 | -54.749001 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5931f95-52fc-363a-9d04-824390394a7d | -9.4491 | -67.420303 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf8380fe-9a73-3e89-9687-f37ab8f5a1ed | -8.1062 | -54.951599 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a030f49a-03c1-32f0-baeb-a739f3aa3076 | -6.6876 | -58.7575 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01c16b99-54a4-3ba4-a85b-d885909800d9 | -3.6506 | -58.915501 | 2026-09-02 01:10:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48301f03-28e7-36a3-9a81-d322a77ba43b | -7.6698 | -62.5396 | 2026-09-02 01:10:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e445c7bc-5fc1-38b3-83f6-61a3fa2ba002 | -6.6748 | -58.747398 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a963efc5-02e2-3d39-842e-0f39f8fe44cc | -3.1225 | -61.234699 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db062538-d5c9-37b7-b90f-39c4c7a2bcd2 | -9.1888 | -65.895798 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7161c4e7-db8b-3948-90e5-22015f0cfe27 | -7.7588 | -61.1908 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2074b304-76a8-3efb-ae05-983c4bde3cf1 | -7.6055 | -57.614799 | 2026-09-02 01:10:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067027fa-4318-3800-9de4-86bc07666039 | -7.751 | -61.201698 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd6dcd4-7e4d-3cb3-aa88-4952f79f2710 | -8.9292 | -62.366798 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e245bc57-c380-3cbe-a395-d0c323206274 | -8.4587 | -54.722099 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ed346d-3244-31aa-9849-0111193485da | -17.0872 | -56.856701 | 2026-09-02 01:10:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 384cd6d9-9b6a-31aa-923a-c0f2cdf2f4a3 | -5.5657 | -60.190498 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 402ee698-7fa9-33e7-9744-166b54695c5d | -3.0864 | -61.212002 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2fb06ee-6903-377b-9427-7f42e41ec169 | -8.9062 | -62.3564 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8de014d-81d5-3838-a4d3-87b4b084d633 | -7.2012 | -60.66 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b072c7a-afb0-339f-93da-c58b7dc4fbfb | -6.765 | -59.426399 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b605aacb-7533-3c30-8ec6-597132aac58c | -6.5483 | -58.563202 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9798a66-879d-3825-98ac-cd07df595764 | -9.0889 | -65.489899 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51eaf524-12de-38aa-b455-aac7dd76a5ae | -3.1105 | -61.2271 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 324cac26-6c35-3f3e-863e-2b89fd150e5f | -10.4862 | -64.323601 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6cf0734-d3b2-31ac-b5f4-7e3c15f906ed | -5.9558 | -53.571701 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64f8d80-6a02-3179-8b82-be6af7093a5b | -9.386 | -60.564999 | 2026-09-02 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 341f9779-ecdc-3b98-ac5b-7e271cf2f6e3 | -6.6778 | -58.7598 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3af901eb-8283-3f5b-ae04-ee1ea41e8be0 | -9.878 | -64.966103 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2b433f7-9237-33d3-87bc-602d26a804a2 | -5.1753 | -60.281898 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 717f6953-54f4-38b3-bfcb-7b4510acb2f6 | -6.8695 | -59.3895 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85e588dc-5c84-34bd-b304-a0bac39c788d | -4.228 | -62.2313 | 2026-09-02 01:10:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71e70607-3b7a-38ac-bf02-7e8544e61d4d | -6.7481 | -59.4422 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35b381ff-21cc-388a-adcf-dbbb089af276 | -8.2215 | -62.742001 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8224d9e7-ddfa-33b7-b407-753d6cc6eef2 | -7.7271 | -60.967899 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 817802d2-a115-3687-9ac1-50ff6e798485 | -8.449 | -54.724602 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f979e6-5846-3062-85db-fc7deef2e93b | -7.3464 | -60.576401 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2cf31b-1497-34e6-a805-1be8a78f462b | -8.0943 | -58.2696 | 2026-09-02 01:10:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be79a76d-a56e-33fa-bb57-9dcdadbe90ff | -6.8008 | -59.101601 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b31e9c6f-ed70-3385-92dd-74f55cc9fece | -8.4435 | -54.702599 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ebb0c5-3503-3bd9-ae77-1a669e560ace | -5.3287 | -60.146 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0d9ec6a-d94b-3f10-aaed-7833eded560a | -9.0917 | -65.363197 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca754735-35b0-39d4-97a1-60200a6a98d5 | -8.0974 | -58.282398 | 2026-09-02 01:10:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4150b40a-6b0f-3cc7-94c2-d366d5296618 | -14.4923 | -59.844501 | 2026-09-02 01:10:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1c1bd6-0168-39d4-b30e-34f81eb20b87 | -8.4186 | -54.685501 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15685797-5483-3900-954b-fd1a205b0809 | -10.4667 | -64.466904 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b73dc064-0ea5-343b-8fa7-b788c9d3fabc | -9.003 | -65.427399 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 393bdec7-23bc-3871-9cbc-274d8b19e906 | -9.8666 | -64.961304 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30ed396a-d8e4-32c8-a5fc-0c44610cc319 | -9.0175 | -65.446404 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9be72721-779c-349a-9941-c4db1225352f | -8.1116 | -54.973 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a75c331-14c5-32a1-8fe3-db17334d475c | -8.4201 | -54.731998 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a45a5ca-20db-3910-99ea-22e7aa2f4b67 | -9.0324 | -65.420799 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf7b7aab-1c86-3394-9d92-5c133cff1de5 | -7.2034 | -60.6693 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf15d0f3-c774-33c4-8ecd-0bf6439c5255 | -7.5532 | -60.447601 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db432814-0f88-3b6b-8313-390bb9ac220d | -8.9275 | -62.359299 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
