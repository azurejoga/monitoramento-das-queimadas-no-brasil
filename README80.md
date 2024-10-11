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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d3de3a-5914-30bf-bf45-fe8d7929509f | -2.65398 | -53.35156 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 151fb4ee-d27b-35fd-861f-9e5cb23f498e | -2.2532 | -53.478 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cfcc198-ceb0-3e2f-a753-b8d9196ff45e | -2.25245 | -53.48296 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07d2b6c2-ef83-31c5-ae41-1f58ca1fc4b5 | -2.2493 | -53.47739 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60f44c4d-864f-35dc-87bc-c444f4b7124c | -2.24856 | -53.48235 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f82cf1-7f27-34f8-a8f3-ef5b9e7f1868 | -2.24805 | -53.4799 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9949a4-7b96-338f-bafe-e71b5c4f2505 | -4.2721 | -53.69475 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb5ee4fc-b304-3512-8273-a22db358ad3d | -4.12448 | -53.47568 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a4ab3b-9f6c-3fcb-9338-4871c2b22bf6 | -4.12048 | -53.47504 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa68a71a-4c92-3865-b109-604becaba6e5 | -4.11944 | -53.48202 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c87b19c8-39e9-3084-a040-85b2b1bdf020 | -3.98383 | -53.43312 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 107a9122-cb2f-3ca7-bb53-fcf769bf5472 | -3.9816 | -53.43304 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81920a80-aa30-3c2b-b955-88017246da27 | -3.97982 | -53.43251 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9238c847-1a7a-3052-9e1d-041f126ca074 | -3.91045 | -53.56641 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a49a4a6-02de-3e9a-8c41-957c83cf3cef | -3.88897 | -53.62843 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bfba9a0-dc33-319c-9f12-19cadedfd2da | -3.83223 | -53.58176 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad6a4283-7ca4-3f0e-a113-7f21c75efd0d | -3.83144 | -53.58691 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d86af5e-41b9-3861-addf-76b56e26d252 | -3.65114 | -53.55256 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728ec590-398e-39d3-a878-4a577d548ca5 | -3.835 | -52.33179 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae77a159-31cc-38c1-ab89-f22998992fc7 | -3.72629 | -52.36678 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0725df47-51cd-33df-bdf5-d975261da5a7 | -1.59345 | -53.34654 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9166b4cf-ace7-3b50-b1d9-79d87b309d12 | -1.58956 | -53.34596 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 116c4b09-6fde-3918-8bc8-b0af775ccc14 | -1.17837 | -53.38628 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6089a1a8-eb54-31a0-bbb0-816c4b59b910 | -1.17764 | -53.3911 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0e377f9-b6f6-36ec-a99d-741388e0cc0d | -1.17675 | -53.38446 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb445c5b-3b92-3235-a76c-bbc26df9dc9b | -1.17618 | -53.40073 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 630fe9e1-807a-39de-b653-84d7ec11036f | -1.17599 | -53.38927 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a208955-edba-35a6-b3a7-33b23309e73b | -1.17545 | -53.40553 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f3c8564-eb92-324b-ae2f-7ebb10a34a24 | -1.17446 | -53.39886 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b91ef06-1f27-3806-af73-644d70a42220 | -1.1737 | -53.40365 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee8ebf47-0e08-3ab8-9244-0df9d58d571e | -1.17304 | -53.39537 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd08bad9-8453-348d-9a71-7fb6bb81fe21 | -1.17231 | -53.40016 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a4ed043-bc4e-36ec-ad35-03b9bdbeddfd | -1.17159 | -53.40495 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c8b09f7-f11f-3b7c-942a-860725d7bace | -1.16845 | -53.39958 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c627e822-431c-363e-b257-95e209142d6f | -1.16674 | -53.39773 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2b51651-b48e-39cb-ba40-deb356f6d223 | -1.16598 | -53.4025 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa9139d8-7486-3095-93f9-93ea63dae813 | -1.16459 | -53.399 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36da2be4-91c7-35d4-b759-04711bb6aa4f | -1.16387 | -53.40379 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 49b4975c-062b-3ce2-953e-b81b4f95a474 | -1.16288 | -53.39714 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d35353b9-a1aa-38e7-be1e-104f9d66d5bc | -1.16212 | -53.40192 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d9d1a57-491e-3b90-a48d-f4db3bece09f | -1.16137 | -53.4067 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99b6a44f-45f0-3e63-8fbd-52212ca5e61f | -1.16073 | -53.39841 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d62f49c6-92a7-3122-8209-73a1f1affd5b | -1.16 | -53.40322 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 387cbf64-4667-3883-900d-3e9e9aba1565 | -1.15902 | -53.39655 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39c676cf-0953-3278-b344-e9a385639cee | -1.15516 | -53.39595 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e00ac690-1818-3b3c-832e-ff3f54f237f3 | -1.12764 | -53.44561 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7029d736-39d9-3c92-a243-a143c243bfa9 | -1.12453 | -53.4403 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21256c6e-e69b-373a-a565-e47b88a0e0ea | -1.1238 | -53.44503 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce184550-4704-3715-8956-20f8ac5050ab | -1.12305 | -53.44981 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0432a7bb-370f-3560-bf84-8e79c107c9ef | -2.10801 | -54.634 | 2024-10-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae995216-5e43-3334-b761-6a0d24f65c19 | -2.10437 | -54.63344 | 2024-10-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d24cbec-2ad8-365a-8ff5-44d7589d3fc1 | -1.99066 | -54.0836 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba4a3d5d-e5a2-3617-8ec7-1f084a39ede1 | -1.70778 | -54.3861 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 156b4bc6-930d-39ce-a454-9eca98e89ed9 | -1.57027 | -54.76308 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 713d6981-42ef-3aa1-8971-b92de37719b4 | -1.37487 | -54.7857 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc353b9-83a6-3361-bd0d-eff88539935c | -1.31593 | -54.6689 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645dcf21-efb7-3fbc-8350-3ab0f4d101f3 | -1.25676 | -54.6821 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d795693c-da8f-3824-b0ea-c050f14fbfae | -1.25614 | -54.68609 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7075c38-79af-3aa0-a30a-ba03d95b2a66 | -1.2128 | -54.52758 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c784b187-15a5-39c8-a9f1-50861ba577d7 | -1.19745 | -54.22048 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef9b5e5-58a6-3603-a173-f5787cc7aeb8 | -1.1968 | -54.17595 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f73a87-2a3f-3657-bdec-4b690a4bacb8 | -1.19613 | -54.18029 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16dee234-550a-3e4a-bcdf-cf35bbf7f2e0 | -1.19577 | -54.10905 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6171f55b-a277-356b-952a-eb54868dd7c1 | -1.19271 | -54.10429 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b060ca8c-e434-3068-8e62-37004918d2a2 | -1.19206 | -54.10857 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 065646f1-b8b6-3af9-9343-aec1ef9db8f7 | -1.15664 | -53.78278 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b65b04-b1e4-31d9-b121-84962d7753ab | -1.13899 | -54.21267 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28769f76-b324-311c-b3bd-6a94aa18ce5c | -1.1383 | -54.21702 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af101e6e-09d2-350f-8418-5ad1fabbc3eb | -1.13035 | -53.65101 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1015e947-858a-3e85-ab14-e11f0084cead | -1.12921 | -53.63465 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80868b5d-3f8b-35c5-b579-6941f01dc076 | -1.12868 | -53.63642 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d58569a7-81e8-386f-b003-1e6483423abc | -1.12847 | -53.63933 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c5524a8-70bf-3688-9536-65750ae550d9 | -1.12797 | -53.64107 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6c7c91-6011-3ca8-bade-80d0611fee81 | -1.12463 | -53.63898 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f936839-f43f-3ce9-862c-8aa9bcb4f8ad | -1.12414 | -53.6407 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c078066-4e93-3de7-9c8c-7406dec3a83a | -1.12391 | -53.64355 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08c03f8f-1cec-3e13-ac60-c60183c467e6 | -1.12345 | -53.64526 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d6c6b9d-991b-3442-bfd1-971fbaf8aa03 | -1.11727 | -54.06162 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863d2a66-54c9-32d0-acdf-d4fcf0819838 | -1.11617 | -53.61861 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d03ac388-b91c-3c2a-a597-cb9fc355c4d2 | -1.1154 | -53.62347 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e86948a1-80f0-33e3-b7b0-18f861367a3b | -1.11356 | -54.06105 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa859e69-7139-3c34-af55-65543c6adead | -1.11233 | -53.61821 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b0a72dd-a612-3884-bb65-bc33a7d75879 | -1.10855 | -53.61749 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79a64830-f131-320e-afb4-83e7318249c1 | -1.02919 | -53.7291 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c68a7e2-1f6b-3945-b6f3-a84358786087 | -1.02843 | -53.73409 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234894fa-fa0a-35da-980f-1f226a3ae81a | -1.02539 | -53.7287 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f0b406e-ee4f-3f5c-98f0-c0af1138ec3b | -1.02465 | -53.73355 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09792941-2ab3-31d4-8f2b-04926fbe4d23 | -1.02158 | -53.72837 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3e017163-1af0-30ef-8ef9-5038483bcf29 | -1.02087 | -53.73303 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 555656fd-93fd-3a96-bd80-f073c1b9dc44 | -0.94469 | -53.72365 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83254c85-2bca-3876-99a7-a46a06843e4a | -0.94094 | -53.72297 | 2024-10-11 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d98c56c-83e5-30ad-86e7-cf99b75d7440 | -3.57713 | -54.53463 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcf39c33-467a-3b99-a5eb-75e5ba9616a3 | -3.4978 | -54.4533 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c41a8169-5697-3e7c-9e77-eb27ce8d3288 | -3.33921 | -54.61943 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ceb77445-21f5-3cd0-a922-b1b9da0a0f8d | -3.15245 | -54.63734 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ae32e34-0475-3e8e-ae8b-1cba31efeffe | -3.07196 | -54.77306 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c183b34-98b6-35e6-99f4-640492f365c5 | -2.9715 | -54.62196 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb0e45a4-58c9-3112-bfdf-d6cb48a4bf8e | -2.94402 | -54.80223 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc8b7bdf-ddf3-3c21-837c-9fd09b661c5b | -2.93416 | -54.81809 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1757851e-3858-3264-bae1-31006bcee20f | -2.86079 | -54.83022 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README81.md)
