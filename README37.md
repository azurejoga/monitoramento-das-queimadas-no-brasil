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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a71c8dc9-4683-3de3-a362-f1056523a7e8 | -6.72112 | -58.9327 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83fa7b3e-fbee-3976-9b93-076df88634c2 | -6.63002 | -56.37463 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04cb3411-3160-3313-bd33-7e520d3f8dc0 | -7.40849 | -59.99489 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a2e36d7-a931-3141-b563-eca92440b585 | -6.79706 | -55.8451 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e404d90-54fa-317a-8ea5-74b29614f050 | -2.94917 | -50.31535 | 2026-08-15 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d83679-f354-306f-abc8-b403edf25b0c | -6.95621 | -59.28421 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da6ec1a7-1a5c-33d5-ba6f-0e5f2eed6f26 | -7.68929 | -55.16048 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fae3dda-21b8-3b0a-a019-6d023743d40c | -6.96267 | -59.29224 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7cdf9ac-cb87-3e14-8b4a-7802c73506db | -6.62005 | -59.06857 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8175be0c-596c-3679-9c72-a9a2e1f85be4 | -3.25221 | -61.19267 | 2026-08-15 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1d2b5a-931c-3a88-a253-82673a24ab3e | -6.60639 | -58.9989 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3b46e77e-2d94-3762-95ad-d281f809c799 | -6.62118 | -59.06124 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 674fdc37-ed45-3035-ad5a-5c0aa4a11aa3 | -2.73887 | -58.18855 | 2026-08-15 05:33:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2dcf2cb-764e-3728-9b00-f9c748edc90b | -2.79079 | -49.5784 | 2026-08-15 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f9f57a-baf8-330a-ba01-d043916536fa | -6.79394 | -58.75698 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0034e73-e92e-315d-b5cf-ff632c4bf8dd | -6.94372 | -62.87473 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ff8209d-829c-3bd4-b168-cb65b0c4598f | -6.93418 | -62.87794 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45968e4b-7b93-3c0e-8c09-fa32bbafc3f2 | -2.94866 | -50.31631 | 2026-08-15 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 063bec9a-3a2e-3b9c-9b34-8fb9893533c0 | -6.96211 | -59.29587 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1f41cfe-86ea-3595-b9ad-cdef5b69573a | -6.60241 | -59.00204 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 61584b07-7285-3ddf-91d3-43f72af7b955 | -1.48214 | -60.29893 | 2026-08-15 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6cb5a44-53d0-3cd5-9962-8fcbc81627d5 | -3.72361 | -55.96691 | 2026-08-15 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be78ca94-914d-35b0-a903-92cee0a17b28 | -6.77443 | -58.74626 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13590fee-4bcb-39e5-9019-ecb5e03dbf5d | -6.7845 | -55.84673 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea8ced7-5f18-3a56-ad03-c8bffd52d552 | -3.59916 | -58.62297 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71fcd058-7315-3969-800f-c02dfbb0ba8e | -6.63469 | -56.26479 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 705d1608-00b8-3994-baf2-f2bbad5ab589 | -6.85834 | -56.39926 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3aa0825-3b9d-3e2a-88af-b19534d25f21 | -6.60696 | -58.99523 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 83199065-c36e-3a47-bcf2-7275fea5bd05 | -6.79201 | -55.85143 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69a859e8-e976-3ad3-ac92-de166a77bb8e | -6.62288 | -59.05029 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c369fb1-b7c4-343a-b51a-6927592b0584 | -6.60924 | -59.00311 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b79920a-fb58-3ee6-a2fd-3b1159092df1 | -6.85669 | -58.96084 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42e99b09-95ea-31a5-bb79-d17f06659d7c | -6.62572 | -59.05447 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09f0bec4-86ae-3e72-9376-9637985b5459 | -6.85142 | -56.41653 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0693dd1c-e5cf-3ca6-897b-87eb0929a7e2 | -8.07833 | -54.87476 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82c3a542-4bf8-309b-81a1-9f68cf92c94f | -6.62175 | -59.08009 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74ca84bd-c4b9-3639-abba-fe5617171352 | -6.58112 | -56.35691 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb727141-39fd-33fa-869d-630027c0c89d | -6.62231 | -59.07642 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f178361-e9c8-3526-bd53-1d8400cb8a7c | -1.48547 | -60.29945 | 2026-08-15 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c66ae20-c314-3d90-8e49-1e004f768b89 | -6.79007 | -55.83687 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cc24a4-85eb-3266-9496-9b80918d1607 | -6.01698 | -57.83199 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0b6b056-a2c0-3bb5-a04f-dce59943a5db | -7.45889 | -55.30267 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec69aeb2-9cb3-3ede-9140-b7186c57930e | -6.86151 | -56.40475 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1495c686-8464-3b3c-90c8-af3ca1498f05 | -6.95789 | -59.29562 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22921f87-c502-3914-8cd2-5140737129b0 | -2.79018 | -49.58243 | 2026-08-15 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80234d0d-a3ea-37c2-9870-9d5cb4674256 | -4.10541 | -50.99123 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1832b2f8-9fbe-3e78-9f91-bc17b4d00b28 | -6.96945 | -59.2933 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26557c7c-fb86-3625-a1e4-2b9c656f4fa7 | -2.79596 | -49.58335 | 2026-08-15 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce6f0692-27a5-335b-9dc6-70edfcbbed17 | -2.80803 | -48.59479 | 2026-08-15 05:33:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bba499da-799c-39c0-9c25-a262b9e9174d | -3.74064 | -59.32928 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c833515c-6cd0-3c00-af5c-dc0984a7a35f | -6.79758 | -55.84161 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80359a9a-566e-3d00-979d-e48f7ff7f2eb | -6.96014 | -59.30341 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 800ec790-ccbc-345f-992e-5fbff41b0c32 | -6.96017 | -59.28111 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bad64727-af06-375d-b27b-234587c8978e | -7.69412 | -55.15709 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35ac18ba-e4a3-35fb-ac1a-fcf5b25a38f3 | -7.69668 | -55.16974 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ee7272-7a3a-3ae3-a55b-847c18871210 | -4.30867 | -59.46415 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c009d18-813d-37b8-bdba-bdec2e268ca2 | -6.62061 | -59.06491 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5031a00a-df5f-354c-a775-a13763650b30 | -2.53117 | -57.88564 | 2026-08-15 05:33:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab61341b-8d0f-3648-bbae-cbd463d382c8 | -6.72397 | -58.93692 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0aadf8f-3e75-38b8-a281-d0aeb4406980 | -5.50033 | -60.14657 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a8acef-6d6c-3583-9d24-84d6bf7236c7 | -5.95348 | -52.26352 | 2026-08-15 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 477463b4-57cb-3e62-adc2-4b4db5ea9648 | -4.31424 | -59.47216 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 153540ae-1f5e-37a0-b02d-c9a8bb33e7c7 | -6.96356 | -59.28163 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 511f8c9b-29bd-3a6b-961f-01a1a43cf6fd | -7.05682 | -56.51693 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62952e39-299c-36ab-b39e-46a69240f018 | -6.70801 | -58.94963 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf1fd8fc-eeff-3410-b451-8a85fc1d1f84 | -1.77935 | -55.52877 | 2026-08-15 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a292ba9-2b29-3397-9d04-bd934d8ca1e4 | -7.45826 | -55.30623 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e83724e8-010f-38d0-a34f-3d1fe75c7d70 | -6.85866 | -56.42432 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26777259-8012-37f5-a842-a82f738ecebc | -2.94861 | -50.31896 | 2026-08-15 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87bcfbb7-9115-3872-8843-42a0bbf66e4e | -6.65256 | -56.41396 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7254577d-220a-330a-8393-ee0a9b8d1e36 | -6.79848 | -58.77316 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c35af683-c10f-3415-b3b2-ac942ace1de2 | -6.58885 | -56.3583 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b0e2fad-ec82-3420-abfe-a39bc0aa8b34 | -6.59843 | -59.00518 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca908be9-be8f-3e6b-b69c-959d94069a26 | -6.78955 | -55.84037 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de50b363-26ef-3047-ac1b-5ff9683c54fc | -6.9431 | -62.8785 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf80b74-85aa-3138-9f6e-788dd165061a | -6.8136 | -56.43074 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ac76fff-df91-33a9-acb6-16b0cb33ecce | -6.8199 | -56.44149 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44ac4eab-394f-3623-bedc-24a351f7f076 | -6.64812 | -56.41184 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89c81764-4612-3368-8b19-b123c690dc06 | -3.26035 | -49.52649 | 2026-08-15 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f70d88b4-5938-3187-8976-9b1a5c4aedef | -6.95282 | -59.28368 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 184d9967-c914-336c-b2db-1ba70dcdf152 | -6.84414 | -58.97404 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3a87a6-7da9-3881-ac75-174b785b4718 | -6.83758 | -56.42934 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2629e188-cd3f-3945-b24d-627ceaeaaf5f | -6.96071 | -59.29978 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb77fee0-cb6b-30f4-91dd-128177d04029 | -3.59972 | -58.61938 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d524ae-8068-3f9d-8359-c4fe67aa5719 | -6.01932 | -57.84048 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee03d5dc-da52-3f89-9000-212265718009 | -3.74785 | -59.32684 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75bf4143-721f-33cf-8c23-e13f529ef7a9 | -6.60264 | -56.34566 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de676e8-004e-354a-9f10-55c52432bb86 | -6.97284 | -59.29383 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32ceaef0-04fa-38b3-a3d1-d3ba67cd6961 | -6.6172 | -59.04193 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a018aca-3fde-396e-afda-be02b192ae50 | -6.84919 | -56.43118 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d6d1d67-f8bc-3af5-af21-6b4723b58c25 | -3.9475 | -59.62913 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b76e9e2-e319-3701-b997-a22e02f98b22 | -6.71769 | -58.93217 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aef1f3c0-ad4b-3222-81a2-a19e17acce80 | -2.74777 | -60.23536 | 2026-08-15 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 788a2134-efef-39f1-8e98-7020fdc4bbf2 | -6.70401 | -58.95283 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96b3e313-abbb-35c1-bdf5-0c2830ef0087 | -6.64346 | -56.07226 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac95b1d5-4587-3232-815f-c701c8ca57fd | -6.79271 | -58.78762 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40443d06-075f-3ef5-9edc-ab422b135bf7 | -6.01758 | -57.82802 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dff28b54-8585-33fd-8f50-06234c78f583 | -6.96242 | -59.2889 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfc0c690-4b7f-3d29-9689-1f125a4a754c | -6.78398 | -55.85021 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae486389-f985-3602-bca2-9b10f5fd82f9 | -6.79111 | -55.82987 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
