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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 918c5522-b4e0-3408-a03d-b3c3c98695ef | -4.47697 | -42.34653 | 2024-11-15 04:21:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 354fc21a-2dfc-36a8-aec4-2d1ffb57e938 | -2.19162 | -46.15689 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96e20a85-e373-33d3-8dd2-72478a1b13e2 | -2.63016 | -46.18089 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d56deac2-8ffa-3fbf-a3b3-a46914a1f8f5 | -2.65653 | -46.19268 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f0eecb9-a4f0-3641-9071-03d0f3c1a64a | -2.65542 | -46.17715 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecd9428f-4157-3147-9043-90c8b51c96a9 | -3.61284 | -44.79398 | 2024-11-15 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef61f995-c210-3979-924a-3790c2e42d54 | -3.41406 | -40.53125 | 2024-11-15 04:21:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a212cb4-05cb-3c5c-b206-1e9e64e7bb95 | -2.43725 | -46.28704 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d75bcd3-5c23-305c-97fe-d3ba05b666f2 | -2.33041 | -46.86656 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7b2079d-077b-34aa-94ed-a9ab83c29478 | -0.95835 | -47.88213 | 2024-11-15 04:21:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b149084-9a3c-3f1e-8373-c160871b105a | -2.42292 | -46.27291 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f80dedcf-f2ea-3823-a83e-ca11b02bd98e | -1.09355 | -53.17799 | 2024-11-15 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0f8c66c-fbf0-380a-9683-b8ec4ebb4fbe | -1.92239 | -45.57021 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 603ba686-58d4-3646-8a6b-98d42f0d248a | -1.90768 | -45.45649 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7857ad7c-aa8b-39a4-9a75-3d59325405f2 | -4.39865 | -43.70282 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bec58e7-dee7-3a81-bce1-c58d62fe6be9 | -2.9046 | -46.85762 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98cc9563-13a3-365f-8f6f-42bd1fcec73c | -2.88625 | -42.5815 | 2024-11-15 04:21:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94a55bee-6458-395f-a9d8-3a8d165524d9 | -2.23721 | -46.83671 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17af3f56-d0aa-3a88-9f0c-b2bf413f3076 | -1.85548 | -47.82809 | 2024-11-15 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c24169e7-6a29-3c4f-bdf4-3cc66857af78 | -2.6399 | -46.18624 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7adece2f-49c7-393a-9106-f1f63a622da3 | -1.9854 | -46.36729 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d34a39b-6148-3c7b-a6bd-8122de2c760f | -2.65484 | -46.1809 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93242b71-b362-34e0-9774-dde8d5046d19 | -3.79254 | -43.90644 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53a0a285-f2db-347c-b6c0-79f86bd8f712 | -2.63646 | -46.1857 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35ec28f2-c4b2-39bd-8c97-78ba8acfec32 | -1.93025 | -46.27669 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0796d69c-3d33-3a30-a4e1-91295554c3dc | -1.46004 | -48.19736 | 2024-11-15 04:21:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f50a24-27af-3593-bca7-1dbec9be4d32 | -2.66114 | -46.18571 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd289c88-45cc-3c6e-932a-e99dd841c740 | -3.12282 | -45.2739 | 2024-11-15 04:21:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76b3e5a4-b925-36c3-ae74-01fd714ad89d | -2.63302 | -46.18517 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fc8cfd6-b726-3ad5-8e79-e6f2bf53378f | -2.23697 | -46.83558 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f411ca-6b43-318b-88bc-5da47113eea0 | -3.87763 | -43.31134 | 2024-11-15 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b9cc686-08c0-3e0b-a73b-75738199a10e | -2.64679 | -46.18732 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13d7930a-122a-3832-8ef4-1bfb174a63fa | -2.6514 | -46.18036 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19009230-ec02-3835-9c0a-f53d471e3690 | -3.61711 | -43.78702 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ad8d24c-961c-3f91-ba38-91fedc5c6ab2 | -2.66517 | -46.1825 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b1b8442-dac6-370a-887f-dcbf5605d721 | -3.44699 | -44.96325 | 2024-11-15 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7be5aac-b8db-3488-aa92-2c7295649d93 | -2.66341 | -46.19377 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b4d1f14-be2a-3cc0-a003-e57733e86b30 | -2.31161 | -45.06457 | 2024-11-15 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1f19f3-ce73-3d43-b4a6-61dc692b3c71 | -2.09781 | -46.33341 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec8b90e6-4f28-395e-a425-8a2a57d9aefc | 0.12244 | -49.84956 | 2024-11-15 04:21:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae510738-0b69-350a-a964-db47ebc4427b | -4.36974 | -43.66986 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 419f6a09-0576-360e-a285-abb76c097e2d | -4.07258 | -44.13662 | 2024-11-15 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fc01c8c-f426-3582-abf9-006e7af7bf95 | -3.71012 | -41.69309 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| df8f0779-4a03-3585-9541-c57c84d5327a | -2.20703 | -53.71602 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02752d5f-735d-36c1-beae-f21e3b641034 | -2.42351 | -46.26909 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04b5fa98-cb76-381b-8c5a-8683f1e0f7c8 | -2.63528 | -46.19321 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 561e553d-1f5e-359f-b12d-04b363eecdc9 | -2.03498 | -46.43832 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f2cae0-aba5-3423-9327-d88ad96d0aa5 | -1.8045 | -54.65953 | 2024-11-15 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6503e00d-1dc8-3b94-83a3-5a3a10268d15 | -2.66409 | -46.18587 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d30c0c4-b601-3efc-88de-da67e2a5df7b | -2.62042 | -46.17554 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e575710e-0ddd-3a60-9c4b-58cd75fd93ca | -2.78792 | -45.95774 | 2024-11-15 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e27b139-9206-325b-b4c9-a9e271e41d32 | -2.3947 | -45.89333 | 2024-11-15 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4928f85-38a3-3bd8-9cd8-b17daefdfc26 | -3.88933 | -43.15059 | 2024-11-15 04:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f3eef9a-b22b-343a-8a69-0afbdf4f7b8a | -2.66229 | -46.19714 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60610c94-1288-3f13-8857-8feb73c18d5c | -3.88543 | -43.15361 | 2024-11-15 04:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0667017b-5d55-3bc5-9f42-43ffb6fcb68d | -3.61615 | -44.79449 | 2024-11-15 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 121232b7-5c74-39f9-8074-e05a1c3e9e4f | -2.66289 | -46.19338 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a6ed644-37b0-3cbd-8295-d3a7822e2727 | -2.64342 | -46.16377 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a8814f9-6420-3855-a31b-5eb0c0bff233 | -1.90964 | -45.45359 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e18da6ba-f274-34fc-9f1b-a9cc624a81ff | -3.79585 | -43.90694 | 2024-11-15 04:21:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8071d58-e137-3ffe-b818-fdfa6c60777f | -1.71248 | -46.16534 | 2024-11-15 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 474403cb-0743-361c-b252-74ff0a951fca | -2.65601 | -46.17341 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 684393b0-bfd2-3ff2-a353-7118fc2e384f | -1.90668 | -46.77134 | 2024-11-15 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37207fef-372d-3f52-ba99-7f8e5289d10c | -4.37307 | -43.67037 | 2024-11-15 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7af0efd7-1144-3916-a6f9-c583f434ffee | -2.09304 | -46.3642 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b06c685a-0bca-33cb-ae70-81071603c6dd | -3.97988 | -44.08005 | 2024-11-15 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22fce469-051d-3cf2-b774-300fd127f1b5 | 1.06858 | -51.15146 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cb2dcae-78c6-37a4-9432-0b32f81ffed4 | -2.20668 | -53.71371 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8be88c16-5f7d-3936-a964-69569808b5f5 | -1.90486 | -45.45237 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f496875-1f95-3e4f-ba29-bd63dbe6144b | -2.32686 | -46.86601 | 2024-11-15 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc74f825-0ca9-3613-aa9e-87b1cdf87f19 | -1.97045 | -46.52824 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e1f8e49-a052-3f31-88f5-1e8262db8b49 | -2.33943 | -47.2205 | 2024-11-15 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1df663b-0748-32dd-8408-534f05009728 | -2.24179 | -46.37094 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8865fac-2ba4-315f-9f19-296cd4253a73 | -1.90824 | -45.45288 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12f64f9d-d0fd-39da-ba8b-28759f28401b | -1.85915 | -46.28604 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 094dc324-ed01-3fec-87a9-aba4504511d8 | -2.65426 | -46.18464 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44fe0146-3c2a-379f-91ae-25a9b8fb1d81 | -2.25084 | -45.62471 | 2024-11-15 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc3d1885-0b06-3a26-8b37-3e1d5471bb81 | -1.57562 | -53.79977 | 2024-11-15 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c546630-0ccd-3171-9d12-e26ad56278ad | -2.65315 | -46.16913 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2299390b-b4c8-33ef-9655-197c31965302 | -2.63947 | -46.144 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507b456f-1a3e-3f94-912b-c58a8cd7c662 | -2.64627 | -46.16805 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1a0e16-703d-36bd-9aa2-d22e55030f11 | -4.02078 | -38.24755 | 2024-11-15 04:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| f4c2cad1-7ecc-3814-ba74-966c02e8570a | -2.65997 | -46.19323 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec16e872-4d1f-3def-8c26-bf5db861c5af | -2.65828 | -46.18143 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55f351f3-98ed-3ba0-abe0-a26dff6aceeb | 1.07593 | -51.13363 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 217756c6-c52b-3af6-abce-ec1fbf6ee493 | -1.85627 | -46.28165 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0612b97-07fd-3898-8330-d845170229c0 | -2.14158 | -46.40722 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70f9f2a8-5648-335c-aff6-80905abca6e3 | -2.64393 | -46.18303 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec4313ed-d672-33a1-8a53-685c986c2734 | -1.8038 | -54.66385 | 2024-11-15 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58525785-c44f-32a4-9133-f97c7321e9fb | 1.06776 | -51.14604 | 2024-11-15 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdb45b42-8497-3e0a-9efe-a99ec70b8f8a | 0.43635 | -50.92741 | 2024-11-15 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ddef4953-8b35-312d-b155-20df79ce34ef | -2.71733 | -44.77779 | 2024-11-15 04:21:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2a9cd01-1e07-3785-8e0e-e7de38029137 | -2.65309 | -46.19214 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 217c7fac-f9ca-3337-8310-24060b989c26 | -4.20192 | -43.76505 | 2024-11-15 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7c4247f-30ee-3221-864d-a3ab7882bba1 | -1.90907 | -45.45719 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad50035b-cbd4-3f50-aa46-78bc1d39e1c3 | -1.91957 | -45.56607 | 2024-11-15 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c53906e-c45e-315f-9908-d176d31df853 | 0.44114 | -50.92664 | 2024-11-15 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7a31f41a-e22b-3db2-bc92-8bffa86ff0c9 | -2.63137 | -46.52401 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117a31cd-72fc-3bba-9512-df018154a9bb | -2.61639 | -46.17875 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44a6a66f-1b45-327e-84aa-e5f1b9009ab2 | -2.09553 | -46.3252 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
