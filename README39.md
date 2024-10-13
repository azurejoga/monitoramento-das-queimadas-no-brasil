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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a64cb8f-756c-3c98-ab07-efd8f6e16e80 | -7.20924 | -42.28895 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0b39a2d0-8914-37a6-8ed9-d61d2e9fad73 | -7.20636 | -42.28093 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bb61d1e6-3bf6-3117-ab34-9b6f68893a5f | -7.20574 | -42.28459 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1e1b2107-eeac-3e42-8d0c-9e79080371f0 | -7.20513 | -42.28827 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 080ae3ba-1e55-3681-aa57-44b9eb6d7c9a | -7.16594 | -42.59812 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 429993c4-df28-3bdb-8a39-467bd37ed465 | -7.16529 | -42.60197 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c17cdb96-c899-35ef-a863-603f1cc77ef8 | -7.16174 | -42.59742 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05b2094b-9d72-351a-a612-ea6fd612a724 | -7.15753 | -42.59676 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f18244db-89af-39b8-8eb5-36cd9b428518 | -7.15688 | -42.60061 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6891e2dc-0b1c-3c9f-9eac-eed8a06cdbd8 | -7.13925 | -42.65384 | 2024-10-13 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 036667de-9d34-331e-ab31-7c68bef63895 | -7.0796 | -42.64746 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72d2bd37-4b7d-348d-b9fb-8633ddfa3023 | -7.07933 | -42.64953 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ef8dcb5-6e6a-370e-8a6d-90ffcd2d583d | -7.07605 | -42.64287 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8632896-55af-320c-9a1d-df77dfde5d65 | -7.07511 | -42.64884 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c33b70a8-9bf7-3dd2-8fac-1bb33ae36e78 | -7.07469 | -42.65071 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 50d093e7-3de0-33ca-bcdf-9c2fddb29f51 | -7.73872 | -43.30307 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf1a5421-3bd9-3218-a3c0-b49a0e52251e | -7.73511 | -43.29805 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8074c643-6b2a-37b7-8822-b4c568a2c8d6 | -7.73436 | -43.30235 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b29fad1b-e0cd-3c07-badd-2af137bfa911 | -7.73413 | -43.29895 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 758ea858-e36c-3177-aca9-bc46adef8c54 | -7.7334 | -43.30326 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac517812-b47c-326d-a331-3ae5f9d281ae | -7.73075 | -43.29731 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce61c57a-2af3-355f-b2c8-5b02f7c14e14 | -7.72976 | -43.29821 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80ea3d7a-9998-363a-a258-623ad358dbc9 | -7.72639 | -43.2966 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f07b42c-eac2-3b18-8cbc-aca7195a3ea6 | -7.72563 | -43.3009 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aafbcb48-ff28-39e5-add9-0c460f6015f8 | -7.7254 | -43.29749 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 623affe6-b0c2-3cea-bd1e-878464b86543 | -7.72468 | -43.3018 | 2024-10-13 03:47:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a9147f5-48e1-3911-ad89-33d0d167a272 | -7.71924 | -43.17516 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b058bfa-4d3e-35e0-91f2-92ce16f6b24c | -7.71561 | -43.17035 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee27b586-6f1b-3ad0-9ad6-efa356482570 | -7.71002 | -43.20317 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2e9664df-e0be-3598-b4a8-7b23598ff707 | -7.70569 | -43.20244 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 82f38ad2-619e-319d-8238-189508d79b0c | -7.70497 | -43.20666 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5dafc795-1566-32fd-bf0d-ece75327e0d6 | -7.70487 | -43.18111 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1da5806e-c34c-32a0-8a53-361a1a05c816 | -7.70417 | -43.18521 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49aef320-fb2f-3913-869d-b58fc725d8c1 | -7.70277 | -43.19342 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dbc77140-a625-3d8e-a8aa-132a00e38474 | -7.70206 | -43.19757 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e5f6421e-3116-38a3-b88a-48ece0f7d864 | -7.70135 | -43.20174 | 2024-10-13 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 674051d8-574d-35d9-8f62-c4081c329627 | -7.60326 | -43.03786 | 2024-10-13 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d96d7e11-2975-3936-91aa-0e2f29e30764 | -10.06167 | -44.18 | 2024-10-13 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec050ed7-e5df-3ad7-a7c9-e9ef36e7798c | -10.93102 | -43.09237 | 2024-10-13 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f2a2e26-7e45-3782-8074-67f9125652b3 | -10.29781 | -43.42544 | 2024-10-13 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35142e6f-4492-3e3c-9751-03c1e2bd8208 | -10.88755 | -44.35078 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ff0ec4f-af1c-3d0e-85b0-81c69480dae9 | -11.10948 | -43.33639 | 2024-10-13 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 3170f45e-51bd-3760-9858-f7151da9345c | -11.10882 | -43.34015 | 2024-10-13 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 39c37574-56ea-3e2b-8e41-9aa733f62a66 | -11.10814 | -43.34392 | 2024-10-13 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c7522c16-89d1-3091-becf-6fb44ed8ac26 | -11.10469 | -43.33939 | 2024-10-13 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b7bbdcb-29ec-385b-9530-12de30f1f233 | -12.29 | -43.83587 | 2024-10-13 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae3795d3-1cdd-3daf-9863-34bd931515fe | -12.28585 | -43.83494 | 2024-10-13 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f3e1934-5697-3330-8736-3bf5415406a3 | -12.12057 | -44.74161 | 2024-10-13 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b78ba13-7c09-3ce2-ac24-c2fad76b5037 | -11.90744 | -43.32038 | 2024-10-13 03:47:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a09a8506-64da-34c9-940c-dea0d5004a45 | -11.74099 | -44.48616 | 2024-10-13 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5e5cd92-8a86-3f56-a35f-92655a11eff5 | -11.73658 | -44.48535 | 2024-10-13 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c45d7745-7059-3e42-951b-fb04ea57c451 | -11.7358 | -44.48975 | 2024-10-13 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d035cf4c-492f-3757-901f-74de044982f6 | -11.45951 | -43.93395 | 2024-10-13 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c9a945c-51ca-3e2d-a744-ecb0fed1269b | -11.45019 | -43.81459 | 2024-10-13 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d19d27ba-9e73-3278-9b90-96d6837f849a | -11.44597 | -43.81372 | 2024-10-13 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c40021-e7d2-3428-99bb-966b34202b20 | -11.25376 | -44.19992 | 2024-10-13 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5520c98-1a56-31c2-a7ca-07ca7a71728c | -11.25299 | -44.20093 | 2024-10-13 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d52268e9-5c02-3e14-88f4-df03e4f2ebfe | -11.24803 | -44.17787 | 2024-10-13 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8904de88-09c2-3795-b6e6-9bf0edc865b5 | -11.24728 | -44.18214 | 2024-10-13 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761ea8b2-9768-3657-b056-8719758a7d6e | -10.86376 | -43.64213 | 2024-10-13 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53001840-9f62-3167-8c95-c9357f412dc8 | -10.85953 | -43.64135 | 2024-10-13 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c00521fd-dcb7-3dfb-9677-6335dde5e14d | -12.29419 | -44.35167 | 2024-10-13 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ebcc5ae-7365-3adb-a249-fad792f3294c | -12.29343 | -44.35593 | 2024-10-13 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3318090-7d5a-3c92-8367-c2c247f226d9 | -13.69469 | -43.88273 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df320bbc-7965-367d-8f78-5b6fa0df53a9 | -13.6906 | -43.88191 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7180507a-a1f2-3655-842f-a605c80ba365 | -13.65573 | -44.22742 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54092a8b-4ed5-34fb-9fef-fea413aeac75 | -13.65154 | -44.22664 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc0d153-1f7a-3a83-a256-048d7796586b | -13.65099 | -44.22709 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65613ce1-c1e8-37c8-a56f-36b22f0e4a09 | -13.65081 | -44.23059 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2aa0071-15ba-37f4-8732-3f198d5d8067 | -13.65029 | -44.23106 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da40958-ddd6-3b46-98c7-4192455cc981 | -13.46531 | -43.66484 | 2024-10-13 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b14db111-700d-38a5-b6d7-67c7c6a5b1f7 | -13.46125 | -43.66408 | 2024-10-13 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaf9d7e2-ca16-364b-89cd-bf4d4a019d47 | -13.4572 | -43.66331 | 2024-10-13 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 283bd64a-dc52-3a46-be83-36f3034ec05f | -13.89445 | -44.27834 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e14bc5a-7547-3115-b6c4-3e30fe5a8cf7 | -13.86103 | -44.41353 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6157868c-ee83-31fd-b725-05707eec3127 | -13.85753 | -44.40874 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ed88a59-cf99-36d5-b334-fbb6d5a44e51 | -13.85679 | -44.41278 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 233a77ce-78da-3f0b-9b12-77a34184db4e | -13.78489 | -44.23433 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a25d621-688e-33cd-893f-2f9140abecb6 | -13.78202 | -44.3455 | 2024-10-13 03:47:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05d27b5e-69b0-352a-811e-2489e274de63 | -3.40774 | -43.3423 | 2024-10-13 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d927ba7a-1fbc-3f22-920a-a304dacd9390 | -3.40691 | -43.34726 | 2024-10-13 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4f3f529-44d5-3afd-acea-103524948d20 | -4.09199 | -43.91963 | 2024-10-13 03:47:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4843170e-fd2a-30f5-bf14-1f93b09d9a5e | -4.09112 | -43.92485 | 2024-10-13 03:47:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc978a28-840d-3404-98b4-06acdf286af1 | -4.82201 | -44.07674 | 2024-10-13 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 29cb623b-ede7-3141-a302-3f8eb716e792 | -4.78991 | -44.62752 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18dc6e6-9a8d-3808-bf71-b13f5df4bb1c | -4.39948 | -44.47561 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5e06dbea-3793-3c89-8812-5a0e6bf38ccc | -4.39899 | -44.47849 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 76123daf-72a5-357e-be79-123d356b2bd7 | -4.39849 | -44.48138 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 456bc1db-6033-348b-8fa2-0ecc94e49ad1 | -4.39799 | -44.48429 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| acacaf2c-5642-354b-915b-fd8104f906be | -4.39422 | -44.47681 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40c88435-82a5-3327-8a22-10e76b0dfc9b | -4.39398 | -44.47768 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0e1ee441-0516-3747-a1ae-c27a3ad4efaa | -4.39374 | -44.47971 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e032d11b-ed4e-39c7-9635-44a2a21bb3a0 | -4.39349 | -44.48058 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 53700194-27d5-3a9f-8c24-f1cfc4bb5973 | -4.39327 | -44.48264 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ff2eec76-f349-3eb0-b271-52167da560e2 | -4.39299 | -44.48347 | 2024-10-13 03:47:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 027163cb-f73c-3e8a-9ae4-63a737f746b4 | -6.4495 | -44.27485 | 2024-10-13 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb63b142-f20d-3fbe-b57d-264f0294ac27 | -6.36769 | -44.09175 | 2024-10-13 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4e549a3-c6d2-3e63-a388-e211b6e3f91f | -6.13983 | -44.73466 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34ab9368-64b5-3488-9041-9600321432b7 | -6.13584 | -44.72829 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a066ea0-102c-3381-91e1-54111511c373 | -6.13158 | -44.63541 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
