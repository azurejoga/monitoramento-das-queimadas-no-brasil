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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24cd1b09-30a8-357a-9bf7-a3e40786b744 | -4.10627 | -48.51028 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a34d617e-7f43-3938-aedd-5fa876b3ebb1 | -4.10342 | -48.50607 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69d68ccf-3cff-3eb4-b618-df584458322d | -4.05879 | -48.24519 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e70bb41e-a715-30a9-b0ec-d61baa16e113 | -4.03147 | -48.2915 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa2bbb71-ef73-3daa-b060-98f520b2a015 | -3.94581 | -48.34382 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6471050-4cc5-324a-aa10-ded2a96baaa8 | -4.93703 | -48.51376 | 2024-11-03 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf16e19-ae01-39dc-b0d2-eb4a900b91d7 | -4.93358 | -48.51326 | 2024-11-03 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3927be40-7283-3e4b-85db-5da40f09d6e2 | -4.92552 | -48.63509 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce664f4c-aba6-359f-8de0-7b2bf609bd92 | -4.92266 | -48.63081 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bddc5767-2f90-35ae-b5f8-15b6a38a9177 | -4.92266 | -48.53862 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0e8aa24-b645-3745-8506-09cfc94e1a89 | -4.89928 | -48.76059 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00a2c58a-90df-332d-86aa-b5b37126ac49 | -4.89857 | -48.58112 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abe5ce9b-bc93-315b-bbc5-6887198a4935 | -4.8957 | -48.57685 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edba1c41-8e21-39c7-9288-511cf1b15a6f | -4.89513 | -48.58061 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c93bc5cb-9534-38c9-a9eb-882773031f85 | -4.89283 | -48.57254 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e1099c-ba42-3829-b165-f748d44cb760 | -4.88882 | -48.57579 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd91aad5-f9f1-3be8-8814-9c222b2757d6 | -4.8808 | -48.58228 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c24f8a4d-82dd-3a00-93c2-ca8de615fb4e | -4.88023 | -48.58606 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93a40314-866f-3544-8e87-8f0d53474c7c | -4.8792 | -48.66246 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee7c9ac1-9679-3d3d-93d0-083f3052a1e6 | -4.87701 | -48.72305 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 199a4e61-bd28-3d55-8b53-c2452d413b72 | -4.87644 | -48.72676 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fea5990a-5fe8-330a-88c2-70194582142e | -4.87633 | -48.65822 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dfa8fb3-60f8-3803-ae79-d8e4be62a6ea | -4.87218 | -48.56944 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8912974-4def-32ee-9cd8-7abc9938e2a1 | -4.87161 | -48.5732 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313c0b26-493e-3ba6-b7af-d43787d93803 | -4.8693 | -48.56517 | 2024-11-03 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ee33d47-617f-34b1-a92b-f3c04799a87d | -4.82724 | -48.52122 | 2024-11-03 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9f209a3-4d0b-38d5-a8fa-7a87f11d2dbf | -4.82379 | -48.52074 | 2024-11-03 04:46:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 864d0456-0818-3865-9e7b-700127d7ba58 | -4.77751 | -48.68596 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab4134dc-88a2-3e0e-851c-5e95596a9f89 | -4.76202 | -48.96946 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67e86c37-a3fa-33e1-a816-6190e9d4a3d6 | -4.76146 | -48.9731 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cf4fb78-ff52-37b0-b998-c2dcc7aa25b2 | -4.75807 | -48.97258 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7cfc778-bc6e-353a-bfd8-c2fe41f9fa51 | -4.75751 | -48.97622 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a639cf6-1c96-365d-8815-9b5c1fda51de | -4.75464 | -48.58334 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c279126-1d28-3879-b3c6-eba5e937882c | -4.75448 | -48.58315 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27cc5ad7-f22e-3a4a-a4dd-3bf8be2fb62a | -4.75406 | -48.58711 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b648e927-3afe-3f40-a61b-8ea092c2ebeb | -4.75391 | -48.58692 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5590841b-a116-327b-a36e-b9c451388b5f | -4.75062 | -48.58661 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b79c09b-6db1-3320-8647-3a6a2091088b | -4.61572 | -48.64262 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ce7e768-fe7c-3f71-af38-e06fe57c4e2d | -4.60031 | -48.51411 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d3557e-ad3c-3fd8-8414-745cf86a37aa | -4.59973 | -48.51789 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d889f793-a847-3238-b72a-cf1e81b245a9 | -4.52815 | -49.03059 | 2024-11-03 04:46:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d847dac5-f1fa-3199-912a-594b2672cb6f | -4.48301 | -48.45464 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9826207a-9acf-3987-aac5-27f379f07c9f | -4.48014 | -48.45032 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0b1f4ca-f4a2-3799-8911-ef395d7e8ff3 | -4.47957 | -48.45408 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 955e72ee-35c4-39b8-9452-356b2fcc2631 | -4.4767 | -48.44979 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e474d0c-5198-3425-adcf-6ba77324ada8 | -4.08354 | -48.31497 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cac6b6c1-7e70-3b2f-82b5-b1d258ec6ebd | -4.08297 | -48.31874 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d017694a-94fa-3234-b487-8db14bc0acd4 | -4.05937 | -48.24137 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f3c29a-8b0b-35bd-9f69-e9fec130f4d4 | -4.03089 | -48.29524 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1efa00a7-cb59-3b1c-b58f-5b8ec6be42c5 | -4.02802 | -48.29097 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 774e1d3c-6d61-3647-b3d3-24d00e9d2dff | -4.02744 | -48.29474 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7032d8f1-0f8c-3b33-9c24-8f940d75dd54 | -3.94925 | -48.34436 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c8081ad-16e9-33b9-bf18-8513c83bf94f | -4.37203 | -49.11388 | 2024-11-03 04:46:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d18ea58-73e0-3433-b496-a6d5912c79a0 | -4.36921 | -49.10978 | 2024-11-03 04:46:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ddae56-1e48-3606-a93b-35acefe53770 | -4.36866 | -49.11337 | 2024-11-03 04:46:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7eb053f-68fa-38f0-80b4-7f0b1c19a415 | -4.35981 | -48.61922 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24783211-d954-315a-b9ba-ef1a3308ad90 | -4.35639 | -48.61869 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416c7964-5d1d-38ef-ba01-3e38d01afa27 | -4.35526 | -48.62614 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92296098-be5c-39b4-a778-6b63ed67e20d | -4.35469 | -48.62987 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a5ea65a-829c-33aa-a9f1-e89f6db9e60a | -4.29272 | -48.59824 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2e7a990-59bc-3b2c-8317-38dffbcf4f70 | -4.23336 | -48.55116 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb665b8-8acf-3d38-a8a2-d23a849a54e6 | -4.2305 | -48.54692 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7cc72df-43ba-3712-87dd-dd8817a1f066 | -4.22993 | -48.55066 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e6bfacd-0564-31e4-9efd-054cb145873e | -4.10818 | -49.08858 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b11d3e92-fac4-3a93-8ce1-0d8e034ba056 | -4.01226 | -48.9603 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7c7ed51-fc1d-35df-962f-c7be2663bebe | -4.00391 | -49.01431 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6662ab6-0a7d-3ea3-afb3-5822b49e840f | -3.96245 | -49.03727 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db00b644-29b1-3c7d-ac2e-af9bdd12d05a | -3.95125 | -49.04293 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0c4dca8-198f-32cc-85a9-4d1e02e1759d | -3.91228 | -48.92607 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92abe181-8f65-34d9-97d9-9544881ec340 | -3.85171 | -48.98312 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8633d76-4b64-34fa-9ade-e890831dd16e | -3.84208 | -48.95588 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c51f1907-5b49-3d1b-867c-5a743c139f81 | -3.83871 | -48.95535 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f80b09b-377e-3a5f-85ee-1bf68b6a4fc6 | -3.83794 | -48.89246 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94bb3c77-e972-33ce-aa63-a42c06e6096f | -3.83678 | -48.8891 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f10d316-5568-31e8-b31e-2b3cd0e9a396 | -3.83622 | -48.8927 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e647d5d7-65e7-328a-b3b1-9da7f31581c6 | -3.83114 | -48.88087 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31cd2fca-b2ae-3b4e-997f-c235b1cedbca | -3.82946 | -48.89168 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2611c99b-5cc2-3795-abaa-4bc788dfdbbe | -3.82776 | -48.88036 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d1ac3ed-8ed8-3b4d-9f12-b648b6802d1b | -3.8272 | -48.88398 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7acb89-7ae0-369f-9577-45465287d4da | -3.82609 | -48.89117 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e3048f0-68b0-38b0-8682-a95c217916e5 | -3.82501 | -48.96477 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84a11265-ca8d-3249-9fac-19a50989bde5 | -3.82476 | -48.97896 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d8bd492-8a2a-3e50-a0b7-942f60c986a5 | -3.82383 | -48.88346 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cec23d2-c0a5-39c5-92fa-b2f0e1c94bd9 | -3.82327 | -48.88707 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42da5f4f-c849-3be9-9f23-9f0b1563d935 | -3.82277 | -48.97911 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a0f2503-9694-38ed-84c1-538e7486bec4 | -3.82271 | -48.89066 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4ef8d02-f584-3eaa-b5aa-deed243fe7ac | -3.82045 | -48.88295 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db70ccb6-9e0d-318c-8a52-38ddcaaa3a17 | -3.81989 | -48.88655 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca367629-0db6-3dd2-9988-9a80fcf2f22b | -3.8194 | -48.9786 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bcc1630-b0be-3772-b18d-11a936950071 | -3.81933 | -48.89014 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42feea76-7aa1-31c0-bb19-fb034401b865 | -3.81143 | -48.87417 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b480bbb-bd06-35f3-bfe1-28078be9825b | -3.81087 | -48.87778 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb2af5f9-8da5-3088-b872-ec4d21d8340d | -3.81032 | -48.88137 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e045c542-5da9-3b75-a6d9-875ae28f3eb0 | -3.8075 | -48.87725 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbddf115-42df-3b12-832f-415ec0e57bfa | -3.78278 | -48.90302 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54fd0d89-dcbf-346a-a148-5dc550bcd5ea | -3.69196 | -49.05456 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4339c75f-9d1c-3012-9930-4925418beca8 | -4.76452 | -48.00681 | 2024-11-03 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 770ea69d-372c-3961-b3f4-0d122b54b878 | -4.7616 | -48.00231 | 2024-11-03 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbf4a521-5002-3f17-a9d0-8d18c7f8032b | -4.761 | -48.00628 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a33572f5-0f72-3818-8d2d-8cd4e04d3cd3 | -4.75807 | -48.0018 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README42.md)
