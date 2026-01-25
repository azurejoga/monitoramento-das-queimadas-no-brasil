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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f46dd5d-e480-307e-96ce-3941cb48e36b | -19.6156 | -57.2944 | 2026-01-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 252e2cd9-503b-3c2e-adc7-50f156a2f9c6 | -19.6357 | -57.2917 | 2026-01-25 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 125a5234-8ff1-3abc-bdbb-7e3226f22a1a | -19.6156 | -57.2944 | 2026-01-25 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 7bd3b1ed-818f-3f9c-a537-5b30680e609f | -19.6357 | -57.2917 | 2026-01-25 09:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| ab866d8b-681b-3dc1-a379-9c88109b1517 | -19.6156 | -57.2944 | 2026-01-25 10:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| fb1a428b-bf12-3288-b3df-a7e85883d223 | -19.6156 | -57.2944 | 2026-01-25 11:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.8 |
| 1f177ead-7bf2-3f3b-9ad9-7e51990dcc22 | -19.6156 | -57.2944 | 2026-01-25 11:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.2 |
| db3fa842-9525-3a98-aa17-26c173366a96 | -19.6156 | -57.2944 | 2026-01-25 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| d3749c38-e7d0-3b15-99d4-7c7327f8f456 | -7.33316 | -44.25692 | 2026-01-25 12:33:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d612dd93-d234-3878-bfdd-f870fe8c3737 | -7.32651 | -44.24958 | 2026-01-25 12:33:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b4e86376-a934-386a-97c9-e485fc54fb95 | -19.28276 | -52.39969 | 2026-01-25 12:38:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e3cf254-6cf3-3c10-acb2-a80ef1b9837c | -21.47271 | -49.21957 | 2026-01-25 12:38:00 | TERRA_M-T | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 2a51bc4d-0c67-3c8b-a1a1-47cbb360a38a | -19.1861 | -52.35487 | 2026-01-25 12:38:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d527c65d-a8bf-30d5-86e3-e25ee675e19b | -22.96077 | -54.5041 | 2026-01-25 12:38:00 | TERRA_M-T | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 0b577ba5-0a97-3078-bc50-8fbe6e8c9785 | -19.65578 | -57.24606 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9e0bbbc8-f669-31b8-8c6b-ddbf0e672155 | -19.6294 | -57.29414 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 6950305e-7f9d-3ab4-b8b5-9b87e7a42b6f | -22.9622 | -54.49288 | 2026-01-25 12:38:00 | TERRA_M-T | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| bb4bcf35-1985-313b-af3c-dece2a8a93d2 | -19.62048 | -57.29269 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| e6081e59-f20d-3e07-974f-06a9990bd3dd | -20.32497 | -57.82909 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 4ae150c1-ea92-324e-8d6f-afdaa78accad | -19.65437 | -57.25555 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.3 |
| e0a70808-8724-338c-8a9f-341043f503c5 | -18.79947 | -57.66138 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| eee5c4d0-7ee7-3b5b-a28a-c6a7dc9ffe73 | -19.62659 | -57.31318 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| f7b3d4f6-3f5c-3589-8167-69820b3c62aa | -18.81979 | -51.60323 | 2026-01-25 12:38:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cb212fd8-1dd7-3c49-a6bb-131fa4eb4ff6 | -19.95337 | -54.39791 | 2026-01-25 12:38:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 40af2c6e-1d63-3487-8b5e-63568e786536 | -21.15857 | -55.82213 | 2026-01-25 12:38:00 | TERRA_M-T | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 01308a0b-2a4b-3656-807d-a45e698a7960 | -19.628 | -57.30365 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 4924ab23-14fc-3bbc-94fc-17e5f7d69741 | -19.28438 | -52.38656 | 2026-01-25 12:38:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d33d3d85-837d-33ad-a4c0-0cf3ebd83143 | -20.33398 | -57.83059 | 2026-01-25 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b53ea1c9-4a05-3c63-a868-599593901880 | -27.86412 | -51.07841 | 2026-01-25 12:40:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 6f805aa3-eb04-326e-84d8-8c5248266a1e | -27.86618 | -51.0556 | 2026-01-25 12:40:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 4f6609f7-655f-3dbc-b7ee-3f4e0eb65ebf | -27.80776 | -51.13353 | 2026-01-25 12:40:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 814618ff-306c-3746-a2d8-bd36e95ed568 | -28.51051 | -50.93602 | 2026-01-25 12:40:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 3ea7dac1-3df7-3ac4-aa57-2bf4f91252f4 | -28.97523 | -51.06725 | 2026-01-25 12:40:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 1515c34a-4f8f-3949-9f4a-d79483419b34 | -29.64008 | -51.00031 | 2026-01-25 12:40:00 | TERRA_M-T | SAPIRANGA | RIO GRANDE DO SUL | Brasil | 4319901 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| f7a692b5-be6c-39d5-8c7a-e7ec445eed7f | -25.77387 | -53.52664 | 2026-01-25 12:40:00 | TERRA_M-T | REALEZA | PARANÁ | Brasil | 4121406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 17dc6915-861a-3a27-9977-3ed3a74cdf01 | -29.22523 | -51.3416 | 2026-01-25 12:40:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 4d33edbd-67e7-3916-8314-24d4b9633974 | -20.3294 | -57.8224 | 2026-01-25 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| ea8d0a29-9b76-368d-875c-f93422176c60 | -20.3294 | -57.8224 | 2026-01-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 7415e0c2-2171-3a14-a40d-99ae792a255e | -20.3497 | -57.8197 | 2026-01-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 1bf4e952-d0a3-3dce-9145-206ac5e235fd | -20.3291 | -57.8433 | 2026-01-25 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |
| c9f6de39-bc91-3a63-998f-2b431581f41a | -20.3497 | -57.8197 | 2026-01-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 10f931e3-a66a-3a02-a8fb-0968512e553e | -5.4881 | -37.6708 | 2026-01-25 13:10:00 | GOES-19 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 5c526ccf-76c1-3647-9e32-fe0989f5ad2f | -20.3291 | -57.8433 | 2026-01-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 3cc1ffc6-9ca5-36eb-805f-caa081f7eb04 | -20.3493 | -57.8406 | 2026-01-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| dcd8d111-782c-3795-aa2e-e98b78b29e6f | -20.3294 | -57.8224 | 2026-01-25 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 5eecf2cf-995d-3d98-8209-da31a065602d | -20.3294 | -57.8224 | 2026-01-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| f89a8679-2860-3f9c-8814-eb30c3f8afa6 | -20.3291 | -57.8433 | 2026-01-25 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 12163bba-8951-33df-94e3-6c790c8dcfac | -5.4881 | -37.6708 | 2026-01-25 13:20:00 | GOES-19 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 122.5 |
| c34d83a4-b5bf-332b-9675-5b5e51255989 | -20.3294 | -57.8224 | 2026-01-25 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 1acf854a-4de2-3cc8-bd2c-81a0b8822b5f | -20.3493 | -57.8406 | 2026-01-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| c7f38704-6833-32fc-9b72-07374e9cea4a | -20.3294 | -57.8224 | 2026-01-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.4 |
| c369702c-c8f8-323c-9a21-7bf77b23748b | -20.3291 | -57.8433 | 2026-01-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.9 |
| f26c02f9-3b1d-3f1a-912b-aea26444d7b9 | -20.3497 | -57.8197 | 2026-01-25 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 6a382a88-725e-32e1-a642-15f41b0bbadf | -20.3294 | -57.8224 | 2026-01-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 3405a156-1a9f-3ce6-8c64-0451d7e782b8 | -20.3291 | -57.8433 | 2026-01-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| f6988e84-7647-37e6-b7f5-31aef1d3c2d2 | -20.3497 | -57.8197 | 2026-01-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| f824b153-e1bd-31c2-962e-6ffa18cbe2bd | -20.3493 | -57.8406 | 2026-01-25 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| f358ddd6-e954-3e85-81e8-a4b538e6684a | -20.3493 | -57.8406 | 2026-01-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 24c0d925-b398-343e-af98-2da8a02fb0da | -19.6418 | -56.9569 | 2026-01-25 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 01a2faf2-0f45-353f-9700-69a3423e5dc4 | -19.6627 | -56.9122 | 2026-01-25 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 635d0695-160f-3369-9d2e-3640274bca32 | -19.6623 | -56.9331 | 2026-01-25 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 4e3e5cfd-c27c-3c8f-9157-66dd796f6320 | -20.3294 | -57.8224 | 2026-01-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.3 |
| aa4131f7-509b-33ff-92a2-671c0ca4725b | -20.3291 | -57.8433 | 2026-01-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 896b4150-69a5-370c-91f5-6a55f91ffc66 | -20.3493 | -57.8406 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| fbb7f246-6713-3968-be1f-a352737c9a2f | -19.6623 | -56.9331 | 2026-01-25 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 96256890-03aa-300c-8367-f61efeeb8316 | -19.6353 | -57.3126 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 249.3 |
| c0dafaef-9a3e-38ee-9c97-add676c59201 | -19.6627 | -56.9122 | 2026-01-25 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.4 |
| bd040ca2-7b7b-361a-b0bd-e18963267e60 | -20.3497 | -57.8197 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| fd8eed20-4248-3ebc-9e1e-1f52cf61c724 | -20.3291 | -57.8433 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.8 |
| 93f8173f-6e38-3fe9-a65b-2c01402577c2 | -19.6357 | -57.2917 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.7 |
| 10272c17-dc4a-3d6e-a0b4-51ab51858ecf | -20.3294 | -57.8224 | 2026-01-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.2 |
| fd201dd6-66f2-3f70-852b-0e85c6b2aa30 | -20.3497 | -57.8197 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 0595967b-e5e5-3549-985d-a0a3f36ddc7c | -19.6156 | -57.2944 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| f58d1a23-bf54-3577-87c4-a6a78a0ebe05 | -19.6836 | -56.8674 | 2026-01-25 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 42b5d977-5f21-33be-9e3d-9cfd9e38e1d0 | -19.6353 | -57.3126 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 195.8 |
| 1259e594-e0aa-39b1-8668-bce0c377c685 | -20.3291 | -57.8433 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| cabc2cc6-fe16-3da6-bb1e-857877310ccf | -19.684 | -56.8464 | 2026-01-25 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| caffb128-3402-38ea-a363-bf6b33ecc38e | -19.6631 | -56.8912 | 2026-01-25 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 5b5391f9-931b-34c2-9748-065e45f224cf | -20.3493 | -57.8406 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| c2ae8024-4354-373d-89dd-a3f020809986 | -19.6357 | -57.2917 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.0 |
| ef88690c-0c3c-32a5-b4e6-820e6154e020 | -20.3294 | -57.8224 | 2026-01-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 90cf1458-56ac-33b4-ae15-ed544bf3b8dd | -19.6635 | -56.8702 | 2026-01-25 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 60d3ad49-5da2-31e4-b6b5-8a9095054ee1 | -19.684 | -56.8464 | 2026-01-25 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 81ca64c4-9bf8-3226-83f2-c00c094bedfb | -20.3497 | -57.8197 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 494b60b5-7d4c-3c45-aa98-ec5b0573c24c | -19.7041 | -56.8436 | 2026-01-25 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| bb32ad91-5824-3c95-9ed4-e6806108d6ce | -20.3897 | -57.8351 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| dec25af1-e272-3738-b9ba-2aca6db59b3e | -19.6357 | -57.2917 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.0 |
| 94392905-f70c-3b62-a098-9319273353d6 | -20.3294 | -57.8224 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.7 |
| 7aa59328-454d-3678-880c-69930fb67f2e | -19.6353 | -57.3126 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 237.2 |
| 9753d583-bd6b-35d9-b366-619e53a9ab15 | -19.6156 | -57.2944 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 00fb7d65-1aa5-37e6-84ca-b74f7454a8fe | -20.3291 | -57.8433 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 06ca7540-3a64-3b72-889a-47dd417e116a | -20.3493 | -57.8406 | 2026-01-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.9 |
| c186d4d3-8e3b-37f1-9c66-1732f76e4019 | -20.3493 | -57.8406 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 0b66e932-bb32-3260-a894-dfb2500142dc | -20.3092 | -57.8252 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| db5d6bd0-81e4-32c5-80b8-59b72aa80bf9 | -19.6357 | -57.2917 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.2 |
| 6a3d1e10-3fe6-3958-a620-d574a845ab3e | -19.6156 | -57.2944 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 0dae53e6-d187-383d-a07d-cd4783dfb725 | -20.3088 | -57.8461 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| db2faf65-b4ef-3b90-ad30-af0cf4fc0b1e | -18.7908 | -57.6726 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 5bc4a098-25e1-31ca-8b6f-71b0cd19b8f4 | -19.682 | -56.9513 | 2026-01-25 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 865cc2b4-df7a-35ef-ab70-06ad04c270bf | -18.7912 | -57.6519 | 2026-01-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |


[Clique aqui para ver as próximas entradas](README10.md)
