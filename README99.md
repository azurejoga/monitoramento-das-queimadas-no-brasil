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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abf0209e-b533-308a-bfb1-42c20393192c | -11.23563 | -46.62001 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85db1908-0000-37d7-9148-3b76453def88 | -11.23472 | -46.98591 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b844134e-35c4-3d5b-9165-528f09f84656 | -11.23409 | -46.9903 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5774c19b-5ad0-3b12-b1ae-54f2f83bd823 | -11.23106 | -46.98534 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e3fef449-20f6-3b04-99ed-e9a5e17ddf03 | -11.18888 | -46.99371 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5f7d9c6-cfd5-36ab-afda-9ec2b67f3e44 | -11.17641 | -46.92495 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0de3c5d-eca0-3153-9749-2b58d97c66d0 | -13.60358 | -48.12744 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84df489c-3a63-3ccf-9a35-bf3e55087a2e | -13.60295 | -48.13175 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f41f6c97-b912-3f49-b2ba-aeab59993bbe | -13.60233 | -48.13608 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b65da39-a4e1-3a11-a37e-8dcbf4744bc3 | -13.59464 | -48.13902 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 992da4da-8928-367d-b852-8e34cdcb5d50 | -13.5917 | -48.13423 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c995cf0-59e0-3a86-94a5-b5e9a5cf2896 | -13.5911 | -48.1384 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 581b9960-1fc8-38d9-8ad7-ba5540bcaf77 | -13.58817 | -48.13354 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2a6e655-bcdb-3f1a-9a4b-6fa0a7784aed | -13.39261 | -48.08899 | 2024-10-05 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d1a0e2e-c80b-3f34-836e-7b8614331996 | -13.29369 | -47.92459 | 2024-10-05 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c25120c-7af5-3b88-9e30-587523141ef7 | -13.29011 | -47.92413 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf5b5872-8550-3bca-b65a-dbe74e93879c | -12.85255 | -47.4615 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc619503-6897-3b2b-8c44-46de0ad4fdd6 | -12.84277 | -47.47763 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee93958b-5257-3ffc-9a49-9cbb7e1941c6 | -12.83851 | -47.48138 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41b1183a-d826-3815-a988-787ea03fbc00 | -12.83789 | -47.48568 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 755ebf09-2184-3310-8258-493af38f0c9e | -12.8355 | -47.47653 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88f609e9-4bb6-3653-9bfd-6a4a0398b7dc | -12.82822 | -47.47543 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e007e1e-e5a2-3767-8341-59b516cc27fa | -12.78116 | -47.43921 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af2b3bb5-4b2c-3fa5-a52a-1c2d88975d04 | -12.85192 | -47.46581 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49a86aa5-1f05-333a-9199-15f72bfecc44 | -12.84215 | -47.48192 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23b4fd33-004c-3eee-b2b1-ba299905e4a9 | -12.83913 | -47.47708 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 505eb945-ac55-31dc-a1c6-aeb3fcdba72e | -12.83488 | -47.48083 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1237513a-4ac5-3c8c-96dd-de2305283eee | -12.8252 | -47.47056 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43f639ae-dc0a-3dab-a72d-57f82ad640d9 | -12.78179 | -47.43489 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 046d9f76-80aa-32b4-b0b3-2cf77248b5d2 | -12.78154 | -47.43752 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33b889a7-f99d-3bd2-b42b-130492e59f18 | -12.37699 | -47.67808 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11f60af9-779c-356b-b61e-566f83eb58e8 | -12.37638 | -47.68223 | 2024-10-05 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e97a937-3709-34e9-9ed2-e1926e3385f9 | -13.18253 | -48.61441 | 2024-10-05 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a79d837-816c-320d-8a17-9591c5fa0d6f | -5.9953 | -47.45536 | 2024-10-05 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe0926b0-5093-379c-b869-c3d93f758289 | -5.99359 | -47.46648 | 2024-10-05 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ed4cd09-9ebf-3be9-8683-6343b02d93da | -5.997 | -47.467 | 2024-10-05 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6397773-380a-34aa-ad61-010e35e6fa0c | -6.92546 | -47.69248 | 2024-10-05 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f07844e3-37d9-3eb1-8203-1cefb032ae94 | -6.79301 | -47.01742 | 2024-10-05 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25aa7072-3785-3653-92af-57ad707b2672 | -7.46073 | -47.18871 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c63b89d9-a379-3ba7-b666-f554dd3af7e4 | -7.39289 | -47.28486 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7c7a77e-0fb0-33f4-8582-1f3d30a6218d | -7.37473 | -47.25204 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de0753af-eb3c-3b8d-8738-09212b1c927a | -7.24865 | -48.0037 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a86c0ac-7587-3264-a46e-b62046b755d4 | -7.191 | -47.8306 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03ee8aab-652d-37e7-9c4f-0374fb23ef0b | -7.19044 | -47.83422 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d940c474-c399-3459-8cd1-a59aada4b323 | -7.18761 | -47.83004 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d373b339-d582-30c3-b9ca-5c11532b5cf1 | -7.18648 | -47.83735 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21a90c83-faa4-3b09-a918-ed746b11748c | -7.18422 | -47.82948 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d49bf68-52b2-3ac5-a22a-db9cee600185 | -7.11973 | -47.8648 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d0ff593-f9fd-3cbd-b467-12fdcf91e224 | -7.11633 | -47.86434 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb27b088-cb3c-31ab-8c10-5820d0b85b4d | -7.11577 | -47.86798 | 2024-10-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e79e0323-030b-3152-ae2b-75cea3710de7 | -6.92831 | -47.69661 | 2024-10-05 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7df90ab0-62a2-380e-a4f4-afebc5a3ec71 | -6.71169 | -47.23695 | 2024-10-05 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef6f5a5-590b-32df-bcdb-86f33336eaba | -6.63477 | -48.10527 | 2024-10-05 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca4a532-c66b-3f7d-abf4-6f46df138b27 | -7.46598 | -47.17764 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb3b8bbc-ed9c-33b0-95cb-5cd458095689 | -13.30217 | -49.31638 | 2024-10-05 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7585df00-2c66-3fa9-832a-a36262d0f64a | -7.46132 | -47.18483 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ee0e629-f89f-3f33-bd92-22c3b6c38a6b | -7.39483 | -47.12067 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c53d047-ea21-370e-9ce5-5f2f4d8c56b8 | -7.37125 | -47.2515 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c679f07-01a6-3e49-9eb5-370a0dfb7f19 | -7.37066 | -47.25535 | 2024-10-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3a6e8f6-849b-34b9-993c-8d2af135d52a | -8.59374 | -47.13027 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5383c2a-c4bb-30c5-87c3-701cfda46366 | -8.59313 | -47.13428 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f07d3be-a209-3217-b3d6-bc929a8a1e90 | -8.59252 | -47.13828 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749c8732-f425-3580-ad7a-86d4e6859094 | -8.59191 | -47.14228 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ff1b26-a471-30ed-82de-b4a2ef139157 | -8.55757 | -47.63909 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0abb543-2d7d-333e-ab77-dddb37d3cf41 | -8.55412 | -47.63858 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e81e3dac-2e0f-36f7-9c32-d4ffd5dff587 | -8.49596 | -47.30188 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ee30bd6-b92d-3cf8-a76a-56b89916b7a8 | -8.49186 | -47.30533 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0165133e-a62a-3b33-b80e-55fc50963afb | -8.49125 | -47.30941 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82f1db6a-0ab3-3e5c-a4e6-6dcbd7ae0b5a | -8.47537 | -47.21974 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59727e25-0fe4-332f-8122-936062a30456 | -8.3998 | -47.73709 | 2024-10-05 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a37db39-9880-3882-8de2-211653751ce2 | -8.39923 | -47.74085 | 2024-10-05 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 257625b6-b96f-3b72-842b-7a3ec6b5ff6f | -8.19397 | -47.64086 | 2024-10-05 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c4d4bb0-26ab-3d8b-aaa1-19a9a79ce992 | -9.20241 | -47.93605 | 2024-10-05 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b689a26e-37f5-30e0-b622-476f47af05bb | -8.80035 | -47.34583 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a49ebc40-d443-3e4e-808a-69bdee9edbbf | -8.69558 | -47.19817 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04471995-17a8-3c11-ae6b-eab311f480d4 | -8.557 | -47.64292 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 641f3da6-0311-3574-9f94-bea69f620486 | -8.49065 | -47.31346 | 2024-10-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3be2ec5-a2c2-32b4-8a10-88302da02bae | -8.47186 | -47.2192 | 2024-10-05 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6bb119c2-20e6-3202-9434-5f568af36359 | -8.18697 | -47.09702 | 2024-10-05 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 310ea3b1-9213-3fc8-af8d-30a30953548a | -8.87436 | -48.32325 | 2024-10-05 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d301861-a399-38d7-855c-030d837fa2b1 | -8.86703 | -48.32585 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f7dfa1-ec5f-387c-97b3-4ec0092c7629 | -8.86648 | -48.3295 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75892769-73cc-339f-8a22-46831a76c5b3 | -8.86081 | -48.32114 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9d0246b-476a-32d8-ba98-19afd14b961b | -8.85954 | -48.32156 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 256858f0-008b-3d3e-a52c-daca5fcb5275 | -8.85502 | -48.32838 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ae83e76-7422-397f-a0d8-3c63b370a4a1 | -8.84881 | -48.32367 | 2024-10-05 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82b2df71-d9ef-363a-b16e-a7c259b2a705 | -10.74281 | -48.71558 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35389b40-28cc-339f-8662-c48a759d1848 | -10.73885 | -48.71877 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02881f86-d1a1-3f06-a735-59b31ca23c14 | -10.73546 | -48.71827 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58af1034-52af-345b-b237-1c859770d744 | -10.6971 | -48.7197 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ca6fbb0-543a-302b-b8d3-3d22889d2be9 | -10.69425 | -48.71564 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9390e946-8db8-31b1-b470-c61c10877927 | -10.6937 | -48.71922 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9552742a-036a-30fb-9311-ae978b4c832f | -10.69316 | -48.72283 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9952dfb-ae45-37d8-8a5e-5d6c1e0693a9 | -10.69261 | -48.72644 | 2024-10-05 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc8e1b7d-f1d8-32cb-87d2-cc9128bbd508 | -10.12442 | -48.82686 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5430d15f-55f1-3cc8-aba3-5ec06f3e3dc4 | -10.12386 | -48.8305 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fbac7a8-22be-3bc7-8522-89851143a5d1 | -10.12106 | -48.82631 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8364ee1-7ebb-3914-825d-85d4b90a3f18 | -10.1205 | -48.82996 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d604a6-290e-3e33-89bf-fb0de413a264 | -10.11152 | -48.82104 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b45ebfe-7d19-3e14-968c-f4c41a18f330 | -10.10816 | -48.82051 | 2024-10-05 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README100.md)
