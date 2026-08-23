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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f92fbd71-548f-3dc6-9e59-deb0113ceda0 | -6.695 | -58.7291 | 2026-08-23 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1aab71e8-422c-3638-8ed3-a3958bd85435 | -6.6765 | -58.7492 | 2026-08-23 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| df5da4c6-689e-3edc-af92-040e51152c7d | -6.6949 | -58.7485 | 2026-08-23 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5a6f3c88-150e-35cf-9995-139a5c2ba11e | -6.9699 | -59.0658 | 2026-08-23 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 9493fde8-9b1f-3598-b0dc-621efccb7e52 | -6.9514 | -59.0666 | 2026-08-23 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7e2cbed5-3125-3479-8b2c-4aac76059966 | -6.6766 | -58.7299 | 2026-08-23 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a9405a6f-f9ed-3aa9-a635-b1df94b7c479 | -7.44144 | -72.73135 | 2026-08-23 06:25:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04ccc47d-f705-3b5c-afa3-620f0254962e | -9.85698 | -60.10754 | 2026-08-23 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0c46fd0-c064-3885-987c-cba91e963b21 | -7.78718 | -61.43301 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7329eb1b-07af-396f-85a5-ce33d688545b | -7.61428 | -60.98084 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52a76857-4b41-3ac7-866d-f4f741367f86 | -10.06445 | -67.55078 | 2026-08-23 06:25:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a4c9de1-853c-3ee1-ace4-b73d9ea99b7f | -8.91926 | -60.72786 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e7d565b-7c06-3917-b033-bcba76991bad | -9.10412 | -60.92421 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83e8d696-c75f-3dcc-a48e-ff500eba38ba | -9.11476 | -61.59301 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f0ea35b-0c90-3c95-8076-589c630fb66a | -7.59936 | -60.93683 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 957095f5-f20d-3eaf-bd60-1190bedbda48 | -7.68436 | -63.34166 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927de8d6-7866-3bd7-a4e8-461e3bdc7da6 | -7.88429 | -72.95227 | 2026-08-23 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12baa2f1-d269-38e0-968f-65541d69545d | -9.08057 | -65.40954 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99d736b5-0cba-3953-86c0-b2cd5f3abf64 | -6.80001 | -62.91426 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e8d105f-ec2b-3657-9e51-ee2cc8543d47 | -7.61765 | -60.98131 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc3022b-cac2-3eac-9c18-52f4b0f770c1 | -6.82171 | -59.67094 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82949224-204b-32a3-940c-a6c7dc466b08 | -8.92732 | -60.71981 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 789a9b1d-90aa-3968-9cd9-e97b61781c11 | -6.82646 | -59.67349 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 195c7817-b9d5-3638-9429-0025eb74a592 | -6.85437 | -59.41344 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b1e06cf-a672-3eab-a15a-3273f022d4b0 | -9.09727 | -60.92339 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8d17320-a11b-3e42-abef-51eff02375d9 | -9.12296 | -61.59932 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 975a5aff-27fa-3f41-a222-e7214dcf5cb3 | -6.81115 | -59.67896 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cf83985-9bfc-3ab8-8ec4-71e82b5ee3bd | -6.79534 | -59.79764 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0aa58ff-2ad3-3a11-9c36-4b41e04ec6d1 | -7.59863 | -60.94267 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fddd6810-e85f-3bd8-b5ee-4be7a40e08e0 | -8.92616 | -60.72881 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8234f9ea-5f8c-348f-b506-87951ea62c0e | -9.04844 | -65.4547 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45de01aa-18ad-30ef-b295-5518c3890e64 | -9.09836 | -60.92317 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3109ce7-eef1-3e8c-ba6f-99a1a0f510c9 | -8.70086 | -62.87493 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23a1df08-7dc8-35b8-8024-bc7f856437fe | -6.79155 | -59.66181 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e9837ec-9bcc-3a34-bf05-e42a3289b2cb | -8.69791 | -62.89748 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a538bb7-d3ab-3304-a3e7-ee1096c0d8c2 | -9.32847 | -68.89533 | 2026-08-23 06:25:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eeefab0-5977-316a-af5a-8d55350b91ff | -9.14496 | -65.9524 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d62aee0-dec7-381b-9b93-7ef7d4e59e23 | -7.97256 | -63.65488 | 2026-08-23 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fbb4ba6-f5cf-332a-a534-c02860070aa3 | -7.59552 | -60.94242 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6a469bd-390f-3a5c-923c-50174ebeea1c | -6.81019 | -59.68616 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 635176e0-6cc3-36b0-b810-9cdfcee0abdd | -9.85605 | -60.11504 | 2026-08-23 06:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 500cfc6c-aa0d-35c8-a2e7-c22ae2fa7ae5 | -6.82743 | -59.66623 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a63147f-7674-32a3-b2a8-e632a3f64105 | -9.12367 | -61.59385 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc195d18-e952-3186-8f90-a78e43d26186 | -8.40693 | -62.69359 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17fda0b-2748-3d68-8666-e6be1842ebbf | -6.8006 | -62.91006 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2bf99305-7611-3025-8036-0dd5ab2f49d1 | -7.78065 | -61.43204 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db275291-70d8-3204-b28b-09133338b6fe | -8.92692 | -60.72261 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93472154-1045-34bf-b45f-b68808739a40 | -7.68491 | -63.33763 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 723ae50f-99f2-352d-8f7f-65ec067db625 | -9.03937 | -60.44406 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4317d45a-67d4-3017-814d-136369c90329 | -7.61093 | -60.98058 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de58c746-0e75-3acc-bfb6-447f60d6a355 | -6.82024 | -59.66544 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82a7a759-2e20-3b14-a306-d3998877b514 | -9.11639 | -61.59838 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5901ea80-ea4e-3829-841e-46897e8a3183 | -9.17587 | -70.89586 | 2026-08-23 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65693769-77cb-3b52-a510-c666aef38541 | -7.59768 | -61.23014 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52b326e5-dc62-3a4d-96a3-481f506dde09 | -6.80118 | -62.90586 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec802f5b-07eb-3db3-b86b-3d3bcec42a94 | -6.85352 | -59.41571 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab25c731-b76b-33c2-9981-4db6d00401e6 | -8.90011 | -60.5447 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba9382ac-8d96-3eda-9fe9-292dd64af761 | -7.7879 | -61.42739 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96896ff3-0123-3792-a14b-e57f8a60e343 | -6.6269 | -69.85266 | 2026-08-23 06:25:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6988c7e8-0685-3cf6-bd17-ec29f258dd6f | -7.78851 | -61.42725 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a92b1fd0-f5f5-36b2-bd7f-e86e307e229a | -9.10983 | -61.5974 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f91798dc-95b6-3a37-b504-df408bbcd638 | -6.81928 | -59.67267 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9487b8ee-76e8-3976-94f3-145f0c727b9e | -6.86164 | -59.41448 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83290e26-67a6-3c1e-ae80-6e6a5175756d | -9.65784 | -63.84005 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4999e17-8715-35e4-bf13-47a2796eeccc | -9.40509 | -65.94574 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 249a0742-3c02-3535-8732-13fd5b73d336 | -9.32439 | -68.89481 | 2026-08-23 06:25:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39a357ae-41e2-3f98-9b47-a9a14c0e0a83 | -8.92041 | -60.71885 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a601e21-8752-3583-8dd2-b37064df715c | -7.60831 | -60.97413 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cfb09f1-f85d-3717-864f-eca343c0d1dc | -7.97825 | -63.65567 | 2026-08-23 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a57643ce-2acd-3245-9c72-dc772eec5365 | -9.40573 | -65.94052 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 941cd9df-da4e-35c2-8e0e-c6c10f58c6e5 | -9.4107 | -65.94133 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a157a84a-97a7-3acf-b0e2-f31bfa1a20aa | -8.92651 | -60.72604 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e467fb-6941-3503-8afe-2fe5ef628b38 | -7.60142 | -60.94948 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f125472f-0fb2-3b31-bdaf-16d36c74ca6a | -7.56767 | -61.20327 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79ae36cb-4af2-3afb-8c13-5684070a1fcc | -6.8289 | -59.67174 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d7573a5-91af-39a2-b236-838e083108f3 | -8.40144 | -62.68813 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 213bdd37-b2cb-3688-b714-3c314518634a | -6.82263 | -59.6637 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3cfa1f8a-4dd7-3daf-9ac5-217089e49763 | -6.79943 | -62.91845 | 2026-08-23 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eba57857-0881-3179-892d-d058cd02f97e | -9.41006 | -65.9465 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1979365-7fa8-319e-a294-90b59bb22f1d | -6.86906 | -59.41016 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c679bf-9a5a-3eb4-a830-c51fc9d7d2d8 | -6.79872 | -59.66276 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a888c69-834c-3ebd-8c43-54174fbb083a | -7.61885 | -61.61288 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f795d14-3fc3-39df-91fc-2888f3a603ef | -7.62725 | -61.59795 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc80f8d-8658-35a3-afb5-71b7328ee649 | -6.79439 | -59.80475 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 12039de4-ddab-3f1c-8235-ee0cef6d4382 | -7.61941 | -61.608 | 2026-08-23 06:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 345bfef2-8d58-3f1c-a364-ba508b3d8b4d | -9.14992 | -65.95307 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06112a42-318a-30f9-8a1d-d7db8c657d7d | -9.1082 | -61.59197 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e803f7f-b41f-302e-bb3d-fe3cdb1b278c | -9.10097 | -61.59645 | 2026-08-23 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c7fc614-615c-3c43-b63f-a8cd14716775 | -7.56842 | -61.19771 | 2026-08-23 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7e2370b-f7be-304a-a4b8-4b79c646d95e | -9.0976 | -60.92947 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4aa5ebc-0662-3538-82d1-39ba3f3dcc49 | -8.69481 | -62.87413 | 2026-08-23 06:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bfc45bc-e5ec-33af-a183-b489ece4a4a8 | -6.81455 | -59.66994 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98e17a5f-4b87-3261-98ef-c883be0f1e46 | -8.92001 | -60.72164 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4abc61a5-2d65-33a1-ab9d-1d017e5d4818 | -8.89311 | -60.54387 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6ebe3ca-cdc5-3fc1-9d1e-9495c2f10eb3 | -8.89929 | -60.55119 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b45a777-6d4a-3d32-884a-7525e48c2581 | -9.14419 | -65.95798 | 2026-08-23 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba280f24-0861-3351-8511-753dffb3b15e | -6.86079 | -59.41673 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f988675e-968f-32b6-94e2-1d720c842e8a | -8.91881 | -60.73139 | 2026-08-23 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e296f8e9-6bef-3d3b-945e-4d26518aeb2c | -6.86177 | -59.40936 | 2026-08-23 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a936025-0a21-375e-863b-6c6f2dbc7865 | -9.66358 | -63.8409 | 2026-08-23 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README69.md)
