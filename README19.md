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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7a9c011-cd4f-3a37-9c52-ea07c1e723e2 | -11.5495 | -44.2876 | 2025-07-31 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 425.7 |
| 3d3eea42-4f9e-3dbc-812a-345ee1d3de53 | -6.6725 | -56.4029 | 2025-07-31 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 600e867a-8240-3b10-b418-6adb171ffa6a | -11.5307 | -44.267 | 2025-07-31 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 7717ada7-5f42-3b78-bf09-58f899493986 | -11.5307 | -44.267 | 2025-07-31 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| bb2282dc-c129-3fd3-b68b-fcee8df926e3 | -11.5495 | -44.2876 | 2025-07-31 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| f1aa508b-a01d-38fc-a8a5-704f33e3ba39 | -11.5303 | -44.2904 | 2025-07-31 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 154cd8b0-6444-34b3-b6a7-9c517ca43c30 | -10.6165 | -45.2742 | 2025-07-31 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 99eae322-8517-3084-aa08-5ece437ad2c5 | -11.5499 | -44.2641 | 2025-07-31 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 8c3ba8a0-40d0-3bec-8875-1fa6d0837686 | -9.7936 | -47.0226 | 2025-07-31 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6eaca428-3696-3ba7-a8c5-3a1613dee93d | -6.6725 | -56.4029 | 2025-07-31 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| aad90f92-7edb-3a6a-b539-6c762f9e991e | -10.6169 | -45.2512 | 2025-07-31 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a613a784-9223-31b1-bdb3-2e4a84af6a13 | -10.4534 | -47.2356 | 2025-07-31 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 664e86f4-a567-356e-8b5f-cb5e8f54687d | -10.636 | -45.2487 | 2025-07-31 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c91197ea-3e06-3ddf-a3ae-e3c3678fa29d | -10.6169 | -45.2512 | 2025-07-31 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| b31a54a1-fa74-3fdc-a987-5fced4b0138b | -10.4344 | -47.2378 | 2025-07-31 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ed661c92-0bf0-383e-9984-5542c8f491e4 | -11.5495 | -44.2876 | 2025-07-31 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| bcf75411-d83f-3fca-a646-c2dee54ae8a1 | -10.4534 | -47.2356 | 2025-07-31 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 394d8627-00c1-3197-b711-7b859dad79f4 | -11.5303 | -44.2904 | 2025-07-31 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| d6bcaf88-bca7-3753-9b3b-77e763a7b80a | -10.636 | -45.2487 | 2025-07-31 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ace4b432-5c3b-3f15-997b-123bf7d3463d | -6.6725 | -56.4029 | 2025-07-31 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f804aedc-2168-30db-a698-c316d01756dc | -11.5307 | -44.267 | 2025-07-31 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5ed906db-b177-333f-96a2-0fcabb1e79b2 | -10.6165 | -45.2742 | 2025-07-31 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| ead2ea11-9942-3496-8688-9fca69e252d1 | -10.6169 | -45.2512 | 2025-07-31 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 3f1d8235-1080-3754-9720-176863cf99e0 | -10.6165 | -45.2742 | 2025-07-31 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 83bd9039-24be-39ba-81d2-3971e1adce98 | -6.6725 | -56.4029 | 2025-07-31 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7e639ad2-5b6e-3c83-8a68-6ee43e1a8075 | -11.5303 | -44.2904 | 2025-07-31 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 170074ea-e462-3d1f-8b98-4bff4ea471b1 | -10.4344 | -47.2378 | 2025-07-31 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 9ab0b96c-2f04-3adb-a627-f01787215847 | -11.5499 | -44.2641 | 2025-07-31 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| b243728a-c890-3feb-ab71-0aa58901e348 | -10.4534 | -47.2356 | 2025-07-31 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 364.5 |
| dac29da0-e62c-3a55-abac-b86f1c4f9295 | -11.5495 | -44.2876 | 2025-07-31 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 246.9 |
| b85e0807-7a41-303e-987c-e4cd5cb06669 | -11.5307 | -44.267 | 2025-07-31 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 185525ce-7144-3968-ac1c-ce2c14d86c41 | -10.6165 | -45.2742 | 2025-07-31 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 222.2 |
| f768951e-d1e5-305d-acb8-3ea35f622618 | -11.5499 | -44.2641 | 2025-07-31 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 94d87190-e53c-331e-b9d5-bfd91a8c1f86 | -6.5075 | -56.1932 | 2025-07-31 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5a9da616-1431-3909-95e5-d42b88a01864 | -10.6169 | -45.2512 | 2025-07-31 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ab80140f-1e6b-38a6-aca6-338a99d4e20f | -11.6434 | -50.1976 | 2025-07-31 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9b15a290-9847-38b3-8d93-dd86501a232d | -10.4344 | -47.2378 | 2025-07-31 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 60405ff8-aa36-3583-94de-e70f21c6020f | -11.5307 | -44.267 | 2025-07-31 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 171d2c15-084c-39c1-86ec-b26863ad965c | -6.526 | -56.1923 | 2025-07-31 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7374c111-5473-3f6d-a665-aab4aec1f7c7 | -10.4537 | -47.2133 | 2025-07-31 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e1c69082-3206-372f-b9b0-bb5e71b03e4b | -6.6725 | -56.4029 | 2025-07-31 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 1a86985e-900e-3eae-a94d-62298efc8d04 | -11.5303 | -44.2904 | 2025-07-31 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| b9963c2c-ae04-3ea8-8720-38874b1a013e | -10.4534 | -47.2356 | 2025-07-31 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 486.7 |


