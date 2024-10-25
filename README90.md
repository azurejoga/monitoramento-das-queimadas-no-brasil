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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 939fa78d-8536-37e8-8087-a63d6a88ca15 | -3.89313 | -52.31514 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f774eb70-fbe2-37b3-ad38-92462a6bf7e6 | -3.8886 | -52.36802 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d25035e-54a0-3c6d-a976-7e0e2c47f1f7 | -3.88042 | -52.35027 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3b9865b-c49f-3b06-942f-18851143a35f | -3.87749 | -52.34569 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df9ee05a-3f16-39ff-abdd-e821bd78e29e | -3.81337 | -52.692 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac999950-962a-3d1b-9a3a-43b2c79d6cef | -3.80987 | -52.69148 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d261c105-c5fa-3797-9f95-2d2b138dfbf3 | -3.79605 | -52.28882 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e822d74-ca5c-378d-8a60-af8f1f903b07 | -3.78753 | -52.39068 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29a3982b-15a4-3e62-a74d-67c157a4484c | -3.78739 | -52.41494 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a07e2f2-c626-3b4e-95c6-d496f7989a62 | -3.78461 | -52.38608 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15247ec3-d579-3bb9-85b5-e841a4408186 | -3.77325 | -52.31846 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a57796d-eb71-3a6c-8cc1-2a4caa62e01c | -3.75506 | -53.40812 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c1f14bb-88ad-38e8-8db9-0c872d169135 | -3.75166 | -53.40758 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 587f2651-1738-3416-ac48-f1e730315e13 | -3.73663 | -53.73548 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6df818f3-b27c-3950-95ed-831f9f158dde | -3.71128 | -53.70946 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14dfad01-4824-3eb0-a994-2e19c633f965 | -3.6893 | -53.42799 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64921b3c-8d48-30fd-ae77-d5a83533f67c | -3.6859 | -53.42748 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d8aa642-9393-379e-9f12-d51bf5d87dea | -3.5614 | -53.75294 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb40cffb-9129-3695-9d4b-53230b0464ac | -5.69988 | -53.4538 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a69b47b0-c5ec-34fb-b7bb-d63c22feff26 | -5.69929 | -53.45761 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84327e63-cd8f-3365-b175-e5660580f19a | -5.69869 | -53.46143 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 785839c5-e76c-324b-9add-b1e9427341f7 | -2.15193 | -53.64207 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 545e753b-bd5f-3878-acba-be97d2c8ee32 | -2.14414 | -53.64808 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb86938f-16ff-3505-922c-ccba25f29abf | -2.14359 | -53.6516 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fed86297-000c-3bf0-a53e-02d12964fb20 | -2.07594 | -53.56519 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937d2d3a-c6a4-3f84-a211-2c0b0087f489 | -2.0737 | -53.55759 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5296d5a0-0c16-31fa-bd18-7ea5b09f0e5d | -1.95416 | -54.03782 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a88c04b8-61d9-395e-8757-6929989a3889 | -1.8965 | -54.62175 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef50938d-10cb-3f75-979e-8ae19c172976 | -1.89319 | -54.62124 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdbaa2cc-c455-3242-9e84-7485b7bb3f8a | -1.69466 | -54.26336 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f26d79c-1a07-3141-9a41-2e589bc16d3c | -1.60781 | -54.77369 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e65182b-2f1a-3939-86a9-1ca01f411324 | -1.3524 | -54.64527 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e45b062-9a3a-3190-a3fc-e6969c5d54d4 | -1.35186 | -54.6487 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77c5153a-3b6e-3a6c-856c-7b96de762b5f | -1.34856 | -54.64819 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dad713d6-ff74-30a6-8774-b47a01c905a0 | -1.21189 | -54.19838 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4803da7d-bad4-365b-8860-e28417bdc3ca | -1.18687 | -54.12053 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41edf56f-5dfe-3bfd-9f5c-e3d7afc23f2f | -1.18394 | -53.90096 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad5f5fb-0c25-368b-8747-2f47a9e818e0 | -1.18353 | -53.6659 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 91c56d35-3537-3aaa-954f-7260c1a21d7c | -1.18339 | -53.90443 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9853ff8-a0ae-3d28-a20a-47a88d5bf0ff | -1.18243 | -53.67289 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8ec5d68d-8d27-31fb-b759-f104df02fe72 | -1.18075 | -53.66187 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 838a555c-c852-3b6d-8641-76058afdf073 | -1.1802 | -53.66537 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fb9ecac1-8d5c-390b-9af7-26e9a410f101 | -1.17911 | -53.67234 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8b02fb4b-7ac7-352f-8b77-4f3c7924e1d2 | -1.17688 | -53.66483 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e83c8b82-40d6-3e6a-96cd-3ba6bd2392f8 | -1.16312 | -54.0992 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32118685-4505-3afc-8c81-ea8252264ef1 | -1.16257 | -54.10266 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f21ef088-ee52-39f8-9784-c10279f1c10c | -1.13397 | -53.7865 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 373c5a9a-d383-3114-8684-84a734428a0b | -1.13195 | -53.64701 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1d3e606-63c3-39a5-8cba-d9fa4b1d6215 | -1.12872 | -53.68953 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce30c8ee-b3eb-30ba-b357-df908a05d4e9 | -1.11003 | -53.61481 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d73d7f-a8b0-366f-94dc-6caa0ba20e6a | -1.08534 | -54.13998 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b3ba33-ba3a-36bd-9084-d95dd2572bca | -1.07624 | -53.65617 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 582d6e1e-a46c-3f10-bc36-9fad20cb940d | -1.0746 | -53.66662 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c5ddf8b-ca0d-3790-9a26-0ea4bccde339 | -1.07236 | -53.65914 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4200d291-754f-33cc-bc53-e92bfc777624 | -1.07072 | -53.66958 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42ae6ca2-40da-3998-a448-3701246bcecf | -1.06849 | -53.66213 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dab708a8-3b72-3912-9011-b015c790fd79 | -1.06239 | -53.6576 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d25196c-d1b4-3901-a18d-69c140a44356 | -0.87409 | -53.68867 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8efa6ae-3a48-3f61-88a6-1f46645bb1f3 | -1.76723 | -53.99499 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d05fd9df-d147-3926-9808-d3bcd3464929 | -1.61058 | -54.77764 | 2024-10-25 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad06dec4-c282-35c5-b828-d0d98a0d35f8 | -1.30055 | -54.21905 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e5a9850-0827-3e99-8b95-7458288cf649 | -1.21519 | -54.19892 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451586bb-cb31-3db5-94f3-e8315004d74b | -1.18725 | -53.90148 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1bcddb4-8d8f-3cea-aeeb-3eb8d0dafc40 | -1.18298 | -53.6694 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 80818926-e75d-3968-ac0a-b1719d86cc04 | -1.17966 | -53.66886 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| af0af3e2-0ef3-32e9-b04e-db87618052b7 | -1.16437 | -53.5049 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 815ff341-08ed-3396-bce9-4eafee40ceb8 | -1.16366 | -54.09573 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ccbd30-22f2-364d-b1c3-12ad5b13e5de | -1.16078 | -53.65881 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 019be45f-ac36-38ac-9845-032287034830 | -1.14197 | -54.1029 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c65c94bb-ced6-3d0a-a2cf-7c9286fdcbec | -1.14039 | -54.13442 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3faf3f42-6940-303f-bb47-3c0164ac7890 | -1.13866 | -54.10239 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38b26555-1393-33d0-89ff-1b2e8a8bad24 | -1.13812 | -54.10583 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad0ffecf-98ce-37d1-a8f6-97f3f3d696d1 | -1.12046 | -53.44016 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97ed787c-d684-340d-a1fd-ca5c25b77d5a | -1.11041 | -53.41693 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70f767a0-30eb-34b8-8d83-83810fc7c411 | -1.10706 | -53.41643 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e7fe2f1-cf6b-3ff0-9c83-df09541a9aa2 | -1.10651 | -53.41996 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a157d6d7-c08a-341a-b91c-7b6d85f6c000 | -1.08304 | -54.11145 | 2024-10-25 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7bbb05e-aed7-3917-a799-69e34e335fef | -1.07679 | -53.65267 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88932966-8502-3d53-8365-98e19db9e2d8 | -1.07405 | -53.67008 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8a1f239-fab3-3bbf-9a3a-309f8f145f79 | -1.07181 | -53.66265 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17427915-9ded-3bbf-ba5a-44d6a6882892 | -1.07127 | -53.66612 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ccae712-e425-3560-b034-88487c19c1f3 | -1.06904 | -53.65862 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95e0806d-e318-3b83-bcda-7f2364295dc7 | -1.06794 | -53.6656 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62f80759-a1ac-3fd3-bdba-4bcdc557a84b | -1.0674 | -53.66907 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf471e89-eaff-3e8c-9b1b-a3c61e82af16 | -1.72278 | -53.51831 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e444594-effe-3f79-8616-ff6898f4d998 | -1.57411 | -53.49525 | 2024-10-25 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2df430c-170a-350b-9102-0800e0834fc9 | -3.58549 | -54.66399 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db89e4f-8b03-3847-ba9b-f92ffe7192b5 | -3.57765 | -54.6274 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 910fff77-1211-326e-9dfe-2b22157389ee | -3.57711 | -54.63085 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9b56ac2-2e5d-3037-9b6f-682fe7756e6f | -3.57343 | -54.5875 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef326dd2-62f0-3225-8b2b-ac785bcec232 | -3.57289 | -54.59095 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce0e660-ad53-32ac-89d7-c2889b424f7f | -3.57012 | -54.58698 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd914516-83a3-3af3-b17f-bc5d6e090fb6 | -3.56958 | -54.59044 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da5fb030-3d34-3fc0-830d-6a2918b33971 | -3.56048 | -54.759 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d3c1fcb-2a75-3846-9308-8eaa0b3ef13f | -3.55717 | -54.75849 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf08e87c-b4d2-3b9f-ab60-cfd3ec9ba229 | -3.54243 | -54.74172 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c642f65-c00e-3e1e-8d32-cc96e46a2ed3 | -3.53913 | -54.74121 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed370264-d21f-3961-bda3-8ce996d7bb68 | -3.50202 | -54.67544 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34254235-fdbf-362a-9e11-4ea79468d252 | -3.45431 | -54.63263 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11e8660a-da76-371b-ba25-8e8e6d632297 | -3.44715 | -54.63506 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README91.md)
