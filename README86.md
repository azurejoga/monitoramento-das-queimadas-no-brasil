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
| 5a702363-7db1-339a-954d-a26af1a1349c | -8.60933 | -62.59402 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5af7607-708d-3e77-959e-21ecab1f6b66 | -10.09833 | -65.28248 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 413ae445-3ae7-3466-bbb5-ac2eae5c9588 | -9.08662 | -67.42562 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c19f725-e9a5-366d-8b3b-4264ea4a7d79 | -5.7996 | -59.21426 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15091772-c54d-31aa-a362-13f9b7ceccdb | -9.64697 | -59.64086 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef0eddc3-f1e9-3620-a719-a8cfaec1ede5 | -7.65787 | -63.51598 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448f1661-81c6-37f9-9308-bb3217660c30 | -9.19659 | -59.47544 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bec1da4f-11ab-347c-a413-272565220a21 | -9.20199 | -60.79227 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cd99fb7-12c2-32fa-9ce5-f9fb4b10eb3f | -9.15769 | -59.47007 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e279d11-26b7-3ed4-ba7b-2dc3cfd2b838 | -9.51847 | -60.51233 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f00f54-36de-32ac-93c3-c853d434d0f5 | -9.20321 | -60.78321 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0e91a90-f468-391c-8395-ecc9e391083b | -9.07709 | -65.71963 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4911f83-7bb9-31cb-afcf-f4ca9ea53b6f | -8.90083 | -62.42142 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f4dfb11-a88a-394a-8ee1-edc4e976fbe9 | -10.42259 | -60.30203 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06176fd2-add8-38c9-b228-97230260abb5 | -9.17257 | -60.8188 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ffd4cb1-a351-3c59-a21d-1293f4a2dc5b | -9.10045 | -61.43336 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc793c5-d8d2-35a3-b01c-95784de8decb | -9.00305 | -63.63654 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e76455-449b-3603-a6f3-46751f8247b5 | -8.98631 | -65.42496 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 500180a8-582a-3e32-aba3-cb23b986defb | -8.02663 | -69.92172 | 2025-08-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1a70703b-cbef-3b97-a648-5733f0ea34a1 | -8.99004 | -65.42552 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2edc1c30-aa3f-331c-9b2f-977451c6b7a8 | -9.51888 | -60.50917 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e03c479-6d1f-39b8-9742-81aca46ae47a | -9.16084 | -59.48918 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359d238b-4aee-3eed-8694-e95eb576a515 | -9.34583 | -62.58782 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60df6922-6821-3cca-b50c-ac8b7ee20071 | -9.19667 | -59.46967 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b13ad13f-aacd-3f22-a244-a7b08cb902c3 | -8.61085 | -62.64833 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91fe1d8b-9c24-3013-b1dd-a9ab7763789c | -9.02114 | -65.69543 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5aad22a-828f-3a82-8c3b-434726ddfac7 | -7.61933 | -62.73207 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f75ef07-d31f-3648-a658-beeeff75e692 | -8.87639 | -62.38793 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c60dca3-b34c-3eee-8841-f3ceeffa34fa | -8.86222 | -62.42345 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7097e0-0483-3521-a955-5f76a17a531e | -8.88871 | -62.4431 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92f9bea6-66be-317f-8712-7f4223623b42 | -8.90351 | -62.43589 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1fe73f-df70-353d-b458-85f913d22341 | -8.90597 | -62.41753 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed72cbf7-82c0-30ef-94de-9f2b1b7fbc64 | -8.2368 | -61.42635 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971fd8e3-e76f-358a-8a6d-669e1b10d63d | -8.98258 | -65.42439 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2d291ff-c263-3b9c-8d16-5fc97018338f | -8.69074 | -62.87947 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c3182db-d996-3824-8f5f-67eeb55fd080 | -8.99137 | -65.41652 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ba8f5a2c-1b81-33dc-bc89-0b9df7549560 | -6.64636 | -58.82057 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f41ee33-2077-30dc-8a13-a87149d8f11d | -8.5037 | -63.87604 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ea13c7f7-d8ce-333f-99b1-11da449bdcb5 | -9.96113 | -60.18367 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43759ac2-81c6-3e5b-957d-d4608b20dd12 | -8.87967 | -62.43065 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6875bcd7-ef1b-3184-a811-61353db44469 | -9.09854 | -65.72718 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4d4f839-115a-3ac8-b023-00ad21883ab6 | -9.193 | -59.45984 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57e1bd06-773c-34f6-a575-6811057b0291 | -7.62367 | -62.73271 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7241f4ee-2ef5-3dbc-ab5f-881c167b4e90 | -9.95749 | -64.98777 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32003e12-d87d-3ef0-970d-f084775fe128 | -9.26345 | -59.78572 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12b0243d-8dc2-3c5d-b173-f0e0f24abb1b | -9.16298 | -59.51593 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa30a1e8-1e27-3b7a-aa43-69cdc95f8a33 | -8.11627 | -62.87746 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fcbd353-8143-3ec0-9dc5-4e757cc4c4bf | -9.07371 | -65.72118 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b82b7ba5-2465-3d96-9548-0ee46e175d32 | -9.80074 | -61.20766 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bbcbac4-4ef4-367f-a9be-a9994f4ffc55 | -8.90356 | -62.45748 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6dc7cb9e-26e9-3b12-8d5d-37a7ef6cd14e | -8.50013 | -63.87176 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b78d641e-a9dc-3113-8369-3943fe3cdaca | -9.01874 | -65.68607 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23cb1c46-f274-3224-891f-a826fd734874 | -9.17359 | -59.60843 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c90c0020-47fe-38c8-a09c-a9f540d7f437 | -8.9068 | -62.44574 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef27d8f6-79a1-36ba-a952-032fac4cf948 | -8.54972 | -63.51551 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2c65250-e98e-3d22-ad41-9bb5cbc9b676 | -7.52306 | -63.81614 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1151f430-48c0-3ee0-95c2-d76e35b517e6 | -7.55784 | -63.86126 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc3f1184-428f-33c3-aff5-a8dd5482fd8d | -8.89592 | -62.4582 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a724358c-f8cd-32f8-baf9-db7eb193a157 | -8.51289 | -63.86995 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10827883-08f7-30b2-b661-4bf62035f603 | -9.00657 | -65.39112 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62674bce-1f18-3657-90f5-57d8728ee740 | -8.87127 | -62.42474 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 514ce09a-bb34-3b24-ab82-01028f41491f | -9.20451 | -59.49714 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c7f120-3f70-354d-b3e6-d6387c674699 | -8.61701 | -62.60418 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df22555-9a62-35eb-bcb2-608fd3801658 | -9.80572 | -61.20843 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17570863-4eca-33a7-b2f2-bf2caab3a209 | -5.79868 | -59.22107 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a460db-3039-3cbf-8c5c-8ae7589992b0 | -9.19152 | -59.47102 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e09c622f-095c-3360-867a-5891c3ec068b | -8.90495 | -62.45951 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10b9cfa2-b6ea-3484-a897-bbb2b5337d7b | -7.09751 | -62.97139 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98600ad1-7fe8-3431-8192-760b835aaf51 | -9.18045 | -59.46361 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 29eccdfb-95e7-3052-a465-d5ab5ae461dc | -10.45669 | -59.13361 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3cd30cb-26a7-36be-891a-16b1257dfd6a | -7.57307 | -63.44259 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a33a1f58-5e8e-30e2-902c-15864389238f | -7.54927 | -63.86361 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ace0c1b-d6de-3b53-9d99-b1769d68eb8e | -8.60488 | -62.59338 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3192134-b596-3678-8044-f390adbb422c | -8.66135 | -68.67406 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 213b19b2-7428-3e70-bb33-c9f7b3f7185b | -9.47534 | -57.8208 | 2025-08-25 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2053aae9-154c-38ad-b0cc-1e4cb59a1bde | -9.02835 | -65.72316 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfecc58b-0e0b-3a65-9321-e7d1a71f68b1 | -7.5271 | -63.81676 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f2dad85-a7ad-3594-b696-a8b078654620 | -8.9105 | -62.41817 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 057b10b3-6ae2-3e29-a44b-ae7a5afb842a | -7.62051 | -62.72371 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac308cba-f714-35d7-ab63-788e3663f30e | -10.3938 | -57.69131 | 2025-08-25 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37ac1a5e-5cf4-3244-ac56-bf9c41701cb2 | -8.65099 | -63.43537 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c988f7c0-0197-3094-a616-a9ac2ad2bcaa | -9.01472 | -65.38771 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59f9b15b-05f0-3c06-8b9f-9d7b4a148489 | -9.2013 | -59.47784 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 048c0ddd-1a0c-3cad-a011-6577e0e7de68 | -8.54554 | -63.51487 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54e18bcf-cb1d-3fa7-879d-6ce6ddd96384 | -8.2315 | -61.3934 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4aeca6c-5dda-3f15-8d22-df89e49e1d07 | -10.2589 | -59.10661 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 737ec19d-80c0-36ae-b0b9-001b07447295 | -10.41371 | -64.39079 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c8605b42-ffcb-3e4c-abd8-abab0da35449 | -8.98083 | -65.41032 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d4b83c2f-101d-336e-9054-5988cdea70ea | -8.98891 | -63.64622 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df599337-216e-3a89-b0f0-629ae2bc4d93 | -9.00724 | -65.38659 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c72fbd3f-4ce6-3865-a819-889b8af12128 | -8.58953 | -68.14912 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4cad1494-19b8-3533-be79-86617e2c6619 | -8.88485 | -62.45946 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97c15016-5b62-32b6-bc40-28ed9552ecc5 | -8.98149 | -65.40582 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a3faeb26-baa3-34ad-aed1-21a645e30fb5 | -9.15383 | -59.49958 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c4948cf-409a-36a8-9c70-f2948b4494c8 | -7.57362 | -63.43883 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9037ca6-e165-34fc-865e-edb9951ab9f6 | -9.47474 | -57.8256 | 2025-08-25 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8a21051f-e229-33bc-bf02-bba407c8d592 | -6.8196 | -58.95164 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bb7f732-f8e2-3229-b424-92407845490e | -9.12879 | -60.73329 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da9f364-546c-3537-9821-99ce08a152cd | -9.06636 | -65.72008 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 233c2086-e365-3c57-9973-b2dda4155100 | -9.51765 | -60.51868 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README87.md)
