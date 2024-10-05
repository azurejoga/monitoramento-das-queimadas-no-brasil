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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8adefbe3-8d6e-388e-8b38-31f2111d6f23 | -11.89776 | -56.94177 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f2ce4ed-2e47-3042-8d21-0874148440fe | -11.89716 | -56.94619 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c56a851-0066-3b6e-8e46-d151aba39c2e | -11.89655 | -56.95058 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3491a047-73b1-302d-a33c-ba879e8d35d2 | -11.89596 | -56.95498 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f419fc42-f668-3ade-9865-c606dcf5c8af | -11.89537 | -56.95932 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 08cca6a3-ff9d-34c7-91c7-7be3ec6f0993 | -11.89396 | -56.93672 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f169dce1-4ff3-348b-b004-d0cd296571c6 | -11.89336 | -56.94113 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58d6b44f-3113-3619-90a1-84e8ad75f38e | -11.89276 | -56.94554 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b51f5481-c794-3799-9512-40fa1db8ebb8 | -11.89216 | -56.94994 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 575fa6c5-3207-3e49-9f60-07cb1ba5208c | -11.89157 | -56.95433 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 20a99032-11f2-329a-849f-cb4e706ebb0b | -11.89098 | -56.95866 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4f262ea3-7e5f-35bc-9719-d7be0bface26 | -11.88956 | -56.93608 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a538d16c-4538-3a19-b34a-547d4a545fb1 | -11.88897 | -56.94047 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60f3f0c8-5c11-388e-a244-9276347dfa91 | -11.88837 | -56.94487 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 908a6313-5d89-33f2-ac91-c1813d459e60 | -11.88717 | -56.95367 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6fd757d0-f318-398c-b012-34dbd91f8bfd | -11.88659 | -56.958 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b902adba-b105-3deb-9035-ff4aaa10f7ec | -11.88337 | -56.94867 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 107d929e-c6e5-3551-b0eb-2da8357a5245 | -11.88278 | -56.95303 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7449a38a-1fcd-3347-9268-4b24bacee2da | -11.82415 | -56.58845 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25ce0d17-c44d-38e1-9131-fe4047859043 | -11.82353 | -56.59306 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d916a87d-50b9-35ae-aa0f-f0aebd15708b | -11.82291 | -56.59765 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27bbd6a9-f454-347f-9378-c507073d4fcd | -11.8223 | -56.60223 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e0d3e3-434a-3687-b179-ab0f7277276e | -11.82169 | -56.60678 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c97a563d-e422-3186-9a4d-5883c0fea7a5 | -11.81842 | -56.597 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 655e8520-255c-34e5-bc95-18673adfc990 | -11.8178 | -56.60157 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0896af17-4e50-37b6-80ab-bb22cc7ed5ef | -11.81719 | -56.60614 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b626eeee-a41e-3911-b0c7-d101b653ba04 | -11.81331 | -56.60091 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eff074d-73f6-3195-9483-4ba5140dd2c2 | -11.8127 | -56.60548 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9d350c4-1f2c-32d2-a9de-adb89e884eca | -11.4912 | -56.795 | 2024-10-05 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50047889-00f1-308d-8db9-369c785b7854 | -11.49059 | -56.79943 | 2024-10-05 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade8e875-d9e8-3174-8b95-c9d297b744c7 | -11.49045 | -56.797 | 2024-10-05 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed288138-f147-3992-931c-aaf25623707c | -11.92003 | -56.94241 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0f81f44-dc92-32ee-9e39-f25894f3f3c8 | -11.91947 | -56.94678 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e415e739-26c7-39bb-9936-b577fec97f4f | -11.91677 | -56.93303 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 367f80df-72fd-30a6-8572-24592e01e9fa | -11.91656 | -56.93547 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 53ee3293-93ab-3ad2-af1b-d2b443c4a0f1 | -11.91619 | -56.93745 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f578f629-c9cc-33e8-adb1-77263d2e1645 | -11.91596 | -56.93986 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e189c29f-d2a7-38e2-ac62-d5a8e621443b | -11.91563 | -56.94183 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c1c5688a-c76a-3aff-8b3b-71d679fb84f0 | -11.91536 | -56.94422 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42b0d292-b544-3f49-9d55-29f908867781 | -11.91506 | -56.94621 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41c8cd11-ac8f-3372-a1d0-b1df5f89abb4 | -11.91236 | -56.9324 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 039f8fbb-410b-3190-89de-84b1bffe3b91 | -11.91216 | -56.93485 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c5f17d11-c206-37e0-a809-a23fe85bf527 | -11.91179 | -56.93682 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e282389-1d5b-304d-a9a9-c6737f6bd76e | -11.91156 | -56.93925 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc0b26cc-5f5f-3612-8654-87e3b0c0991e | -11.91122 | -56.94122 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b19720f2-bb9e-309a-8d07-b16686bb8b7f | -11.91096 | -56.94363 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e6668f9-d259-3f75-8ab5-9b00212312be | -11.91065 | -56.94561 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f426e8d9-ecbb-3c8c-805e-da80fc32f78a | -11.91036 | -56.94802 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2dd4ce0e-2774-35c1-b4a9-cfd0f717d1ee | -15.56549 | -57.45646 | 2024-10-05 05:31:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d24e1a9f-dd79-3850-a834-f4c922892722 | -15.52387 | -56.89223 | 2024-10-05 05:31:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b922dcfa-d98f-33dd-b75b-83e4b36ffcb9 | -16.59916 | -57.25572 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 84a637e6-485d-369b-a292-c2eb22a4b876 | -16.59906 | -57.25217 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b7d1d590-b37e-3863-b22b-f0cdc4cdd494 | -16.59849 | -57.25706 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 00fd430d-c5f3-35d9-8ecd-3be00bd05bb6 | -16.59394 | -57.26 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 78f9cca0-017b-37e6-926e-80b76396297a | -16.59331 | -57.26134 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a8bb2d6c-e2ea-3267-aa93-c5854d05ffad | -16.57321 | -57.16164 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b9ebf87c-6e65-3a3b-847e-a9c51a3dc353 | -16.57261 | -57.16658 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f1689d4e-2daa-3d33-b850-90bb5344b705 | -16.572 | -57.17155 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ef715a16-06d8-37d8-a82c-87cc64194752 | -16.56737 | -57.17091 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 79d3b36f-5760-39c1-b844-6c0265b5b66c | -16.54749 | -57.21861 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3e51aa6f-b4c5-3d95-bc91-dc5796467aa0 | -16.51509 | -57.25438 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cf8e0699-de25-3a6f-9c14-68527026659e | -16.51451 | -57.25923 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b893a5ad-28e7-36f3-9aff-a7258acdb910 | -16.51393 | -57.26408 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 48b4ff89-5ddb-3328-a90e-f5ae70ad0cb2 | -16.51048 | -57.2538 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a0a49264-91b2-32b2-bdc9-cc347899eaab | -16.50991 | -57.25862 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c385009a-e02b-35c4-b852-03f4bd866b30 | -16.49162 | -57.29374 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 87743cbe-84cf-387f-9c48-8cfcc320c92f | -16.47772 | -57.294 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 000b6836-27a5-3401-bdff-5891b5051e03 | -16.46012 | -57.28452 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d01512b4-648a-3927-b37d-7c7fd20d31a5 | -16.45094 | -57.28327 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 37ca994e-7eee-3cb1-b80e-16ea95100cfd | -16.42256 | -57.36306 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a6eef4e9-dd30-3331-9bb6-86c865c8f972 | -16.41917 | -57.35283 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| cea4648f-f6e4-33fd-ab55-d18cfef1884e | -16.41858 | -57.35764 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a28e5fab-246f-3e80-b770-31503582f76a | -16.418 | -57.36244 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ddf49ebb-b2f1-35d4-8fc1-66dbdd827b26 | -16.4146 | -57.35222 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 016c550e-ca00-3cb8-8077-a87f9ab7bee1 | -16.41402 | -57.35703 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6a204e0e-0ba7-3977-8776-e984e0f5505d | -16.41343 | -57.36183 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 409cc5cf-cdb8-3d41-98ab-e32becc6ef51 | -16.40945 | -57.35643 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 48bd00b8-0e96-3823-a98b-7d7bf1c42e98 | -16.40887 | -57.36122 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 27ec7357-0960-3249-afa0-63841f8ab4a5 | -16.40489 | -57.35582 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fcb25a71-0417-390f-8a54-499c5ebd7115 | -16.07112 | -57.52782 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1651f089-35c1-3332-9016-34f203e80af9 | -16.07058 | -57.53213 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0595d6b2-8c38-3381-9034-b9ff53cd5ab7 | -15.73378 | -57.42649 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc4e4e8b-df64-31d1-a542-df99b7ae796b | -15.72984 | -57.42134 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6fb070f7-4295-3616-8222-96568eea4f1f | -15.72927 | -57.42601 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e052cd5-ca60-3c3a-ac22-be648ed43921 | -15.728 | -57.41972 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c2d5f0a8-db96-3d6a-9a21-16fa6b9a066b | -15.72741 | -57.42434 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d1df039a-ab97-3a2a-a156-3e08f8160d7c | -15.72681 | -57.42895 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 898eff8d-6b15-3bad-b401-10f1872d0dbb | -15.72589 | -57.41613 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e3e7c229-5a98-325c-9981-de11625c6c47 | -15.7253 | -57.42107 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd91aca2-f76d-3969-87db-2dea33ecdca7 | -15.72419 | -57.43014 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2ec7bf4-a090-3157-be02-2428e459464d | -15.72411 | -57.41434 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99e625ee-3da1-3c45-935e-d0776cab53ca | -15.72229 | -57.42852 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4920f5a-0294-3571-8d5c-ca18a87b64f8 | -15.72022 | -57.42522 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69af1ab4-cf41-3622-a0d4-7425eb7028b7 | -15.71959 | -57.41391 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3748233-d688-3825-9c0e-9cc51a83e459 | -15.71834 | -57.42361 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c070c54-9960-3bed-b301-2c90f80f9ef2 | -15.71778 | -57.42797 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| afea0f35-69fb-3bf5-aecd-676020a912b7 | -15.71722 | -57.43239 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1111095f-ede3-34fd-9946-143a2430fbe8 | -15.71572 | -57.42463 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| af973af9-f9f4-377e-b292-fae1f0f9ca26 | -15.7157 | -57.40852 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc002837-ae02-3f64-b4f9-e990a31fac31 | -15.71519 | -57.429 | 2024-10-05 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README140.md)
