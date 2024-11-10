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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2f82df4-1e9e-3fcd-873a-2e817e3a5126 | -3.94043 | -49.75837 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0a300ff-0d2e-36d2-87e0-379d4ea32397 | -2.03256 | -46.54409 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af481fa0-9827-36f5-acbd-e0f697da9a73 | -4.85097 | -46.98132 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db039e23-5427-3767-8b76-3baa7c5d6869 | -1.62347 | -52.53452 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01149b28-22c8-3187-8714-47fe3010e2ce | -3.03319 | -50.35039 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2b4148f-e0bd-32aa-bd9c-c29087afe875 | -2.10318 | -48.90034 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| faf85825-250d-3206-9bdd-e83ce3b3a644 | -2.93789 | -52.77253 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4210cd02-a19e-3f28-9d03-9a3ec2b2d53d | -2.09223 | -46.34214 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35e2ada5-e14d-34f6-bf55-696ce924489f | -5.89218 | -42.82792 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 747bd8cd-db64-3ed7-849f-dea099be1753 | -2.25861 | -47.06417 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0b71894a-248c-30b8-a09f-d965b4c1cc47 | -3.28734 | -53.67916 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44fce297-9323-3a55-8058-ce1cbe22be01 | -2.29813 | -48.50411 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 739de22b-7b88-3229-9665-e1502d73a6ae | -3.14407 | -48.58053 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9439368-69d4-3e1b-8ac5-ad7767be26a9 | -3.43775 | -50.30403 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 319d0be0-3c24-33a4-b71f-e3a9e9de8571 | -2.73257 | -51.71387 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6492811-4314-3589-ad95-c6a673453692 | -0.40923 | -51.93262 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbcc8995-8523-31ca-92a7-d773b9bbb5f7 | -5.22439 | -49.68791 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c83c356-76d2-396a-8099-3a75e398dbb3 | -2.35112 | -46.66505 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5762f37d-9bb5-3cb0-ae6b-8f53ef785179 | -3.65686 | -50.16579 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3677ebf4-f3e1-3ce0-adc8-5c3218ef5f1e | -3.92156 | -45.01094 | 2024-11-10 04:14:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3572f92-f09e-3882-a2d5-0bb9a0a5c73b | -3.53058 | -49.98156 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6936c738-e36e-3063-8aaf-526985e0c2f3 | -2.1399 | -50.69725 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a5f358-7643-3279-9eed-3052c6c48ee9 | -5.51404 | -43.7879 | 2024-11-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce76499d-50f8-3cab-ba41-a3e314ac885d | -3.82098 | -49.85558 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d14be55f-ffb6-3f9c-a638-f85cf160c4e7 | -3.99416 | -46.41074 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bf61f63-6259-3686-aa8f-40b45f806074 | -2.7329 | -51.74531 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d208a6ac-6a68-3dc4-a7f5-3b55292cc7dd | -0.04427 | -50.78949 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a39840e4-2979-3840-becb-4b749658ad63 | -2.4689 | -48.44587 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 33431d53-48a4-35ce-ab81-cdda4a55bb36 | -4.09685 | -48.32277 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e70cff-c685-304a-a771-4c7cae1e5dc5 | -5.13643 | -46.18567 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a4125436-e2c8-3b63-9cf7-8d8cbaa99a6b | -1.34973 | -51.40697 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc241497-efc3-3e2a-b88a-cd125560c1eb | -3.19443 | -48.66369 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3161fc0-b033-34a9-a13f-195d494e06ef | -6.73577 | -40.81266 | 2024-11-10 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d96761d-ef9e-362c-82f0-0e8b9657a330 | -2.6644 | -49.89514 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58b1de80-b90f-3372-a0ec-f9ae2f5b668d | -2.08345 | -48.82441 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 831fe7d5-12cf-38a7-a64b-dab781d8a098 | -5.27413 | -37.95034 | 2024-11-10 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82751e10-bee4-37c4-b10a-0b3fb90eb84d | -3.10664 | -49.41682 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9ef8db0c-ad69-362e-86fe-fcbde84978a6 | -1.64188 | -50.44102 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 489de7d0-a27a-37d2-b245-4ebe300b1c5e | -1.47957 | -54.2986 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6a8efe2-3ba6-37ba-8bd2-0c33360cb231 | -2.42747 | -49.42318 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb31d24-e24b-35b5-bffb-82d43d7c75fd | -5.06147 | -50.01109 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c7e469ae-258d-3ee4-91d7-f1f7eb3ac9b2 | -4.90748 | -48.3888 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c62e1f2f-8485-3544-afbf-ee2334692b7e | -2.91845 | -49.35785 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4664b047-2527-3d0a-9d50-a4cf90d5cc51 | -3.26025 | -46.27755 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcec1cf6-3599-3a6e-83be-3b12ca4c70d7 | -2.26941 | -48.73962 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88a14536-aa19-3930-8854-bc4c88546ad1 | -3.05182 | -51.08905 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75b77eb8-c083-3369-813f-880b1ed4d149 | -2.93673 | -49.36072 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f6b73670-ca2c-39b2-aae1-8a095c2091fa | -2.45265 | -47.1644 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f81b54-a38c-33b4-91f4-58998a7306bd | -4.38169 | -47.22233 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54246bc4-8801-33ef-ac59-61dbf96a0711 | -5.36517 | -48.24829 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3adb8ee-296b-326d-bc50-c22657f4b2a3 | -2.48933 | -50.28175 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0961ac29-a761-3c46-bf7c-1775894e7e5a | -2.56956 | -50.67873 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09b2af9e-ccd2-362f-9fe1-7e7bc1fe3633 | -2.42316 | -47.82979 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16650779-ce40-3200-8cf7-c4ea096ffb82 | -2.24108 | -46.35832 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf946413-781a-3ceb-a8ab-f809a9caaab0 | -4.06359 | -49.28735 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59a7a716-5a30-3092-8488-29859ee35049 | -4.09924 | -49.12073 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d546dd05-85e4-3e6c-8109-6ec5c9898920 | -3.62066 | -50.61283 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6245e00d-ae3e-3605-96ba-5a9fac18d836 | -1.64029 | -53.38771 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7bfdc47-ae62-3093-9419-ecd24c73e82a | -5.55363 | -46.3429 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6498b67-888a-3abf-a810-9accc5ec75b3 | -3.21939 | -50.37943 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 744c402a-2025-3554-b59d-077d643d4ba1 | -3.84078 | -49.96996 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2d5a98f-2470-3267-a8cc-4a6f5adee14b | -5.5702 | -43.97198 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bddfabad-bd92-36d0-804f-2d95dfe70034 | -2.87519 | -46.66296 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26317282-0e1d-3cbe-8cc4-f57bfce521fa | -6.31481 | -42.75643 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bab9164c-b7a6-3a36-9caf-9a64cb42da6d | -1.50655 | -52.18515 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dbf16f2b-6d29-3f5e-8a7f-01582a402c8c | -2.09165 | -48.83023 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fd1849ca-dd04-30b7-9daf-3548de9fc01a | -1.21586 | -51.77379 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef57fd9-9c67-3b44-8158-f6c0e01b8f03 | -4.16913 | -48.602 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c3bf2df-50de-3615-ade3-8d08fd6b0af9 | -2.6551 | -48.49834 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4d7302-2b15-3f46-bb9f-1c90fc67c8b3 | -3.82564 | -49.85634 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 777d6fe8-f5bf-3f0b-a82e-e36b7030f35d | -1.95574 | -48.87056 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4eb0b09-128c-31a9-a918-1d7e1b10486c | -4.71836 | -50.58766 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b3628a2-5c37-3a04-a9c9-cb9bc5bc29ab | -3.46699 | -50.1848 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad757b12-b9b1-3813-953d-35b163e83899 | -2.67392 | -46.70899 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbd7f995-b85e-3fac-b538-55f44a8842e7 | -4.79289 | -44.30298 | 2024-11-10 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba29f08f-9e1b-3e7e-9e3f-8f4108157e21 | -5.57353 | -43.97251 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb3df499-9237-33d0-ba2a-4d397ac8ba6d | -0.40946 | -51.47364 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1397280e-785a-376e-8ff9-a80cecb158fc | -2.50734 | -46.27242 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5714380f-77c3-3b30-b26b-faff78604a4a | -1.28206 | -52.20887 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78f440c1-8b45-3379-89c7-bbb2519c47b2 | -3.36008 | -49.50707 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef34be8d-c396-3cbc-8cf7-fdc5d8bb5b3f | -4.06398 | -48.23553 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64dd69c1-8346-3a95-ab30-a8f3f291fb09 | -3.07567 | -50.57004 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 064accaa-35b8-31eb-a5bd-0d1e533810b8 | -2.99587 | -45.03231 | 2024-11-10 04:14:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 760e557c-fd7d-3f0b-a1ed-e59e2b2e308b | -3.95219 | -48.99835 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc6e714b-907f-30a7-8669-c5718e9e72fb | -0.04688 | -50.77325 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b90079a5-b9ed-3f67-b028-e07695f87248 | -2.64805 | -48.63375 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c108774a-15e3-3a7f-b452-2eb5ddcb7ffd | -2.16342 | -48.72466 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f2b5565-3c29-3c0d-a74c-c1377edb704d | -2.29043 | -46.51157 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd607d3c-fdd3-3ef4-95e5-678cb3e94704 | -2.20098 | -51.87749 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 064373ff-82f9-3f0c-9e27-c5fd5721d471 | -2.93163 | -49.50997 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 59e6fb35-4133-3936-a0a9-f49c5dd84405 | -2.7218 | -51.71216 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b8e5728-e639-3ae1-a3d8-93cb8d985177 | -3.72926 | -50.17562 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7483f86b-22d8-36c3-963b-2d38a8d68aa2 | -4.07753 | -46.07283 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f66f53-ef88-3062-9edb-87824d052457 | -2.21204 | -48.36454 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32904802-8454-378c-b658-3c0732edf2b2 | -3.23844 | -50.26151 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f72d3210-5f03-3523-8b75-319fbe82a9c2 | -2.04849 | -52.08367 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4f34572-9dbb-311a-a1c8-5d24bebcbcf1 | -2.04789 | -52.08737 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3779868a-5383-35d6-b1c4-638dbcc28cac | -3.53814 | -49.25942 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f37b3cd6-60d8-3b49-9fdf-8c5650082762 | -5.38528 | -42.76269 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18c41150-6975-3a51-903d-96f768ddee7e | -5.67044 | -41.75486 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README27.md)
