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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 843bf7b6-dfed-3765-a658-d120ff15595c | -14.29181 | -47.18608 | 2026-08-16 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fec02c8-160f-3a46-b7d9-170940ae56c2 | -16.88671 | -54.1494 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d9ce6ad-77b3-3fb0-bff8-dd129e71dc17 | -15.17647 | -50.06441 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69ea7d49-3d5a-3a8c-a0d2-9fb79ac4f658 | -13.42852 | -57.05005 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c4feda-5afe-3ece-bdd5-e669568b4af5 | -12.0628 | -58.04362 | 2026-08-16 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89080958-04e6-3051-8e5b-782a4ca964d7 | -13.5006 | -48.23423 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd11c208-c536-36f1-a3c0-874c6662ef87 | -14.41611 | -51.9404 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 889d92b8-4d76-3096-8cf7-ab711abb369a | -14.3914 | -51.88137 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bf12842-d321-39de-9a2b-74f75807d781 | -13.77751 | -53.82444 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85d25396-d586-31b0-b227-91a33ae88e60 | -14.48483 | -45.6908 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7896a5cb-3f69-33ff-b690-842148f8a0c8 | -14.71466 | -52.88345 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9f93e47-0ed4-337f-aa45-8901dd9f1190 | -14.65551 | -55.87728 | 2026-08-16 04:42:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6bd48e6-ebd2-3893-a7c6-305e4b04dbb7 | -12.70002 | -48.47533 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cacd2b0-099e-3375-bebd-1ff020df18ab | -14.44036 | -53.29861 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 723df198-170c-30c2-9a31-025b3973f8fd | -13.80402 | -53.81661 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ff1e006-025b-3d86-a920-3045eb07dbe9 | -14.3986 | -51.87889 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 584d5281-a262-3b49-9039-0a645d643a95 | -13.49051 | -48.22838 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f508fab-92f8-39c0-be5e-91f2ab9f592a | -12.74821 | -48.43914 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8da6656c-caa5-34d3-8619-ad7fd183d237 | -15.98347 | -49.16022 | 2026-08-16 04:42:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f78bbef0-73a5-35ae-b151-d722229d4a6b | -13.27788 | -48.69621 | 2026-08-16 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0fda4ed-409c-363e-9c1b-cfb858092f48 | -12.68663 | -48.46907 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5647c963-6dc6-3867-be6f-952fbf9e3315 | -12.20593 | -52.86819 | 2026-08-16 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea2fc72a-09ac-3283-b45a-e24616a81a14 | -14.90181 | -46.63024 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d4250196-ee59-3fa7-b8c8-659b13a9c12f | -13.69465 | -46.24594 | 2026-08-16 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f0d1406-ca19-348c-b047-7d48b73167ee | -14.11978 | -52.91649 | 2026-08-16 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916a9a11-73ea-31a7-9bcf-42d1262cc2dd | -13.78018 | -53.80837 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad4d5d52-fd15-33d6-9532-cb8aad189c10 | -16.78279 | -49.25151 | 2026-08-16 04:42:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7247cec2-c76f-3c71-b6d5-97a360aab757 | -12.90452 | -52.82857 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fce14b57-6d02-3283-bddd-e3798464d548 | -15.04877 | -47.02205 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5383bbc1-37ed-384c-9337-6e40c2c98702 | -14.07729 | -53.70655 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 786c2971-aa64-38d7-8217-62d08851fe67 | -12.69889 | -48.48312 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e9243942-91ed-3820-b749-185e692fefc9 | -14.21478 | -51.81524 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 584c7408-fcac-39d6-84b1-0e3edb19fb95 | -13.79751 | -53.79053 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a683555-88e0-356a-a32e-a69fe7a62d19 | -13.81721 | -53.76477 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf6d0a6-0b3e-3d1a-b14e-f524bd454e42 | -14.41419 | -51.84489 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85507f0d-8e6f-3887-8e0e-5a0c731b9503 | -13.44398 | -57.03658 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26c9c559-809c-3827-97f6-d9c9e842f03a | -14.46784 | -52.00011 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fade224-7b0a-3bd8-ab33-2437082ef9c6 | -14.48024 | -45.68283 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 231b03d1-d3df-3444-8a07-1a6106636ac7 | -12.70588 | -48.48423 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5beddd23-d6ae-3b3d-889c-20db2dfabbb8 | -13.69921 | -46.27225 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2af16da2-45e2-3b64-8d67-faa840e5f0ee | -15.09164 | -48.70175 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12101191-6b86-39a2-bbd3-5b9c00fd9734 | -15.69837 | -47.45747 | 2026-08-16 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 175dab37-dcb7-3f60-a75e-c843f9331eaa | -14.42138 | -51.84243 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad034a90-14fa-306c-af95-4fd1d2ba1e80 | -14.74314 | -49.24588 | 2026-08-16 04:42:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4121e74c-8bbd-35dc-8ea7-de6fc30bcc47 | -12.89833 | -52.82367 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeac4862-22e2-30e7-8936-ee8adbeacc19 | -14.39571 | -51.91869 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80f612c4-4616-3200-b1e7-6b45c0126819 | -16.87504 | -54.1556 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ba18f93-6fb0-336c-932c-f6a09fb73b93 | -13.52745 | -46.24577 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38dc8174-ef41-33f1-af6e-8cc073adb58e | -12.66844 | -48.46318 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f66eaae-a231-3732-ba23-7f9da1d57a96 | -13.78452 | -53.82562 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13dbe139-0fbb-3b0b-a898-9c9a82cd1102 | -13.68596 | -46.25013 | 2026-08-16 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 511b5114-b9d9-3235-b029-1281c8abb441 | -12.67367 | -48.45202 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81311f37-f68c-3727-acfc-4701e98bdb7a | -15.22761 | -57.64931 | 2026-08-16 04:42:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ebdd9cf-83cd-3adf-9fee-4537f130cc08 | -15.15925 | -50.07668 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb0b395f-951d-3f6d-af85-4b36315cf7fa | -14.10853 | -54.51867 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bae0acbe-a943-3644-98d2-d17ff59cd973 | -14.92842 | -46.61206 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 775d9dbd-8d79-3312-9486-27595d89a72c | -14.65705 | -55.87974 | 2026-08-16 04:42:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a18bacb-d420-3194-a191-579d73d93193 | -14.41807 | -51.84188 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efc12ab2-172e-3f3d-9804-7d50953139f0 | -15.06021 | -47.03511 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d81f65b-9772-3c55-9d75-02fe380713b9 | -14.75588 | -56.34464 | 2026-08-16 04:42:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae4ca167-26dc-39a2-9880-0250e75206cb | -12.74593 | -48.43022 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0664cfd3-1e61-3881-b695-236252a6e8c0 | -15.27224 | -56.12143 | 2026-08-16 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e0d5218-ed42-3548-b9de-fea146fb8b41 | -14.2956 | -51.94979 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63169bd2-cd9c-3bc0-a929-a0c2906f0f96 | -11.58367 | -54.68683 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 75df6a93-af1b-36a6-987d-15abe7f79011 | -16.87914 | -54.15223 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aecc88e5-d69d-378e-9881-28a5332c808e | -14.33043 | -49.17329 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d87c34b-ed0c-3917-8eb2-f1b754e6c6e4 | -14.29285 | -51.94567 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c9fcc73-4f98-33ca-92fe-34731848ab6c | -12.68596 | -48.44898 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71c8db2b-d9da-35f5-ab9d-0e3377f88e51 | -12.68371 | -48.46457 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7b3b16a-7ec0-30f8-a89b-534a36ce13e7 | -13.69829 | -51.87594 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458f51b7-1a6c-3e82-8734-29860752bc67 | -13.43955 | -43.85355 | 2026-08-16 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5bbbc9e2-bade-354f-b31f-bd3cd2edb114 | -13.49407 | -48.22892 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d22ca473-bf9f-307e-880f-4216c196afb8 | -14.46815 | -53.08287 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d01afa39-0d61-3df5-b6a6-cefe9f440018 | -15.14672 | -48.62151 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ce89ee8-a5ab-3fec-aa28-3bfffeed05d6 | -14.07019 | -53.68491 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09f9a116-7fae-3a47-9524-883430dd9038 | -15.1658 | -50.06644 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf3f9f97-8a5d-3044-ba00-1ae0eb6dce25 | -15.54255 | -47.38581 | 2026-08-16 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90d27d7b-bd12-3eac-981c-0890ef11d5b8 | -15.23185 | -57.65016 | 2026-08-16 04:42:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba6a1a94-7c3d-34aa-ae01-2a4a30f56c7e | -16.88883 | -54.15801 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c290b33a-4591-3f7a-b7a1-b666e42d84b2 | -15.05717 | -47.01842 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 529967ec-a572-34b5-bcf1-36b18b388bd1 | -13.60043 | -51.48409 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38b16af4-cfe5-3511-83f4-c2ed0217bcb0 | -12.90112 | -52.828 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 655a68e4-76af-3f65-868a-d728bc518409 | -17.3552 | -45.62148 | 2026-08-16 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdfd3fbc-daef-31df-b7b0-544f618d6b23 | -13.50416 | -48.23476 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ef535f6-bb8c-3e1f-bc00-8d08813528a0 | -13.80168 | -53.78705 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94a3654f-a919-3e97-832c-cd44c8dc178c | -13.79219 | -53.82283 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af3506f5-3a94-3ac0-8680-86e5001354a3 | -12.71105 | -48.47325 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07c82bff-3236-3103-95cb-724d28504408 | -13.79115 | -53.78549 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fa70ba0-d516-3e18-9c81-5330efbe7348 | -14.96272 | -46.62738 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ae81e6b-0227-3701-9dc5-6a544198b4c6 | -13.50476 | -48.23056 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baf1bb20-7ebe-39af-ad24-edd90bdd1255 | -14.2994 | -53.06536 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ef3ce47-07f9-341d-b893-e45917776497 | -13.79969 | -53.79916 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 233b3f42-1420-3c8b-852d-4b98e3f0436e | -12.67427 | -48.44799 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d1a961c-aff1-37d7-8056-08319c24257f | -13.5 | -48.23848 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23e3be68-6799-3bdb-9f83-d27327ebbf17 | -11.57913 | -54.69088 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea535bce-e83c-3262-901c-c813921ac16d | -14.92767 | -46.61777 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6f0302c-f977-3c5f-a2ec-d40210c05595 | -13.70494 | -51.87704 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09a5149a-1697-39e2-8227-7e5afa8ad5ee | -13.80336 | -53.82063 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55047bfb-403d-3e25-b15a-84b13f190904 | -12.7488 | -48.43509 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd4413e0-08ff-3354-bdbe-5f7f3db73757 | -14.2231 | -51.80564 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
