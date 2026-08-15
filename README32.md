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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53ef9681-6fea-3b08-8445-11b3973d6bbf | -13.26661 | -54.19419 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52ecfd69-9106-3bbb-8181-ff387c375a8a | -14.44152 | -51.90329 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 39a1376a-b208-33c2-a042-cc35f41b8421 | -14.43712 | -51.85675 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a6ac59f-c15d-3b80-934b-d0f93ccc23ce | -13.75411 | -53.42612 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 355a9232-49d3-3d6d-9be5-4ab8aae489d0 | -11.58549 | -54.67282 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20b8de0f-cf9b-3d2c-8894-8fad0bc017de | -14.98552 | -46.60909 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf61eb1-53a4-3a42-8914-b022d3303a74 | -14.06416 | -53.60486 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fb35c7d-fe1e-3ff7-a4ac-fc2a347ffa8e | -14.44346 | -51.88881 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 826e869e-e8a6-329f-b64e-7774ff912196 | -14.71673 | -52.88918 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37578b5-9bfe-33c8-bcd5-a5b92ce19757 | -14.40725 | -48.95873 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b75d176-f779-325d-973e-b3eae1165466 | -14.49369 | -52.03273 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41be8c6c-cf00-34b2-84b2-c7cafb8e71a9 | -14.44024 | -51.9129 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 386b8ec9-2de0-3924-b035-d3a865db71d8 | -13.75353 | -53.43007 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 220449a5-6745-38de-bda3-3b7e837e7d1e | -14.98522 | -46.61157 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a0246c5-39e8-39bc-9ff0-15a8f50616c4 | -14.42705 | -51.92882 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0374f1c-29b5-302f-a47a-f5ed9f2a6405 | -14.96729 | -46.62361 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1887fcda-a3a6-3c9d-8cca-b854c16e7ea9 | -12.1363 | -47.1641 | 2026-08-15 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a29d65f-3946-3439-b08f-5501265cce70 | -13.27229 | -54.20269 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c304e157-5f80-3c79-ab5c-a3d9d362e761 | -11.49937 | -54.63699 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b42f8dd1-6b87-31e9-9ab5-bd4fc9fbc135 | -13.42325 | -57.04929 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40f38bde-f5e5-3bcf-a8ee-69e6ad1c6ad7 | -14.44639 | -45.69242 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74dbf3c4-703c-32f5-851c-f870644d7f22 | -14.30793 | -53.09212 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3944be59-9ab5-3d83-8a2e-9eb73ec10c89 | -14.12911 | -53.68302 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b2815645-2984-3f4c-b423-59cd06afa1e9 | -15.0421 | -52.22617 | 2026-08-15 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc00b1c1-c7c2-38f9-a555-61fc708f4aa6 | -13.75645 | -53.43456 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c645b98b-19d9-34f9-9d83-d0ad303e628a | -14.41341 | -52.16263 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7464f05c-ec62-3ee8-b57c-675d529fefaf | -14.44716 | -51.94813 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5fd30c1-75aa-398e-a45e-b7b0e306e6bb | -11.501 | -54.62634 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 680131d6-1fb2-3c05-8434-2de5a9cff7ef | -14.42011 | -51.9229 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d4b8e48-4c7e-30c5-94f5-26a743880ea3 | -14.44878 | -51.91249 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b2182ba-952a-3c47-906a-c3530b59f309 | -12.90139 | -52.82994 | 2026-08-15 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 407779e2-1e72-3e8f-bed0-0d90b169f810 | -11.58664 | -54.68755 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17117551-dddc-3d6c-b152-8268c4f7a6d4 | -11.51602 | -54.63959 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fabc1171-5262-3801-aadd-fcdf69000380 | -11.59601 | -54.67087 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 079af204-9ebb-3031-86ed-8e3536301151 | -14.44339 | -51.95074 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfc1e709-ada5-3c68-8989-68933a3b2dfc | -13.44173 | -57.04122 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e99ee680-0a9f-3ebf-9b50-69cb6f88ad16 | -11.22903 | -54.82644 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f2ae12-aab0-30a0-ab14-12411c5d178e | -12.13861 | -57.22263 | 2026-08-15 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7e71fa-519d-3aae-aeed-4f3430ec2cfe | -13.75003 | -53.42952 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 223194db-5c79-3a4a-a0c5-f079918d1648 | -14.43575 | -51.94644 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 591c78d0-6ca9-3340-ac23-141a68c8ad40 | -14.45354 | -51.92957 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53a17b6-0fb6-34f5-a5c4-0b829eb6fec5 | -15.16071 | -50.06852 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5723e114-53bf-3c5e-a79f-3b598bffdfec | -11.49992 | -54.63344 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a68556c2-ddd6-3cb5-8f9e-f6558cfc3c87 | -13.75118 | -53.42162 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c796c041-b527-3ef3-a3b1-aecb92cf8d35 | -14.43955 | -51.947 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6063a28-7245-3143-b351-a7c6171e2cf0 | -14.44429 | -51.91673 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d437a65-6a41-32ae-b611-8ed84584b9d7 | -11.23566 | -54.8275 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a137fbf-7b7b-37a5-bd1c-c4a63ce0d7c3 | -13.2338 | -54.17451 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3ae9ef7-8fff-317b-b943-aec4781bbaf7 | -14.44743 | -51.92208 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b03552e-a09e-3e8c-9971-f5c16966fd83 | -11.50549 | -54.64158 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6991b0b6-c98e-3851-9498-e572fa4d8642 | -14.7561 | -48.24419 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c64da146-62d5-3b6e-8ba6-df7c12bd52d1 | -11.49931 | -54.61515 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b215d315-1818-3769-a993-2c9f91bfbf49 | -14.44341 | -51.91827 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| edc2f2ea-88cf-3fe6-b384-d785a5e9a538 | -15.15742 | -50.05975 | 2026-08-15 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c28c28e0-515f-393a-a058-cc2d519e9308 | -14.45419 | -51.92476 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69eb6ce4-45aa-35f9-b0db-bd305520db41 | -11.24067 | -54.83911 | 2026-08-15 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fbbca75-6db1-3fc1-81e0-7f20b2d8a8d5 | -12.69344 | -48.45112 | 2026-08-15 04:59:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4c8d365a-734b-3ce3-93ba-0a903941ba38 | -14.46953 | -53.07683 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b67057d9-20a8-3e31-845a-48d4e1334f6c | -14.05893 | -53.6648 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ebe1ce3-cc74-3777-86f2-62c6b16b1fe8 | -14.45167 | -51.91459 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa34ccbe-2b82-384c-bbb2-0f0a4e079ee5 | -11.4921 | -54.61767 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d702444a-4186-36f8-961e-25c9e373c559 | -13.26322 | -54.19367 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ece0c6e-3c32-3de9-9b6c-a598377025e8 | -14.46019 | -45.67342 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 616444a3-ffbd-318d-b532-9ec24f1daf6d | -14.13259 | -53.68354 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a5d46a0e-7b6c-323b-8d37-19100923f08e | -14.09285 | -54.52612 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ae6a72-efdf-3c49-a177-b2e24155d527 | -14.1233 | -53.67411 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca4d1511-a4b8-3515-a724-93db1954b24d | -14.08948 | -54.52558 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 120494ab-2ce4-3bc8-af58-d887d1f8dba6 | -15.03727 | -47.0337 | 2026-08-15 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4430de6e-a35c-34e3-a2a4-83b77ffd1d55 | -14.46473 | -46.76725 | 2026-08-15 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10d86106-3cbb-3ed4-b7c1-db8afdf5f61e | -13.25191 | -54.19262 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcc4ea15-136b-34f6-bd4c-e278f12c904d | -12.146 | -47.16851 | 2026-08-15 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a87f9c6f-6b7d-3eca-8f18-22e3337f9323 | -14.06182 | -53.66931 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08199f49-283e-3a52-80ea-e6f99f94bd34 | -14.43981 | -51.92095 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf62cdc-412b-33b1-85dd-7a5ebfaf3e88 | -14.93842 | -46.63521 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab69f580-ff7f-34ea-8958-01405dbbe25f | -14.42391 | -51.92347 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50997f66-925b-3f11-82af-6a7881d5edea | -13.48194 | -44.04169 | 2026-08-15 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f310c866-8e91-3d42-b506-9a5a9c6af7a4 | -11.50155 | -54.62279 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f0c600-5766-36a4-a5a9-8848eda151c9 | -14.74592 | -48.24661 | 2026-08-15 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a7445ed-0560-3a33-9021-226b0137c2f8 | -13.24398 | -54.17614 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 851a60fc-a7c5-3191-96b6-604f8fd760fc | -14.13317 | -53.67961 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e05ce3dc-3495-3030-b701-7ff90f1ec73c | -14.08508 | -53.60798 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29d9454f-87e1-30f4-9456-fe152a5e793d | -11.51269 | -54.63907 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27ceae29-fc8b-338d-b773-33746418547c | -14.44974 | -51.92899 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cf1bdcb-08c2-3fcb-a4bd-46f6516cda22 | -14.98581 | -46.6066 | 2026-08-15 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 384fa320-23b6-3a8a-aea3-c93727edba30 | -14.0934 | -54.52243 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91810a5c-9547-3a75-8556-c22fbad156b6 | -11.49102 | -54.62477 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3480996c-a7d5-3e1d-abce-f5be0a46655c | -14.45571 | -45.67207 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10550204-4542-3fa5-9b61-c1e6d44c2b1c | -11.5027 | -54.63751 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84d66014-db9a-3bd7-af74-45cf175c4f8b | -14.32338 | -53.06047 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2740ab02-34fc-36e1-bb0a-3a4348f290f0 | -13.92175 | -53.95403 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3eb29512-1f63-3cee-9ab7-8f7f26551f8d | -14.52158 | -53.292 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c1bec12-7aa4-3789-826c-66b3025994ca | -11.4938 | -54.62885 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc2593ef-43e5-3e66-b32d-dc1a9ff90844 | -13.25135 | -54.19634 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ecc44a37-88f3-3382-bc12-03e682c257e9 | -13.24115 | -54.17187 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17ba3e1e-911d-3c1d-a3a9-d2870b12ef28 | -14.43265 | -51.94429 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa19f0ab-7d5e-3006-8fba-fb30ad75b01c | -14.13607 | -53.68406 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ee27d8f-34bf-3042-beb2-27218dab1065 | -13.75995 | -53.4351 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c75260-528f-3828-b481-e3fb6b858910 | -14.42525 | -51.9139 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3faab2e2-eccb-3542-aaeb-46a88163b0b8 | -14.72523 | -52.88148 | 2026-08-15 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 926534a4-5e52-341a-8bc3-d9aa0918f086 | -14.45212 | -45.69314 | 2026-08-15 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
