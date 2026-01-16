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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 561d3678-e963-3749-b5f0-8d6ae25d0b1d | -14.47706 | -44.3305 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb33ac4d-e18b-3780-9cf0-1f347d825e84 | -10.74023 | -48.69172 | 2026-01-16 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fa4215e-26f3-3b56-bb8a-2bc3f33ad0ad | -11.16009 | -43.57677 | 2026-01-16 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3144b5c-fba7-3502-9533-5cabba9d982f | -10.74368 | -48.69218 | 2026-01-16 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3d4ac2-d146-3c16-9a75-039306ce5005 | -13.69368 | -52.60316 | 2026-01-16 04:46:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e2a0d2c-b059-3eba-a01a-4502006654ab | -12.65219 | -46.75325 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| efc110ba-de6d-37d0-9765-acd3cde96ce9 | -11.12937 | -43.53623 | 2026-01-16 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da9c081a-50ca-36d4-96c6-27a7fb6c0beb | -14.20768 | -57.40397 | 2026-01-16 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c59013e0-9ad4-323f-82a9-bcc545205e3f | -14.47642 | -44.3354 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5548ab9f-20a9-3b79-b6dc-8f5189c64c4c | -12.65281 | -46.76014 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 32217e51-af32-3a18-a3f8-e85b586e8600 | -11.83776 | -49.19303 | 2026-01-16 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed984a2-7694-3c71-a1ff-f0fdbdeffb71 | -12.46586 | -47.81774 | 2026-01-16 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9daa2ec7-8c77-3694-8423-3493fe381409 | -11.74579 | -48.51925 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a106f4-5b3e-3e35-8442-3e19608089ff | -11.74644 | -48.52238 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eeec097-bd1c-33a8-b815-dc9cc2b0e86b | -12.08472 | -43.76595 | 2026-01-16 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6307c4f-164a-32b6-8fab-4a260a3738bd | -11.16122 | -43.58026 | 2026-01-16 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54817cc5-a975-3ef1-86e2-995e733c687c | -11.95525 | -44.2112 | 2026-01-16 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfce4c6f-a5e4-3714-874e-4735663608e9 | -12.64896 | -46.75957 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a65ae7c4-7119-379f-9c2a-b7fe1bfd5d90 | -13.69428 | -52.59949 | 2026-01-16 04:46:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28bdeeb0-7447-34f5-bc8c-29f8574c2ae2 | -12.64963 | -46.75471 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b6aac912-4cac-30bd-8ba4-b6a341dc6196 | -12.92218 | -49.48787 | 2026-01-16 04:46:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| edbc0cd9-d242-38d0-9080-b36a81914386 | -14.77536 | -45.9406 | 2026-01-16 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a33e567-c2cf-3d20-bda1-98bad8d1aab1 | -12.6761 | -46.64913 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab2d0fa2-42e3-37d2-9e63-68978772f0c7 | -12.91934 | -49.4836 | 2026-01-16 04:46:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433f856a-fa5e-3bf0-9361-f61dc63b98ef | -12.14172 | -45.5834 | 2026-01-16 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88eb9371-5f17-3979-9ba9-78ccd796372d | -12.66367 | -46.76672 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ee4d37a-830a-3080-a5c9-158798c38da9 | -14.91634 | -46.3893 | 2026-01-16 04:46:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ca95c3-9215-3c93-bfa8-475507fd5bec | -12.14225 | -45.57966 | 2026-01-16 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d53c616-d27a-369d-a264-ae9d8c70a7f3 | -12.65801 | -46.75098 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ce9f544-5496-3349-93d2-2bb6d357e7fa | -9.37673 | -47.08463 | 2026-01-16 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba4b9d6f-312c-38ea-95d7-eefd923e16e6 | -12.65149 | -46.75811 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3fc70378-c9c9-3c45-bca9-3d9fe5f9170c | -14.77224 | -45.93225 | 2026-01-16 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8685c5c9-fd9b-3f45-9d4a-2c81abd9f7ae | -11.83662 | -49.20047 | 2026-01-16 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e43d3a6c-e08e-3e8a-95ac-eb38e6494604 | -13.69766 | -52.60007 | 2026-01-16 04:46:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ef0f7f4-9288-36e8-924e-52eb9a420b90 | -15.45233 | -43.16863 | 2026-01-16 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad8c43cc-9c15-3425-8123-d28eeb114b51 | -12.65604 | -46.75381 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6287be35-4d83-3bbb-aa57-cef3c1cba94b | -12.49627 | -46.34363 | 2026-01-16 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceaf71bb-d936-3ada-9276-dd720801167e | -12.64764 | -46.75756 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f51f2605-0687-36f7-88c7-f1a9ac88e8fb | -11.83719 | -49.19675 | 2026-01-16 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4471371-decf-34e1-9049-c997e3bc34ab | -15.44726 | -43.16795 | 2026-01-16 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 930e16c4-74b4-38bf-b894-061e92c59148 | -8.72612 | -48.31944 | 2026-01-16 04:46:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7703ac6-b51b-3570-8acf-3a6129e9e1f3 | -12.68066 | -46.64479 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 803c31ea-5b66-3ae3-ac2f-f4d31d2ffa79 | -12.18222 | -48.46641 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cc8b6ac-3a25-3497-910c-4a0ae73a43ea | -12.49927 | -46.34579 | 2026-01-16 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 091892d4-0b80-3d32-8408-35057a6c7518 | -14.48104 | -44.33598 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7609f3e9-c8d1-3e64-b4c2-8edd6e6769b1 | -12.65348 | -46.75526 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e154f25d-da45-381d-a681-42bb3d84ed44 | -12.085 | -45.28481 | 2026-01-16 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 859355c6-0700-37a4-8fa4-3a9948dd1273 | -14.48169 | -44.33108 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c925c307-57eb-37f6-aa61-4e1c2c652c0d | -12.18227 | -48.46939 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e166e461-0746-3a86-b8c8-a3c1d9e8101a | -14.76859 | -45.92778 | 2026-01-16 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd43dfdd-e4d1-3367-813d-3c39b3039870 | -14.77172 | -45.93612 | 2026-01-16 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd95f253-6128-3d05-8263-cb8ac5b1f702 | -12.08392 | -45.2925 | 2026-01-16 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89c8aac1-4ba7-3423-8d59-1ca0a415017c | -12.92274 | -49.48414 | 2026-01-16 04:46:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 058f5919-bb78-3a99-bce4-e828c93659aa | -11.83378 | -49.1962 | 2026-01-16 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4baab31-a4d6-335f-8d4a-fa3f59226db2 | -12.65534 | -46.75867 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b8d538e-d0c5-35d1-8183-d63dd8573343 | -8.7267 | -48.31572 | 2026-01-16 04:46:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96974901-96ad-399c-8a31-a913d26dee0e | -14.76807 | -45.93166 | 2026-01-16 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 328ab54d-7118-3b54-bc39-2e36fc04f841 | -16.65919 | -43.35175 | 2026-01-16 04:46:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b23120-c0dd-362c-bff3-514d24aa9717 | -10.35754 | -48.91116 | 2026-01-16 04:46:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dac4bed8-b09e-3500-b0b2-0d09b62c7f6e | -12.65598 | -46.76555 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f213a5-64ff-3af9-8e43-bd1ed44a4aa1 | -12.08227 | -43.76694 | 2026-01-16 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e94852a-d321-37df-b898-88b635563afe | -14.20341 | -57.40317 | 2026-01-16 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59f09d7e-35f4-3d2b-84ec-3e4ec09e4321 | -10.73678 | -48.69125 | 2026-01-16 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f76c4648-63d4-30bf-bb16-d3bfc251123c | -12.08446 | -45.28865 | 2026-01-16 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7136f5cf-e628-34b8-8b92-3f3810d080fc | -13.43267 | -43.85747 | 2026-01-16 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92e8a417-5070-3f7b-82b7-4e11c2d79274 | -14.47572 | -44.33205 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0c5603d-57e6-3a19-95bd-b4c1a1c570d7 | -12.65983 | -46.76614 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecce02b4-8942-3229-9e5f-64979639c747 | -12.08691 | -43.76769 | 2026-01-16 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04537708-f3c8-3b8e-8bbf-a7c7056da5ec | -12.91877 | -49.48732 | 2026-01-16 04:46:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0208851f-d6c0-3836-9f03-53e8adf83076 | -10.21577 | -48.30958 | 2026-01-16 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1bb12c7-4233-366d-a275-1737d1229036 | -14.20693 | -57.40804 | 2026-01-16 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d3e5c1c-385f-3885-85cf-3c5f4473205b | -15.6198 | -56.15426 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc057126-a172-37e8-b367-5b8756f45d11 | -18.81834 | -51.61642 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a615a496-d63e-372f-9413-f730d5d656a0 | -15.58983 | -57.3403 | 2026-01-16 04:48:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e21ed0-86d0-33b3-aeb3-dc2eae49f03f | -15.42844 | -56.32632 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39790b91-f0d4-33e9-8b5e-9c12294f7d38 | -20.42709 | -57.85383 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1020b3b9-51cb-386a-a498-013082b8e96f | -17.61329 | -46.65712 | 2026-01-16 04:48:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d553e158-8984-3122-ab83-fe17d8c545d7 | -18.8167 | -51.60473 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f0d3a13-3573-3519-9233-849ad70204da | -17.62205 | -50.3563 | 2026-01-16 04:48:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef4b215-245e-3843-9277-773da6ae27cc | -18.81499 | -51.61584 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0ac3e6-a905-359d-a9a0-c692ed4f66a8 | -20.44584 | -57.84116 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cb7579e7-b9f4-3fbf-a307-e837d60658b9 | -20.43896 | -57.83416 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f55331b9-64a4-3686-a4a8-c90a7f16cbe9 | -15.43845 | -56.33542 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93034b48-cc0f-3456-bfee-a20cd201ad07 | -20.72836 | -55.16446 | 2026-01-16 04:48:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 332581f2-6f74-33e9-93fb-d65ac8b84645 | -19.17342 | -57.54121 | 2026-01-16 04:48:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a81a83a0-7a25-3573-b918-d43c59b97212 | -16.26357 | -56.88364 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 345e190c-d297-3796-8696-564ae9ee9b4a | -16.25959 | -56.88287 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07560d7f-8dc0-3279-9f1a-bb135c555d30 | -18.80943 | -51.60728 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a358adbb-75b8-3808-872a-c2c6ae79bc82 | -15.43938 | -56.33037 | 2026-01-16 04:48:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19aa5c0c-9ba3-35f4-a1ff-e26bddedeb73 | -20.4429 | -57.835 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ba723e85-406b-34f2-a958-692d0cab6150 | -18.82063 | -51.60159 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 123be5fe-8736-3973-93e0-b8c7019a3139 | -20.43797 | -57.83949 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 517b96a8-909f-3337-bc61-e711621c7c0c | -20.43209 | -57.82718 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 067679b7-7cd1-3aa4-9a94-da8999df7917 | -15.77674 | -55.7543 | 2026-01-16 04:48:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da787ad3-9be3-31f1-a0c9-17cd85477cc9 | -18.80886 | -51.61098 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f1502d6-ec9f-3ff2-8188-a8ad4f9bf42b | -18.81727 | -51.60102 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f551e9a-4704-3ebd-b70a-abb4d08c7806 | -18.8284 | -51.61813 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bc923df-6def-3793-86ea-cffa0dcfd79c | -20.44191 | -57.84033 | 2026-01-16 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 64a91d78-9098-3440-9965-93c280348b73 | -16.10188 | -56.7605 | 2026-01-16 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b12e92ed-fe3b-3a9d-9a43-55c8f016af67 | -18.81949 | -51.60901 | 2026-01-16 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README9.md)
