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
| c6766497-2ccf-337f-bf6a-7955e3a1c574 | -9.19544 | -59.68415 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b39b5ce3-a90f-3569-9a75-48dc7ddaf810 | -7.03902 | -44.34976 | 2025-07-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15d3174a-cfd1-3abe-94cb-c77c2346f58b | -9.33799 | -58.83659 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cce2dd2-bd1d-30ed-b578-53c860930918 | -9.21049 | -60.81904 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eecf4a9-74e3-3799-8ec3-4ef393e9f74a | -8.3469 | -45.63062 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96458f9d-55f7-35f3-b137-3bfbde2ada8e | -8.89065 | -48.08453 | 2025-07-13 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b141a7c-6172-34a5-a9d4-0cf0f3dcb563 | -6.45698 | -45.36992 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc7cacab-e4bf-3e42-a26e-d71d2f4b071f | -10.95726 | -54.37654 | 2025-07-13 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18a58c19-3d16-3578-9ce9-827f757ef256 | -7.82435 | -44.79094 | 2025-07-13 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a868029-118a-3ec8-8dc2-ce48df325af5 | -11.72671 | -48.52155 | 2025-07-13 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9be3cfb3-d7d9-31f1-b1c0-cf354eb2ab77 | -5.2679 | -44.87142 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4699392-8f10-3c21-aef6-4f529c0b04c1 | -8.92739 | -47.34173 | 2025-07-13 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4859cd7-10fd-3dec-909c-efbb7c912293 | -9.02026 | -61.2223 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 856d55f5-a3ea-394c-b5f8-aa9dd50a3028 | -8.69243 | -63.94263 | 2025-07-13 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18fcc59f-b78e-3894-89e3-1a84dd27c224 | -5.72747 | -49.11017 | 2025-07-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4b87f0-12ea-3033-b2cc-a77127f4e469 | -6.43992 | -45.39489 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 687939d0-14bf-33e5-a0a8-facf054b0fce | -10.29813 | -57.12603 | 2025-07-13 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36e4e4a7-9138-3fbf-8feb-71749106af95 | -10.66917 | -56.54752 | 2025-07-13 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c625a1c7-4a48-3ede-9ae8-a3edd35dbf1d | -4.53593 | -48.01661 | 2025-07-13 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c18e7cb8-e048-3c89-bd60-5c610675ab51 | -7.08912 | -44.07099 | 2025-07-13 05:10:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ccf0107f-7eed-3064-aa7a-b54d16af29b4 | -11.72834 | -47.46568 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee0fd255-9a7e-3c89-8524-b05e1c6a0ccc | -5.74095 | -44.99017 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dcee027-a97b-3323-b967-28a5d88ee78f | -7.03825 | -44.35805 | 2025-07-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a512658-3811-33c4-94f4-66c841ff6814 | -11.72719 | -48.51764 | 2025-07-13 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 911fdca2-5f8e-3209-ac0c-83aa701f9a81 | -9.34131 | -58.83713 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8546ba5c-f3dd-3ef7-b65b-36c4a3bc1f49 | -4.77429 | -45.34961 | 2025-07-13 05:10:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7a7cf30-cf85-3956-aa5a-b7ed69c2635d | -5.72739 | -49.10885 | 2025-07-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfb9e866-4dc6-3a7d-8c67-cf670594f19d | -5.74169 | -44.98484 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 814c0eb6-1438-3e55-9cf7-b0bb62a2411e | -6.44634 | -45.39613 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 441aeac5-5f98-33c3-a19e-157aa2b92532 | -10.04865 | -59.11066 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb24b8b1-b935-36bf-86b4-90258c17d972 | -10.70002 | -48.31548 | 2025-07-13 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b3e44ff-adfd-3891-bb2f-f54b16096d26 | -6.4837 | -45.26939 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 64fda131-9df1-3a2e-bf3d-b5a5b1515ac8 | -10.08374 | -60.49942 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 808954af-7039-39ab-a732-820473a6c4e6 | -6.63029 | -56.28287 | 2025-07-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c13acc21-8eeb-3ead-b120-a6335cdd7b2a | -6.48346 | -45.26912 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 04efaae7-77b0-3847-a5df-f04fe38f0b12 | -7.30803 | -45.33117 | 2025-07-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0740e761-72fb-3f49-a441-4b9172eb4a73 | -7.43031 | -60.02813 | 2025-07-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c9e75f9-9d07-3639-8b78-f9cd91591298 | -9.02607 | -61.2318 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b55d8283-c018-3f26-b8a0-c691f1d854ba | -11.82906 | -47.5084 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1349aa3c-7fa0-3969-a79f-ad18d3ed8c11 | -7.03914 | -44.35148 | 2025-07-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a1a8f43-5cbc-3423-939d-d99632123e29 | -7.53882 | -46.08276 | 2025-07-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c2a1bf9-bc1e-3dfa-a6bc-30b827490e33 | -10.57475 | -49.1326 | 2025-07-13 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 621c61d9-86f4-330c-9e22-180a4061e224 | -10.05585 | -59.10821 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 427b7242-1347-33b4-b9e5-7e846582852b | -10.13028 | -57.77591 | 2025-07-13 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9eb4928-4ddb-30a3-99b4-cc70113a1a57 | -5.73436 | -44.98939 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6d3d48c4-5ef3-3477-9197-ecfc3b509519 | -9.9202 | -59.91031 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b11f516-c953-3b28-a1fd-50e5bfab4076 | -11.73288 | -48.51837 | 2025-07-13 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e294b6b9-14b6-3ff6-859a-24ff3607f955 | -9.34739 | -58.84171 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dac2070-1461-3fd4-a9f7-fa9f1b345dd3 | -7.03817 | -44.35643 | 2025-07-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecc51bd3-0fb7-3759-b798-443a58751416 | -8.35079 | -45.65265 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae00d7ab-3783-3cb3-b710-4c70bb3d559f | -10.05197 | -59.11119 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90a14592-d4ac-359c-b2be-6a09bedf6d1e | -7.09112 | -44.07271 | 2025-07-13 05:10:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15f69362-ae72-37d1-ae20-3971937d4017 | -7.59634 | -63.47128 | 2025-07-13 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0532e45d-5be9-3d76-9f1f-83dab38d47c8 | -6.44053 | -45.39484 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9367352a-7e65-3870-ba4a-717dbb373b85 | -9.02317 | -61.22704 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5315d498-329b-312e-8ecc-998daaa1b2bd | -9.02385 | -61.2229 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be2789e-603a-3af0-8a01-bfb10c9c33e8 | -9.46401 | -62.18774 | 2025-07-13 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f80ac8-e057-336f-8663-547f396a14dc | -11.72889 | -47.46098 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 563daa3f-78a2-3c7e-97cb-638f1059ba5c | -11.73442 | -47.46648 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 151ea615-8d07-3eeb-9e10-493099304c7b | -10.0413 | -59.3493 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aff40fa-f73d-321d-bdb5-4e6024412a7f | -10.68875 | -48.31306 | 2025-07-13 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b180f2ae-9f40-3e37-9fc2-ef667ee42764 | -11.82244 | -47.51232 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db08bd15-d7ce-3a64-b0c4-27ad7eecd1c0 | -8.35137 | -45.64798 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ac92fa7-a482-3d73-b0f0-7ddbe629079c | -8.92091 | -47.34523 | 2025-07-13 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63eedb5e-4bb0-34dd-ac4d-16dc0369df3d | -10.04476 | -59.11364 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eae0878-8c0a-37c0-9121-7a3f41cab082 | -6.43985 | -45.40008 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20f766f2-69de-36fd-9e37-4285abf49cac | -9.02225 | -59.53746 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b7f7081-0ff0-3fd6-a519-045186f4ebac | -8.35277 | -45.63683 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 030c6c8d-e886-3f21-855d-bf80b2b017dd | -4.54123 | -48.01757 | 2025-07-13 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9ac899f-5437-30b8-ba5f-895480d80fce | -9.02167 | -59.54108 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b03e7ba-c7f7-3967-bb4b-597a28f6ef43 | -9.79929 | -48.5649 | 2025-07-13 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c47a5a-41e1-3b99-b53f-7a5ef669fd4f | -8.92147 | -47.34089 | 2025-07-13 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13dbfb7c-0bc5-3ffd-9f8f-f5318ce8a6ee | -5.26716 | -44.86793 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a38594f-4f8d-3805-ac95-d6b6be2217c4 | -9.25016 | -58.74728 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3753699-93be-3c6c-9274-0e0af77623cb | -6.4392 | -45.40013 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85fb964e-ed76-34ce-b4de-506c3ecf467a | -8.01532 | -50.10336 | 2025-07-13 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d12efc5-efda-3517-ba98-88062c115bda | -10.57109 | -49.11817 | 2025-07-13 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a622d92-b0ce-3b0a-9fa6-86a2e71d1ebe | -4.53497 | -48.02325 | 2025-07-13 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 079e5a1c-d477-337a-9393-6d9261d5389a | -5.6292 | -44.2691 | 2025-07-13 05:10:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f00c213-192e-368f-a5be-0399bea77083 | -10.56981 | -49.12836 | 2025-07-13 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1cc448a-84c4-363a-978c-cf0ddee26951 | -7.53815 | -46.08772 | 2025-07-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbff5d0b-49cd-3dd2-9af3-4b050efff0f6 | -10.34334 | -49.91762 | 2025-07-13 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23c71233-6c78-3306-8d4e-8b5e53ae692d | -4.53546 | -48.01992 | 2025-07-13 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f548352-9cec-3c8a-b67a-52bae20cf5cd | -5.62233 | -44.26825 | 2025-07-13 05:10:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09b12663-8a60-3d21-a661-e6b4928ee2c4 | -10.50125 | -53.58636 | 2025-07-13 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc46fc86-7fc8-3c6e-81e0-611d52c5c937 | -10.57024 | -49.12498 | 2025-07-13 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff3838f6-f148-3c00-ba70-9322ce240120 | -10.89629 | -49.20869 | 2025-07-13 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c0a03e7-6a0a-3eb6-b718-81152b882e40 | -7.82508 | -44.78547 | 2025-07-13 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9b59c1d-38ea-36cb-b8d9-508a989d3276 | -11.73714 | -48.5309 | 2025-07-13 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 076159a7-a279-3a81-93cd-2e623bcab864 | -9.8651 | -60.29354 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd8f8de3-36b3-3d2b-962a-2f5e680b63a8 | -13.47238 | -60.91829 | 2025-07-13 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c386b53-71fa-3a91-9b75-3be31bf148cb | -13.11591 | -47.29386 | 2025-07-13 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cde27969-a065-34fc-b846-ca9250dd8511 | -12.01944 | -49.52145 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a74c026-180f-3b21-b84b-9d2142b58e41 | -14.17822 | -56.30527 | 2025-07-13 05:12:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9310504-ce53-340b-af1a-da4cc59d86ab | -11.86573 | -58.70781 | 2025-07-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5f28e17-f859-3a1a-9b1f-c51351bfd3bd | -12.42701 | -50.46042 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44130860-59ed-3076-8d34-06f96c3c28a1 | -12.02088 | -63.78126 | 2025-07-13 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37eb4f31-76de-39f5-ad28-41ce97d07857 | -12.42159 | -50.46274 | 2025-07-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c14d6fd7-946d-39a6-856d-19b0e1156cbc | -13.02556 | -47.81957 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20e3d292-fa69-3b0d-8c07-8ea7b69e6d8a | -13.02665 | -47.82187 | 2025-07-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
