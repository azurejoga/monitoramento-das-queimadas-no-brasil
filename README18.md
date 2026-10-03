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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e70d1170-8d69-3f46-873d-c5e83de86789 | -12.97731 | -41.17488 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7db5d7e3-6537-32b7-80ba-0b8bb01917a9 | -12.97379 | -41.17425 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3846fd9-ad50-3286-b274-5a9c3718c07b | -11.46499 | -43.39726 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 109712b4-b295-3d98-b21f-249165321a24 | -5.88829 | -41.5176 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41804a36-723c-3702-8005-63d9a306f9ad | -12.95914 | -41.19669 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b02352c5-15b8-324d-bcf3-6fdd259205a3 | -5.73104 | -45.14951 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16e77c54-a0d0-3876-a214-ac5bf699ed58 | -9.72925 | -36.10373 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| e930b665-b09e-3f40-8bf7-967352bfcf4c | -5.941 | -43.65665 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6bd28fb0-9535-31fa-98ae-8a2d21ac9a24 | -5.74715 | -45.14647 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86ca2536-5148-3ab0-badf-728a5553945a | -11.83221 | -43.56544 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65638c3d-bdf7-3a1d-97c4-33a6f92c9e83 | -5.74126 | -45.06102 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d07f9a6-534a-3689-83d0-e8e21a00d036 | -5.82682 | -45.01237 | 2026-10-03 03:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a26d083f-05c2-3526-a991-2d985b4411b5 | -11.46841 | -43.4017 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97d80bcc-f4c1-3285-8095-e7f9a00e605d | -5.94553 | -43.65751 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7d7eff17-5b84-3a3a-927d-8935f02641e8 | -5.74012 | -45.15705 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 605bfd2d-ac74-33da-bcbc-09e4f2990349 | -5.74665 | -45.14934 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9f05900-5d9b-371f-90c8-cf692bebd27a | -11.48272 | -40.87365 | 2026-10-03 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fde19fff-9cf4-3716-bc1b-cce2335aa746 | -5.94844 | -43.64651 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 3cdd0679-5089-378d-9c44-88566aaf2719 | -7.89 | -44.18259 | 2026-10-03 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ec4f908-935d-3291-8084-796487e0f682 | -5.40455 | -45.19357 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 006fc58f-f5e7-3995-bbfb-8337a8085047 | -11.80479 | -43.53423 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f12442f-4542-3c03-91e9-b919a4c54cb3 | -5.61394 | -44.37914 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 53d003e9-e212-36e5-9709-a916dcaab53b | -5.17098 | -45.41994 | 2026-10-03 03:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e4eb25-a341-308e-bbe2-c9e18e6bc146 | -6.1568 | -43.68825 | 2026-10-03 03:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cea661d-9a1d-3d80-b9a7-e5827df33a56 | -4.40476 | -49.96997 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8f85082-4646-3c09-b493-db1cd0280b26 | -5.76054 | -42.34607 | 2026-10-03 03:55:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66d6c10f-f5e9-3438-914a-0608ffe6c7f0 | -5.74765 | -45.14357 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4179519b-30cc-36ce-a3ed-ef29d904e35f | -9.7253 | -36.10687 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| bf2e1a12-a464-312c-b8b4-fc4817a25e88 | -5.73154 | -45.14665 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2148cfe2-723c-30d4-9954-870662b1ed8a | -15.2401 | -43.27782 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 103.2 |
| f17a9e5e-f6bb-3545-8cad-ad27674f8cc8 | -16.54595 | -40.52464 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 19ba2ad2-a4f4-37d1-b93c-763f30067b1b | -16.55117 | -40.556 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f121997-d23a-36e2-aebb-1e5906d0d1a9 | -16.55419 | -40.53757 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8d2798d9-3104-3283-a404-f81db351b4c8 | -15.23629 | -43.2771 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 16e582fa-4f38-310a-acbf-dc6784a09e7b | -15.24097 | -43.27299 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 8cb4f38b-8acb-334b-af42-81e5a84ab82a | -15.23411 | -43.27457 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.7 |
| d32d315b-9226-32f7-8244-41f5e0c41a50 | -16.12137 | -42.22937 | 2026-10-03 03:57:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7103ffd8-90c9-3e2e-9aa1-49060225650f | -15.23495 | -43.26975 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a5af032d-e0fe-3e72-8722-56a8ec073e02 | -15.23542 | -43.28194 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b0f51b27-cc9c-3e1e-b017-00d60adafe92 | -14.94023 | -39.27338 | 2026-10-03 03:57:00 | NOAA-20 | BUERAREMA | BAHIA | Brasil | 2904704 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 713877e1-2d7e-3772-a4aa-55bb5120aeee | -16.52614 | -40.54024 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 66b5bfff-bdae-316e-a7f2-5e1f3ab203a2 | -15.23804 | -43.26749 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 393a3a36-7636-303c-be8e-1e11aebfde23 | -16.55145 | -40.53325 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3e78d62a-55b2-355f-82c7-cb0c494ecd95 | -13.49561 | -44.37326 | 2026-10-03 03:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2abb1811-0afe-3d5f-89d1-f030616009e6 | -16.54963 | -40.54435 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 978102e1-11f6-3f27-a050-694ae004e026 | -15.24172 | -43.27602 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 78.8 |
| e2d00f49-5f32-3f86-9e47-811b2909dfb3 | -16.54656 | -40.52094 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 18311e72-2a77-326c-9f17-86f5a3af308d | -13.52203 | -44.39501 | 2026-10-03 03:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69571f74-7591-3200-ae9c-4f2976f27b5d | -15.15513 | -42.51749 | 2026-10-03 03:57:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e74066c5-e323-389b-a464-388dd1efba92 | -16.55479 | -40.53386 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b202da97-1254-3c9c-b404-dbaf519137fe | -16.52554 | -40.54394 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 40fd07aa-ba4d-371f-a844-6ff37010fbbe | -16.12205 | -42.22546 | 2026-10-03 03:57:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 832e1dd5-3196-3659-a246-5d8775fe170b | -15.23707 | -43.28014 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 90bbcd5c-d6f2-3544-a888-dd8ab9fed290 | -14.78303 | -39.84726 | 2026-10-03 03:57:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a3de817-7182-3e96-a4d8-9a6e48ff32d7 | -15.24257 | -43.27118 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 25519344-4f84-33b8-8fe7-0205f6a35a16 | -17.24833 | -39.43368 | 2026-10-03 03:57:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b4448a4b-dc94-3009-bcff-781a6fc5252f | -16.55298 | -40.54496 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9926412-0b39-3319-be47-c9af39fecb4a | -15.7086 | -39.24786 | 2026-10-03 03:57:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f72d572-81a4-3bb3-8cbf-435dd5f14490 | -16.5426 | -40.52408 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 94a8a40c-a266-36d6-9984-06f48c7a91fb | -15.23876 | -43.27047 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c6be6c8f-fa38-3d88-b173-016854cfba11 | -15.24983 | -40.10973 | 2026-10-03 03:57:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ce0b0cf-26ff-3053-b082-a7dff0062d9a | -16.1347 | -42.25875 | 2026-10-03 03:57:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a6639d93-c83c-3e0f-bed9-cbc5fbd16989 | -15.23792 | -43.27529 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 78.8 |
| daff66a2-5f6e-3240-9563-b7a1416f9170 | -15.23327 | -43.27941 | 2026-10-03 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 35fc8b3c-462f-3953-a66f-f32ca335812b | -13.52135 | -44.39887 | 2026-10-03 03:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 677875de-c114-379c-8ac5-46a7a7209155 | -13.52186 | -44.39782 | 2026-10-03 03:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2715c387-a555-3350-a5bd-ed7e2c8fc812 | -16.54386 | -40.55847 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fe642afb-b25c-3c1a-be40-8c741254891f | -16.53924 | -40.52352 | 2026-10-03 03:57:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c7a685d-6092-3ff8-84f5-66aa7ab1a5fe | -3.1116 | -53.7234 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 955c1be1-5799-3e4b-9594-53074de8d6b8 | -3.1299 | -53.7431 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f1642754-a28e-3c63-8f95-8bffcff85b41 | -12.8676 | -44.6878 | 2026-10-03 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a9b18bc2-4bdc-3261-8148-1a23e56e73c9 | -3.1483 | -53.7426 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 437190de-6790-3f13-aa3e-08c650c2949b | -5.7376 | -45.1533 | 2026-10-03 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6fc50d20-3a79-34c7-bcc5-2780a0833a03 | -5.9381 | -43.6714 | 2026-10-03 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b37d9c96-14d3-30c3-9e0a-96813ec2bdde | -12.8483 | -44.6909 | 2026-10-03 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 5b7b2eab-0670-3666-927c-23fad7a5354c | -5.9384 | -43.6482 | 2026-10-03 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d8376f90-5318-3ce1-b9c3-050ddfd262ae | -3.1299 | -53.7633 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4e6ca95f-ec5e-3be1-93d0-89c94828a82f | -5.9571 | -43.6467 | 2026-10-03 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 5537a4b1-1bde-33e3-8ec8-be3f1f94b6cd | -5.9569 | -43.67 | 2026-10-03 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c215cd64-615a-364d-a1ec-7a98a7347e5d | -9.4574 | -40.3641 | 2026-10-03 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 4364eb81-1660-348a-bbe6-abed4c6f688c | -3.13 | -53.7229 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 954627ad-3f93-3581-a4f4-5b0a6ccbc11e | -3.1116 | -53.7436 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cda202ef-615a-38b7-afba-ef1712b0e8f7 | -3.2951 | -53.8395 | 2026-10-03 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2f28d095-1148-30b6-8498-5a016d2c7d82 | -3.1483 | -53.7426 | 2026-10-03 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| a961a48e-2440-36a8-a151-f1e2461f28e7 | -5.7376 | -45.1533 | 2026-10-03 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 929e7678-3c58-3f54-9207-ea0b919df841 | -3.13 | -53.7229 | 2026-10-03 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e742b48f-b4c6-33b8-901b-7e52167d8de4 | -12.8483 | -44.6909 | 2026-10-03 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a398a356-71e1-3fbb-a0c5-62bafa5646b7 | -12.8676 | -44.6878 | 2026-10-03 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7b3c05fc-36dd-379a-9c30-9cd53f76895e | -5.9571 | -43.6467 | 2026-10-03 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 83a925c8-5ec4-38a4-8be2-34dd3f814071 | -3.1299 | -53.7633 | 2026-10-03 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| cc6260c9-16db-334d-ae9f-04d7bb594ad4 | -5.9384 | -43.6482 | 2026-10-03 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| d7711b8e-c382-34a8-8e21-8ef6a0ab138b | -5.9569 | -43.67 | 2026-10-03 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9caf4e1b-b560-3a89-97c5-9bde3bba0832 | -5.9381 | -43.6714 | 2026-10-03 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 332d451a-eab6-3196-880a-0dbf918c831f | -9.4765 | -40.3613 | 2026-10-03 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.8 |
| b44b394f-7373-31cc-8120-47fa30ffbaee | -9.4574 | -40.3641 | 2026-10-03 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 175.5 |
| 85787c43-a9f1-3090-934e-ebdd2215a421 | -3.1116 | -53.7436 | 2026-10-03 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0a13fa22-f2d9-3358-830c-7519fe4292be | -12.8672 | -44.7112 | 2026-10-03 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9262f103-3a8e-3d92-acf0-c47d60f650ea | -3.1299 | -53.7431 | 2026-10-03 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 59ed4797-7665-33e1-8670-50fe16f55f29 | -9.457 | -40.3889 | 2026-10-03 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.5 |
| fef71b02-c936-3df7-bdd3-36535216ebaa | -12.8478 | -44.7143 | 2026-10-03 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |


[Clique aqui para ver as próximas entradas](README19.md)
