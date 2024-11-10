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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ec7aef9-a0b4-39bb-ae2d-7aad377adf5a | -2.39717 | -46.78661 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15f054d-0edd-360e-a436-1dbd53c1b99d | -2.16064 | -50.19576 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bf3a2cc-05c7-3447-b545-e30bdb90e42b | -2.67541 | -46.79132 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7981ab03-89d2-35d0-837f-10cf3776990d | -1.82901 | -51.35149 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ed22c37-c97e-331d-b38f-71c38885eb02 | -2.36428 | -46.79645 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba03ee4-fd26-3444-a6ec-880b3d0b6481 | -2.35345 | -49.08338 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fec52a04-d59e-3bbb-b61a-25c130dad78b | -2.36409 | -48.8861 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd368939-2d21-3478-8237-03f90f9dabb3 | -2.21181 | -48.37077 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fbd0d5f-53f8-336f-98f7-154145864e8a | -1.2135 | -53.66292 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb078f8-470a-3151-9ed1-5a2eaac05eb0 | -2.10146 | -48.89788 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb5c391d-1b82-3358-bcd4-2eb54e4d6e2f | -1.47741 | -54.30325 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f710bb84-109f-3752-a193-c36fb50807f8 | -2.30756 | -48.53746 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36b13089-b5fb-317f-9d4c-98385900d855 | -1.63881 | -48.20715 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b00d0a12-5a6b-301c-abc8-6000f70a39eb | -2.08945 | -48.82878 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40ed1d68-e5e3-31fe-9c23-f63ce2ea1e36 | -2.42545 | -48.47508 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 017efb4d-db11-3198-ad89-a10a3cde3300 | -1.63998 | -50.43694 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c8919dd-2136-30cf-8422-394036c88fa8 | -2.17918 | -48.36217 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f7dd549-6805-3c19-87eb-4121afb0b7fe | -1.87183 | -50.79005 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e453599a-f6ae-378e-a3b4-8fdc73052033 | -2.23168 | -46.61547 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d2b7f82-c60f-3cd3-84b1-c858846ec53f | 0.78548 | -51.97432 | 2024-11-10 04:36:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e6a4fcb-3049-3f8d-a3b8-650e87a54474 | -2.3379 | -48.51746 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8029b48b-c9f6-3e61-88fc-aecaf066d036 | -0.10623 | -51.76034 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69156602-308a-3c88-a0d8-3331f5326442 | -2.08037 | -50.34641 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c12c252f-c0dd-3a9d-a174-539b241706db | -1.58884 | -50.4368 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 402ae3fc-ca72-3652-834f-92317cb1e1b0 | -2.15262 | -48.74643 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b8e2512-d318-363f-888c-b9c0af2235fb | -2.36708 | -46.86744 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8e75137-50aa-3b29-9c4a-6559b3f40bb1 | -2.3966 | -46.79026 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e95ba1f-ce86-34e0-a780-9dec34e5ef34 | 3.37605 | -51.27593 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50560ccf-a60f-315d-958f-cf9728e6553b | -2.28469 | -48.46684 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d691934-d34a-3279-981b-8a801a7a1566 | -2.62908 | -46.14106 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8644316-cf4b-3fa0-b12a-41194e80dbde | -1.69275 | -50.02189 | 2024-11-10 04:36:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53a60e83-4d95-31d6-bee5-08853ad46611 | -2.1247 | -48.88022 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdd35361-b583-3277-9e21-b3a043e795d3 | -2.19908 | -48.36526 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6546c9fb-64b4-3813-9587-8db445442ea9 | -2.05249 | -48.89042 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 381d10ce-6c7c-36a6-b686-088a073a93cf | -2.31161 | -46.09083 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 807ba05a-af13-3c43-976b-53a345bb4608 | -2.26881 | -48.71862 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4643f032-baac-31c6-a08c-19c979f0e1a2 | -2.28533 | -46.51809 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2320f78-9f77-3b19-853f-ab1ef075d9b2 | -2.03207 | -50.89393 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 83a204e8-0e2a-35d3-aeab-ff08f5e6c8cd | -2.2483 | -48.37645 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14241ee4-9f21-3ffb-818c-ae442eb21070 | -2.52278 | -46.38183 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6968c48f-d00d-3434-ba5c-0d020cbf2c95 | -2.20216 | -48.86044 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e1c541-c700-39e0-9ebe-c2fe9bbc40ac | -1.05408 | -51.7452 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be769641-50da-383e-a37f-bd381732fd83 | -2.10659 | -45.33326 | 2024-11-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50754cdb-ef01-3973-a68a-59c553fdad9c | 2.42391 | -50.77411 | 2024-11-10 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e8cc65-772c-3449-8a3f-e51a62a276f4 | -2.38198 | -47.9343 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaa481d-96bb-31f8-9d23-280ac8b116b5 | -0.97939 | -51.78314 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 000ec3e1-da45-316c-85f2-1f6694188236 | -2.24775 | -48.37989 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3460276f-62b3-3a76-9681-a9d9f33e3ee5 | 3.37531 | -51.27124 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 362079ec-b99b-301b-a874-0e6d400f644c | -2.14008 | -48.37736 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f251a83-fd3b-3e09-b3a3-324d1d6fb19d | -2.23225 | -48.37043 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7877b7-3fb4-3336-b6d3-fef791407a8d | -1.60839 | -47.34423 | 2024-11-10 04:36:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd40ea17-bdfe-344b-8bb7-6abfcf269ecf | -1.69941 | -51.08378 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78bda0b5-7ccb-36c9-b043-09dc35621f7d | -0.04143 | -50.78338 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f6e71d9-2e00-381f-b00c-e0efd9d10e4b | -2.12437 | -50.13733 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 194b3368-2955-3523-ab67-a7cbf14de36e | -2.37255 | -47.92929 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8523ec7-839d-3f60-b75d-f17865a2e1b5 | -2.19353 | -48.35735 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbbb526d-7323-3693-9eed-b7000e229275 | -1.6124 | -48.67595 | 2024-11-10 04:36:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7a97a3f-e0a6-3abf-ab29-4c4b9bdc1365 | -1.53968 | -52.21706 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba881590-a325-3601-acbd-410ab95806ca | -2.24705 | -46.56133 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa7a3953-9dba-3820-9bef-681b47a34a50 | -1.83383 | -52.01637 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3f17bb7-28c1-3af3-ac0e-4ea23de5522d | -2.63818 | -46.76311 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1bc0704-3514-334d-abe1-71d2915f5b0e | -2.17742 | -48.33014 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5577a6b4-7e18-313b-90ef-37c7789aca1c | -2.40959 | -48.5326 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88803e03-6464-356f-8003-75a41647dac8 | -1.38756 | -51.57038 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45674fc1-762c-3684-9b12-315e0c902f8d | -2.18928 | -46.77686 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdaa57ce-cb5f-32f4-b7f8-1cef143aa562 | -2.17688 | -48.33358 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9cfafb-ded4-36de-8ed1-14b5b9db8045 | -1.34251 | -51.43036 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91545d5d-e25c-320a-959a-e33253e1808c | -2.073 | -48.89006 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e34918-5e00-3d73-923c-09f6d0bd1701 | -2.22237 | -48.39006 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1803c7d6-d8cd-39a6-bcd4-308d14487621 | -0.14998 | -51.5596 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d7fd3f7-44c5-33e8-aaab-9fe8ea505f24 | -2.14151 | -50.27224 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03e43e07-6eec-3397-836f-20bbbd6a93de | -2.33924 | -48.59533 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c71e46d8-8690-354d-b0d1-ef3ee7391b7a | -2.05642 | -48.90878 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ba4a133-3076-3464-b954-829297e61994 | -2.56823 | -46.53732 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9acafd7-622c-352b-9b78-ce42ba3f90cb | -2.23182 | -46.55133 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe04dca4-1791-3bc8-b077-7ac30ddbdcce | -2.22417 | -46.42117 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7718c121-1ebd-33e1-824c-84d84e6e8f7e | -1.11491 | -51.92538 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47314c63-93ac-32a5-aac5-b27c97180329 | -2.17437 | -48.41433 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 754b08a2-8104-38e0-afdc-5bf14f8bd0fd | -2.42254 | -46.30949 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| d17f36b2-75a8-33ec-9f1d-80021d8b5e4d | -2.26871 | -48.48199 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b4ed948-680d-3150-92da-037e22e55056 | -2.22644 | -46.42916 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9105fa66-22b8-3a6e-9148-b8852e5d8e79 | -2.11193 | -48.21069 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b14a9bf8-cae5-3a0d-85f7-7abf712dde64 | -2.36936 | -48.57222 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a6f5d53-8bea-3218-aed4-a8345a13b9c7 | -1.22373 | -54.17523 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b602ba54-880d-3a52-bc92-5b7731403f6e | -1.16222 | -54.07663 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa6fd7c-228f-321a-8524-28eebffb07a0 | -1.1576 | -51.99671 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c91b8a46-3483-357d-bbb1-359a4cd5394c | -2.14696 | -48.69603 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e96385d7-1572-3b4e-9187-839ad3291d79 | -2.16914 | -46.4127 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ba2a01e-61c9-3003-b6dc-0ec492c7f9f8 | -2.35733 | -49.08043 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f6ad002-db63-3910-8458-755ee8fc7a5f | -2.24648 | -46.56501 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a69e598-6bcc-32e0-a3f5-e6d1ccc79f2d | -1.39676 | -52.3635 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ea54697-092e-3760-aa0e-a18a7403fb7d | -2.14767 | -50.4567 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3d48e10-b906-3f39-804e-e97af33760f1 | -2.6862 | -46.81169 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25ab541f-2619-32a5-a1e7-0e679569ae7c | -2.37161 | -46.86072 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a62eadb-6a32-3f88-a7db-c485c93cbfeb | -0.41049 | -51.93447 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae1ad28-a9f3-3a56-9f7f-5e6fa87e0aad | -2.29874 | -46.72326 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb86c6c4-3f2b-3a80-a621-57e51cbf8479 | -2.63078 | -46.76574 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cce788d-89b3-34ff-a4b4-b287665002dd | -1.40369 | -52.36942 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11e792e5-7ee3-3a72-84de-b9b6549118ea | -2.04719 | -46.07911 | 2024-11-10 04:36:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02151dcd-3813-3a33-aca8-c1fc2724011f | -2.18084 | -48.54588 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README59.md)
