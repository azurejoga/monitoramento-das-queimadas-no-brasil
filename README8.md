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
| 274faa8e-4828-3522-b76c-3c9038861d7c | -12.9292 | -54.7538 | 2025-09-12 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ff8ec84e-b663-3255-b258-925e365a0459 | -21.6296 | -53.9704 | 2025-09-12 00:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 8902ba58-59ac-3fa9-afb1-13872750876f | -21.6291 | -53.9923 | 2025-09-12 00:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 389abc6c-ef09-3a0d-93a1-f4c0a94ed1df | -11.9717 | -51.1427 | 2025-09-12 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8ceb9f55-3a91-3944-91eb-1e152e9a0e82 | -11.8757 | -58.8221 | 2025-09-12 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9c18bf39-7ede-3d5e-9a7e-2fef2b23aa1c | -12.8839 | -62.1256 | 2025-09-12 00:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 947abd6a-acf5-3a66-83ef-74317e3dd5aa | -20.3639 | -48.4019 | 2025-09-12 00:30:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c260eafe-251f-33de-951f-3de8210bb7fa | 2.5064 | -61.039 | 2025-09-12 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 32c8c565-0b44-3c96-9afc-7700106d97d3 | -15.1058 | -47.9983 | 2025-09-12 00:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d387e9f4-3741-36c1-8afa-3e6473205cf9 | -23.1146 | -47.4915 | 2025-09-12 00:30:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| 8dd229ed-9cb4-35af-a40d-89d6299759bb | -12.846 | -62.128 | 2025-09-12 00:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b670191e-0722-393d-a536-93119209e0c5 | -21.947 | -47.5578 | 2025-09-12 00:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 51c5dce8-a291-3f37-b4cf-898582c2293f | -11.7012 | -46.5605 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| cff20162-07d9-3477-9408-6ac59900cf2c | -12.8837 | -62.1449 | 2025-09-12 00:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f8d1cace-3089-3279-996f-50e6a1ae0fef | -11.6828 | -46.5179 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| f56540be-df82-30a0-8c87-cef898d56ba9 | -20.4052 | -49.1278 | 2025-09-12 00:30:00 | GOES-19 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 4ce2e400-7553-3bf1-b701-8f1c3e369ef6 | -9.2287 | -59.3823 | 2025-09-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4c6230d7-e3b1-302e-8e1f-9c7a7eabb038 | -8.9563 | -46.0849 | 2025-09-12 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 975abfe2-a8df-357b-aee1-d7b0569490b9 | -9.057 | -47.0355 | 2025-09-12 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ae1a2c42-1c3c-3423-95a1-8924fcb9d132 | -11.702 | -46.5153 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e6987f47-5202-33ea-b019-68626affdeef | -11.6821 | -46.5632 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6aada62f-e7d4-37d8-b223-fa86b8d9126e | -6.3092 | -42.2072 | 2025-09-12 00:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 7e78f9f3-f074-35bb-b317-8f3c95ceecfb | -8.8899 | -49.945 | 2025-09-12 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| c130753a-b7e3-371c-a894-ab30d4b77dbc | 2.5064 | -61.0201 | 2025-09-12 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f96b6cb8-f893-3443-8ee1-b6d57a63b5e0 | -6.309 | -42.2311 | 2025-09-12 00:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| ab18c7ad-fb2e-3814-a175-a7559fdb5d16 | -9.5137 | -54.6292 | 2025-09-12 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0d437a8c-e88d-3759-9b2c-9d04e7552a6e | -9.0175 | -45.7397 | 2025-09-12 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 835bf909-b286-3185-9943-246c64e0602a | -8.9087 | -49.9433 | 2025-09-12 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ac90980c-916e-374a-9cf2-01fc7a4ce4ec | -17.3372 | -46.6718 | 2025-09-12 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a273ed4b-8e40-3dd1-91f0-cda01b1671cc | -21.6496 | -53.9886 | 2025-09-12 00:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 55802f50-6576-34e6-93a7-fe9710ffc532 | -12.8647 | -62.1461 | 2025-09-12 00:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f138eccb-dccf-3eff-a263-122473921b3c | -23.1358 | -47.4859 | 2025-09-12 00:30:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| 9477fc25-d436-3d80-86cf-5f6bcf4d6e95 | -21.9679 | -47.5525 | 2025-09-12 00:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 21f4c3f6-bb89-3b9d-a50c-293135ca5a6e | -23.1139 | -47.5156 | 2025-09-12 00:30:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| 8d679b7d-4e84-3f38-b35a-4c72e8326d66 | -11.6825 | -46.5406 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5b85e042-d1e0-3556-b552-b250beeed110 | -8.8901 | -49.9236 | 2025-09-12 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| b7dc7cd9-861e-3e8d-8fad-73e19a67c972 | -20.0192 | -47.6459 | 2025-09-12 00:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 435d8db5-e7ed-3145-8ea6-754398894f91 | -11.1809 | -55.0821 | 2025-09-12 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9b11418c-cacd-3a32-baf1-4b406f5cd356 | -21.9686 | -47.5287 | 2025-09-12 00:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 93e7fb60-5c41-33b7-b8d4-6a7e1c37ecc8 | -9.2101 | -59.3833 | 2025-09-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| c49a0279-1962-3e8d-b147-07edea7686fe | -11.7016 | -46.5379 | 2025-09-12 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 106143d3-bdc2-3a56-a1f0-46ffc0ccbdbc | -13.3238 | -44.0945 | 2025-09-12 00:30:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9f5ec3b9-b780-34ed-8e95-d1753ecbd85a | -15.1053 | -48.0209 | 2025-09-12 00:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c3784982-6014-3ed1-8a7c-ced7fdfa168b | -12.8649 | -62.1268 | 2025-09-12 00:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8ecf357a-716b-36fd-bf31-122524cfc013 | -12.8839 | -62.1256 | 2025-09-12 00:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 28b594ff-3d40-3ca5-bf39-28355a0b953d | -11.7012 | -46.5605 | 2025-09-12 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 703234a4-0aba-39e8-80f0-6bef5f50bc62 | -8.1837 | -46.0965 | 2025-09-12 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a43ba589-20ff-3b92-b984-5d59cca652a7 | -19.1813 | -47.9932 | 2025-09-12 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f77132d8-c2c4-3c2f-962b-4b8a49f08fac | 2.5247 | -61.0198 | 2025-09-12 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 088edd6a-c93c-32a3-b6d2-319c82b8fac2 | -21.9679 | -47.5525 | 2025-09-12 00:40:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 190.8 |
| f716991f-696f-3724-93b4-d81e02e75a52 | -11.6825 | -46.5406 | 2025-09-12 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3bae5bd0-a42a-34fe-8895-99deab54001b | -6.309 | -42.2311 | 2025-09-12 00:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| d474cd5b-f3e6-3392-889a-fedd86408cdf | -9.5137 | -54.6292 | 2025-09-12 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b0a5c1e5-7220-3624-977e-1f67607dc8b8 | -11.0201 | -51.3521 | 2025-09-12 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e97e80db-4d26-352b-9668-6278489dc5b3 | -20.0192 | -47.6459 | 2025-09-12 00:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6b3dbf9e-5ccc-3b62-9ba8-8563126226d9 | -12.846 | -62.128 | 2025-09-12 00:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e8990caa-40e1-3874-abb9-bbe71bb398dd | -11.9717 | -51.1427 | 2025-09-12 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1ed82150-2786-3b34-8eec-cf37c50040eb | -11.8757 | -58.8221 | 2025-09-12 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 558039d2-5293-3286-a930-583b786bb49e | -9.2287 | -59.3823 | 2025-09-12 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| f197fdac-40ec-3899-ae70-92cd3e43cb04 | -12.8647 | -62.1461 | 2025-09-12 00:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3f2da40c-c06d-33f2-b356-0b4b741b700a | -11.6821 | -46.5632 | 2025-09-12 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| c779fb88-425c-324d-9109-149aba30a543 | 2.5064 | -61.0201 | 2025-09-12 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| cd751525-29bf-3efd-99ce-2566f894c12b | -21.947 | -47.5578 | 2025-09-12 00:40:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 422fffbf-306b-3c36-929c-afe19228e1e8 | -8.8901 | -49.9236 | 2025-09-12 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f10bd874-88e8-3b6e-995b-f9be7f85a03c | -13.3238 | -44.0945 | 2025-09-12 00:40:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9df22ac2-c083-3598-864d-32ee459a04e5 | 2.5064 | -61.039 | 2025-09-12 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5ab12703-aa45-34b7-86f1-2c0561804559 | -6.3092 | -42.2072 | 2025-09-12 00:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 18f96726-488b-3093-b99a-7bc79a0958cd | -23.1358 | -47.4859 | 2025-09-12 00:40:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 061ceb12-f6d9-33a7-adb3-6e40989a6b34 | -9.0379 | -47.0597 | 2025-09-12 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3824b688-01d8-3045-b8f5-6a1582fa445d | -20.4052 | -49.1278 | 2025-09-12 00:40:00 | GOES-19 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| a3e26009-48bd-3b7a-bd5c-aa19d1f1f05f | -23.1146 | -47.4915 | 2025-09-12 00:40:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 97784ac3-4c7b-34c2-b50b-fee1c351a78b | -6.2902 | -42.2327 | 2025-09-12 00:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| ad394a02-1563-3af3-9efe-2954b2136060 | -8.9563 | -46.0849 | 2025-09-12 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 2d17d0e5-e8b2-3cbe-b27b-7900c12f6747 | -11.7016 | -46.5379 | 2025-09-12 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| cad611be-cac1-3be2-bce4-adfe9e21702a | -11.702 | -46.5153 | 2025-09-12 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1728db77-56f9-33f0-b4f4-4ba05a503ebf | -19.1807 | -48.0164 | 2025-09-12 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9d535832-bd8b-30bd-86ad-2f8dd39619ef | -9.057 | -47.0355 | 2025-09-12 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f78a319c-175e-318c-9951-366c796ec487 | -23.1139 | -47.5156 | 2025-09-12 00:40:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 6a1fca31-a02c-3d5e-88ec-734716798680 | -21.9686 | -47.5287 | 2025-09-12 00:40:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6ec73e47-12db-3919-9829-94cd79bc1f65 | -22.6404 | -53.0946 | 2025-09-12 00:40:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 9a55880b-404e-3cd0-8388-ec6ad98e027c | -12.9292 | -54.7538 | 2025-09-12 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 2fe529a7-eb12-3f1c-a3be-1e413f98d49b | -8.8899 | -49.945 | 2025-09-12 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| b5b45641-5461-392f-b8d1-2250d9f69c89 | -14.2685 | -54.7743 | 2025-09-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f6b4087b-123b-3a37-bbf5-f84b1b9de7e1 | -9.0379 | -47.0597 | 2025-09-12 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a6e319cd-d0e5-392d-94b6-b78aca262723 | -11.5235 | -50.5968 | 2025-09-12 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 11219b19-dfe8-3fbe-86d7-6953ccc0cc93 | -12.846 | -62.128 | 2025-09-12 00:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| be960e84-5ea0-3c5c-aba9-60988119bf0d | -6.3092 | -42.2072 | 2025-09-12 00:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 4cec9096-e574-3825-a5a3-62d3e1e10bbb | -11.8757 | -58.8221 | 2025-09-12 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| bd478fe3-6062-3855-ab51-1c398bc0147e | 2.5064 | -61.039 | 2025-09-12 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f697b031-8f78-338e-a6cd-63b201efd983 | -14.2682 | -54.7949 | 2025-09-12 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a396752a-0ccb-30c2-be67-1406a1e190c1 | -8.8899 | -49.945 | 2025-09-12 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| e88fdab6-d86a-33c8-a548-4a526cc9575f | -9.0376 | -47.0819 | 2025-09-12 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 48710e4b-5659-305c-b4eb-141ae7604881 | -11.9717 | -51.1427 | 2025-09-12 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c7fe218d-e5dd-337e-93fb-92533666daa5 | -11.7016 | -46.5379 | 2025-09-12 00:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 24d27b56-0374-3431-a3c2-e0f87c1ad7a7 | -11.6825 | -46.5406 | 2025-09-12 00:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| cc665f5f-f0e9-386f-bad2-2bfbdeb8b8ad | -21.9478 | -47.534 | 2025-09-12 00:50:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1dc6fd3d-aca5-3f03-8efe-fb2258969400 | -21.6496 | -53.9886 | 2025-09-12 00:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 35cbc886-9081-3988-8c0d-eba3e32a84ba | -16.6133 | -49.7939 | 2025-09-12 00:50:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 1ae5da2a-b2ea-32a0-85ba-7af28e01f136 | -12.8286 | -61.9551 | 2025-09-12 00:50:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3e910e63-b1c0-3bed-8c14-ff14e76ae54c | -16.5099 | -55.1459 | 2025-09-12 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |


[Clique aqui para ver as próximas entradas](README9.md)
