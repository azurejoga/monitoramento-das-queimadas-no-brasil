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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ad0067-f49f-3c46-98de-79ce8b344df8 | -1.99517 | -56.54435 | 2026-09-22 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c1d3214-4ab2-393f-a44f-64b8f95c2f18 | -1.32379 | -54.66434 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ded47a12-0366-302a-84a7-69dbb4482217 | -1.32854 | -54.65968 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a00a740-43ad-37a6-96f0-ca331ae2d551 | 1.98908 | -50.86614 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 756ef403-7461-3e3e-9ae9-1fe0a82c6491 | 1.50931 | -55.88054 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d177aa9-6921-3929-80ae-c4777c4be73f | 1.08242 | -60.67786 | 2026-09-22 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4698649-bf5c-3c0d-8e41-04cfe18e941b | -1.06989 | -48.81107 | 2026-09-22 04:44:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 380bf490-8081-37dc-bac4-f3eb5f207539 | 2.09416 | -60.21336 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7df5de39-9e63-35ce-91fd-bd20dfc7dce7 | -1.65014 | -54.91582 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fef96666-6dc3-3533-a405-0cc8133057d7 | -1.74798 | -47.13113 | 2026-09-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 07c77cd2-e73e-35aa-9b76-8149b419ffff | -2.82828 | -46.70935 | 2026-09-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ce69ded-dc8c-37a6-b5e6-951a940acc92 | 1.07635 | -60.67886 | 2026-09-22 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51fae45c-ab3d-3c27-a13d-b866e0903755 | -2.94688 | -50.30315 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c02aa86d-1a7c-3af2-a98d-70f7282eefd8 | 3.24692 | -60.23632 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff305107-5881-3433-a2c3-0ac5d617a73b | -1.24906 | -47.383 | 2026-09-22 04:44:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0d0a29b-e299-3895-9963-ad18633d8738 | -3.69069 | -42.95992 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d529be90-4692-3d13-bd1d-1daeb1807d26 | 1.98964 | -50.86974 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 037be0d7-6b69-38a1-b0e5-ddaa8ce28964 | -1.64934 | -54.92092 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9926ef6-73a3-3982-a59d-01a02e7753d5 | -2.17525 | -48.31848 | 2026-09-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e262667-d25c-3ee0-881a-46c1924d2eac | -2.73762 | -49.45997 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 142c4371-6f30-32ab-a234-4ee727f0f47d | -2.95741 | -50.32233 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cba45a8-56c6-32a8-b385-383b4082c7c6 | -0.81767 | -48.74667 | 2026-09-22 04:44:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fc92c96-4462-3b2a-a7c6-5a92afb0a2bc | 2.10011 | -60.21212 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d0887a9-d0ad-383d-8183-683e4d0f4402 | 1.53091 | -55.78814 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d3d0a4e-ca2f-3d39-9dd8-d26268b50424 | -1.94211 | -56.59291 | 2026-09-22 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 20caa4aa-55a6-3cc5-8969-09fe9904af81 | 1.07686 | -60.67636 | 2026-09-22 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5410389c-b2b5-38d0-b68d-18539ab4c11b | 1.47725 | -50.91846 | 2026-09-22 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a52e228-672f-3364-b956-300a674c7f34 | 0.16548 | -60.49178 | 2026-09-22 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d723ec30-c336-39f4-be90-69abfb6fc710 | 1.51238 | -55.87119 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e1328d8-74df-328e-acb7-7e7bde9dabbc | -1.20717 | -54.2269 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6beae2fe-b159-3154-9f4a-5590693d3590 | -2.45391 | -49.22963 | 2026-09-22 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5c3b0e3-3502-3831-a9ac-755c75a33c55 | -1.38442 | -49.32492 | 2026-09-22 04:44:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f905399-1138-3122-a0c2-4f2720ef71cf | 1.53977 | -55.78709 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5df2cd28-73c0-39c2-9fe7-06aa395ac1bc | 1.51066 | -55.88911 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6992a90-5e43-3cfe-abf8-80ce073c66ba | -1.61221 | -54.6235 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be1c245-f9c8-30c3-9b5a-ef2c7f0ec8fe | -2.72715 | -51.55415 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a465042-6800-3d46-b925-eba2cc7b6aed | -1.33165 | -54.6654 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f82193cf-414a-328a-b63c-1fed5de18bdc | 0.17943 | -51.43819 | 2026-09-22 04:44:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ee9978-0e51-35f1-8c7d-9b7d162ccf5b | 2.29104 | -50.93106 | 2026-09-22 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed7bb662-2666-39be-9f5c-2e1e3475ac9f | -1.45284 | -54.24024 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d97501-38a7-3192-8c10-dec1aec2d0d8 | -1.11634 | -54.16255 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7decbcc5-9ef7-390d-b7fb-a75d966dbbd1 | -3.34046 | -42.78299 | 2026-09-22 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11b210e6-9b82-31b3-ad4d-83f1b1cc186c | -1.025 | -53.73414 | 2026-09-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5751603-d6b1-3f6d-9f03-102e27b092ef | -3.6851 | -42.96443 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c405a600-fb1f-3d72-881a-29afab937c0e | -3.68588 | -42.95917 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4d120829-aa25-3b25-81cb-8711d9d6b0e4 | -3.16798 | -48.61483 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b54ef3-ba8b-3fd1-bec9-c2cd2032037e | 4.02956 | -59.65272 | 2026-09-22 04:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa30d3fc-ad45-3638-b23f-89566188bd7b | -2.44202 | -46.01657 | 2026-09-22 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16bb6b6a-c738-3035-a2e8-6621b26cdc95 | -3.68991 | -42.96518 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d72fdbdf-45e1-38c8-a955-e33114c2b3ba | -2.83434 | -50.45712 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 877d6470-5385-3a42-9d86-b62f1b427dc8 | -2.90858 | -48.90713 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 271b1c91-e6e2-398a-8f26-1c5ba9983968 | -2.90183 | -48.90609 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3714f4dc-e66b-360c-abd5-c1fdb04abb19 | 1.99246 | -50.86563 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66d62eca-70bb-3b85-ac34-d655d29ef80a | -1.94237 | -56.59321 | 2026-09-22 04:44:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d354ad72-0424-3c0f-b6cd-0919d94ea0f4 | 1.5117 | -55.86688 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d80fa0d-2440-3d98-94a4-bf4772df9164 | 0.16985 | -60.49684 | 2026-09-22 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b938e92a-f7b0-3d8f-8943-343825d4d909 | -1.29516 | -54.20867 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34624b94-9b1d-32ff-984c-991325a5b1bc | 2.09352 | -60.20907 | 2026-09-22 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6596b248-f848-3835-a138-c8fcfdcd34e2 | -3.02131 | -51.19573 | 2026-09-22 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2f8c4fe-df9c-3553-bd19-2d338f9c985a | -2.55194 | -49.10089 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a692def5-ec84-3439-8318-a39bf0da4fe0 | -2.16865 | -47.88306 | 2026-09-22 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5233eda-1edd-3427-9c52-a0098a0f6441 | -3.69147 | -42.95465 | 2026-09-22 04:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8e1b1d15-4d79-3726-a712-74d740058c04 | -2.92418 | -48.73937 | 2026-09-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2747be41-a37c-35e3-a6f1-5ebb4f064e12 | -3.85068 | -40.59929 | 2026-09-22 04:44:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a2b67e3-4fcb-3329-8401-83dd159c5035 | -2.54859 | -49.10038 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a654e5fa-fdd1-37d5-894f-8ce379fbcc09 | 1.5062 | -55.88967 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d951811-704b-3c6c-b075-481ca90a1d5f | 1.99302 | -50.86922 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 90870fcf-efcb-369e-baf3-e9c39bd7166f | -2.94688 | -51.04243 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b9ef5e-88c1-33a5-956e-245e388a0e87 | 1.07757 | -60.681 | 2026-09-22 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7873e5ef-ad7b-3950-9035-79215611f99c | 1.50428 | -55.88175 | 2026-09-22 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b099a387-be63-3869-8bcc-c2271cfe0fdc | -1.45663 | -54.24092 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b3358f0-1b0e-339f-a491-d499b9f2f1ec | -1.09377 | -54.20705 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c5a9395-d887-311f-88dc-0fed2b571b03 | -2.95946 | -50.41748 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7e9ba1-f796-3fbb-b1f2-5da55eeda4e6 | -3.04072 | -50.2649 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c1b8bf8-f035-3764-a115-028fff734d4a | -2.73905 | -51.36895 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1dfe22d1-71a4-32d6-b8da-094cd5a35ec9 | -1.45313 | -54.24247 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b00c857-9b57-31a2-b868-079803c4b388 | -2.95019 | -51.04295 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be5a597d-b58e-3c2c-91d5-a21f941ad08d | -2.17127 | -48.32164 | 2026-09-22 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3de4210f-6066-3955-b20d-4e0942d9a5fd | -0.93613 | -47.55227 | 2026-09-22 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51425a71-5d12-33d9-89f2-e52068168ea0 | -3.34326 | -42.78926 | 2026-09-22 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0524e3bb-cac1-3dfe-a511-1e327e59f82d | -1.20955 | -54.01407 | 2026-09-22 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47994e87-eea4-351a-b1d1-f133bc22fc40 | 1.95825 | -60.56659 | 2026-09-22 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fae92ae3-ce88-328d-825d-661a55cde053 | -1.33245 | -54.66031 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 188ae6e6-e9e0-3715-99d9-bf21b56d57f7 | -1.11711 | -48.03519 | 2026-09-22 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f1e1157-2be1-3a83-933f-d91e52a6e2c4 | -2.26229 | -48.75349 | 2026-09-22 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c89eb31-3b68-3bf6-a469-239cf2463eb6 | 1.07562 | -60.67424 | 2026-09-22 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 601298ed-fe58-3e83-a6b0-2c50478128e7 | 1.9919 | -50.86203 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5030ef0-515a-3a7b-9a9b-e16c65f9b318 | -1.84477 | -54.95533 | 2026-09-22 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 371782d5-e6ec-3c31-ae77-ffd60f56872c | -2.45256 | -50.37279 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04abe534-4e2a-328b-aed8-0071c63d7a21 | -2.7266 | -51.55767 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d60b069-e20b-3303-9f13-51db38fad3a2 | -2.16806 | -47.88689 | 2026-09-22 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 102a132c-899d-3269-8f8c-ee43ae6f0980 | -2.17184 | -48.31795 | 2026-09-22 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d62cd3c3-184c-32a4-8856-80c7e19cfa50 | -4.683 | -40.15005 | 2026-09-22 04:44:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60cd5556-59c5-3c65-afe0-99032f2f45c5 | -3.04679 | -50.26936 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c212687-2017-35a7-a3ce-9b6058b3fa54 | -2.31417 | -50.45327 | 2026-09-22 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85fe8203-f73f-37b2-8374-cb954e5cebbb | -1.61107 | -54.62495 | 2026-09-22 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 815e4511-2c71-3c40-823c-ecc7c54da3f9 | 1.98063 | -50.87846 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787336b3-0b65-32a4-889c-a86c42d61aba | 1.97162 | -50.8872 | 2026-09-22 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a585ac2f-c6f0-3a51-a183-313c7204d22a | -1.46597 | -60.27223 | 2026-09-22 04:44:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ead40b45-fc4c-36e4-aa1f-f200b62e4f37 | -4.9634 | -55.82439 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
