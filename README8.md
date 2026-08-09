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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b1a43b8-50d4-3002-9c78-b0f20fc2a68b | -9.47069 | -40.32308 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 53967fba-4f3d-33ae-9d7f-9bc03ad68330 | -6.96209 | -41.50745 | 2026-08-09 04:06:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d31ab383-0a0d-324d-85d9-875f118a3947 | -6.90872 | -41.92894 | 2026-08-09 04:06:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e81899dd-6f45-3ff3-a4b4-994404977349 | -4.45641 | -47.91683 | 2026-08-09 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93219921-dfb7-3280-bd87-0bc84b069d1a | -4.28009 | -48.56185 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9269f2c1-eecd-3394-a603-db4d3b9ce178 | -7.58535 | -45.21219 | 2026-08-09 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a78f19d9-2104-3b7b-b3dc-366b01ebff55 | -9.6741 | -37.86344 | 2026-08-09 04:06:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd5311f7-2f78-32b3-b6ae-7cdfb0f890d9 | -6.86081 | -39.88085 | 2026-08-09 04:06:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 262cb0cf-3f1e-382c-b684-3cf4c6657afe | -2.96086 | -49.26069 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d6e9da0-3cb4-3a7e-b9cd-a61ccd063638 | -8.33378 | -46.3804 | 2026-08-09 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4df3c1a-b99b-3cb7-9fc9-b439c3abab58 | -4.26792 | -48.18609 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa1f4622-2a06-3c36-9e47-51df8d12364e | -9.46456 | -40.31841 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 211.1 |
| 13277405-db29-3720-b3d7-79505f2e6b42 | -8.04669 | -37.55827 | 2026-08-09 04:06:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f21b66a0-1395-371d-ac3b-2accffaf585c | -4.27347 | -48.56517 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d848dd2d-c889-3710-9eb3-e820523c525d | -6.93188 | -42.4352 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62e5561f-0ddd-309a-859a-c3e238872531 | -4.74217 | -40.43301 | 2026-08-09 04:06:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1bc43b8-9110-3e97-ab8b-6c13717bbb34 | -6.77698 | -46.47203 | 2026-08-09 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71a14428-c066-319e-a921-9044799ceec5 | -9.46675 | -40.32611 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7959c3f2-c8c6-3d04-a48d-997f107520a6 | -7.6296 | -42.74797 | 2026-08-09 04:06:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ecc6a8e-fbd5-34b1-befa-fe7c06c02bd6 | -4.10556 | -49.26988 | 2026-08-09 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff03e47c-d263-33e8-9669-4ca05cef7617 | -7.8976 | -37.75448 | 2026-08-09 04:06:00 | NPP-375D | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 940eb83a-5699-3251-ad69-990933372c4c | -9.47405 | -40.32363 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 035cb30f-b4b6-3a73-8906-28820681d9a0 | -6.87964 | -44.92195 | 2026-08-09 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5cc63c55-1fee-3448-9c10-acd707504d05 | -7.58456 | -45.21674 | 2026-08-09 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6911e65f-de73-3ef4-b8f1-53e0f044edb0 | -8.32904 | -46.37962 | 2026-08-09 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a821d4e3-a906-3efe-9814-c6efa5997812 | -15.40752 | -41.80199 | 2026-08-09 04:08:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bcb8a10a-78b5-365d-9323-0c197dc185d9 | -15.65324 | -43.29112 | 2026-08-09 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 78b15607-cdda-3864-80be-49599ab46934 | -10.45467 | -37.14336 | 2026-08-09 04:08:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b173c21a-09a2-3c30-9ab7-5e087d5d8632 | -15.16629 | -41.95014 | 2026-08-09 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b131f936-9161-388f-9982-a074dd0f81b8 | -14.08112 | -53.98878 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c1acdda-c968-38f8-b70c-3764ec03cfc9 | -11.62266 | -51.09798 | 2026-08-09 04:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 841aa0f6-9ed3-38ee-a93e-46eb8ef1ee13 | -14.0671 | -53.82473 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90b45a67-993e-3d4b-8605-ba64fb07c1bd | -14.90889 | -48.23558 | 2026-08-09 04:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 367220aa-67b6-3c35-bd0f-9a3ca71b3692 | -15.87259 | -43.61162 | 2026-08-09 04:08:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed8e1821-fd96-3add-9d0f-691d89f421e7 | -12.33289 | -53.15053 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 127fe5a1-9ae0-33f0-8414-1d67244988fd | -11.04568 | -44.27523 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 615b615f-6a42-3e57-8d18-06654297a5a7 | -12.34637 | -53.15359 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 720faaa6-8c70-3018-b0e2-a6cbdda7ef90 | -14.03418 | -53.84351 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af52cd70-d184-332f-9481-4258c67a9f06 | -14.03275 | -53.8517 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6d4d183-0caa-3349-a852-4c0e4ced91c3 | -14.06279 | -41.01585 | 2026-08-09 04:08:00 | NPP-375D | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d230c6b9-72af-3734-86e6-09a6af385747 | -14.02203 | -53.83384 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68bffff6-db2d-3ed0-a891-a8f40deab1e5 | -14.03415 | -53.8452 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e3a249a-ed75-3cf1-a448-d135b2e3624d | -14.90988 | -48.23046 | 2026-08-09 04:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb1ef44e-3f95-38d5-8561-794a28b3bd3d | -12.32485 | -53.15519 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13c42b4a-7ff5-396f-b1e9-6d86be3c11aa | -14.06732 | -53.82294 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04478045-827e-3be4-a25a-ac43fd139711 | -14.02054 | -53.8405 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d5ce1d6-8da2-31e0-8a36-e9096428248f | -14.15966 | -54.02225 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4dabf85d-3196-351c-8ffe-b02f50668d38 | -14.06566 | -53.83148 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e88a1805-d4df-3681-a3dd-2009673adeb3 | -14.86935 | -43.89912 | 2026-08-09 04:08:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b10082a-d942-38c0-a11f-b0cd6d46c24e | -11.62327 | -51.09669 | 2026-08-09 04:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99b4f027-c092-323f-82f8-272d66feae7a | -15.76242 | -47.76964 | 2026-08-09 04:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f529fda-09aa-3439-afee-4c62286e152b | -9.66349 | -43.84969 | 2026-08-09 04:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b454ec7e-6291-3030-ba40-7323e50c8938 | -14.15433 | -54.01372 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ca91406-268e-386f-a0c5-159dc848142b | -14.08539 | -53.99952 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c449296d-459f-31ae-83ef-3e2513801096 | -12.35051 | -53.16761 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc2e2306-1ff4-3683-82cd-f7e7bd1434b3 | -15.40812 | -41.79834 | 2026-08-09 04:08:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 70a48350-4878-33b4-8903-673d47e48843 | -12.59295 | -46.9943 | 2026-08-09 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 251b98ea-2da8-321a-b15a-0b188a3ee0c8 | -15.76144 | -47.75021 | 2026-08-09 04:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f044d655-b6f6-320c-ac8a-c78587fd2cbb | -12.35181 | -53.16137 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bda90d4-e466-3407-a017-8711335d98ad | -12.95665 | -41.81783 | 2026-08-09 04:08:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7c4bdba-c0df-38c4-860a-07cb5501330f | -14.31857 | -54.92934 | 2026-08-09 04:08:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ec5d8ab-33d2-3684-a941-c74761e7976d | -12.96006 | -41.81841 | 2026-08-09 04:08:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e5dad53c-e4ac-3147-beb2-4d9d02e99630 | -11.26952 | -44.8656 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cd77cad0-610e-3367-898d-8e1f92ff6c78 | -11.27293 | -44.86998 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 701a4c9b-7670-3d83-ae50-5dd18f751298 | -14.02339 | -53.82885 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 685c42fa-033b-3df8-997a-6ed3187de304 | -11.04175 | -44.27451 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6920de4-968c-37fa-b736-0d94f98afa52 | -11.78246 | -41.19992 | 2026-08-09 04:08:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16f08373-9448-31e2-9ffa-789026590912 | -12.34767 | -53.15488 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c39fd63d-96bf-317d-bdea-110c0f4ef142 | -15.87696 | -43.33257 | 2026-08-09 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e5c59a9-2da0-3ed8-8810-bb75685bb38a | -14.04237 | -53.84018 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29d93e30-a26c-3d97-bb09-59f24f11cd55 | -14.02196 | -53.83546 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1ea5c29-978b-33dc-8fe1-fe526d4c8854 | -14.08667 | -53.99634 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 077c76e2-cdf4-3b08-8656-e0d34dcf0e20 | -14.10409 | -39.72834 | 2026-08-09 04:08:00 | NPP-375D | IPIAÚ | BAHIA | Brasil | 2913903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13ccbd10-df2b-3b4a-b5dc-52c5b331660e | -11.78307 | -41.19624 | 2026-08-09 04:08:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90a2e2e0-ad20-39fe-910d-46ddf1a5159f | -14.03273 | -53.85001 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7417b2c4-4272-35f3-9c44-1f31db7ed8e7 | -14.04928 | -53.8399 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 706c2add-4a11-394e-9df0-0a2292b861a9 | -10.25274 | -45.82032 | 2026-08-09 04:08:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10bb3265-70a7-3911-970f-e582cd63b45b | -15.87344 | -43.33192 | 2026-08-09 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aed59201-b6b9-335f-9eaf-729e9a7719fc | -14.07266 | -53.83113 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e33260b9-b508-35cc-9a84-7f846f745505 | -13.52868 | -44.03678 | 2026-08-09 04:08:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 456b58b5-239a-31cf-aaaf-35ce217b6795 | -14.32022 | -54.92212 | 2026-08-09 04:08:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7098aac-c688-3097-a450-d0de2a6fbc7d | -15.83605 | -42.23443 | 2026-08-09 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 81e9cfb6-476d-3110-8b24-c1a7e4d2f663 | -13.53243 | -44.03745 | 2026-08-09 04:08:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 537ea0e6-60a5-3999-ae1a-12752f7b2e3d | -16.7732 | -41.48564 | 2026-08-09 04:08:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 774d38f7-03b0-3c93-98ae-25aac756b7cd | -10.45815 | -37.14391 | 2026-08-09 04:08:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29cf1fc2-c225-31e5-a19c-d352f35d212d | -14.08692 | -53.99273 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e4033ef-3b15-3a0e-9d55-8670004db511 | -10.71313 | -49.3441 | 2026-08-09 04:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8d71114-05f8-33b3-8a54-95374c46aa95 | -11.27359 | -44.86635 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b0f5002e-8fec-3b93-be1b-fc92a6c61128 | -11.6236 | -51.09333 | 2026-08-09 04:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48889066-3a61-3100-a8ce-895bce4e81a8 | -15.87414 | -43.32789 | 2026-08-09 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e5a519-8110-3801-aff2-f524b74d437e | -14.04245 | -53.83845 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dadaf3a-bc86-3dad-b386-49854fa279e0 | -14.17343 | -53.99236 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a295c0d8-48be-3d0b-b375-87cae838c705 | -11.04311 | -44.27292 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a6d5a07-ff5f-3844-8c97-057bbdfbaedd | -15.87765 | -43.32853 | 2026-08-09 04:08:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02b06b36-b158-3056-940c-42767f792716 | -12.32615 | -53.14899 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c002ae4-d8f6-31a7-b70f-bc345762c262 | -10.25357 | -45.81571 | 2026-08-09 04:08:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a613f9a-9b17-316a-aa34-617d29f417cc | -14.91262 | -48.24185 | 2026-08-09 04:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39a5029e-4782-3a4a-91f3-d79b2bb24d3a | -10.23005 | -45.80165 | 2026-08-09 04:08:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98219147-5fc0-3c84-b26b-fa07fa7128f4 | -10.25724 | -45.82063 | 2026-08-09 04:08:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28951ae3-9b7e-3632-8910-8b1f2b5a55ac | -15.8363 | -42.23363 | 2026-08-09 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README9.md)
