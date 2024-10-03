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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5aa4a59-288e-3421-9d92-5cd03089ae3f | -16.68204 | -57.45446 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| daab8f57-baff-3745-a9fa-fa78fb9deb41 | -16.68201 | -57.14977 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 978be5b5-1abb-3d26-b8d5-d774640ae37f | -17.84429 | -57.69667 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 14bfe56a-8560-33ef-ac14-901cc33ec0ad | -17.84365 | -57.70127 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9b76961a-425e-3ef0-8b0e-2d275fa89881 | -17.84121 | -57.6915 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 12ee26fb-e819-3af5-80ae-198f02c0f4da | -17.8375 | -57.69093 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6f906205-fb95-38c7-95ba-e27d0c2860a7 | -17.83378 | -57.69038 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cc342b89-572b-3e99-b0ec-99fe8c1899ca | -17.83251 | -57.69957 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6f90e5ee-6fcc-322d-a61f-cb199ea6b410 | -16.90936 | -57.69097 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 26149aee-3739-31ca-b44f-6b98c1d90bb2 | -16.89955 | -57.68031 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9eaaf478-104c-3178-88e3-a7844708103d | -16.76814 | -57.82331 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b8f46db3-fe6f-330d-9e9e-27c747e58a0b | -16.76752 | -57.82771 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aab96445-276b-3009-948b-bfd8acb98e8d | -16.76416 | -57.82527 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5560ae1-0460-3e9a-8f85-1e0b747eedbe | -16.76387 | -57.82716 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d3dc9e90-de1d-31cd-8db8-e22cfc31df4d | -16.76356 | -57.82967 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| de406650-7352-3216-a9e2-ba727c005434 | -16.69189 | -57.46528 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7b11804e-1b18-3ebd-80d0-55115dca698a | -16.69125 | -57.46985 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7dac1cfa-dedf-3ef2-93e5-569877ae3eba | -16.67823 | -57.14921 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| d710364c-580d-378e-8836-5a3c270e0914 | -16.67759 | -57.15396 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| dab5e168-c7a3-3b5c-914a-2b94fe702454 | -17.84237 | -57.71046 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3981d2f0-cfa9-3a91-8898-a560a1824684 | -17.83994 | -57.7007 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2fde9033-80d3-3994-a2e8-98a3f473ff8f | -17.8393 | -57.70531 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4bfdda8a-d620-35db-a0ad-fb9b0568fa67 | -17.83686 | -57.69555 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7357e2d2-c5be-35c2-ae3d-c665ba52c9a3 | -17.83622 | -57.70014 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a2f13e59-da8f-3312-8542-d47e629c36cd | -17.82943 | -57.69442 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8927f2e8-05ee-3ba2-afaf-16788c308f68 | -17.84672 | -57.70643 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 56176b9f-7727-396d-8974-629cad734bd9 | -17.84301 | -57.70587 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 065e3c75-adcb-3b17-a6c8-1da876e238ef | -17.84057 | -57.6961 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 041a9976-439a-3ed1-8c35-df89ffcd98f8 | -17.83314 | -57.69498 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cae1e3c7-80d1-3a3d-a61d-7088bd0c81d6 | -17.03976 | -56.74907 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c385cc4e-3c28-3e45-af51-656fb66b161d | -18.90689 | -57.71022 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 121b0e41-e215-3d4e-8f39-557f1f12f096 | -18.90313 | -57.70966 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 244db571-27de-3f61-9bf1-0b0677e10fa8 | -18.72646 | -57.33258 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2a9e44a5-0733-3a61-8824-45f708b50baf | -18.72262 | -57.332 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 968e7b96-66f0-34b9-b154-a45e5b828444 | -18.71945 | -57.32647 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b4ff0e29-63fe-3ecb-8973-f22b52c6e8da | -18.71879 | -57.33143 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b7e1c58a-1b01-3e49-8ee5-da120efcb8e9 | -18.71627 | -57.32092 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 15999dc8-174c-33cd-982c-14da0633ca93 | -18.69839 | -57.30816 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3d589481-d8c7-3262-b8f1-0d07fe4ab2a8 | -18.69455 | -57.30759 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6d785908-c38e-3b3d-bed0-395f5f3a5c0f | -18.6939 | -57.31257 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 74524204-95db-3d83-bdb4-9d0eb2c12870 | -18.69324 | -57.31754 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 387143e9-3283-352d-82da-5208840cbd06 | -18.69071 | -57.30704 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2e24bfec-986a-323d-a60b-18a75523cd33 | -18.69006 | -57.312 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0af420a6-00cc-3058-895b-58720d577968 | -18.61892 | -57.58783 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5c015bd1-6cde-3fe2-b610-e1b8e6efe382 | -16.60217 | -58.2159 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 739c9283-1e72-301b-b857-cd3c9df347b3 | -16.6004 | -58.22858 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a900a200-7df5-3836-ab66-68b32c0ca7f4 | -16.59959 | -58.21665 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 3d8b4e3e-de5b-3638-b62d-e1ac3025804d | -16.57939 | -58.20488 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 26f0e932-e9a2-3280-baef-9d5cb5de5817 | -16.57582 | -58.20435 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 8dca56b6-9552-303f-b777-f4ffd0065f48 | -16.57225 | -58.2038 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a6a7c174-6ae2-32c8-9e9c-cf582245b77f | -16.56571 | -58.19848 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 8d4340b2-ebc3-3813-9f8c-74061fe93f86 | -16.5645 | -58.20689 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 8c388e18-4a20-3a57-8333-9816fb5e36e5 | -16.56393 | -58.18534 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 153384eb-1b27-3945-90a4-4c7e66ba1c1e | -16.5639 | -58.21109 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 285be1c0-2cd9-3e31-b971-dfca78cf2d97 | -16.5633 | -58.21529 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 73898ac0-13d3-3d7e-bd5f-231eb73fca88 | -16.56214 | -58.19793 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 02f97975-bfda-3092-ae66-df163e18d431 | -16.56153 | -58.20213 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| a0a7cf08-cce6-33f6-b70b-b1cb98d1b7a7 | -16.56093 | -58.20634 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| a029dc2b-6ddc-3602-8fa5-96cbac8367b5 | -16.55676 | -58.21 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 1eda74a4-3ecb-31ad-9115-7c23f3f88b2e | -16.55499 | -58.19684 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| f0daff88-e610-3d13-91e4-cfd5b3036caf | -16.55319 | -58.20947 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 58fae171-e765-3646-9197-586a998ec706 | -16.55259 | -58.21368 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| c5132515-f138-31e8-8bdf-2774cd41c89e | -16.55142 | -58.1963 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| cdc60762-760c-3423-84ef-34d0b9750317 | -16.55082 | -58.20051 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.3 |
| 450cf867-0f3e-37eb-ae16-f825308a95fc | -16.54902 | -58.21315 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 237.8 |
| 89ac59ab-ffd6-3c5e-a815-eb859cbb5822 | -16.54784 | -58.19577 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| 7b6b19c9-6ed4-3819-9eb8-fcbb5e273d13 | -16.54725 | -58.19998 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.3 |
| 456e1cc0-4f4a-3cb3-a82f-2b59616908d9 | -16.54605 | -58.2084 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 237.8 |
| e5df7855-ae97-322c-96eb-bb93182e5584 | -16.54545 | -58.21263 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 237.8 |
| 57b9d447-ec7b-352b-b712-c0cf5b4a23e0 | -16.54308 | -58.20365 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3551d97d-c208-3fe6-9559-d530c95103fd | -16.53951 | -58.20312 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bf1cb8c3-4471-345d-b307-d31a5e290d97 | -16.53891 | -58.20734 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4af53536-187e-3ad3-8ce5-fdfc47745150 | -16.57164 | -58.20799 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e97cf199-5c6e-352e-ae0b-7752ad0f13bd | -16.56868 | -58.20325 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| fc448feb-6584-32b4-a14b-5ad38467bbda | -16.56807 | -58.20745 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1ac64899-5d62-3767-8633-f026336fbcd2 | -16.56511 | -58.20269 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| ed983573-9642-3b1e-9175-99a96b156de1 | -16.56036 | -58.1848 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| e01564a8-995b-360c-90f0-3d63c3ddca2a | -16.56033 | -58.21055 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5ca4e142-7bd4-350f-8ec6-deb949639990 | -16.55973 | -58.21476 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3361fe4c-38b4-3acd-9d5c-8f483292c7ea | -16.55857 | -58.19738 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 0f603c66-b3e2-38b4-81c5-7a578cd0ac03 | -16.55736 | -58.2058 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| af669be3-ed0d-3eb3-bf98-88eb2f313a3a | -16.55616 | -58.21421 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 43b9813d-a93c-34b2-948b-48590f3e514d | -16.55559 | -58.19264 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 8764cef0-c45e-3aff-b3cb-17cd16170c2e | -16.55379 | -58.20525 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 9b9b908d-8fd5-31b7-8b3f-724662e3e245 | -16.55201 | -58.1921 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| 23188924-7f09-350f-af98-6c06635834d0 | -16.54665 | -58.20418 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.3 |
| d9f3a857-cbff-3d60-88cc-fa9baba7bbfb | -16.54485 | -58.21682 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d1cbb634-dd83-3bce-8746-1fabeef90645 | -16.54427 | -58.19524 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| a5c102f7-2346-30c0-a50b-19d41f20d52d | -16.54367 | -58.19945 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e3f2b929-7a06-3fb2-a2fb-3e8330a657a8 | -16.54248 | -58.20787 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c456bd7f-2a8b-355d-b271-466b4e5bfc42 | -16.54188 | -58.21209 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 74863686-7661-33c4-ba85-8e8cca144622 | -16.72904 | -58.46794 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5f1034e5-d80c-3be2-a77e-235e03a13433 | -16.73258 | -58.46848 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b30682c0-2aed-3555-8900-e5499c259f23 | -14.78661 | -59.42968 | 2024-10-03 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa4dd70f-48c2-3567-a754-3bd4fd79374e | -14.78325 | -59.42914 | 2024-10-03 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77684634-3f34-362f-9223-11bffff86e0e | -14.77652 | -59.42807 | 2024-10-03 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f9147da-9beb-3ffa-9dba-3c97da3a2897 | -14.77315 | -59.42754 | 2024-10-03 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a2c3338-e38f-339f-b7c3-62e2cb94f668 | -13.77176 | -60.07092 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ed9f05-2f80-3b64-b10b-5637dec18a16 | -13.77121 | -60.07446 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbc2a2ca-2043-306f-8803-c494f430dafb | -13.76844 | -60.07038 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README180.md)
