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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d378561-3963-35e8-99c2-e8f5378a3181 | -5.25295 | -57.12165 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0bac66e-d2e6-3f3c-bb7f-fc45e66c4ef3 | -7.39758 | -61.62582 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0cabe81-76e2-3b86-9f99-4b33e200f89f | -9.20152 | -67.561 | 2025-09-08 05:21:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c9c74c-5ee4-344a-b546-8ac58884d2c2 | -7.40398 | -61.63089 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c8512751-37b4-3112-974d-265225bb36e1 | -10.51091 | -57.79645 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf5531f-d64b-3306-8c1b-a265670cebcf | -9.79632 | -59.80697 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58219f2f-259b-383d-b3ca-18ffa12e9d62 | -11.1948 | -55.0073 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 963a56da-72e8-3e36-8667-0a7db937b99c | -12.94898 | -54.80782 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50ce5b94-b1d6-3882-af92-c2d11322db4c | -6.84359 | -52.85783 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669bc6f8-6bbf-3cb8-a0b5-a969744884fb | -11.19983 | -55.00085 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5de455b-790f-35ba-9b9f-561ef0949739 | -12.92752 | -54.77713 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69d7518a-2a4a-3f09-8ffb-5790f3a26cec | -9.20674 | -46.045 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 193818ef-30c4-3d38-8273-d45e7704dc6b | -10.2986 | -48.81117 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fad251e0-6686-358e-a640-071397a8884e | -9.47794 | -60.4883 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a7210d-212b-30d8-a01d-2ce958417064 | -11.41093 | -50.3953 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d45ff57b-67c0-37f4-9369-dcd23c3b7cda | -9.2028 | -46.03576 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| db89bb59-1c82-3c32-bf50-9bee8eb029ed | -10.00276 | -51.65638 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5adec7fa-f937-363c-855e-1d9d1c79dc24 | -10.45775 | -53.62823 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76d9ca48-b73a-3c5f-96e1-264f9290aded | -10.57965 | -61.2579 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20eb8b09-1bd7-32d7-b678-dadb6459e0f7 | -11.89409 | -50.96335 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d82ae58e-33a6-33a8-9ef8-e3abb418edfa | -6.81175 | -52.82898 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 618789e3-353d-39d2-8710-80b7ee457d97 | -7.42843 | -49.25667 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01bda2b0-5d28-355e-993c-ccb9dcfb6182 | -12.95429 | -54.76902 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e541eccc-a790-3065-ba17-c03eebd554d0 | -9.13004 | -65.9603 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 018922c0-cfde-3f9a-9dc3-22589b4d6132 | -9.58729 | -48.29406 | 2025-09-08 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 429232d4-b32f-3734-a00d-d777307bd581 | -11.41418 | -50.36979 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a41c442b-b1f6-3665-ad77-e1950873bc2b | -9.33158 | -55.19592 | 2025-09-08 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74612d91-67bd-3c7f-be5c-ed3d3dcc005f | -11.38057 | -50.41347 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 652ff2bb-ebf4-3fb7-a23f-981f1fe0e15a | -12.94848 | -54.78021 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46377935-489e-3c2e-9a8a-395adc386966 | -9.9336 | -60.09888 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4140bc59-6e57-3952-83ea-caa195537f5e | -10.14899 | -61.1353 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 026a8c44-e42c-3493-ad08-b1701104302c | -9.0662 | -60.48367 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c98fe8a-128f-3ceb-9a1f-72a9b2946080 | -7.66151 | -47.94584 | 2025-09-08 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 975a73fc-227b-3f16-865c-7bc48f47c86a | -9.35737 | -65.42535 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfa56af2-d7df-3da6-8cf9-0dc73826f561 | -9.95194 | -51.19047 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27b92e58-1130-3b20-93c4-19e8e55de125 | -12.938 | -54.79443 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8fe4808f-4ba2-3d14-93a5-228e229f128f | -10.77306 | -59.85589 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b319783-ccc5-31d6-970b-ac8b6a71ce96 | -9.48014 | -60.49596 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e794922f-adff-309e-b1f0-3e0a2bca522e | -6.62312 | -53.34943 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1475e4c7-9e35-3db2-a391-bffed4492bb0 | -6.63517 | -53.35515 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6071fa-0f01-345a-a64b-812d41a08cba | -10.00642 | -51.63396 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056bad89-99d2-3078-be55-0ec0f0bb5e68 | -9.88872 | -56.14333 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebee2d5a-62a7-30e5-8c46-8158c284716f | -10.47386 | -53.60903 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70b6874-86b6-3337-8818-64870675f2c6 | -6.54889 | -54.99363 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1d48d51-fa35-34bb-aeb4-fcc83c9418ee | -9.96532 | -51.20808 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd7b7f1b-c0dd-36ca-922f-9be13be668fb | -12.62734 | -56.97706 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 84df07a5-ce13-3194-bb7a-cbb945c86422 | -11.22302 | -55.01147 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d26b46-d0d5-3f53-aa34-c82ff9c8c541 | -10.27229 | -63.17047 | 2025-09-08 05:21:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 018324f7-4f70-306e-86aa-c847a498b8db | -11.20688 | -55.00919 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad819b99-9a40-3210-a2c7-2b200cf6f291 | -10.4661 | -53.63176 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daec1ac5-88fd-3638-8273-1d3536e6c886 | -11.03524 | -45.94427 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 982a9180-bf96-3663-b8e2-ffeda1d5d931 | -9.35312 | -65.42462 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efb37dab-bc98-3e7c-98f1-6d8a39150486 | -9.78557 | -48.34114 | 2025-09-08 05:21:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04ce1565-7cb2-34ee-a40a-5fa9fcd32f2c | -6.95775 | -62.92668 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1501561b-9501-3a1b-a597-a89cb1fd167f | -12.64199 | -56.97922 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c62cae3-6f20-351e-b066-473fe90bc5bc | -12.94376 | -54.7835 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999927e7-9360-3d3d-91aa-4dcccb17768b | -9.88202 | -46.53165 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb32f251-7413-392a-8409-842b5148d899 | -13.73531 | -46.90367 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a634b997-49e8-3b14-9df0-53dd5a3aed60 | -12.83416 | -52.94065 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bd80bfee-1b46-3c2e-b62b-605bf3f9f712 | -9.97488 | -51.68195 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d256a7-eafc-3666-b9c5-ca03ee1ea8e5 | -6.62809 | -53.37378 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0c99e56-71dd-3b73-acf0-9f74e44ba3fc | -11.89137 | -50.96512 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 191a819b-6576-333a-aff1-c794c5c5309c | -10.29334 | -48.8042 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 65cc20c6-4ebe-3fe3-aeb7-2cfdfbc61695 | -6.82049 | -52.80013 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c5928c9-d5cd-3ee9-b8ab-e0b8319a54ee | -12.19649 | -53.90429 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9623a29-d18a-350a-9290-cc17d36d4d1d | -9.96569 | -51.20526 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 277f5b1e-ed7b-3220-a465-7c646d563006 | -6.84478 | -52.84949 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5fce1ff-81ad-3658-99cf-c512a1adc2f8 | -6.63344 | -53.36673 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e58ec9e-1340-3cc0-817f-ef65f22eaaef | -11.18829 | -55.05335 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7a1b07e-195e-30c4-bc0d-63d4e729efba | -9.20054 | -60.62324 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44bc6505-dce5-3354-9f0c-a03b8b7a160d | -6.82056 | -51.8776 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f824457-a380-3b22-8176-f9a2685c4ee8 | -12.95003 | -54.80013 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be90457d-c063-3ce4-8db5-6eeb0d63f274 | -10.51148 | -57.8047 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b9ac526-8637-3962-ae0e-10d8c6a03f7b | -6.83307 | -52.80585 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ff25d0-14a1-3167-afbc-26aefe62e187 | -6.27924 | -53.43006 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f54a213b-c53d-35cc-85c0-60db0dd2cbbc | -13.81223 | -46.2809 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38b5103a-d60f-3fde-add5-f60516b0d849 | -10.50977 | -57.80408 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a60ab4e-8f2e-35f3-841d-1579661487ce | -6.5451 | -54.99307 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5703f666-ef38-3881-8e24-755e3a3604f4 | -12.62002 | -56.97595 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ba13673-5428-30ec-a3d5-ac87b4a4bd28 | -12.95161 | -54.78859 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f04509-db27-3196-9dbd-178ecc5990b8 | -9.86804 | -46.59202 | 2025-09-08 05:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd2b271a-fe5a-3203-9178-fafb6635ed2c | -12.60905 | -56.97423 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 348d8ea2-9237-3b64-b92d-0092ac847591 | -9.73446 | -63.42988 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bccf3d0e-d28b-3dd4-8f41-b60aabc6b648 | -10.349 | -57.50551 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b505354e-4825-3fc2-add8-3d7e6bc316f9 | -6.6279 | -53.34623 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec51682-679b-3e3c-a097-66174d4cbac3 | -7.12662 | -63.07283 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d200a1-ec8e-3a46-991b-2fd770c96734 | -7.22207 | -46.21046 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f3a1acc-fe37-31e1-b372-0f8340105fed | -12.9448 | -54.80719 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41a816e3-8075-3643-ad7d-8759455b377d | -12.95316 | -54.80844 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c72a2c8-59f4-3c4a-9ca2-2df6a6bd4c0b | -10.62109 | -54.91852 | 2025-09-08 05:21:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a926228c-a381-3dee-b56c-3ce73a741409 | -12.89521 | -47.99084 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aded263-01b9-3fcd-8ab3-ee9bc0c58eeb | -6.20102 | -53.26458 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f57d6086-e745-3c4b-9047-ff37ecbaf52e | -13.03649 | -47.13185 | 2025-09-08 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e49634fd-f669-368a-bc00-3a6c51ca98d0 | -9.17054 | -59.36226 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9f7f34-183e-3710-a263-3e8956611659 | -9.06841 | -60.49134 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18e6f90-1c9a-349b-aa7a-2e553cb61218 | -9.10661 | -60.9708 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7322681c-c1eb-3b8d-b71b-adecb96b3149 | -11.21545 | -55.00682 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 884fcdba-d1cd-32a6-8e64-a51351658ba8 | -13.83826 | -46.24233 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05be4493-0112-3bcd-9e6f-fe4fd282533e | -6.63229 | -53.37441 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0c06615-b9f9-389a-b681-04729c6c4675 | -9.47679 | -60.49541 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README80.md)
