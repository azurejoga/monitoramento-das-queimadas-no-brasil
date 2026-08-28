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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e069c1ae-37d7-3ba8-a40d-92b66e3b534e | -10.05619 | -68.8407 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.8 |
| eafd8b1d-c616-3e19-a3db-7351c846559b | -14.43616 | -52.60375 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2456403e-f0d5-3659-a0e9-4089f47b49af | -14.7319 | -58.71558 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b146025-1e2e-3634-a16c-022a0224c001 | -10.51095 | -59.6272 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d04f84ae-59f8-3f85-84fa-c6fdffd80455 | -9.8623 | -60.26166 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fa9ebc0-07b7-3bc2-af60-698528917886 | -10.78647 | -61.41962 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dde07383-a216-33ba-b1ef-6c5b3fa499bc | -14.40888 | -52.57365 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 661daf0b-2f85-37f4-9c33-cf9884df9586 | -10.49424 | -68.40784 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4846bf19-0a8d-3d0b-a7ef-4a65e85c9bd8 | -10.15153 | -64.43813 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 2d18e7ce-d689-31a4-9c0b-d2c6092a6a68 | -11.27056 | -54.01224 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 71ad2f08-06af-3666-8e9c-ce3a1b6153dd | -14.17278 | -48.76888 | 2026-08-28 17:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66851d51-ee0d-35af-a8db-328f8f5d1f94 | -14.92771 | -52.61273 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 053bcc2b-201a-33fa-a30b-a3b15217de3b | -11.2701 | -50.7049 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2c8dabdc-42bd-3b86-b19f-5215bfab5aa7 | -14.7411 | -58.70547 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb33980f-87df-37aa-be04-15db74fcc9cf | -9.2485 | -57.07912 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3df3cd36-5756-3fe1-8159-9620ee7741c8 | -14.46056 | -58.5188 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 97d7d661-7767-30e1-ba95-d2cd02d22804 | -14.20114 | -52.85183 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f751119-09b3-3c07-9580-63fa66569cbf | -9.85855 | -65.04276 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2b2298c6-e41c-3d21-a3c2-34d2a3c287f9 | -10.50361 | -64.50056 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ba459b4-bb94-3fb8-81e0-8ca079cf5c2b | -8.59845 | -54.79774 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9dbd1ce8-2b9e-38cb-99cf-1e880978adbd | -10.59899 | -69.56275 | 2026-08-28 17:45:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b406a5d8-f494-3295-9e21-09977dcbd8e2 | -13.86665 | -54.11885 | 2026-08-28 17:45:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 27b61b1c-ae4a-3bb4-81aa-7b761a60ae57 | -11.01464 | -59.23376 | 2026-08-28 17:45:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9f629eb0-e458-316d-a9fd-5d40028aca5f | -14.43949 | -53.39294 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6245a5fc-00aa-3232-8ac7-5bd2c891c809 | -14.88264 | -52.61327 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d311fd1-3880-3355-bef2-157c925c9b64 | -10.07488 | -68.55436 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1db5fa21-ba45-3d8b-a00e-8b15ddb414c4 | -14.51557 | -53.25207 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a4b4329a-6fea-386c-b853-a6282118f2a5 | -14.64058 | -57.01053 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b7102c69-056f-33a9-8502-dc7835981a5b | -14.91372 | -56.31969 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0b373666-e32b-3a51-8921-faca7bde380e | -11.62992 | -54.58566 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e260f2cb-ae77-3bfb-9620-f4f8b88bc792 | -8.67301 | -49.53136 | 2026-08-28 17:45:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e514d511-f0b8-3bb1-a104-ec1c25dc6593 | -14.92847 | -56.30948 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e6f2bf6b-1cd8-3ec6-8aca-e9938e29bfee | -14.87419 | -52.62422 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bbdca6c9-f232-387d-98ae-c615e6625a1b | -14.29135 | -49.38491 | 2026-08-28 17:45:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0494056a-230c-3580-baea-f52503e0055e | -13.88807 | -53.24438 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 63fd4203-3c84-3bc1-98a6-1ae991b0868b | -9.41705 | -50.4323 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2b47190c-e0e7-3286-8519-1fa8b694c7f0 | -9.17395 | -59.39334 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 90b83f1f-74e3-3556-aa02-71e1ca6b646e | -10.85183 | -50.21988 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ea929e41-9603-31f3-967f-ae84f95dce00 | -10.56705 | -57.48647 | 2026-08-28 17:45:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 46e7d06e-9237-328e-a34f-9c13be60f7a6 | -14.6094 | -53.14931 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 66532dd2-79e9-39e7-a89b-3fbf4325166f | -14.46414 | -58.51819 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ca6423df-ccfc-3a3a-9a7e-6bc3fce56d1d | -8.79689 | -49.99314 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fc4341c9-b060-3cd9-b7fb-c5825325ab89 | -14.19613 | -52.85321 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 32dacaf2-a144-3da4-baff-3e5779aa1517 | -10.20339 | -69.36281 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.3 |
| b1489379-9b84-3c2e-a237-ad9788ed956b | -13.26216 | -51.56219 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de987181-7ab2-39a4-9517-fb34b507bec9 | -14.88615 | -52.63132 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0adec444-fae5-37a4-9ae8-f623c301d36c | -9.85912 | -65.04666 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f4c290b3-706f-30c2-967f-aaf56bda2762 | -11.27385 | -54.0296 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 009d3009-e43f-30c1-8081-1815a2816f71 | -8.59061 | -54.70196 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 65bd0ecf-9a43-365c-9af4-700f8e0cd6dd | -11.20538 | -55.09925 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 83b82fb3-c0f4-3285-ad4d-57dc2f9230df | -14.91836 | -56.32251 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7fcd6b5e-f007-372d-a1d9-0fd4384ba156 | -9.94142 | -60.43432 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a0f14f64-425a-35e2-95c0-e33793a1653b | -8.82035 | -49.62441 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 37831ca5-6e2a-3823-ab45-a5855263168e | -13.87604 | -54.11691 | 2026-08-28 17:45:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b78045e1-74e3-34d3-9220-f502cf6899d8 | -9.22211 | -59.67184 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ae675616-61c8-3ed7-b5ac-2df4282e661b | -8.5071 | -55.32652 | 2026-08-28 17:45:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| dc098468-2f80-3192-b463-cc7120042346 | -8.59113 | -54.75762 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b2a9a83f-1cdd-3cc4-90fb-196b0b0d1eca | -10.26983 | -64.5044 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4b19bab5-fea0-3764-bbc2-7c2bc3458642 | -15.57088 | -55.99012 | 2026-08-28 17:45:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f4b80fe-bddd-3332-96e9-768121c2b88a | -13.43298 | -51.76359 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6f1c5cb7-e07d-3b7e-9c62-b8639c28365c | -9.12287 | -61.59634 | 2026-08-28 17:45:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1d0fbd31-57d8-3ece-93c3-f2452ddd86b2 | -14.56932 | -52.03659 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ac8be6c-fca9-328f-84df-600d92cd8ad1 | -10.46992 | -64.48632 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e0f196e6-a8c7-35f7-a155-35ff74cfaef5 | -13.88116 | -53.23534 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c25df28e-8c23-367c-b142-dcde3698f0a1 | -9.42371 | -50.43502 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 1b6f4b8e-3795-3386-beeb-6ef035f88f53 | -9.4183 | -50.44163 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 2ce7445f-c3ea-3db4-95fa-3115da61d11f | -8.95439 | -50.78958 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 88320953-4eba-31fe-bca3-f2dcd627088d | -10.41242 | -61.19786 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| eec12027-4f5b-3e3c-902a-8ebaf15b6282 | -15.60953 | -56.40231 | 2026-08-28 17:45:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2ae6ab39-ed89-3689-b7fe-8fd89f158a88 | -9.61724 | -55.11946 | 2026-08-28 17:45:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0785b207-c76c-37f1-9375-db34fb7595c1 | -12.90949 | -59.89962 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b4fb3018-d307-3235-a67e-2d5ba736dd1a | -14.47128 | -58.51697 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e5d444cd-5391-385f-b6e4-a0fa60bcc310 | -8.15881 | -54.96789 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 816b58f6-8fc5-334a-b774-dbe3ac80461a | -9.88124 | -60.25861 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5129809-8f81-3e28-8d36-135df60b381d | -9.23525 | -57.0773 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2229a184-f7f7-3dc4-8796-25c3c126ec81 | -8.5932 | -54.76899 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ab542b71-9690-35da-97f2-059d542d82ea | -14.65425 | -57.00555 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 0bf506c8-07f2-3349-bad3-b834e1afab04 | -9.25073 | -57.06703 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d23c642f-72cc-36d8-8000-62a03b72e540 | -9.42474 | -50.44048 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 261.2 |
| 3f5b1852-46a5-3982-808c-62d3c446cf0d | -9.90798 | -60.15821 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2f9311b1-81e6-331f-92b0-ec8cce44677b | -14.16593 | -52.83336 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c304cf5f-4a06-30e7-af57-1b476cf67802 | -8.59763 | -54.77165 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 83dc0097-db00-346d-b798-c0ac2ee6d893 | -10.16422 | -69.01035 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| feebc4f5-bdc2-34d6-83f6-b8d5e2a96ec6 | -9.93168 | -60.43984 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 702.6 |
| 0a8a2340-1d8d-395c-85c8-57a10c2b3c83 | -14.63883 | -57.00066 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4f5507c3-1dcf-3d2a-8982-d7f910297b40 | -10.90028 | -50.49878 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9881462f-f726-3d9f-b146-de9ab0783a52 | -10.50872 | -64.51137 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e66f5155-77ab-3f93-bb64-32b566a3980f | -11.26927 | -54.00846 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e9686b6f-fc5e-3ab6-948a-20f285410505 | -10.76356 | -50.63536 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6fc93e6e-acf6-3f6e-bd35-0584ba79b711 | -10.76162 | -53.96851 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9ebdb04-25e6-3df0-af79-82d3c2282466 | -14.9251 | -56.31382 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 30bc5175-8f53-34eb-b12d-96f325acb5b2 | -13.42744 | -51.76458 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c7a47f54-dedb-3e81-a847-745f84a17ab4 | -12.33404 | -63.73012 | 2026-08-28 17:45:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba3aa406-7345-3cf8-9e0a-f25cc36945f8 | -12.39354 | -48.19506 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 40d2ddcd-9352-302b-9147-7732b8735c83 | -9.61248 | -55.12027 | 2026-08-28 17:45:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 521874a7-9a94-355d-9351-d7fb05891bdb | -10.08084 | -48.68807 | 2026-08-28 17:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fdf31341-5333-33a9-aac4-25a7b67005e8 | -6.84473 | -59.9531 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 53483e35-4ffd-391f-8c5f-4c9875cc2a47 | -8.27741 | -70.7782 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7d56a784-b6be-3ad4-89ef-657d43735b29 | -8.63538 | -70.71709 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 85c925a9-20c1-39f2-a64c-b63cfcdc1639 | -7.26016 | -60.63141 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README145.md)
