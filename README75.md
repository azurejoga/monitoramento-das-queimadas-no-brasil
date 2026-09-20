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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 387331c4-7d14-3b5e-8135-7a16283ead1e | -11.87272 | -49.00447 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a63065e-cf86-3d09-be8c-950d41fe424d | -8.18026 | -54.76144 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9f051fa-c07f-3ca8-a73d-eb5587401da1 | -11.37649 | -51.38752 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad95583c-2dbd-36f5-928c-809ad6a16241 | -6.67262 | -50.89684 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 895b2729-f618-3fcc-bcbc-874b5b7ad835 | -11.86341 | -47.66538 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7988048-5bc2-3c3d-bfa0-fbb174f8cceb | -11.85367 | -46.87465 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd5fe7ae-d91e-3719-becb-10712479cb76 | -10.27397 | -50.2529 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 710b5e2d-5d04-39fc-9c86-3357326c83e2 | -8.70311 | -49.53827 | 2026-09-20 04:40:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a994a75-e53b-3b92-b5ab-de4465006b94 | -6.66331 | -47.73265 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b176db1c-47ee-3f10-9d33-103c9accd5b8 | -7.12015 | -44.82666 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4e2379f-5174-3ff0-9aaa-a55d9ef0905b | -10.39513 | -48.89907 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48592342-4eb0-38bc-9e96-6a02e1b631cb | -7.28225 | -45.55747 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b67e1916-4dd7-3a40-ba68-a12d893d403a | -11.02904 | -48.34535 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39473d94-64d9-39e8-8905-edfe4b90d1a5 | -11.22596 | -54.08496 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9097a3e3-a3d8-3f5a-b42e-8b593f671655 | -11.44845 | -45.31891 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d50bb22-0ff2-35c5-ba02-97775d298778 | -7.60107 | -55.70945 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6832027f-9167-38cc-8b61-342f9a0c90ae | -8.30054 | -46.85933 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61dc13cb-1ef1-3f32-bded-317886b964ee | -13.00978 | -46.96979 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a7bf079-059a-36ca-9a74-1cd408581d84 | -11.13402 | -54.01273 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b95de7cf-0467-3e69-aa22-2f72ceea3195 | -13.2641 | -51.72833 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60ed8b77-78bb-32af-8e28-91fb7b48b60f | -12.5846 | -49.11997 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2a1b239-0cfd-3429-be96-2e2426f0b749 | -8.47364 | -44.50266 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eb4c784-4bdc-38f5-9845-f1a09b9feddf | -9.0285 | -48.77865 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70dd9b7-dd4a-3e08-a3c0-7bc66944e212 | -10.55007 | -46.75089 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b605aaf-94e0-3945-8aeb-76a3a0bbfa06 | -7.54974 | -45.44012 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fbee8b6-9e70-3e10-8359-2186654cc402 | -13.72838 | -48.79292 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4bc069-c8b6-3490-9604-d1ccee701402 | -10.27441 | -50.27155 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d8a60fc6-b55b-3fac-8d5d-fd434a69808a | -11.8467 | -46.87352 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcaae3b0-ae22-3a2f-8e2f-76be62ba22b1 | -9.82141 | -46.43063 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f42b9b3-9d78-3b58-a667-86db9dcc820f | -12.28929 | -47.12164 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5302f46f-d57b-3505-9362-c31e286bf943 | -11.03177 | -48.34562 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38b8d70f-2b18-3174-9ac1-7b054c6f16f0 | -10.30081 | -45.4329 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4d8b495-4d36-3429-a39f-efb802dbc9f7 | -9.54417 | -45.40079 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f7f6101-5ce5-3566-abe1-173c899be794 | -9.01134 | -44.99273 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1444a70d-a3d6-32c5-b41c-62ded9b0a3c6 | -8.9237 | -50.9178 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb805f5d-e4a1-3abd-adc3-bdab5143fd8d | -6.19919 | -57.78028 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 617388c8-0289-393b-a392-56bc62ccbf1f | -7.01556 | -45.24384 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5231fd1-772a-3bbc-a097-de79abf8ab5f | -8.18099 | -54.75719 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c49c4f7a-3780-3271-99bb-308159d8a5ab | -7.55765 | -45.41232 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34674a85-df41-3941-bcc2-af57e00baabc | -9.66721 | -54.32312 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e08e642-a8b0-38b1-a187-58883d4f9bdf | -6.97626 | -49.77882 | 2026-09-20 04:40:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d28b431-2b8c-35c4-993b-2f04fb19779b | -7.68701 | -44.66451 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e44e7cc-e82e-30cf-9801-bcf80afba808 | -8.73692 | -52.35933 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c9e40c2-88d3-3d6c-9e49-c5135e671776 | -7.57024 | -45.40166 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6496e36-d2dd-3134-9490-7bbd6c27d9bf | -7.79771 | -44.9417 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28913081-04a9-365b-b17e-51ef62f67a81 | -9.24089 | -46.22697 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0bd738a-417f-3f16-b292-b20523ad7585 | -8.05317 | -46.28482 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42dc4704-eb0e-315f-b10d-d0bd52e509ef | -7.86419 | -44.84957 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c734bcdf-246c-3531-9953-49db56cfdb03 | -8.99456 | -45.00372 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9057710f-5b1b-3b2b-b5ba-cf75c850dd04 | -7.35049 | -44.61459 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0aaf446-3c79-3760-891d-f609afd4d972 | -7.08975 | -44.73092 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dd66999-12d2-3541-a2fe-dc7a5bf5dd02 | -7.17988 | -47.90344 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 149d0f1f-3c52-3ee7-aa99-48260b46aa1e | -10.89249 | -53.98655 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa093931-5653-375e-8152-c3fc4dd2800f | -12.41475 | -47.46952 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce9342b6-b642-38a1-8549-cd9342c39dc2 | -7.35973 | -44.87313 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f89f11f-5fa7-3ac0-aba0-f69af6306823 | -7.52357 | -47.33443 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b0c2a89-c44e-384c-a31b-91747f73b11f | -5.84139 | -53.52168 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19e2bfd3-d72e-3ce6-8baa-9a27d3546e3c | -5.85299 | -53.5041 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45b8784c-3038-3359-962b-4f5eb580db12 | -9.12606 | -45.72016 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45bb71d3-f95e-33c3-a909-70c4bca8be63 | -9.0511 | -48.76448 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df084463-3911-3daa-9069-d992e2abb0b4 | -11.05179 | -54.17611 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ebe45049-ee51-31ff-811d-81c2118164aa | -11.45543 | -45.37585 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9159fe2-d73e-3cba-8180-aea63fb1e671 | -5.85551 | -53.53962 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11de0a8c-b123-3b73-99dc-c3decff57aa3 | -7.9127 | -46.01824 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe0f30ea-ee80-393b-b11e-5f4166cff1d2 | -5.85421 | -53.54726 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2199f45-894d-3388-b399-0394a7de39db | -10.32446 | -48.00497 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83a8b12b-2afc-3af5-974a-a01b73945ef3 | -11.84728 | -46.8696 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12d69f94-7d50-315d-9bc1-e8d4c3f432f8 | -11.09491 | -49.51881 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84ebf2a9-75bd-3664-aa2f-83b7eb00e436 | -7.18374 | -47.9005 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 706ce1fd-03b6-351a-a200-f25e8230f9e8 | -9.03566 | -48.71205 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d2d017-fab9-38c6-8592-c18749c6693f | -12.98226 | -46.93681 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de43c60-0c7a-3a29-81a7-9bcd42b5e972 | -11.06435 | -44.68564 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 511faf0d-0742-35cb-8437-5246eb3fd828 | -10.07523 | -45.67268 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b095366-9daa-3932-a360-2e2c338c4936 | -9.26085 | -46.18979 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab9ef42d-5682-3d57-bcaf-ebbc4c05b9c2 | -13.02921 | -46.95989 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b4838b-66a9-30b5-8b69-2005bbec5ff8 | -8.13801 | -46.80462 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d18aff9b-f7b6-34f0-825f-660ce8152c80 | -13.94674 | -47.84007 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de5932ea-3125-3f91-8302-7fa189de49d2 | -11.02015 | -48.33676 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32812191-d3e4-331f-ae2e-c13efb48abc7 | -9.67068 | -54.3277 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b74aeb64-26af-3d80-9143-c905fedf5e37 | -6.45887 | -48.44498 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b54d42de-71c2-3d96-8aab-57d600e95274 | -11.41557 | -44.21719 | 2026-09-20 04:40:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc402496-e87f-3e4d-9305-a756bec7d427 | -13.52318 | -48.93611 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24ae0c44-62b9-30be-bedb-98feec6aa36b | -7.54554 | -48.68299 | 2026-09-20 04:40:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ed330d-434f-3251-876e-7a16beec923b | -11.28281 | -54.05481 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b7339c-4f33-3607-8f09-32a2cc410f62 | -9.82024 | -46.43846 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82f60ab0-6bbd-307d-9b71-e2a4f4c270ce | -11.85323 | -47.64103 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1d9487-f0d9-33b2-84b3-456ca3a6d9be | -9.93416 | -60.73522 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51a1d313-e35d-3497-bce1-7971f4ee649b | -9.02573 | -48.75327 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26fa1a2e-39e8-38f6-809e-9ce42d5bfe09 | -10.7789 | -50.88182 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77701471-f541-3b00-9c4d-041c60cd333c | -8.61549 | -54.601 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf9badb0-c2d0-3b0f-97a9-aac7d31dfc17 | -7.76906 | -44.83091 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1b8a658-9723-3108-b270-a23760fd1246 | -8.16789 | -54.75492 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d443266-fe9c-3b8a-87f8-f2803a718c6c | -8.45496 | -47.65368 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66010f90-b351-3072-865d-8e4ffcdbc7b9 | -7.59636 | -55.70864 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3da1ae0-2431-360c-97e7-ee8cff7ec1da | -11.85136 | -46.8662 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3915891a-ed2d-334a-94bc-11386ffaa48b | -10.92841 | -53.94479 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa511675-8d7e-32e6-8a95-8eb255b30dd7 | -9.71544 | -47.2242 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0802c099-54b3-3ba3-b4d6-8b6f0369d4cb | -12.16125 | -47.01527 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2e64aff-a0db-3612-ab7a-69ca918687a4 | -11.85211 | -47.67116 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04548146-e718-306b-80dd-6e63969140a7 | -11.12722 | -45.29576 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
