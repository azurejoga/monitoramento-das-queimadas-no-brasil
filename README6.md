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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7fef81c-e842-383b-a932-ed8fa5f2fd8f | -15.8778 | -43.32912 | 2026-08-09 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f88ccdb2-2d9d-3855-922a-2e7ffbe5a010 | -9.4657 | -40.32397 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.8 |
| bcd0f72f-a851-351a-8ead-142e8c6f5443 | -11.04467 | -44.27931 | 2026-08-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a8edc69-1354-31bc-84a1-cd802173fe26 | -14.92022 | -48.23518 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 13429413-f114-3100-888d-662da6e62faa | -9.4723 | -40.31458 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5e76ca9-0696-3d7c-935b-c49afa81ca9e | -10.90487 | -45.12148 | 2026-08-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47195192-a75c-3758-b2db-2deb42acfe52 | -15.83739 | -42.23259 | 2026-08-09 03:32:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5756dfc4-6d06-3d09-b667-2074b7fc67f8 | -9.47519 | -40.32563 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 089a3c6a-936a-3e2d-98fe-93cd5d8dc34e | -14.91182 | -48.23995 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 38f39324-a6f8-3da2-8856-3a5c2dd1ae10 | -13.53381 | -44.03665 | 2026-08-09 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9685123f-2d2f-3311-af56-47d9269c9345 | -9.47044 | -40.3248 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.2 |
| e95e2589-2ed5-3aaa-a2b5-c102791d8513 | -10.9083 | -45.11961 | 2026-08-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfcd9145-bfd9-3083-aefb-b3f3eb2cc4ee | -11.78271 | -41.19807 | 2026-08-09 03:32:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62dce5ff-46e7-3ec9-80bd-14f42c46a4d3 | -15.65142 | -43.29231 | 2026-08-09 03:32:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 706602b2-2c17-391b-8dbd-2b96bf276965 | -14.90629 | -48.23175 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20fce255-e2cc-3cfc-9e0c-caadc2e790a1 | -12.11257 | -47.22517 | 2026-08-09 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bad3f56-948d-3da9-8568-a538dc3843c4 | -10.48865 | -46.63168 | 2026-08-09 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 41911fc9-797e-3621-85f7-76bad35824c6 | -10.88924 | -37.08017 | 2026-08-09 03:32:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21369282-15e1-3eec-af2c-811c5fe4ed0f | -15.87202 | -43.33117 | 2026-08-09 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d401efe0-8f26-31b9-a7fc-b0e860b46787 | -9.4645 | -40.32692 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9d62add3-b4aa-3638-8146-43c0bfde0931 | -10.91112 | -45.12294 | 2026-08-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d0c0220-5fbc-32e4-9cd2-21f62be8ff69 | -14.9133 | -48.23325 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34172458-e402-3202-b9af-a30d0489cdef | -11.04555 | -44.2748 | 2026-08-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 973044b7-d94a-3bcd-bddc-5bf0fa24b4a5 | -11.1529 | -45.93566 | 2026-08-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4c5d5970-6064-3d91-87f0-eec0d343d9a7 | -12.11819 | -47.2267 | 2026-08-09 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e9ddc420-a538-3f20-a998-3924803bfd35 | -13.52817 | -44.03561 | 2026-08-09 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 203447fe-3484-30df-9596-f80723173390 | -19.57682 | -42.58858 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2cd69e65-d0e1-3bce-8fc3-d5e2dffce86c | -21.66214 | -43.63472 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 80ff9452-a3c8-37d4-ac36-7b6c4d4eda42 | -20.27264 | -41.65285 | 2026-08-09 03:34:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3435fb3c-6fbe-300c-8cfa-b9c84f9ebd73 | -20.38205 | -42.00595 | 2026-08-09 03:34:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4aabd96f-310f-3597-a74a-771549404abf | -20.78343 | -41.15429 | 2026-08-09 03:34:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fc0778a5-ee22-37a7-a731-540467e3f69c | -19.58166 | -42.59114 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7547e9af-84f7-3fe0-a991-00814eaf4e8d | -21.66806 | -43.61195 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f892f40e-40e9-341b-8f42-dce211d05c54 | -19.58528 | -42.59704 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 8030fdba-b327-36b4-a9b7-d60be515894e | -20.38646 | -42.00657 | 2026-08-09 03:34:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 741ffb38-39c3-3ac8-8af1-1143b12afab9 | -21.3248 | -43.77772 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9444c24-1914-31d0-92ff-b39ca3edd9f4 | -22.90663 | -42.94746 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ce36d8d6-b0a8-3cfd-b498-54906921d460 | -19.18582 | -47.19155 | 2026-08-09 03:34:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb72e31f-98ee-3d5f-b444-18d4bb66b80b | -21.74657 | -43.564 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ab94847e-a4ac-3694-abc4-d010261bd267 | -21.27909 | -42.93985 | 2026-08-09 03:34:00 | NOAA-21 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f4e37fdc-e576-34cd-b07d-cfca2e6d2b82 | -20.37854 | -42.00077 | 2026-08-09 03:34:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4690a9a0-08bd-33f5-b721-d65ad027a7cc | -21.08737 | -45.80797 | 2026-08-09 03:34:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9c8166ed-08c3-35b3-817f-ee01d1a8ba12 | -19.59055 | -42.59158 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee49d99a-a55c-3b97-be3b-a6597d2aca88 | -21.31615 | -43.77307 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2367bac4-fa51-3b8e-ad72-5bfef0c10d21 | -15.76521 | -47.76872 | 2026-08-09 03:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2af6616-9814-3d18-b6ba-d5e7716e2034 | -22.07435 | -42.34274 | 2026-08-09 03:34:00 | NOAA-21 | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| b66b4df4-6446-39bb-94d9-eb0f36540ea2 | -21.66916 | -43.60667 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f7a9f947-931e-38e2-8b4d-9a31b47bc5db | -22.18855 | -42.47723 | 2026-08-09 03:34:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0fdc266-1c42-37a8-bcd0-ba245041ad12 | -22.90604 | -42.94551 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e7be53c3-187c-3475-b670-785f603ab34d | -20.54107 | -42.39984 | 2026-08-09 03:34:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34af2881-bb07-3fb1-bcc0-4811c2b4d4b4 | -22.19204 | -42.48243 | 2026-08-09 03:34:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09f7225b-8f7e-393a-806d-e3382b8ba32d | -22.8904 | -43.50516 | 2026-08-09 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0e17cc90-2f2f-34b2-969b-0a70592fd276 | -18.6597 | -40.78748 | 2026-08-09 03:34:00 | NOAA-21 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2e1a7a35-f729-302b-872d-533f4f8ab19d | -19.5908 | -42.59324 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0fd35c6d-3d6e-3e9a-8f64-ca2280cad081 | -22.90784 | -42.93668 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2aa707c3-7246-3a99-809d-826de1f9a5aa | -20.54563 | -42.40015 | 2026-08-09 03:34:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a9041330-c3c3-3cd6-a325-ac9345e3050f | -21.66365 | -43.63297 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9e35c79e-9d97-3b71-bd70-ab8102b59bd7 | -21.85972 | -42.03613 | 2026-08-09 03:34:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0615963c-d9e6-3949-9047-eb421927c3f1 | -21.27455 | -42.93886 | 2026-08-09 03:34:00 | NOAA-21 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8abaaa2f-e229-3b88-a491-69c9d3c1b8b2 | -19.58626 | -42.59203 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e112dc3c-59d3-3aea-bf79-1d8bc8db9bda | -20.66508 | -45.02372 | 2026-08-09 03:34:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f969959c-5935-39ac-b371-f80c90894527 | -22.89086 | -43.50316 | 2026-08-09 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 534a72bd-f9b8-36bd-b7b2-f0c3e9336320 | -21.60176 | -43.46434 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc1245cb-ad0d-338f-b051-e04cbc77e6bd | -20.55671 | -41.24192 | 2026-08-09 03:34:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d19a0165-d3bf-3809-abf0-127853769516 | -19.18475 | -47.19623 | 2026-08-09 03:34:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 306d02f0-b5fd-36c5-97b8-c3ddbe56e0a8 | -21.32115 | -43.77129 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77a35b83-b52e-3042-aa45-935c3645a8f8 | -19.99237 | -43.97284 | 2026-08-09 03:34:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 100d9dfe-1bea-39e4-b4d3-f39a0a1524ef | -19.58957 | -42.5964 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 532a6fbc-96f5-3bea-8373-810caf736eba | -17.76203 | -42.79988 | 2026-08-09 03:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e56aad31-cf82-30dd-b50f-f37f56f53c01 | -22.90837 | -42.93866 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e8044cb3-39bf-33de-9c50-69565d2af60e | -22.29467 | -42.60855 | 2026-08-09 03:34:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2747cd33-49b8-3e6f-ac3d-620c5649a92d | -20.97524 | -43.92707 | 2026-08-09 03:34:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd2fff5a-2644-3bfa-b068-ce3f17f52878 | -21.67216 | -43.60946 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 64d4c627-3536-350c-99c5-5ec4d75066ab | -21.32094 | -43.77402 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bfd51f0-39c2-35c7-8e62-252429de70ca | -20.2734 | -41.64889 | 2026-08-09 03:34:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8089d614-9234-3e9f-871f-0ae1d36b64de | -22.22832 | -43.03788 | 2026-08-09 03:34:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7c7010ef-3214-3fa8-b958-4aae4cf007a3 | -20.66578 | -45.02043 | 2026-08-09 03:34:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 87411615-914e-3e8e-9e53-8af658bb4c15 | -22.2991 | -42.60912 | 2026-08-09 03:34:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f720d6d6-6287-3ea6-8f98-218f572da913 | -19.19191 | -47.19307 | 2026-08-09 03:34:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d623be2-930f-3292-b03d-e41eea2e4c4b | -20.58052 | -41.91782 | 2026-08-09 03:34:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b33d215e-8ab2-3469-b5ed-9c2851c73934 | -21.66323 | -43.62932 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ccd3690-80cd-346a-a640-d4e67e4bf8ea | -19.09589 | -48.31104 | 2026-08-09 03:34:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b473a86-c932-3d3f-99f3-a7e7f104cbdc | -21.31636 | -43.77032 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 374562ba-a49f-376a-88fc-13ddc20860e0 | -21.04547 | -45.68328 | 2026-08-09 03:34:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ee9179d-1d56-3dc8-bdae-60123adf568d | -19.57706 | -42.59025 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eefdece3-d803-3538-9d22-5ede41d156e4 | -20.97046 | -43.92564 | 2026-08-09 03:34:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d49cbbe8-1d6b-350a-a291-f621263ab333 | -21.27315 | -41.74407 | 2026-08-09 03:34:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f07513e3-2c28-3542-bee9-eb6d8c30e9e8 | -21.92468 | -43.0404 | 2026-08-09 03:34:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c882450f-31bd-3936-ac3b-ae5ec20fafde | -20.38291 | -42.00156 | 2026-08-09 03:34:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dfe0b2cb-3529-3a6a-823f-98a9eea7f3f4 | -22.91041 | -42.94664 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2071238e-8155-3028-b15f-2198367ac874 | -21.31726 | -43.76758 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2401016f-b76c-3071-af4e-4939b90948e9 | -22.29827 | -42.61331 | 2026-08-09 03:34:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 188213bd-c915-3a66-ad65-557ceb34029c | -22.18771 | -42.48151 | 2026-08-09 03:34:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 452ed51f-2a25-3877-bac9-786f914f5de2 | -22.19291 | -42.47803 | 2026-08-09 03:34:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88d4d535-9d61-3711-ad0d-ce787b4c3538 | -15.75853 | -47.76702 | 2026-08-09 03:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4124a8bd-db83-3641-b4e0-21b334876a20 | -21.04633 | -45.6794 | 2026-08-09 03:34:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4be9a64e-39c1-3ac8-a958-3e60fdc8f3e9 | -20.38558 | -42.01103 | 2026-08-09 03:34:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4b843f4e-aba7-3c09-a6c9-508158bb3966 | -22.2317 | -43.0444 | 2026-08-09 03:34:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b5769227-b09c-337e-bf54-322e890e0607 | -21.27316 | -41.74535 | 2026-08-09 03:34:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| de1119a4-41e7-3382-8774-41633e1e105a | -19.94027 | -44.3731 | 2026-08-09 03:34:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README7.md)
