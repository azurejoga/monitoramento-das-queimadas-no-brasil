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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beaf659d-8efd-34c5-8a4b-888696db1045 | -3.09506 | -53.72264 | 2024-10-26 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34b0665d-9dc7-3a91-99ea-f55f75d2709a | -3.01377 | -50.4669 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6a996eef-0d12-316e-a777-72c48f504374 | -3.01122 | -50.4847 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ecd8fe33-4af8-3cf2-acae-228102c74b59 | -2.99898 | -50.48296 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5d3fad3b-7b81-36e7-8c3d-beaf049245f6 | -2.98677 | -50.48102 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e3141af8-4188-31d3-9b9b-13ec5c1e3d20 | -2.98032 | -54.62998 | 2024-10-26 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cc9ef4bc-70e7-3dcf-be37-73e6442282ae | -2.96804 | -53.26193 | 2024-10-26 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7fc6cbc1-7d1a-3513-8869-2a89b690aa01 | -2.95504 | -50.41527 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ccfaf3e2-30a4-30c1-90b5-572dae5d380a | -2.95245 | -50.43314 | 2024-10-26 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 15a83529-8836-3b37-9aad-6fa03faeb8fc | -2.94997 | -52.5536 | 2024-10-26 06:03:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cea9f948-cce5-3509-adef-711c50560079 | -2.94809 | -52.56617 | 2024-10-26 06:03:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 07b6ae79-e9a8-3281-adc3-d039a7500944 | -2.94651 | -52.55896 | 2024-10-26 06:03:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 06f019b1-078b-3035-80db-91bd9f6679f0 | -2.94473 | -52.5715 | 2024-10-26 06:03:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 4828bc91-4d32-309b-9eeb-f1bdc8c802ca | -2.87938 | -53.31055 | 2024-10-26 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 2efd85da-fcc3-3faa-b7c1-cd1be2ce86d8 | -2.87778 | -53.3215 | 2024-10-26 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f476ed89-9227-365a-9a9f-16d96395a2a4 | -2.82157 | -49.24385 | 2024-10-26 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1ff444bc-d532-35bb-9e4e-452ae3f6e933 | -2.80192 | -54.09969 | 2024-10-26 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 45a2a14a-ecc1-3b52-89ba-686e85ef09d8 | -2.73174 | -57.46555 | 2024-10-26 06:03:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f917563d-a6ed-3258-aa5b-75ee3ee79ac4 | -2.6818 | -54.02527 | 2024-10-26 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9260e83d-593b-37c3-a532-01eb00d4b459 | -2.56324 | -54.0122 | 2024-10-26 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d42e1402-24d0-3078-b44b-2eed2f9606c8 | -2.37226 | -48.93693 | 2024-10-26 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 98aa4110-f88f-3f45-a150-47d3e245daa0 | -2.20088 | -48.81095 | 2024-10-26 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0d6b31b7-7f2c-3b76-b7cc-7f4a8f36f5f3 | -2.1944 | -48.80485 | 2024-10-26 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 85d7d701-2ae3-35d8-bbc8-be855bd3bf0c | -2.19271 | -53.72163 | 2024-10-26 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 83a0f17c-04eb-3893-ad66-c58f8db4aa0e | -2.03733 | -55.75903 | 2024-10-26 06:03:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aefef424-7601-37bf-922e-7adc34123e3e | -2.03447 | -46.96072 | 2024-10-26 06:03:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 96a54568-0b65-3825-98dd-f90d74107f5d | -1.34992 | -54.60881 | 2024-10-26 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 235d7294-57cb-3cf0-8d03-e5cfb2ca92f8 | -1.06569 | -53.66225 | 2024-10-26 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 84fd3cdf-5d4d-39d5-8b3d-e9767226f478 | -1.0672 | -53.65199 | 2024-10-26 06:03:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32f976b9-7f93-3d10-9b85-0058b0547cce | -1.1807 | -53.89722 | 2024-10-26 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 305e4f62-3577-385c-a3eb-e519f4f21662 | -1.28691 | -55.71737 | 2024-10-26 06:03:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 72083805-2cfe-3a8b-b38c-fb38466f881d | -17.05592 | -57.47813 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 26c7941f-d600-3f8e-b37f-e169015b072f | -16.88886 | -57.67224 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ed271559-d151-373e-a3b7-a4d89b86895c | -17.2308 | -57.20196 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| ae999c3a-b62f-37ff-811a-c168058c97a2 | -16.93973 | -57.71012 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 84607bf0-b632-3f52-a71b-53b8f1687a0a | -17.04876 | -57.39422 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 961a0921-c15b-37d1-83b1-28b8d7b624f7 | -18.25977 | -55.98876 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 78c45f3d-d8a4-3ad1-80d6-7d2c960b2e31 | -18.25812 | -56.00133 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| d75d8f7b-8359-3665-899c-813fd32b0794 | -18.24787 | -55.99991 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| bfba06e8-067b-3bb0-a3ab-71d04b703f34 | -18.1112 | -57.27457 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 4332105b-d3f7-372c-adff-3899c1b60deb | -18.10977 | -57.28519 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b485de09-587d-3cd4-98fd-26af0a3c95d0 | -18.10508 | -57.2789 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 7ef7c182-1602-3720-9820-e0d3bd69ef16 | -18.08615 | -57.27614 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 9a1802ba-3d72-3f72-9305-acaa69de7bbb | -18.07451 | -57.22014 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 58d64aac-0a78-39cf-9a45-cf7497fdaae7 | -18.07445 | -57.36063 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.6 |
| dc56b90a-979a-3f27-bd69-a0c6c5475122 | -18.07299 | -57.37114 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.6 |
| c928c0d6-8d7e-390d-b01f-bc061c347350 | -18.06502 | -57.21876 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fa074966-9531-3b5e-813d-39900e606041 | -18.06357 | -57.36975 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 0eaa9bb9-e8b5-3ddf-9053-ad6a6f0813fb | -18.06356 | -57.22942 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 199b2543-49a1-378c-addb-b7d0a24503cc | -18.03819 | -57.34458 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| e31f96e2-d184-31de-af04-ccfc3e23e8ad | -18.03163 | -57.32211 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 2f752a8c-ceaa-3ae3-b505-ab9888acb070 | -18.0302 | -57.33266 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| a900b282-84d7-31ff-bb31-fcd1e36a1889 | -18.02219 | -57.32073 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 8dc1ce41-37b0-3ba0-82c7-01499d5a47c1 | -18.02076 | -57.33127 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 991d4859-19ca-3724-9ebc-867ae1b1c5ae | -18.01989 | -57.26643 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 41703f5d-700a-3167-bde6-6afd22b2e2b2 | -17.94885 | -57.53753 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 6fe3e42b-1ed2-3344-a686-3b96550ef59a | -17.94732 | -57.54846 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 7ed8bf12-a7e3-3488-8552-78769559e776 | -17.94584 | -57.55902 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| efb6daf2-d5cf-3167-9832-b968abab5807 | -17.9395 | -57.53626 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 6dc49fa3-0934-378b-b91a-3512462785fb | -17.93799 | -57.54708 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| ef8019d5-5d88-356a-a2f8-485b61cb27c2 | -17.93648 | -57.55795 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 4c815c5b-3954-34cf-8171-08b889178349 | -16.90336 | -57.50129 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 0b8927f9-59d9-3b91-8636-d89b845758e9 | -16.91922 | -57.65653 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dd453af3-2085-3ad4-a9c6-8fa6113a4f4a | -17.93508 | -57.56804 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| b7f25d49-6c40-3a05-bbc0-8f36595fde69 | -17.93009 | -57.53544 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| d0b488bb-59f6-3302-bfa2-9c4e9013204b | -17.92865 | -57.54583 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 6bfa7f61-e39c-3ce6-bb8b-4b23ac7b117e | -17.9257 | -57.56716 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 03f4e107-aaa8-3a88-9eb3-736ddfbebbaf | -17.92219 | -57.52372 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 6406559d-4d16-3846-a65c-eda2cddac7e7 | -17.86981 | -57.50905 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 3b3b7037-0d60-349a-a025-a219d2a23980 | -17.86837 | -57.51939 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| bf48dc27-2be7-358f-9888-f52910fd1cee | -17.8582 | -57.59195 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c0afe21b-6486-39c5-87b6-0420c693feb0 | -17.85761 | -57.52828 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e431a0bc-dfc6-358e-bbb5-5a0cd0e00a97 | -17.85681 | -57.60188 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 1637c0a7-6015-3c40-93fe-7e1309e6a2b4 | -17.84616 | -57.61028 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 33085638-fde2-3622-815a-95137d609a42 | -17.84541 | -57.54753 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 3bdd35b5-39cf-30b6-add5-3f104deff820 | -17.81183 | -57.58419 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| cfd7d951-7e81-3a04-bae8-7d0b63af3f14 | -17.81042 | -57.5944 | 2024-10-26 06:08:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fa0e4293-5780-34e1-84b0-f4803ed221fa | -17.23224 | -57.19152 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 581edc5e-ba9f-340e-bf7b-c284560f8754 | -17.85905 | -57.51796 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7f35d5ab-8a85-3431-a570-c938a6afd69c | -17.85257 | -57.49598 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.4 |
| a3d519e9-385e-3c48-a2b5-a5d60081202d | -17.81239 | -57.51105 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 720f8171-e54d-3f5f-a5b0-4ab0310da439 | -17.81098 | -57.52133 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7f91c9b6-b393-38e4-b182-9b8cd44d224d | -17.79197 | -57.34277 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 1b86e4bd-a87f-3489-828e-4d0662016c38 | -17.78537 | -57.59449 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 0fcd72e8-243f-3204-9bc1-3930e7c96d3c | -17.78401 | -57.33092 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 1077b9da-6b6d-3e61-854d-3b2fb8c32f3b | -17.77825 | -57.5099 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9ed3712c-e757-3813-be4b-0dcab8c32da5 | -17.74601 | -57.53652 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 229d7735-01cd-38b8-9592-320b9b0a1d73 | -17.74459 | -57.54676 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 03e4c643-0811-3edc-902b-e8ca2edbaaea | -17.73669 | -57.53514 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 81d426be-76ed-360f-92ea-00219182300e | -17.73386 | -57.5556 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 3007300f-8d18-3107-8cec-be76cb4cd17a | -17.7237 | -57.49133 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 2e1151ee-28d2-34b1-9afb-358cd00379b1 | -17.69914 | -57.48192 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5d1a432c-4f61-3a78-84f4-e6999440441d | -17.68981 | -57.48054 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 22b03029-3ed6-3930-af3b-c59bcc2b159d | -17.68048 | -57.47916 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| c84c8426-ed87-359f-95aa-23e8a9faae6b | -17.66182 | -57.4764 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a94a7f16-0c41-396b-ad7b-03f43efb0084 | -17.26119 | -57.2595 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 1041909c-893a-343f-915c-4b478e8e1293 | -17.25325 | -57.49542 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| b91f43ae-ff1d-34ad-ac7d-ebb5b6fd859f | -17.24814 | -57.48797 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| adbcac67-8709-372e-8f16-363d8e18d369 | -17.07524 | -57.40852 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 25699a07-f06c-3fc9-888e-72d92af6eb02 | -17.20204 | -57.27198 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |


[Clique aqui para ver as próximas entradas](README103.md)
