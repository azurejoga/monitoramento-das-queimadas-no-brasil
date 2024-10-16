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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65de53a6-b05f-3873-8c24-61593efd50bb | -9.87353 | -67.19808 | 2024-10-16 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52adae1f-74fd-3f79-a1c6-a57675caac68 | -9.86816 | -67.29776 | 2024-10-16 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b9ceecb-c840-3b4f-9647-d7b381248e82 | -9.81627 | -66.52701 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f50c4b23-10a8-3e3c-942b-041cd967dedf | -9.70248 | -67.0599 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d65167d-c392-34b5-9159-4293b2753191 | -9.69249 | -67.05831 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a57da1e-e59b-30c6-ad68-962f7004caef | -9.61563 | -67.15755 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49cb4a24-2043-3587-8977-e5572dfdbd55 | -9.59273 | -66.78295 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cbd6980-14d5-3c18-8aeb-fa9c0212752c | -9.55954 | -66.4546 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de28daa0-37eb-3be2-b911-dce79d2af69a | -9.55899 | -66.45816 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bbd75f4b-9abd-3671-842b-2b25bb23e77c | -9.4774 | -66.55071 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 450c0d76-767c-3f13-8041-6b0232a744cc | -9.47685 | -66.55426 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0771218c-79a6-32ad-9b20-d657e00c551b | -9.46647 | -67.1629 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 970319a1-8149-3cdd-a615-2bd719b543e5 | -9.46129 | -67.06523 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31128a6a-236c-3e37-88f4-075e41f21791 | -9.45851 | -67.0612 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9f39d2e-188a-321a-80a1-ac58439e2168 | -9.45796 | -67.0647 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 554b8f17-e587-360e-808f-579b7d56029e | -9.45534 | -67.14685 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c30f5eb4-13d7-30e0-8c3b-55a8e2acfe3c | -9.45481 | -67.15028 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11148e67-3e89-300d-b3fd-ee698378b3a7 | -9.45202 | -67.14632 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79204df0-6c2a-3fcf-8efe-2b7d073b03e2 | -9.45148 | -67.14975 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 379de442-ca83-3404-ac8b-ea3164665fb2 | -9.44967 | -67.07416 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928c7511-681e-3908-a1a6-eaeffcecb039 | -9.44869 | -67.14579 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f205559-b74a-3215-93e8-22939527a06b | -9.44816 | -67.14922 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6886a75e-b5c9-3042-b16e-86155c1d60ca | -9.44689 | -67.07013 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e89012-583a-39ff-b485-27439d3dffed | -9.44356 | -67.0696 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff15e53f-1d14-3e6c-b5b8-714713e353e2 | -9.44078 | -67.06557 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b89bc41-6011-3140-8eae-96edc88f61a0 | -9.44023 | -67.06907 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f0a966-e781-3446-a0aa-bea1f4daa268 | -10.01963 | -66.82082 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d71a3ee1-aba0-365f-80b1-1b175958d294 | -10.01933 | -66.93312 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8812900-f83b-34e2-ab14-f86587e2d595 | -10.00315 | -66.90523 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1fd74c-0f3e-3e7e-9804-1243f415a420 | -10.00036 | -66.90116 | 2024-10-16 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5d8d61-7a37-3831-b57d-d0a55c1c03e7 | -10.33109 | -67.41101 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89df1fe3-3bdc-3352-96a8-c045b69fbf86 | -10.32777 | -67.41048 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f57c3d1-0f10-343a-b7cd-dbdbf47ba8f4 | -10.11462 | -67.23669 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bcd088c-d339-381c-b7c3-6dac8bfff9f3 | -10.10038 | -67.34943 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a1a031b-a9c2-3f6e-a454-f66e67f24b55 | -10.09706 | -67.34889 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04527d92-1867-3b8c-9372-0c948c807b01 | -10.0963 | -67.223 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0e36e07-7a34-3f96-9296-4136f0035a4d | -10.09575 | -67.22651 | 2024-10-16 05:48:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddae86c5-deb5-3b1e-a6df-373bbaf55558 | -10.03048 | -67.29523 | 2024-10-16 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca631526-c9c8-3df6-af37-5329f8f240d2 | -7.60899 | -67.35745 | 2024-10-16 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69df1fd-1f91-3620-9bcd-27c56608aaae | -6.79393 | -66.8827 | 2024-10-16 05:48:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00973a6e-ba70-3deb-a6b2-f58cb671a3bd | -9.15176 | -68.68079 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ac001df-ef1f-3ad3-94df-783e367d91dc | -9.15119 | -68.68439 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf4075e6-514e-3620-9942-bba8396607c6 | -9.14839 | -68.68024 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 25b27535-bcda-3b5d-8c9e-66a919d921bf | -9.14781 | -68.68385 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8cca72c4-c0c8-30d7-b7d0-269a05ddbee9 | -9.14608 | -68.69466 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68200763-3fc8-3d6c-8d2a-6812ad44ce05 | -8.99984 | -68.50143 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85ef2c4a-3a2c-3e90-9b28-be0fe62046a7 | -8.88088 | -68.75999 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4de7322-5c2a-3a00-884a-3e2baf75a51d | -8.79381 | -67.62807 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39ea2a60-86ca-3678-8e37-dab7dd4b4e43 | -8.79048 | -67.62754 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 593d4a65-11a0-34bd-b606-92abf868744a | -8.78716 | -67.62701 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a3c1f42-00d7-3f9b-b724-461cb11754d5 | -9.44118 | -67.8362 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f8134dc-b4f0-36c8-b5bb-24598ce3c72a | -9.42345 | -67.81898 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81447a97-f7dd-3611-b21b-d50cb39306f1 | -9.40237 | -67.84435 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c840a6e-280b-3dc0-9f45-387f3ad6fe1a | -9.40181 | -67.84785 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0434b42-e47a-3319-aaae-5393750c8654 | -9.39727 | -67.75401 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e811e577-b52a-3cca-9e30-88ad3d6d120d | -9.35737 | -67.83379 | 2024-10-16 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b22c02-1240-3cc8-816b-865b52fed259 | -9.78381 | -67.94119 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfb11846-190a-3ff8-9ced-57da81c2d14d | -9.78048 | -67.94067 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35d645fd-272d-3e8e-8cbc-e3a5cc393d97 | -9.77992 | -67.94418 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5108a12-9f66-375d-9981-b8d99c66d262 | -9.75313 | -68.40338 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 572198d4-7094-39bd-b32a-bcf052230855 | -9.66225 | -68.57479 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acbf05c2-80ee-3937-bb99-cc0dad16b983 | -9.64466 | -68.96487 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2dcad3f-15a7-3a86-9343-09329b0a08a0 | -9.64407 | -68.96851 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e5b2ef4-f26d-3ed9-b473-03826b07df7e | -9.63914 | -68.61143 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fa9e9a-68ad-3645-8c49-f02cf9066cad | -9.60905 | -68.55173 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ee3f56-d61d-3950-9d6b-4c8da2352913 | -9.60569 | -68.5512 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6a05ee-c6ef-3abe-bc8b-5dbfe603f05a | -9.60012 | -68.54295 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ab91d56-3e7d-3403-adbe-c11e4fbcabe0 | -9.59955 | -68.54652 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb27570e-fc76-3230-8955-1b24a2fd0a9f | -9.59676 | -68.54241 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd2831b9-5310-34b7-8a83-14643caed521 | -9.59619 | -68.54597 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc79a541-399b-3fe9-b673-706166c21e2a | -9.58905 | -68.50449 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 863ddf51-beb9-3179-b414-f3f3d692ea60 | -9.58848 | -68.50806 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 073951e6-9031-3eda-a391-8cad0b240961 | -9.57696 | -67.81483 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8a4c942-e702-372d-b015-a7ef8ab055d4 | -9.56542 | -68.54459 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff77211e-877c-31c0-8e52-ceae5eb14b04 | -9.56287 | -68.62502 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a348747-5564-355a-9813-5b7092d6fcf9 | -9.54267 | -68.49326 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac57f9de-97fe-3e5c-9b8a-19c7f17f7719 | -9.54117 | -68.58834 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7035e19e-34f5-310e-b312-752001829643 | -9.48469 | -68.50253 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7132309-d90c-3b6d-b9fb-828fb40d73d2 | -9.4746 | -68.9149 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68dd7741-b937-3ecd-bcf3-8bbb59b8ef2a | -9.47334 | -67.80544 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f52829c4-d8fa-37ef-b16f-b69f15433c47 | -9.47191 | -68.47481 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cb10745-d19e-39a9-8c46-cf7e9b924ef4 | -9.46685 | -68.48497 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ca90a5c-fc8d-39a7-bc80-27f5c6d431dc | -9.46334 | -68.52835 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894c354a-3838-30ee-abf5-6c39c4786e5d | -9.45998 | -68.52781 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17211e37-f7bc-301f-94fd-73c9dc27d993 | -9.45941 | -68.53138 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf3d98a-9c99-3036-b82e-8a60bba33e65 | -9.41024 | -68.20284 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c89b058-c6c1-3f87-b903-b6633c1035c7 | -9.39948 | -68.29184 | 2024-10-16 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 821f54dd-f74d-36f2-b553-23a64bda8859 | -9.38294 | -68.68475 | 2024-10-16 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e696b62-66b3-32aa-9879-f0d9008444e9 | -10.55906 | -68.57735 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28420f01-3151-363f-9025-e08bdc41cd92 | -10.54574 | -68.72541 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e4bfe3b-dd7c-33cb-ad55-b164b28f547e | -10.54547 | -68.64098 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23b6a237-9c61-344f-897f-95de6ebb8e8f | -10.54516 | -68.729 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28c03714-b360-34b5-8f77-e4ae4f842401 | -10.51441 | -68.85655 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0eb6f56-67a0-3242-b761-c574a5105f37 | -10.48875 | -69.03793 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e7cf8b-7382-3f02-8a4f-272e12aabc28 | -10.48817 | -69.04156 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 690d8c7b-941c-368b-8a7c-549662914ce9 | -10.46295 | -68.72642 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0d58702-cc5a-3c70-9d6d-c6463d5a8203 | -10.43076 | -68.46541 | 2024-10-16 05:48:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d240b5-a6b1-3c1f-bb61-d5e4fbf0565b | -9.89566 | -67.59322 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 917de0ee-22e8-32aa-8547-202e1170bf5e | -9.84464 | -67.55598 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2beed049-1d03-33e3-98c7-135658219b2e | -9.83361 | -67.60443 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README67.md)
