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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae7d8ad8-7a02-34a4-a1c7-df12ff569f2d | -4.19188 | -50.6853 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0dbaae4c-64b7-32e6-8619-b46048fb0237 | -1.14207 | -48.34086 | 2024-11-29 00:52:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a12e4ddb-9d97-3f47-a2d8-cd08f7e94fef | -1.67991 | -46.92902 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e9f1e5d8-2be0-35fb-9fd5-824ef529d47d | -3.24965 | -50.5947 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b72dd9da-e4bc-3007-a742-365648159056 | -2.66704 | -46.13675 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef63f2da-9cdd-318a-9e2b-51786905a436 | -1.07322 | -53.63197 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 699e902e-69b4-339d-8b29-caf9048ea49f | -1.71136 | -52.7724 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e67e4488-71c3-32eb-849e-743fa9dc2a58 | -2.6575 | -48.78193 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 281.8 |
| aa403831-55b0-327a-be93-59ffb2078920 | -1.73029 | -52.47615 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 743e1192-6643-39bb-8a9d-5605bb5a4aec | -2.01385 | -51.1869 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| abeb7006-c8fd-3c98-82b4-e949816f6853 | -2.75906 | -54.111 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 7e568589-81c9-35e3-b273-22c9f292d25a | -2.71436 | -51.97458 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 7e8153d2-8426-352c-88b3-a3a2497070e2 | -3.24826 | -50.58463 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c43d934b-012b-3cfb-be94-172b34b94ff5 | -2.98766 | -53.28717 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 608.7 |
| b4dc49f8-8f8c-3487-a137-a83ea9925f0d | -3.23857 | -50.18804 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 903f5db8-b3b0-3202-b7f5-de38bec7edc2 | -3.97232 | -47.24252 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6afe6bf-f2c0-31e4-9e28-dba06c6fc0c7 | -3.32179 | -54.1716 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c1154c7b-33fd-36b0-8357-d4ba721a74fd | -4.11249 | -50.77677 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c7d7769-defe-3bd3-9fde-ce8c1f61cecc | -3.28463 | -50.04468 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 82b81472-a129-37d5-b969-2d92ee721440 | -3.06602 | -45.11226 | 2024-11-29 00:52:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ef3c3812-e184-3adb-91bd-a6539ac970d7 | -2.85068 | -54.02298 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5e0e3602-66d7-3f5b-a41b-679af7a60d87 | -4.06977 | -46.82368 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 857f03b0-b39e-3670-8c24-6261392be937 | -4.02428 | -49.13452 | 2024-11-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7648e415-0c30-38da-adf4-8c2f3e7d5733 | 0.9767 | -50.26134 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5e0affc1-2225-37d9-96fe-f24269b08510 | -0.56983 | -51.69736 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 687650f9-09ef-34ea-a116-2921ab9ee92e | -4.04508 | -46.84314 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5cf58ff1-0081-3c94-bb58-794ba889aebc | -4.14754 | -43.81522 | 2024-11-29 00:52:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ac9b3d0c-5fa0-333b-b815-ec4e7ffcaaad | -1.38327 | -53.63201 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7f99f837-b8c8-3067-9c56-f649f86a736f | -4.1734 | -48.61785 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a6d5df0b-68dc-310f-93e8-882c599d3262 | -4.02775 | -48.89569 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a3944ba-78e0-3e2f-aa6d-0087a24c94c4 | -1.62539 | -52.45899 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac2853e7-a4d4-371f-8358-7e9115c66219 | -4.65802 | -46.54981 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 562b0ed5-dcf1-3166-8ef1-8e45c19c3e96 | -3.469 | -44.92736 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5fe2a0ae-9f43-3bb6-9d49-f0df6fe27f50 | -1.34603 | -51.98104 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 35cfce66-baca-32cb-9264-554f4f0c32b2 | -3.70657 | -47.12252 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1125f4b4-a7eb-3b73-b3b2-6dc12abd6452 | -0.16234 | -51.48842 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 20.6 |
| fc33502c-218a-3ae2-b617-f5df3cd74d39 | -0.99448 | -51.72939 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d9e4ef85-97a2-37e7-96dd-b4d0a23bf0f0 | -3.40649 | -49.52983 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0f35bf03-329b-3bc2-8a17-a9b3d06272b5 | -2.66578 | -46.60355 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c1360374-507a-373b-93b2-bec584e8b0d5 | -1.31127 | -51.73375 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a31cb2a0-6ee1-3035-8eb8-facd5d156e95 | -4.05047 | -50.32631 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e106801d-6ba7-31a7-a9db-6f013fcebc49 | -1.49189 | -52.43924 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 227af4ad-0c1b-3456-a56d-dd3acada8175 | -4.07213 | -47.03655 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e43439f-036a-318b-a95c-2bb9a430ca23 | -2.83761 | -48.0906 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 057b478b-a013-3b06-8744-3b2549860d81 | -4.36971 | -47.25351 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7d38cc8d-ed80-3477-8256-d528ed14c9cd | -1.59319 | -52.28182 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b9889388-c92e-334e-a816-019e7e2ffb65 | -1.62708 | -52.47145 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d9254ab9-d9ad-3423-acc1-a0ebc395f383 | -2.14715 | -50.60835 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1896c093-e38d-3389-9ef4-7169cb557b09 | -3.37294 | -50.82141 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e382cb24-85b3-33f4-bf8d-a4f3a6ad6f97 | -3.77476 | -46.69371 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 87a7a19d-3dd9-3393-a501-e48581643a7d | -2.84307 | -46.8743 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 698cd025-b7c6-3dda-b187-426e98f4abaa | -1.53588 | -52.67676 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bd7c5db6-fa1a-3236-9fbf-35c784485f01 | -3.72852 | -51.0941 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5d8589cb-2b95-3673-8a19-dec441814f8b | -4.07987 | -47.02615 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4cdce57c-744f-38c1-8bfb-1d7977158837 | -2.80519 | -47.5896 | 2024-11-29 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 26c55a74-bd01-326d-8337-90610dd72323 | -1.36556 | -52.11986 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2896de3c-a2c4-37af-aedb-68a4043acab9 | -2.98972 | -53.3021 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 8a21360f-68d1-3b95-96ba-ee0d1895f47c | -1.35221 | -54.9933 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 856d9fa0-9d97-3b5b-b590-226ae89919f3 | -4.17463 | -48.62672 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| e7a1afbf-acdb-392d-840a-9aafbf02b35a | -3.80085 | -46.68042 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 48ba3a95-a81e-3141-8b8c-65887cce9352 | -2.94746 | -45.71996 | 2024-11-29 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ebdde23f-cc25-3888-a428-108305063f46 | -4.76016 | -49.53315 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17aeccd6-ff7a-38da-ab49-22864a6ae882 | -5.62722 | -46.96003 | 2024-11-29 00:52:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 85892d15-434e-33fc-be09-f564c858a26a | -3.11215 | -53.10716 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d0a3d75a-1631-3430-968f-141241c02201 | -2.85855 | -45.52874 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6ceac055-325a-33b2-a862-c8fda4c744ca | -3.96217 | -46.90817 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87178acf-ac0f-3999-9855-4855bfa47f75 | -2.23013 | -53.69614 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 7ae58b05-1264-3983-90aa-5dc97ae2569a | -0.05024 | -50.82399 | 2024-11-29 00:52:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 531fa5a2-aae4-3ea6-99f7-bf5da92ca8fb | -1.64845 | -52.7468 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2548eda4-43ea-3fda-8cad-b37118e89e5c | -3.68984 | -47.13422 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9e81ae9c-4262-36d8-997e-91438578e9cf | -2.84175 | -46.86486 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| af71129d-3c0b-3cd0-93c6-d1f47ea7945d | -1.65135 | -52.49352 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 335bde63-dd9e-3648-b02e-78e1bfb51074 | -2.58125 | -45.51975 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| dd16230a-582b-37bf-b0e8-49130f1d7a54 | -3.30461 | -45.5009 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 6fd2c6d3-6ece-39d2-bdcb-ac6e4adb2698 | -2.76148 | -54.12827 | 2024-11-29 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6db9ce40-d5b1-31fe-a8e8-a9e1e0a5f9b7 | -3.22252 | -46.29708 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 781cff09-b908-3d7f-aa5f-661a1d5ff640 | 0.33501 | -49.71725 | 2024-11-29 00:52:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d51c8c97-74c6-35a4-ba05-67e7543a83ee | -2.83911 | -46.84597 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7bac1d82-8aec-3729-a7ed-27d4b2bafeb6 | -3.17717 | -46.31374 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ccea4527-2ea2-31ae-9ad7-88bed41a6af7 | -3.17814 | -50.28182 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd643b71-2eb3-3d86-8cce-5f19b9112a9a | -3.52863 | -50.47611 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 088ddc7c-5b54-349d-91f9-0b1ed3ab32d1 | 0.36165 | -50.90286 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 208bb7c6-b511-3870-8d18-1156f21763b8 | -1.2609 | -54.54335 | 2024-11-29 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 50a225a8-eee6-38ee-a3f7-0846990fff50 | -3.02877 | -54.03234 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 473358af-2aba-32e4-a957-fb28b1706ff2 | -2.55643 | -46.41497 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cceb3a5b-fb0d-3b0f-804f-057a7a0199b2 | 0.18647 | -51.24505 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45f7ca1d-ad5a-347c-89e9-adcbf46bb1ff | -1.04505 | -51.73343 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5397cd7d-7df8-3026-8e70-9a93c92b5ac0 | -4.00055 | -49.96443 | 2024-11-29 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 792a994b-fbf8-3858-a418-2092e73cbb6c | -3.53295 | -44.94807 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7b9b5863-1860-3926-b62a-6e3f1cc53c25 | -3.6085 | -49.85911 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 29ea9385-5cc1-333e-a87f-50d2d98b9ed3 | -1.89144 | -47.51225 | 2024-11-29 00:52:00 | TERRA_M-M | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4c129083-a10f-3665-b7c6-74b12b353f7e | -1.04661 | -51.74441 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 759565e2-2246-3711-afba-4b125fbcb8c2 | -4.23508 | -45.7792 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2f5a0785-953e-3fef-8848-bd4d06073c39 | -3.82311 | -44.0397 | 2024-11-29 00:52:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 23143b7b-3e43-31f2-9e30-b7eea60cfe99 | -1.30124 | -51.95237 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 5df5ebf5-7b53-326a-944b-71c17984539a | -2.88275 | -46.83393 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2edfe06c-c4de-35eb-bbbb-ff5564993740 | -2.67733 | -46.27979 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9f9034cf-2822-397e-9b12-15ed168271f7 | -4.43223 | -46.58492 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 41867514-e0dc-3b72-8949-f21b40d28f00 | -3.3756 | -50.17293 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 52d73e08-bcbd-3822-b17d-ab78529627c0 | -2.06118 | -46.37378 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README8.md)
