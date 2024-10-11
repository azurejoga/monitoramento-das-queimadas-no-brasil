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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38397494-b5d6-3d59-a869-cf2209de77a7 | -2.9857 | -52.9164 | 2024-10-11 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 26d33227-6d04-3431-ad6f-3227ed4f3168 | -2.9673 | -52.8966 | 2024-10-11 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 89e28ce5-1a29-3a1d-b76c-a76ccdbcf882 | -2.9673 | -52.9169 | 2024-10-11 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5494c269-236e-3da0-bd64-6a05dcb30f60 | -3.1608 | -50.4347 | 2024-10-11 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 77c25a14-371a-364e-9a4d-96cecedce80e | -3.1607 | -50.4556 | 2024-10-11 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 453bd2b9-5cf1-3c8d-afd0-312cd5c9f2b5 | -3.1423 | -50.4352 | 2024-10-11 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8d4bc504-8320-3d0c-85b3-671ec825d27a | -6.5589 | -60.0252 | 2024-10-11 03:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6fd0994a-63b4-3a27-81dc-ea22bebab774 | -8.4417 | -55.4692 | 2024-10-11 03:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 98e3d2ae-3b62-32bc-9448-19449a1e709a | -8.4231 | -55.4704 | 2024-10-11 03:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c217b29a-1f5d-361c-a7e8-b48875946405 | -9.9481 | -58.1092 | 2024-10-11 03:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7b0810e1-2cc5-3d36-9011-962270e1e2e0 | -10.6965 | -53.0147 | 2024-10-11 03:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d67499a2-ab9b-37d0-99b8-b2a9b41d9211 | -10.6962 | -53.0354 | 2024-10-11 03:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2ee6e22d-9823-3c1f-b832-dae3fdf9db94 | -10.7059 | -64.1138 | 2024-10-11 03:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 86001a1f-0123-3fb6-8abf-c3dacc3c27b6 | -11.2912 | -50.9208 | 2024-10-11 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3381626f-6334-365a-8b52-d859fed9825a | -11.2909 | -50.9421 | 2024-10-11 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8f56956d-ab61-37fd-9ce8-796dc37eed09 | -11.2722 | -50.9228 | 2024-10-11 03:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8172379b-3247-3d9d-97a4-b72c99d55996 | -11.2328 | -51.0333 | 2024-10-11 03:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 90c9925f-ad37-325c-ab02-4a7c591b2b17 | -12.5996 | -55.1958 | 2024-10-11 03:06:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b4c97f1d-d13a-341f-9085-403cdac670c7 | -12.5994 | -55.2162 | 2024-10-11 03:06:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0e452813-a40c-38d9-9969-c764c452bd84 | -13.7348 | -60.5883 | 2024-10-11 03:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| df5604b1-f7e2-3ce1-a4df-8a325c2cdd1f | -13.7346 | -60.6079 | 2024-10-11 03:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7d48f2b8-b023-319f-bf8d-c6150d7cc590 | -13.9857 | -45.7992 | 2024-10-11 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 079a28ae-571f-3a0f-ad30-3ab6a9e7b197 | -13.9663 | -45.8025 | 2024-10-11 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a7649569-17f5-373a-bcaf-d89b229c34e4 | -2.6533 | -53.3506 | 2024-10-11 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 11835f0f-2176-30a8-b172-51bf83d4318e | -2.6716 | -53.3502 | 2024-10-11 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| bfc25c52-0508-3eaf-94cc-195afe5e3673 | -2.9673 | -52.9169 | 2024-10-11 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e11fa465-9a9b-3262-8aba-e97517d2daa5 | -2.9673 | -52.8966 | 2024-10-11 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7ba76f9d-2b90-3b1f-9858-b5508b725e00 | -2.9857 | -52.9164 | 2024-10-11 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 038100b4-4e43-31a0-bc0b-87b265f88610 | -2.9857 | -52.8961 | 2024-10-11 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 360f5e01-315b-390f-9991-27d642ce4342 | -3.1423 | -50.4352 | 2024-10-11 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 54673efc-5a38-3397-93d5-ef86fac24fd2 | -3.1607 | -50.4556 | 2024-10-11 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 94c0d065-a369-306a-82ca-545e69aee72c | -3.1608 | -50.4347 | 2024-10-11 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| ffe01b7a-9484-30b2-9386-6ec26479d174 | -4.0962 | -48.2523 | 2024-10-11 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8046d986-a435-31d4-8fe8-f8484eb77c77 | -4.0963 | -48.2307 | 2024-10-11 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ed803666-3aad-3cba-99d1-249de3bbd5a2 | -4.1148 | -48.2515 | 2024-10-11 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 67d04f20-5cab-33fd-86d7-f5c7c93ca142 | -4.1149 | -48.2299 | 2024-10-11 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0e4fa47e-b31c-39b7-bbd9-2254c56bbed1 | -4.1333 | -48.2507 | 2024-10-11 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| fb7d1d23-11ea-37cd-bd1c-616d2a185d90 | -6.5589 | -60.0252 | 2024-10-11 03:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 2d548e81-b779-3cd8-9c13-5fd04c465905 | -8.4417 | -55.4692 | 2024-10-11 03:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3c08c061-c9e3-357c-9597-78b443e5ce5f | -8.4419 | -55.4491 | 2024-10-11 03:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6e7da0c0-8e66-35e2-86ef-29f7be8fb0de | -9.6389 | -64.9664 | 2024-10-11 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7d206757-c28e-35c2-8386-0828de03b037 | -9.9481 | -58.1092 | 2024-10-11 03:16:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2aa74bfe-0531-3f05-a536-2ee34356e51a | -10.6962 | -53.0354 | 2024-10-11 03:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a2fbed7c-6103-34dd-bb1c-60783b96795a | -10.6965 | -53.0147 | 2024-10-11 03:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5fa3b60d-d884-32d6-a935-8835b4c10fb2 | -10.7059 | -64.1138 | 2024-10-11 03:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e25d5118-97a2-315c-a952-c5038ccfa1d3 | -11.2328 | -51.0333 | 2024-10-11 03:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e35b0c31-369b-3b0c-9fb8-b2f037964092 | -12.4182 | -53.1544 | 2024-10-11 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 62859aba-e74d-3304-8a18-4222153a127a | -12.4373 | -53.1523 | 2024-10-11 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ee49bf56-deff-3ef5-9f60-04d80554d0bf | -12.7678 | -44.8671 | 2024-10-11 03:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7da2aa6f-a46a-3827-98c3-08fe583b1e7b | -12.7871 | -44.8639 | 2024-10-11 03:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| fd623f4f-13fe-3631-a862-ea6e3fba50a7 | -13.9663 | -45.8025 | 2024-10-11 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8524c46c-ac2b-3531-b72e-0d345cdba5af | -13.9667 | -45.7794 | 2024-10-11 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fae406b4-884f-3037-b3b8-2044e27f8a5c | -13.9857 | -45.7992 | 2024-10-11 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| dd1a0bf8-dac6-3196-a45b-181289f9c13a | -13.9862 | -45.7761 | 2024-10-11 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a172dd9d-109a-36e3-8324-c6de198f6471 | -13.7346 | -60.6079 | 2024-10-11 03:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e61de96a-0db9-306d-b24c-b4bf567001ef | -13.7348 | -60.5883 | 2024-10-11 03:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 244014f3-7a46-3b71-a6ed-43de7138ff07 | -2.6716 | -53.3502 | 2024-10-11 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 40c86c86-6752-35f4-b2e6-e629c25e88c9 | -2.6533 | -53.3506 | 2024-10-11 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b104655e-14d1-391c-b3bc-52e656d99627 | -2.7847 | -52.4933 | 2024-10-11 03:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a4d9aad1-5e5c-363d-8304-a3f932de941a | -2.9857 | -52.8961 | 2024-10-11 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 59b93c6d-6ee3-34c0-aea1-df6149600206 | -2.9857 | -52.9164 | 2024-10-11 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 268c354e-87ef-30ff-8a16-0df89ff416ce | -2.9673 | -52.8966 | 2024-10-11 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 456e0425-d596-3c4a-9e27-47b2084f2695 | -2.9673 | -52.9169 | 2024-10-11 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9e1cb9e7-46dc-3207-ad19-c569743708dd | -3.1608 | -50.4347 | 2024-10-11 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 11140c23-fa85-3e29-adc1-b3c275061802 | -3.1607 | -50.4556 | 2024-10-11 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a0a21912-1882-35b0-af88-3fbe68cb59c3 | -3.1423 | -50.4352 | 2024-10-11 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 13ca23de-30c8-374b-9f72-ae63ce17f4c5 | -8.4417 | -55.4692 | 2024-10-11 03:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 61910092-3327-3750-ba7e-e1548bbe3d99 | -9.6575 | -64.9658 | 2024-10-11 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 70ebba23-a14c-3182-bda9-469d5aa5ae98 | -9.6389 | -64.9664 | 2024-10-11 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0e5763af-4c91-378d-a778-7c173889092d | -9.9481 | -58.1092 | 2024-10-11 03:26:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| e4e187e8-dfd6-3220-b338-b6caae8b0e25 | -10.6965 | -53.0147 | 2024-10-11 03:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b36f3a66-4c45-38aa-bd9d-58dd600ef0d5 | -10.6962 | -53.0354 | 2024-10-11 03:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f16bff0d-def2-3b16-bfc8-b2281d1c9da8 | -10.7059 | -64.1138 | 2024-10-11 03:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4b37487c-1b11-3d16-a5ac-f79242f42c93 | -11.2328 | -51.0333 | 2024-10-11 03:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d9761ef4-b528-31b2-9c24-d43ba96ddd7c | -12.4563 | -53.1503 | 2024-10-11 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 505c77e7-a07c-329c-90c6-fbd538f6c77e | -12.4373 | -53.1523 | 2024-10-11 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| bfdec96f-af61-372e-bd9a-86bd4f3dadd9 | -12.4182 | -53.1544 | 2024-10-11 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e9f6c545-cabd-3d90-afeb-07cef41c39d0 | -12.7871 | -44.8639 | 2024-10-11 03:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ea840163-d80c-314a-b303-9fbe1d13115c | -12.7678 | -44.8671 | 2024-10-11 03:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0c8e1f99-e5c9-34e2-b894-9e449d475594 | -12.8708 | -53.4799 | 2024-10-11 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 696a5821-1d1e-30df-8e3a-bf981c0001f8 | -12.8517 | -53.4819 | 2024-10-11 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| dc9a92d6-0c01-3316-9603-0fcee16d2df7 | -13.7346 | -60.6079 | 2024-10-11 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 85a53365-7efc-3b6a-b343-6933d10d1539 | -13.6687 | -59.6497 | 2024-10-11 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f8a30598-42f6-3873-8dc1-1f3926c2cbc3 | -13.9862 | -45.7761 | 2024-10-11 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0ccf23f4-65ec-3c8d-a59f-1916be7de1e5 | -13.9857 | -45.7992 | 2024-10-11 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 4f4b6cd0-70fb-3645-8eed-1cc4e193bdd9 | -13.9663 | -45.8025 | 2024-10-11 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 36b79203-fd04-3cda-96ab-e12685a256b3 | -2.6533 | -53.3506 | 2024-10-11 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| cf53fcbe-0254-335e-a976-20e2c0c52d99 | -2.6716 | -53.3502 | 2024-10-11 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 9703cc23-8e30-338e-b58d-21e46959fdd2 | -2.7847 | -52.4933 | 2024-10-11 03:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2ca6bfb4-ac7d-38cd-a8c9-d5e47c2ee89c | -2.9857 | -52.8961 | 2024-10-11 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| b836b3fb-8a90-3a83-8b13-cd0860bc15b3 | -2.9673 | -52.9169 | 2024-10-11 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 324a7960-628b-3797-b6cb-d755ef38e33b | -2.9673 | -52.8966 | 2024-10-11 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c176a0fe-34ce-3505-b3a4-490528f27aaa | -2.9857 | -52.9164 | 2024-10-11 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 59069bee-5456-327c-b5d8-1bb3549cfdaf | -3.1423 | -50.4352 | 2024-10-11 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| cd038099-2d39-3a8d-bffc-8f4a673a81dc | -3.1607 | -50.4556 | 2024-10-11 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 470138f2-5a45-33a6-9dcb-bc9a1d37264c | -3.1608 | -50.4347 | 2024-10-11 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7d55dd0f-cfe5-36fd-ba03-4888f6eee8a7 | -8.4417 | -55.4692 | 2024-10-11 03:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 718df704-0881-3129-baa7-1e92cba1dea5 | -3.60623 | -44.78656 | 2024-10-11 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 704e9ef8-5243-30ea-9e4e-a901266d2416 | -3.36803 | -44.36699 | 2024-10-11 03:36:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e19ff1a9-0e37-3216-b0fb-56d79bd1e0b7 | -3.36774 | -44.37461 | 2024-10-11 03:36:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README30.md)
