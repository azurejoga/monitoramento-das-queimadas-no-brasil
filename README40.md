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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec1ee717-9ee0-39e3-90b1-3da02d66f8ff | -12.29216 | -50.59217 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5acf6ec-26a3-3cf2-b498-c68511c3d4fd | -10.798 | -54.00212 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61732d3e-ffea-3694-943d-c9296f6d00ec | -14.88171 | -52.59713 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ceb1b224-880c-3acc-aad7-7d90b733a9cf | -11.48639 | -45.06785 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc7b17e0-147a-3541-aee0-9bb8eb25b1ee | -11.20243 | -55.09399 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e85fef7-c9dd-3914-a98a-e8ba513ea83f | -8.60838 | -54.71807 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977edd94-93f5-36e7-9b98-95613615a3d4 | -9.45767 | -51.71518 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49e727c-808b-3a2f-96ec-dd2fc611d872 | -13.59912 | -45.78265 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7003d969-b020-3072-87ba-280a9421a328 | -14.16717 | -52.82016 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 991ee11d-7366-3225-a3fb-f155aa455385 | -8.33605 | -45.72177 | 2026-08-28 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2d8ddff-cdb3-3b2a-a184-dfc896d4bb3c | -11.20172 | -51.2361 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0fa92c3f-5190-381e-bd0d-c3db5547f162 | -12.28551 | -50.59108 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76d7908c-b7e6-33be-b508-bbd327e6a9f9 | -11.19771 | -55.09814 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f29bf50c-faf8-33b5-a767-607aa41d3aed | -9.22661 | -51.54381 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e62f6c2-cb13-3f85-911d-da6100f5b650 | -11.21864 | -53.99547 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf90a62d-19bc-38b2-b44f-057399209fd9 | -14.15394 | -52.83696 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9ccaca5-de95-3ccb-9b43-84b0aae33565 | -14.41162 | -52.58874 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c08de40b-a1ee-3b30-b4c2-a6ac46a898bb | -9.22308 | -51.56575 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae469641-7e8c-3690-98ec-38f2b348989f | -14.84651 | -49.21856 | 2026-08-28 04:51:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e563b4e-78eb-37c8-a4f6-87402f30ed3b | -10.50718 | -64.51002 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| d56552b0-41de-3519-8d21-c5b3f1827311 | -12.23339 | -50.57534 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e65534ed-b194-396b-85b0-230d111500e3 | -9.87298 | -60.25261 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 356eeac6-38f1-3e7d-ae6f-d211d9eca91a | -11.20002 | -51.24672 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46d77b3a-913c-3bed-add1-87847057e1b4 | -11.47877 | -46.94254 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deb0a2a9-541a-36aa-8e93-930d0680d9f5 | -11.22482 | -53.99887 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c8e21c-83a5-3abf-86c8-900ebc6c26ed | -14.91807 | -52.61416 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 431ff269-734a-3776-b1c1-848f81774d8e | -8.60267 | -54.79185 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3dcc077-5354-3019-92d4-6611ce9d0bfb | -10.78917 | -54.00954 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 044f4966-d463-3290-8310-8082a816f2ab | -13.37326 | -41.35232 | 2026-08-28 04:51:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a927fc93-c11c-3014-80ac-b7699cb1ce13 | -11.19612 | -51.24971 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e389c0be-2934-3633-bc6b-8f3f1143fcdc | -14.96648 | -52.59252 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cee305ea-3d5f-380a-a920-2dbb98526a58 | -12.78439 | -46.44599 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9462dc95-6a28-300f-af05-56852cc57c10 | -10.63407 | -45.22459 | 2026-08-28 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e061701a-1bd5-3282-a958-af9dcb565f74 | -11.23939 | -54.00153 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47a16c83-2360-325c-a311-1baa26ab0530 | -11.37671 | -45.14287 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd0d4e11-3419-3843-8e14-c3af915340c2 | -10.79519 | -50.64234 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d734d9b1-cd3a-307b-b28b-87852150c4a5 | -14.15639 | -52.82215 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8443a825-efbf-344a-8668-e90fdc2fc498 | -13.59551 | -45.7782 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07599511-cd7e-319c-86e2-1418731b0f7c | -10.79295 | -50.63857 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 302ab7b5-41cb-353c-b9cb-6f072729720c | -14.16378 | -52.81959 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcf42446-6109-343d-9859-97f4d311c7ce | -7.38305 | -55.15306 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac7df212-592a-3cb2-9fac-dec1332358a6 | -8.5882 | -54.75798 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 669b495a-5ded-3d29-85ac-271f11604cd0 | -10.06044 | -46.94286 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc8fd381-2030-3a42-9e0e-f5a73fbb6e58 | -12.28884 | -50.59163 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93c2d3f9-5905-3840-8d8f-5e455d236453 | -10.55653 | -50.48476 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82625a3e-1978-3461-ab61-a434ef5b9fa1 | -6.7593 | -55.69118 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a43d7509-61e9-33f6-b168-6dd92543a6f1 | -14.93113 | -52.59769 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e75fa2f-e656-374a-a6f1-ff23566aee0e | -11.63577 | -46.73381 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86e61c5b-b3f7-3399-b801-30cd0c910c04 | -11.16344 | -51.2189 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3c7d049-2df9-3326-9690-1147c940d2f5 | -11.27879 | -54.01277 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69080d5b-cb19-370f-bdef-cdd2dfe338bb | -8.79169 | -50.07189 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80957a01-ee68-3c20-a304-20e43651b5df | -12.43276 | -43.41141 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8a3bee5f-2c8c-35b3-9cb7-37a18dd05e5a | -14.584 | -53.17554 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ebd564f-e223-31c9-bd57-4ba112b565b8 | -8.81383 | -50.08259 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66eb6dda-bc6e-3f40-88eb-8be145fab23b | -8.93653 | -50.71562 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9618b1f9-56b0-3768-b4c3-46e5c3799619 | -13.46552 | -57.04692 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1652bd42-149c-338e-aa4e-325f85441229 | -10.77184 | -54.03107 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcc6be29-e310-30c8-8f02-99ca5cb9d22b | -10.5726 | -57.48985 | 2026-08-28 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82764c91-a67d-3537-9651-81d336000848 | -11.02154 | -49.65826 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb942cbe-2c1a-3162-80dc-c150fb63dedc | -11.20229 | -51.23257 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ab872bf3-defc-3f5a-b641-211073ff25f2 | -9.61367 | -55.12427 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82020726-cab0-36c6-866c-9d78a389a611 | -11.20392 | -51.24373 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 301552e0-8670-3c47-82fa-b2b9ab5bcc5f | -12.76667 | -46.45834 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 523af01f-b78c-3ea2-aaed-23150406909d | -13.58212 | -45.78385 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c155c85a-0e86-3f3d-b487-b85b502e16de | -14.93448 | -52.59829 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4d92b26e-03aa-34c8-b292-c048b431b6c2 | -14.86901 | -52.6327 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02f38b84-eaef-353a-96ca-52269ebe1e12 | -14.16039 | -52.81901 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30433fe9-a01a-391c-a3c6-cdc988977df5 | -8.77452 | -50.07272 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d9324a0-d9b6-34b0-becf-91ae115fa494 | -14.95917 | -52.59502 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f1d2b48-fc32-39d5-9744-b90371db2ab6 | -14.98483 | -52.60698 | 2026-08-28 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53480a55-e2c4-3f46-a67b-a408130281a9 | -11.16571 | -51.20476 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eef74c02-3c0f-3c99-9002-7c27f6b45cfe | -10.92115 | -50.52934 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e00679a9-1791-3653-b90a-b1b04c3f3c8e | -11.64403 | -46.73017 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae791ace-f3d4-337f-a2ae-59d271fa6126 | -8.59514 | -54.77299 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4106ba39-979b-371f-81dd-7fb96c4293ec | -11.17067 | -51.21646 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b152cc70-2887-3541-910a-26a5dfb45392 | -11.23973 | -47.08072 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5663d13-9a5c-3e6f-af9a-b3dae5f024e3 | -10.78775 | -53.99589 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ee7a37-2612-36fa-82c2-a1eb2a6ccc9e | -11.00869 | -49.65256 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0393d5c1-10e2-3021-8875-7201efb35c20 | -10.91548 | -50.52863 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d54d7701-b31a-3c51-9bd4-28bbd2e8ef37 | -11.65027 | -46.7407 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ebe0697-166c-3090-9718-e8da2faebcbc | -12.45447 | -46.52222 | 2026-08-28 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5a09874-86ab-34b0-b595-26b57b58c743 | -14.40379 | -50.12319 | 2026-08-28 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f50851e-7432-3ff9-9118-04c7e2b43a51 | -15.60101 | -46.57756 | 2026-08-28 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7249dcdb-8a71-3366-885f-acde8d1a5676 | -11.65406 | -46.74121 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f222d7cf-2424-3772-81bc-30c719366d95 | -11.51174 | -58.51238 | 2026-08-28 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ce1522c-8689-3286-b88e-26702ff3d57e | -9.43373 | -51.68924 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dad77c45-3bce-38b0-a52b-12a2c748fbec | -12.91511 | -59.88657 | 2026-08-28 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b126f6c-6f7c-3bf1-9797-55ee73a2c00d | -8.59958 | -54.78616 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22ccd1d6-e573-3bd4-8026-e10df9974263 | -9.96443 | -53.9391 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e7833f2-1db2-36d0-a08a-c6aaf4b1d673 | -14.43383 | -53.38398 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08d68920-179e-3548-8867-dfc41bb48301 | -6.76291 | -55.69611 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6859f707-9b11-3d9e-8fd2-304daad8d4b5 | -10.50801 | -64.51918 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 245b1744-0db8-333c-97bb-119318f70943 | -11.20115 | -51.23965 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f5230ebc-c1f2-3f9d-a8fb-89a02e6fa1c4 | -11.19952 | -51.22848 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6ae74e0d-3ae1-3f08-9c6d-3f149a0f0cad | -14.86409 | -52.62052 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 84565799-14a3-3ce1-8c2a-464bf422c6f6 | -7.34859 | -55.66096 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 590c4a6d-0766-3ed9-91df-a1424737185e | -9.43757 | -51.68935 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dbc6e25-34f2-34e2-bea9-36471170090a | -14.99154 | -52.60812 | 2026-08-28 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ffeaa3f-f888-3344-a619-b6cb032c2795 | -11.19553 | -55.08762 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 438f29e6-442e-376b-9092-ee562e4b206e | -13.41323 | -51.41457 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README41.md)
