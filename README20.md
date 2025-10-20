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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b60c266-85b5-3af3-87c2-8a6ca8f1fef6 | -1.74608 | -56.05695 | 2025-10-20 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a85893-80e3-3981-8f4b-64954109d199 | -2.25562 | -51.92235 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eb540f0-8536-346f-83d3-ac8b5fdd1039 | -1.4441 | -49.29865 | 2025-10-20 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad048c58-8e23-3799-9846-32beea001e2d | -2.25175 | -51.91114 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa6b6ae-aff8-35bc-ac91-5cd72fea5e6a | -3.49575 | -55.48179 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9db532d7-d2d6-3451-bad8-3a724ea11723 | -3.13845 | -50.25041 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eede7125-78d5-3a03-8499-8a76c95b1ee5 | -3.14527 | -50.24675 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e802c351-3217-3d1c-880b-507b049a0d23 | -1.44329 | -49.30375 | 2025-10-20 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca49f463-06f6-3bd6-9c97-7724057692f0 | -3.5001 | -55.4824 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c79803-d0af-3a8d-8570-1e46b8638c3e | -2.15228 | -56.65481 | 2025-10-20 05:31:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dce9cbc8-2b35-3562-bc3e-18bf38a7e2cf | -9.64705 | -65.25749 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 988b39aa-1804-328b-bead-d17b611125a5 | -14.19683 | -51.54292 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bce65c87-218d-3362-8e5e-a065ed5f8da2 | -14.18556 | -51.52459 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f3d2091a-0099-3874-8840-fe3c4b271476 | -9.89826 | -64.17438 | 2025-10-20 05:33:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b00ae25-71a2-3b6c-af1a-3d89290ffa83 | -9.67523 | -63.66595 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81aed823-f680-3d00-b429-04d9f3d776db | -14.18375 | -51.54139 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 06232dd6-a855-3e42-958d-4c9cbb3445d4 | -8.36247 | -64.07893 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d49ba6ae-c751-3627-b4b1-dd8e140324fe | -14.19211 | -51.52535 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88551296-dede-3914-9a33-40cf55eaed95 | -14.19332 | -51.51414 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a6c42936-e277-3a07-b21f-7bf74b78cf7b | -14.1956 | -51.53976 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 09d11771-a1e1-354a-b1dd-8a444928bb3f | -9.78113 | -64.16595 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97ded161-87b6-3a5f-890d-c934eb5e0a24 | -9.60964 | -65.26347 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85690e7a-f469-33e8-a9ba-54c833036a79 | -8.63951 | -63.04856 | 2025-10-20 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51fafb0d-1a0a-386f-82bb-55eb4a8071a9 | -12.36642 | -63.88294 | 2025-10-20 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ecb074d-9dd3-3fa9-b81b-ce5543c86e54 | -9.64357 | -65.25322 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6ade4bd-d4ee-3356-aebb-c93fb372874b | -9.61313 | -65.26406 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 104710ea-0905-37d6-9311-775739562385 | -9.62939 | -64.15659 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54141260-207a-35b8-b82c-275b6dce3c80 | -10.63444 | -61.78859 | 2025-10-20 05:33:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe6b0008-1d57-30fa-a2d0-9f3f002fb7dc | -14.20157 | -51.54615 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ca13672-6780-315c-837a-b0cd9756f9e9 | -14.1915 | -51.53095 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 274ca471-38f8-353c-8f90-e58676b58c45 | -9.64706 | -65.25381 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90122a9-b5fb-3ce4-b8d0-81242498e483 | -9.63946 | -65.25652 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38626ebf-aed7-3291-9681-06d1e3044395 | -9.22716 | -63.60814 | 2025-10-20 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e4b13ba-4b69-385e-be4a-c46dd1c8853c | -9.64158 | -64.74477 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22d50814-9dc9-3a85-b210-9b2eaf6252b4 | -9.4867 | -63.36113 | 2025-10-20 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 3f5b3448-0c16-3293-8a09-f11b0d4af415 | -10.63783 | -61.78912 | 2025-10-20 05:33:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c88b219-c352-3b4d-b8fe-bf13639adb16 | -9.76291 | -64.53676 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f65b5b86-e4e2-38af-8e9a-80fbceeb6705 | -14.19731 | -51.52295 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16766283-96b0-31cb-ad21-67cf3c8eb306 | -11.75615 | -61.07582 | 2025-10-20 05:33:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6cec3a9-1e4f-390b-a9c1-085712b000c7 | -8.02612 | -63.88768 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fc8e951-5386-394e-8281-a6027c3ed08c | -8.02621 | -63.89079 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ef0b0e-3208-326e-9d7b-64ba82db9abc | -9.64643 | -65.25769 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e256f472-2bca-3f23-913c-be444d575710 | -14.19788 | -51.51733 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fe46259-833c-34fd-8aa1-1715342a9463 | -8.99255 | -63.63588 | 2025-10-20 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b498d06-4f1b-35b3-8523-b2f4b26b5648 | -8.36586 | -64.07948 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e075dd1-07f8-37dd-aa07-00a19b847014 | -9.64009 | -65.25263 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e26438e1-d8ae-37c5-9c1c-071a8e9a7d21 | -9.64356 | -65.2569 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b02808f-333e-3e2d-80d7-444530094f6b | -9.63755 | -64.74791 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b48e748-1757-3fcd-94c2-f8259e84911e | -8.02554 | -63.89129 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89901601-c866-34d1-bea2-e45afa4dce37 | -14.19845 | -51.51171 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7182734-0257-3d12-b165-1bc219ced094 | -10.05364 | -63.85807 | 2025-10-20 05:33:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d89c5a1-883f-3714-86a1-1b4ec38e0d81 | -14.1909 | -51.53654 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| adafe7b4-b5c5-335a-858d-c193be43cbf8 | -8.03017 | -63.88773 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb31220a-f387-3cf5-8dfd-87232b7026b2 | -8.64229 | -63.0526 | 2025-10-20 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 190ab745-57cc-32d8-ae36-eeac37ac1b2e | -14.19987 | -51.5149 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3bbcccc-94bf-36e4-8351-34c27254f60d | -14.19503 | -51.54538 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10da0205-c8fb-3f82-b902-a02ecad4177a | -9.69136 | -63.30729 | 2025-10-20 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa24699-6739-38cb-95d8-36925806ffa5 | -10.61182 | -63.49596 | 2025-10-20 05:33:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6fb8ba8c-c9e9-31a6-b816-ac7e38efd102 | -9.62602 | -64.15604 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57c8cd20-9f7c-384a-860a-2d8f44fa211a | -9.11975 | -65.36278 | 2025-10-20 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbe3ebed-2b2c-36c8-b89d-cc3eefc5cd98 | -9.26603 | -63.34329 | 2025-10-20 05:33:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b29539a-e012-3138-9b5c-c605a4eebc10 | -9.89487 | -63.58526 | 2025-10-20 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffa61921-4308-3211-a627-4df2960a507b | -14.20271 | -51.53495 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 071f6d4b-eb44-3f81-939b-efd65a5d7f86 | -14.19271 | -51.51975 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7cee2a6e-855c-31a6-91bb-7eb68dc89ed3 | -14.20214 | -51.54055 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 637f93c9-8782-3666-8d14-2b5b80e7ae7d | -9.6422 | -64.74104 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ef62c17-77a6-3c4f-bfac-29374a7b403e | -9.62423 | -65.26193 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90b7599f-3837-311c-8e03-25d384913e23 | -8.99219 | -65.90274 | 2025-10-20 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b11ea3ea-8bd2-3c83-9603-54366dac2848 | -14.19617 | -51.53415 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ac5e47a-5509-38ef-8ca9-31e69e554b8a | -9.74833 | -64.19763 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28d5d809-01db-3a34-b028-682189e751d0 | -9.64053 | -64.17323 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1863d98b-5297-33cd-92d2-a8c0f10dd66c | -12.36918 | -63.88704 | 2025-10-20 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e081bdba-5a1e-34bf-9e5c-2ac319b7f4c0 | -9.89821 | -63.58581 | 2025-10-20 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae06dc7b-dce1-3d29-b326-3e0f8d4a91e4 | -9.76305 | -64.53666 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6b752f3-a0e9-375e-9d22-362808e05bf1 | -9.64623 | -64.73788 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e5629388-80bf-384b-8602-c847c84e2e9c | -14.19674 | -51.52854 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1980ca36-df22-38f1-8cbb-8fe44a585d3d | -9.63816 | -64.74419 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1df277f9-391d-3153-9723-2580725373ef | -9.64281 | -64.7373 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d7ef96ea-b01d-35c8-9c54-8e2fed1d7e84 | -9.8886 | -67.43315 | 2025-10-20 05:33:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ea21c5b-3459-32e1-8677-48b5c4a99e5c | -14.18496 | -51.53019 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 67eb5044-d446-3faa-8aea-e0783c83ab4f | -9.64342 | -64.7336 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de7c39bf-61f2-3fd8-9819-d8820200f8a5 | -14.20501 | -51.51249 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48a31eb2-1566-3238-8d87-bf6bdda223e1 | -9.72121 | -65.87547 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cf27ce9-fed8-35e1-893f-4edc2e22033b | -9.64421 | -65.25304 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7078d6bc-37c8-3830-852c-e13fdab8138c | -8.0268 | -63.88718 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87ffd868-1807-3e3c-9a07-e76e8561aa1e | -8.36644 | -64.07584 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6db9b2-7e30-31d7-a1db-75cce370f6b8 | -9.64684 | -64.73418 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63310e9b-59ea-336f-b024-b8cefba8c6fc | -9.63877 | -64.74046 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92d2261b-b0e9-332a-8bbf-9714f7b8e74a | -14.18436 | -51.53578 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 523b2881-9a73-3d1b-a1f9-d6d8f0194983 | -9.89489 | -64.17381 | 2025-10-20 05:33:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d90d4f6-76ec-3fc8-bd5a-5fcfdf0f4891 | -8.63896 | -63.05206 | 2025-10-20 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00cfbf5a-ebc0-3a9f-9545-b1d972759df8 | -9.73618 | -64.89144 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3570c988-a5a4-388c-9d51-9e4fdd28f54b | -9.90544 | -63.58336 | 2025-10-20 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409def14-f31d-3879-a993-541079fb1f21 | -8.02274 | -63.88713 | 2025-10-20 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a99916-cd98-3264-a38d-3307e3055ed6 | -9.11623 | -65.36218 | 2025-10-20 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2e7f794-ae4e-307c-a79c-bdeba8abe87e | -9.11558 | -65.36613 | 2025-10-20 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b43958a2-bc7e-322c-bda6-268d05b26328 | -14.19029 | -51.54215 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 764bde24-92d7-349e-91b5-c932ba234ad2 | -9.11206 | -65.36554 | 2025-10-20 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb790165-74ff-3e0f-93b6-9f4c90b9d03d | -9.7303 | -64.94865 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0408c1e-e976-318d-a652-9088904d9967 | -10.59409 | -63.47866 | 2025-10-20 05:33:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
