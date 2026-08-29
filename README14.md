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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c11e972-7502-3cfe-a5db-4408fd82a3c3 | -13.4772 | -57.0466 | 2026-08-29 01:16:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32628241-d85e-30c1-b6a8-aac6827f84e7 | -7.6117 | -61.361099 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6abc6ddc-33a0-381f-9b22-df223c0ed224 | -8.6054 | -54.830898 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556112f4-0c0f-3002-97f7-1cc37aae2448 | -9.2061 | -51.5634 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8d6395-0b59-37b7-ae57-86e2a6349404 | -5.8937 | -57.738998 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d05787-275b-39a7-b8ae-d6023216645a | -27.8619 | -50.568802 | 2026-08-29 01:16:00 | METOP-C | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0e8ffac-7896-3721-a7a0-ff28edf606d8 | -14.9419 | -56.316299 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5504d92-193e-3b4f-8e40-20fda6dc40b1 | -6.1723 | -57.784698 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bb8bd2-7b06-3903-b317-944b43ace275 | -9.9745 | -53.936199 | 2026-08-29 01:16:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcadbe61-7f64-3f91-8447-39903de6808b | -6.2633 | -55.4081 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb913b63-befb-35fd-8f5e-f4de87607aa1 | -7.3617 | -55.162498 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71e7ee22-d2f6-3eeb-b7b3-f93d8617e26d | -6.8275 | -59.954399 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 372a6339-fd1d-3c56-a65d-76d75565688b | -15.1209 | -53.584099 | 2026-08-29 01:16:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc32336-b71c-396c-96f9-c57cb42b86de | -6.1609 | -57.779999 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66f7566-cd1f-3afb-8483-f969f23a1a96 | -5.8804 | -57.771 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a14551c6-12fe-3f99-9667-6a5de51d7954 | -5.8953 | -57.745899 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707b0534-fb87-3496-9986-e56841e969e5 | -3.2043 | -61.1441 | 2026-08-29 01:16:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a337e50e-cec2-3852-96f8-8005e6aa2f1f | -11.2384 | -53.993999 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4565ccd-67e5-3f2e-99f3-e53efa37c6be | -15.1288 | -53.5737 | 2026-08-29 01:16:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5158df92-1873-3a71-a6dd-1c24108dc5d0 | -7.5314 | -61.369301 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dccdb06-6270-3a3f-a0c5-8f52ae65e435 | -10.556 | -59.613602 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e83137d-6853-3aaf-b7c5-1d1289dd0adc | -6.9711 | -55.700199 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74271329-b4b2-3207-8678-9bc5351eef51 | -4.1618 | -60.688499 | 2026-08-29 01:16:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0a8eaa-ba00-3f56-9be0-3db6119d9d06 | -7.3501 | -55.156898 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a428639d-4b46-364d-af8a-a4af9e83b969 | -10.4612 | -64.489502 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1d61d7f-9e00-315a-be95-1110fed9a1c0 | -9.9647 | -53.938599 | 2026-08-29 01:16:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c34d5af0-f617-3400-a60f-2e35eb065511 | -8.9872 | -50.799599 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3144feac-89ef-3985-81aa-20e5502a92e0 | -6.9533 | -58.955101 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d97cfe8b-3baf-3164-ace0-c3d90f0fe7f4 | -3.2025 | -61.136501 | 2026-08-29 01:16:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d21fd9aa-07e4-3b76-b3ff-7253e003c747 | -8.2446 | -54.965401 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11927f97-9f88-3c7e-b584-2a9f5d546d28 | -5.9953 | -57.687302 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b90fad90-caa3-31d5-8612-623de5559b51 | -9.1833 | -59.632999 | 2026-08-29 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 039996a3-70e7-3d1e-8eae-26703520567a | -8.5071 | -55.337002 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85915707-0cb1-39f2-b2d9-3ecc14c2b12e | -23.685699 | -51.633999 | 2026-08-29 01:16:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5c89aec-4859-38b5-aae3-3e70d3ef182b | -6.1656 | -57.800598 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48673edc-529e-31dd-8de4-bd0796cdb92e | -9.428 | -51.584 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3389696-909e-36ec-81c6-83d77fa55074 | -5.984 | -57.682701 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0b55766-38f5-3da6-88e0-3aada9cd473e | -14.8924 | -52.6227 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31e91d1a-6bf9-3127-a679-5590d4258143 | -17.619301 | -51.609402 | 2026-08-29 01:16:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70bbd7d5-b4ff-314e-be17-6c1ed38b1156 | -9.5992 | -55.106098 | 2026-08-29 01:16:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1c6e6e-e244-385d-9ae9-c77ffcc2336a | -10.4046 | -61.1917 | 2026-08-29 01:16:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8680434-df00-38b6-baa3-a4827374d1a0 | -11.2364 | -53.985802 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc1ca10-2cd4-3770-962d-43c767a394d1 | -6.9585 | -59.4818 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 904653d1-a639-3ca3-a2ab-f1864dde94c3 | -7.4862 | -61.397301 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 448e8064-b548-321e-90ec-44be3ee3e51e | -9.2002 | -51.539501 | 2026-08-29 01:16:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 177b18be-7ad9-375f-b4b1-c13388a9a40a | -11.2149 | -51.287601 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17a3172e-211a-3aef-aaa6-b1c74a74f294 | -13.4741 | -57.032501 | 2026-08-29 01:16:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3f757b8-64b6-3aca-a885-9f972cc78504 | 0.1381 | -60.404099 | 2026-08-29 01:16:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3c6c99-1a41-36d9-b84d-0574408a729a | 3.1133 | -60.698601 | 2026-08-29 01:16:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bad1a19e-74cb-3af5-8e86-564b809aaac9 | -7.5826 | -61.321999 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92d2a6c0-c455-3aed-bd62-252a11f20973 | -4.6937 | -55.668098 | 2026-08-29 01:16:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef41ccb-0aa9-39d4-9a5d-4dc5eb4f7775 | -6.7754 | -55.657299 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54aea44b-df93-340f-af51-74480abb33d9 | 2.4115 | -60.881001 | 2026-08-29 01:16:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9ad093-5dab-37c6-9dfe-b09f1cf10598 | -4.2984 | -59.471001 | 2026-08-29 01:16:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa160e0-0097-30de-82ea-6e05628353c3 | -14.1981 | -52.833599 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d383c29-621c-3388-b1b8-34ef7bf11c1a | -14.2001 | -52.842201 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea11aec5-aa6c-306b-a179-c711455ca80e | -6.8883 | -59.444599 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac4115cb-4679-3bb8-abe4-87f3c72400af | -6.7685 | -63.0397 | 2026-08-29 01:16:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37c43c8f-d945-336c-800a-9053b91f9a1d | -7.5295 | -61.360699 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3219f912-67ea-3813-8341-0e349f7d012b | -10.7496 | -54.024399 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e43a080c-13b6-350a-b5e9-2d17baf5599b | -6.7789 | -55.672501 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d168c69-87f7-315d-80c6-6672b7453481 | -6.2307 | -55.490002 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e138855-4bbd-3c08-96aa-c751bb61419f | -3.9358 | -59.3265 | 2026-08-29 01:16:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f546fa6-1a5d-39ff-a9e2-88c3d7368bbe | -6.1746 | -57.7047 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eec16f9e-85bc-30fe-9920-b4f2ac5604b6 | -6.1625 | -57.7869 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 433d51fd-b3c7-35ba-8be0-aa4d08c35a1b | -15.1172 | -53.568199 | 2026-08-29 01:16:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62d316ac-f57d-33a0-b75d-ac95ea27bba6 | 0.1396 | -60.397202 | 2026-08-29 01:16:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 58febb71-256c-3d1b-8604-a43094f45787 | -8.9564 | -63.277199 | 2026-08-29 01:16:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e401331-6cea-3e18-951c-42d51f7190e8 | -6.1393 | -57.640499 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e92116f-14d8-3a9c-95dc-540b0c0dc9ce | 3.1118 | -60.705399 | 2026-08-29 01:16:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 91b0b949-f3b1-3740-bfb4-0fa9492538bc | -11.0308 | -57.2076 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2b1a23-93d5-3f2a-8fb0-ccb3a77dedac | -11.2286 | -53.996399 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce6524f6-7a40-3058-bf3c-fc46dca7577b | -11.0273 | -57.237598 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb6fea12-c249-33c5-a899-8d20f2fa8fd4 | -9.2565 | -57.065701 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4d1e556-d83b-305d-aba0-26a90bb0b8e3 | -8.592 | -54.817299 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb218bdb-1a1d-3cf9-8111-a9cc6d3881ae | -6.7807 | -55.680099 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2744d6b-10ef-3af4-8342-5604fc68abb1 | -11.1954 | -55.087898 | 2026-08-29 01:16:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 281f278b-178e-3978-8c4c-56874bdb9095 | -11.7264 | -54.530701 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca24aa40-72e9-3c0a-8b4f-70a83b28b983 | -6.7736 | -55.6497 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5e4cc8e-8006-32e9-b8f5-5142cc213b15 | -6.1641 | -57.793701 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a330a37-1bb9-30f8-9f5b-2a6bd6adc542 | -5.9922 | -57.673599 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77969a9-5775-3b09-b552-097f1f4ee9b1 | -13.1734 | -55.653198 | 2026-08-29 01:16:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b04bb5f6-6f4c-316c-998b-daf96e395be8 | -4.0649 | -56.292099 | 2026-08-29 01:16:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1849b51e-61a4-3717-9fc2-44891ec8cb02 | -11.2656 | -54.021999 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5759982-f0ae-3b32-983e-6cf763c5a0e8 | -7.5176 | -55.299599 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009e8478-4c3f-3061-9d63-ee37ebded52b | -6.1099 | -57.827499 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d523e231-5b2f-3f99-b8e0-244e8bff653b | -11.1799 | -51.271702 | 2026-08-29 01:16:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 171c1089-a0fa-33b4-9ab9-557b555ee6b0 | -23.1483 | -48.662601 | 2026-08-29 01:16:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a202364-2b4b-36df-8268-0afdad660836 | -6.7262 | -60.007801 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e484910-0d3f-33b7-9201-a83b3767efc6 | -6.9517 | -58.948101 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d510ce00-7c9e-332b-824d-815ef481a8f5 | -9.4342 | -51.693802 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23be04b8-67a2-3e24-ab55-9fbb5a0527d8 | -14.9434 | -56.323399 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4808a26e-ff50-3fac-89e6-5016290abca3 | -9.8636 | -60.2999 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 496db817-afdb-3d22-9b1e-fe7b59aa25b4 | -10.8102 | -54.0187 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 839197b9-5a1d-3b5b-8f7f-59ae66f100b7 | -10.5087 | -59.632198 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4331be9-a825-34c0-8fab-9224498f5f59 | -4.152 | -60.690701 | 2026-08-29 01:16:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61ea40a0-f319-32b0-a32a-f95b99415b91 | -8.9741 | -50.788601 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95294730-4497-33da-a8ad-d5e589e7376e | -10.4935 | -64.498703 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9f742d-f481-3e2f-be05-9c122e04016c | -6.2651 | -55.416 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb5b7cd-e5d0-301a-bce7-7d21193faa03 | -6.744 | -55.478298 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
