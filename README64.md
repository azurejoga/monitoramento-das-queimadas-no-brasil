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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32cabe33-3e2d-3074-a28d-0aa8fca61bb3 | -10.85748 | -68.25235 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2241bc87-a432-35e3-b545-9bb59e299991 | -10.85583 | -68.26317 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4656039d-59c8-3d23-aac9-8be2888823a6 | -10.85529 | -68.26676 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74378aae-3a87-35f7-8f4a-68efd67732f6 | -10.85474 | -68.27037 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bde27219-fe76-3efd-b083-2a9af50e5bb0 | -10.83071 | -68.27757 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74cd094e-87e1-32f7-8f47-aebaf5e8008b | -10.82153 | -68.35338 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8d2c7fb-2b5c-3814-bfa1-a24372ff6aea | -10.81908 | -68.35288 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfd6b634-e8ae-343e-a498-985a839dd856 | -10.77269 | -68.27579 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac90e801-ee03-3dad-8429-e5e8f1e4f353 | -10.57488 | -68.14927 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1042d3-1b6d-39e7-a482-ae9d06d953b8 | -10.57098 | -68.15235 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41ac8c5f-e4be-395d-b3cf-bd4c52ecc9d5 | -10.50069 | -68.10473 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 448de841-691d-32fd-9500-ec37a86f6be4 | -10.45456 | -68.22642 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10f55e25-d5cc-3800-830f-23b86b5af19e | -10.41332 | -68.22726 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb1bd9f0-1e48-3f7a-8bb9-ab63373874f6 | -10.35919 | -68.07215 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8a226c-939f-367e-93a7-638f0dd18d40 | -10.35864 | -68.07576 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff69d2a7-6d73-38b8-9df3-4629e3bda555 | -10.35583 | -68.07162 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16088df1-aa34-373b-8753-c6da3730acc6 | -10.35247 | -68.0711 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be56d7ea-2c60-3247-92df-bc5767e3f23a | -10.32788 | -68.07465 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 646a63f3-b29e-30c6-b414-afed93a83e56 | -10.32507 | -68.07051 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb4539ce-acdb-3bfc-8748-449d546c12e1 | -10.32475 | -68.03751 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01813090-120d-3997-aee3-4928494ae794 | -10.15828 | -68.3666 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5017e750-331c-3634-a752-02fae5265491 | -10.15495 | -68.36608 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0ff3ed6-3c38-39cf-8703-b43c7419f392 | -10.13816 | -68.29794 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 730340ec-e700-3440-8c1a-0a071ba958da | -10.78421 | -68.48991 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f36b1405-b8bc-3b4b-89b2-16decd08f1e1 | -10.78088 | -68.4894 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66d17c01-a432-3785-a0b7-881e5f5100d6 | -10.769 | -68.8068 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64a3fb5a-d27a-3ce1-b972-92468ba2320b | -10.74512 | -68.6763 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b87ba20-0c93-3b71-9de3-d99ff9e42370 | -10.73047 | -68.85815 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa599738-9b07-32b4-9730-1b067d56650b | -10.72992 | -68.86167 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abf152b1-05f3-3ce0-aa51-45980887d023 | -10.71511 | -68.62807 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebe16acf-2ad3-34d4-b649-775b2f4f5529 | -10.71065 | -68.61285 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e4b3d2-4447-364b-a334-9117f01f66bd | -10.7101 | -68.6164 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2602d1b-4fc3-3259-8ee2-b2127092fee0 | -10.69352 | -68.63554 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b03dd883-a00e-3010-b039-ed6cc75f3837 | -10.69074 | -68.63147 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f7e514-e3ce-3f95-8219-6aba6e13fd9a | -10.68787 | -68.82617 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf2eeff-81ce-3413-be2b-fcf336b872ea | -10.68191 | -68.88648 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fabf72a-5f97-3dfb-a5f8-ee5de64f1501 | -10.66617 | -68.57327 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fecd774-4b58-37b3-b029-99c66b2f3fb8 | -10.65371 | -68.8712 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19620069-d4a6-3cbd-9700-7bc88b692bed | -10.6534 | -68.74129 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab5792d9-ad7d-3eb8-ab8c-0161ab3452e2 | -10.64377 | -68.86962 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f031c0-e122-3c3e-8f1a-de97467f1af4 | -10.63411 | -68.62623 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42166628-c27b-30e7-86ae-bb1650295018 | -10.62677 | -68.56347 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0aab022-9e87-335f-9035-a3a97ef4649d | -10.62623 | -68.56701 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbfa5835-29c7-3cd4-ba96-88695a6b13e8 | -10.57895 | -68.7188 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d118846-52a4-327f-bc65-4a1a71cbd10a | -10.5784 | -68.72232 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ede6788a-9db0-3e2d-83a4-5eaead798714 | -10.57813 | -68.61379 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a54ba7-1292-36e8-9945-dd44fa81f7c7 | -10.57563 | -68.71828 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f934c444-02c2-322e-ad43-de1cdcbf7a1d | -10.54786 | -68.56902 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 645dac33-f373-3d07-b432-f4dc7fc3e47e | -10.54399 | -68.57204 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e914d5c-a119-3503-beb5-8bc4958109a5 | -10.54066 | -68.57151 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e645b9-9ff4-3a18-82ba-24e2c8149da4 | -10.54011 | -68.57504 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356c1fe9-a36a-36d6-965e-fd082d40c59a | -10.51578 | -68.60019 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d30e7e9-c9f5-3a89-8111-5e76c324b80f | -10.48036 | -68.60909 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 518cca56-e12e-342a-b59e-d1a883870b70 | -10.47394 | -68.4957 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e059d97e-43cb-31dd-8846-f7fa1c88b07c | -10.4657 | -68.72601 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16aa2da6-d7b3-384e-9cff-8a9617632be0 | -10.46239 | -68.72548 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d65ae0c-1114-33da-b0fe-7af09cb1789a | -10.4555 | -68.8576 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2a8356-4f42-3640-b142-729476e67b3d | -10.42063 | -68.46931 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35675fd1-6aa9-396b-ac81-46bcd74aa683 | -10.39545 | -68.61028 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca6ebc8-5c68-3ccb-b566-c81ab8bff8ea | -10.35007 | -68.83733 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a90b4125-c6be-33c9-a34c-3fe3a490024f | -10.28971 | -68.83169 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53cb2333-eee9-32b2-8a82-06ce58374088 | -10.28862 | -68.8387 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9faeae8d-5cac-38f1-8bbb-ee793b8ad999 | -10.28807 | -68.84221 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0820b59-595d-3ef2-9c65-06c7d3d5c7e1 | -10.28752 | -68.84571 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44bfe69b-780c-3470-8612-05422b759c5d | -10.28698 | -68.84921 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b402c8-9313-382d-8a24-78b1cee22e5f | -10.28643 | -68.85272 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b03b9000-2da5-3f8c-b264-dba39f39977a | -10.28588 | -68.85623 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85560459-3972-34dd-a988-e59e2f19fe74 | -10.27711 | -68.60639 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fd6a914-96ed-383a-a402-4015bfc298e8 | -10.26099 | -68.81995 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62dfa017-601b-3f80-8f10-90a5d2144523 | -10.75459 | -69.05289 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a7625fb-f57b-3fc9-90f9-423d0561882c | -10.75404 | -69.05638 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 212fa430-f6e4-340f-bd49-1ef1da7b89e2 | -10.73818 | -69.13641 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a66cda1-84e2-3425-9306-fba307a56183 | -10.65018 | -69.04677 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e91e44c-2d0c-3f8d-9490-62b5c8ab6c93 | -10.63163 | -69.1657 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aebb743b-94a8-3246-9bd8-cf9cb48acd61 | -10.62832 | -69.16517 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9278707b-6401-32f8-903d-541269df54db | -10.61015 | -69.17301 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbcfa00e-c414-32d0-bc60-339f451022d5 | -10.5751 | -69.02766 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a0803b3-c60c-3594-b34b-f5033da8c395 | -10.5183 | -69.02222 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af170674-e094-3fb8-8e14-204d7cafbcd5 | -10.40251 | -69.13249 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c90e0f0-d734-3dea-a2da-8e6ca65c102d | -10.20522 | -69.09061 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09705b0d-6f21-32b2-84b0-95c00ccfa2a5 | -10.20246 | -69.08659 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e33f1ad2-6500-38c2-9112-9213a8bc688e | -10.20192 | -69.09008 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ee062aef-b68e-3b5b-8e3d-91b008019013 | -10.20137 | -69.09357 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47a219b8-1336-371a-9bb3-48b82974676a | -9.73992 | -68.41395 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f788517-c11b-38ca-8018-2653931e9055 | -9.67986 | -67.58911 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca8b1cca-5519-385d-93f4-85394e86d177 | -9.67759 | -67.58128 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a07cc8aa-15a4-3d50-adab-7c21f711f489 | -9.63957 | -68.25329 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b1dfc88-bbd1-37f7-bd31-ca8449a9f2bc | -9.54586 | -67.71028 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 007b1294-6034-35cf-a62e-90e618756b6e | -9.4607 | -67.73827 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a27523f9-978f-310f-918f-c28f75619ce1 | -9.43333 | -68.07192 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e395e1ab-1b5a-3857-9eec-7d5fc61d9ade | -9.43054 | -68.06783 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e4e601e-ba6b-3832-aadd-b2c2e1cb9f70 | -9.41855 | -68.21135 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56eecbac-8944-340e-bb7e-ff91965d0b6a | -9.40965 | -68.20271 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a53e4b6d-5330-3dc0-a203-767f678799de | -9.39873 | -68.29514 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c6325f-7be8-3e39-96d2-685b18fc95f1 | -9.39485 | -68.29813 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7338555-23af-39c6-9e40-a6144a903009 | -9.3943 | -68.30167 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c65093c7-e300-378c-be11-ffc190a4beb5 | -9.39376 | -68.30519 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49e0218-bdc2-36f5-80b9-ee72c8fac24c | -9.39043 | -68.30467 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4a47cc8-78f4-399e-b6c1-69efabe8348c | -10.63209 | -67.84201 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18282374-6c21-36ba-a788-87d90b21eaaf | -10.62871 | -67.84149 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
