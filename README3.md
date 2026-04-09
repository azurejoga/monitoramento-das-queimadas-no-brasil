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
| 8003c0f7-cf33-3861-bfc4-f5c3f758a612 | -18.503 | -55.51313 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0ac72d33-a235-3ced-818c-6cc885864d3d | -19.59845 | -40.07479 | 2026-04-09 04:14:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fba2c458-7e57-3c4a-a0ce-669ef60fbd22 | -18.50021 | -55.52603 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ae708071-3232-3161-a173-77911504534e | -18.4947 | -55.49325 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7ab6b2b7-9eac-3ad5-9ddd-5711f43fd30b | -18.91323 | -53.21235 | 2026-04-09 04:14:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c062609f-98a2-39cc-b3f6-2c4457530ce4 | -18.91755 | -53.21661 | 2026-04-09 04:14:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5a093dc-15ca-3770-8731-90c379528143 | -19.589 | -40.07725 | 2026-04-09 04:14:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 27aa98a0-3e17-3662-9ba4-ba91bcc7be07 | -18.50332 | -55.50895 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 74c69836-f687-3f48-9c70-dfea20b53f82 | -18.49522 | -55.49308 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a9b78f6b-0268-3f97-8285-6b706b7e9ec6 | -19.59674 | -40.07842 | 2026-04-09 04:14:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1523aac3-2699-3856-bf22-af6318896a94 | -18.50619 | -55.52326 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b6ce5518-5865-37bd-96d7-913e8e7bf666 | -18.50043 | -55.52184 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6d05e5c-970b-3883-b7aa-1ccc599e8250 | -18.5069 | -55.52316 | 2026-04-09 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a33f61e4-3792-3388-928f-ab110551fb84 | -27.45449 | -48.45342 | 2026-04-09 04:17:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad8f3e1a-99cb-37c5-b0d1-5ddbc84ee7af | -12.83611 | -45.95345 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e885f1aa-1556-38bb-85a9-fb59c507411f | -12.0301 | -45.23795 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ccc9199-d6a0-3c23-a4d2-29cc1df60995 | -10.72527 | -56.04588 | 2026-04-09 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9714a95c-65b8-3b1d-a9c2-65b647fb7a2a | -9.45993 | -47.80366 | 2026-04-09 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a303d46f-01d4-35d2-b849-804f008b1e74 | -11.93653 | -58.07976 | 2026-04-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e0e4ff-d9e3-30ce-b2a6-d29d795c2fef | -10.66561 | -54.30472 | 2026-04-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2135785-c587-3a70-82ce-36f8fd98cdfa | -11.3455 | -55.28829 | 2026-04-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcc94873-20c3-3e62-a3f6-3736283da0d3 | -12.01878 | -45.23643 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b23410be-ac86-3b30-96fa-e2494c30f114 | -9.45272 | -47.82215 | 2026-04-09 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d809c026-90fa-3c8c-bb78-208c13b1aed1 | -10.66616 | -54.30119 | 2026-04-09 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b0eb81d-e945-36de-bccf-6578cc4bfd0f | -12.03057 | -45.23404 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 670f5680-e15d-30e0-8e6a-35a4c11a39bb | -10.7247 | -56.04944 | 2026-04-09 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1dd72e1-ccec-3a4f-88ed-8869b450ce22 | -12.2978 | -57.18475 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f06fcd-0354-343e-bf97-943757b978b4 | -12.01311 | -45.23568 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90c85f4f-ed91-37cc-9703-6dbea91a87bd | -12.30457 | -57.40168 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e1ea6d7-67eb-3e48-99d4-fe872e21c176 | -11.93786 | -58.07173 | 2026-04-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ff5eb8-ab83-3737-8294-9f6e24155da8 | -12.01925 | -45.23252 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e99ca131-827a-32f2-9d3f-20af19c94168 | -12.03104 | -45.23011 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abc415ea-9368-3f39-beb3-25aa7fafed0b | -12.01831 | -45.24035 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a196e66-3821-3457-bdbf-e066fc391be3 | -12.28471 | -57.39414 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3376c5c3-853c-3356-a36b-5fa506d539df | -10.72194 | -56.04534 | 2026-04-09 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 079aa315-f141-3bfe-b4cf-a175c73b2957 | -11.2028 | -56.87814 | 2026-04-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574b47ee-0a8b-34b6-8d7c-b90a73684094 | -14.12309 | -43.41922 | 2026-04-09 04:59:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e977950-5018-32bd-b7bb-cec4907eee1e | -11.60527 | -55.32281 | 2026-04-09 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef0fc1f7-d18a-313e-8bfe-41c33fcba393 | -12.84116 | -45.95779 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf51a3c-332d-3195-86e8-611a4b0eed75 | -12.06904 | -45.34151 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e23bf540-f8ef-3507-9182-7819946bf911 | -12.83569 | -45.95705 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 226629f5-e48a-3ba1-a46b-571c308303bf | -11.9372 | -58.07574 | 2026-04-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fd86692-fff1-31b3-9f19-c45180f51da1 | -12.28813 | -57.39472 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d83289a-3df3-3059-91b2-eca45d03431f | -11.3444 | -55.2953 | 2026-04-09 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d9d3b9e-4ab6-33e2-9c0b-47e16e028101 | -12.30115 | -57.40109 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4605cacb-4267-3f68-8907-e7907e3777fd | -12.02444 | -45.23719 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f32c7830-e3d0-364f-92dc-a5f79832f8ce | -12.30053 | -57.40486 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0649dce2-26e2-3ecf-92b0-d1dff791e0b4 | -11.60802 | -55.32685 | 2026-04-09 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54dc281b-5c6a-3ddc-8fcf-4e7e065b77aa | -9.45927 | -47.80849 | 2026-04-09 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad46e4f3-be63-3b58-86cc-238a57b09fca | -12.83993 | -45.95884 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad22b2d9-3f67-33e5-8567-d1494a1b90db | -12.02538 | -45.22936 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e891474a-018c-3895-8f08-7aa13e6c623b | -12.84157 | -45.9542 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66b45a61-1041-379a-beea-53b53de97f89 | -10.72137 | -56.04889 | 2026-04-09 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b5a17a-8b6b-3da7-9746-63229be081c7 | -12.30394 | -57.40544 | 2026-04-09 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fc73f67-7425-353c-8028-537dc911e696 | -11.93368 | -58.07513 | 2026-04-09 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cc598ed-aef3-36f3-a656-a77199fb6611 | -12.01265 | -45.23959 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7427a28-e652-359a-af62-ae48b42b3321 | -11.20619 | -56.87868 | 2026-04-09 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed28285-050a-3311-806e-09d8b04005bd | -11.60472 | -55.32632 | 2026-04-09 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d51f9aeb-ee94-353b-baa7-d4930ea43a3b | -12.02491 | -45.23328 | 2026-04-09 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc20933-68e5-3d3f-8b22-7edc286415d8 | -12.84037 | -45.95525 | 2026-04-09 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b54602a-6525-3458-bc9f-1a5791c27408 | -18.49804 | -55.50177 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 085b2a21-5c09-37cf-9023-7c3d0f771c19 | -18.50647 | -55.51473 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 65c7bc3a-1e0d-37f5-9372-30492f752faf | -18.50928 | -55.51905 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5590230d-3f2d-36c8-850e-fce27357114a | -18.50536 | -55.52225 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b21a67c4-7fdc-3a7e-8cfb-1cdeeaa2e3da | -13.04261 | -57.48615 | 2026-04-09 05:01:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7acc35-e942-382d-827c-18bf64cdd7f3 | -18.49579 | -55.49368 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 595846d6-fc78-3327-bc83-7e8b28abf83d | -14.92335 | -55.97913 | 2026-04-09 05:01:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6534e10e-e3dc-35e3-af5f-ef330eb9a480 | -18.50422 | -55.50664 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| da3e3712-f128-34c6-8e5e-5a55549ca3a4 | -18.50985 | -55.51529 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ffe76423-268d-349b-9692-ecd8e6f3d1b7 | -20.14094 | -56.3411 | 2026-04-09 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd7c0e2-009a-3c63-97ff-dbdb37948d7d | -21.7178 | -48.43405 | 2026-04-09 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a80d686-ff82-3636-a6c6-5e229feab014 | -18.50592 | -55.51849 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4e2131c4-845b-393d-a943-26b902bc02bf | -18.4986 | -55.498 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 7cbc1ee6-dd2c-3d52-a4ce-d3090091f2df | -18.49523 | -55.49745 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f3a85a57-1434-342c-86b0-55c46a5a7872 | -18.71942 | -57.54624 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cec55ce5-7eca-31ce-a48f-7fc7b487f0fe | -18.50199 | -55.5217 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ede8da7-c003-3063-a838-f46cb9143624 | -18.50141 | -55.50232 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a0391e9a-0344-34f4-9f12-182c13385072 | -18.49916 | -55.49423 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 671472e5-d46b-3b63-a0fb-48e246b2cb3c | -18.50367 | -55.51041 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 199a0d10-fe43-3d00-8a61-9874e43e0578 | -14.91993 | -55.9786 | 2026-04-09 05:01:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 654246d9-caac-35b1-87b6-0b41ac3d9f31 | -18.5048 | -55.52602 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 298f1a8f-9127-3b0e-acf6-afb3a02c0e9b | -21.71702 | -48.43302 | 2026-04-09 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07edba9b-8b70-3e1b-8c1c-a0dc96ece866 | -18.50311 | -55.51418 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5283e7d5-1b6e-3b5c-a906-0c47e9446fe3 | -14.92391 | -55.97557 | 2026-04-09 05:01:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e021929-a5ad-3287-a734-d14560f70d17 | -18.50085 | -55.50609 | 2026-04-09 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 620aba46-951e-3d74-b2fa-602da437bb03 | -29.71246 | -50.68368 | 2026-04-09 05:06:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| da052f99-0725-3e20-81f9-4b462991ffa2 | 3.08574 | -60.85497 | 2026-04-09 05:27:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3cce85f-db7d-32f8-85a0-a4a0852c863f | 1.32102 | -60.62503 | 2026-04-09 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f0b0b1-edf9-3e9c-bbd0-0c8ac410f250 | -10.72217 | -56.04493 | 2026-04-09 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbc1071-f56e-3f2c-8b48-c40050ae93c4 | -14.92019 | -55.97763 | 2026-04-09 05:31:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fcdc4d3-5692-3691-a5f0-f36a4e0f24ac | -11.2038 | -56.8789 | 2026-04-09 05:31:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a498ac4-768d-3a6a-b56c-0240d6210174 | -11.93814 | -58.07014 | 2026-04-09 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 572e03d7-cafb-35c9-87a4-50e87cd2ae73 | -11.60716 | -55.3255 | 2026-04-09 05:31:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 356cd447-abeb-3015-aaee-2d9406faf34c | -11.20505 | -56.88048 | 2026-04-09 05:31:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01cd644e-85ce-3d04-b406-5ec65aeda003 | -11.93375 | -58.07414 | 2026-04-09 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa7d42b-cd4f-32a1-8875-5a86d993d736 | -10.72163 | -56.04877 | 2026-04-09 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63277459-031f-342e-be6a-e873f668fd93 | -11.93309 | -58.0787 | 2026-04-09 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a5ada70-6269-387b-88d0-e8fe14ae58c2 | -11.60272 | -55.32486 | 2026-04-09 05:31:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ca971b-f3b1-36c1-8e80-1cc3b4d87087 | -11.93749 | -58.07469 | 2026-04-09 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f081b26b-ea1a-39f1-af2d-efcc39527d12 | -12.30392 | -57.40278 | 2026-04-09 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
