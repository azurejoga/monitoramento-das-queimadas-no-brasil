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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65a7728d-000b-30b1-b89f-a885753aa79c | -3.97 | -48.09 | 2024-11-26 05:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2655871c-83cc-3d6e-8337-d0be4342eff2 | -3.97 | -48.04 | 2024-11-26 05:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d08b518-34df-3a05-8dd6-075e5cf15e0a | -4.0 | -48.04 | 2024-11-26 05:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5da79de4-6281-3785-81a1-f81b91d572ea | -4.65942 | -49.72009 | 2024-11-26 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d62d143-813c-3303-8552-f75f66b5ced0 | -3.28307 | -50.01776 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c6a37d5-3c16-3890-9a08-de63ae8fb1e6 | -3.43666 | -54.06752 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efc27299-afeb-3e1d-94c1-3def359146fa | -2.61056 | -53.96446 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125cb418-4714-3491-8eb3-c5249487b9aa | -2.79834 | -53.01523 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bfba29d-4583-33ef-b907-310556da6b4d | -2.94504 | -48.56114 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac3e94c8-8d11-3c5b-b7df-f84e82983e42 | -1.89802 | -53.0108 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d1fcb24-a9fb-3414-9376-a904462926cd | -4.03221 | -45.5471 | 2024-11-26 05:01:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6962eba1-2907-3279-830e-a9bbc2187771 | -3.4451 | -50.01728 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b92d758-64e0-3ee7-936d-5f6e19b74b9f | -3.11772 | -53.75829 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73ab27ca-adb9-39d4-96d6-d68ff40cb552 | -6.37282 | -46.78082 | 2024-11-26 05:01:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ef340ce-3a48-3607-a143-9b84040b10bf | -1.76901 | -53.63367 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be8b966-5afc-307c-a961-aa015ce7c1fa | -6.37226 | -47.35716 | 2024-11-26 05:01:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e5eb714-05ac-309a-b789-30394eb24acf | -3.95996 | -48.0658 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0c5f1bd9-7475-3252-b5e1-02f9da7de780 | -3.15257 | -50.61578 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e61e56e-0267-3ab7-93d7-c5654990aad6 | -1.68178 | -55.00907 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a820f52-7cb4-3c2d-a022-b2f06ce618a5 | -3.24946 | -53.28966 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 849c6d86-50a8-3414-89c9-f381573401d2 | -3.16733 | -51.10553 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d90bc1b-7cc8-378a-8234-1f736fc80873 | -3.68355 | -50.23123 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c76b265-3d86-3ae6-9036-34ea20d30ff5 | -4.54073 | -43.2762 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88427b57-50e0-3e34-ad53-e915ab091e12 | -3.22759 | -53.92707 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a6658ce-8ddc-3c41-aea6-2318fba24719 | -1.89584 | -53.31993 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f417cad4-03c6-3e89-ad7a-f3282b4f1dc6 | -3.08518 | -49.21178 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013408ae-9a8d-3d91-a2ae-74056ebde495 | -3.38786 | -44.17698 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a28c35eb-c9b2-3040-8e0f-31db86eb1059 | -3.0719 | -50.94829 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 188bdf11-b333-3909-a4bf-adb8d93f29ff | -1.88519 | -53.32195 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44b01341-a156-3650-be0d-4488ac0ad42e | -3.24549 | -53.29278 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eef2992-5fde-3935-a5e0-64f42c067aac | -4.54572 | -43.28762 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa10871b-da30-35fb-a40c-45e7136f3454 | -2.58861 | -51.7234 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d9ef6c6-6e43-3ac5-af5a-84b56132d1b6 | -3.32249 | -50.05593 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bcc2ed7-b281-359a-a3dc-5fbcab0698ef | -1.9034 | -53.0262 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4906427c-9122-352a-b88f-3c1df319a0c5 | -3.50367 | -53.81454 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f71e8f60-7ac2-3f5b-80a3-3e8b3c2c4f1e | -2.93614 | -48.82798 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f9d84d6-1f40-300b-a55b-64b75db50046 | -2.58431 | -51.94032 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b0b80c-b299-3f9f-ae4b-9eb7e337114b | -3.10091 | -53.73393 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 885373b6-7dd3-36dd-8f1f-d5d4a8d09e21 | -3.11827 | -53.75475 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f81286ac-4d5d-3a1d-b78d-552d33e6890c | -1.98859 | -53.28983 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82e3ed67-b67e-3aaa-815d-10aacfc805b3 | -4.54529 | -43.28225 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 746b4b2b-a51f-34f4-9442-4bf338648235 | -5.653 | -46.64594 | 2024-11-26 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b1c9488-cbe1-32dc-aa7e-a68c065b88db | -3.97204 | -48.04802 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74299a1a-62b7-3808-83ad-90742b4f49bd | -3.17897 | -45.26145 | 2024-11-26 05:01:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc9e23f8-e784-306e-903f-6b3afef181f7 | -3.38913 | -44.16826 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dfd63582-8bdf-30cb-ad89-2668f96a00d0 | -3.98244 | -48.07448 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e77b428c-0c8a-39cf-a900-4c5da05c364b | -2.66899 | -53.03717 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6015049c-6f80-36f2-9118-50cfd548fc70 | -3.29364 | -53.68013 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b308259d-73f9-3e7a-a59b-01560b6e6a49 | -3.50257 | -53.8216 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45bada4a-e1af-3926-bdf7-a2220cc2c6f9 | -6.00443 | -46.54984 | 2024-11-26 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51d40b68-20dd-375e-90b3-c0a39c02f59b | -3.41493 | -50.10594 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b8ba958-9906-3732-9c5d-1af9b25b8fb3 | -3.38186 | -44.17612 | 2024-11-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd135aad-e9bf-3709-ba43-07f78d590e7d | -1.96608 | -53.136 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42ebac44-f57e-3ad1-9736-c951d127e6e2 | -3.05983 | -53.22399 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f09eb825-1a8b-3f64-bfae-420af144a1a3 | -3.22926 | -50.78381 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c20e3ff2-eb3a-3d3a-a9d2-7024a1b3bcbd | -2.38112 | -53.67066 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e694c66-5632-364d-96a8-88a7379bbfbf | -3.007 | -51.01838 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84956b85-69dc-3f03-9e87-003797cba043 | -2.38277 | -53.6601 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c08ad3e-543e-35d5-b30e-3543e178292e | -3.97185 | -48.06104 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 727bc521-c71f-37d9-8a88-9e65f72c7036 | -3.18013 | -48.43171 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 1a90b396-a1cd-39ef-b6a0-7fb5a615eba3 | -3.99253 | -48.07043 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cdfd648-ad76-3098-af5b-0f89ff819ab2 | -3.08941 | -49.21242 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 632bf9c4-7054-3741-bf92-376e72b7fb0d | -5.76079 | -47.81169 | 2024-11-26 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 35003f58-d77a-349e-9468-e42798cff812 | -3.91532 | -42.42013 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 76581cdf-21ce-3fb2-9cce-f62d5e5ac4e9 | -2.43961 | -53.96972 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d49e0405-b3bd-36a4-a031-8e0dbc5ff71a | -3.96889 | -48.08035 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 99cc0fb5-4af7-35b6-b5bc-5f2bcc25d3d2 | -2.80631 | -53.03156 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f95e17bc-2554-34bb-921e-198ab4f1de0e | -3.51819 | -53.78769 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d4c963-45f1-37ef-91dd-56979068cd4e | -3.30175 | -47.01955 | 2024-11-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b74e93c-ce3b-33ec-9ff3-a36e1ce19f5d | -3.71351 | -51.85445 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c3a385e-0673-3133-9ac5-4a1244605fb3 | -3.97995 | -48.05902 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 343279ae-0c74-3d88-95ce-ce2aaf458521 | -3.96389 | -48.07145 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 44fa2d11-f528-38e3-b740-fd57caeb2020 | -2.57951 | -53.96681 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb17cd60-d27d-3e09-975d-3149cb8cb14d | -3.98171 | -48.07944 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 2898bb82-4bef-39bd-98c8-f4b52568c492 | -3.97494 | -48.0933 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a5eb27f5-412f-31eb-935e-f02185ba3d1d | -3.9665 | -48.06499 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 2b0d73d1-9c04-36ac-b688-2ee53554395b | -3.09701 | -53.73696 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b175e06-d154-3510-9a7e-5e157e9e2434 | -2.60614 | -53.97092 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c31631c-1372-3d4f-8a41-fd3efa2996be | -3.49697 | -53.8135 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f51faf1b-78e4-3896-afe4-d72b4acf3a36 | -2.35727 | -53.71384 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfba3014-2a59-371e-ac20-8eb63cacc70f | -3.1846 | -48.43239 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 1a57eac3-e8fa-347d-934b-6762856ccd07 | -3.96188 | -48.06409 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a78ac2-b6d0-32a1-9477-3d2561417155 | -3.39507 | -50.02062 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b724e0c2-9b8b-32f4-8bb9-6001cbb3bea9 | -2.60723 | -53.96394 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b66d65a-fb72-3e42-8a43-af0bfdfb12fc | -3.06941 | -49.20134 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 977aece5-7ec5-305c-bfe9-5db804e10edc | -3.27604 | -50.64694 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 699613c6-810d-3b12-bab4-d0a4f60f0142 | -4.53808 | -43.28669 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6b796b65-5349-3ea2-920e-425bf2d87d6b | -4.77489 | -47.83875 | 2024-11-26 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68659209-c759-3746-938c-14b75ca5cff1 | -3.28628 | -50.76114 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfa3aa84-b13d-32d1-961b-60c8b1b31c30 | -2.16486 | -54.63805 | 2024-11-26 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f000c97f-3fdb-3626-9611-ed7dc3b4c637 | -3.32705 | -50.05306 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 143a49e0-213c-3a4d-af08-13de5eaca1b1 | -3.2472 | -53.28186 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44f5ba2e-6128-36d1-89c7-3728befd5bda | -3.96116 | -48.06885 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be92f3d-66e7-32ed-9a88-ad273723bf10 | -3.44161 | -50.01319 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0d4e1e-ba91-33da-8973-df186b861a8f | -6.0719 | -48.02942 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b758b93-0806-36a6-ada4-48bda63e7d98 | -3.06194 | -53.28347 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6a319c6a-ee05-37c4-8e08-1273257347f9 | -3.99106 | -48.08046 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e17a3a0-39f9-3b54-9cad-ee8a0fa0652f | -2.81913 | -51.30025 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 762d50dd-083b-31ba-b2dc-3ddab327a93b | -4.54685 | -43.27154 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a65ac83c-0be6-3676-b16b-795dea6f67fe | -3.981 | -48.08435 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |


[Clique aqui para ver as próximas entradas](README37.md)
