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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cf96c14-d741-3f4f-8b2b-92310670640a | -0.87722 | -52.00226 | 2024-11-02 04:10:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6ae237d-71a3-314b-8f04-2edc7ff9e4ae | -0.87661 | -52.00616 | 2024-11-02 04:10:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6d10e38-3c58-3eaa-980d-99a302685b6a | -0.87413 | -51.99766 | 2024-11-02 04:10:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba8eece0-c63e-3adb-8b25-fa6da7a6113b | -0.8735 | -52.00152 | 2024-11-02 04:10:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12b96ce5-7637-3e0d-8a87-0c45a62a6a38 | -1.57727 | -54.76207 | 2024-11-02 04:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea4e063-03e6-388e-acec-708ed90afb31 | -1.57446 | -54.76102 | 2024-11-02 04:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c349a9c-c8ed-36b9-b706-a33ea93bc571 | -1.57055 | -54.76107 | 2024-11-02 04:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e254d349-34b3-341e-853f-cff0cc21e030 | -1.52521 | -54.28469 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1df1a78e-6f57-3793-a236-b8328ffdbfb7 | -1.52426 | -54.29049 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08658f1c-f689-3551-9d80-9bf6591baf34 | -1.51867 | -54.28373 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb64de04-f67b-3310-a449-ed4373a5053a | -1.51774 | -54.28942 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18f0b269-e2b9-3a6a-ae35-27bbd8e2f7c5 | -1.38462 | -54.12778 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab24e1c-c2d2-369c-b210-28f8ced6c1c6 | -1.38384 | -54.13018 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3685fe16-dc9e-3b24-bb26-af5da2a63691 | -1.38378 | -54.13278 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f63eb7e0-c4fd-343d-88a5-166ba0e95afe | -1.20809 | -53.65179 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2519a99f-644c-3b43-8058-ef949adc8644 | -1.20732 | -53.65656 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0876845-6c67-3e4d-8b19-e3092bf814c6 | -1.20657 | -53.66117 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d8beedf-1c40-39bf-8661-f0ebd2193ddc | -1.20064 | -53.91158 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2e8b2bc-1153-32d7-9a64-7be9e18806bd | -1.19983 | -53.91641 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 959241c9-5356-36a5-b2d8-5cb26fe8d03c | -1.19875 | -53.9135 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1f0a1636-d449-37c5-ae64-3a44fbde9cfd | -1.19798 | -53.91831 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 72d4ce6a-0584-37bc-afcd-e5f2cc11b019 | -1.19347 | -53.91512 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d99655ee-a966-3ec8-b583-764c6b840d6d | -1.18849 | -53.69289 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07c9b9b9-d7ec-345f-83b0-fcd33b9c89d0 | -1.18761 | -53.6983 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4161aba8-cd5e-3009-a0eb-3aabaad17e08 | -1.18295 | -53.68703 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f34bf398-4448-3286-a1f1-481ac2d68389 | -1.18222 | -53.69154 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f2e32cc2-9cab-3adf-8b71-9cee18971946 | -1.18145 | -53.69628 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd9f38a6-7a86-35b2-aeaa-789442a4fe27 | -1.17732 | -53.6818 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3a83431-5c50-3063-9c15-94c96bcb184e | -1.17659 | -53.6863 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fa23798-be7a-3ed1-ac83-28035d190df8 | -1.17094 | -53.68117 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4459adee-ddc4-30a8-aed1-9ede6084a3e6 | -1.17021 | -53.68562 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eb976de-984b-3408-8522-a3ef2bc91db8 | -1.16945 | -54.18147 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55300bd5-0ada-3737-8da4-da9616a5b440 | -1.16871 | -54.184 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 560c3e0b-0847-395a-8d29-6ee28560083a | -1.16406 | -53.68359 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7376d72b-a36e-30bf-a139-0c7f468ac280 | -1.16334 | -53.68795 | 2024-11-02 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e8d7e9-87c1-3513-9973-1ed45106af9d | -1.16311 | -54.17742 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42a78eb0-6d2c-3cc5-8e82-c94042b99640 | -1.16292 | -54.18053 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4f7cd36b-86d0-3c04-b3f1-8a830485a185 | -1.16219 | -54.18301 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 244e4ac7-49bb-33d6-94cf-012c00955e18 | -1.15901 | -54.08199 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a6f516f-0bfe-3f2e-8fa7-844cfad90f6d | -1.15824 | -54.08453 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b6bc051-c63d-3959-8110-f15d19d1e1e4 | -1.15811 | -54.08734 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb88edf-e0b2-3c3d-9be0-98b19127aeec | -1.15738 | -54.08989 | 2024-11-02 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b7a1257-3cc7-3aa0-8847-957491dde274 | -1.27227 | -53.37186 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d47a6463-d0dc-3380-a809-ecb60b58a213 | -1.27155 | -53.37011 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f4fa66-76a6-3195-86fe-93c6ce405f50 | -1.27148 | -53.37678 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4089afc6-82d0-32b8-a055-aeb98ee84ddb | -1.27074 | -53.37497 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d471e85-b82f-370b-8abb-4a7a31c2278b | -1.26604 | -53.37112 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69cec7e0-ad8d-32de-bfdc-39384ba6921c | -1.21349 | -53.38163 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c5efd56-8db8-30c0-8837-a373aba41cbe | -1.21274 | -53.38626 | 2024-11-02 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24c9d85b-6a20-314a-9c9a-3d921e63754f | 3.52312 | -51.2819 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef5a241f-25c4-3681-bc19-6abab6d3e01a | 3.51855 | -51.29099 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19f8d16e-0b00-311a-87c0-8558b6db4ad7 | 3.51834 | -51.28948 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c68ef36b-1ffa-3384-92bb-e03fbc030faa | 3.4193 | -51.26231 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37daa0d5-8d60-3d32-811f-26a87d422616 | 3.41914 | -51.26003 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84870972-2bc0-345d-adfc-6423b420cc5f | 3.41869 | -51.25823 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8220fa8e-a1ef-3904-bf74-f56554f0d02c | 3.41855 | -51.25595 | 2024-11-02 04:10:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882e6c60-94df-383a-9bc5-8526475b9b11 | -4.23367 | -48.03439 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 733614ad-a895-31a2-bb51-cc00906a316f | -4.57453 | -43.10241 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533e7b24-a2b3-3770-b989-d2350fdd6eaa | -4.57123 | -43.10189 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33d01e30-0e7f-3d23-bc85-85f6c71861c9 | -4.57068 | -43.10534 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34382095-312a-3efe-9b5c-84a2bc74b0ab | -4.56792 | -43.10138 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d5794a2-9ad2-3210-af8f-488da952c971 | -4.56737 | -43.10482 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e16c1d5d-8bac-37a8-8626-849138a3e339 | -4.56386 | -43.10425 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe6c621-25f6-3742-8158-301d2128c921 | -4.56332 | -43.1077 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbbf8ea4-e2f8-33bc-a67c-26acc6393c11 | -4.56218 | -43.09338 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc59cdb3-b4ad-366a-8147-d774a7d723c3 | -4.65864 | -43.81807 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f93dd20-6a95-3b5e-8f63-b15b2989a79f | -4.65809 | -43.82159 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a49e5b8b-ea71-39cc-a5b5-381008289980 | -4.65531 | -43.81754 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04129009-792e-36ce-a305-63e61cf76779 | -4.60667 | -43.99496 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce6a5810-3a80-3c36-9b6a-b2c4e9c8fea8 | -4.60331 | -43.99443 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0925f80-570e-3130-8d51-3912d611a6f0 | -4.60275 | -43.99799 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93f111ea-0d18-3797-adb3-f1db37bb04f1 | -4.59996 | -43.99391 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f56e044-fc85-3650-8cba-23f7efd7def6 | -4.56055 | -43.10373 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a0b2259-09d1-3672-b819-5d487ac3f1d2 | -4.55833 | -43.09631 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d53906f6-cd78-3d79-941f-f77060a16031 | -4.55779 | -43.09976 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22a93b7a-243c-3afd-8043-8566a9c7d958 | -4.55725 | -43.10321 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2429739c-518b-3bec-90cf-25c875418790 | -4.5567 | -43.10666 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca06c3a3-863a-3ec9-ab40-7e5d0872b9c8 | -4.55616 | -43.11011 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1406286-ca17-322d-91ec-1dd0abda5140 | -3.8046 | -42.55421 | 2024-11-02 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23306692-4394-3fe9-88bf-54ee1818ede8 | -3.54539 | -43.57095 | 2024-11-02 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 58271d32-af1b-39ca-928f-5e388174de85 | -4.08283 | -43.9564 | 2024-11-02 04:12:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10081508-5f11-37f4-9cee-27dd9dfea6c9 | -3.77982 | -43.55038 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9f7bf1c8-1110-3c1f-aa59-fcfd13d98f6e | -3.77705 | -43.54633 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a8ae6685-a8d5-3b8a-9d18-49a64bd08a78 | -3.77649 | -43.54984 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3b56a33b-5364-3cbe-aeec-264bf77ca929 | -3.77593 | -43.55335 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba0020b7-0df2-3240-9f8f-0943ceb7b1a8 | -3.77538 | -43.55686 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 960dd3a2-9721-32cc-8e9c-19790b49515d | -3.77372 | -43.54579 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c798becd-913e-341a-866c-d554373ae91d | -3.77316 | -43.5493 | 2024-11-02 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 33d12a7c-81c6-3213-8edb-25928a672345 | -5.6676 | -43.38826 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70a16794-e725-3e43-a435-d534eb18f9f8 | -5.58028 | -43.33908 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 349b6a73-dee6-3367-89ad-e98bb0e7271b | -3.53143 | -43.6157 | 2024-11-02 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac59e3ff-535d-3687-8343-4d61aabe52ea | -3.53086 | -43.61923 | 2024-11-02 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3717b9e6-2355-322e-8b54-b206590e12d6 | -3.52752 | -43.61871 | 2024-11-02 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40206514-b29a-36d1-b512-4cd22a2018d5 | -6.1254 | -43.97456 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1bb72b97-3ad3-304e-8986-5aceaa390100 | -5.43659 | -43.25946 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b9b1d3e-ab7f-376e-8701-43fec403053b | -5.31279 | -43.07352 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 492beebe-906a-3a23-b7fa-a393759b2106 | -5.41629 | -43.32354 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bf3b2d0-6d42-344e-8348-f96a4f00aaa1 | -5.56218 | -43.88171 | 2024-11-02 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c02d5e68-bd50-3964-bc25-505253346c1c | -5.25275 | -43.34695 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a52375b-a256-3067-a499-ff2ca7288515 | -5.14568 | -43.82981 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README36.md)
