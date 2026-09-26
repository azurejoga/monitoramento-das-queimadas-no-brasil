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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e8c2a09-bd8b-3b25-aa7f-1217d4ef8a47 | -8.51796 | -40.23441 | 2026-09-26 04:25:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 679c80d1-49f0-3196-b056-5d5ffaa41935 | -3.98708 | -48.43266 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39d028e4-89d9-3841-b711-90911bc9c380 | -7.39957 | -39.78442 | 2026-09-26 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8b8e9306-2871-3403-8c00-2ce17c56dfc8 | -5.78019 | -45.07015 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d39395f6-f2ba-32df-8cf7-dc23e4fed4a0 | -5.77082 | -45.0864 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6225596-41b0-3178-bdff-5a4a4f708ec1 | -4.26937 | -44.59325 | 2026-09-26 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9e51a28-9ba1-384a-a51d-00a050a9fd15 | -6.12863 | -43.74072 | 2026-09-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94eb1600-2103-3209-a585-ce5d66b6acea | -4.83885 | -48.20343 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22c3125b-c09c-3a72-aba7-6bfcaffbf902 | -1.14871 | -54.09919 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f9c279a-4462-32a7-b4d1-fa046d05d468 | -5.7366 | -45.0668 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 42733400-8a4e-3078-bba7-e3a3cd70f508 | -5.77965 | -45.09489 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5440195-d120-3aae-b7c6-ab5c9840ec2f | -1.21237 | -54.57044 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d42eff0-4b98-3fbd-9d3a-7b0b5d9f9f2d | -8.51847 | -40.23083 | 2026-09-26 04:25:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba165d49-c79b-3305-adeb-935785b6bd75 | -6.02011 | -35.4389 | 2026-09-26 04:25:00 | NOAA-20 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6927c29e-0c4d-32df-9e60-ff9f3b7061b7 | -7.3626 | -42.09312 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f1a4906-9b47-3beb-8bcb-1c9ecb89231d | -3.94483 | -42.99212 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92c2074f-b87a-3b76-8be2-04ae1b2e67a1 | -3.26917 | -50.14526 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0574a723-ac23-3b7d-ae76-3c5b484446dd | -7.37222 | -42.07782 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1ac76be7-7fbe-35f6-ac03-1c0d318ee2e5 | -5.99867 | -44.91397 | 2026-09-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10289988-153e-39aa-881f-70b0e04e7cbf | -2.99749 | -50.47591 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75b81f24-465a-3901-85ea-b568c3b0effd | -5.91206 | -45.54382 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b98cfc5b-db7f-38eb-8ad2-7fd045d9120d | -5.52243 | -39.86781 | 2026-09-26 04:25:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3379bbde-c964-3bf4-843e-fc271b32d082 | -7.37283 | -42.07368 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 617c7e7f-d536-3649-8d88-0060c1e24536 | -2.99377 | -50.471 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2311616e-72f0-3ed7-a1e7-33d585178813 | -5.68281 | -45.86775 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e75d232f-5cda-3f1f-9dc3-953671f347d1 | -2.99306 | -50.47528 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 376bcc58-750f-39e1-ac60-f5140568371d | -5.77689 | -45.0909 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bab2f2ba-9d3e-3221-be0d-9e9624c32f71 | -2.98863 | -50.47466 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e62ca60-8f0e-3548-accd-547e9ffe750b | -5.72717 | -46.45859 | 2026-09-26 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac730630-9f65-3b0c-9ce1-998897b7ee62 | -6.74898 | -39.80383 | 2026-09-26 04:25:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 313ad89c-cc88-395a-b0c9-272c445a39f3 | -4.30731 | -49.12144 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09632741-1f00-3eac-8d2a-aec4e796368b | -1.29046 | -46.60438 | 2026-09-26 04:25:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33997f9e-dcc3-3410-aad0-1f4e3c3cba73 | -2.15471 | -53.71148 | 2026-09-26 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42ab3fad-5abc-3df6-bd13-a64e3f022fcc | -2.15026 | -51.97493 | 2026-09-26 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ef2f023-69a0-3546-b368-e5d504f4d567 | -2.56294 | -48.25611 | 2026-09-26 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30cb7fb8-bd10-3a78-8a88-345e323bf7b9 | -5.77304 | -45.11516 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d704f9-792f-3c00-9e5d-35d42c34bcfc | -2.89955 | -54.09861 | 2026-09-26 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5e68dfa6-1088-3029-a7dc-08b4c38b80ec | -5.77854 | -45.08052 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 931cb039-cceb-3af4-adab-b5d2585cc1ac | -5.68339 | -45.86421 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c00e494-8143-3dc9-99c8-15ac7b029a42 | -3.98405 | -48.42736 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2b9c960-6acf-3840-9598-6b6246b2c3d6 | -1.14358 | -54.09409 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c30954b-8fd1-362b-8c88-ee715854bc50 | -2.14851 | -53.71428 | 2026-09-26 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9d66f79c-a862-3adb-9cb4-534534bd8251 | -2.44625 | -49.22291 | 2026-09-26 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e253955-547d-32d0-ab5c-9386af89f537 | -4.89841 | -46.01065 | 2026-09-26 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70f3b198-9aa8-37de-bde7-039ef202e5c1 | -1.90602 | -52.08801 | 2026-09-26 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8332c0ba-a140-31ad-9213-ccbe626b9eaf | -3.41726 | -50.42199 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d232290-81fd-3eae-8913-b7deeed0ea28 | -3.41714 | -50.41926 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083dfe3a-416f-36af-b806-93011e9ab9f8 | -5.11664 | -45.67243 | 2026-09-26 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b30dcbbe-34fe-3df1-a017-96ead0249a7e | -1.21776 | -54.55957 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 456d9219-e279-352f-9a00-8fb0e1b4dbff | -5.5244 | -39.86621 | 2026-09-26 04:25:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ced53bf-46a5-327e-b534-b9383f9c1da3 | -5.74598 | -45.07184 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d22b0670-8b51-39ca-8a65-873ad5a3f462 | -6.8345 | -43.56792 | 2026-09-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d827aded-fc6c-3fe2-ab75-b6a1716ea83e | -2.9077 | -54.11968 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f2609d5-72bd-3643-9e29-0644e9cd629a | -2.14913 | -53.71057 | 2026-09-26 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 540c4bb4-8b19-3fbe-b596-f35fc4f78fc3 | -5.85786 | -46.25831 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e240b205-9f0b-380f-ae8c-fa009c216ea4 | -4.41018 | -47.79751 | 2026-09-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7560337-b5be-355d-bc5e-c66e24e105d1 | -3.77217 | -42.39751 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 823e7284-1607-346d-b590-02a9789c2920 | -3.98328 | -48.43201 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 93572cde-c015-3502-8757-a8293297a366 | -1.14225 | -54.10224 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced0c295-b1fa-3f26-8c24-5f600bc31400 | -1.83848 | -54.72721 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 526d0fab-d786-3141-b40b-c0991b010bc4 | -3.49908 | -53.45697 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5cfb784-cd64-3ab3-bfed-a943934315dd | -5.99922 | -44.91052 | 2026-09-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 819dc13e-3293-3ea5-a660-9077d4333640 | -1.83598 | -54.71991 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 15826c74-77ed-3f78-ad2f-01eb43f11114 | -5.78021 | -45.11274 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b88027f6-2903-3950-8772-644c0af748d6 | -3.8729 | -52.28095 | 2026-09-26 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0204642-9b91-396a-a99b-662343c4d82a | -5.77468 | -45.08346 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75365b0f-e6f2-3705-afca-b11f96fa0bde | -2.90833 | -54.11586 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| edbe291b-54dd-30e0-ab75-947c62cf7180 | -3.20603 | -53.41059 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 340543c7-14f3-35a4-9d6a-abecf692a232 | -5.77524 | -45.1013 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd52c3ae-de14-39d5-beeb-c54b5a1ceb04 | -5.7769 | -45.11221 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b52faa-ffcb-3e20-ab83-eb7dca2477dd | -4.28763 | -48.60984 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ec5cbeb-e28e-35c3-b5e4-5480f5062cfe | -3.23869 | -43.22613 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9d83c72-a8bc-3ee8-a153-79757c0e4485 | -1.1952 | -49.1277 | 2026-09-26 04:25:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d25aaec-5ba0-373c-80e1-17459b039459 | -3.49452 | -50.74179 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7de9ea97-c3a7-35d3-bfc0-66dc8d0ef9a2 | -4.45719 | -47.924 | 2026-09-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4ff5f318-32aa-3687-96bc-c435121f505d | -3.42454 | -50.42903 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb1cff40-dd98-3096-aba9-497e144bd423 | -5.77192 | -45.07948 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c75d6482-3943-3e12-b207-7cbd87830517 | -3.49847 | -53.46054 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09db6784-dcb2-3f7f-a80c-5fc396e9e75c | -2.96797 | -51.04894 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a09c1e0e-9850-33f5-8a78-dac75dc603ca | -1.8392 | -54.72279 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c21effa3-5b1a-3d9e-809c-dfed4b5d8848 | -5.4849 | -45.93813 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c887976f-7c2b-3b88-bb64-f51fbd35b47e | -3.20547 | -53.41393 | 2026-09-26 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ae0ce06-9d34-3291-85cd-f14208f7a243 | -5.77635 | -45.11568 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 097cc926-db01-320d-a1bd-1c58d6d85a9a | -3.00262 | -50.47231 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da6216a9-7a18-3616-9705-9f03e9a9e902 | -3.93457 | -40.59204 | 2026-09-26 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1045f93-eb3f-3eab-b31b-78c522b7a4f5 | -1.13847 | -54.08891 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70a4cfc5-1d3d-3f35-a059-51c316d3ffc6 | -5.68502 | -45.87539 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aee3d1d6-a342-306c-b5e3-d62d6f1b8baf | -3.42456 | -43.16546 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afd5b509-f915-34e4-a647-c598a0431002 | -6.71028 | -45.99165 | 2026-09-26 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d64e008a-a629-3803-9fd5-1264f5bbb3d8 | -1.14806 | -54.10324 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f827add-461c-3afd-bc03-785df3315893 | -5.78131 | -45.1058 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e78d0c4-b135-386e-9b41-066af9d29bb1 | -2.84014 | -51.36071 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d976da28-18dd-3f45-8d7e-ab0af0cdf5ce | -3.21623 | -48.81805 | 2026-09-26 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2428997e-5d6f-356e-80ea-6fbaf93c6d23 | -3.05618 | -46.92846 | 2026-09-26 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e236cd16-04e8-38de-985b-bc1bdcb9a16f | -1.21301 | -54.5666 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f678adf-abc7-3ec4-b037-f7089a76c3df | -5.52321 | -39.86246 | 2026-09-26 04:25:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c385280-9e84-33d5-9ecb-415685fa8fec | -4.30421 | -49.11572 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0c2df2-d7b0-3752-98f9-57b7d84ab815 | -4.11037 | -51.08009 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc7f7fd5-83f5-3571-9414-d437f1b57c94 | -4.27268 | -44.59377 | 2026-09-26 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c504a723-ea27-3022-881e-180ac1018317 | -2.15522 | -51.97577 | 2026-09-26 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README14.md)
