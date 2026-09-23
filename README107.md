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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aeff88c4-e089-34f5-a0e6-51bb1b44fe18 | -3.0145 | -54.1842 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef0757b-9f77-3229-9f96-70fd451d256a | -3.063 | -61.27035 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275b7120-1bf9-3ce9-8ddb-3ad6853fa5dc | -8.22988 | -62.84113 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a789d85-ad3f-3acd-817d-4710db195b74 | -11.78223 | -50.96998 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8a49882-ed5a-3b2b-98b9-e808374d571a | -3.06702 | -61.17635 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb47433b-c6cb-3d2a-a09f-ab4bcbaa9972 | -3.10877 | -61.09588 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171d66c3-d6d2-350b-bb4a-b2c9adb83442 | -10.90342 | -53.95993 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc5215e4-5800-3ee4-8810-5cfb03d72157 | -9.97097 | -50.25652 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b49ee2e3-2c17-33fa-823c-25148aef09de | -3.78236 | -60.7559 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0014ec4-01ad-38c9-8a56-e3c14ded4fa1 | -10.4406 | -50.35691 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69c3f557-7bad-37da-a926-7153a97368a2 | -10.26428 | -49.97123 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbe6b2cc-866e-378f-82e4-6cbbf5fafcab | -5.1816 | -56.18361 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7e78e2-52b2-3b7a-b999-b6fb878651ab | -11.98814 | -52.4617 | 2026-09-23 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b1eff6b8-f49e-3337-9afe-19ac1513a53c | -3.1575 | -57.69421 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c668022-2617-3a13-b1fe-d3f0a2977112 | -4.16544 | -60.76908 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6c5f79e-8335-3381-beaf-886c72fbd547 | -3.82805 | -59.40039 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8a301ef-3d08-3ba7-be85-c57299fd3035 | -2.4674 | -57.91248 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05f9edb6-14a8-3f56-a1c8-552ebfd349bd | -3.60915 | -60.56768 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9593a03e-7470-330c-8554-da946b50b5f3 | -3.28677 | -53.26315 | 2026-09-23 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7342992-8118-31df-86c0-cf599809eba4 | -4.53541 | -54.96955 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30ae2644-2af2-35ce-96a5-e40e414ee55b | -10.4551 | -51.29183 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16fb8fc-563e-3e0a-b3fa-ece2f1787925 | -11.66364 | -50.97945 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aab6839-4a11-3d85-b70f-02775196a7bb | -4.42537 | -55.08112 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 008fc899-1689-3601-8277-e131b31d4816 | -2.6824 | -54.43226 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc81dd89-b0f8-3a27-870d-a72d715a66ae | -4.97954 | -56.95889 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f0c265ec-3032-33c9-ac27-dba455be6a36 | -3.35116 | -58.18899 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7271af6-f4db-3604-90b1-6a16463ae410 | -4.56652 | -55.06479 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b964a9b1-d791-3b6d-8465-24724210c902 | -8.52058 | -67.00565 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15e92e4-740e-3ab6-877b-470548a692fc | -10.85134 | -56.22212 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300b983c-4727-3736-99b3-42a184a8466e | -3.7953 | -59.37378 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59c02221-f92f-32a9-933e-41930c89b029 | -3.44209 | -50.61444 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 168f9bb4-5d51-3cee-a44c-992762c17bf1 | -11.12052 | -51.05707 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32b64f47-2cab-3da2-8df0-93cf3d524bb4 | -3.77217 | -60.731 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8be64a4-253d-3746-8ca1-5c7c00801554 | -3.10967 | -60.70715 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 423d5c25-c322-3e97-af19-e293c4021b58 | -4.42975 | -55.07725 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc02ad4b-eb32-3642-b876-f63ac3cc7679 | -3.90339 | -60.58975 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b16c8f41-645c-3ba1-9aae-e58358543bda | -3.00757 | -54.1782 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe836c1b-75a3-3835-941e-911bbac66ab9 | -3.07076 | -61.26745 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ca66856-01e6-389d-bafe-71f2ea316116 | -9.04849 | -65.42257 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79766f28-c414-361e-a37f-1eb63bec552f | -10.29546 | -50.52156 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3d32405-5039-3a5d-bb1d-d43ec2047a40 | -8.94387 | -50.91399 | 2026-09-23 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2242d783-1835-3a95-acc5-07214b964839 | -3.68644 | -60.5871 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2e3d00dc-dbae-3215-9897-3fdb11dad6c3 | -4.22077 | -48.61436 | 2026-09-23 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6dfb62b-86ed-3e16-9b32-44b84cdb7069 | -1.82766 | -55.71757 | 2026-09-23 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81f86451-3074-306e-9d9f-8b1e25f8a820 | -5.8708 | -52.06968 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ceb9a7de-b5ea-3532-ab5d-0317f7c12cb0 | -10.28361 | -50.52722 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3f4e9feb-c94b-3e60-b3a3-97514dcdc0fc | -3.78297 | -60.75211 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58ca5d6b-d433-36f3-8c3b-8032279cdcae | -3.82146 | -58.88784 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 905f13dd-a385-3754-b941-71cc62f11cde | -1.11959 | -54.12268 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 694383db-09e9-3be6-9cbf-8cc0614a464d | -10.30139 | -50.51873 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c321066a-f417-3215-80b3-2e633d34eb6b | 1.07712 | -60.67632 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f94538a-16d7-39c6-8902-cb98c59eed1e | -10.28579 | -50.55271 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6cb18b4-bc63-3a51-afb7-0eb6036b57f5 | -9.63154 | -61.82004 | 2026-09-23 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6587b07-721c-37e2-b542-8c6736e3a49a | -10.29607 | -50.52482 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c704219f-03a6-38e1-81d7-b847a5d39bae | -9.10505 | -61.43406 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c39697da-f631-3edc-a514-1c7cb01b6a8c | -10.28751 | -50.54895 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 376bf7ab-e80c-3273-9638-91919ccd6f81 | -10.28907 | -50.52794 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| bc0d2801-2ce5-3347-963a-0eed968a229a | -5.73957 | -49.83041 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb47a891-d597-35de-83a9-84fcc1617688 | -2.47293 | -57.92041 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89105f62-8683-3a3f-a940-5299feb88889 | -11.63328 | -50.98173 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a57c9f1d-dfdd-3ee1-a96c-80be7232fe07 | -3.91046 | -59.71533 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f25d0ac-7495-32d9-8bc2-8682ef362528 | -3.60796 | -60.57515 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b65b94-0682-3f95-8f50-c2f10724eb28 | -6.34002 | -49.87383 | 2026-09-23 05:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1af9813d-3beb-3b84-99d2-cc829f7a1708 | -3.68704 | -60.58336 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 578f9972-867c-3bdd-b5c6-0625ebd00fec | -5.17857 | -56.18009 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9cd240ee-f2b4-3eeb-82f7-e8a6f3d41bc9 | -3.04228 | -61.26289 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d949dc0-e866-32fc-a627-ef495f39695c | -3.00996 | -54.1883 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e99ac6f-8959-3857-a395-8d910b392088 | -4.26061 | -60.0077 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7965b2be-0de1-336e-8d8b-b05c00f44026 | -10.26946 | -49.97585 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ffe4c34-ae7e-3aa3-b2ca-420daed07c21 | -11.99015 | -52.46331 | 2026-09-23 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 311f6cc0-e9f3-3b4f-bab4-bdeb52a484e3 | -9.18599 | -65.85157 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6869cd2-e836-31cf-8c3a-e0377bc72114 | -8.2342 | -62.83752 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79f97e20-b40c-3b77-9cbe-9a5a510c359d | -5.12071 | -48.79977 | 2026-09-23 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 280837fc-a510-30c7-af08-f663686cf197 | -3.24514 | -53.95477 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 734a651c-243d-3a3f-907e-772bef74fd64 | -3.89593 | -60.59238 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60488b6e-3e40-3af6-a254-649e3b7fbc17 | -3.10436 | -60.71806 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 669da0b2-5b83-35d8-9e9e-36304d4469d5 | -6.18228 | -52.79045 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a0cf4c7-1f8c-3622-ab09-ba443a6197d2 | -9.56465 | -65.99083 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 171f31a0-e642-386b-8808-457e43f5f916 | -5.1821 | -56.18064 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32a781b1-678c-36e8-80a9-8ef0e7514167 | -7.50265 | -63.88083 | 2026-09-23 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97d7daa3-0215-314e-940f-6226b0697a5c | -3.69335 | -58.92383 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9ba7b58-109e-3204-a5e7-58edf7e173e5 | -7.87974 | -61.1832 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e5308ee-4233-38e9-9637-085a35227ac4 | -11.12137 | -51.05035 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a4a757d-48a2-37ae-9f82-093f71d13d52 | -3.83417 | -59.38348 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2943ea73-a79d-373e-b252-eae70d805c5e | -4.53033 | -54.97791 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03566866-cb3f-3360-8f59-4a931615d0d2 | -10.31011 | -50.50137 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8ce30568-9bb3-31cc-8b91-25ecbc1b7938 | -2.97512 | -50.39236 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f489f20-e15b-37ba-8145-13d43b36d258 | -3.78357 | -60.74834 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2493591-6e33-3767-95f8-f190d364b4ee | -3.22455 | -61.05307 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4243f9-a54f-3564-9ce2-a506bc6ae8ee | -4.64059 | -50.99543 | 2026-09-23 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fccf404-0062-3fb2-b969-47d59ab16fc7 | -3.76143 | -59.47949 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71b85e54-991f-3af5-8c7d-d4bb9cea2b51 | -2.86039 | -57.78985 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ddd6227f-b755-3d0b-bb9d-ca11526d1317 | -9.16423 | -61.19668 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4eeef40-0d66-377f-9c5c-880aca7d0d90 | -3.51611 | -56.90568 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d742818-9d11-3e13-bc0a-5b43a7d17933 | -2.7199 | -57.64723 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0047a6f4-c5c2-3436-8e46-cfe09009761d | -5.56523 | -56.18206 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42497ae6-d310-3fba-8157-1751c7115797 | -3.90155 | -59.70668 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e3609d2-6d4e-3ded-9d16-83ae536a7579 | -10.29358 | -50.53574 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee6d3b59-a347-3ae8-abc3-94ad36c2bd3a | -1.82418 | -55.717 | 2026-09-23 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43898aa8-e76d-3269-80e0-95240a73e92e | -3.22327 | -61.06091 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README108.md)
