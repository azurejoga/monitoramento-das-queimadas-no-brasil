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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a031260-ec45-3f5a-bcb0-2f8f4f3149ef | -12.3519 | -49.9617 | 2025-05-22 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 39e8fba2-b370-3e0a-99ed-a54b80be3973 | -11.5719 | -47.4521 | 2025-05-22 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2fc88c19-ad2b-3eb8-b138-b7fb436cf6b7 | -12.2753 | -52.5016 | 2025-05-22 12:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 77704a79-4215-3d8f-8403-d29579a53b07 | -12.3324 | -49.9857 | 2025-05-22 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 34d24c18-9839-3d49-af3d-f16b1554dbf7 | -11.5719 | -47.4521 | 2025-05-22 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f844c95c-9ccc-3ec3-b1aa-209287089dbf | -12.2946 | -52.4785 | 2025-05-22 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 8b96849c-7c3a-3388-91d0-833d1ea94783 | -12.2943 | -52.4995 | 2025-05-22 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 354.6 |
| 8aef02c5-9ffd-37dc-9524-03af5c906ab8 | -12.3134 | -52.4974 | 2025-05-22 12:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| b210c96c-ec62-3f67-8e6d-3c356be202fa | -12.3515 | -49.9833 | 2025-05-22 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 7a0e9e3f-53bf-319d-abde-8d991d76bbdd | -12.3134 | -52.4974 | 2025-05-22 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 510e76b4-244e-3db6-b3f9-7f2e51ffdd12 | -12.3519 | -49.9617 | 2025-05-22 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a7e8d973-c6e3-3b1f-ad95-0f1e698850a0 | -12.2946 | -52.4785 | 2025-05-22 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 73269643-fcf3-3505-811c-82e506a03841 | -12.3324 | -49.9857 | 2025-05-22 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 60d8baf3-94b2-321c-b047-edc989906de9 | -12.3512 | -50.005 | 2025-05-22 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 26b83cb5-64ac-3893-b9dc-df4870ed6a56 | -11.5719 | -47.4521 | 2025-05-22 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| eb8b3a2e-e761-3f13-8347-3e294e3eb936 | -11.5528 | -47.4546 | 2025-05-22 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| fcc0a921-ad32-3da9-9bb7-4355aee5c199 | -12.2943 | -52.4995 | 2025-05-22 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 321.5 |
| 6389e559-7b10-3212-983c-b28f6edb9d49 | -12.2753 | -52.5016 | 2025-05-22 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| a905a022-4e99-3087-a88d-d7261b4315f6 | -12.3515 | -49.9833 | 2025-05-22 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 365.9 |
| 01f6662c-4d71-310b-a130-81b5404fc6f2 | -12.3134 | -52.4974 | 2025-05-22 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 5af55ddb-8735-3646-b96e-2712c6e01577 | -11.5528 | -47.4546 | 2025-05-22 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 78a8b4f2-fd1c-3fd0-9435-439e6c7c4dc1 | -12.294 | -52.5205 | 2025-05-22 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a13b83df-60d3-36e1-89d5-3c4e53783333 | -12.2943 | -52.4995 | 2025-05-22 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 357.2 |
| caf3d351-d2cb-3ff6-9778-7c697936b1e2 | -12.2753 | -52.5016 | 2025-05-22 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 34dde12a-ef02-3d0d-8d8a-c396ceebe0d6 | -11.5719 | -47.4521 | 2025-05-22 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f39e4ed8-3495-38d8-a25b-3d71d1f8d88f | -12.2946 | -52.4785 | 2025-05-22 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 3e42e44f-7711-340f-8c89-5f454ad82601 | -11.5719 | -47.4521 | 2025-05-22 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7637f3a2-46c3-3588-8df6-0c7e1944366e | -12.2946 | -52.4785 | 2025-05-22 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 3bea757f-ff57-37b5-bb2a-f92ae1e33c6f | -12.3134 | -52.4974 | 2025-05-22 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 6e264f46-0d51-3b59-9eeb-af4f9a2b8762 | -12.3324 | -49.9857 | 2025-05-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 231.1 |
| afcd320e-b9fd-3fd5-bb6c-e107407e9d2e | -12.3519 | -49.9617 | 2025-05-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| cf63e1d9-2512-37a5-b054-2170f9065db9 | -12.3512 | -50.005 | 2025-05-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| af50600f-9cd7-37a6-96ee-7f47765507a5 | -12.3515 | -49.9833 | 2025-05-22 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 424.2 |
| a2e78bc3-5ef4-34e7-898f-4e1d66d93c06 | -11.5528 | -47.4546 | 2025-05-22 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| bce98aeb-a983-3d7e-80a7-5df98cc50e52 | -12.2943 | -52.4995 | 2025-05-22 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 444.8 |
| 90d4c841-af3e-37aa-ac57-c5937c70a0d6 | -12.2753 | -52.5016 | 2025-05-22 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| acbf6d98-1781-3d03-8078-b71100b7d9b4 | -12.3515 | -49.9833 | 2025-05-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 424.1 |
| 62254ee2-d5d7-3dd6-9321-9e37a7d245a7 | -12.294 | -52.5205 | 2025-05-22 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 87328c7c-30e6-35ac-870b-7eba706c9287 | -11.5528 | -47.4546 | 2025-05-22 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 47ef3e13-cf97-3ee3-8f2e-a05d6cb00ac3 | -12.2946 | -52.4785 | 2025-05-22 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 220.7 |
| b133e0de-be28-3659-8017-b12ae1be6e94 | -11.5719 | -47.4521 | 2025-05-22 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bc27154d-ab5f-327d-96bc-17ec6611dbd4 | -12.3519 | -49.9617 | 2025-05-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 331da31f-08be-3665-ae72-2236213e153e | -12.3512 | -50.005 | 2025-05-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1bd5c5ef-cd24-3a6c-b200-6afdb50fdd90 | -12.3134 | -52.4974 | 2025-05-22 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e60a30ae-8913-3d1f-bd9d-c569acf73336 | -12.2753 | -52.5016 | 2025-05-22 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 05c8a983-ac16-3ad1-b743-20a242ccf56c | -12.2943 | -52.4995 | 2025-05-22 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 554.2 |
| 603bab42-8028-305f-a09a-3ed2d5645ec7 | -12.3324 | -49.9857 | 2025-05-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 203.2 |
| f2e7f6b9-d775-3d3a-a7d1-cd936b7a5335 | -12.3515 | -49.9833 | 2025-05-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 369.4 |
| c658bd60-b823-3274-ad72-ec1841b2e460 | -11.5719 | -47.4521 | 2025-05-22 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 86d4850b-8771-3f55-a316-fd280a13b62d | -12.2943 | -52.4995 | 2025-05-22 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 599.5 |
| a59544f4-25a2-346a-ad77-4d226f66a5c1 | -12.3512 | -50.005 | 2025-05-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8d78853d-f025-3a53-9965-c0fce99ef940 | -12.3519 | -49.9617 | 2025-05-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 94175c65-8706-31ed-a40b-853ca4a0d899 | -12.2946 | -52.4785 | 2025-05-22 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 3dcc5332-3ae7-35ab-9987-86dcda6f8dc7 | -12.294 | -52.5205 | 2025-05-22 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 170bfb77-e83c-3532-844e-973124f30dab | -12.2753 | -52.5016 | 2025-05-22 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 6a6b7c09-cdff-32de-a612-be4bf53a18da | -12.3134 | -52.4974 | 2025-05-22 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 97da0b4f-b33d-3c6d-8a88-72f71bf4302d | -12.3324 | -49.9857 | 2025-05-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 7c9433d1-eaf9-37f6-9463-b73daf27bda4 | -12.3324 | -49.9857 | 2025-05-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 227.2 |
| b130ff60-8d21-30c4-bb64-73b9a6315169 | -12.3134 | -52.4974 | 2025-05-22 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 2dec7157-d19c-3a9c-94be-ccae531f3c53 | -12.2753 | -52.5016 | 2025-05-22 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 597c30ac-7c32-396b-b74d-40475dbdd8b6 | -12.3519 | -49.9617 | 2025-05-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| a4b03a0d-50d5-3067-be14-7326b17b078c | -12.2946 | -52.4785 | 2025-05-22 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 251.7 |
| 80b1efda-e320-32cb-b138-b73b7302fe1e | -12.2943 | -52.4995 | 2025-05-22 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 615.6 |
| b72f89ea-3dad-3bc6-91ed-9dce761af3e3 | -12.3515 | -49.9833 | 2025-05-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 348.5 |
| 9731f7bb-804d-343a-8f85-567d53cfc045 | -12.294 | -52.5205 | 2025-05-22 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| bec3b303-08c0-3daa-b806-800ab7c9b7a4 | -11.5719 | -47.4521 | 2025-05-22 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a30a7252-17b3-34a3-8877-7a3562c9d302 | -12.3512 | -50.005 | 2025-05-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8256ccdf-f9c2-34ca-9914-907a141824e4 | -12.3327 | -49.9641 | 2025-05-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 30f2f85d-a7c9-38bb-8c7e-a3c312587bd8 | -12.294 | -52.5205 | 2025-05-22 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f66f7edf-eae2-31ef-a0f9-4ef359ea5cf1 | -12.3134 | -52.4974 | 2025-05-22 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| ef15dbbc-6e4c-3ac9-bf62-408b87897cc3 | -12.2946 | -52.4785 | 2025-05-22 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 230.7 |
| 8cb6db0c-8ec9-3b4a-9ba3-da8dfffa218e | -12.2943 | -52.4995 | 2025-05-22 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 620.0 |
| 465c1d1d-e7c8-3c7e-821b-18d69e871fe3 | -12.3519 | -49.9617 | 2025-05-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 77e0b0bc-d102-30b1-9395-0c24d76317b1 | -12.3324 | -49.9857 | 2025-05-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 46f28945-6879-3b95-8527-cb39021f8725 | -12.3515 | -49.9833 | 2025-05-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| c96aa17a-c6bb-31a8-9b58-f91c80f143b5 | -11.5719 | -47.4521 | 2025-05-22 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ae753ff4-9014-3805-8c38-6183ba9c2d01 | -12.2753 | -52.5016 | 2025-05-22 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 62df1429-175d-3b52-a3ee-3928a3287d2b | -12.3134 | -52.4974 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| b8cb3c75-5142-3142-a255-568657b976f1 | -12.2943 | -52.4995 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 652.6 |
| 3299ca44-310b-3fca-86a9-34fad8180ee6 | -12.2946 | -52.4785 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 310.4 |
| fcdeeef1-ef95-3f93-9334-fa5d5ebc824c | -11.5528 | -47.4546 | 2025-05-22 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| df39270b-3cc5-322d-ba78-2a61d77b1631 | -12.3137 | -52.4764 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5472611f-e55d-32f5-92e3-eae6a72efa0e | -11.5719 | -47.4521 | 2025-05-22 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8f6b4749-a2dd-3bd2-9c00-32c8e07e0ec8 | -12.294 | -52.5205 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 8879c8be-2e45-3607-b507-008a29c8695f | -12.2753 | -52.5016 | 2025-05-22 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e96779b2-e19e-398d-a2eb-deb4b5066378 | -12.2753 | -52.5016 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| abe1bb16-2669-3ad5-a8cf-b3694d0efd3b | -12.2946 | -52.4785 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 326.6 |
| 17240011-6a5f-35e2-8323-a40e1e26d764 | -12.3137 | -52.4764 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 41f9b643-763c-309a-a390-b8d28e4c4f54 | -12.2943 | -52.4995 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 796.5 |
| b1bf9168-7cb2-3af3-91f3-72510869cd9e | -12.294 | -52.5205 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 14a048ac-7df4-373e-bec1-2cb21ed4ccb7 | -12.3134 | -52.4974 | 2025-05-22 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 45bc6603-300a-37d0-a605-76fa76f5df64 | -11.5528 | -47.4546 | 2025-05-22 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8277dd4b-6219-3875-8a66-57b7827066d8 | -11.5719 | -47.4521 | 2025-05-22 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| edd6059a-9225-3874-8338-7dd3b5a83084 | -12.3519 | -49.9617 | 2025-05-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7b3341c0-809f-3bb6-a244-49d725c16c1c | -12.3706 | -49.981 | 2025-05-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 58688512-8fbe-3166-8107-7910dd09b933 | -10.8318 | -49.9023 | 2025-05-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 2624aacf-0072-322d-a8b1-ea93c9a4d723 | -12.2946 | -52.4785 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 295.6 |
| ea7b7648-42b2-377c-ba48-37d15909a8e8 | -12.2753 | -52.5016 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| d6008221-417e-3676-89df-4f3927b7a515 | -12.3324 | -49.9857 | 2025-05-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 9e7cce06-be90-36e7-a75e-7b2f5e64da58 | -10.8129 | -49.9043 | 2025-05-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |


[Clique aqui para ver as próximas entradas](README24.md)
