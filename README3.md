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
| 8ee83e39-b6d8-3519-89d7-121c7a8f754c | -23.35815 | -45.49124 | 2026-04-25 04:14:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c4242240-ccf2-3703-a164-442c755fb7d3 | -23.07892 | -48.61181 | 2026-04-25 04:14:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3df8152-4278-3a1a-9e40-4fe302094682 | -19.70101 | -43.95596 | 2026-04-25 04:14:00 | NOAA-20 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bcda5dc-89f5-39ac-afab-5ce7d8bf5d24 | -18.50968 | -55.50069 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6f6fad53-cb84-360a-abb4-a9340d1f7ee7 | -20.19745 | -46.79398 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 437aa5ca-0c32-3368-8727-12f5d1b08177 | -20.17814 | -46.92912 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2ac1883f-a0c9-389b-9208-5240f86555dc | -20.15603 | -46.85059 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be6d233b-359b-3a53-89eb-cdb20e7cdfa6 | -23.37727 | -53.6181 | 2026-04-25 04:14:00 | NOAA-20 | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f85a0602-ecb7-362f-822a-bcc11000fa10 | -20.25368 | -46.77115 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99daa08c-e524-3cc8-aed7-40bafb6e0c5c | -18.3501 | -50.38049 | 2026-04-25 04:14:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b95820f-990a-3734-9116-245715f0a5b1 | -20.25091 | -46.76672 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf531e25-7537-3ce3-bc80-e6dd656eede4 | -20.18281 | -46.88054 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d281ccb9-9657-358b-a609-8ce7744d047a | -25.04778 | -49.33721 | 2026-04-25 04:14:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b550fb17-6a20-3417-aa43-fdb86c05eb38 | -25.2324 | -50.73326 | 2026-04-25 04:17:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae393588-71b8-3d42-b0cf-82a6066a4691 | -25.46431 | -51.50972 | 2026-04-25 04:17:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 47c87a45-b138-3825-8fbf-dd6ef7562b93 | -25.2334 | -50.72804 | 2026-04-25 04:17:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbc9b522-8104-3729-9afa-dd7501743c7a | -13.372 | -45.3087 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d40132e-698e-3987-ad55-8c8a917e6ffe | -12.39983 | -49.94933 | 2026-04-25 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ff1d2ad-7b7e-3f97-a855-c108cd49e190 | -13.37867 | -45.30133 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e45e1bbc-7a9a-3d70-a94b-9baf9728fc5c | -13.37294 | -45.30063 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb3bbf0e-b7fc-354e-97ba-c1f1703c8642 | -13.3782 | -45.30538 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8830ed51-c3c7-3fa1-804b-7e8c38a5d7cb | -12.88959 | -56.66386 | 2026-04-25 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e90185d8-1c30-3990-9c5f-0725c0440aa3 | -13.38033 | -45.30072 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca7f1a0f-20c5-33f8-bb12-801805174eb8 | -13.37342 | -45.29659 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d91ec3be-82f2-35f0-b219-ef7ec40576df | -13.18625 | -52.7054 | 2026-04-25 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f341af81-89f8-30d5-8a5d-94617f25150d | -11.99505 | -47.76952 | 2026-04-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2533e6a2-9e3e-3f76-9493-878ad114500f | -11.84608 | -55.01659 | 2026-04-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 023eb054-01b5-3440-adc3-6743b31d00ff | -12.35278 | -54.77168 | 2026-04-25 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b88c6bc4-b3ba-3fb9-b5c4-4353e28abaf0 | -12.35 | -54.7676 | 2026-04-25 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd89b440-1463-3eaa-9d82-e2eb3d585c27 | -11.84222 | -55.01957 | 2026-04-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29d2a69-99d9-3dcb-bd15-4f0fd5635579 | -13.37989 | -45.30478 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eba1d378-1e80-34ba-9be4-4c57c90ab4e7 | -10.72244 | -56.23374 | 2026-04-25 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67408060-718a-3fd9-b64a-bd4b4d9ef024 | -13.37247 | -45.30467 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30d8dd98-6382-3f7d-8900-b344d7ea7e43 | -10.95266 | -48.83863 | 2026-04-25 04:59:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d562d9a-f141-3193-9070-17e423a15b99 | -11.99437 | -47.77477 | 2026-04-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b1acd60-62b8-3c8b-b76f-d50d8c04c427 | -11.77907 | -43.66274 | 2026-04-25 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bf3e8c6-3437-3290-80a2-2977ef3ddb99 | -12.35882 | -54.64535 | 2026-04-25 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d13ac566-a3d1-3eda-86f5-4c7f46a26340 | -13.37915 | -45.29729 | 2026-04-25 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93cb02fe-f9ca-33b8-adec-c4781060b8e6 | -20.18253 | -46.92475 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c16999cf-581a-3807-b1a0-1e47c4fa9dac | -13.99173 | -56.6437 | 2026-04-25 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 145051cf-2379-3c9d-bab6-fa1fd99bb5cc | -20.19259 | -46.87941 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 896c3d38-235c-392d-bbe9-c645d1491c83 | -18.50422 | -55.50252 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8401a729-bc57-3e29-b51f-96f9e1977281 | -20.17988 | -46.89336 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c520b01a-4ab9-3202-8bbc-56a6b70fd3de | -14.3154 | -57.73408 | 2026-04-25 05:01:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f43e56a3-12d6-3a0f-b100-e82821286313 | -18.41586 | -54.5531 | 2026-04-25 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a5b36e9-a15a-33c8-9b0a-c1910e42c804 | -13.71742 | -57.47952 | 2026-04-25 05:01:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6abc48fc-703d-3b8a-9def-9339d4234efc | -19.77629 | -50.72894 | 2026-04-25 05:01:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e4235f27-4e7e-30c8-86b8-352a9e4f3c25 | -18.51152 | -55.49986 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a07ca45d-e9f8-3459-b040-db64b5d8852d | -20.1853 | -46.95457 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75d016d0-0e0f-3216-befc-b1f107caddeb | -20.25459 | -46.77104 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5930bbd-c4b4-3653-9a45-bff193f0197c | -16.42234 | -54.92271 | 2026-04-25 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa777814-d61c-3d37-9d33-71d132dda0ae | -20.25181 | -46.76774 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a240ba9d-426e-3e7f-bb6b-b5e596e8a9fd | -20.68002 | -48.96215 | 2026-04-25 05:01:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 936a168a-3dd1-3264-9bb1-e87dca558e14 | -13.71681 | -57.48324 | 2026-04-25 05:01:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6711a62c-043d-35c3-9e9b-c82173025c2a | -20.2004 | -46.79853 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cfdc5d6-b923-3b13-a2b8-f9defabcfd64 | -18.07258 | -53.89552 | 2026-04-25 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22985243-dde3-3ba8-9a05-b40a8c911590 | -15.97904 | -56.37753 | 2026-04-25 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| da73f577-8895-36d1-8ec4-2ba18e813848 | -20.17956 | -46.8967 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fd85ab9-77aa-34b9-a559-8a16670606b9 | -15.96842 | -51.36947 | 2026-04-25 05:01:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f45e8ed-a4a3-3418-8cda-f9956b2543e1 | -20.19302 | -46.87495 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fabab595-cd01-3a71-976d-e87fdca227bf | -18.51096 | -55.50362 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1db25b24-63a3-358c-92d1-974135f95c1c | -13.65616 | -60.63034 | 2026-04-25 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a464e963-2278-370c-b6d5-4ccb46aec8a2 | -20.17643 | -46.92923 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c4e13cd-9e38-381d-a69e-e4d45ad50419 | -13.7202 | -57.48382 | 2026-04-25 05:01:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca4eb28d-db19-3754-adc6-7659a72a99f8 | -13.99448 | -56.64784 | 2026-04-25 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ca8cb1c-6e53-3427-8fa9-5ad620ec3ecc | -20.18173 | -46.933 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bebbb50-5c4e-3f24-a4aa-1eab95786c38 | -20.19872 | -46.87479 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8dd075a-2b1d-32be-ac41-b3ee92629187 | -18.50815 | -55.49931 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 65d58e96-2386-37f0-910f-6db22ebd405a | -20.2494 | -46.76551 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4e622e5-0787-3a57-9a50-25bbd0264749 | -15.86416 | -43.60154 | 2026-04-25 05:01:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e4d62d0-a1be-38cf-92a9-f8a4ddaa6e47 | -18.3509 | -50.3782 | 2026-04-25 05:01:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 94a4dbc1-593c-3d46-94a6-14fa9f182131 | -18.50759 | -55.50307 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d6f70005-28f9-3610-b002-7913bb6b4070 | -20.795 | -55.37244 | 2026-04-25 05:01:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0c45bb8-c665-3b48-a9fb-ba5c41507be5 | -20.17605 | -46.93322 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47f94a20-dacf-3099-ace1-23173acef0b4 | -20.25229 | -46.76243 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb0c7321-2798-3047-9d9d-d27d4bd60e37 | -18.2302 | -54.59819 | 2026-04-25 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc9b5bee-fe9c-3335-98d5-8dd6239068ed | -20.24368 | -46.76541 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c29d387-304c-3cc6-ac0f-d59c6111edc0 | -20.52108 | -54.60791 | 2026-04-25 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3a3968b-e062-3099-97bc-d28163e38cc5 | -18.50367 | -55.50628 | 2026-04-25 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4f7ae3be-5d2b-3659-819c-06cdec1b0f5a | -20.18212 | -46.92901 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3590521e-a4ec-3732-b9d6-ca95b58fff5c | -16.42289 | -54.91901 | 2026-04-25 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b855656-4c0f-3b04-b5ce-4b1c75918249 | -20.25513 | -46.76555 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a1d1c68-8ab5-37d7-a421-b4af1b476e38 | -15.9796 | -56.37395 | 2026-04-25 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6289f720-95ca-34cf-9c1c-1ce6f8c606ef | -18.13304 | -54.23228 | 2026-04-25 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c03cfb84-2fe6-3cab-ac7f-bd3f2950dd42 | -18.48318 | -51.68165 | 2026-04-25 05:01:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f081d780-3041-3279-bb39-81ed92094a35 | -14.20267 | -57.4307 | 2026-04-25 05:01:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b3466eb-ae42-37b1-a05b-1bd4fbed62f9 | -15.96711 | -51.37032 | 2026-04-25 05:01:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 985e0343-3626-3d86-8c01-23c0fdf6288e | -20.15567 | -46.84904 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf6ee340-25fd-3946-89df-17bb3510fd91 | -20.16107 | -46.852 | 2026-04-25 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d84f7775-4577-3190-9c20-aabf69e0e2b4 | -20.1857 | -46.95047 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49a9198c-ee9d-36ad-b6ad-54eff1e6af95 | -13.99505 | -56.64425 | 2026-04-25 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d23d415a-e3ef-3aac-b372-c0f88ccd3903 | -13.65755 | -60.62859 | 2026-04-25 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcd8a78a-5f2c-3585-9911-8819fad59b57 | -20.71882 | -55.17317 | 2026-04-25 05:01:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2d97fc-8784-3bd9-a525-cd27eba99334 | -20.17722 | -46.92103 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ccd58ed6-e426-335b-b4fe-e9b90eefce64 | -13.99116 | -56.64729 | 2026-04-25 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aa9c694-9f8f-3ead-9265-317159c9e49b | -20.17682 | -46.9252 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46ee0dd2-58a9-3686-95a0-09b3de6ac3d2 | -18.2283 | -54.59493 | 2026-04-25 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c90fe3-1b12-3ada-a176-7d53f657e88c | -20.18698 | -46.87864 | 2026-04-25 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 063d250f-21f7-38f5-8aa9-4dc6c9300b10 | -14.21204 | -57.4243 | 2026-04-25 05:01:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2758d699-8c4d-33f4-ac16-a744659fcbed | -13.6571 | -60.62516 | 2026-04-25 05:01:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
