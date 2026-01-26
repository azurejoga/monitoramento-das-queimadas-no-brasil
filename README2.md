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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e24c3d90-1062-3e11-965b-3589627bde50 | -18.8499 | -57.7064 | 2026-01-26 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.0 |
| acc26e14-abf9-3b82-9872-8e8057b62239 | -18.8296 | -57.7296 | 2026-01-26 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 8541e268-d392-3812-8740-cfc26a2385f8 | -6.2083 | -39.2848 | 2026-01-26 01:00:00 | GOES-19 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 2c5d7cac-060a-3176-8e39-e951cf459569 | -6.2163 | -35.2573 | 2026-01-26 01:10:00 | GOES-19 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| 087235a9-bdc0-3025-86f6-443dabcba941 | -19.7238 | -56.8618 | 2026-01-26 01:10:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 4ece6ba5-c002-383a-addd-f07f7839a1c5 | -6.1975 | -35.2321 | 2026-01-26 01:10:00 | GOES-19 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| a7f61d61-2eaa-3167-955e-4449c35eece3 | -6.1972 | -35.2595 | 2026-01-26 01:10:00 | GOES-19 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 168.1 |
| 3a0cacbf-e25e-3a84-a656-0f4abf310d3e | -18.8495 | -57.7271 | 2026-01-26 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 516d38c8-5bfc-3c01-a883-22bb7f9abae3 | -19.7037 | -56.8646 | 2026-01-26 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 2c52b670-3b14-3776-b517-7294ac247e43 | -20.3294 | -57.8224 | 2026-01-26 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 38bc26db-eef6-339a-90d1-682c7167ff3f | -19.7041 | -56.8436 | 2026-01-26 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 056fa850-b223-33e4-aa6c-4a0bb9d39d0b | -19.7238 | -56.8618 | 2026-01-26 01:20:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 8acecbe0-a63e-34e7-a469-459d831eeb6b | -19.7242 | -56.8408 | 2026-01-26 01:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 918fb346-f516-39b7-853e-f743bae07dde | -19.7238 | -56.8618 | 2026-01-26 01:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| eba1e59b-ce05-3acc-ad9f-4c05a65af905 | -19.6554 | -57.3099 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 0096b4e3-bf0b-3de0-81bb-8ba45ce6a82b | -19.7037 | -56.8646 | 2026-01-26 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| d9398ab5-339e-3aa0-951d-8bc9eaec89d6 | -20.3294 | -57.8224 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| a2ba79e8-3d58-314c-8402-278b40390d5a | -19.6546 | -57.3516 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 8ebd9277-aa72-31d9-bfb0-c906853fdc2b | -19.6345 | -57.3544 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 55c3041c-e713-36ed-9216-3769db34f251 | -19.7041 | -56.8436 | 2026-01-26 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| be53ab61-a441-3d5a-9b0c-4c92de480d18 | -20.3298 | -57.8015 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 49c4aaa2-8e6c-3419-bb1f-d88a56e78dce | -19.6557 | -57.289 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.6 |
| 70d04bd5-9848-32f7-8106-a3fa60106543 | -19.6758 | -57.2862 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 3a807167-7966-36e2-9bfd-07b651b1d7da | -19.655 | -57.3307 | 2026-01-26 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| d061b40b-7834-39ae-b841-4e827fd47e8a | -19.7242 | -56.8408 | 2026-01-26 01:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.6 |
| d84e754e-bb31-3c69-a003-f38a4ce68041 | -19.7045 | -56.8226 | 2026-01-26 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| d79c8191-1aa3-355f-b5f4-3c9f813ca6f8 | -19.6557 | -57.289 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.5 |
| 2d7c4641-9b9f-3272-9a91-dfd6eff6b03f | -19.6349 | -57.3335 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 77622ea7-45d5-3d4a-8c19-96771dc30057 | -19.655 | -57.3307 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.9 |
| 7bc0111d-af28-3848-a279-ff90b5f34f12 | -19.6345 | -57.3544 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| c946c401-a5fc-38ec-a7bb-4fbc10ea0ba2 | -19.6554 | -57.3099 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.5 |
| cf207a29-6eee-35e1-9fc6-d8bbfe80e5e7 | -19.7037 | -56.8646 | 2026-01-26 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 6e760f56-72fe-37a0-9866-6a7248ac4c5b | -19.7041 | -56.8436 | 2026-01-26 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 179.2 |
| 6cd5d54a-8b38-3c13-98e0-935b17710d92 | -19.6546 | -57.3516 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 7c6a4613-8322-3be2-a542-674253698b3d | -19.7242 | -56.8408 | 2026-01-26 01:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 191.8 |
| 1c9b58c4-82d3-391e-8136-55d33cf2be8b | -18.8495 | -57.7271 | 2026-01-26 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| d2d4d634-cbfb-393a-90f5-cfd645c81271 | -19.7238 | -56.8618 | 2026-01-26 01:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 124.3 |
| a26475c0-b123-35f8-bb95-403e9872a342 | -19.7242 | -56.8408 | 2026-01-26 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 242.0 |
| 1e24bcc7-5700-3edb-bff3-3339164976c5 | -19.7238 | -56.8618 | 2026-01-26 01:50:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| ba9268e3-f6e5-38fb-bf50-4fc5f53a0451 | -19.6546 | -57.3516 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.7 |
| 07091d4a-ff09-3a7a-b96f-917ac50fc1f9 | -19.6349 | -57.3335 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| fac731e5-e4e6-3d1a-93fd-736ec7f92a0b | -19.7037 | -56.8646 | 2026-01-26 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| e30c7755-d580-32cc-b699-d5e5e0f857ae | -19.6345 | -57.3544 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 66eda1d6-879c-3e7a-887a-bb2354f3aeff | -19.7041 | -56.8436 | 2026-01-26 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 168.1 |
| 66ecce46-9db1-3a8c-8d1b-dc04e129c5ba | -19.6554 | -57.3099 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 03e1d847-b8ff-3569-bbd9-4996eb01355b | -19.655 | -57.3307 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 33a7a457-58ac-3090-951c-66c980d0d43c | -19.6751 | -57.328 | 2026-01-26 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 41ffb537-d01b-33ea-9fab-3b588e322be3 | -19.7045 | -56.8226 | 2026-01-26 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| eb44429c-e304-3fc9-b636-4ca68353d65f | -19.7246 | -56.8198 | 2026-01-26 01:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| aa5245c4-4412-32af-9985-78b5ff9fb922 | -19.6554 | -57.3099 | 2026-01-26 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 174a672f-73d4-3b48-8c08-a026ed451325 | -19.6349 | -57.3335 | 2026-01-26 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 0949d3ca-409c-3316-a1a1-0070d4ced29d | -19.7238 | -56.8618 | 2026-01-26 02:00:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 6860e63c-f2cd-3962-a4e3-82ac21a12033 | -19.6345 | -57.3544 | 2026-01-26 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 8c8377b8-6abe-3f5c-aefa-e8a8a4b61cbb | -19.655 | -57.3307 | 2026-01-26 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| a310a851-f906-3fe1-962b-e52afa2ba82f | -19.7242 | -56.8408 | 2026-01-26 02:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 255d0557-e782-31c2-9df9-68c21e53e25e | -19.6546 | -57.3516 | 2026-01-26 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 3ed011bd-fc0e-3367-9d11-d2029352a937 | -19.6554 | -57.3099 | 2026-01-26 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| f22f6dca-e927-367d-8786-cf9a375a59d4 | -19.6345 | -57.3544 | 2026-01-26 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 5efb8277-37c6-3a1b-bc3a-1991a24d0257 | -19.655 | -57.3307 | 2026-01-26 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 2613c29e-2c44-3784-a953-c81cb35890a2 | -19.6349 | -57.3335 | 2026-01-26 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 1f5bbbbd-0ced-340b-8774-e8116105a7df | -19.6546 | -57.3516 | 2026-01-26 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| eebfc79c-e641-39d2-8a64-4b0d82e3cc43 | -19.6345 | -57.3544 | 2026-01-26 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 96d32089-7aa1-3be2-a6b9-308eeeb3113a | -19.6546 | -57.3516 | 2026-01-26 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 55f63481-8365-3252-b7e2-8a0dd108efd3 | -19.6554 | -57.3099 | 2026-01-26 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 93233f40-1078-3fe5-b22b-f1754ea15b0a | -19.655 | -57.3307 | 2026-01-26 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 7fadd893-ce68-393a-bcb0-3d7e000c48e0 | -19.6345 | -57.3544 | 2026-01-26 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 366cc5e0-85c3-345d-b5c1-81f1da9853da | -19.6546 | -57.3516 | 2026-01-26 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 87671d1d-2f13-3631-a3dc-9f1288d305de | -19.655 | -57.3307 | 2026-01-26 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 7c34792f-f047-391d-bfba-8e3360337b31 | -19.6546 | -57.3516 | 2026-01-26 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 51fc1500-96dd-32f3-86ff-4ad346f6bd19 | -19.6546 | -57.3516 | 2026-01-26 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 8febb6fc-0fae-37b6-abb1-18fb0fe74a37 | -19.6546 | -57.3516 | 2026-01-26 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.8 |
| f4ec4856-eb86-3fcc-980e-6a55d9dae5d5 | -19.7037 | -56.8646 | 2026-01-26 03:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 53d473f3-49ff-334e-a935-41970ce59dee | -19.655 | -57.3307 | 2026-01-26 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| ba1c03fc-5fac-3afe-b04e-76ce88a7121f | -19.6546 | -57.3516 | 2026-01-26 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| e20f72b2-9704-31e7-b990-cefd50c0c4d4 | -5.58298 | -35.60876 | 2026-01-26 03:17:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31091194-cddc-3004-8de1-947bf3b55498 | -6.73249 | -35.20932 | 2026-01-26 03:17:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ac9185a7-2419-3e64-bb0e-a754252e678d | -6.37316 | -37.37933 | 2026-01-26 03:17:00 | NPP-375D | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83018159-c194-3782-bde3-49e9c47b1fed | -6.73637 | -35.21584 | 2026-01-26 03:17:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a0e327d6-6819-334a-bf18-5ab8d2efbb82 | -5.58248 | -35.61171 | 2026-01-26 03:17:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 877977a9-ac85-3df7-a411-2ade25dd6f23 | -5.18035 | -35.86014 | 2026-01-26 03:17:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e1bd14b-4451-3c9b-82e3-f921da3cd5da | -6.7373 | -35.21043 | 2026-01-26 03:17:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9b853293-af83-3477-b723-829376178f6a | -9.09653 | -35.36613 | 2026-01-26 03:17:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1834c245-84d6-3129-b624-7a4114c3b35c | -5.17513 | -35.85927 | 2026-01-26 03:17:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d13b4b6-90c7-3ae3-bb0e-bac881538ae5 | -10.00425 | -36.48665 | 2026-01-26 03:19:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba6445a6-a795-3523-9f4c-ea0ef97a931b | -10.00141 | -36.47414 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8ed9614d-5be1-371b-8be8-71ef1ef49a2f | -10.0053 | -36.48101 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d704d080-88da-3772-9255-71822ac7e410 | -9.595 | -36.62103 | 2026-01-26 03:19:00 | NPP-375D | COITÉ DO NÓIA | ALAGOAS | Brasil | 2702009 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3debcee-af7a-3a36-a29f-b1ecd9aa3019 | -10.00106 | -36.47903 | 2026-01-26 03:19:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6760b2bd-4056-3e22-b1f6-7c9db34690d3 | -9.96461 | -36.78382 | 2026-01-26 03:19:00 | NPP-375D | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5637b200-124e-34e7-ab77-08e29b9106f1 | -9.96517 | -36.78083 | 2026-01-26 03:19:00 | NPP-375D | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 70cc2e19-bbdd-3037-ac4b-810cc79a99f3 | -10.0064 | -36.47508 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e807af44-d66d-3d46-ae64-f10eddc0eb45 | -10.01032 | -36.48185 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51c6a559-1a94-3a19-bace-78f8049323bc | -10.00032 | -36.47998 | 2026-01-26 03:19:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6618e9f-e02e-3b1b-910f-e298ca9a86e5 | -10.01142 | -36.47595 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89e22b94-db49-38cb-bdbc-412fb1f3c97b | -10.00212 | -36.47309 | 2026-01-26 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37a3ebec-53cc-3464-a63b-8aea30de0bc1 | -19.6546 | -57.3516 | 2026-01-26 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 61e9d636-b904-3b89-be5e-e1bb16246daf | -19.7041 | -56.8436 | 2026-01-26 03:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 4a021133-fff2-3801-b23a-e0f51870ef93 | -19.7242 | -56.8408 | 2026-01-26 03:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 6f3ec06e-c207-3500-bdef-f87775bbf087 | -19.7045 | -56.8226 | 2026-01-26 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| f5bcee30-76b2-3ac1-bd66-7a718c8e711a | -19.6546 | -57.3516 | 2026-01-26 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |


[Clique aqui para ver as próximas entradas](README3.md)
