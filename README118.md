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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42008722-6da8-30d1-9306-cb2e8da9895c | -9.86002 | -59.83727 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88f70d63-a9ca-325c-ae08-9e35bb080dff | -9.85936 | -60.31619 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e888d825-a4c1-3927-8dd3-b7d49aa70d75 | -9.8588 | -60.3192 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d0db192-aad3-3311-8ad0-563c1e585c18 | -9.85824 | -60.32222 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11e0234a-5133-3b24-88df-55d18739753b | -9.80732 | -60.44083 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f45271d9-3464-3358-9ae2-8c8841e808a8 | -9.80221 | -60.43987 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d86df86d-7def-3606-97c4-eec4ba62f88c | -9.94906 | -60.11088 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 417a31ec-b919-35f8-80b3-ac081b870a3e | -9.9472 | -60.14958 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af4d9915-a79a-32fe-8f4e-1ff18e52b360 | -9.92471 | -59.84375 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 929ce691-946a-3a91-aac9-ebf99e0ad73d | -9.9021 | -60.31153 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0da492d-f8c9-3197-ae3a-e2519b2f10bb | -9.86442 | -60.31714 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a8776b18-5eba-3d5d-b0a4-62e6dd617932 | -9.86387 | -60.32014 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30183e07-75f7-39c1-927b-289f5c4860b8 | -9.85871 | -60.69443 | 2024-10-10 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9564e629-1f8a-3faf-8fcd-90e794488ce1 | -9.85812 | -60.69762 | 2024-10-10 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae2cc4d4-383a-3887-ad8a-8a9e133d9b3e | -9.80788 | -60.43775 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48edc17c-50e7-348f-b821-bfe791ae22a1 | -9.38911 | -61.05176 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23fccf58-dcf8-3b6d-9b27-bfdb18585fab | -9.38376 | -61.05071 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04daf0d1-002e-3430-9c5f-9234a378876e | -10.17849 | -60.89755 | 2024-10-10 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32c8504d-36ee-35e2-9cb7-e7e4f0054aca | -3.62913 | -60.21085 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60c90978-9377-3705-a541-e5e01a8bd9f4 | -3.62849 | -60.21458 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e62c115-cdab-3346-bf01-dc5098f28592 | -5.50028 | -60.46231 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83944bcf-b7ee-3590-a3eb-2a0dc25f80ed | -5.50011 | -60.46165 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ee4863e-af66-39f3-a562-33ecc2e6eaad | -5.49477 | -60.46134 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7343f32b-eb46-3110-8145-65c440990bce | -5.4946 | -60.46069 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5505f896-5a90-3aba-8c26-460435c1b10f | -7.93543 | -61.27876 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4509951a-012d-3c18-bb65-59ed6b8f8d73 | -7.93418 | -61.27573 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 878bf61f-f827-3c64-81fb-4c75fb158cc3 | -7.93348 | -61.27948 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1f81840-0f37-328a-85d8-c5b7b735a913 | -7.92985 | -61.27774 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09979c0e-6dfd-34f6-b2d7-8d1e56ae9d14 | -7.9286 | -61.27475 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9649a7fc-fd73-355f-ab60-910bed1d461a | -7.92476 | -61.24194 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e4e2b29-07ad-3f32-88db-4f8192fb1eea | -7.92408 | -61.24569 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c334dcb-1eac-3e39-9fb9-0b77abc600f4 | -7.7791 | -61.35534 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 053a7e04-a80c-3cc1-845b-edbe42d76348 | -7.77418 | -61.35046 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa62ab40-788f-307a-89e6-cd713efd972d | -7.77348 | -61.35431 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1edd4020-d38c-3687-85a0-d69f820184a6 | -7.642 | -61.20845 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f556a8d2-509d-3aa9-ba19-4c937edd272d | -7.64133 | -61.21222 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e5e14aac-c633-3d8b-a9dd-31c7ec78eb40 | -7.64034 | -61.20846 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674cdc82-7630-3e50-89d3-cf34e6184cda | -7.63964 | -61.21223 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e3d18b-b467-3e5a-9c9b-c80b140a7680 | -7.63642 | -61.20739 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 335e2c97-c2b9-3982-9ab2-59833c14830c | -9.08188 | -61.40042 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb8e3ef-0406-361d-95b0-9feef25dc7e2 | -9.08122 | -61.40406 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a1e2031-9b8e-31e2-9b72-e60f67dd6e1d | -9.07704 | -61.39572 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdfa2ed7-865f-3685-8514-35057b7152a7 | -9.07637 | -61.39939 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ba254c4-d7f6-3f75-9fa5-f9e4441b12bf | -9.07153 | -61.39473 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3468cc-c0dc-3d2d-b2f0-0016e62015da | -9.07085 | -61.3984 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91db6af8-3306-35a1-88f0-0650457fe77c | -9.00094 | -61.62108 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce666419-bc68-3a45-83b5-b2ad060bb036 | -9.00022 | -61.62494 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3eeb8a45-3e21-3ae8-8991-3817a2acd15c | -8.99677 | -61.61235 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d22b12df-113a-321a-aea4-343cfc89cee6 | -8.99606 | -61.6162 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b721b18-1c7f-341d-94ac-751a1f74b2c6 | -8.99534 | -61.62004 | 2024-10-10 04:44:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16254b87-cc29-37ff-aca0-ab431f5c2ddb | -2.6533 | -53.3506 | 2024-10-10 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| b73507a6-84c6-34f4-b5f7-756dcbe6cfc3 | -2.6716 | -53.3704 | 2024-10-10 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 42690ada-63ce-3e8f-8714-78a981dde485 | -2.6716 | -53.3502 | 2024-10-10 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 227.9 |
| d9c239e4-0640-3f33-a534-5e4abfd4979c | -2.6717 | -53.3299 | 2024-10-10 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 936f56d9-adb6-3a2e-a599-4c4f5cca1f6c | -2.69 | -53.3497 | 2024-10-10 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a3851a41-5f14-3d3c-9c69-ad4340589974 | -4.0961 | -48.2739 | 2024-10-10 04:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| d5a4b162-2692-329d-b286-787602ae658e | -4.0962 | -48.2523 | 2024-10-10 04:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| eb28ed14-a6ce-3b19-9b33-3769da3329e9 | -4.1146 | -48.2731 | 2024-10-10 04:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| ac3f92ff-2fcc-305a-8abd-eb4a11e5dd6b | -4.1148 | -48.2515 | 2024-10-10 04:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| e39b4134-48c1-3c12-9466-bb3ed46bf6f6 | -6.7654 | -59.3252 | 2024-10-10 04:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 9f68a1ab-a8a3-32f3-9abe-40eeaafb8783 | -6.7655 | -59.3059 | 2024-10-10 04:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4964c384-862d-3bc4-8077-44ea85dbca3b | -6.7839 | -59.3245 | 2024-10-10 04:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f5e916a7-58c0-32e5-bde6-8e811bff7469 | -6.784 | -59.3052 | 2024-10-10 04:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d35778dc-4cd8-39b1-bc9b-3d692ed92795 | -7.0971 | -59.408 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 23c85df2-dfea-33b3-a00d-e2826cf80c07 | -7.0417 | -59.4103 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 63b45ed1-e0c0-364e-8569-cddb46a8aad3 | -7.0601 | -59.4095 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b47419a9-d434-3d6f-ba3f-f55358c9b75d | -7.0785 | -59.428 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f641f84e-d615-36ca-b216-e0b90f48b3ed | -7.0786 | -59.4087 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 8128b577-cb72-329c-8cc3-e0f36098f097 | -7.0787 | -59.3895 | 2024-10-10 04:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b96952c3-ceca-35cb-9cce-3b842e4e1abf | -9.0656 | -61.3934 | 2024-10-10 04:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a57e117c-676e-3946-82af-c894fdcb9567 | -9.0841 | -61.4117 | 2024-10-10 04:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 81e88835-d704-36b6-a29b-2456d050edaa | -9.0843 | -61.3734 | 2024-10-10 04:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f2a5190a-12c2-3e8f-8b93-38571a235af3 | -9.0842 | -61.3925 | 2024-10-10 04:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c1370d0f-2e32-3fc1-8cd5-a8d78b86baa6 | -12.98662 | -62.74682 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d75223f3-5417-3ff9-bdae-c9666d2716cb | -12.98585 | -62.75069 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0184bd11-f594-3e58-87cd-944f6b89d90b | -12.9753 | -62.69799 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a870e5-e286-3bd8-920d-4625ec23114b | -12.96972 | -62.69678 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2cd5a5e-76fb-3017-a6f4-13f979881681 | -12.96897 | -62.70065 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d3db87-1681-3178-b810-be5a35eab03a | -12.96822 | -62.70452 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d06c6ad8-9be6-365b-8bce-9e407f94f2e2 | -12.9672 | -62.69841 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df2be6e3-bb79-3e26-b547-5d2e857e4275 | -12.9649 | -62.6917 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a6abf4-0736-33f1-95f2-2a640599be95 | -12.76174 | -62.27116 | 2024-10-10 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0752e2de-b7a1-326b-b333-fa14dbb9611a | -17.32121 | -54.98639 | 2024-10-10 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8f13267a-3664-3565-ada6-0d1b988e4217 | -13.84824 | -44.50981 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65d77856-8f64-3678-b594-204b4ca2e359 | -13.84754 | -44.51561 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e094dc6-37ce-3d6d-84ff-6441a157a389 | -13.84188 | -44.52085 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c908b9e2-a5d5-3d77-8e7c-f367963409d9 | -13.8406 | -44.52105 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a670b101-5e50-3038-aa50-ce89c756f98c | -13.83693 | -44.52024 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eed5107e-0d42-317c-858a-f9f19f0e53ef | -13.83565 | -44.52046 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c365ccf-add0-3d77-943c-5ca069fdcdb9 | -13.83198 | -44.51963 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc5553a2-40ff-328f-9601-5aef2b70037a | -13.8307 | -44.51985 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbb62ac8-5c03-3597-b3ed-de68ad728dfd | -13.20381 | -43.12679 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e961f766-d400-3be5-b3d0-73c501021ae0 | -13.20339 | -43.13025 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3fbf9fd4-85ed-3a7b-abf2-11572a840722 | -13.84872 | -42.6412 | 2024-10-10 04:46:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82705671-72b1-3cd6-8de4-0de1a35139b3 | -13.84542 | -42.63768 | 2024-10-10 04:46:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ff9e73c-a205-3870-abda-0937b91330e2 | -13.8449 | -42.64193 | 2024-10-10 04:46:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4808efad-5d7d-32b1-82d3-3e248f767847 | -13.84309 | -42.64066 | 2024-10-10 04:46:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c049fec0-3fe5-3675-837e-b4c9ca2700e1 | -13.82623 | -42.41242 | 2024-10-10 04:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9fee3298-4682-371e-8a17-efc7ec6d4720 | -13.82577 | -42.41639 | 2024-10-10 04:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 97fa6140-8686-3048-bcc2-4eae1899556d | -14.44172 | -43.18202 | 2024-10-10 04:46:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README119.md)
