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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a491a63-5354-3a07-8976-a564306f1f5c | -15.24444 | -53.88514 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7390d048-a3f4-34de-8274-d969ae9c8058 | -14.13293 | -52.79388 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7dd0e13-d519-37a3-aba8-632b3451d1f8 | -16.06643 | -52.16809 | 2026-09-01 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fca4ca86-9a12-3b15-8f44-cad6c0c2decc | -14.45429 | -52.50652 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfa11a32-b4cb-3b01-8996-a73faf0b08c5 | -14.5135 | -52.2866 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aedcf8a-3fd2-362c-af8f-040d6a7a48fe | -15.25089 | -53.84614 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6f7ee26-2dca-3267-8462-7cbf7e455a90 | -16.14175 | -52.37974 | 2026-09-01 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c0b8339-4181-3a50-bc65-d06d012e826f | -15.18592 | -46.23247 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4aaa5230-2556-3167-b20b-4fd40f2f982c | -14.66341 | -53.55162 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a757b1b-a69f-3b81-9c28-c6e106d79b0c | -12.89533 | -45.8326 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fdd7940-cab7-3da1-9d1e-731196d9937f | -14.97159 | -48.15032 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae2e2adc-538b-3e07-b56f-c0198d971546 | -14.2649 | -52.89613 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65e49d55-9864-399b-8a27-e15e63865e39 | -18.30349 | -45.08094 | 2026-09-01 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a9612a5-6aaf-3e70-8d3f-51a4af053fb9 | -15.66626 | -45.95488 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e11895e8-d94e-3824-9cd9-526d105fcafd | -15.66404 | -45.90648 | 2026-09-01 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8338382a-b6f2-3106-87ad-3ab890de899f | -14.13174 | -52.80126 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf06e5cb-a4e7-31cd-bf60-2074bf7bcadb | -14.39364 | -52.52642 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de7ef7e0-1a39-3be8-84d1-a4bbfe3de69c | -14.40889 | -52.49545 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3848328-65e4-3154-a895-efdc5a72512d | -15.65118 | -50.09381 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1c86167-78b3-39b3-a957-c313e5bb836b | -15.45546 | -53.96961 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15c881eb-244a-31dc-9dbb-3134ac5babf0 | -14.71986 | -53.59212 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2be5fbe5-f3ed-3e44-be9a-8a0b6de1b1d8 | -17.13169 | -46.8553 | 2026-09-01 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d14a37d6-7dea-3618-b808-484d09568845 | -14.45705 | -52.5107 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 747cd7f9-3dd6-3659-ad16-c8e697d03fac | -13.38179 | -51.80848 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16a1fe20-070c-3997-9640-e5232c9d96a7 | -15.84925 | -47.68742 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb3d1fcb-451d-3edf-b9f3-011dd4e9eefe | -15.59474 | -46.46436 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38da8ef9-63a5-3eaa-8098-f11ee442842f | -16.67673 | -46.65676 | 2026-09-01 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f295e022-1785-3ea6-9635-cda74ba22bae | -14.41696 | -52.50392 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1865bf23-1e88-3928-bd5f-6f1322b247ea | -14.39422 | -52.52278 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49224c35-2756-32ec-8972-ff09faebcd2e | -15.04318 | -48.16987 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41db9de2-1219-3ef1-8e3e-82791225b0c6 | -12.787 | -46.46567 | 2026-09-01 04:42:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7b41dfd-ff4d-33be-bac2-7aa09172a6c8 | -15.01151 | -52.76907 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eedab1e-5884-3344-a5e5-ca1b116cdc2e | -19.39247 | -40.87049 | 2026-09-01 04:42:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6b29482e-3979-3623-ad93-cd5c54dc1daf | -15.7631 | -56.09296 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f4263971-6f47-32e4-8bf4-7594db4f2242 | -13.47896 | -57.05798 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 492924f9-34cf-3dc5-bc37-8f01c1fe1d73 | -15.76938 | -56.08688 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 43f1b7cf-a4c5-3721-ad2b-fdbb913dcbfa | -15.609 | -56.38557 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84398eb9-7986-3f63-9f10-70940bfb5e1d | -15.65943 | -48.70551 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fabddf8-b4be-3514-b46d-9466d7803bfd | -14.50489 | -52.23349 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d63f877-4f2c-3810-a8d1-158f5d57a723 | -17.88803 | -52.10881 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f89a149-6da6-3e1a-82bd-466f34b34482 | -13.32846 | -51.7809 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64b2e3dc-c6de-3a5c-a719-713b715cb1b4 | -17.87961 | -52.16298 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39ca3946-6be9-322c-bc31-f3d7428c27e2 | -15.77161 | -56.08954 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| d5672bd1-6eec-3017-b54a-e38a3ad09ae3 | -15.23538 | -53.87549 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b309d08-3f1e-3235-bb1e-99903bbb9e09 | -14.65871 | -53.55877 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2610fb6b-be38-32dd-9fa3-5d2f6339477e | -14.41108 | -52.50324 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2b3a385-ea64-3a70-8e27-6e502048e2c7 | -15.50625 | -56.00711 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9774c2ae-2975-3a64-88b2-a7db78ebe0d9 | -14.13511 | -52.80182 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcf084d3-a50b-3849-bdcf-1b36714541fa | -18.50646 | -48.4471 | 2026-09-01 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3342d90b-e8e1-3c87-974a-d6d7ec56e3ad | -16.08988 | -48.04731 | 2026-09-01 04:42:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6a42cc0-a7d3-3cc5-b924-34d5a71b11dd | -14.00898 | -54.08635 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac4b3f31-76ea-3922-9818-13ef90d8e2d4 | -17.38967 | -42.35815 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7c96bff6-8af3-3c85-9f5f-a2e1e73629d8 | -14.37909 | -52.5315 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd497fbf-e013-385c-bbe0-d4c72dc57cdf | -18.15892 | -49.59505 | 2026-09-01 04:42:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 2fe098ad-d57c-36b5-af4f-6a1347629242 | -16.30579 | -42.03576 | 2026-09-01 04:42:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a3d46860-6c9c-3db5-9342-114117897fa3 | -15.7639 | -56.09576 | 2026-09-01 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 106abf99-2633-316b-860d-09a42709b117 | -15.25889 | -53.88371 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b64eac7-d94a-3f70-92d2-ddce5dcda791 | -16.70194 | -49.90311 | 2026-09-01 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0bed1b4d-2fb6-39cb-9798-1b50fcf7ecf0 | -14.25842 | -52.87221 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e53a275d-7180-3802-9c1b-516ee8022ecb | -14.2636 | -52.86167 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a384f05e-8bc3-3083-ad89-f48dec0afbea | -15.61695 | -56.38382 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5fac6c6d-b3a2-3771-8a65-3c11b4f85d60 | -14.46866 | -52.52386 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03e60ba3-756c-3736-ba1b-f26b9a096eaa | -15.99537 | -55.95021 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dff13eb9-3193-3f69-9402-23cb10a35b36 | -11.68869 | -54.54577 | 2026-09-01 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34aa1d75-84a0-317a-9581-e2375d983264 | -15.60716 | -56.39573 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec5c9e73-7b08-3dd2-8440-ccb3b4ab7f15 | -15.60808 | -56.39065 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b026cc6c-7b31-3a2e-86e5-967fc54efbe2 | -14.40715 | -52.50632 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15b55c77-d02c-38c7-8190-02c7a5dbe2d4 | -14.13688 | -52.79078 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7bd5072-1a71-3ecb-a6d5-acc6393ceaa3 | -10.41701 | -64.45399 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1031059-7036-3410-bba0-87ca8adebf7c | -14.1357 | -52.79813 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8edd8f49-8a74-3941-b876-9230f45d6a2a | -15.43344 | -52.68274 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e4b75787-661f-3de7-801b-90276585bb27 | -16.59591 | -50.24278 | 2026-09-01 04:42:00 | NOAA-21 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0906f03d-e185-387a-a8e9-c7fccdf5f92d | -14.27286 | -52.88987 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee514ab5-1d67-300f-871e-c832411e52d7 | -15.83546 | -47.67576 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26d234cd-39dc-3e08-9f77-ea4aa2b9e785 | -14.40773 | -52.5027 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f64a4aa-85ad-3406-9ce9-598c35671a23 | -14.46951 | -52.13583 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560c28eb-723f-3148-8b75-7e0c0d6a0a41 | -14.39989 | -52.50884 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9cda497d-fefb-3279-9e93-a823e45df99a | -16.14232 | -52.37615 | 2026-09-01 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e199ea49-6f83-3575-9948-13210cf16e99 | -14.40844 | -52.47677 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0af801fd-90ca-3f83-818f-f2d9015df32c | -15.64106 | -56.38617 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb4ca182-9661-3526-9dc4-3f1f0e08f446 | -17.89078 | -52.11299 | 2026-09-01 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bcf5e58-7ebb-3bc1-8e01-e346216c08c0 | -15.19562 | -46.22218 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c522b86d-9069-33bb-9b88-58da01463b70 | -17.18771 | -48.71782 | 2026-09-01 04:42:00 | NOAA-21 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 22516fe6-2ec8-34bd-bfbf-cb17cec4f392 | -12.69135 | -47.45453 | 2026-09-01 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5270f86-26bb-3aa0-8fab-b970bbfcafa2 | -14.38521 | -52.53623 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d4c1d4c-e345-37f1-89bf-5f5f0feeb680 | -14.45763 | -52.50709 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d21854d1-59f9-3f3f-8416-53ae670dfb13 | -16.47629 | -43.42389 | 2026-09-01 04:42:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ff9848-623c-3b83-b77b-8275b10d8cfb | -15.03771 | -48.18214 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b5fd69a-094a-3384-bbb6-cad4fa7135de | -15.03409 | -48.18152 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b3ba2a-ed6b-3d01-a8a3-0d89012f587c | -15.84172 | -47.68625 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae9bff66-a1c4-3846-8afb-b0423635cba8 | -17.14263 | -46.83429 | 2026-09-01 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47c2929a-0b7d-3daa-ad19-c3c18e8793cf | -14.42363 | -52.50508 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5157931-63d6-3688-8048-532241f9ca1f | -14.40787 | -52.48039 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa1e83e4-8ec3-3901-813d-21e55f270410 | -14.46199 | -52.52269 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60cf6cf1-76ea-3a2b-8548-447421e85b70 | -14.5803 | -54.07832 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e69bf2d-7e17-3ad0-a5ef-2cb3fd8f71ee | -15.39273 | -53.75436 | 2026-09-01 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b0d5a7-b8d3-3a6b-a494-d2fbd521bea1 | -14.73208 | -53.58228 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38645d18-1f33-39bc-910e-a21526db8470 | -14.47259 | -52.52081 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ff99daf-8bb5-3354-a8d8-65b627850e77 | -15.25199 | -53.88247 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df566d8b-23c2-3691-b251-d825c9f84c01 | -16.61445 | -43.37394 | 2026-09-01 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README48.md)
