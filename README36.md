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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e618b274-595c-3e0a-bbf7-19297caceaeb | -3.21776 | -48.61372 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec0598e-89d6-3943-bc99-f129f861797e | -3.21722 | -48.61715 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4c10fe9-d6e1-31cd-8767-54c47b31fd03 | -3.21446 | -48.61321 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3fc8ba4-efed-3886-ac0a-9db082cb8095 | -3.21392 | -48.61664 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e0b5fe66-65a1-359c-ad28-fefd9bd1af6b | -3.21338 | -48.62007 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35270855-71aa-3b92-857f-5d29603f72f6 | -3.21115 | -48.61269 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c52dc56c-29f8-36d5-95dd-87e09dd52ad7 | -3.21061 | -48.61613 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b618fe81-1182-357e-8dac-5bece5b0e98c | -3.21008 | -48.61956 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f284aad-97f4-393d-8fe4-130e6235ebab | -3.20731 | -48.61561 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c8e133a-f87f-3532-b870-7b37fc8653d5 | -2.87286 | -48.90776 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 325759ec-a7f3-3ad1-8449-4a9fd5976b15 | -2.84844 | -48.45694 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50aef0aa-bc51-3cbb-9154-82db6c7a3e56 | -2.80127 | -48.6711 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e04c590e-5c6e-3e50-b1e3-71f71830467d | -2.79965 | -48.6814 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3faad762-eba3-3e43-a1d9-12b025433f36 | -2.79911 | -48.68483 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ecb4f0-06b2-3042-89e5-029a2290c4a0 | -2.79797 | -48.67059 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5495bd9c-a4e0-3af9-9a0c-f7a5205fc7b1 | -2.79635 | -48.68089 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f752456e-a2f4-3cc4-abb1-06f219a55a79 | -2.79581 | -48.68432 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b27f5bb-e3e2-3390-ba6b-6df433548e83 | -2.77225 | -48.65942 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9957aa63-1ad7-35b5-ba33-d15714804576 | -2.74482 | -48.68328 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ebaab4c-844a-3d8e-96af-d4de0ba648b3 | -2.74152 | -48.68277 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 015a96f3-7e45-3fef-bf8b-191e8681f55d | -2.73822 | -48.68225 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98cd9172-fdbf-301d-b175-2f8925085522 | -2.73768 | -48.68568 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d75a27-4247-3a81-a4d4-cb8d7b7d7aa8 | -2.73492 | -48.68174 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eee6fdac-7b4a-35d6-87ce-69bb76239f7e | -2.73324 | -48.67093 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7767ce27-6619-3696-9070-ae4896247465 | -2.73162 | -48.68122 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9409031-5622-38fb-8ee3-0c6d8245fe75 | -2.72993 | -48.67042 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73644ff2-e632-31fb-b97e-e23798942ecf | -2.63043 | -48.52507 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9e6ef0-5793-338b-ade6-71413aaa7a97 | -2.62989 | -48.5285 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca6aecd7-21cf-3cba-aea9-a01a171f0f5f | -2.47732 | -48.05005 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1924e50f-4f28-3342-b319-d9d92027cfc3 | -2.47595 | -48.48996 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea1d6594-b9cf-330c-8fb5-75114515f793 | -2.46093 | -48.43491 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 123b2821-22ff-3d4f-a946-26770ceb19a3 | -2.43539 | -48.53286 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c4b1e16-8682-3b81-8f86-5a81fd979e48 | -2.4325 | -48.48673 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91d775d-d5fb-35d0-aa03-616cea5661aa | -2.43155 | -48.53577 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 315d3eda-2fd2-344b-b1b7-14142088ecfe | -2.42273 | -48.52738 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d617e474-aa37-3742-9a5b-5869e41d34ae | -2.41754 | -48.45278 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47ee2715-1015-34e6-a935-1914ba5f4c60 | -2.39867 | -48.16127 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed3354aa-f336-3c23-9c89-9acfc13a0bee | -2.37813 | -48.50991 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5defcc7-f909-3bea-9990-3e7274d0998f | -2.37759 | -48.51334 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b790c873-d924-3ea5-a563-6f346a1e80b4 | -2.31911 | -48.58144 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08546540-5e0e-3853-9ef2-6a6c512321c9 | -2.31211 | -48.45387 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df10ca9-626e-313a-be93-d1608c07dad0 | -2.30591 | -48.57938 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81ea89bc-0208-3b82-825a-0d32abd88044 | -2.30261 | -48.57887 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3a7264-e550-31fb-8fbb-40e76bd04707 | -2.30207 | -48.5823 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6de46f8c-ed8a-33f5-8fc2-00dc4ebe1063 | -2.29823 | -48.58522 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3829a9d6-cc51-3beb-aed5-bb24ecbe7336 | -2.29493 | -48.58471 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59242e3d-ce65-3f2c-afd7-40572044036a | -2.29439 | -48.58814 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b04880b3-c7aa-3bc8-b0be-8892d8967b94 | -2.1419 | -48.51889 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b1d925e-0581-3073-8bb5-468c3a169d5f | -2.1195 | -48.81433 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 893df325-f9c1-3b21-8598-b5c08d673770 | -2.98419 | -48.60857 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71bd4ab1-aed0-3d73-bf81-45da9849564e | -2.98088 | -48.60806 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f955defb-9488-3b6b-983a-2cbb8779f809 | -2.97489 | -48.6247 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb22d86-6927-3a30-a65c-0cf15abfadec | -2.97435 | -48.62814 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1c8ada4-3d63-390a-9556-811fbafb514c | -2.97212 | -47.99252 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6475b56-f6a5-3bcf-b4e3-3fab8ef4657f | -2.97105 | -48.62762 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b935f68-c0b9-3433-9710-203c970beeaf | -2.9688 | -47.992 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1e3d45b-76bb-3ed2-99a3-01ab69470254 | -2.96826 | -47.99546 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bb189f2-9ce0-36d4-848f-75ef3d41782e | -2.9672 | -48.63054 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6712b0b0-d07d-32cc-8cd5-3bee562e33b6 | -2.96495 | -47.99495 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 021646a2-8a81-30d7-80ae-8c89469f8768 | -2.96217 | -47.99098 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa0ee5cd-1d89-31c2-8e7f-5fe9f423a84f | -2.96163 | -47.99444 | 2024-10-21 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c80c627-ebee-3e5c-9bf7-f8bb83764ca4 | -3.98884 | -49.02671 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7249267-68db-32c4-a2e8-f768c5dd80c7 | -3.9883 | -49.03015 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb34fccd-02de-355d-bb62-a2495ee382b6 | -3.97563 | -49.02465 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9161a1-e11d-33ea-9464-de3f579cf513 | -3.93414 | -48.94426 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b2d3f5e-a234-3fc5-a5d1-96a25fe0666e | -3.92402 | -48.33582 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37547bbd-f438-320a-ae16-634dc8087c8f | -3.92349 | -48.33928 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad61a211-f593-387f-817d-d48b7003034a | -3.91856 | -48.34912 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13063eaf-0e57-3981-9b50-1735b1a5bb4a | -3.91402 | -48.33416 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d067fcab-b9d6-3424-b308-c767852f97c0 | -3.91348 | -48.33763 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 140fb5a1-7247-3e13-a9e5-9de9f2ea2682 | -3.91071 | -48.33365 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3756cf90-f4aa-372e-b3c9-5e0895fd898d | -3.91017 | -48.33712 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32818fb1-9e08-3732-8aa9-1a5c41f485ea | -3.90969 | -48.36179 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 942b6c45-fe3e-3f3f-b840-808270f5af12 | -3.90914 | -48.36524 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0939af49-f4db-3242-ac45-89396c7c0e3f | -3.9074 | -48.33313 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91fe0cc2-1e9b-321d-9e0d-a8dfd9796954 | -3.90686 | -48.3366 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb6ca387-6c27-3248-91e5-231f26d011c5 | -3.90409 | -48.33261 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7aaf377-efaa-34bb-9305-3dacf0d750e5 | -3.90355 | -48.33608 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a487a51d-6c1d-30cb-97c8-020608c1135e | -3.90132 | -48.32864 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ee01a55-069f-3b3b-9963-d925520786fe | -3.90078 | -48.3321 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f863beb2-690a-3687-a3a9-4ede7df4ef50 | -3.89747 | -48.33159 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c00c6c6-a9f1-3ba8-b315-c2d05520c0c7 | -3.8947 | -48.32761 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdd75389-5d09-3df6-ba49-7061f14ef005 | -3.89139 | -48.3271 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f51916-a08d-3d2c-bd43-582ce9c8bb60 | -3.86726 | -48.37289 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf0aaf8e-8917-3e45-acb5-9f7171580c73 | -3.85237 | -48.98741 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dce6684b-b177-3bb6-8e8a-024d7e4ef2bc | -3.85183 | -48.99085 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae30362-15a6-3218-845c-0bae608a81d9 | -3.84906 | -48.9869 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f68de6-84de-3ef2-b2da-5a8d1dd33309 | -3.84852 | -48.99033 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dae57cf0-be4c-3969-86a6-386ecb352c57 | -3.83502 | -48.88264 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70b41590-c520-35bf-a26a-2c5f1b6b9733 | -3.83448 | -48.88607 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318d4e72-29cc-3673-b4f0-701c31d1b37a | -3.83135 | -48.88195 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d6df4c0-8e8a-330c-968a-cdb1589ec55c | -3.83081 | -48.88538 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 035cadb6-0fc3-35a7-9371-7e1bc6161fd5 | -3.82637 | -48.87061 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae68bc38-5742-3a37-8da5-46e008f9f8dd | -3.82307 | -48.87009 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef1ca208-66de-3c65-bb4a-f1ec3f3a349c | -3.82253 | -48.87353 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b982c812-5fc2-3a38-84d1-ef0fcef6c8e7 | -3.81977 | -48.86958 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ccfa11-cdf5-36a6-bd6a-bd6d4773f884 | -3.81923 | -48.87302 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebcca781-782f-34e5-ba12-ec5c4316ab58 | -3.81869 | -48.87645 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0ae648-df34-3b48-a9f6-8b25ce55f9c8 | -3.81592 | -48.8725 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf1bf486-db15-3379-90c0-eb9ab4af1774 | -3.81538 | -48.87593 | 2024-10-21 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
