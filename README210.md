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

## Dados Diários - Página 210

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5a1cc6-a41e-3bdf-919b-cea920a2a7db | -9.58553 | -56.47296 | 2024-10-09 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0180a919-9d96-3366-aa12-faaa2ebe74fa | -9.49152 | -56.07962 | 2024-10-09 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b530f6f-438e-3377-b2af-4e8a081d9388 | -9.49052 | -56.07745 | 2024-10-09 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 590c2800-db92-382f-8bb9-930d57e6d474 | -10.36488 | -55.86413 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cf9ad34-6e68-3f9f-bdf2-c6afe3c2fac1 | -10.35877 | -55.86531 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b3d85bfc-9f81-3f77-879d-8ba448d2fe8b | -10.35791 | -55.86318 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9eb248f7-9bf5-3d7e-ab3a-25c9548de9f2 | -1.24207 | -55.68459 | 2024-10-09 05:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 487d2088-2d30-33d1-bdf1-2f1961d65f82 | -1.24133 | -55.68942 | 2024-10-09 05:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d069f3bf-fce1-34c6-991b-0d79f98e7ce7 | -1.23509 | -55.68829 | 2024-10-09 05:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb2427e5-7054-3745-981d-73f7fc75772a | -9.92909 | -58.12918 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 517457fb-2cf5-3808-9d8c-2e91baa2e4db | -9.92854 | -58.13369 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d141846-5577-3ddd-9ee2-af947c46b660 | -9.92305 | -58.12826 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d027c37f-fd4b-3def-944b-1dafc3399233 | -9.9225 | -58.1328 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ac66e58f-e004-3123-8d96-4294d90534c3 | -9.72591 | -57.80163 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef014606-e35c-3239-bce3-9aaa107675ea | -9.48487 | -57.93394 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f74fb4ce-818d-378a-b94e-f7f978c12f84 | -9.48411 | -57.93334 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf6a33fc-0c5e-32f3-ab5a-d167221a1f37 | -9.48353 | -57.93789 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c26c7c-3114-3b2d-962a-31649af09cf9 | -9.47993 | -57.92354 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a59669-ea5d-3f72-83dc-cdc1756a50c2 | -9.47881 | -57.93286 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52698a9-8bd8-3c73-b762-98c5617cbb8c | -9.47825 | -57.9375 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65fbef19-9606-342b-b1b4-978214c76316 | -9.47805 | -57.93229 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e591f5b-8c50-3168-9872-fb88b365085e | -9.47746 | -57.9369 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d21d39-8c88-3a71-b9c8-91b2d2eabde4 | -10.33548 | -57.50383 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 431ebe21-567d-3093-9f47-cc5f70de7f27 | -10.33486 | -57.50898 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb07a49-70ef-344e-a45f-e5f30b511ce4 | -10.2297 | -57.81598 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bec753a-6047-30e0-afb3-4443b7fb2afc | -10.22908 | -57.821 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b3c6c45-5ce2-37a2-923f-bea42635d990 | -10.2285 | -57.82574 | 2024-10-09 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e520e7da-551d-3790-bcb7-4bc69b08d7e2 | -9.73636 | -56.98451 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4459c7f7-6635-3eec-a7b4-12a3252644df | -9.73592 | -56.98296 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57a9bb23-ff2c-3d3a-9c4d-2d0c0ec6d8a4 | -9.72989 | -56.98353 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e319b0a5-e540-3617-aca3-8e7ac68eed46 | -9.72945 | -56.98204 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78eed798-2adc-3f42-83b9-5bb5b5df73a3 | -10.25705 | -56.76215 | 2024-10-09 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8250063c-9441-3e3d-8d02-b1556074ff63 | -12.29602 | -57.88087 | 2024-10-09 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce86e7ca-2fe7-3045-9998-c2b0fda2c59c | -12.29546 | -57.88582 | 2024-10-09 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e17d4def-a7d5-33c1-826d-ff37bed23da2 | -11.96464 | -57.60219 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84863c25-cdc4-31d9-9647-c05efd47ec9c | -11.96315 | -57.60003 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26edaf39-a4fa-3da7-87f3-b1ae783ee3a7 | -11.95883 | -57.59582 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8235406-df8e-3960-864c-8e288ed5b251 | -11.95824 | -57.60123 | 2024-10-09 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3f89ae3-1e14-3f16-8e63-2ad24cd16271 | -6.52949 | -58.41688 | 2024-10-09 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bcc58a3-dc0a-3ec2-8db8-59ba4ed6f47e | -6.52897 | -58.42067 | 2024-10-09 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 732e6c0f-2ad0-307e-9d11-d5f82732ebd8 | -6.52843 | -58.42456 | 2024-10-09 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c8764a7-712f-35a6-915e-ad6f8024c89a | -6.52328 | -58.41998 | 2024-10-09 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0950f42-dc11-38d5-ab0d-617763fc6eca | -10.39807 | -59.1328 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa069b95-24e6-34e0-b26f-0fd65f82e589 | -10.39759 | -59.13678 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c52c5a25-9e9c-344b-a1f6-cac461c311ce | -10.39579 | -59.13512 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c84f4dd-c194-339f-8c5e-123e6928756f | -10.20228 | -58.79415 | 2024-10-09 05:55:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec2cb537-aef5-35b8-b535-d43d599300ad | -10.20175 | -58.79833 | 2024-10-09 05:55:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10e88fd5-23bd-3b19-835e-b07ea5f3c1ba | -10.20125 | -58.80238 | 2024-10-09 05:55:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e99d4a-868e-3ccd-a7ca-3b6389d0507f | -10.06284 | -59.35705 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9958b4-7c59-35c5-8379-e9f2fabfa2e6 | -9.8792 | -58.33869 | 2024-10-09 05:55:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d1ce48-d364-3b99-8c5c-7351f92315f4 | -12.31351 | -59.17421 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ab8e73-140c-308e-9781-afaafb61a872 | -12.3133 | -59.17109 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6846ba6-a056-3019-8ca3-e8c923b9ccde | -12.31299 | -59.17845 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a3c0167-2f83-30a5-8eb1-f95b4698d535 | -12.31281 | -59.17536 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4acc59d2-82cf-3f29-bebf-b89ae109edd4 | -12.30718 | -59.17748 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0f3c404-a728-34e0-aec8-74f59966128c | -12.30652 | -59.17863 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c39165d-6780-3ef1-9fb5-f4ba5c5e7689 | -11.57787 | -58.95324 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf4584ea-fd5e-3f46-bd0f-e6e9ad366de0 | -11.57199 | -58.95256 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f34de53-d507-3799-8995-76e60fa45e5f | -11.57148 | -58.95685 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b10171a7-6d30-3377-80ac-8629ea2ac248 | -11.48973 | -59.09579 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b872a6-820e-3928-a473-7ef81352ab0b | -11.48945 | -59.09667 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 014cbad1-19ea-31bb-88c6-14f571dbfed5 | -11.48923 | -59.10007 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bc964d2-9112-3922-8024-949bb3cb6a36 | -11.48892 | -59.10093 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dba1c0a-e590-3dd7-be27-feeb029d1948 | -11.37158 | -58.99671 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42727f30-8662-33b2-a66b-10303fd16b95 | -11.37134 | -58.99721 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4ba8419c-1d7e-37b1-8e4e-f9641de20ab2 | -11.37108 | -59.00072 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93aa5f44-35e8-3815-82eb-69c6a51f1648 | -11.3337 | -58.91718 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f345faa4-921d-310f-9c41-f2f07b7ce733 | -11.12952 | -59.09061 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f73f631f-61cc-307a-83a5-6d7bea6cdc0e | -11.12901 | -59.09478 | 2024-10-09 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e30384f2-4ada-36e1-bb50-533d5c202c9c | -5.09719 | -60.2261 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 590a63dc-b6b5-3ef8-8976-353f5b57b5e8 | -5.09639 | -60.23162 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d28d580-9a0e-3ca5-8b9a-5839556a8e6c | -5.09309 | -60.21983 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 870de6cf-120e-356f-9711-4c7aadee827a | -5.09228 | -60.22536 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5385678-c1aa-3c88-ba6c-4e31630be78a | -5.08737 | -60.22462 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c87b286c-f860-3c5a-9555-58d36a3a3666 | -5.08245 | -60.22388 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dbd056d-afd1-3105-b209-6d2897ef7077 | -7.29957 | -59.73932 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0afab06-ad3e-344c-a5eb-ad258c12fabf | -7.29434 | -59.73845 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734b1791-e3f7-3502-bbb2-b459a3d53e73 | -7.25039 | -59.62988 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43adfc64-2b1f-3198-8fe1-8d79cad6a159 | -7.25008 | -59.6286 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3931b5f8-9b23-37dc-9138-0834109b66a8 | -7.24996 | -59.63297 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 546db48b-a6a7-3fca-a139-c205eb440548 | -7.2451 | -59.62918 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95c6df17-3162-3f1c-9c91-95208c223d18 | -7.19223 | -59.77777 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f26d104-c0e7-373b-ad4e-b9cb57d65dce | -7.19179 | -59.78092 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1ab09976-28bc-3488-bd36-ffb4a37198ad | -7.16508 | -59.35746 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79260d04-9833-32f2-bcc4-84455530e6fb | -7.15971 | -59.35665 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead1cc72-201e-35fa-b0bc-bd18e78bffaa | -7.1345 | -59.30037 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa72552-3589-335b-b13d-b2a24b686463 | -7.12911 | -59.29954 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b8d3c0-ff7d-3cc4-8b90-0fe1417916b5 | -7.06996 | -59.45411 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051cd06b-a790-3c2f-a132-c242b1d8bd6c | -7.06952 | -59.45743 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8b94487-a837-317d-a011-668bce650d84 | -7.03292 | -59.41891 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0f0aede-efc5-3c89-840c-282fe67b83f0 | -7.03256 | -59.8117 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34183714-3ab2-38fc-a977-953ba629dfda | -7.03213 | -59.81486 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ad49bb-ef71-30ac-89b7-8ae0b307d44b | -7.02805 | -59.41473 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d3fd001-c708-3c43-b560-1837ce1cd494 | -7.02758 | -59.41809 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f30dcbbf-4873-325c-b031-8537a0ffd0e5 | -7.02271 | -59.41391 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b3fa24b-0255-3791-a8fb-d58e4be0ed33 | -7.02224 | -59.41729 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a11cc6bd-7222-3bc5-914c-a8b0381e563d | -7.02177 | -59.42068 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eedb37ee-fba5-30eb-9448-049610546914 | -7.01783 | -59.40972 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4af0573e-538b-393e-b9c9-c75141f2acc9 | -7.01737 | -59.4131 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 546f5630-27db-35f4-9ae8-2c4eebf448a0 | -6.80075 | -59.35091 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README211.md)
