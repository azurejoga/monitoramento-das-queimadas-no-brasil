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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b97831b-306a-31ad-953b-4c9b3188e3b2 | -10.5237 | -50.2993 | 2026-07-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 93f2f50e-3298-3e76-b325-7d67b094ec07 | -10.5424 | -50.3187 | 2026-07-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6b6679e0-dffd-378c-9237-2fb2cdd00854 | -10.5426 | -50.2973 | 2026-07-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e5181c78-8a86-3881-baf2-cf22b368f6db | -18.5476 | -56.8135 | 2026-07-21 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| df779b2f-2c0c-3034-b839-3f09f2374890 | -10.8626 | -50.413 | 2026-07-21 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ffc62cd8-e96a-3844-8380-07866f254626 | -18.5675 | -56.8109 | 2026-07-21 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| f6761bb8-f104-3c3f-bbdb-c08800113f79 | -12.1312 | -48.2653 | 2026-07-21 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2c62c0c7-d121-33a5-a3b8-e0ceba71dc2e | -18.5476 | -56.8135 | 2026-07-21 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 1d2e9be8-c102-3026-92d0-67cf3a75d956 | -10.8626 | -50.413 | 2026-07-21 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 24d8bbde-7d43-341f-aa4d-d0d348f80b76 | -10.5237 | -50.2993 | 2026-07-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f833f642-22e0-3677-ab56-e8977df8c3d6 | -17.5947 | -47.4956 | 2026-07-21 00:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 512b7782-e516-324d-aafb-a207f2d88448 | -8.7685 | -49.0765 | 2026-07-21 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a54151a5-3753-30ac-bd73-e641fc9e0142 | -8.7497 | -49.0782 | 2026-07-21 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 976c92c0-34d4-3e8e-a50b-27bd8a7b84dc | -10.8626 | -50.413 | 2026-07-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1e77ba8d-61b5-3050-9686-d11938ff1f66 | -18.5675 | -56.8109 | 2026-07-21 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| b25f90d0-cdb0-3c92-9843-6200b6e96eff | -10.5237 | -50.2993 | 2026-07-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a9a4a71a-d88d-37dc-b9c3-6578fb5ba6eb | -18.5476 | -56.8135 | 2026-07-21 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 3245641d-15a5-3202-95bd-756561620e0a | -18.5476 | -56.8135 | 2026-07-21 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.6 |
| f35422ad-03da-3f1f-bf18-61d33aacdfc0 | -10.5237 | -50.2993 | 2026-07-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c96c3c45-cbf0-3476-a71b-f19f19b9f523 | -10.8436 | -50.4151 | 2026-07-21 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e550e7a6-bfdb-365e-86db-c8614d3e9b6f | -8.7497 | -49.0782 | 2026-07-21 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ae50734c-43e3-3778-8ca5-bc13515a1d8c | -10.5237 | -50.2993 | 2026-07-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3eb96882-2fcc-3542-8965-25eebf0ed909 | -8.7497 | -49.0782 | 2026-07-21 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 79fd0bec-2236-3780-a181-dac0f7acc681 | -18.5476 | -56.8135 | 2026-07-21 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.9 |
| 6fb60380-2b9d-3cb3-beaa-f547b71f3ad3 | -8.7685 | -49.0765 | 2026-07-21 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4b47af9d-5825-37cb-9d3d-504e8859fe7f | -18.5675 | -56.8109 | 2026-07-21 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.2 |
| bb3c0eca-fe43-3a1c-bb5a-38f991b849dc | -10.5048 | -50.3013 | 2026-07-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c84bc7e8-d8b9-37ff-a22d-73fdd7a2c269 | -8.7497 | -49.0782 | 2026-07-21 00:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 489c7f43-b7ae-30f8-99f0-a12f0791ab48 | -10.5237 | -50.2993 | 2026-07-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f8537be9-380b-370f-9956-475ffc58a6d8 | -10.5048 | -50.3013 | 2026-07-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a99cb9a8-85c5-32ca-9757-dd555d13f87e | -18.5675 | -56.8109 | 2026-07-21 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 4182bbb3-8fdf-3416-8ba1-e8a2cc6c7997 | -18.5476 | -56.8135 | 2026-07-21 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 221.0 |
| 0088e921-ceeb-38fb-85fc-55501770cd1f | -18.5472 | -56.8343 | 2026-07-21 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 36f1e1b3-0968-38d5-8277-bed8a18f2232 | -18.55001 | -56.80949 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 244.7 |
| 80fc1203-cfb1-38ee-acc2-affb7e04d9b5 | -18.5613 | -56.81886 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| ce6ec2c7-0329-3683-9f7e-b08e2e8d3a7f | -18.5596 | -56.80783 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 881851d2-ce75-32a3-9993-93c151981bb2 | -18.54726 | -56.8157 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 229.0 |
| d9778fca-5811-3f66-86ac-1bd5eea30dc9 | -18.55172 | -56.82051 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 264.3 |
| 8885d3fc-2856-3a83-8b29-1ef1d4061d29 | -20.89581 | -57.4887 | 2026-07-21 00:54:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d400626a-898f-30a3-a16f-ea13f2e8b9c6 | -12.98856 | -62.15002 | 2026-07-21 00:54:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5ab02f9-d239-3272-b985-c0db0d976643 | -18.54892 | -56.82672 | 2026-07-21 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 364379e2-4db2-30f1-bdb7-e03b7af355f5 | -11.59831 | -58.51663 | 2026-07-21 00:56:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 674aa56c-d9d1-3afb-a2ad-fc7a58b69316 | -7.68509 | -55.36436 | 2026-07-21 00:56:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 92c54d32-45f4-359e-8937-fb856b1382c0 | -9.49942 | -63.29889 | 2026-07-21 00:56:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae61ba54-e30c-3c11-b9dc-16faf0f18169 | -9.50072 | -63.3086 | 2026-07-21 00:56:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 297d337c-a814-3519-b951-bbce48d48d30 | -9.098 | -59.40486 | 2026-07-21 00:56:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0014edc3-a8bb-35c0-8424-0631e7274180 | -10.47154 | -62.45363 | 2026-07-21 00:56:00 | TERRA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d8d7b1e9-eef0-392a-8f29-f4ba8455cd50 | -9.49151 | -63.30989 | 2026-07-21 00:56:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30e0c12f-cece-316f-bb9a-e2b561885139 | -11.59678 | -58.50608 | 2026-07-21 00:56:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 41f88f71-8257-3c0c-a246-1cdc8d2d2cd2 | -10.5505 | -56.34048 | 2026-07-21 00:56:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bb350ac8-3f74-36e1-abee-9e0069469ed1 | -10.56054 | -56.33324 | 2026-07-21 00:56:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 05e8b621-cf49-3dab-8cac-cd583b1c3d30 | -10.54925 | -56.33495 | 2026-07-21 00:56:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 31951989-8ed7-3e34-9b95-a202c9d393ff | -10.499 | -50.298302 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9bd20f9-43eb-3839-8ce4-18ee5669c7e7 | -11.602 | -58.503502 | 2026-07-21 00:58:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b67e63df-1cb0-31df-9ee6-c4d9d4a9032a | -10.5086 | -50.2957 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d5399d5-971f-3e7d-8b80-f8e995f6709c | -9.5011 | -63.287998 | 2026-07-21 00:58:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29f653d7-4589-32e4-9c20-3d76ecde1d1d | -9.4929 | -63.297901 | 2026-07-21 00:58:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03aa2c8b-dbae-34bc-83ab-e76f7aea0fa7 | -8.7413 | -49.076199 | 2026-07-21 00:58:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b30ecd84-c8a9-3c96-8d4b-563c5fbf5319 | -20.873501 | -57.489498 | 2026-07-21 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d1c1264-2755-3b78-89fe-b06fa1b3a002 | -11.6003 | -58.495998 | 2026-07-21 00:58:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe3e3dfe-1134-3043-a54a-0dd05c1663d8 | -10.5536 | -56.326401 | 2026-07-21 00:58:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7ddd23-e53b-39b6-a69f-ac0b5e23b437 | -10.5149 | -50.319698 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 328512e8-04e4-351b-b89c-181b9e32c8e8 | -9.5027 | -63.2957 | 2026-07-21 00:58:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c2d6835-7923-3db9-880f-e4e706f89608 | -18.5497 | -56.799599 | 2026-07-21 00:58:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d85744ff-88b0-341a-af1c-87b834363d68 | -11.6313 | -58.273102 | 2026-07-21 00:58:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 133ca20b-bd90-3fcf-8c83-62a6004a7667 | -10.5119 | -50.269001 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43d2146f-79e3-3f2d-94bf-5d1fd76a0ac7 | -18.551399 | -56.8074 | 2026-07-21 00:58:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cdc4bbeb-36ea-3249-941d-c49c0d42aab2 | -9.0802 | -50.572601 | 2026-07-21 00:58:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a505ad4-73ca-339e-9ba4-0de472f86cd1 | -19.916599 | -56.859901 | 2026-07-21 00:58:00 | METOP-B | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ec24b15f-74b8-371a-92c2-5aace25135a3 | -10.7383 | -50.386501 | 2026-07-21 00:58:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d34aa7b-16cb-3d8b-98af-7d82e04f03f3 | -10.5023 | -50.271599 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec221ea4-2cad-38c7-9147-c2c79ed11cba | -8.7508 | -49.0737 | 2026-07-21 00:58:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e98d6d6d-bae4-3129-b2e6-220097ae949d | -12.9908 | -62.144299 | 2026-07-21 00:58:00 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 589b9210-8d08-3b0e-96a6-de73a60be848 | -9.1034 | -59.391499 | 2026-07-21 00:58:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fec5a720-e772-34e4-bc4f-d528c1bc8951 | -20.891399 | -57.4771 | 2026-07-21 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8412a7e8-4f21-3b80-b1b1-dfcfd85eaa55 | -18.5417 | -56.809799 | 2026-07-21 00:58:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9cdafdb6-42ff-3d60-8a07-7267d1856032 | -9.1051 | -59.3988 | 2026-07-21 00:58:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba84fd7d-f915-390e-a1b5-22756e154603 | -10.7287 | -50.389099 | 2026-07-21 00:58:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 934e4527-b1a2-31d5-803f-dfd774e1020c | -7.6897 | -55.356998 | 2026-07-21 00:58:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c22504-e3d3-37f0-98ec-2a2863f65e83 | -12.1279 | -48.238098 | 2026-07-21 00:58:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3590fd0-e1af-3e31-8d43-671dab1d7604 | -7.68 | -55.359402 | 2026-07-21 00:58:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb52cc2-0104-35ae-b308-ba02c34261ed | -9.4913 | -63.290199 | 2026-07-21 00:58:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b11016df-f2fa-3669-8aa8-353529914fdc | -10.5182 | -50.293098 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d283513e-2067-395b-8528-7fa62a05c18a | -10.837 | -50.409901 | 2026-07-21 00:58:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f884436-731d-3090-97bc-9a4944beeca4 | -10.5918 | -50.298901 | 2026-07-21 00:58:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56e78d97-872f-30f6-a5be-b29541290d64 | -18.561199 | -56.804901 | 2026-07-21 00:58:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b21b8f7d-fe45-385c-a470-a6460e164c5f | -10.5513 | -56.316799 | 2026-07-21 00:58:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62d492b2-b7ea-36eb-8fe6-1503f6dbbd5c | -8.7685 | -49.0765 | 2026-07-21 01:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 711b5c88-ff2e-3aee-a033-355c5e51d4f7 | -18.5476 | -56.8135 | 2026-07-21 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 187.1 |
| 315ba2e2-6849-3a64-8b91-87e57fb6b18c | -10.5048 | -50.3013 | 2026-07-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5665e0e9-5dad-31b9-8815-2342c3d1c22c | -18.5675 | -56.8109 | 2026-07-21 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.0 |
| e1082c60-4180-3048-8db3-78eb4ac6731f | -18.5671 | -56.8317 | 2026-07-21 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 0a839f77-ae71-39a9-bfb1-1980dfbb47a9 | -10.5237 | -50.2993 | 2026-07-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2e2bb1ca-69f0-32a1-a3d9-33fe4f3b36dc | -18.5472 | -56.8343 | 2026-07-21 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 85104360-8a34-3a84-9b7c-ca6b2fce07dd | -18.5472 | -56.8343 | 2026-07-21 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 9d9aff3d-e1cb-3202-b088-3bb398b16cc0 | -10.5048 | -50.3013 | 2026-07-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 09aef6fe-1005-30d2-a5bb-139064de97ce | -18.5675 | -56.8109 | 2026-07-21 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.1 |
| d7be2e5b-967d-3009-bba6-eee5f70b52dc | -8.7497 | -49.0782 | 2026-07-21 01:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a34568aa-e5e8-3401-85dd-0c07a565ed17 | -18.5476 | -56.8135 | 2026-07-21 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 353.0 |
| f7e71588-8dc4-361f-b300-c054e360e2cb | -10.5237 | -50.2993 | 2026-07-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |


[Clique aqui para ver as próximas entradas](README2.md)
