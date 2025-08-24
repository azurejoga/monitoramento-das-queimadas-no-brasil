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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9804498-4e59-3ca7-8579-55c5e19ab76e | -20.3599 | -51.68 | 2025-08-24 03:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 119.8 |
| d9468bf6-311f-3205-b11f-14a36a2ad584 | -9.0232 | -65.6982 | 2025-08-24 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c100f4cc-fa3a-309b-a7c6-20da35d8b924 | -8.6131 | -62.5929 | 2025-08-24 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9eb85161-8eea-3acd-b093-5a542aac385e | -20.3594 | -51.7023 | 2025-08-24 03:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 86.1 |
| db235738-e12c-3a87-8d15-f753d5304e99 | -9.1721 | -59.4823 | 2025-08-24 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7c99c349-4e23-396a-974f-c16b630cf6d7 | -20.3594 | -51.7023 | 2025-08-24 03:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6ac716ec-5973-31c2-9df1-be8911d673c8 | -9.1536 | -59.464 | 2025-08-24 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| b7011920-1b03-30f0-a888-ada712d198bc | -20.3396 | -51.6839 | 2025-08-24 03:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e6cc74ba-9601-3a7c-a618-996fec53ba10 | -4.9605 | -55.8226 | 2025-08-24 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| cd6bbeeb-30b2-3a6d-a11e-08f01257e7ed | -6.8927 | -45.6963 | 2025-08-24 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 9a356664-ad5a-3cbc-8d42-ef5f0396991a | -20.3599 | -51.68 | 2025-08-24 03:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 73f3ce8e-bd40-3b88-b178-661c788692dd | -9.1722 | -59.4629 | 2025-08-24 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6bc0789c-13e5-3bb1-b35c-bd01c47e9c07 | -16.7965 | -51.3637 | 2025-08-24 03:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 14e95580-5c15-347d-9506-40cbecf79dc6 | -9.0046 | -65.6988 | 2025-08-24 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0249c59b-6f69-3592-8511-d565bbaea23b | -9.1721 | -59.4823 | 2025-08-24 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1a9b5b73-4355-33eb-b74b-ab5546d2808a | -9.1535 | -59.4834 | 2025-08-24 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| ff9ff947-ba26-3760-8373-b8db256032bc | -9.0231 | -65.7169 | 2025-08-24 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f48c6317-38c5-32fc-aecf-a77a9d1dbfda | -9.0232 | -65.6982 | 2025-08-24 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 1a0c9ab9-839d-3aa0-b30d-c314c0635fd1 | -10.6128 | -44.3284 | 2025-08-24 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0ad3ce04-306c-30fc-bbf7-9546409c6c95 | -16.797 | -51.3419 | 2025-08-24 03:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ec0b5b20-e93b-3e07-ab73-6af64e3a51f3 | -5.4181 | -60.1784 | 2025-08-24 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d61de093-74b5-39cc-a132-b018de653f85 | -8.6131 | -62.5929 | 2025-08-24 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3d7bedc4-a544-3d53-97ad-700e45551f2c | -9.1998 | -60.793 | 2025-08-24 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8ab56d98-4847-3d6b-8f9b-86248f0b3e92 | -5.6912 | -38.48722 | 2025-08-24 03:40:00 | NOAA-20 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f7582213-4aeb-3286-869d-7d87fc807249 | -2.86703 | -41.7542 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb5dbc4c-693a-3af7-8b8a-07d7ac241fd4 | -4.69472 | -43.25739 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14916455-f015-3f26-9123-efb7440d545c | -3.78704 | -47.56558 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7af0d4f1-f067-3cf4-8743-8bb969e84f30 | -3.44304 | -44.14368 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f064ca1f-de64-3fc2-9003-da3722446673 | -3.52516 | -42.6986 | 2025-08-24 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9433541-5395-313f-98e4-fc5ef8098e5d | -4.55696 | -43.22768 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22095bd2-c96b-3dde-a998-0af917a3115b | -4.5557 | -43.22527 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbf4a7a1-aa9f-38f2-a360-a3e9dd854746 | -2.91684 | -48.30694 | 2025-08-24 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dd99878-0fb3-3040-89b6-813c7886829f | -3.15796 | -43.25847 | 2025-08-24 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0ab167c-1d2d-322b-be57-bc594d9358e5 | -3.5933 | -47.5236 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 60644b72-ec48-3858-bf42-34a28a8c9f48 | -3.53013 | -42.69944 | 2025-08-24 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10275095-d7c2-3249-b091-a93c54caabfb | -3.44244 | -44.14719 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c3f3352-27e4-37bc-a9c0-8aaceee70e5e | -4.65747 | -41.41811 | 2025-08-24 03:40:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6d55883a-e051-384f-b545-6f9488ec66e7 | -3.78598 | -47.57151 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b119775e-f515-30fb-9edd-80558c4c8c25 | -2.79091 | -41.88486 | 2025-08-24 03:40:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56ebc978-2f7c-3699-9cba-80050e881e4a | -2.25508 | -47.85513 | 2025-08-24 03:40:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c3fc3ec-8bbe-34f3-bde0-0248227941fc | -3.80884 | -42.54547 | 2025-08-24 03:40:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6613abda-8a70-3ff5-ba11-c4ed2409ee0d | -5.3717 | -41.21524 | 2025-08-24 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f9ab7ee-2b36-3f91-814d-adfb5db0fc05 | -5.53178 | -36.8471 | 2025-08-24 03:40:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a2d58cc6-eae7-3fc6-b7fa-5f8faf22e4b3 | -3.59899 | -47.53102 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b47f248-1806-3b0c-a2dd-9c5059ece88e | -3.51245 | -47.21326 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1e46aebb-fb32-318e-9673-05344437ef1a | -4.53329 | -43.98311 | 2025-08-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 293279b6-bd3a-3f76-85aa-0cd40a173836 | -3.79579 | -41.00495 | 2025-08-24 03:40:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06afc5db-2377-37bd-804c-75c34634e625 | -5.53238 | -36.84341 | 2025-08-24 03:40:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d5413966-ac3b-3e15-b2f9-55761dcf086d | -2.9127 | -48.31193 | 2025-08-24 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5427163c-a608-32a4-87b1-a3ca29d834a9 | -3.58729 | -47.52922 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aae26f2b-3419-31cc-92ff-4ecdb975ac8f | -4.78331 | -45.33097 | 2025-08-24 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c37066b8-f8c5-3ac4-8347-4aa53bf9a960 | -3.81184 | -42.54464 | 2025-08-24 03:40:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2320e97f-dc1d-32b9-8fea-adee0a2189da | -3.44879 | -44.14043 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7e02f25-c7cf-36f9-a95c-ba4eeb5ed5f3 | -4.55622 | -43.2223 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a8c63f-76c9-3b62-a842-ca9eb17d0202 | -5.36663 | -41.21877 | 2025-08-24 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93acb84c-9747-30d5-845e-8dadcacbb052 | -3.16237 | -43.2578 | 2025-08-24 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0dd8ac5-67a3-363f-b8d5-1a9bc0777bb9 | -2.25983 | -47.85558 | 2025-08-24 03:40:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00cbdf52-d3e7-30fb-bd2a-1b5eb6477247 | -3.44973 | -44.13758 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2111d5f6-e08f-33f9-8dd0-82973f9a0791 | -2.87174 | -41.75498 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fd6f29b-ee79-3e5b-94ba-ba9d8bc6489d | -3.15718 | -43.2569 | 2025-08-24 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83cf6477-62bc-3b5b-b0fc-1e1ba555c1b7 | -3.52918 | -42.70518 | 2025-08-24 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f96bc5fd-cec3-34a0-8ab7-945ad1bb6c94 | -3.78491 | -47.57742 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4bacb69-b5bb-326f-8754-cb83fb66cfd7 | -4.69421 | -43.26037 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 660ba884-00b4-3ac3-b69d-e6c6458ceb67 | -3.60081 | -47.53152 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2cbf6875-f912-35ad-afce-f8e6e9bfab34 | -4.85048 | -42.69854 | 2025-08-24 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 649aaa59-a63a-3252-9421-aea122a5f8bc | -3.79139 | -41.00424 | 2025-08-24 03:40:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 339dd6cc-693c-31b9-b538-f48eeb462824 | -2.91557 | -48.31408 | 2025-08-24 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c9be079-f3c0-30dc-b127-86256c01ae1a | -3.51349 | -47.20723 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5f9d394e-0aae-3ed4-8128-3ba6d4fae302 | -4.55238 | -43.22386 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8242b2f2-5472-3562-bfcd-d778e6197b44 | -4.6323 | -41.40363 | 2025-08-24 03:40:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f016122f-1937-342d-98dd-875281157d5d | -4.4815 | -38.61917 | 2025-08-24 03:40:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1a222fd-15a5-3e12-b77b-6fbef32dfe68 | -3.78987 | -47.57804 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8725a34-f597-3da4-938f-3236338cd7f4 | -3.59401 | -47.53057 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ea5f376-4c71-3943-a1fd-f0bb2f9acc6a | -3.59222 | -47.52991 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a8605159-e9aa-3277-b302-501ec832afe5 | -3.79089 | -47.57215 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51ddb631-8e82-310d-9b24-adcb490e4c33 | -2.86895 | -41.76291 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b32cbcfc-b391-3857-96dd-1f3aa61b2778 | -2.86974 | -41.7579 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b01264b-314b-3f8a-b0e2-15f5cc08c447 | -2.9097 | -48.30574 | 2025-08-24 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d19db52c-7d4c-32b6-9778-56d516fea3ae | -4.7241 | -38.39642 | 2025-08-24 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2cb74727-067e-3de2-89ed-419c0a1fa28f | -4.65586 | -41.41562 | 2025-08-24 03:40:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| caaeb954-e547-3991-8a7b-29dac5c29657 | -4.53713 | -43.9814 | 2025-08-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37df48be-cb33-38d8-84c6-494294d20949 | -4.55745 | -43.22469 | 2025-08-24 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c275140-c252-3805-b580-394ab9d21379 | -3.15848 | -43.25539 | 2025-08-24 03:40:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a55ee3d-6cbc-3fd5-9283-b75b8aaf63da | -2.25277 | -47.85464 | 2025-08-24 03:40:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430cd37c-6c2e-3417-8986-68ed5596fc74 | -2.26213 | -47.85613 | 2025-08-24 03:40:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56922f48-f9a3-3989-8593-d7b7d36323d4 | -3.59514 | -47.52426 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2c81c329-bec5-355a-b202-ef4087c1b8e3 | -3.54741 | -41.62357 | 2025-08-24 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8262d518-aac7-314c-9069-e0cf48219d68 | -4.30864 | -48.10149 | 2025-08-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 214f868d-85cd-306b-b76a-799b4fcbbd90 | -5.90221 | -37.82245 | 2025-08-24 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c58cb25-ee4b-3cbd-a872-5bdc981dbc41 | -2.91391 | -48.30484 | 2025-08-24 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9352349-9bd4-34e5-904a-6b7f189c592d | -2.87007 | -41.76496 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4c9c5fe-8e82-36eb-be69-5991eb1985de | -3.60006 | -47.52477 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e136d26a-754e-383b-ba33-5aa22d892d6d | -3.60192 | -47.52531 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d4e00477-1ad5-3a58-88a8-e12f771c6c1c | -2.87091 | -41.75997 | 2025-08-24 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f5fcffb-fcc7-32e3-9008-02b1b5c39922 | -3.44913 | -44.14109 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cb65684-bcea-3faf-8644-0ece3676caee | -3.44215 | -44.14652 | 2025-08-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b97d117a-36b1-3846-bdf1-e5315d613927 | -5.90573 | -37.82303 | 2025-08-24 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c3ac7fe7-1e07-31ad-95b5-dfb082fad3fd | -3.78418 | -47.57067 | 2025-08-24 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d947b99b-695d-3ea0-9c37-a8a9a845675d | -4.78402 | -45.32692 | 2025-08-24 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9baa6fe7-2741-3500-938b-0651a94fa02c | -11.105 | -44.78114 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
