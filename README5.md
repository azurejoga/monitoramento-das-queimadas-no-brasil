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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d458d9ef-d777-31ee-96b9-f465cbe18dee | -4.39821 | -43.31844 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3074f30-0c8b-3eb7-b3e0-2ef531e5b399 | -3.58484 | -41.65569 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f806e4b1-38f5-3794-a75f-aacb373e4adc | -5.61958 | -43.64818 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d454568d-22de-386b-8771-2ab95e3e9390 | -6.21104 | -40.9685 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30e312da-0c7e-3229-9761-643db370967f | -5.62637 | -43.64629 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 30bfc718-1bc4-3a3e-b8fb-adfc0bcfe2d7 | -5.62076 | -43.64158 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f85ccef1-ebf1-3140-84f8-70908e4203e6 | -2.9901 | -39.96615 | 2025-10-20 03:21:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b1cba6c-a4ed-3d50-b0b9-1df3adaac0cd | -3.59846 | -41.65273 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 55a1394d-8f34-369c-88fe-7920f2f6df75 | -6.30362 | -40.88808 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 04de671e-bba1-39b8-b96d-adc322c47643 | -7.01042 | -36.74757 | 2025-10-20 03:21:00 | NOAA-21 | JUNCO DO SERIDÓ | PARAÍBA | Brasil | 2507804 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f5b5d3c-d976-3abe-a9ca-61fd9860061a | -6.2126 | -40.9599 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 79dc426e-bedb-3682-8e6b-04aa72f413ac | -6.31293 | -40.90274 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1c6b31b-ac03-3587-8b6e-92296ee5e858 | -6.21534 | -40.97809 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6ee49a8c-cc2c-35e5-b69d-41913785659e | -3.5887 | -41.65713 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 652c1999-91b0-3da7-aa64-62040eb892ae | -4.39702 | -43.32502 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67045006-f94b-3148-a2fa-8b4801ee5115 | -7.02213 | -35.22781 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 632879ff-606e-32ee-8a69-478376c4f6ef | -6.21182 | -40.96419 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c5d9a7a-1edb-34e3-a7a8-8b2ff5c4c808 | -7.01343 | -35.23149 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3b736f32-ebaa-3003-b8e2-ce046f038d14 | -4.39583 | -43.33159 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25937bab-c926-39be-907d-18d232fb3f1e | -6.31219 | -40.90681 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc465d17-a524-3462-a1bc-ba417efe3838 | -7.04411 | -39.22222 | 2025-10-20 03:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 458e421b-39df-355d-9d31-f768ab7bff53 | -7.30493 | -39.27175 | 2025-10-20 03:21:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 201335d3-3cf9-39f7-b6dc-fef69b0e33fc | -7.01736 | -35.23216 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7332e4d9-9411-3110-972f-f7d159375aac | -6.40017 | -38.28237 | 2025-10-20 03:21:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 837ea2dc-2154-3534-9cf6-d8cadf4d7d63 | -7.11295 | -39.43685 | 2025-10-20 03:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bdf5961c-0a8a-3430-b7fa-72e9681f7aed | -7.3003 | -39.26799 | 2025-10-20 03:21:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a0f411d-56cd-35bb-8c77-a12ae9c86894 | -7.04465 | -39.21925 | 2025-10-20 03:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 14e1df19-1238-39d3-ac39-02d79752af22 | -7.01903 | -35.22213 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| b617e3b4-4e14-3514-af44-9d0290538b2c | -6.98542 | -39.6988 | 2025-10-20 03:21:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 760a889c-3302-3808-8f0d-628a9f21c722 | -7.0182 | -35.22714 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| a9cce84d-447f-3976-a3e6-93034d044dd1 | -5.61944 | -43.64505 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc00a9ae-63ce-31c9-b72e-b1e1bbba7e70 | -7.02129 | -35.23282 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 00da4667-83f9-37ae-a6cc-d37cdd6aabd1 | -4.39806 | -43.32165 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5824079-5c3d-371a-a4be-be000ffb08c0 | -4.39578 | -43.3348 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32886fc8-8824-3571-8d4c-9a3efe5934b3 | -5.11031 | -43.19532 | 2025-10-20 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa8aecd7-99bd-3320-be41-3c7392c8d797 | -6.21612 | -40.97377 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a0bdebd2-fcb9-3e87-b942-93acfc5ef930 | -7.04195 | -39.22206 | 2025-10-20 03:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c322ae5f-1b03-37c7-8798-a2563d1acf97 | -6.30334 | -40.8891 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b1b640a2-ed99-3935-8fc1-3097096b9896 | -4.39921 | -43.31498 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 582e8801-42af-329c-ae65-03d8192cc031 | -5.62769 | -43.64281 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1061cc06-9016-3bbc-95ca-e59b7e7edae5 | -7.5031 | -38.81982 | 2025-10-20 03:21:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23564892-9df8-31fd-9b4c-e0a0fb1d3e86 | -7.01652 | -35.23721 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b4cc6712-8eb0-3829-91a4-14749add53d8 | -4.17918 | -42.18942 | 2025-10-20 03:21:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9d600872-a899-32f9-a990-2a0c7d55478b | -3.59505 | -41.65829 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f164e8c4-e0f8-3db6-adb3-b7e91e512081 | -3.59753 | -41.65798 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b0791a5d-04ef-3b84-9077-45081dbb5f34 | -6.31203 | -40.90788 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d51e8dda-82f6-3c48-b56c-1fc991fbaf0e | -6.88912 | -43.5957 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d3e5291a-987a-3d08-b614-ce46b6b8daae | -6.8823 | -43.59465 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0af808c2-927f-3e5d-b3c0-e5b654d1c796 | -9.76157 | -41.92139 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| fd1af731-4ab8-31a8-9d7d-e72dec965a90 | -9.47213 | -41.03603 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6ea2a5e-7f3c-3e18-9a52-249f165c4a7e | -6.88353 | -43.59868 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0c0cee7d-9f81-306f-b1c5-fc6176c0e9f7 | -6.88236 | -43.60476 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a562681b-f66b-3051-ba37-756fb880b26c | -9.56419 | -40.33408 | 2025-10-20 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cfb308b-4616-320f-9360-912d9cc1a753 | -7.64926 | -43.06797 | 2025-10-20 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7077ddc3-8700-3d52-bc84-f30d9fa6ad74 | -7.99943 | -39.62519 | 2025-10-20 03:23:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ebda097f-39a9-303d-9ba7-929976bbb451 | -10.15965 | -42.21478 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3fe1b54d-0b5a-34e8-839b-6eac040a9f2f | -7.64999 | -43.0644 | 2025-10-20 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 99621fd1-e6dd-33db-bfe9-ef7ec88615fe | -7.12921 | -44.25138 | 2025-10-20 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 19f14844-9fbc-3ebc-9893-bf891bcf805b | -6.88471 | -43.5925 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c87e8844-c879-30ab-a83e-d026e0eddb68 | -7.41792 | -40.07076 | 2025-10-20 03:23:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d99064ab-7296-3d17-9dab-afda24f1a7bc | -9.76239 | -41.91705 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 859a856b-f51e-3ffa-97ca-ebcda566206a | -6.88591 | -43.58624 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6b86baae-20ed-3a57-a5ae-74be7349a7e1 | -8.15668 | -38.62979 | 2025-10-20 03:23:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 5e5cb145-03a3-3d5d-824f-4d9a48ac9dd4 | -11.86698 | -41.2737 | 2025-10-20 03:23:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 960f9ed8-654a-38e2-8ee1-25e74f71205a | -6.88346 | -43.58838 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 3e78b288-bd28-3191-88ae-cc8c273cf55d | -10.1546 | -42.20924 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a8436e5-0828-3b26-a2e9-3f416c7aa39b | -7.13765 | -44.24521 | 2025-10-20 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0abe9e91-55b2-3a6f-92ac-89b2f15c1f36 | -7.13884 | -44.239 | 2025-10-20 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7d6de3f3-f767-3482-bc5c-7f8fcb850b28 | -9.56887 | -40.33839 | 2025-10-20 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 31500a88-ef0b-3b26-ba13-3e8000b83cd8 | -8.16154 | -38.63057 | 2025-10-20 03:23:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 25.0 |
| f668f052-383f-3f3d-9228-3ded4b8593ca | -11.86578 | -41.26979 | 2025-10-20 03:23:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d91d95c5-ec3e-38f5-b4c1-e77ca4c5a150 | -11.86509 | -41.27345 | 2025-10-20 03:23:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 06cf0689-0d47-3c3d-b165-b37f99f68f0c | -7.13171 | -44.23836 | 2025-10-20 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d3b385b1-09ee-3325-84c0-55338c22d413 | -7.13051 | -44.24461 | 2025-10-20 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 74314ba1-7648-30fc-b7df-6e4d3159624c | -7.99422 | -39.62431 | 2025-10-20 03:23:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 955b30df-63dd-3a89-9c39-8a4d9be46bc3 | -11.8677 | -41.27005 | 2025-10-20 03:23:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02596acb-baca-369a-ad4a-d3500cec80e3 | -10.15619 | -42.21341 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a5612238-4f92-3538-8ab6-2d1c7c8fa663 | -9.76829 | -41.91786 | 2025-10-20 03:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02065b24-534e-3303-8075-d632b271daf4 | -6.88118 | -43.60073 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 93402cfb-9c0c-345f-a6b9-4c7fba0656a9 | -7.99829 | -39.63153 | 2025-10-20 03:23:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b93c6948-f2ce-31db-a208-eff47b02d193 | -7.99886 | -39.62836 | 2025-10-20 03:23:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 64440179-a818-3033-81eb-b10105ba3b3b | -6.87788 | -43.59156 | 2025-10-20 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 18089a4a-010e-30a5-a382-c0e1f44a7840 | -9.56949 | -40.33505 | 2025-10-20 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 82d873b1-aaba-32e8-b099-2278d145cfb1 | -9.57011 | -40.33173 | 2025-10-20 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 84c1081e-17b8-3aca-bbaf-64891c500a70 | -9.5721 | -40.3475 | 2025-10-20 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| cd636501-ab5c-3500-bc2f-a00db91b5ec9 | 1.7482 | -55.9216 | 2025-10-20 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d7cc6073-530c-37ff-8939-ff433273d5c6 | -2.2527 | -51.9108 | 2025-10-20 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 12858e2f-1cf3-31e5-9589-6262e873ec8d | -9.5725 | -40.3227 | 2025-10-20 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.0 |
| cf32f9ea-a464-319c-8877-0b96988eacfd | -2.2527 | -51.9313 | 2025-10-20 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f4094272-ede1-3d51-8d39-749b9c1b7c50 | -9.6401 | -64.7411 | 2025-10-20 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6b54eff2-3d64-36d5-b944-9c042831598e | -6.8962 | -43.5902 | 2025-10-20 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8d752db5-53c9-3c39-8b35-4b34b1cb2339 | -4.8386 | -43.0516 | 2025-10-20 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5ada9e6d-7d8a-302f-9836-ffdb20bb733a | -6.8774 | -43.5919 | 2025-10-20 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4f7311d2-0edd-3e19-bbfb-85ef8827fe91 | -4.8388 | -43.0282 | 2025-10-20 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 274.8 |
| eeec06b2-7974-3644-acbc-69cb4e46264b | -2.2527 | -51.9108 | 2025-10-20 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| f6eaf6ad-2fcf-3ada-a3e2-25c48f9032cd | -4.82 | -43.0294 | 2025-10-20 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b5bf8cc9-af01-3139-8cf6-f149dde0f4c1 | -4.8389 | -43.0047 | 2025-10-20 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d22a30c9-54d3-3595-b8c2-f07513667408 | -2.8644 | -50.7361 | 2025-10-20 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 79570ec1-4f8d-34f9-b584-2f61a46db334 | -4.8575 | -43.0269 | 2025-10-20 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 26fb7734-a073-338d-b488-2e05be517115 | -3.28019 | -40.88145 | 2025-10-20 03:49:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
