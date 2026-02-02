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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1c0dcd5-a3b4-302a-8421-cc750d768cdf | 4.20449 | -60.67573 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51d055bc-5b9f-3f3f-bc58-96df7b2c9122 | 4.37082 | -60.37088 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad01692-54a0-3217-9136-fb2ba540a654 | 4.35424 | -60.37376 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05b26f1d-e1be-3892-a077-9c8d497f5327 | 4.21566 | -60.57432 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af0c255c-1348-3a37-8097-521265b62546 | 3.8447 | -59.67019 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca9fa84-1e83-3f3d-a73e-064a63d960d7 | 4.36751 | -60.37149 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24524f59-9ffa-3209-9985-976d0dc04aae | 4.06439 | -60.694 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec3ecac-a207-389c-a988-071cb0aa2ea9 | 3.42328 | -60.66668 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de18167-a915-31c9-9e55-768075bbef5d | 3.8412 | -59.6481 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f5de2f4-b73b-3bd8-a99d-f81502c5fbb4 | 3.41553 | -60.66073 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 397d5a36-839f-3694-8921-b9832ac3c40a | 4.3603 | -60.39047 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49e54ec7-7b13-3b28-9d00-f9d585c2040a | 4.35256 | -60.38462 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c23d19c-9ed6-3957-97c3-da0b0b85da7e | 2.83349 | -60.83472 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2452f19-bf3f-3030-886a-3bb7f603496c | 4.3548 | -60.37725 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ded7170e-f81f-3438-8040-b62199bf7db3 | 4.3642 | -60.37212 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad027ac0-b499-3c47-b8ff-fca5777f8af9 | 4.36696 | -60.36804 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aeeeee0-e248-3e80-99c3-9fc5db6b49b0 | 3.83439 | -59.64918 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e250a0bc-4aa6-3723-9ed1-ac3a9478de4b | 2.81302 | -60.83434 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecc50187-2d9b-362f-859a-9918babc0514 | 3.8481 | -59.66965 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e777cb8-40a2-3d3a-9657-271f960f6bfb | 4.60494 | -60.68734 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a449f8d4-30b2-396f-8b92-e651a8f002bf | 3.84752 | -59.66598 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9cf5d58-7515-396f-ac6d-c437a2358fc3 | 3.41719 | -60.67122 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a504713-419e-317c-8a1f-eb880a3c8105 | 4.35534 | -60.3807 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f61b76b-d6b7-39a6-bc25-74e631d7bc82 | 3.42106 | -60.67419 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d06c3e5-7fc9-3e99-903d-e124ed73b63d | 4.07432 | -60.69243 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd2dd40-2695-3d4e-9e38-48ec4bba3378 | 4.20403 | -60.58674 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae98a78-3960-3f87-be42-a7c69c30a680 | 3.83099 | -59.64972 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eb8197c-93da-3ff9-b026-746cfc895450 | 4.08469 | -60.24277 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d2d6c85-aecd-3018-9b4a-b18ddc4701bc | 4.06053 | -60.69105 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c847fe-22bd-345c-8993-4ed4609a65ba | 3.8378 | -59.64864 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14cfb7e3-5918-30b0-b647-506bf7f7231e | 2.83626 | -60.83072 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b94e231-e81b-3107-8834-684e65df63c1 | 3.41221 | -60.66126 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a0f9fec-06f0-3d75-bb0e-191498117352 | 3.84694 | -59.66229 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a5169c-16c3-3a9b-afa8-fb4d8c68a4d0 | 3.84976 | -59.65808 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d921de82-37bb-31dc-8c88-01824dca63a2 | 4.60824 | -60.68678 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df9cba5-7467-3521-bc75-ae8887519e29 | 4.36089 | -60.3727 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bbc5a943-6a8f-35e3-b780-293684115716 | 4.35976 | -60.38704 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1271ce5-45ed-38b1-96a1-4b7edcbc7109 | 2.82907 | -60.82827 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| def2e7aa-0d78-3889-ad72-f77b67651a3a | 4.35202 | -60.38121 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e85655b5-9a3c-3752-86a6-c910190e779d | 4.35812 | -60.37671 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30989d23-3f08-31d4-b403-148483e191b7 | 3.41608 | -60.66424 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbf76db2-5419-39b5-9862-9dc73d061dc7 | 4.15524 | -61.03368 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 265f626c-ec6d-3176-b0ab-58a573b7585c | 3.41165 | -60.65777 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c9f48e8-aa1a-3006-b04f-7dcdd84f0cf4 | -9.47924 | -65.73717 | 2026-02-02 05:37:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 717f420a-7683-3364-8b13-6c634107c281 | 2.83601 | -60.83397 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7446502d-9ce5-3338-b5b2-763716469d7d | 4.35451 | -60.37592 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d8183d37-03eb-3ce1-ac88-2ab27851944d | 4.3639 | -60.37375 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b74039f3-a62d-3a64-a3e3-86a45305b694 | 2.8313 | -60.83474 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b812d51e-b94b-3abd-9ee1-b8347dde5366 | 4.35506 | -60.3743 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 807c6585-c96d-3c3c-a7ca-01e470c5a4b7 | 4.35121 | -60.38541 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 238a2131-3c68-3ae8-90c0-dc0330ea4a32 | 4.35978 | -60.37339 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7833db92-c8bb-31da-b299-1fa057c0fbc9 | 3.41411 | -60.66236 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd5592e-a8e5-3750-99db-83f167597806 | 4.37362 | -60.36882 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccd8d998-e8e7-3038-91c7-a4b59c30d0ca | 4.35923 | -60.37499 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da323912-1fc5-3547-8621-9c58acc8a284 | 3.41329 | -60.65734 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66e92c8e-6331-300f-9240-714a99847286 | 3.42172 | -60.67501 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07bee1da-eba3-3fea-b640-778bb872b2e2 | 4.35527 | -60.38052 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e410cf15-2814-3c1e-b3cf-ab9c75eb62f8 | 3.42086 | -60.66999 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59cf8dd5-efce-3e14-b429-cc1774979d2e | 4.35844 | -60.3702 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b8f3623-4f6b-3a83-b4c9-6a7ae61e8ebb | 4.36314 | -60.36911 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76fdd695-c038-3ca4-9421-fb0ea5e7d739 | 4.36901 | -60.37035 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26c8f2df-0a9a-3987-8b5a-2077960620be | 4.36443 | -60.3721 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e7ba93d-7500-395c-8ca7-a38f3e4aa680 | 2.83519 | -60.82902 | 2026-02-02 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2408b7-4645-367d-8d11-d999a17ae4a2 | 4.35588 | -60.37902 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 51362b51-6e50-3f04-b22b-6440e9cc4d23 | 4.3537 | -60.371 | 2026-02-02 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1deb7214-dc7e-3d3b-bfc1-efd928b4ad85 | -3.27399 | -42.38359 | 2026-02-02 06:05:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4cce2442-eb7c-3e6c-bc2c-1cde71d44114 | -3.14563 | -48.14353 | 2026-02-02 06:07:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5995be32-491e-3429-997e-a92b848e09ac | 4.35893 | -60.37523 | 2026-02-02 06:24:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4783de52-1b42-3c72-9308-8f20c6512c5c | 3.41668 | -60.66116 | 2026-02-02 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f36c647f-10fa-3096-b655-079af1866a34 | 4.35186 | -60.37643 | 2026-02-02 06:24:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1abcd168-4f5d-3b8e-9962-2ad7e9527ac8 | 3.41909 | -60.67493 | 2026-02-02 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b5248ae-e4e3-3272-80d8-e42388d850a7 | 3.41788 | -60.66802 | 2026-02-02 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cfd5c3e-6368-39d6-b92d-115ec037ea92 | -8.2329 | -35.30215 | 2026-02-02 11:14:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 9e123f2f-c511-3a67-9e19-47871652f9eb | -8.58511 | -36.66977 | 2026-02-02 11:14:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 5f718600-07a8-3a2a-af0f-56556c8bbbe9 | -5.39424 | -35.46408 | 2026-02-02 11:14:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 25ec3cbd-6646-331d-a7c5-de7694956cb9 | -6.23678 | -37.50355 | 2026-02-02 11:14:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5568f902-7b02-36c3-9009-2cd214c8ddba | -6.32541 | -37.5987 | 2026-02-02 11:14:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 9.1 |
| feef17b1-c0e7-3f8b-ac31-528ae295dafc | -8.93633 | -36.40639 | 2026-02-02 11:14:00 | TERRA_M-M | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 64cc8bc5-f9c5-3f6c-9651-e6324fc8713f | -7.39931 | -37.46967 | 2026-02-02 11:14:00 | TERRA_M-M | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 4aa2f4cc-ab71-31db-a974-d1092d8bdf1d | -3.4217 | -42.4739 | 2026-02-02 13:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 7ec37d44-6ee3-3637-a1fa-f9326c588a91 | 3.4202 | -60.6647 | 2026-02-02 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 27deaa3a-22d7-3907-8c02-be9505839cdd | 3.4202 | -60.6837 | 2026-02-02 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b7134bda-2c0f-32ac-9acb-9b737904f690 | 3.4202 | -60.6647 | 2026-02-02 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| febdc0fc-b196-3b07-aae6-5d22af84c20f | 3.4202 | -60.6647 | 2026-02-02 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 95.5 |
| b49b413c-9f6e-334c-ae69-146d5ac54071 | 4.06 | -60.7088 | 2026-02-02 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4427d5bb-9d3f-36cd-ab0e-93da28bc34ff | 3.4019 | -60.6651 | 2026-02-02 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6745d76c-e4c5-31a2-85e7-26bee14708b7 | 3.4202 | -60.6647 | 2026-02-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 0d35c59d-6dda-3840-bab7-cd3f676092c4 | 3.4019 | -60.6651 | 2026-02-02 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| da42fbf7-8cb0-30bd-a1a2-4455521537dd | 4.06 | -60.7088 | 2026-02-02 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2e9d6b30-f186-3f7a-9102-34073d5d3785 | 3.4202 | -60.6647 | 2026-02-02 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 112.5 |
| a9a0e29f-2df7-3651-ad7d-e0de72965144 | 3.5289 | -61.0228 | 2026-02-02 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 866011c5-f4e7-3109-a733-06daa1a5b05d | 3.4202 | -60.6837 | 2026-02-02 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6fa46b13-1b09-3625-b1aa-04b7fd58876a | 3.4019 | -60.6651 | 2026-02-02 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ad4b3ac2-a2c9-360b-bab6-ed4f591731f5 | 3.5289 | -61.0228 | 2026-02-02 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d17b3e93-c048-399c-a90e-34321fb65e2b | 3.4202 | -60.6837 | 2026-02-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 46d21c2f-3f7f-3aac-bfe1-d4a24232e790 | 3.4202 | -60.6647 | 2026-02-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 20229c3f-4c33-320b-8fdd-8452c397dd2c | 3.4019 | -60.6651 | 2026-02-02 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c20bf9c6-eaec-31ab-b3cd-abe375592902 | 4.06 | -60.7088 | 2026-02-02 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |


