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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b91bdc2-c0b6-3902-ab50-3601175041b3 | -4.06062 | -53.77824 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72f5d07e-64e1-3e9a-b2d1-c2fa2f26492f | -4.05898 | -53.59491 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa3b2d05-adf1-3582-8a0a-f8ccd9f685de | -4.0584 | -53.77085 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 711bb012-00a6-3042-b1c1-22da6dc3eb79 | -4.05786 | -53.77429 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 000a9a22-8ef8-384f-bc34-c8b2a9b6a49b | -4.03562 | -53.24576 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 139fdf77-09eb-3980-8992-293a985c533f | -4.0133 | -53.77789 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d842d94e-33ca-3cd6-909e-d020f4fde3ee | -4.00892 | -53.78425 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0a7963-a748-3c91-a81c-b751cb617c42 | -3.93943 | -53.47054 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 515a33eb-cea7-3441-8654-4fac1dd97e58 | -3.91631 | -53.46694 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99efd513-f716-3568-987a-34b23590fea5 | -3.88801 | -53.53603 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25e37137-291b-35da-bfb6-a39e52fba496 | -3.77452 | -53.41615 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 233d317f-4ae9-302b-a622-2000c252e032 | -3.769 | -53.40825 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1ed9d0c-67d7-3c5c-8eb1-46ce2a465b03 | -3.76846 | -53.41168 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 500a2be1-3f2f-3f2b-b490-1167b2cdbca9 | -3.7673 | -53.39745 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c732f929-6299-3c17-a7c0-1a7a61a11edf | -3.76569 | -53.40773 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5a74a8-46fc-350c-b039-cb08c8d1fd07 | -3.76515 | -53.41117 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6283c060-32f4-3cec-8e8e-a4532ce9125e | -3.58992 | -53.46795 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc96d469-f08b-3d28-b444-26ce1fdab95c | -3.57145 | -53.5425 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 702ef109-6b16-3c7d-af35-50876a6ee91e | -3.56929 | -53.74976 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 615b9d5e-015e-3c38-8001-7c9122d7b64f | -3.56877 | -53.75311 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb04525b-67e3-3896-8097-fd9f43f32315 | -3.56876 | -53.53553 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 663cf8c8-f2d9-3fcf-8c85-6d52897ae1c6 | -3.56823 | -53.75655 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a2dc9db-cd8e-31a5-a841-d06663a0a603 | -3.56822 | -53.53897 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c5254bf-a435-3756-a8b8-d1fd60eb247a | -3.56768 | -53.5424 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfa83848-e2ac-3efd-be0a-7bbb1accef86 | -3.56654 | -53.52815 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf709f9d-a98f-309f-84ab-cf71502f6e1d | -3.56653 | -53.74581 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f16b5f83-86e2-3ed1-a09e-8ecad53bbec8 | -3.566 | -53.53159 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afd9db4d-0863-3170-9ecf-da88e4454bb2 | -3.56599 | -53.74924 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c472905-a435-3a73-8a44-f2118175045e | -3.56546 | -53.7526 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20305290-0eaa-374d-b57f-aac23ff799ab | -3.56492 | -53.75603 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 337702bb-bcc1-3bd6-9428-8f5ef6750e7a | -3.56492 | -53.53846 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4c7a03f-0bc1-33a2-bfcd-a5a9a8f9489f | -3.56323 | -53.74529 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecf442e1-3729-35b0-811c-b77da780ee3e | -3.5627 | -53.74865 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e333b5c-a433-3c2a-9db1-e72d2a0ef119 | -4.46885 | -52.71097 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 769da649-0e63-3b65-ace3-ae4f631dc9ee | -3.90166 | -52.3852 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e28137-ff0a-3af1-b7e0-4628ed444839 | -3.90111 | -52.38876 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a834e0-3d9b-3722-8582-60849044de67 | -3.88316 | -52.34956 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6bceea4-ec78-3250-8b41-055acb949ceb | -2.21447 | -53.69953 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51affaa4-f1a1-3a8c-a9f5-0349ca373411 | -2.21117 | -53.69902 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0fb631a-3f03-3223-9da4-372ac0daafd1 | -2.21062 | -53.70247 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f66be39-6360-3592-9cae-ca1d17970862 | -2.13848 | -53.64149 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 971638cb-1f58-3fa9-a6ff-0494552ba9f5 | -2.09148 | -53.57428 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192b0c3c-4d21-33cf-a6d8-c5c091d7419d | -2.08817 | -53.57377 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f385926e-04ca-3ffb-9815-e483a91efe0c | -2.07604 | -53.56483 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc32ba6f-e471-3b87-81bd-25dd974ed44b | -1.87387 | -53.61804 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c9d9cf8-e342-33c9-af97-a6043a5d8394 | -1.57966 | -53.5012 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f29a870d-933d-374e-90c4-b3e7424f1c23 | -1.57912 | -53.50463 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad06e44b-3e9d-3b43-b15f-2f1a813923e1 | -1.5769 | -53.49724 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f051815c-4a77-39f1-b8a8-9acba33ba4d1 | -1.57636 | -53.50068 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0183636-9ebb-387c-92fa-e7dd682759fc | -1.57582 | -53.50412 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2929934-54c3-344e-a2f9-eed747e904bc | -1.57527 | -53.50756 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 830c34cd-5ae5-3705-bec9-71fb2188745f | -1.30012 | -53.39754 | 2024-10-20 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0a79b1-b1e8-335f-badf-d22c4994bfa8 | -1.90607 | -54.59666 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5e5c2e5-41c3-3fdb-bdc0-89cb0fbd7ac7 | -1.90328 | -54.59256 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 606ce2f0-c987-3d56-ba1f-9a1e041d47d9 | -1.86393 | -54.70057 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3c61888b-a597-34a1-b086-08cc9e0cad63 | -1.51838 | -54.78041 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db8cf3d4-b1e1-3c43-b27b-6febcce18efa | -1.33875 | -54.65883 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7310842-835c-3ccf-8f02-a6ff852def4a | -1.33817 | -54.66246 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56679870-f61e-3d60-80fd-bd7b7f39d5d2 | -1.33537 | -54.65828 | 2024-10-20 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2baf8483-9d3f-3a81-b3a5-c7ebc91a96ba | -1.27264 | -54.54212 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1145707e-3007-3de0-ad8d-340a5e42decf | -1.27208 | -54.54571 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcdb0347-7424-3b74-ab90-7e6e71f49dd4 | -1.26984 | -54.53799 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cd6e082-2efe-3fd8-a8da-027acc4c88e4 | -1.26928 | -54.54158 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3bdccf5-2853-3c7f-890b-e6235f679a21 | -1.26704 | -54.53387 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22def9ac-5950-38d3-b300-7e8bcef33043 | -1.26648 | -54.53745 | 2024-10-20 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b97cd32-c5a9-3dc4-81c4-bdc1c5169fde | -2.28143 | -53.72765 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf65ed0d-38f0-3042-b9bd-8a0d663797c1 | -2.27867 | -53.72368 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73e83924-9671-37b7-8f25-36876b89a5d1 | -2.27813 | -53.72713 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb2c04c-5cdd-37a0-bd32-da7221bdc404 | -2.27536 | -53.72317 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21a1b3fa-4835-3523-90d2-d8c0c33b5a37 | -2.27482 | -53.72661 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6782488-461d-3b1a-8cab-6a61fef39caa | -2.27205 | -53.72265 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b562289-ae5e-323c-93c2-30738b94d573 | -2.27151 | -53.72609 | 2024-10-20 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5856530c-a38a-34b6-ac62-c0a4bd487bf3 | -3.43771 | -54.15339 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e010901-a479-38d1-99fd-f2f2d35fa88e | -3.43447 | -54.19547 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0e24ff-0f15-359c-9fca-c5d1ab0f9948 | -3.4344 | -54.15286 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b740401d-f11d-3290-97f5-ff939822038d | -3.43163 | -54.14887 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f48bbd7-08fa-33bf-8754-13ba952942fc | -3.425 | -54.14782 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3612e3d-9537-3e8f-af6f-e8c421268afd | -3.42446 | -54.15128 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5658291a-da6e-3f14-be77-1fac51e4ef5e | -3.42169 | -54.1473 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23302d08-fa91-37a8-aa83-9e33f53cde75 | -3.31332 | -54.12294 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b29d500-8756-3d6d-9bee-10299ba59996 | -3.27356 | -53.70724 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c20e16ee-cc1a-3e36-ac6b-cc536180e253 | -3.27303 | -53.71061 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8eff11f1-095c-3904-a283-4cc8033b733d | -3.27194 | -54.1484 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e63d401-aa35-3e9d-bba2-faf37d070c40 | -3.27139 | -54.15187 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ee55bff-0d85-3cf5-988f-95580beaa3a3 | -3.27087 | -54.17661 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8157c06c-9c5b-35e4-a45b-6f026c9a89d9 | -3.27026 | -53.70672 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d613add-23e8-348e-a258-310dd3b235cb | -3.26972 | -53.71016 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d13572ca-974c-3984-b4fa-0db558bce42e | -3.26863 | -54.14788 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 340f540f-db51-39df-a4e7-c47afda17931 | -3.26701 | -54.17955 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e48f91e0-2e08-39be-b549-fba84a375fe9 | -3.2505 | -54.17699 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 586c9966-8f0a-3744-ba0c-6b5bf7baa134 | -3.11857 | -53.74248 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d7db49c-26df-3927-b769-a4c51c80a661 | -3.11803 | -53.74591 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4a39f62-8347-3e62-a2a9-fbd5c47873c5 | -3.01987 | -54.04479 | 2024-10-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11b5db71-2d89-3e01-8f41-b70cb7221d82 | -2.97896 | -53.72081 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f9a5828-3809-3939-97e0-1012708a1853 | -2.95046 | -54.16172 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59ceec7e-279a-30da-a62e-dd3ed32268ec | -2.94769 | -54.15773 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4f86a42-d90e-32df-842f-50a364a11121 | -2.94754 | -53.70543 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a40034b-09f6-301b-ae7e-9616b57f594e | -2.94714 | -54.1612 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1c0420d-6e2b-37dc-857a-329f03a77f3d | -2.947 | -53.70886 | 2024-10-20 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0e04b3-900c-3804-9dad-3c85df7d60c8 | -2.94438 | -54.15721 | 2024-10-20 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README52.md)
