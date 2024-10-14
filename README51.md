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
| c9c9af78-19da-3e88-8c28-ed15ea352bbd | -3.6184 | -54.13178 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e474d29-86e7-33f1-877d-9d75d54b0a15 | -3.61573 | -54.13049 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6807fffc-afe6-3b3b-a110-26239ac45be2 | -3.51787 | -54.66454 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b583e1d-f170-3023-9404-a27c0a67afe7 | -3.51708 | -54.66288 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dec2dbe9-2cea-3a91-8929-5cdfea3de820 | -3.51634 | -54.66711 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c2536e2-b160-3552-976f-c5a2264b74c7 | -3.51198 | -54.66366 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1140382-31d0-30ef-9169-d75c7e1d51e8 | -3.51118 | -54.66206 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51d9f95d-effb-3c76-97eb-9508b88ce7df | -3.51044 | -54.66631 | 2024-10-14 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35e2df77-9f12-3f7a-829f-7ee42b38dd24 | -3.48318 | -54.15828 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4fb815-f6a5-3826-98ca-728cfcddf3fc | -3.42722 | -54.17789 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d34cda-0413-3357-ac80-f7f0e0a0f50d | -3.30131 | -53.85487 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06cffb2b-a542-3296-981b-b2ddb70ab90b | -3.29698 | -53.84649 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2d8c23b-924f-3eb3-819e-42017ceff0e9 | -3.29635 | -53.85025 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a51a28f-1b82-3401-bfb1-9990a54c8c65 | -3.29572 | -53.854 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0620a987-c983-3afc-aba5-8171373b5a32 | -3.25957 | -54.20935 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81d0b404-5279-39f2-a809-88af358e9d64 | -3.2545 | -54.20448 | 2024-10-14 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9d7ef56-afaa-3af3-a5ad-fbe28bef94d4 | -3.08215 | -54.23902 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2107a9ce-4036-301f-9b24-72ae880218c7 | -3.08147 | -54.243 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a520d3e6-329e-34a1-851b-341c2a533768 | -3.08079 | -54.24701 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f08a544c-6bcd-3957-a250-d467282f6243 | -3.0764 | -54.23807 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec30427-741b-3ca2-b556-7fbec9e2fa55 | -3.0757 | -54.24213 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad4a2e56-f3e5-3772-9038-39c881fac714 | -3.07561 | -54.23656 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d9b61dc-03e4-307b-ae46-84bfac167e50 | -3.07501 | -54.24622 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29402c78-0d85-3304-b581-2613459369c6 | -3.07495 | -54.24061 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2207a4ab-93d0-377e-9047-1f9d4d4c3659 | -3.07428 | -54.24473 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ee2dda-d87f-3314-8cf2-97840838627e | -3.07361 | -54.24882 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a9a6aa-00a8-33ad-889e-0f41d5a8279b | -2.99297 | -54.90509 | 2024-10-14 04:19:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d14f642d-1332-389a-a399-d8399d99d64b | -2.99222 | -54.90952 | 2024-10-14 04:19:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad1b97f6-834f-37f5-a920-8f73daf1f1c9 | -2.96501 | -54.65239 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4545a935-4c5d-30a4-9687-198904440868 | -2.9643 | -54.65666 | 2024-10-14 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aac312c-38d6-31fe-b808-202cacb059d7 | -2.80925 | -54.0844 | 2024-10-14 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f72616d-ff8c-30c6-9419-b1c738110bfb | -2.6523 | -54.30736 | 2024-10-14 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5d321e1a-52bf-3674-a70f-6091cdc75994 | -2.6516 | -54.3115 | 2024-10-14 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34e2a292-5a3b-3bd6-bc99-7b65b4b14aae | -2.57156 | -54.00942 | 2024-10-14 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b91b5f3b-35c2-323f-947d-f9c3646ce81e | -2.57089 | -54.0134 | 2024-10-14 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3d73133c-2900-3533-8c3b-5751b48866da | -2.56952 | -54.00993 | 2024-10-14 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1f15a2cd-a296-33e6-80a3-8f310a5fcf20 | -2.332 | -54.58718 | 2024-10-14 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb73fa61-c29e-3be3-ab70-82b1d04f1cfa | -2.33126 | -54.59163 | 2024-10-14 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9ce3e4d9-90e2-3211-9c7d-dbbd86bda66d | -4.49926 | -54.9617 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e01cbb-ede3-3eeb-94e5-481a79915d2b | -4.46189 | -55.07144 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e98feab-bbd5-3f2c-9c86-3885e6e02c04 | -4.407 | -54.97978 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 712230fa-7912-374b-a8b3-05f5f399ec0b | -4.35623 | -55.13213 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a701db54-a420-3790-8d8d-b2aa3a4db4d5 | -4.3555 | -55.13632 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 0e0a5ebb-b66b-30fc-b434-440e35aa25f2 | -4.34427 | -55.13022 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 199ee685-9f8d-31df-8866-3b86dcd55811 | -4.27021 | -54.97277 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93a4855a-bc28-3445-b99b-0018802c5467 | -4.26339 | -55.08263 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c58bb516-f85e-3e44-823e-038a3c5a58cf | -4.26267 | -55.08674 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27605ab3-0566-3810-ac50-d2df56b6f5f7 | -4.26152 | -54.95277 | 2024-10-14 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c87d3011-db3e-31d9-a6f4-cfffe8c19d9f | -4.34754 | -47.57478 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0b42ce7-192e-3a33-8d3d-e3df8f950efd | -5.7493 | -43.06427 | 2024-10-14 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1199646-d807-39ac-9707-3f25c06a21b4 | -5.73279 | -43.0694 | 2024-10-14 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e67d264b-7b4f-3c21-b4e6-0c47a5a79b23 | -5.73277 | -43.04738 | 2024-10-14 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48950990-b16e-3e84-a16b-c5c5401d6198 | -5.67826 | -42.99837 | 2024-10-14 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05d1b93b-08fc-3f9e-a0b5-157df3ef9589 | -5.53197 | -42.939 | 2024-10-14 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38263543-3fdc-3871-b455-f71d47f080f8 | -5.53141 | -42.94259 | 2024-10-14 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 77199349-ace8-35f7-a713-339f711af113 | -5.52804 | -42.94207 | 2024-10-14 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d5430ab5-2915-39cb-88df-5610857c2da9 | -5.5213 | -42.94102 | 2024-10-14 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3602a2c0-1e09-3d3b-bc37-6836fbed6ce3 | -5.4805 | -42.77901 | 2024-10-14 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27018b6f-6a66-34bd-89c8-62a26b1c9bc2 | -5.47939 | -42.78629 | 2024-10-14 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9506eb79-7a08-3418-81fb-05d2db4845f5 | -3.83408 | -55.98352 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f6ef09e-b7cb-396c-9c63-5a93f894d941 | -3.83316 | -55.98872 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2612f3c6-d143-379f-bdfb-e97e81df99ed | -3.83201 | -55.98101 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 93b3bd1a-d6e7-3efd-aa10-759274180f4d | -3.83112 | -55.9862 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b2c7fec8-68c1-326e-a005-02b45207ed15 | -3.83023 | -55.99142 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ca4f9730-274f-3713-8aae-1243e2de49a8 | -3.82772 | -55.98255 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e51b942-5867-30d4-ba1e-5344500a1008 | -3.8268 | -55.98774 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 93c28a64-bbba-33c1-baeb-fe16e1ad5251 | -3.82588 | -55.99291 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 854db255-a5cf-3bed-805a-58d57210cd4b | -1.65135 | -55.09089 | 2024-10-14 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52dfbd81-27b1-33dd-b613-26a87ca419a3 | -1.65058 | -55.09571 | 2024-10-14 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4782fd8-3468-3131-abfc-45e99325e255 | -1.65001 | -55.09063 | 2024-10-14 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 740a17c9-3889-3b52-b712-8cf204835dba | -1.64921 | -55.09539 | 2024-10-14 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23b9e2db-796e-314b-a043-17ffc22a2912 | -1.34634 | -56.03354 | 2024-10-14 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc5a307f-e422-3832-8b91-46279ad5596c | -1.34541 | -56.03931 | 2024-10-14 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53be344e-7aff-3000-8ec1-fdac8cb6aac6 | -1.34455 | -56.03434 | 2024-10-14 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a440108-6eac-353e-8e73-1ccf105fe908 | -1.34355 | -56.04018 | 2024-10-14 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cae9a94-4a78-3c80-a30e-58997bad7686 | -3.99347 | -55.73601 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae577fba-21cd-3690-b83f-68a0c99910e1 | -3.99219 | -55.73274 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6335d5d-476c-3df1-8ae4-ba5dab2f3d64 | -3.99139 | -55.73725 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43375be7-8c77-3abf-9603-294a13e95b3d | -3.98725 | -55.73488 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93cba23a-1c84-3182-9d66-d5277074d468 | -3.98644 | -55.73965 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ec05d9a-d804-3933-b756-b71f9eaf789d | -3.98596 | -55.73172 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58cdc3d5-d1fe-3087-9bd6-49450c1f89eb | -3.98515 | -55.73627 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c92b3093-ee96-3a6b-9e51-5324910d75db | -3.98014 | -55.73896 | 2024-10-14 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 364201bf-a98a-33b4-a151-9ae18c65e3d3 | -3.93119 | -56.02616 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e42ac6d9-6c3c-368e-a1c8-4398d00a6159 | -3.9303 | -56.03138 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed5ef477-236c-37a2-a26b-cf1a4a8c78da | -3.92702 | -56.02699 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 243492ba-113d-377b-bc53-df5a25bbec48 | -3.92608 | -56.03226 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2b2ca1a9-d6b3-3512-9e6f-d0ada33c8548 | -3.92394 | -56.03036 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f660191d-f003-3847-b0e1-6d391cb44030 | -3.92303 | -56.03569 | 2024-10-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2932cfde-87d1-3594-824f-91b21bd6e280 | -9.35588 | -44.48565 | 2024-10-14 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfaf335f-ca18-35b5-ad77-498c2d68b1c1 | -9.26736 | -45.22987 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b2b37c2-3ee9-3ea9-b025-004b245924f0 | -9.26462 | -45.22592 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e610a34-f3a5-3f9d-9672-3985ff39c453 | -9.26406 | -45.22935 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57138549-0f23-364c-8794-976411102d9a | -9.17707 | -45.58904 | 2024-10-14 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e3ae93c-32a7-36ca-93b2-9704f23789a4 | -9.17432 | -45.58504 | 2024-10-14 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 713bc61c-5176-3639-9da8-44e67c6f72b9 | -9.17378 | -45.58851 | 2024-10-14 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc15d3c1-5ddd-3750-bb43-cc6a484ad7bf | -8.53339 | -44.08558 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07dce8e8-b9c5-33c4-9934-384b3745ccaf | -8.53253 | -44.15791 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f06d27-ebc8-3941-aea3-8837329f5e19 | -8.52866 | -44.16092 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 466ae96b-5f01-3966-b5ed-0a398365b38a | -8.52587 | -44.15685 | 2024-10-14 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README52.md)
