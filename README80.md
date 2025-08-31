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
| 84396cc9-066b-3ccd-9011-14cc628fa83f | -9.44463 | -60.57375 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ef50e5f-492b-31b8-af53-7be73e1157b6 | -9.45256 | -62.33934 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e79a222-2c69-331f-a2d3-508a3e99d4c0 | -11.31221 | -63.26939 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e27e39-992b-3f9d-9f90-310f39447893 | -8.74094 | -62.39893 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02d7a068-b243-33e9-a7e8-ac7e6737d894 | -9.06282 | -71.25753 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ed9e173-a7a3-3cf2-bf44-6eb13c5dec87 | -7.92885 | -63.01371 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20f28198-de72-3d87-bd1d-635ac4e60353 | -7.4614 | -70.12947 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953120ab-2443-337a-a131-f38d01aecf31 | -8.6691 | -62.42981 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708fdd7d-b04a-35db-8763-75305a49103a | -8.0361 | -70.08714 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b3a17d-1c7d-3735-b8a2-fd1872662d7d | -9.45576 | -62.359 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e0c186f8-c0aa-350c-9d59-e02dc415dd86 | -9.70417 | -61.28283 | 2025-08-31 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a11ea3b-5491-3c84-a3f9-13a66bb79c49 | -11.41992 | -63.24834 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2ac33bdb-7319-3467-8c5e-84209413944c | -9.45014 | -62.35817 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a43e83d5-a236-3990-ae16-fd2bd39ed0ed | -7.56758 | -63.41607 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b2acc7-92a6-31dd-9da9-83da798d795e | -8.8673 | -71.2776 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee668acd-046f-3c61-9c94-db62547a850c | -8.67621 | -62.42813 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7025f5f-c4fc-34a2-b875-0920e3bbd3ba | -9.28099 | -67.64673 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a384431-cecb-3c8a-9b99-28d0d9f16d01 | -10.7257 | -65.04726 | 2025-08-31 06:10:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72d487bc-763f-3869-bbb4-fc1927d0bb26 | -8.7714 | -72.76003 | 2025-08-31 06:10:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1afb92f8-3e8a-3fb9-b072-10b162e6e0c9 | -7.92314 | -63.0162 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab5e887c-9cfc-3dea-9cd8-9d805728c49a | -11.41543 | -63.25052 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| edfb6b82-cedb-3433-8390-b8d164829c87 | -9.45063 | -62.35438 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12014ad5-0fd6-3b7c-8e3d-a4387cda1042 | -7.84444 | -71.90881 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4839d2eb-5c8c-31f4-a829-9497b9f79086 | -8.69317 | -62.4183 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fccd2f-dad6-33c9-8d56-8bb4b77919f9 | -7.94886 | -63.33065 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd91d9d6-2a8d-3fa1-939d-3b0e3721288a | -9.45094 | -60.57449 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7569187f-2831-3d0f-87a7-cb1338f8746a | -8.68255 | -62.41315 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca87e7ea-fe1d-3d57-b9b2-def2b1d09b0c | -9.44036 | -62.34511 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32641213-0668-3210-a31f-bef91a64afb3 | -9.0718 | -72.23335 | 2025-08-31 06:10:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b630cd9d-ef7c-3cee-adbe-4bf24716d20b | -8.7918 | -71.022 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63311a7b-1734-38d1-9ddf-ffb63ed95076 | -7.8828 | -71.64368 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ac82ece-eda6-3ea2-bf49-e7af55496a49 | -9.45209 | -62.34302 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 981ee7cf-2f62-3553-851a-fee17de43580 | -8.69263 | -62.8799 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b46110b-b0d7-3be4-99a9-24c6cba7899e | -8.5616 | -63.0222 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc9c6daf-86ce-3f7a-b6e5-8404c7aae910 | -8.73985 | -64.08631 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0367fd41-5d0e-3f10-875b-25603762d39e | -8.65507 | -62.83316 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ee8292f-661f-3a00-a43c-95d5dd420df6 | -8.23835 | -72.81189 | 2025-08-31 06:10:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a0c9f3-2c8c-38fc-bf03-ac8d02edb5b3 | -8.73793 | -61.84887 | 2025-08-31 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647bd7f4-6327-3271-a437-63f45025f942 | -7.60729 | -70.20038 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937340b4-e73f-3f6c-b118-acb374448a5a | -8.67166 | -62.42018 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ed478e6-084b-3e8c-8a2c-bf7fa991a6fd | -7.2072 | -69.89838 | 2025-08-31 06:10:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb40e9ee-a8d6-349a-b79a-db48a4a4d4d6 | -8.91684 | -62.41875 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3a7a5f1-8667-3ca8-bd4c-492ffe7a8d2e | -8.88267 | -62.39095 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5026e53b-3017-378a-ab3a-fe5b46475220 | -11.32206 | -63.27189 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41cda10a-e0a2-39e9-862a-384cf71e1408 | -9.46138 | -62.35976 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14a966ec-b50b-306c-a18d-42b3d16f1151 | -9.27778 | -67.64114 | 2025-08-31 06:10:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abb509c8-3577-3305-af8b-5b0d02d5f22b | -9.44774 | -60.57334 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46e711d9-2f99-3361-8428-fdbae8de7ae1 | -7.91394 | -63.00502 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfb4a22b-aec2-3fff-a147-02b105920948 | -8.85324 | -70.62526 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad8de981-8c1d-33dc-a864-d07a92f63861 | -8.68019 | -62.43128 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a68c8122-3355-3f09-98b9-73aae56ca4f0 | -8.65569 | -62.44649 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f133072-6dec-393a-ae2a-e74c0c02de27 | -9.43521 | -62.34061 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41eefedd-2942-3a1a-a351-d03a9b9ef381 | -8.66137 | -62.82711 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53991c64-bc05-3a82-91ad-ed15c6798b1e | -9.89665 | -67.01663 | 2025-08-31 06:10:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e313145e-4ba8-3c14-a1ce-5270eddb7331 | -7.82842 | -71.94552 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d057b818-3a4a-33f5-a802-aaee0bcdac4e | -8.66289 | -70.04261 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e7a60f6-af34-39eb-8109-857085db743d | -7.60388 | -70.19984 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37a1f17-454d-3c77-a896-5ce08155b46d | -7.56539 | -63.41646 | 2025-08-31 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58afadc2-fed6-3acb-80c2-883c338fb725 | -8.88317 | -62.38729 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e29ac189-3411-3d92-ad39-c8e7cc83524d | -8.87064 | -71.27812 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72822289-51e3-3b9e-99bc-491b205fcd4a | -10.45786 | -69.45271 | 2025-08-31 06:10:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2649a6f-6cd4-33ff-8f52-e5b075639aef | -9.44084 | -62.34142 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49b8cc29-4890-3a59-818c-0846c4a5842e | -8.39256 | -70.82822 | 2025-08-31 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4acdd7-63ca-3006-8649-acbe4e3fca0f | -7.89725 | -63.0092 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be6bb403-580d-3a51-be05-8210b6f99d50 | -9.46286 | -62.34828 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 231887dc-f6e1-3495-b160-6ce251423f67 | -8.68621 | -62.42839 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89a9ad21-7113-3abc-bcdd-3a012cd10190 | -7.91787 | -63.01546 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 00391882-3679-3546-9599-cd85ebeab63d | -6.92751 | -71.78102 | 2025-08-31 06:10:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a5dc903-7dd0-3d3b-9801-5195c0d39e12 | -11.41448 | -63.24757 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| acfd8f24-8f07-3f97-ab90-3f04417ca2e9 | -8.74748 | -62.3923 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf7e084-2827-32a8-96ba-e6989f4cfdba | -9.44742 | -62.33477 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15adda02-9999-387b-b013-f308c263d58c | -8.84985 | -70.62473 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb84f51-285f-3ebe-93da-227b26f3a7ec | -7.73322 | -71.99113 | 2025-08-31 06:10:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156bce21-0e84-3fb5-a3ba-9593acca27ba | -8.677 | -62.41245 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed37c76-b586-3972-966c-91369472fa5e | -8.67067 | -62.42739 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0575f1aa-ef9e-3cec-82c4-b37989c64e68 | -8.67721 | -62.42089 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d045521c-a4e5-3cce-8b77-bc067b5ed268 | -7.46425 | -70.13367 | 2025-08-31 06:10:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90114f6a-91c0-3a03-8e4d-aff614d7a5ca | -9.44404 | -62.3611 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e3af9c-f213-3c3c-8365-8e82ae4d3426 | -11.3887 | -63.27616 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1379d986-1233-35ce-bc02-b0cd66a11ea2 | -8.55674 | -63.01816 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed450b4f-4446-37c4-9b28-d5f9148812e8 | -9.00167 | -63.62298 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68fffedd-3c4e-3216-a229-cc3ae732e434 | -8.58626 | -70.11585 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03f6b610-ce36-3cdf-b636-21afa258af96 | -9.43177 | -62.34129 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 694db745-b7ba-3d25-b591-654d1162bc2f | -8.03953 | -70.08767 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 911ac18f-2d18-387c-a3d6-31de2fde2ad4 | -9.46236 | -62.35219 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86e7fd4-babe-3225-b283-90cf9b342e42 | -8.68066 | -62.4277 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d70803f-e6e6-3ba6-97b9-ba48336ff6af | -8.74897 | -62.38121 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d58b09-426d-3aea-99b6-655fb64e60fd | -8.66092 | -62.83052 | 2025-08-31 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c4878f9-84f1-3963-af77-ab8a12827ad4 | -8.23444 | -72.81489 | 2025-08-31 06:10:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f1aad4d-d476-38de-8f6d-c1775ab72993 | -9.45161 | -62.34674 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6340dad-e68a-3d85-9d9e-bdd0c94780b8 | -8.67572 | -62.43173 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b0093ca-db9f-33bb-9293-15a6564b39f1 | -11.32351 | -63.2673 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9a452ce1-4d67-3b6e-ace7-b3837eb3fa5f | -9.04722 | -71.59866 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 389516e0-a043-3798-9dd1-ae061db47eae | -9.06617 | -71.25805 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26b70b77-f556-3b76-b60c-c803c6f6a16b | -8.88823 | -62.39176 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22890a4c-2b73-31a9-8fae-3d540981a060 | -8.15384 | -70.54836 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d558cd85-d0b7-347b-8d95-9de018e175fd | -11.38282 | -63.27892 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec823a7b-0ffb-362c-be3c-c8668b605e81 | -9.56027 | -66.68906 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01e3ba0-0745-3ec5-8cb0-5def683e2bbc | -8.73958 | -69.41541 | 2025-08-31 06:10:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4281bcca-2272-3baa-b9e3-f24a57126c33 | -9.56866 | -66.69028 | 2025-08-31 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README81.md)
