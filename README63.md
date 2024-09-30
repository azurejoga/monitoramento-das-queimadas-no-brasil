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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42b17dc-e09d-3a35-8a60-18072a666eea | -9.67426 | -56.964 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6cdc1e6-0904-3b74-a705-fbfcbccd0e98 | -9.67111 | -56.95862 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ea0939e-74bd-398d-89d6-9b069632aec1 | -9.67043 | -56.9634 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d220139e-882d-312a-92cd-133b12c62cc7 | -9.66727 | -56.95802 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd922b9c-b671-342d-8345-90379c212e9b | -9.66564 | -56.95126 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cfb3f5f-b091-3c48-8f2d-36269bc7db21 | -9.66493 | -56.95607 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5316e573-10cc-360c-9a94-c85b374240ea | -9.66411 | -56.95262 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 392e4de7-bb16-3340-bd12-78a7538c56ee | -9.66344 | -56.95742 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c8df2a3-8a3b-3a65-af25-6dd2cd563da9 | -9.66181 | -56.95067 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffc83a60-c97c-31da-b689-5ba54529b6b8 | -9.6611 | -56.95547 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e7ba296-4e8e-37c4-bbf2-96f80de3e5b4 | -9.66028 | -56.95202 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15ba0ce4-e08b-3957-ba66-fc2150d665e2 | -9.65062 | -56.97348 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 043fd3a8-3da6-3247-9c36-77798e47b9d1 | -9.64992 | -56.97006 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eff27ee0-8c4b-34d7-80ff-02bf02f2647f | -9.6496 | -56.95371 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0928ef2f-4133-368b-ab03-b7831df95429 | -9.64925 | -56.97488 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae3b5419-c224-341e-bb82-b01ab4ce8382 | -9.64749 | -56.9681 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3981940-ca10-35a1-9cbe-87cae9d3c733 | -9.64678 | -56.97291 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adbd8c76-2296-345c-b92b-a01581bddf01 | -10.52507 | -57.78216 | 2024-09-30 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab641b26-8a0a-3c85-9df7-d257d4120c7a | -10.522 | -57.77718 | 2024-09-30 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 456e036e-a431-3287-8406-9f6ff23dd762 | -10.52137 | -57.78162 | 2024-09-30 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f532bf5-5d5e-3474-b909-98cf3be92bf3 | -10.51919 | -57.77904 | 2024-09-30 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aee9277-ce79-3678-b350-ee689e36c8b5 | -10.51831 | -57.77661 | 2024-09-30 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b47a5d-9600-39c5-b7de-5af7a3f093ee | -10.13563 | -56.76061 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4253fd94-ba2c-3a64-9612-7d792b6e6df2 | -10.13242 | -56.75503 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 028c0f24-344e-3781-b946-d3308d6990bf | -10.13173 | -56.76001 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 318b5325-a480-34a8-9736-d301c6403a54 | -10.13103 | -56.76499 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 357e69f2-cee1-3912-a342-650adccf44fd | -10.12852 | -56.75442 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1bb7a46-972d-3884-b77f-8f6b617d9a50 | -10.12782 | -56.75942 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab69bd6f-aef2-3df8-abf4-8baf8ce2fa4a | -10.12759 | -56.75703 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63668da5-1472-37ca-987a-bc6c361fefbd | -10.12712 | -56.7644 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b83232-aa18-3072-9cdb-4cc19425eafd | -10.12686 | -56.76201 | 2024-09-30 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e75f1b00-292c-30a8-8c45-23e9126e1827 | -8.13289 | -58.26815 | 2024-09-30 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05a17b3-dcfe-317b-bc95-701eaa50dd66 | -8.10512 | -58.04324 | 2024-09-30 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34ef8dc0-f36a-3eac-93bb-545d0ba3d0e5 | -8.10158 | -58.04269 | 2024-09-30 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07553bdf-97ed-32c9-b8f3-5bb43234e071 | -9.82426 | -58.97178 | 2024-09-30 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b8acee-4418-3641-87d1-4d19f7d1775c | -9.82137 | -58.96742 | 2024-09-30 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb9aff64-448c-36bd-a35a-9584c33c5a5b | -9.81386 | -58.97022 | 2024-09-30 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b7203e5-e6c2-36ac-859b-978b5a0c2b0a | -9.81329 | -58.97408 | 2024-09-30 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 270efe73-3067-32a0-9362-5376be17e8ec | -10.69663 | -58.52838 | 2024-09-30 05:23:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 845b3e58-94c9-3dba-b9ab-6299754b86b8 | -10.69603 | -58.53247 | 2024-09-30 05:23:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3adb331-8e2c-36b0-ab3f-bced79dd4f3c | -10.68653 | -58.52275 | 2024-09-30 05:23:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f79c823d-379f-350e-89e6-5a9b97893498 | -10.27889 | -60.98829 | 2024-09-30 05:23:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 917dab3a-2f73-3832-879e-12e19a074152 | -10.19475 | -61.30708 | 2024-09-30 05:23:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b6fe5c9a-5a57-3131-bfa0-3d49110036ea | -10.19145 | -61.30655 | 2024-09-30 05:23:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1361b5d-425b-35d3-882c-9e8865dbc820 | -8.80402 | -64.25555 | 2024-09-30 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6ff719f4-e542-39cf-bd8b-159aa38273d9 | -9.98604 | -67.57018 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4bbc5ab-112f-3bd3-9395-cf300bc4de8c | -10.11133 | -67.88728 | 2024-09-30 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c353e21f-aa67-387b-830b-8989154a07bd | -17.71976 | -53.18311 | 2024-09-30 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58580ea9-d6f2-3d39-9e1b-72d8fc32d277 | -13.49202 | -48.59863 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e54a51f7-d9a7-3bd8-a519-115b5e62c90c | -13.48324 | -48.61603 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4103d6bb-0c57-39cb-a9bb-f748c3e63e01 | -13.47616 | -48.61808 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfa418bc-49ed-36d8-a909-f3034de54c7f | -13.4926 | -48.59572 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f7a6ccfe-86a0-3cb1-a1f2-847264a43a40 | -13.49259 | -48.59295 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f63dade9-869c-3c9f-a635-710be0bea096 | -13.492 | -48.60136 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| dcd73463-bf8e-3306-92b1-8bcbdaf97746 | -13.48511 | -48.59747 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6185e256-adc3-3a30-87aa-5a46dab8c410 | -13.48386 | -48.60989 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 40056f8a-9980-3503-8b2d-ee2dcf0abd56 | -13.4768 | -48.61213 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 103a3926-e7a4-3234-8e22-9b1e6610962f | -13.20892 | -48.56094 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9b2c47a4-4758-3244-bb8f-1431dae11b8d | -13.19484 | -48.56571 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94b01ea5-66f4-3a1e-94be-9ed5a7c321e8 | -13.18791 | -48.56483 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8cb3480d-b4c2-3fef-98ee-239b0a09eb7b | -13.18069 | -48.56241 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a1022dfa-2c84-3f96-95f0-eefec9b9cd1d | -13.04271 | -48.61347 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61c3e3d5-55dc-34d1-8598-75545c6d8d43 | -13.04236 | -48.61312 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e4f264c2-584d-3bd7-bd39-8c26b03599c3 | -12.9809 | -48.53182 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44653fe0-aabe-3d96-ad88-acf2d56cebe3 | -12.97413 | -48.53248 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a51812e1-31df-3691-8b4e-91d4bfa330c6 | -12.96044 | -48.52932 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c32e0f25-44a3-36b3-9013-5e81de0198ae | -12.96026 | -48.52773 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 483e3005-5a2e-3d5a-b4d1-7724d8535baf | -12.95418 | -48.52232 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa35287e-7cff-3ac2-809c-170d141f97de | -12.95342 | -48.52598 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c3caf02-1a23-396d-a133-7db168cbdc00 | -13.48567 | -48.59189 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfbc8fbb-0b4c-38c1-80e1-3c3999299c62 | -13.49322 | -48.58996 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5577c29d-5b3e-3514-a296-1af4f05b8dbe | -13.4857 | -48.59454 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38f44f6c-19eb-3f6f-b2c6-2fa5292aec05 | -13.48374 | -48.61285 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5aef2b24-d9b9-36f7-82fd-a61b07db5c49 | -13.47631 | -48.61519 | 2024-09-30 05:25:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c58e4946-d2fc-31c6-806e-7e7fa12f089b | -13.2094 | -48.5564 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 497d887c-5688-3381-9318-1f3e28cdc1f3 | -13.20838 | -48.56614 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b7147f07-2f8f-3a6b-a54b-e7268049b4e5 | -13.20147 | -48.56509 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b02f3044-275f-3d29-8ce9-1557bd2a7321 | -13.19455 | -48.56414 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c5dbe56-bcaf-3023-974e-703d8d20803b | -13.18159 | -48.55843 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 865d06d5-755e-3dfc-94f7-198fa9e68e01 | -13.18125 | -48.55686 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ed51b0f7-821f-3907-8bd4-9fbaf257de0a | -13.18098 | -48.56403 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9fcc0d6f-52ef-365c-849e-d0e288704d5b | -13.03513 | -48.6193 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad0f1c2b-c3e0-39ab-9b77-38f0e4ca477d | -13.03474 | -48.61897 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 026b176b-dfb3-3710-b568-37e4bc2f31bf | -12.98107 | -48.53325 | 2024-09-30 05:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bfb8f5c-3743-3d91-af93-37b22b390722 | -17.65014 | -53.15514 | 2024-09-30 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acdf7f6f-3516-355d-aecf-19073c11938e | -12.97395 | -48.53113 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12680f51-b12b-3b65-b0aa-93144f8836cc | -12.95361 | -48.52758 | 2024-09-30 05:25:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7a6f0c9-b39e-37ee-898c-4b622099bc81 | -14.75654 | -48.74955 | 2024-09-30 05:25:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ace12c74-bbd5-33f1-9595-ace17d4cc154 | -14.76267 | -48.75916 | 2024-09-30 05:25:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 817cc296-254a-327e-9225-e5344c58b777 | -14.75725 | -48.74221 | 2024-09-30 05:25:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b67ab6b-bb7d-389a-afdc-5afd4d6218ff | -14.76344 | -48.75118 | 2024-09-30 05:25:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 338e3e2b-7aa6-3cd7-b939-78b3d07cd23e | -13.57793 | -51.07659 | 2024-09-30 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b340979-c6ff-38da-bd37-d07f50894b83 | -13.552 | -51.09155 | 2024-09-30 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc49cc47-1c33-3406-9329-86a08564dd12 | -13.5525 | -51.08704 | 2024-09-30 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a5590df-2cce-3b61-a2cc-7208e940873d | -12.53002 | -50.63991 | 2024-09-30 05:25:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b290c1bc-4072-327b-8d1d-23797f91868b | -12.5295 | -50.64457 | 2024-09-30 05:25:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d4ee5c-e56a-39c4-9d47-12b5c60411ee | -12.28217 | -50.45986 | 2024-09-30 05:25:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71f2e931-7ab8-3da8-9d16-618d9ad3575e | -12.22702 | -50.67117 | 2024-09-30 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98eac55a-6d68-3b80-8ba7-9c3537252f98 | -12.22649 | -50.6758 | 2024-09-30 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b57bf28a-41b7-3f7d-8ea2-da8f42889d28 | -13.68886 | -50.92366 | 2024-09-30 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
