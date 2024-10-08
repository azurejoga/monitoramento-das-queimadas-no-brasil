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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c5a23f0-ae29-3e8e-8806-023df8914cc7 | -4.63451 | -50.98062 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 840de084-26d8-36fb-8842-81f8f53370f6 | -4.63416 | -50.97945 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4280495-0e45-3d8d-b32c-6d8b086a2c7f | -4.63388 | -50.98463 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beb89311-a302-3d8e-b08f-6610f7ecc8ac | -4.63356 | -50.98346 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56f74f17-1af2-3595-a8bc-4779650342b7 | -4.63158 | -50.97611 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a0ac3fd-9ec4-3ba3-8470-61a997d834a4 | -4.63097 | -50.98008 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd4a4bff-7efa-38ca-80d8-c5b2028c9015 | -4.63034 | -50.98408 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 249a3ff6-a0c2-3935-9eee-2af12751bd71 | -4.62972 | -50.9881 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64276a82-948c-3298-82b9-d2124971f772 | -4.62742 | -50.97954 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e8a46f-fb1d-3b9b-a43a-a255b3677fa8 | -4.6268 | -50.98354 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8aac6cc-0c50-3ade-8251-7a20936a1d00 | -4.62618 | -50.98754 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f344553-a685-35ca-a028-a35ff38e0400 | -4.15606 | -51.04454 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e7198e7-e80b-3255-a916-08d627ed033d | -4.15545 | -51.04848 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfb4fd10-5d38-3b65-ac66-8ed29fa5e6e6 | -4.15485 | -51.05236 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 878b61bc-d102-3f3c-a421-2527a6a97ab9 | -4.15254 | -51.04404 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b3778d0-9fe4-395f-9161-adaaccb584b2 | -4.15193 | -51.04796 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d2b5adee-f81b-3825-b910-f6f461852f97 | -4.06184 | -51.11874 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 052b0a12-85f7-31cd-977d-03f04f39c039 | -4.06123 | -51.12263 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b26fc046-7f80-3723-8dfd-ceaf36e3ab63 | -4.05833 | -51.11823 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99846ff-8ca0-3900-aef3-6d221a2b74e2 | -4.05772 | -51.12212 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49f12fad-ed3e-3025-9e6c-3506827b8ed6 | -4.05482 | -51.11772 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8392723-347a-3fe2-89e6-9529ca1c2b39 | -4.05422 | -51.12161 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d953fb55-bce4-3ee0-a1cf-9c0c750fbb27 | -4.05071 | -51.12111 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f0d452-3569-393a-b9b4-560fee66c946 | -3.90838 | -51.01627 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6d46d5b-a5e9-3212-8018-9061efc06bd3 | -6.421 | -51.70951 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23c47e96-0364-308f-9ad5-5e3f2689179a | -6.4175 | -51.70901 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 311b2538-0f7f-3a8d-aeda-89a3c0e3ba85 | -6.41689 | -51.7364 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0dee03-4c04-3911-a061-a5873c7d100a | -6.4163 | -51.74027 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d857bfe8-bc7b-3baf-95d2-c3dddb12141d | -6.4134 | -51.73588 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 964f1c94-9b36-35e3-ae08-3538b4a5861c | -6.34983 | -51.7035 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 029c1d20-f21c-3b80-beb4-fd55ef8cefb7 | -6.04194 | -51.38414 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60eb6f5a-6808-3cc3-99c5-5b2df4189d40 | -5.87855 | -51.58361 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68042ff9-fc61-3c56-a605-70944ab4fe4a | -5.87798 | -51.58737 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3a20edd-4b72-301f-bbf1-7aef85ea3541 | -5.79812 | -51.61137 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b38aba-d6d5-3ad3-b3d4-d5186668928f | -5.79463 | -51.61083 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2dcbc59-6dbd-3711-9539-53b3d1046e26 | -5.77571 | -51.45325 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b9b77b0-6c96-3399-bd81-6f43d074a5a1 | -5.77278 | -51.44882 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e302ef-ed5d-3245-918e-5dedf09c921f | -5.77219 | -51.45272 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6225143a-50f0-342a-9c77-d1e0d2340ba5 | -5.76927 | -51.44828 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69ee5cb9-24bc-34a6-9d04-28143cb749fc | -5.76868 | -51.4522 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68769612-6a70-37dc-822e-4703463ed13a | -5.76576 | -51.44775 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef0604a-57ce-390f-afd1-acd824f32c8b | -5.76517 | -51.45167 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0281cabd-e30d-341c-9b91-c22029ac0754 | -5.76225 | -51.44722 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c69dfeb7-9597-3b9e-8aff-8d1a3986118e | -5.76165 | -51.45115 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 578ace47-3064-3225-8298-8aed89db7fad | -6.06446 | -51.23674 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f542f415-dd2d-3128-9515-246bf6ec3cd3 | -2.20282 | -51.95516 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fc8bd09-979b-339b-9018-9d04df8880e7 | -2.19946 | -51.95464 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edf2e0ce-2446-3e93-b50d-f57e2610e93b | -2.02399 | -52.63632 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 759e4bdd-1328-3a00-adbf-20f4c9b0765e | -1.94567 | -52.06042 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 889fdc1d-389a-3581-b381-7ac2287844ed | -1.72251 | -52.50811 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98747073-cbc4-32b3-95b9-f6d8d970ce98 | -1.72197 | -52.51158 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c467fe4-ccd1-3e15-af27-e9ac819d2713 | -1.72142 | -52.51504 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 120462eb-f26c-3326-a28a-fb16adfd45e9 | -1.63677 | -52.58303 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe801354-4520-3bd0-98f0-e3005e2c25cb | -1.63399 | -52.57906 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 889bfc50-207e-3ee7-9f25-a7fd9b319bd4 | -1.63345 | -52.58252 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2ef05ab-e501-3577-be87-275f6b3f9fec | -1.32377 | -52.80673 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f3d0e6-f879-39ec-8757-79598e1f76f6 | -1.32323 | -52.81018 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d09b0f4-1b6a-3fc2-b2a4-9e04299f883f | -3.54708 | -53.14693 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50ad28d3-9158-3388-90a6-8f0c777f9834 | -3.54376 | -53.14641 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8b9641-4979-37bf-85fb-57f58a63e70e | -3.54322 | -53.14987 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a8d31a3-81aa-3cf7-8c79-f311d7ddf27b | -3.54211 | -53.01101 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d0d77ac-08a3-3b60-a900-fb3436a0369d | -3.54157 | -53.01447 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 846e56b5-dea6-319e-b4c0-b78c32ba7d0d | -3.41655 | -52.72835 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8d91511-becf-3e0a-9471-82a82b4ad2a7 | -3.33281 | -53.39235 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee6fcf94-2db7-3320-82f4-b9ed370ade85 | -3.33003 | -53.38838 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abf60bc4-8f1e-3d31-8b7f-6bdd9a257a7e | -3.32949 | -53.39183 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 440af500-68ca-358c-b22e-11c9b9aff8a2 | -3.32895 | -53.39528 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aaafeec2-1e98-336b-8da2-62dfa66f239d | -3.32671 | -53.38786 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 205c167c-0bcf-36d9-8bd6-3a4635780c8e | -3.32617 | -53.39132 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8fe8292-03f2-3540-bf51-e5842535cc8a | -3.32562 | -53.39476 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ae09ff3-9c93-3097-9404-57342d624691 | -3.25713 | -52.84262 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| facc64c0-cf65-3c66-91a8-55e3092ccb04 | -3.20592 | -53.14648 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abbcd65f-4844-31d2-ae47-61a089ca4ed1 | -3.04703 | -53.03708 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccfef52d-9781-3265-a229-e6e242eed2e7 | -3.03984 | -53.0395 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d60186f-276b-32bf-8ba6-f9912714f812 | -3.0393 | -53.04295 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 822991f9-cffd-366e-a13c-236b42d07e98 | -3.03876 | -53.04641 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6b3ba5e-855f-3a55-adc0-523833cee702 | -3.03652 | -53.03899 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abeee177-4719-33d4-8971-212d4d0c98aa | -3.03598 | -53.04244 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a74d6dc-cec1-3e9b-8508-282a19954fd4 | -3.03544 | -53.04589 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4dbab1-54dd-31da-8610-d0adcf42dd6f | -3.03211 | -53.04538 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b2cb3b-3a3c-33ae-a453-842d2bb69ce2 | -2.87972 | -52.89733 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53d06fb9-6128-36e3-b8b5-4e24a963e214 | -2.87918 | -52.90078 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc2f5382-0e04-34c7-8867-f2feba4cf4bd | -2.87863 | -52.90425 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0410b4c4-79e3-32af-90be-114dfdedf20b | -2.87809 | -52.90771 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26b4c617-cb82-3540-b3db-a3e79d38db10 | -2.87755 | -52.91116 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97608dc3-5428-3a41-bd7c-31e99c75a8e9 | -2.87585 | -52.90026 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81d48f59-5a6d-36eb-bd30-1a87c83c51ee | -2.87531 | -52.90372 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 904d4cd2-6f48-37d4-99a2-d99ede5ded0d | -2.87477 | -52.90718 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb0f12b0-b076-3c57-823a-46b2d7809a13 | -2.87422 | -52.91064 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cefff115-9dd1-3b75-a69b-8ab694e14da2 | -2.87253 | -52.89975 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e3c7578-98e9-3167-bca4-02deceab1592 | -2.87199 | -52.9032 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 424e0d77-eadc-3fcf-afc3-e36629d4c035 | -2.87144 | -52.90666 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24209243-a814-3c32-9664-272fe43c571d | -2.8709 | -52.91012 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc8c8d77-4540-38cd-b994-c5c4c111e811 | -2.8692 | -52.89922 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87c1869f-4c0d-330e-9a74-293b6826e07b | -2.86866 | -52.90268 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05015695-20c2-3187-b7b0-7ad0689c28ba | -2.86812 | -52.90614 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80cb6678-ec5a-3215-b99e-a62a63f12f9b | -2.86758 | -52.9096 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5153ef4a-2049-342f-8c79-6216b213f16b | -2.86534 | -52.90216 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d3fd8e-11ca-36de-a4c7-8564e2ac0ee7 | -2.8648 | -52.90562 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f750e5a1-d207-3982-b119-ba5303c73a0d | -2.86425 | -52.90908 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README83.md)
