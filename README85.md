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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd36eca2-7c70-3e21-a978-04695985fc38 | -9.24161 | -59.79095 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b39d10d9-1868-37c4-ba16-3c9f9d9a8256 | -8.04202 | -70.09402 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d5fb8b0-664c-34cf-99ed-364dce652671 | -9.40455 | -60.56595 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb15f51a-b151-394c-bd79-456e79694e3c | -9.12143 | -65.7786 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 265a9ee2-05d3-365b-9156-279621bec4ea | -8.92043 | -65.92843 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b85f84cd-23f2-3bf3-848e-43d136567104 | -9.1575 | -59.58776 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6640c3aa-5abd-3bdf-a4dd-b877e6a34381 | -9.12919 | -65.28569 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d01d523a-9454-36b2-84d2-b893cc13442b | -8.88737 | -60.75446 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94879517-df52-35bd-88b9-5841c7362388 | -9.10723 | -65.7802 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66460d8b-dff5-3ea6-b0b1-8445ad80b44d | -8.91733 | -60.71473 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209c0ab6-32b6-3f49-ac84-e78930d4b8fb | -8.34489 | -62.93517 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79ca3c82-5fdb-355e-bd3d-317f20ee25f1 | -9.08902 | -65.73943 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6c9c0374-f478-3217-994d-6b62182ecd6c | -7.54219 | -63.84154 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd514eb-e2d0-3b3b-a97d-a010c2c2414e | -8.94474 | -65.95091 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c35ee95d-4c97-3d53-9bef-1e2e4879f87e | -7.86975 | -69.95239 | 2025-08-28 05:48:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ea4957-c2e1-32f8-80e9-410b30cadb4e | -9.19654 | -59.64627 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e23451f5-fbca-31c6-ae5d-40f50a4b0423 | -8.70333 | -70.54987 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d8437b9-8477-3723-85fe-3be079b73150 | -10.47333 | -57.95066 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77567d6c-8cce-3a09-aab9-148237d740c9 | -8.69008 | -63.8362 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c153d4b8-9d10-3b5f-b2d7-3d839100a553 | -9.54142 | -62.3918 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cacfa8b-d187-39c3-9105-11cd3c97d270 | -8.50333 | -70.02361 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb7b8a0-1d09-352f-808b-92181517e051 | -6.25535 | -60.018 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2786895-ae47-36eb-bfe8-f702e05d71ae | -9.11688 | -65.78551 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| eedab714-c703-37b5-adb1-594c8dd90143 | -8.57485 | -63.92656 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79a96bd6-ade3-39ed-8794-c5b09f9385bf | -8.10366 | -71.24901 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9184be51-22b2-3bc3-bb97-f64de09c4284 | -9.24541 | -64.41431 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1104bb2e-3222-30c8-81ea-e1e670475667 | -8.95151 | -65.95197 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5362fcab-05ce-38eb-8905-14d2ad38ce5e | -6.24553 | -60.02128 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d18f0b23-040a-3f3c-bfa6-eeb213727333 | -8.96279 | -65.94624 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 904674b5-8b03-36d8-ad26-0371f6ff3d9f | -9.50708 | -62.7822 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba0bb49c-a386-3a6d-98d0-c2b93c140ac6 | -7.60416 | -63.3468 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04fff52b-e45f-34e1-97a9-60a44751f489 | -8.92776 | -65.92583 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 444d12e8-4e6f-38dc-b57c-92d3507520d9 | -9.00448 | -65.71902 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8507ba7-40a6-3a19-9da1-b617d87e2951 | -8.99651 | -65.70259 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 223ac38e-1dca-3898-891e-b07173486f54 | -10.46723 | -57.95375 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d51f3927-4481-3013-914e-25b12560ea4d | -9.00674 | -65.70421 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4d1ffed-613c-32a3-8021-3aa4e64e6292 | -11.23183 | -55.06327 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a198a030-997d-308f-99bc-92e3446af13d | -10.47942 | -57.94766 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd9a8d92-168e-3179-8591-1bf00bd03232 | -8.88156 | -60.76295 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95442902-df75-3501-b3e9-158fa3bdff1d | -8.92948 | -65.93732 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86322807-8b3e-3a3c-b9d2-5ab5f9668cb4 | -9.31728 | -63.43959 | 2025-08-28 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63388de6-ab17-3bf7-aa8e-3bc53d023853 | -9.08729 | -65.72777 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 492f5220-03a5-37d0-a7b4-070aea79543b | -9.41313 | -60.57206 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 95e424a5-aaf5-3f14-8c71-ade1836541f5 | -8.51647 | -70.1852 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 836869d6-4899-37ae-b409-24d68a8a7f45 | -10.24483 | -59.66464 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bd81724-ef7e-31bb-b5b9-fa9d0ac5f328 | -10.48189 | -57.95833 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbd734fe-abd4-338f-ab3a-3f46e4fe6c09 | -8.57917 | -63.92274 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d759ae60-1757-31e1-816e-4d12e630992f | -7.402 | -62.2869 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e106e8b0-0d76-32ab-936a-f3ce636c77cb | -9.1367 | -65.28292 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe20879d-c9d3-31d9-b60c-e4038d91ea73 | -8.68176 | -68.69038 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f09814ba-6c73-3d7a-a07a-dd4bba8e8c02 | -7.34828 | -57.63392 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d11fb3-8c2e-36b5-a3c1-2fb90eb7c454 | -10.47537 | -57.93506 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 43baca1a-946d-31ef-8013-a346d908b170 | -9.12711 | -65.78706 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 7caa6c5c-2de7-3cae-9793-00e4e76760ed | -7.54392 | -63.85489 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e442082f-bf03-3389-ae65-db716af70c38 | -9.10948 | -65.74261 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c23137d-b61e-3943-8d28-b4ad0209ce10 | -10.47207 | -57.94564 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| accf894f-5e00-356b-90ab-fa91351d3c3a | -9.0856 | -65.73891 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34554cdc-d394-336c-835a-e44568a30b5e | -9.13052 | -65.76482 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e254fe8-4216-342c-9827-c75530865b3b | -9.79094 | -64.23973 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f15d08-d3f8-3c7c-bdfe-a51afaa7460d | -9.49184 | -62.38834 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf62e588-e6d8-3092-b077-bfff0e8ec9b8 | -10.08403 | -62.89202 | 2025-08-28 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39afc4e5-94be-37cc-892e-8c33f211e805 | -8.68511 | -68.69093 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ab52b69-3a9b-3ad0-8b94-e7bd4991e20e | -9.12484 | -65.77911 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 310313f9-7766-3f69-b156-864add3bfaeb | -9.13847 | -65.78123 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775ddde5-e5c1-31d9-ac8c-cbfac858be14 | -9.13208 | -65.29008 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2156885d-ece3-3570-aed2-5d7202b19098 | -6.00245 | -57.85382 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f04d5d2a-d327-3030-af0a-b1ed1baec412 | -8.9026 | -62.47689 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe5410c-2a7d-3737-abab-1d11a3ff42a4 | -5.4234 | -60.16206 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aa9e1db-a340-319a-bd98-e820523d1017 | -10.47765 | -57.94659 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bc4d1b1-11db-397f-9bc1-fa81fc44f473 | -8.87704 | -60.76231 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a13ca23e-ab17-3333-ad0e-10936e6214d9 | -10.47187 | -57.9618 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0615b407-888b-3eea-8c7a-e45b870a308d | -9.08616 | -65.7352 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e919ea63-270c-33e2-917d-339f0cfbd1ab | -8.92437 | -65.9253 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31e1c986-13ea-3442-b74c-24fa42149149 | -9.73083 | -64.90513 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cb0cc6f-6846-3f7a-a03d-96b668ccbccf | -9.11745 | -65.78179 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 539fd06f-ac5d-35f2-b1a1-88b10ff8e36a | -9.13323 | -65.28237 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aaa17d32-1dce-3951-8dc8-b72174b96101 | -8.57109 | -63.9322 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a62e21b-7203-3ac1-bbdb-c1f8d4e0fed6 | -9.00733 | -65.72327 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b731e16-ee50-38e1-97a9-68b104aff66c | -9.13393 | -65.76536 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d4097e-e4f2-3fb7-84ce-103e06e11ce2 | -5.91722 | -61.30775 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56bfd8b-1778-3b92-91ef-c6c88698d42a | -6.25011 | -60.02197 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3a66ec1-ebe5-3c0d-967d-faefafd83fc6 | -9.48011 | -62.38279 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acdcfc2d-0f63-3c2c-9151-b6125e52299b | -9.11972 | -65.78973 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e1c4c3f2-192b-3d7d-b20f-eb288d61ae43 | -10.46551 | -57.95274 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c999ebb7-0fb7-3d13-b2c5-857948010bf7 | -9.02211 | -65.69514 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53d055a6-5127-3831-ba33-b7e96033e973 | -9.4668 | -62.38847 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fceeeb7-8966-31fa-9c52-6e61b544e93e | -8.92892 | -65.94096 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c54a5fc1-9152-3c0e-af3e-a2bdf294e240 | -9.45141 | -65.42365 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1d54cdb-f4e6-307f-9920-2f23a11edd31 | -11.21901 | -55.05545 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb72f2c4-17e9-3b25-b691-0036d8bfe6a2 | -9.70945 | -61.28458 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bef49808-edb7-3fae-bbbb-19bd5c6f8657 | -9.00959 | -65.70843 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a02836-57c8-3081-8a28-ecc29b33d24a | -9.46336 | -60.30877 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab6e9eea-8f45-3e98-9a47-ae9935ece2f2 | -9.51033 | -62.78802 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 736d59fa-4959-3650-9fc3-68d0614c2085 | -9.40648 | -60.51695 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13a5677a-4bd6-37f7-b38d-0d6e4691987c | -8.71924 | -63.75652 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01664be-a98e-3a02-8cd1-a5f5280d44ed | -8.5779 | -63.93145 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce60f51e-82a5-3ee8-a8f0-d271cd7b1889 | -9.73437 | -64.90567 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2592e46d-03b4-3aab-bee8-84f9254bdb8a | -8.99579 | -65.4117 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d496fb8-bd98-3bfc-b795-75819e26c6e1 | -8.95829 | -65.95302 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5389b673-7f1f-3c76-b218-147571b53930 | -8.65619 | -67.26681 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README86.md)
