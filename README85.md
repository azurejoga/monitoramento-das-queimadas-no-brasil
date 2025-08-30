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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a376c08f-51c0-30ac-b0bd-b4cece784d85 | -8.66017 | -70.04266 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc9469ee-a3d6-3a99-91e3-bcde6d452b7e | -7.56934 | -63.86196 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5dc04a5a-f77d-3165-ae8b-d19efd83015d | -9.44693 | -60.56852 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 21d864e9-7492-36cc-b1aa-8c6e1625a435 | -8.759 | -71.06703 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6ba91da-c0f6-3c48-b4c0-69010c403fe5 | -9.43889 | -60.54618 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4bfb342e-3d11-3244-97e2-13cc0b6a9d8b | -9.45718 | -60.54048 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 114e731d-882c-3cab-8b0a-59218810c82b | -9.44216 | -62.33901 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8580d6b1-240e-38f3-a262-8b805c6f3f2c | -9.43674 | -62.36287 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0576a100-9754-3ce8-8b2b-2534b9525d18 | -9.24229 | -59.77564 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8facb30c-5728-3f57-86ef-183d0b4c9a57 | -9.43985 | -62.33854 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4c07f22-df44-3356-86e4-ceab8ba62ab4 | -9.45091 | -60.54382 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f1405a11-c224-3ba5-98d2-c0a8b0bfab56 | -9.46047 | -60.56136 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4cadd61-105e-3ca8-ba66-80538e156c71 | -9.43857 | -60.5426 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1293e798-899f-36a7-800e-1060751b1be4 | -8.09784 | -71.2465 | 2025-08-30 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e75ebcb-119e-3701-95b8-84c4bc6ced61 | -9.45141 | -60.53975 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5272afe0-d185-31cf-aa35-3b8f79c64594 | -9.17957 | -59.58776 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9a51a5e-f099-34b4-9228-c897f7f0bb86 | -8.29558 | -61.42057 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b4d9a1b-7a1a-3913-8734-902a3988501b | -9.43705 | -62.33822 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5d646d1e-aa73-363e-9ae7-369c85ab02c9 | -9.78876 | -64.24136 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55174421-47f6-3080-bc1c-225768c24932 | -9.1623 | -59.5766 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5186e4f-2535-37a9-8bc5-d544434eac36 | -9.12018 | -65.78805 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5b9bfb5-6c8e-3617-a174-66e915fdddce | -8.67827 | -62.43136 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 257ec439-e120-3348-aa94-7c2838b4b5ef | -8.55229 | -63.01931 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cee5cb3-edd5-3964-ac49-ac91faed285c | -9.43646 | -60.5589 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5897b274-03ec-3b13-93d9-69e2e335b46b | -10.40835 | -64.53674 | 2025-08-30 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b23bd1e-a7d6-3cc1-bfaa-6db28d437964 | -8.85557 | -70.62334 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f85906-7537-3d99-a666-e1f27cfc8455 | -9.44314 | -60.55937 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 70e45c08-1ed9-3a29-a3db-4f1f685bb936 | -9.44467 | -62.32048 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 160a159c-0a71-3f53-8b1d-823eb47e11ba | -9.45566 | -60.55287 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb646ada-cbfc-3659-a575-677bc37f4013 | -9.15106 | -59.56411 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0785fe3c-270e-3387-a5be-1258eef585cd | -9.43435 | -62.34079 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 54fcf2ea-790c-36c5-a9fe-c25331580423 | -9.44614 | -62.3301 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c516632e-b4b5-3e9c-b600-eb055805eae8 | -8.64041 | -67.25331 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c646f287-4f0f-377b-b295-9d6ef6d85500 | -9.44745 | -60.57204 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea3dc82a-6ab7-3098-aadd-0169dac7ed40 | -8.76285 | -71.06407 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 703ef33a-53d9-373f-8e69-1faf1c73c3b6 | -8.07318 | -70.5808 | 2025-08-30 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc221f7f-e5ac-3a7e-b2e2-7398207c2d07 | -8.1751 | -61.37438 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e54fa8-8862-33c1-9351-37b72f949560 | -9.12872 | -65.81468 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e27cb1a-3ed7-3844-9ff9-010e844c935b | -8.54697 | -63.9397 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d148bb0d-99ea-3f46-b73e-5a545064dec0 | -10.07148 | -62.90083 | 2025-08-30 06:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8336c2f6-2923-3a01-8053-8cb981f557f2 | -8.87457 | -60.73284 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aeaab994-4de7-3f17-8655-d45c73044a26 | -8.62514 | -63.95251 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16c1751-92d3-3c54-8e26-9d9fb5042dd1 | -9.63063 | -68.00485 | 2025-08-30 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08211490-c904-374f-a0bf-4f066f8c544b | -8.18874 | -61.37869 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b772c529-1b90-3221-878a-de2bbc7451d3 | -9.46057 | -60.55389 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4594e534-ded0-3067-89fd-7ec561bdde70 | -8.84963 | -64.15206 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b19c48c-9317-32ee-b930-70c39a1630e3 | -8.18426 | -61.37113 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d22ff8-c727-3468-8832-70de8d964601 | -9.43913 | -62.32288 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65681479-5348-33f6-a183-4914d031a4aa | -9.4537 | -60.56879 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 086faacb-c854-3a19-9b14-6316b8e5e39b | -9.43789 | -62.33204 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b959e5aa-fd2d-36a6-9863-cc693b186e3c | -8.66071 | -70.03915 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83166db0-2403-32dc-934a-2761e2cb84f9 | -9.1106 | -65.76844 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3564d2ef-b3c3-3eb2-b98f-795d4fc77aa8 | -10.37634 | -59.20311 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ac05dff-03cc-3a69-a9a1-b1b1e80440a4 | -8.17846 | -61.37375 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3867c9e1-93cd-3fa6-aece-6e749f4f19ac | -9.45638 | -62.37186 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e06cb9-3c9f-3263-aa67-ef7552917d58 | -9.3355 | -68.21566 | 2025-08-30 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef817316-b5b6-3b64-8461-976e78943083 | -9.45638 | -60.54098 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d6cc107e-f682-3f74-9fac-a6768d19169b | -8.1883 | -61.38208 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80e5d2b2-7d88-36d6-acf2-ab54faab684c | -8.04332 | -70.09581 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38717410-74cf-35e8-9368-8d971cdc146d | -9.76275 | -65.08366 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c2a150-98ce-3720-bc89-d102e10c5ee6 | -8.34426 | -62.93262 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f42bd72e-e510-335b-beb9-569b82cd9a3a | -4.9933 | -67.00174 | 2025-08-30 06:01:00 | NOAA-21 | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66cfdb3-1dd9-3dd3-9f92-1fc4fa7b37ad | -9.11057 | -65.73931 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46c5b948-e90a-39c2-a652-44c425532b93 | -8.28384 | -61.40295 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 630f05f1-c39e-3e8d-85e9-ffe6009d58fa | -9.18014 | -59.58313 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b47638fb-ff64-3492-9a55-e4ad7bb3c554 | -9.13298 | -65.29065 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31afa75d-a166-3731-a080-890996a3e500 | -8.67804 | -62.4314 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc19e1a-e565-3f26-8477-4729d364e512 | -8.91104 | -62.10798 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e9beb01-ffda-3608-b045-dc4fcab0473f | -9.45128 | -62.37113 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6671d4aa-53fc-350a-9a3e-1a284dd272e7 | -9.11161 | -65.76122 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 73f1745f-9037-3160-a4ef-7d28a816b69a | -9.45998 | -60.56538 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7840fd0f-942d-37fb-b400-3226168b4c28 | -9.44135 | -62.34496 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab5d36ce-9c93-30dc-889e-aae5f4ebca90 | -9.44117 | -60.56778 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 939bcbaa-8c8c-31a8-9461-34a8c4ba98c1 | -9.46096 | -60.55742 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c2e681-086c-3e8f-ba75-07127667db34 | -8.18093 | -61.37177 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1ae99c9-570e-391d-aa3e-9b6067f7a631 | -8.96224 | -65.96716 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8806687-815d-32ea-b4fd-ce362147230f | -9.44302 | -62.35445 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53562c71-deb4-37a9-a5b5-7f6a10411faf | -8.90199 | -62.09714 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2bfbf93-96e5-3f53-851c-adc5dc850c85 | -8.28977 | -61.42324 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f97a7472-3a15-3b7e-bdea-9b0f056fbb62 | -12.4355 | -63.92307 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12287367-7e20-3e2c-9348-adff6fd4d5bc | -12.42753 | -63.91032 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3621d772-0f87-392a-97de-79711ea4c056 | -12.22691 | -64.22274 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250e5a15-8ad5-342c-837d-d52ca616f75d | -12.43574 | -63.92222 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b86d4a17-7928-3e42-811a-873ff0dd4481 | -12.22626 | -64.22785 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9db9f383-b7b0-3181-93d8-e8c3b53bc090 | -12.43095 | -63.92158 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1641e46-a6d1-3e04-9bf6-a6611fe66443 | -14.78829 | -59.73368 | 2025-08-30 06:03:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f9ef694-cbba-3dda-8323-1532c71b5164 | -12.43615 | -63.91776 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f103178c-2ed2-3365-962e-6e2a9dd3ecab | -12.42684 | -63.91563 | 2025-08-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e6736ca-c72c-3b37-830b-7690ed11c9b1 | -14.78171 | -59.73389 | 2025-08-30 06:03:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 783be985-6dc8-3d96-adc1-77767b473fd4 | -14.78784 | -59.73796 | 2025-08-30 06:03:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10aa8d5f-d02d-3072-aa89-6528451abf5c | -13.5373 | -46.9456 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 90135e24-b7a7-32f4-b8a5-174084ef5ec5 | -12.0153 | -43.9818 | 2025-08-30 06:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 763cbd1b-65f3-3ca0-8b12-ec8c33974a3d | -9.4498 | -62.3294 | 2025-08-30 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 326.4 |
| db74738a-df7a-3700-9a5d-3e8d19882670 | -13.3817 | -47.015 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9efc56f3-3871-3410-8eeb-61a1b9ae06b3 | -10.0351 | -46.03 | 2025-08-30 06:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 9b33cf21-3a29-3ce3-b64c-8c48a780790e | -13.3632 | -46.9727 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 64ae7cb9-187a-36e7-b029-6bb0bb1d1edf | -9.4683 | -62.3476 | 2025-08-30 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 1b5d468c-e74e-35d9-9806-4629a91cdb56 | -13.3628 | -46.9953 | 2025-08-30 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 6692d39a-5523-3aeb-b58c-3a48facf9942 | -6.1853 | -43.3257 | 2025-08-30 06:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e05fed52-f2ab-3cb1-be6e-4161868dffd1 | -11.8369 | -46.4514 | 2025-08-30 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |


[Clique aqui para ver as próximas entradas](README86.md)
