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
| 8ca74dfd-8568-3310-9057-060a68316091 | 3.59405 | -60.94045 | 2025-01-14 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d84e4bc-d17c-3f27-ae50-c00fd0e0ff87 | 3.91069 | -60.84255 | 2025-01-14 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c99acf2-d31d-32e6-afdc-40774a9e3ddb | 1.3217 | -60.4262 | 2025-01-14 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e450c809-78f1-3136-b626-fe5c34d8b9fb | 1.3221 | -60.0463 | 2025-01-14 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8e3bb279-ba37-3215-bd34-f2b6e0ac9867 | 1.3221 | -60.0272 | 2025-01-14 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 20dd32b2-c8b9-3fdd-afc4-8f8069501f14 | 1.32302 | -60.03897 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3abd4604-19ed-31c0-a8c7-05511d01212f | 1.32107 | -60.02702 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcae4e32-6954-3774-86e8-4fa76b002af0 | 1.32254 | -60.036 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1746acac-c42e-3d29-aeed-d78075be6280 | 1.31691 | -60.03374 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a6489bc7-2f3e-32ac-a91c-296c7244eb3c | 1.32817 | -60.0383 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 17e9bcd2-7a9f-3254-98cf-349a7572db45 | 1.32399 | -60.0449 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3fedf85c-eef0-3931-bf61-5d09793c1c50 | 1.31643 | -60.03077 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e306c8a-60bd-3460-b5fd-7cf0ce9c1983 | 1.18232 | -60.4929 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d6f7948-9d5b-3d4a-9c64-fde8050ec321 | 1.3147 | -60.42444 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d025be58-1552-3fd7-bfb3-46ec7a6b8634 | 1.31968 | -60.42359 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38f01157-550a-3dc8-b4e4-7bfc64d146c8 | 1.32718 | -60.03227 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b80fe817-fe7e-302d-b61d-708021e5c665 | 2.18692 | -61.80906 | 2025-01-14 06:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef06c57-65c4-3b6e-862f-31f192ce1bab | 1.18141 | -60.48729 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39c3a23a-afb1-3984-95c0-16d245b4abce | 1.3156 | -60.43006 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f451a027-8c0f-3400-9ce9-615cdecc4314 | 1.32157 | -60.03006 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70d39611-3690-3227-8766-1926adedaa9c | 1.32205 | -60.03302 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 527f0b04-e460-3dbe-82e0-58302beec04b | 1.17825 | -60.49929 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26009ad-76e5-3e88-b758-b371ecf6c319 | 1.32768 | -60.03529 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8f28cefa-5c7b-39a9-a7cd-8790a19821d1 | 1.11588 | -59.45783 | 2025-01-14 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54fc34a4-d97d-32e3-bc11-b00d6080c070 | 1.17734 | -60.49369 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02f9c4a0-6960-3c41-9f83-6d8bb9d0ca76 | 1.32669 | -60.02924 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91827fa3-803c-31ed-ad78-74834db7b4fa | 1.17328 | -60.5001 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4301cab7-3ef7-3187-a5e0-d25f4b70090b | 1.32864 | -60.04124 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 56f56eb4-770c-3eef-a908-2894f0904af8 | 1.31837 | -60.04268 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ad1b2101-2c45-3425-a606-2a68397e5175 | 1.38493 | -60.80069 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7da2fbae-8fda-3d6b-bf56-dc7a62963499 | 1.3174 | -60.03673 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d6d3f78-1baf-3f5d-a694-c332a17f32f1 | 1.93616 | -60.40964 | 2025-01-14 06:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ccf1ea0-2aab-3909-ba1c-221f14ab2da7 | 1.32351 | -60.04196 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6179f743-e850-3cc8-a203-627a2ae4f599 | 1.31789 | -60.03971 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4bbb2b39-502c-3e47-87de-ea5736078c37 | 1.32912 | -60.04418 | 2025-01-14 06:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2941696-84b3-3c2b-ba85-7be88dcea8c6 | 1.9024 | -60.57182 | 2025-01-14 06:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa3d88f-e4d6-3ec5-a24b-1ffd2aa2c35e | 2.18246 | -61.80981 | 2025-01-14 06:01:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91be74a1-3f38-3f29-bcaf-392c383a29f0 | 1.3221 | -60.0272 | 2025-01-14 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 18106557-2a2c-3a29-8d60-7eb592e5173c | 1.3217 | -60.4262 | 2025-01-14 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 02a3c752-05b2-33d9-a593-1f40ef0b41af | 1.3221 | -60.0463 | 2025-01-14 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5ca5da7b-987b-3317-8f82-ac903da0e9d2 | 1.3403 | -60.0271 | 2025-01-14 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| eef67152-6f99-325b-a0db-047f97aab3e2 | 1.3221 | -60.0272 | 2025-01-14 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c470b7e1-438c-3ec9-8083-b4670ef3661e | 1.3221 | -60.0463 | 2025-01-14 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6cf43099-12d8-3f49-9225-8471654d0fff | 3.60338 | -60.94433 | 2025-01-14 06:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc7e6a44-37a4-3632-a014-dd6583c2ed55 | 3.59648 | -60.9454 | 2025-01-14 06:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c9343f-4029-3630-963a-71261ec5b6c2 | 2.43223 | -60.65189 | 2025-01-14 06:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 557be8a0-4db7-35e8-a7fd-5b47ff18f645 | 2.42759 | -60.64693 | 2025-01-14 06:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 848c1060-995a-345d-91bf-b306e94f4d36 | 2.20203 | -61.80644 | 2025-01-14 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eabd04f5-d7a2-34af-98fc-d6cd1f301f0f | 3.60441 | -60.95027 | 2025-01-14 06:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7388fadc-8248-3b71-b1c8-0bdddb8fd75e | 2.1954 | -61.80788 | 2025-01-14 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 053fb935-5ace-3c48-a59e-9b1eb33872be | 2.42874 | -60.65382 | 2025-01-14 06:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a953251-8afc-30c4-8998-97db26bb97e4 | 1.3221 | -60.0272 | 2025-01-14 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e5b5683e-24ff-3fd4-968e-64b45d318ecc | 1.3221 | -60.0463 | 2025-01-14 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 714f879d-a550-31ee-af02-5bc6f21dd3fb | 1.32508 | -60.02413 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 33327680-49a1-3b57-b328-63721fe73dc3 | 1.32055 | -60.42656 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| a169c862-ce79-3fb0-9183-585ede763fd3 | 1.18177 | -60.48742 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a1195bf5-e175-3153-a8f8-8fa7905f53b0 | 2.95576 | -60.17876 | 2025-01-14 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e0a927a2-525c-3880-85ac-56807e3da880 | 2.94539 | -60.17096 | 2025-01-14 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f2186e2c-4b7d-36fd-a378-6d7deee22656 | 1.3265 | -60.03368 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 02fe86a6-5cba-32e8-8bee-4172edaff2d2 | 1.31733 | -60.03498 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1a53fee3-8853-34a9-8373-f0da978f5ea6 | 2.43403 | -60.64945 | 2025-01-14 06:35:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1656c09d-e483-32df-9ea3-c8fd5cfa7221 | 1.31915 | -60.41736 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d4f67288-0193-3620-b85a-4887676b2eee | 3.60739 | -60.9399 | 2025-01-14 06:35:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f55e477-ea60-33a2-9759-6d60bf368ebe | 1.33567 | -60.03239 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 915c57f5-4c9a-3b5d-add5-d5453d7a3915 | 2.94679 | -60.18011 | 2025-01-14 06:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 36.6 |
| c869544f-d510-3c1e-bf07-c9b7108f57fb | 1.18315 | -60.4966 | 2025-01-14 06:35:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1c16d9f6-8802-3e4a-b218-6f5fe8b74249 | 2.43269 | -60.6405 | 2025-01-14 06:35:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d6aa153a-3323-398c-893a-8b08f1211b9d | 1.3217 | -60.4262 | 2025-01-14 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 7aaf4b22-fedd-35f8-9318-1cde372d2f01 | 1.3221 | -60.0463 | 2025-01-14 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 21a5e6e7-035e-3a8a-9b15-6b5fe412cdb1 | 1.3221 | -60.0272 | 2025-01-14 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 37339f23-7ada-3423-a7b0-4a79df9c61d2 | 1.3034 | -60.4263 | 2025-01-14 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 2544d369-cf66-391a-b412-de64f1efa202 | 1.3221 | -60.0463 | 2025-01-14 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| edede2a3-4f04-3e3b-9f01-a4f4a3089987 | 1.3221 | -60.0272 | 2025-01-14 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a12dac3d-b7d3-39a3-ad02-be0f86e53335 | 1.3403 | -60.0461 | 2025-01-14 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4c4406a2-f409-3e3e-b46e-938d69c95103 | 1.3403 | -60.0271 | 2025-01-14 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f517121b-d148-36fa-8074-4af3f157c548 | 1.3217 | -60.4262 | 2025-01-14 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c637d98e-b4c7-388b-8c3c-2c95bcbbce39 | 1.3221 | -60.0272 | 2025-01-14 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4436760d-6eea-3ee2-a744-a30d40554a41 | 1.3403 | -60.0271 | 2025-01-14 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 84a42132-813a-3c54-80d2-d1dc32964def | 1.3039 | -60.0274 | 2025-01-14 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| be571273-b007-3625-b9b5-f2965b780e01 | 1.3221 | -60.0463 | 2025-01-14 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| bf44d44a-6368-3ebe-8b91-33d74fc57d6b | 1.3403 | -60.0461 | 2025-01-14 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e7ee29ec-36a9-3177-9f3f-ff71d5f61317 | 1.3403 | -60.0271 | 2025-01-14 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1354952f-9f8b-334f-b8e3-de502a985910 | 1.3403 | -60.0461 | 2025-01-14 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 83b7cda9-7174-31ed-a5e2-1bda0b6234d0 | 1.3221 | -60.0463 | 2025-01-14 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.0 |
| b2c8cd75-2d54-358f-b149-2adc03ab045b | 1.3221 | -60.0272 | 2025-01-14 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 50f26b61-7f15-3eae-bd98-561f9a29a39b | 1.3221 | -60.0463 | 2025-01-14 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 2c9a815a-9ba1-3617-a026-59b999cf1ae0 | 1.3221 | -60.0272 | 2025-01-14 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| f2960919-7dea-3d35-b329-cb92923353b7 | 1.3221 | -60.0272 | 2025-01-14 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 899901ee-ecc8-3824-8a0a-1a47329be798 | 1.3221 | -60.0463 | 2025-01-14 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 872d4d4a-7997-3fc7-a2cc-0ec313773056 | 1.3221 | -60.0272 | 2025-01-14 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7757072c-40af-3c7a-9710-a2e58c418de0 | 1.3221 | -60.0463 | 2025-01-14 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 88513d19-f66b-3252-8b74-66cb93eec807 | 1.3221 | -60.0463 | 2025-01-14 08:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 60781898-ab2b-3fab-8ebe-1363be4da8cb | 1.3221 | -60.0272 | 2025-01-14 08:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| af847d8a-7d04-300e-bdcb-e8e9be116cdd | 1.3221 | -60.0463 | 2025-01-14 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a8672991-587b-372f-8884-b6fd4749d351 | 1.3221 | -60.0272 | 2025-01-14 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b22fe6a3-68b7-3ca1-9a86-bcfee44867c0 | 1.3403 | -60.0461 | 2025-01-14 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8429154a-7a18-3ca8-8cf9-d14be2cff001 | 1.3221 | -60.0463 | 2025-01-14 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 12a8e069-4498-3fd2-a951-3dccbb97e922 | 1.3221 | -60.0272 | 2025-01-14 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 475a6f13-9650-36fa-841b-8f3138d9f734 | 1.3221 | -60.0463 | 2025-01-14 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 683c4bb8-5b65-3761-bbff-3e5acda7b6ba | 1.3221 | -60.0272 | 2025-01-14 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |


[Clique aqui para ver as próximas entradas](README8.md)
