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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2edcaa8a-eec6-3624-ada1-59d3ff7e09b1 | 0.53103 | -50.89861 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b004ce84-83f7-3879-aab9-207e1598f125 | -3.01004 | -54.069 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f9b548f-9b3b-3322-8dc0-22f5d589aed4 | -3.18725 | -50.54333 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aa8c381-0420-36e8-9c7a-3e71653956ba | -1.32658 | -52.4473 | 2026-10-09 05:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad3b694d-a24c-319d-9f0d-9e7e9abe2e0a | -3.05585 | -53.93523 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aed32046-7eae-363c-aeb2-d1c5aacbf43e | -3.00417 | -54.76987 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06448847-b861-3095-8868-a0358f3a54e0 | -3.09494 | -54.28866 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b83ef183-1015-3058-800f-0c46d54defda | -3.0661 | -54.17688 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91f31de0-450f-3868-932f-d3c0052b3a43 | -4.35838 | -55.2251 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83368708-b3d6-3a3a-8805-8d18c98bb468 | -3.39769 | -60.85007 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9142027b-1574-3fe6-86c1-7c671474f71c | -2.03076 | -57.05742 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9606d9e1-f472-32b5-a571-44ff2a517837 | -2.49804 | -56.06182 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fddf65bc-a1e0-3dcb-b922-375df4b7b571 | -3.01273 | -54.7396 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aeba3e2-9272-3e7a-82f8-33c27f1143c7 | -3.27924 | -54.07227 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6abc8f31-74a1-3695-9bd4-8fed5d874a84 | -3.53137 | -59.57544 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17e48be4-ffb7-3f35-a647-50858387dd65 | -4.29293 | -54.80323 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bab12296-6a44-3a05-8afc-c535adc56420 | -1.77415 | -55.02074 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f27de9-761a-35e9-b52d-a82347f4027d | -3.74357 | -59.47953 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b1a8a11-03af-3904-b7d4-49b25921e101 | -1.83148 | -54.9946 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6fdd80e-ecab-3137-871b-5d751f9f3ce7 | -3.9284 | -56.03006 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a50ef5b9-95ac-3596-927f-a40fa68e04b2 | -3.59081 | -54.66617 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72acd17e-b997-30ea-af6b-5f8c35d08190 | -3.00363 | -54.12377 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45de98b9-9fb8-3387-a39c-b37282be4b49 | -3.56698 | -54.67176 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8fc3f04-6304-37fc-b756-a8cc6902607e | -3.72897 | -57.14939 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 727df1b3-c27b-3a4f-9216-893322b72e24 | -3.11059 | -54.19301 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2bbc7462-09e3-3f5f-81e8-56f3a305715d | -4.32605 | -55.02016 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07aeb67a-cc02-3402-82ed-604ba43826a9 | -3.18573 | -60.40292 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 420f4432-7ea0-3cc9-8105-c86cd7558605 | -3.72954 | -57.14581 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33372945-ee58-3e20-85ea-87f90e457af9 | -2.82359 | -57.13654 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8f73090f-d726-34c8-b21c-e14538a5074e | -2.99924 | -54.06247 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2325d3c5-2000-30d1-932c-ba73bcb42ff0 | -2.98621 | -54.07022 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e7efe83-75be-3f7a-bca4-0674d18a3a41 | -3.19455 | -50.56118 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f296ef-fcd7-3750-bcad-671e59e7aed3 | -6.95387 | -59.52739 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 496fb817-72d0-3666-9d69-d0fdb609d9e7 | -1.40297 | -57.93423 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c08c174-7006-3702-a128-4072e0fb1564 | -3.69312 | -47.68353 | 2026-10-09 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 819bff28-c547-34b7-b43b-3b30d352da1c | -3.25273 | -54.03854 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6d59e7b-1782-3918-b711-ee6c75433e98 | -9.25905 | -60.89878 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10878cc7-0058-31e3-8329-cda104324c6a | -2.88674 | -54.18751 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4264f17d-7045-302b-9808-0d4b9a4fb98d | -2.83984 | -54.1372 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22cafc75-de0f-3277-ba12-6a697bcd9b01 | -3.41199 | -59.57834 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a09e7a5-36a9-3da0-a0fd-be9d906507ca | -3.59622 | -61.61399 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebfda2bd-d17c-3eea-a0e7-cfc1a3aec752 | -3.46933 | -60.2537 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d29d64cb-4a3c-34b6-a095-4aeb08355a62 | -2.73972 | -48.42882 | 2026-10-09 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51143345-3af3-38c0-8ebc-e8580f09b213 | -2.78199 | -59.98901 | 2026-10-09 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5d839e-2f61-35c3-a8e7-895a4877ac2f | -2.87984 | -54.18169 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed00f633-3b40-37b9-9f66-95246d57c995 | -3.32859 | -58.0048 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39455461-180f-3f8c-977d-7393c14300da | -3.97025 | -59.35752 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a438b1f8-7a09-367f-9c53-177a0b0dff70 | -0.64107 | -58.02496 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad8a5513-22e9-3386-be8b-7c27583f4d89 | -3.0016 | -54.07258 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78aacf4a-0b52-35ef-9e7b-56ecd0ad18f2 | -3.75791 | -58.51373 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e4eabc8-d90c-3ba8-97a4-1e933452010b | -3.25773 | -59.605 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab157c5-77f4-3cb4-aaca-faad2a85065b | -3.65232 | -59.70697 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3318c02b-21f8-3f5f-b6aa-083f2d9ee935 | -2.81882 | -54.09538 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21a242fc-1b0d-31c7-a494-c0fd15e5d5e8 | -3.35898 | -50.48702 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ace87d4-8a19-3b70-89a1-84d8bfba0731 | -3.85289 | -58.89906 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19e039d4-dd50-3759-b596-41c2eb8008a0 | -2.5834 | -56.14831 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6320b5fc-a7ad-3cec-baa3-170494180095 | -3.05733 | -59.26699 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f771a1-cf78-3a3c-bc6d-78ccedafe6c5 | -10.25567 | -59.0288 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b5769da-dcc0-3859-ac1c-97fafcd70195 | -2.87689 | -54.20042 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33ee592-3fae-30e6-9b07-abbe5776561d | -2.98338 | -54.11354 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b48df332-4c27-315b-9222-547405b0e61b | -2.47011 | -56.08899 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d0e8e73-264d-3c3a-9037-bed7cccd17ce | -2.78414 | -51.68119 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc9cda0f-b210-3299-ba5c-656e228e4222 | -3.30926 | -54.05724 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85a4a14b-2243-3be9-962b-ae7da6cd1ae1 | -3.36274 | -50.47207 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20646c3d-cb0f-33e5-a620-e9ca9f0ec544 | -3.47897 | -59.5816 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29f56f81-57a5-3e8f-b936-c9d3ff8d79c3 | -3.10876 | -53.77187 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f05650f9-b5c0-3f3f-ad87-61c584d44cb3 | -1.82788 | -54.99405 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86f405f4-15f6-3818-9043-90051bd0d154 | -2.07189 | -56.883 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e1083f27-86dd-369e-8a87-eddfd849ddb6 | -3.75974 | -58.994 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cad3387-ff54-3117-91e3-eb11a4e6c22e | -3.90167 | -58.95663 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7887853d-4e51-340e-84e9-a14b9e1e570b | -3.08185 | -54.25132 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 538b6a3a-de0f-3a9f-8048-62e9cb951010 | -3.16207 | -56.86037 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef9d227f-8620-3967-84db-88c20cf3725f | -3.00721 | -54.09998 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e849fa6f-b614-38fb-a53f-4fc41bd1c545 | -3.08435 | -54.28505 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ecbc26e-e9ee-3d3f-b818-e34952c5bf87 | -3.87957 | -55.99176 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79c7259c-b313-3481-a0ec-147b81d3d67c | -2.01832 | -61.27065 | 2026-10-09 05:23:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea2dd7b-e7c4-30d5-8843-ac31a255672d | -2.81128 | -58.29013 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| cfadb94f-f9d2-37bb-8ba0-48f89ae305cd | -3.08353 | -54.2869 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c3bca8-dcc1-3dfb-acb7-05862d66a7c3 | -3.54118 | -54.63382 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1796282f-f3ee-3861-a2b8-e15aefdc9e5f | -0.99716 | -53.74162 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc9829f8-aa01-3bf7-b0c9-3f66f0876eaf | -4.3714 | -54.74867 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55756185-5fc4-3f8b-97b6-b24d1bc9324f | -3.5639 | -54.66029 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bee71ca2-d18b-33d2-9e46-1e92f902c18e | -3.02017 | -54.09229 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 781a5005-34bd-3f1f-a1e0-3964612b037b | -2.94156 | -54.15551 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 594bcd20-c268-36b0-9cc8-da5cccba7921 | -9.25583 | -60.87629 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8010dee-e9dd-31b1-a244-eb704336a06c | -4.13124 | -54.27021 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21e2e1dd-3139-3fe0-bbf0-6d06fbd37a96 | -6.67336 | -63.02954 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5f27c43-48d5-3c8b-808f-43eaf013f509 | -1.47143 | -54.54481 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1ecc85c-b9ab-31d5-bdd9-4bfd5806d2cd | -8.5277 | -46.90651 | 2026-10-09 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6411065a-fcb9-3a87-8d82-cc6958659cde | -3.15748 | -61.08089 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 235c5884-889c-3c9c-9931-ff1506853eb4 | -3.26451 | -54.06519 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e3b918-4f97-30d5-8ca2-84595ddb14a2 | -2.73589 | -54.10932 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3d4ad09-023a-3bc8-b7bd-a13decf33550 | -4.98307 | -46.04118 | 2026-10-09 05:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fbe7342-85fa-3daf-b6bb-4a313e581eaa | -2.88846 | -54.07692 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ba7cad9d-dec7-3d2c-850f-34d8a9d7b545 | -1.51666 | -54.52037 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 585ea0d5-b9b8-30c3-b534-6aa6b9f1acec | -4.6176 | -49.2101 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f04707e7-abf9-32ce-87e4-60b116e77d64 | -2.88685 | -59.204 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21d7c123-f943-3b9a-bbf8-7dfb1fbd217d | -2.50308 | -56.12043 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113a5e0e-87aa-3c75-b86d-cf7551b3116f | -2.88726 | -57.63788 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e588a3b4-3a94-33dd-9d05-c45ba08f603a | -3.16486 | -54.08685 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README198.md)
