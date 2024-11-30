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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 037e5bd9-620f-347e-abc1-181b101041ad | -3.24218 | -53.63447 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204c6562-7de7-3ab2-a443-e32d96d941c5 | -3.53639 | -54.08245 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e643a8cd-022a-36c1-8b66-623499ca286c | -1.10215 | -53.60606 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eb5e674-9a38-3585-bb60-757a4d1db933 | -2.61807 | -53.98713 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f888ce1-e1a2-3fa8-812d-ba8679e6e027 | -1.74155 | -53.74791 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30c4b713-ef76-3171-94d8-8fb133ae7c1a | -1.4539 | -54.48416 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20cda54d-c9bd-3e0a-914a-9cc386fdcf3b | -3.24613 | -53.63137 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2a33a7-8f79-3263-997f-23d1c9eedc2d | -1.59857 | -52.29321 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4054d755-c0df-36f4-a8f0-27639908428a | -2.69272 | -48.65909 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7adbb55e-1c9d-3b0c-8382-9586684f09aa | -2.89716 | -53.95886 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3411cd-a625-37e8-9e3a-7a08b42ed10b | -3.09696 | -54.04339 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ae6ae70-d401-3574-8a12-e80cf0f98e8e | -3.179 | -50.27854 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e1c5abf-d841-3d7f-84cb-1f4d0cd69d79 | -2.78048 | -51.71935 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07cb3c54-4a96-3c96-9cd4-4ac9c8ec65ee | -2.80601 | -53.00866 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0db8f7a9-b6c5-341d-b94f-3389bf318974 | -2.6264 | -54.217 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cccce51a-b35c-3f3d-9ec8-27949809e669 | -2.22639 | -46.39225 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b7a332-3dec-3da2-8ee7-fde232f195a2 | -1.3946 | -52.05282 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc67c4d4-1a55-3707-b820-b407735b740a | -2.87545 | -53.98787 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c57b2674-52fd-3095-ad48-0f6022c032e7 | -3.75617 | -49.94095 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15cdc6a9-f11f-3357-9062-1d0d84275874 | -2.66935 | -49.86918 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3baa9146-d5f1-305d-b489-d9de7538f334 | -3.05681 | -54.03717 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 856ba21a-a1a5-3eb4-8821-55d2347d3949 | -1.34331 | -52.12857 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35946200-1fba-3c1c-a643-7cb6d83f61a5 | -1.43922 | -54.92284 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50048b3-5053-3907-867f-861e1316d066 | -1.15409 | -51.70272 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce0cf2c3-472c-3eb3-a6b8-ba232d6b85f7 | -2.82682 | -52.94337 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1af6a207-2d3e-3b4d-8207-a090c75c7117 | -2.60039 | -54.25216 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76ce34e7-42f0-3f3a-8ba7-b80f26404f8c | -3.05961 | -54.0412 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38715797-860a-3c5f-b588-2742a9750619 | -2.83614 | -54.1073 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb18cee5-f23d-37af-a2a3-37e593b8f5dc | -1.16762 | -51.93565 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e749135e-3607-3ebc-b5d1-b7087a3a2e51 | -1.48608 | -52.67394 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2afd99c9-7d9d-3a4f-944b-fc19f6618f13 | -2.61267 | -54.28251 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31b5330b-e484-3082-8f61-f073ae759498 | -3.49024 | -53.81443 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8580125e-ca56-3889-aeab-07440cdccac6 | -3.64785 | -50.21761 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9dcd8be-6072-3423-ad62-7b23744b73b1 | -1.62596 | -53.88381 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5365a9dc-7a80-3c85-a07f-5598eeb26ff1 | -2.84822 | -54.03033 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5edd6d9-f587-3718-a442-26debfe6eb19 | -3.21389 | -54.17662 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8ff671f5-261c-383d-8311-fe4a36d8fa13 | -1.05647 | -53.20846 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e85c33c6-9c45-36ba-abae-12a51ac0689e | -2.41354 | -56.43448 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb93ca2d-8955-3288-91f0-b89d4fb5ea0b | -4.08692 | -47.02414 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a8aa64d-ca4d-3cb9-93a5-edd6b2b81d3a | -1.32334 | -51.74689 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56829d15-048f-3cd0-a3ef-964d81d77e19 | -1.25215 | -52.18282 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731cab9a-1867-34e2-9f82-fdd771fc2b79 | -2.08161 | -52.48186 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a54248-9a60-35e9-b429-38d75b72b3a0 | -3.14431 | -53.84161 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a12d0257-a6ec-3a2a-a65d-26d180356533 | -3.74428 | -54.68293 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c2fee21-4a64-3221-aac3-a9217c455361 | -2.79643 | -54.03308 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c452b2af-6b44-3c57-9a32-8ba86df33465 | -3.09439 | -53.2409 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44210f12-bef3-3c8f-a891-ab87b5e14eef | -3.1123 | -53.10418 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f6c9be9-99f3-344b-8408-5fdb6f2aedf6 | -3.32454 | -50.21949 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| daec2f4a-e1ca-3a1e-88c6-5450e3b7f208 | -2.95241 | -49.44364 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5830fcad-650d-32fb-b331-9024fa557bfa | 1.44085 | -55.87881 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 455240f1-9d9e-3d6c-8d11-91f4c75e63d1 | -2.73391 | -54.02709 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83bea758-1634-3a8e-a36f-9674aac0b206 | -2.86753 | -46.82899 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74701923-bc08-3084-919d-09fc8b207b0e | -3.08236 | -54.56575 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6be0b9d-3a99-391c-9434-674789f458a3 | -3.11115 | -53.11155 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a6ada52-8836-3520-b656-bd1da615300b | -1.20228 | -51.75811 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c470cba-cedc-341c-932d-c21ce74998f8 | -2.27369 | -46.43933 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3396c186-50eb-30f5-8ae1-0af2a9bf32c8 | -2.90086 | -54.77035 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71337b3f-e50d-33d9-90cf-fa04bd387837 | -3.22811 | -53.63597 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbbd28bc-2102-36da-9c23-23ebe849c373 | -3.23884 | -53.92846 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64798661-5bd9-3107-af36-e9ed1f8f80a3 | -0.26281 | -51.49534 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bbaacc3-ed0d-3ab7-b61a-2090dc2db2f3 | -1.77479 | -52.95113 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 377c4d04-d590-3b9f-8f6d-3b7d668c1919 | -3.99386 | -41.50701 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5f2a8a3f-0ed1-3a36-9cc8-9ffe1b87403b | -1.43228 | -55.24435 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76337f4c-cf76-383b-800c-dcd2ed8161a9 | -3.95436 | -49.75923 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17f18796-e100-3d03-ba89-56e5eb13d1eb | -2.4087 | -53.85427 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcc5bdb1-f06d-3292-85ed-4fde37471c1b | -4.97825 | -47.23617 | 2024-11-30 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b3e790-8557-3ee3-94e8-08bc0bdb9433 | -1.19578 | -51.75299 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 836ad913-65a4-30d3-b971-00eb51d123e3 | -3.33309 | -54.15198 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79705ab0-a3c1-377f-b0e4-655722c4c510 | -2.31454 | -49.07596 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e45875ea-f25f-3572-b55e-4e21fcadd7f0 | -1.18852 | -51.77647 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c28e796a-5128-3738-a912-2621cf341bd4 | -0.9988 | -53.69767 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aaa7b78-eae4-310d-8ce9-f422591f39cf | -1.17165 | -53.41465 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| effa31d6-26f0-330d-86fc-9f4c4834aad6 | -3.30697 | -54.1658 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69c5fce4-6f3e-39f9-96fc-e0f613c754b5 | -3.1129 | -53.81101 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 90603a7a-eb5c-3444-85e9-0a73127b2d74 | -3.22248 | -53.06725 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c21f7975-9fdb-3396-bafa-e7476727c4f0 | -1.19127 | -53.87331 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b035e29c-4c4b-3158-888d-ab74404f30fc | -2.60245 | -53.97754 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 491d4554-b940-3834-81ab-f78b112fa425 | -2.72359 | -54.13644 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ff56a80-0b7d-31cc-8baa-a475b5ac5c07 | -3.70695 | -47.14762 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 823d009a-78e1-3c04-80c5-e3d8859ebd5f | -2.2036 | -54.51663 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53b3c48-ff63-3971-9be4-5787cd21ea80 | -2.82717 | -54.07727 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eff5918b-574f-3829-b288-7d44b6c0ada6 | -3.27496 | -53.42517 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c654104-0945-387c-9a91-987ad1dc0791 | -2.95552 | -51.69564 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc90265b-e42d-39d7-80dc-4caac9c36030 | -1.15736 | -53.54977 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1142ce23-d9b7-3533-9f8e-923097f2669a | -3.4203 | -50.42794 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b65c1b0-c0b3-3162-b599-ad19509848e3 | -2.20692 | -54.51715 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b1d2b46-6cb0-35fe-81ea-322002de453c | -3.09304 | -54.0248 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a2030b6-091f-3688-b7ed-1251e0a17a4e | -3.34682 | -50.51375 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d1e2e16-3c4c-3ebe-acba-e49303e01927 | -2.36946 | -48.63153 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a27f80a-2487-3b8e-8f54-b871f84074dc | -1.44802 | -54.37036 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a38889-f275-394f-a3e9-7e4a78079c99 | -3.26779 | -51.62592 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e69852e-d311-3cb7-9fc2-dd8649e8583d | -1.37948 | -53.64542 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3086029b-4100-3d40-adb2-af6602fd33ae | -1.59841 | -53.82586 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c4c10ac-0836-3d46-ad31-03f93cadaf15 | -1.35586 | -55.64066 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 617be38f-e562-3d07-9d23-b397abca6697 | -0.8804 | -51.71973 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81ee8f22-4459-3bba-8e20-cb2973161847 | -3.47367 | -54.16266 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b279aa2a-b1e2-3a18-a073-49a6040ae062 | -2.76733 | -54.03231 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c79c2e95-ad1e-3e1b-bca2-228b7ab8946c | -2.44036 | -46.5127 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89871de7-01ed-3e94-a8ca-2819bad49884 | -3.42192 | -53.89142 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280680ba-01a2-3ccd-9f7c-e70430d5e9da | -3.37081 | -50.82436 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README82.md)
