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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 920a3e9a-697a-397a-b078-f01506782eb4 | -3.22464 | -53.39487 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6708799-d8b8-33fc-a576-ed37bb2da5d9 | -3.224 | -53.39901 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05a0bd4e-be0e-3def-952c-a989b91a3ff9 | -3.22335 | -53.40314 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4555adf2-a744-3a05-954d-1491acce61fc | -3.22041 | -53.39845 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19929a1a-cc0a-38c6-9549-606d46542b82 | -3.21912 | -53.40665 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b894f574-429e-3c84-984e-9533de736e82 | -3.21848 | -53.41071 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bbfe8b4-6b9a-3829-beb9-6a9a5c740f03 | -3.21784 | -53.41481 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f143b8f9-dc30-361b-85ab-1aa8dae06d95 | -3.21426 | -53.41415 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e2927b-e225-38b1-9af9-56cd40df3291 | -3.21196 | -53.40537 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb72eef5-f864-38a6-b826-265f47093fb6 | -3.21132 | -53.40945 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65fe8a0a-252a-39a4-93b1-58e5ce180676 | -3.21068 | -53.41354 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3db57420-b57f-39bc-a60c-58aa93a91433 | -3.21003 | -53.41766 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4938f8f-16df-35db-943c-707a24a568aa | -3.20837 | -53.40481 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa93d82-15de-343d-a744-1bb70c50112d | -3.20773 | -53.40889 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c0c12d5-585a-3c52-8681-742ba197726d | -3.20709 | -53.41297 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1196bca6-71c2-3fd2-80c5-0cd52ebaacc1 | -3.20644 | -53.41706 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f111744-0127-3ecd-a891-4abd501c93b7 | -3.20478 | -53.40425 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a4d998f-5b27-3c69-85f9-5460a2ec97ac | -3.20414 | -53.40833 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f87d945-513b-349d-953c-b9f9f1d77e8d | -3.2035 | -53.41241 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 459cf03f-fee8-3e0d-84ce-5222925f6d4c | -3.20285 | -53.41649 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94f9a472-3a20-3abf-8764-28376e6d4341 | -3.20221 | -53.42058 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2db3193-195e-3756-bfb6-2b1c5c460910 | -3.20119 | -53.4037 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cafb8fc-e0ca-30f8-bb00-f5b1e118fb1b | -3.19991 | -53.41185 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 802d5614-6762-324e-8e4f-a818256b3768 | -3.19926 | -53.41593 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e190281-f8d0-3fc3-9376-eeb81f4acbd9 | -3.19862 | -53.42001 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e427372-bcd0-38e9-8f6b-ec4aec26925b | -3.16576 | -53.00737 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 684e43b8-142d-389f-806a-4428add4f60f | -3.12224 | -53.12249 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45146007-d9b8-3a92-bf57-aca8f3f54a73 | -3.05543 | -53.24414 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffce61b9-4653-3e6a-a852-92f092b6e4dc | -3.04462 | -53.27254 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da26032a-15e5-3f6c-a58d-02697a5b7614 | -3.04437 | -53.26735 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 214d73ef-f7ad-37ee-9a8d-064933ff1bf1 | -3.04372 | -53.27137 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 323687ab-321a-3275-bc63-0d37f335997d | -3.04231 | -53.26394 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e823fd16-b320-3a37-9158-94101f9870cd | -3.04168 | -53.26796 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 754724dc-e2b1-34ec-be32-7c3038b09bd2 | -3.04145 | -53.26277 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95846d29-3215-3927-be99-3d2399b77921 | -3.04105 | -53.27198 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4594957e-6339-36b4-858d-e80cfa5d9156 | -3.0408 | -53.26679 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7dbfa6a-cd31-3bf3-bba0-a93e7423b7d9 | -3.04015 | -53.27081 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 887e7218-143f-3a75-ae54-a301ff500cb0 | -3.03874 | -53.26337 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcae8beb-ad5d-3bef-84a6-c825f6632366 | -3.03811 | -53.26739 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0f21cc6-929b-334c-a474-d44cbf8525bc | -3.03748 | -53.27142 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1853aca3-727f-3154-abf8-87d63f28ff29 | -3.00689 | -53.44358 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18a44a1e-3ea0-3d71-872e-72c950b995f3 | -3.00329 | -53.443 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a92f2a39-7443-3f12-9318-c382bd052fa9 | -3.00263 | -53.44719 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b973f66a-5d7a-3b43-a147-a613595d7b58 | -2.9905 | -52.9043 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e4d2925-d2ba-3e29-8db6-678068b5adae | -2.98962 | -52.90427 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a14ab54f-8ca0-36b2-b812-5d61736cce84 | -2.98923 | -52.91214 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfba93f0-c1ff-3291-83eb-4d41587440fb | -2.9886 | -52.91608 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58bd4519-5071-3bf1-b7dc-035717826f03 | -2.98839 | -52.91213 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e79a4a-a9b6-3007-a33c-1c3daa0a8d60 | -2.98778 | -52.91608 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74423a5f-5177-3fac-8a52-ff0013e3544d | -2.98517 | -53.20912 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f6c112e-68b2-3654-b1e5-c556c986409b | -2.97898 | -53.27087 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa937c68-0406-3ab3-85eb-4b08f86f451f | -2.97541 | -53.27028 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73e276e8-74a3-3a1e-a61b-d681ca0ac55b | -2.97184 | -53.2697 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ed369e1-169d-326f-a111-9fbe3a89c3ff | -2.97119 | -53.27382 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a0b6e8e-ca01-3797-859e-ae81756406a8 | -2.95906 | -52.91548 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d43bbad-9c85-3afb-a266-cb4d6e54c581 | -2.95785 | -53.28845 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3509e985-8d36-38cc-a9b7-49b296cdcf3b | -2.95427 | -53.28792 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caad8404-2f27-3d2f-adcc-ed6603d6e4f4 | -2.95003 | -53.29144 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f546b6c0-a4f5-3556-8eaf-d04676dd8b2f | -2.94645 | -53.2909 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11041b72-1650-3b94-b1f4-28da582dda4d | -2.94615 | -52.56882 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd942b56-5461-310d-8f1a-61332435304a | -2.25491 | -52.2128 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a246718a-89a6-3c79-921b-049e9aefb567 | -2.87926 | -52.89183 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d82437e9-efff-3ef2-a9f4-9107fea6701a | -2.87575 | -52.89129 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0469aa0-a30a-36fc-92a3-528a2c21f116 | -2.86613 | -52.43282 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98bfc8c3-f2c7-33d5-8677-dda753eada43 | -2.86526 | -53.32463 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e081a432-79a7-3e49-b250-c28dff1f2037 | -2.86268 | -52.43228 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb6e33f1-b982-34a1-b112-11eaff67fb01 | -2.86234 | -53.31991 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbcabac5-95da-32f7-8f3f-e4e9acc97990 | -2.85774 | -53.34875 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2e157fd-73b3-3d82-ae8e-b307bd04a103 | -2.85416 | -53.34817 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b4fa0c1-ab1b-3551-8235-3a88fa8144a1 | -2.85123 | -53.34342 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c2bc0d-f435-34b7-9530-cf2de501788f | -2.85056 | -53.3476 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00dd7cb1-a12f-3541-9e19-7abaec6d73c0 | -2.84045 | -53.34177 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c76df893-0f62-3277-a316-3622363c8536 | -2.83979 | -53.34591 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52676a55-921d-3c42-b5da-13f22d67f53d | -2.83892 | -52.87362 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff99e40a-3d62-3302-ab2f-d72070008def | -2.83831 | -52.87751 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 723ba325-a17f-3561-a6d7-ecbd7fb08cbd | -2.83752 | -53.33708 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c11606f-45fc-35ad-80e3-f8416de858af | -2.83686 | -53.3412 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef655425-7615-3891-8613-440a14b2f2ce | -2.83541 | -52.87307 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc286286-8971-3d83-8747-711191457b06 | -2.83479 | -52.87698 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d00daea-e01f-38f0-b5d0-15a8cdf999c5 | -2.83189 | -52.87255 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc4a6f28-8bdb-39cd-a781-09ea2b21e000 | -2.80491 | -52.46652 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d5d9fe6-3eba-31d3-ab0d-007f593b7d81 | -2.80431 | -52.4703 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfcb5dc4-4f1b-3a7e-9947-464a731db87c | -2.80146 | -52.46594 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 750b9acf-655d-35e1-a08f-d76f26cbbfd5 | -2.80086 | -52.46972 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07bfd94e-c0a9-33e1-87fa-a4fdf3f8f604 | -2.80027 | -52.47349 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fcf458d-2ee1-3bc6-abcf-7b89859e1fd6 | -2.79801 | -52.46536 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 420fe270-dba4-301e-94d5-da4ce8951fab | -2.79741 | -52.46914 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9376d77c-9d2a-32da-87b2-ce971697db95 | -2.75245 | -53.21206 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00fac8fc-5f3b-3910-b73f-21e7cb4c6459 | -2.75179 | -53.21618 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c89eb06f-bb63-370c-ac29-0eafdfb63907 | -2.75113 | -53.22031 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26db923d-ed3f-346d-87de-58e5549242e9 | -2.74887 | -53.21153 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d072bf30-625a-3e41-a974-f70c18796903 | -2.74821 | -53.21566 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f806d37-7534-32b0-a8d5-0e41f57d44c3 | -2.74755 | -53.21978 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf57d5e9-99f4-3dfe-adbf-7d0f453c269d | -2.7453 | -53.211 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6d37bd-6b4d-318e-ad98-9b798cab17dc | -2.74463 | -53.21514 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f87d0b3c-6c86-3f89-9641-fad46ddec887 | -2.74397 | -53.21925 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f18fa4a-f739-3c5e-81c4-d05c29b3bdc2 | -2.74105 | -53.21463 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56f239d-f1c7-3775-86df-52ef2af629e5 | -2.73747 | -53.2141 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a03887e9-3569-3ff5-a60e-45e1309f177d | -2.6737 | -53.02334 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9053bbf-384b-366c-81fa-caf1b9e108d3 | -2.5912 | -53.37748 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README56.md)
