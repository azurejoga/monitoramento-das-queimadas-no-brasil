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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a27899d-ad64-3f8f-afcb-553f702a6887 | -3.7783 | -49.98153 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5817ab84-5f0c-3e60-8f1d-02db9db57992 | -2.95735 | -53.7039 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14fdd24e-50e6-3a2d-95b8-90b4819b46c2 | -3.22751 | -54.17242 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7550a8b8-1f29-3ef8-a63d-b0410c236be4 | -2.22796 | -53.62484 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da2374a7-9070-3782-a143-d828058d7509 | -3.98066 | -46.99146 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aa395f1-3392-39d1-9da4-fe5f6933f41b | -2.72201 | -48.63634 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9088a618-f7db-36f3-a8a3-238cb7f01307 | -2.85898 | -54.02642 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2d3ac44-ba03-360e-8f8d-a1fc2ec49fe8 | -3.48944 | -54.67171 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88c47700-21b1-3246-86ff-508aaad51dfd | -3.48612 | -54.67119 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02e31adf-f16f-3a26-a32b-7d735f72f967 | -1.47016 | -52.35466 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e44048-659c-310f-a16f-cf8882952e01 | -3.27418 | -53.30647 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaf344f9-17b5-36a9-8cb6-d0306b379d1c | -2.19006 | -53.78074 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa150d1f-a9bf-33ca-b118-c1345027bbea | -1.88789 | -54.40693 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36cb3504-49e1-39cb-8cbf-7779ad8f6bc9 | -3.25185 | -53.62342 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50d30943-32bc-3819-b4ad-f783dc6f63ba | -3.2614 | -53.2798 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1027435a-8fe6-3327-8765-c3f2b956094a | -3.12116 | -53.10915 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 341b2117-1fe6-3e65-bd7f-c2755e2363df | -1.62588 | -52.46786 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c0cfa6d-3d47-3d13-a3ae-828db60de73d | -3.87527 | -54.22845 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1ded8f4-164f-3628-871c-d9f68168d099 | -3.13543 | -54.26055 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56aadae-3938-39db-b80f-3c42637cca3f | -2.87373 | -53.99697 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 610d514c-b491-3d18-af03-414cd101df26 | -4.16686 | -54.58203 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c69d86ea-392f-3452-a018-ea5f0bdc27aa | -1.93962 | -52.94248 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 821ced77-9dfc-35be-aa6e-11dcc0b419f4 | -1.52531 | -55.37449 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da42439d-cbb5-3c66-b978-095f8c3f0315 | -1.36304 | -54.65636 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea84c11c-7a04-372b-93ba-263ed1158ea5 | -2.7708 | -54.20004 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dcaa621-7e8f-3f0a-913c-e72ef807bbca | -3.17995 | -54.32429 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc4dab46-0c76-354f-91a6-f6e0e1b7443b | -2.83583 | -54.02285 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ba088aa-c803-3d0f-a044-df946d3df096 | -1.33894 | -52.51957 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 810aa37f-b122-3601-9435-67b4855afe8a | -1.16272 | -53.58387 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c0540b1-8a99-3bbe-9494-cc304543f20c | -3.20764 | -53.84166 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e14b283-c14a-330d-a39e-1d36c73edc79 | -3.46925 | -54.54022 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c281e8d4-05e3-34d2-8ca9-92437bf38e1b | -3.94073 | -49.90801 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bccb0a03-1b78-33af-92b9-c0a25361ac38 | -1.08765 | -53.38957 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9842e1b-8bf4-36ac-b6dc-0f4fbdb41dd2 | -3.18935 | -54.32928 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87c52c3e-ca8d-3168-ad95-7697a765b884 | -3.72876 | -51.09145 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be11f9e5-6e29-313e-883d-f64b1252050a | -2.25107 | -53.6284 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ded9e6-fc42-3edf-9f0b-044231e4002b | -0.77421 | -52.38968 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 862107a6-05c9-3f40-8ab9-e9a0b3d15062 | -1.12099 | -53.21923 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1825ed03-fc0f-3925-8fe5-75f333907819 | -1.71232 | -54.98705 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c23070a3-0791-397c-b125-131c610d8e01 | -1.70389 | -52.64424 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 55ce0e6d-86c3-33e9-9bc4-20d5be86c4ad | -1.38242 | -53.63611 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42458b76-d812-35d9-8264-71470188aa34 | -1.79737 | -52.04029 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1cbc9b5-1845-3247-bdd2-0cfab46235a3 | -2.82322 | -54.03852 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 368edc9e-6ce1-3807-a0ca-da530471dd3b | -2.58451 | -54.23772 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fbf4d56-fb34-328a-9606-9c817eee55db | -2.83591 | -54.04401 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e1fde0-2d6c-3c6f-8be8-a4a15c653e86 | -3.85788 | -50.14682 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ef207b1-b5df-3d6b-bd91-f345b4263b43 | -2.71816 | -54.16639 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a35a73-ef09-344e-8ce7-c610e447c6b7 | -2.99814 | -53.72424 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6eff148a-7dce-37db-b8fa-238e7facdd54 | -1.40365 | -51.58578 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f701d9a-bc6c-3d32-a2d2-9b141355cdca | -2.01291 | -55.39986 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 069bee6f-1d3e-3f89-83c8-ddc4b82d9c8f | -2.83037 | -54.03611 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98c517f5-8dc6-3bba-b7db-aec9fde086ed | -1.36359 | -54.65281 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c1a82a82-7d64-3475-a51a-a2a7beb80849 | -3.12483 | -53.26178 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec0f076f-3de0-35f5-9ba3-d4966963be1c | -2.45444 | -54.00546 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d9c5922-03ad-3c3e-ac5b-22185183ff62 | -1.30831 | -51.75271 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14ea1289-4449-3ae2-85cb-6697a5bbeebe | -1.10725 | -53.22063 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266290e1-d3d8-3ca1-b725-c149280c3fb6 | -2.82945 | -54.08533 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1bf7e9be-fb93-38cc-bdcf-84ff64d2fab0 | -0.95686 | -53.20449 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55725185-52f1-3458-834a-d47b655d946a | -3.78138 | -46.69339 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db29d6e4-320c-35ea-96a5-557f9c3ce666 | -2.69617 | -52.91202 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 862434aa-4e6d-3e6f-a356-1f1728831c9c | -4.18576 | -46.61873 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c04e8321-3458-3b74-b9e6-2fa09a7bccee | -0.96392 | -51.64488 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14c34a46-37cd-3286-a292-4cb1c72bad0d | -3.34703 | -50.23489 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 74548c40-2bb8-3c7a-ab47-15c6aca20e5e | -2.96574 | -53.73682 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41cfff58-708c-3717-91a1-973ea3502331 | -3.12045 | -53.26816 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1cc339ea-5ce7-3683-b9a1-bd26a67420d0 | -1.60455 | -55.42882 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e0b247a-a9c9-3f05-8999-561f48621b1c | -1.21396 | -53.75798 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 471fb828-b715-3cec-8715-d2253b2b67ce | -4.47004 | -46.31307 | 2024-11-29 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac3f5ab7-3d9b-353a-9dcc-37f0bdf52e4b | -2.7505 | -54.11123 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8e2e817-7183-31cd-96a6-c9adb3629311 | -2.59888 | -54.0808 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b422c1db-d1c5-374f-9e56-d699139390be | -3.96287 | -47.94137 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 349736a0-60df-338f-ae38-1610eeaee017 | -2.85749 | -45.54467 | 2024-11-29 04:57:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ce70373-755f-3813-a3e4-f1410638f99d | -2.77361 | -54.03088 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ff86b66-5a0b-3f30-a512-c14736b874f4 | -1.2144 | -54.19041 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aabccca-566a-37fa-a5ee-8a4c8fa8521b | -2.58113 | -54.21593 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6e4e8ac-6583-3200-b10e-34eee93f3cc1 | -3.0549 | -54.03567 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 527dde13-0b6c-3b87-937d-5e550bf8b63d | -1.44662 | -47.11737 | 2024-11-29 04:57:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e61e3a7a-884d-3eda-a7ee-aaee3cb35088 | -2.24071 | -53.7815 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 447b4177-ddd5-3071-8281-69d08b4dd50b | -1.96067 | -46.43988 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a7936004-ac11-39b9-981e-4182483ee2d0 | -2.7268 | -54.11111 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 421e6dbb-4bf9-35d9-a1d0-384ae65f3bfc | -3.081 | -54.5649 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a50ac63-2ede-3e8e-b865-6a01205945d8 | -3.64461 | -52.34397 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26b979ae-1abd-3a2c-89c0-e270b68c6f13 | -3.90056 | -50.53281 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58efeaed-a020-3aa5-ad49-708b17863aec | -2.78675 | -51.71922 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea4c119-615a-398e-9959-7888fcf0c31e | -2.44512 | -53.9752 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0e523bd-7c91-3502-bc0a-4aa019c708b9 | -0.75125 | -51.79198 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 957ebd4b-6f2f-32ee-a84a-da5ac671f1a0 | -2.73377 | -48.89509 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4c36f76-24a6-3c8d-8a45-826fd03c95f0 | 0.93989 | -50.74883 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b3aad5e-27c6-369b-83cd-e6eef4c07d21 | -3.10193 | -53.82124 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 137eb4e1-b628-3154-be8b-7dd31591dc79 | -1.31168 | -51.75323 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fde269f-479b-3518-a64d-cfbe11e86e13 | -1.36551 | -52.12959 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cfcc808-f492-3db8-a245-122420864217 | -2.54424 | -53.99453 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcf471aa-1f43-3a13-8779-1f89c2de33e2 | -1.33603 | -51.92928 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89e9c04c-131f-3eb5-8458-f0161020e268 | -1.06669 | -51.79634 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d10321-09f6-30b4-af20-2c113d3537b6 | -2.73383 | -52.58236 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 749a7d6d-1391-36ff-a2ec-3f990c62144e | -0.29594 | -51.74411 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2208389-94ff-3606-8a24-d9540807ccad | -2.33357 | -53.86274 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4ff9b7a-d688-3e19-b5bb-1dc22e5c9aa7 | -4.79505 | -43.78021 | 2024-11-29 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff46bc44-8939-310c-902d-a12c23595f19 | -6.0977 | -43.9668 | 2024-11-29 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42bf5559-36b0-38c0-8c33-2431865962ed | -3.86025 | -50.15625 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README55.md)
