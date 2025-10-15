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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac8fe327-aa52-3c2f-b779-af274bf9e502 | -13.47833 | -43.71463 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6082df24-db86-3269-bcf2-198326ca9023 | -12.21414 | -50.41498 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 975f85a3-5108-3e48-9bc8-6d9842e29244 | -12.22606 | -50.38741 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 92a680e9-c4a3-3365-9ee2-b4c92264a2d0 | -12.14733 | -50.38318 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e7e2dab-72c4-373c-9b56-18cd8a8a078b | -12.27245 | -50.40886 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d602cd20-b190-3300-88a9-e837d8155100 | -12.25428 | -50.39153 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c835316-0288-39fe-9699-32ef4e2868fd | -12.26539 | -50.40049 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| ccfff7a5-03be-323b-bd14-5fd38b844f85 | -12.24279 | -50.41552 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e72363b0-130a-3c38-86f4-48a4a58cc04b | -12.26341 | -50.41487 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a888dbfc-a92d-30f4-a452-986ae03aca3b | -12.14331 | -50.38259 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3979a04e-eb89-3324-bb8d-1038c92d0bf7 | -13.38536 | -43.65513 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4f8794fb-aea8-34d2-97e9-74e4f088d6f3 | -12.27295 | -50.40527 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 37b3bbf4-227f-3f2b-894a-22811b461a8c | -12.24878 | -50.40174 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10762c05-8ab5-3695-91c7-457e4fcf5ff4 | -13.39116 | -43.66135 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af481b95-9352-3551-963e-da74367acbf1 | -12.24829 | -50.40533 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c2ca8df-cc0e-3514-b6a1-98386d75f73e | -12.218 | -50.38623 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5404ff8c-e5ba-3908-9532-3430685927b7 | -13.36152 | -43.63572 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 710145c4-f570-3204-bbf1-c36fceff168d | -12.26793 | -50.41187 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 239b9491-a3bd-333a-a326-27d9b495902a | -12.22961 | -50.39161 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ace5165f-728c-3d22-95f1-1134e676d647 | -12.27195 | -50.41245 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d408ad17-6631-3852-88fc-6c7650a6e014 | -13.4847 | -43.71539 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8598b7f2-9bec-3067-bf77-16833a31ab94 | -18.2052 | -50.74294 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd5043ae-e924-3240-a732-cd522fec62de | -12.20609 | -50.4138 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b8081fc-c97e-345b-b377-7d178b57a854 | -12.25585 | -50.4101 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd55aa61-d754-339d-9d29-68d9766fe1ae | -18.19807 | -50.73971 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab796158-3cca-330e-8ad2-520c71584a4a | -12.25281 | -50.40233 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19c003a0-e84d-345d-818f-0f5c3f159bfa | -12.23474 | -50.41434 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f61df572-bd28-312e-b7ec-4dad3b4be5c4 | -12.22219 | -50.41616 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6bdf98ff-c264-3df9-9334-aa8dff22618b | -13.31069 | -45.55026 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 795fc60c-4e50-3ff7-a0a3-4fab8990c421 | -13.23592 | -46.54556 | 2025-10-15 04:59:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c7021f-82f0-34df-bdd9-981eb6c1cf1c | -12.25634 | -50.40651 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb55349b-fc3e-3b63-bec0-1e25b96d6706 | -12.24976 | -50.39455 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 62ed785b-7d35-34ae-b111-569fe7017eeb | -12.21816 | -50.41557 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d2ea22c-0593-3657-830d-70cb464306bb | -12.13928 | -50.382 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d6a55c2-60ac-3251-902a-6251f8a44164 | -18.20094 | -50.74215 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f9b937f-d40e-37d0-acd3-72f677fdce5d | -13.47945 | -43.70407 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| cd454f13-7d65-3452-a97e-7062c364662d | -13.36734 | -43.64192 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bcbea0a-2580-3576-a628-65a81eede0a7 | -12.23072 | -50.41375 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b58bbe04-96c1-3501-8489-10d984a67a24 | -12.2533 | -50.39873 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 96ed8715-6a15-36c0-b741-362e713f2c28 | -12.2704 | -50.39389 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c23e6dd5-4a68-3b83-95a6-52f7fe34caa6 | -12.26489 | -50.40409 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4da749cf-c943-3921-ae9a-b160bc02d32f | -13.47691 | -43.70459 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 460b43da-27b7-320d-beaf-8ace44cda638 | -15.85665 | -53.98978 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f35bd7de-9c67-3af9-a62f-9d246c000d80 | -12.06487 | -58.02707 | 2025-10-15 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f9bb290-b2b5-39d3-96e5-392073518d4c | -12.70025 | -62.18723 | 2025-10-15 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8811f5b-7415-3c38-82fd-b9fa63016bc3 | -12.26991 | -50.39749 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49b7e7f4-6040-3122-8e43-973f7ecb5864 | -12.27344 | -50.40167 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37f85b49-2d82-3de9-8cfb-2f699ff02223 | -13.47572 | -43.71513 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 209d9634-6beb-3dba-95d8-4fac90c24d5a | -18.19667 | -50.74144 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a80e3ca4-d8d4-3c53-8b3a-cb261f178f4a | -15.86877 | -53.97953 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd7afbfe-7630-3331-b16e-b1655cbaf386 | -18.19754 | -50.74394 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3bb4a48-afb0-3c4b-aee6-34cb713ae6fb | -12.24573 | -50.39396 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 50481fbd-3f01-3c98-b51f-bc8dcfeea051 | -12.23877 | -50.41493 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a6a662-2166-3093-a713-418aa1d0eb55 | -12.25733 | -50.39932 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| a657ba25-b4a3-334b-ba64-62d6d278b237 | -12.2417 | -50.39337 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f87cf32-4813-30ba-a44b-926cb4b7f5d8 | -12.22203 | -50.38682 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ecec395d-c864-3246-a99b-b77adb997dc6 | -12.26941 | -50.40108 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5be2a4a5-f898-39b5-b251-16080627e2da | -13.3116 | -45.54248 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3e25271b-e51b-3153-9cd0-01783338963f | -12.25536 | -50.41369 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d77467e7-871b-3cd3-b8d2-48f63b90c164 | -12.22621 | -50.41674 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6de6f605-cf29-3f0d-8f66-82bf0761beef | -13.3055 | -45.54551 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c3a1c734-6754-3593-ab3f-a84e28ff8147 | -13.31024 | -45.55418 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c920aa3c-35db-38b2-b3e3-1c63cb27d2d5 | -12.21397 | -50.38564 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 485a4362-1332-3969-8d74-ae0e690a6cf0 | -13.31115 | -45.54636 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 58952ffa-0665-3a92-9873-7bc0c4b105d4 | -12.26136 | -50.39991 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 5ff1523d-1836-367d-9eb0-4a939ec061f6 | -13.3679 | -43.63656 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3c33076-047d-36bf-a19c-2251331c2ac0 | -12.21042 | -50.38145 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59c257b2-44d1-3cb3-bc27-2a442d64ee55 | -12.25231 | -50.40592 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 184ca258-4cba-3531-9278-cf07143584f5 | -13.30595 | -45.54162 | 2025-10-15 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ff2c0bec-d1b7-3d9e-bc9c-13919b346b1f | -15.86934 | -53.9756 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bde371d-cdd2-304c-923e-dee3c539259f | -12.25831 | -50.39212 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 841a46f8-afe7-3399-9b52-9d2b04ca10cc | -12.20471 | -50.41349 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc32c3f7-e09f-3e6c-883c-e3a51e689547 | -12.2644 | -50.40769 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 36b82ed1-f79f-3a89-a486-418a21246175 | -12.27394 | -50.39808 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f41aa585-5eac-3c02-9c4d-ca628ee37dc9 | -12.22669 | -50.41317 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22974e1c-b7de-3934-9be0-66c75d4c70d1 | -12.21011 | -50.41439 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cef5dff-c4de-3e67-94df-5813d33ebd42 | -12.26037 | -50.4071 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 775f3fad-6a8f-3deb-97d4-8e029df02961 | -12.21445 | -50.38204 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a78e6f78-c86f-3bb3-a97c-e55dbd9d6914 | -12.24121 | -50.39697 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 317add7f-b78e-388d-b9d2-86e35d403dbb | -13.23502 | -46.54458 | 2025-10-15 04:59:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27673a80-ae82-332f-8e76-0fd87a67f277 | -12.2639 | -50.41129 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7578cf2c-6b3c-388c-adae-177cd44b3dd6 | -12.25379 | -50.39514 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 15724703-c0cc-3d7f-b052-3dabbfcde198 | -13.48584 | -43.70473 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 080ff1e4-68f6-333f-a0fb-a75f17c546ba | -13.47751 | -43.69925 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c001a7c9-8581-3a4a-a03f-2d05c7304673 | -12.25683 | -50.40292 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76fb88cb-cd4f-32ba-bb0e-5e00e6a46fb5 | -12.2106 | -50.4108 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02ed71af-b36e-3bd8-9a8d-e69ee4b0b59e | -12.24323 | -49.36214 | 2025-10-15 04:59:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f25c5ff-06c2-392b-8dae-c826be630874 | -12.26743 | -50.41546 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a56e3771-2bd6-3591-873e-56b7c89ee7ea | -17.21118 | -47.65498 | 2025-10-15 04:59:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53f37b32-d205-3067-81ed-18807b115a72 | -12.26588 | -50.3969 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 9434e75a-9f2a-357e-ac6c-bb071eddf114 | -15.87281 | -53.97613 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e232c41-c2a8-361e-9a33-85b5d5e3fb76 | -12.70465 | -62.18805 | 2025-10-15 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43afed73-3b87-374f-8185-2344cab6ac8e | -12.26892 | -50.40467 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 393606e3-770c-380c-b8c7-5959b3eb320b | -12.24524 | -50.39756 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 56fa57e1-0b18-3317-81e1-90f8f88242be | -12.58928 | -62.02354 | 2025-10-15 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc539a9d-a4dd-354b-a930-96ff0538770f | -3.564 | -51.1104 | 2025-10-15 05:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6ad126e7-18e1-3a45-a767-049d395a8c9b | -2.8147 | -49.1993 | 2025-10-15 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8a3d4754-82cc-3b4f-bf92-fc5def38f0c6 | -21.95484 | -57.31701 | 2025-10-15 05:01:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8af131ee-1b34-3e46-af11-28fa301b9ec5 | -22.40585 | -55.43189 | 2025-10-15 05:01:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 325a75e6-541d-3128-a4d0-c29f41ea08fe | -19.84669 | -50.63062 | 2025-10-15 05:01:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
