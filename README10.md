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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 303f9b5a-9537-3fec-8cf2-95d377a5fa75 | -13.33377 | -54.31249 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6acad80b-d09a-39b8-bfb3-98ad1e534948 | -12.46024 | -46.51736 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a9c2064-e799-3d25-bd34-8d5518731b6d | -9.70156 | -47.7027 | 2026-07-22 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85acaa33-1e95-3c34-afe5-7cb3454fe639 | -12.32784 | -50.00824 | 2026-07-22 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a02e37-1b8f-37c9-ab27-d84f0e1d17d1 | -11.6302 | -58.28122 | 2026-07-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b57071c-7ac6-3eab-8766-46c252290fcc | -12.52698 | -48.53474 | 2026-07-22 05:04:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d92f76-9c7a-3cc2-bd2b-a400358b60b9 | -11.40132 | -47.50357 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d43f9ffe-45f6-3780-bc2d-a2e57ade2271 | -11.63337 | -48.54851 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 273c261a-2a7f-39d2-ba58-e02deebfb3ab | -11.31113 | -56.78253 | 2026-07-22 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 977e1e2f-a031-3ac7-a0fb-b6721b3f1a9f | -8.74967 | -49.08045 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcf6309e-c061-391a-849f-ffc1436f1636 | -11.39993 | -47.49145 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93679729-3579-349f-b53b-b2ee8bb871d0 | -12.23306 | -46.58417 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a45edc60-786b-3beb-b2a9-1754601bf9d0 | -11.90956 | -43.84638 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5994a812-676f-3995-96ce-07f4e728067e | -8.75079 | -49.07246 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1a1a6af-9f99-350f-a415-ae99ccaa4ed8 | -11.39794 | -47.49149 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b60f5bfd-e223-3f52-ba66-8e3638ca4b2e | -13.33602 | -54.32048 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a36e046-3807-3178-bd80-909363c628cd | -13.33264 | -54.31995 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65835837-0333-3451-a2b9-84d1d415159a | -11.81165 | -47.33494 | 2026-07-22 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 667f8ed1-dd86-3deb-bef6-8bd1bdd2d21e | -13.85077 | -53.90298 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccde74bf-6bb1-33ec-aa70-733f6bc47e14 | -10.51058 | -50.27873 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0424f293-a22a-3745-aeea-1d616f5db223 | -10.16486 | -56.79976 | 2026-07-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e8112aa-5987-3047-9c05-bd7ac5a70649 | -12.52761 | -48.52998 | 2026-07-22 05:04:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e83d74ba-1ee9-349b-83f2-eb9e0f3df0f5 | -10.42613 | -50.19827 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bb58fc4-d834-3d49-8f71-92f2ea97d14f | -7.61187 | -55.26709 | 2026-07-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5ebbd4f-d897-3015-a3ea-397fe3bef379 | -10.0602 | -60.49939 | 2026-07-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e7a654b-baaa-31b9-91b6-9ee41b9300d4 | -9.10467 | -59.39855 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e917d7-9887-3cd7-8cb0-da0710282019 | -9.64187 | -47.8099 | 2026-07-22 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5668675a-0cb7-3737-b45f-cca27de2db99 | -11.88887 | -43.82943 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4377e24-bc00-35cf-886e-6d1ce963bf91 | -11.40626 | -47.50397 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9a189ef-38e1-334d-8455-550703dee47d | -8.49151 | -54.77741 | 2026-07-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd3510e1-e596-3432-a50c-2e3f4032be8e | -14.25593 | -54.7618 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e9dac38-74a9-3f7e-ad37-465a4fa8b970 | -8.75757 | -49.08571 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3199c7de-960c-3e57-bdd7-121d5ac43710 | -9.09998 | -59.40273 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd6cf3b-8dbf-3d49-88ed-9c10e1768456 | -12.66649 | -48.21481 | 2026-07-22 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b453089-4514-3b50-a12f-cd23346ce8cd | -9.20433 | -49.82586 | 2026-07-22 05:04:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0374a41c-2566-30dc-bde1-c4f606fccbf6 | -13.33207 | -54.32366 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ded3f0-d407-390c-a59c-41cc52ab7df2 | -13.31966 | -54.31406 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bb7fed1-fa3a-360a-b58c-c795cebaa546 | -12.88116 | -58.28682 | 2026-07-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a752b0c-b858-3159-b03d-461e77de8c67 | -11.8109 | -47.34072 | 2026-07-22 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14dab2be-0c8c-3252-89e4-984b5a28068b | -10.95374 | -49.81173 | 2026-07-22 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eea0cc19-6068-356e-af96-aa6189434e56 | -12.46066 | -46.514 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dddb195a-2e27-3d65-a38f-418b0ad5c074 | -11.40413 | -47.49775 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c868cde9-f3e6-3ff7-bdeb-63e21c1cddce | -11.88618 | -43.82809 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 46da1851-0fcf-3caf-8fd9-10797fff9338 | -13.31402 | -54.30553 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff060f42-5747-3ec1-9388-b2a913ecb8e2 | -12.23264 | -46.58746 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f48cb2fe-8548-305d-b7ec-1c930d0e317b | -14.43411 | -56.4478 | 2026-07-22 05:04:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b93a44d-0e56-31ee-9477-8a0021901773 | -8.52541 | -54.75825 | 2026-07-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d133017c-e4ac-325b-bd1a-0c46e349b387 | -13.3095 | -54.31244 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a85dfb4e-78d2-342e-95d3-6bce98c389c0 | -15.24115 | -48.25154 | 2026-07-22 05:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a8e1066-9d7f-3ea3-a291-1e5175d79955 | -12.88463 | -58.28743 | 2026-07-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24cdd7f4-0648-39eb-8db9-dd52947639f0 | -13.31797 | -54.3252 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82932d87-2b67-3638-be9f-0ccf6e040352 | -9.10081 | -59.39789 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b362e1-a362-3ff7-9967-27f9184b8b3d | -10.54472 | -50.26926 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf5fcd83-a22b-3192-8f08-0d49c3c10aad | -13.3253 | -54.32258 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d3f06f-00f8-3a84-a9c2-6c23ea7fd5d9 | -13.32587 | -54.31886 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2254cb91-2321-381c-adcf-8d9515e7d8e0 | -11.33344 | -48.00706 | 2026-07-22 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eee21b19-8480-3017-93a0-e98d1d41ccfe | -11.33506 | -48.00234 | 2026-07-22 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530fd605-cc89-3d2e-8e0e-95456a353ed6 | -11.55188 | -52.77474 | 2026-07-22 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c630f297-32ce-38ed-bdb8-ab670c0e02e8 | -13.36935 | -54.30673 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6434ab6f-6ed9-3a5b-bac0-b051e0d42f75 | -11.99155 | -50.54924 | 2026-07-22 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83839e66-6987-3bb5-ab2a-21644af2f7d3 | -13.32925 | -54.3194 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3afc1b4d-64f1-3fe4-a574-37941feb5aba | -7.68459 | -55.36411 | 2026-07-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b245a2b4-2135-335c-9066-ca1b326f1289 | -13.33659 | -54.31675 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8036e481-da96-3c09-96c4-c1d6d2019ea8 | -11.63922 | -48.53961 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81b9a1b0-b680-330a-87c5-d4436666f507 | -11.88826 | -43.83441 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d8f30fa-6c89-37ad-a891-c554a2dff1ac | -9.22642 | -48.55962 | 2026-07-22 05:04:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e012f0fe-f0dc-3b83-9f96-01956d7337e1 | -8.49096 | -54.78088 | 2026-07-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97848cd4-02a2-378e-806a-c1e2198e339e | -10.43016 | -50.19885 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9abe16b3-fba3-394f-9cde-24477e1683e1 | -10.13937 | -55.3995 | 2026-07-22 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3aacefe-1096-3351-b955-7ce2f4d12c2a | -8.746 | -49.07579 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48bf440e-dc3a-3919-bd04-6699247e599c | -11.38379 | -47.48504 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a344434-07c0-374e-9d88-00f1f21a0226 | -9.11891 | -61.09104 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbffba87-08e4-363c-8189-ce052314cfc0 | -12.13872 | -48.26102 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94595456-a434-3ecf-9a9f-d23af7afb991 | -9.47932 | -57.31903 | 2026-07-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8d0064-4b43-3436-b8d8-53e50d354b2f | -13.33941 | -54.32102 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3cf4ef9-f7b2-3e05-8c05-9f69df3414ba | -10.63296 | -47.48696 | 2026-07-22 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| db2dbced-eb7f-3746-904b-384e033380a6 | -8.75023 | -49.07646 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27087e2a-55ec-3e6e-b1e4-40567b8e2a05 | -8.74037 | -49.44511 | 2026-07-22 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6c89c57-4509-3eb4-b54e-6cd07a908535 | -11.99204 | -50.54566 | 2026-07-22 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 580ac9ab-1719-3f40-aa94-acc1d16db5e9 | -12.5209 | -48.25132 | 2026-07-22 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d3f0d16-255b-38e7-9bc5-e24a17242c00 | -9.22617 | -48.5582 | 2026-07-22 05:04:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20dd1249-8e65-35c4-a81b-f3d21980e3c0 | -10.54421 | -50.2728 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29060767-ce0b-39d4-bca8-9cb7685c7bb1 | -10.62808 | -47.48641 | 2026-07-22 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3134a0fa-30d3-32e7-86a2-0f211dd2e652 | -14.2593 | -54.76233 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9038a1b4-5cfb-3c6d-acbb-0d64f1709a80 | -11.33414 | -48.00188 | 2026-07-22 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6501d2b0-3a06-33dc-b4e3-48379e360872 | -7.60911 | -55.26307 | 2026-07-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f899dbb-d24d-324e-9146-3b1c30f2d14d | -9.37978 | -47.09038 | 2026-07-22 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc806693-251e-3512-aba1-c125bbe45335 | -8.48821 | -54.77689 | 2026-07-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1116ef0c-8662-323e-9bc2-881527b38f4f | -13.3174 | -54.30607 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec0d2add-31ec-30a0-9475-690973f53522 | -13.31684 | -54.3098 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3233b02-db2e-30d9-a684-83b327676829 | -8.75813 | -49.08176 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ddb1ecc1-24fc-31ce-a4e0-6cfa18ef2ffa | -13.33998 | -54.31729 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88c5c7ee-edb1-3b5a-be9d-f49feda743ce | -15.24009 | -48.57228 | 2026-07-22 05:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| accd08d4-2b6f-34aa-af04-d6c1db964746 | -8.49206 | -54.77394 | 2026-07-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c7d0521-faa8-30f4-843d-aca2ae0a0c1a | -11.91584 | -43.84719 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37478136-e285-3e6f-8fdf-c50673c74718 | -9.11461 | -61.09024 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c7806ea-40e4-3967-b466-40a00ed5ecd0 | -13.32982 | -54.31568 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b1081a5-dd7e-3fc1-be21-b41d1c71738f | -8.83131 | -47.07102 | 2026-07-22 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e10689b7-7f0f-3ad9-9cea-94753ca2d6a3 | -13.32305 | -54.3146 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce03d503-8cdb-3848-99ed-8f32634a9bb9 | -16.80756 | -54.59058 | 2026-07-22 05:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
