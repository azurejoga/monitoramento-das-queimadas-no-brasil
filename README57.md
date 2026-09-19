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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c2a7c0b-c231-30f6-a97f-cf275c47b4b9 | -9.90686 | -46.59081 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bbacc17-9d33-30fe-8c80-5193a1b07975 | -11.12353 | -47.71338 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a72b1d3e-1a0c-3477-aabc-a0e1526fee82 | -13.38507 | -48.03672 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4510b5a5-4de5-3ced-9774-c95409ef5358 | -10.70528 | -60.74052 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ee52ee23-573f-3275-a188-2ea46733129c | -11.85473 | -47.44916 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a69a6554-398d-387c-8f5d-a497a0d070da | -11.05494 | -49.74092 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9fa9812-0c29-39d4-b716-0a1ced4e2336 | -12.68974 | -45.95525 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc606548-0b83-361d-bd08-fb299896a9cf | -9.8633 | -48.34476 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90afdc4b-0ea4-31ab-a57a-e1500ee08078 | -12.7445 | -47.02153 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b34d4eb-5367-3f09-8c01-f2336cb8dad3 | -11.91305 | -50.11665 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 958a4060-0acd-3936-966c-91e70e3c2c54 | -10.79588 | -50.87937 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 337187f5-38d9-3234-96b7-5b90232fe6a1 | -10.13617 | -49.15583 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2a8d05d-e42a-371b-afcd-056692739e25 | -9.60887 | -45.37956 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb32b7c9-0733-351a-bf6c-e95afc1adab8 | -11.87614 | -47.61556 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c53ff52-cae4-3284-ab9a-84f6d833fdaf | -11.42051 | -51.45629 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79175ef1-6f5c-3ae4-a1f0-7991c2f8465a | -7.59505 | -55.69594 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d03c2c6a-e87d-369e-b68f-f619af2e854b | -10.32607 | -45.34008 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef22723b-4c23-34b4-aaea-3d53a33d9deb | -9.89254 | -45.82304 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a16b5a-67a9-3f90-b4e7-4a8b955b2b15 | -11.222 | -42.83026 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df9b42b0-d0df-3abe-bb88-ec0c13b56439 | -9.03109 | -48.7291 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f134691d-6f0b-33eb-8d4b-9cb83c7a6287 | -12.86468 | -46.3384 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50a31295-b30e-3d38-a342-11d281844e1c | -13.623 | -48.30944 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dcf50791-d6c5-3a7e-a58c-a27c3d1d293b | -10.86155 | -56.20467 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb665b98-3638-3df4-a1da-41f863bca5c1 | -9.79759 | -48.33701 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df6104bc-7050-3fed-80df-7c93a13d61b6 | -14.79619 | -48.54148 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 007b577c-ac69-39e2-86ee-8a4cfb8f0876 | -13.3028 | -51.64784 | 2026-09-19 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67c56ecf-c516-33c5-8f44-3b3be4d1831e | -12.13809 | -47.00124 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 783e5c40-3aca-3285-b75f-1821b3384102 | -10.8604 | -54.10538 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aab0adc6-3be5-3819-b2f4-b9df5de7c761 | -11.13591 | -49.04572 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1bdec45-f6ad-3efc-8271-123835535373 | -9.70153 | -54.83088 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79ef1dab-df0e-3baf-92d1-f267e851238b | -12.1392 | -46.99415 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4323ce2f-3a4b-3bc6-a1d4-9b027499af54 | -12.39699 | -48.48397 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cd7bd70-0a14-3420-8454-7dd9b260fd4a | -13.18564 | -47.03321 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06da5e9d-3c84-39e8-b024-160c35c87ab1 | -11.30938 | -47.26669 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b125f28c-5b4a-3bd1-a8a9-637ce26e5473 | -10.92768 | -53.96314 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f462935-2d3a-313f-bf98-a8cd43d1a8a8 | -11.13598 | -49.04184 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8208c473-7e35-3231-a099-e428d063492d | -10.13141 | -45.56548 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14c6be8f-5ddb-339f-9f96-d795baf5c973 | -10.85999 | -56.18473 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dc01fa1-db49-3020-984d-0f503874f4bc | -9.24903 | -46.21614 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 902ad75d-b51f-3a6f-b2aa-c0670bfc0289 | -14.6773 | -46.68013 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7502d5b1-13d2-376a-a668-6bc27fbefe9a | -12.70401 | -45.95361 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 92e2135e-3299-3b00-9b43-317ae1356ab1 | -9.72008 | -54.81172 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 940d4a04-958e-31f8-850e-09c272909e5f | -11.46837 | -47.65043 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e639308-8d82-3946-94e9-ee90656672a1 | -13.62634 | -48.31 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f010d6e-da54-37c8-b586-40cece2d7245 | -12.86211 | -46.33121 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94ea34b2-d58f-3506-a04b-18aeccffad13 | -8.77825 | -48.67676 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9d28f1a-9cf7-3970-9cb1-f1756bc90959 | -8.50387 | -57.63298 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b01d41-5444-31d4-8765-7d9a2b250e21 | -9.70945 | -45.99364 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46b0da15-003f-3221-91f5-9c805bf7ecad | -10.17033 | -48.51716 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4fdc426-2ee8-3c58-b8a1-1c159bf58ad8 | -11.27194 | -54.11794 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f021d36-5af1-38ae-8ce4-47626254a016 | -11.41753 | -51.45096 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad64dd7e-63b6-33c8-9ced-06b5941dfe94 | -14.79262 | -48.58504 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35bb2d8d-c9d7-34a8-816f-558981651b63 | -10.53894 | -46.59747 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea9ef4c4-1946-3d77-bde2-7873e34637bb | -9.91349 | -46.57029 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3032b44-b93e-3f54-8a42-9382bb823a21 | -9.25119 | -45.92887 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76842b60-9452-3a26-a694-3eebb180f213 | -11.14278 | -54.02893 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9ed27ba-0094-3c7a-8d90-650addbeb257 | -9.24008 | -46.18574 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffda6807-a988-36da-ac99-304fc3a9bc40 | -13.61683 | -48.32673 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e6cdaab-d074-3a20-9c42-f1668230cdaf | -10.86615 | -56.2088 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9f9e5ac-e4f3-335d-aad8-498d7ae955e2 | -8.77605 | -48.66863 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76db89d1-6fda-3e3e-bedb-44159d156ace | -13.87958 | -48.60516 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed19e8a-23b4-32e9-88c7-2e41e22dce1a | -9.96408 | -46.61808 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f0cb69f-ee45-340d-883b-ddd1cf657411 | -14.69373 | -46.66365 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db810df3-86dd-33bc-9a61-844718e07b83 | -9.89988 | -46.55383 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96ea3b04-b0f2-3379-9d10-da7847e92a0c | -11.44381 | -51.4797 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 961cf1ba-b73f-310f-a70c-e97693809990 | -7.59243 | -55.69406 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bddc708-b763-3b16-a216-336a9757d25a | -12.27934 | -49.16616 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b737776a-52cb-3f41-840e-f9c6bea484db | -9.67975 | -48.33269 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c435e9d0-0e16-3b24-a6f3-aa35343a6bc7 | -10.12577 | -45.55686 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb781845-fff9-3234-b387-7a9f28b1254b | -12.26212 | -47.67435 | 2026-09-19 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10731f5b-38e3-3c05-93e2-0587a902c0b9 | -10.27094 | -50.0037 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 961827fa-9a3c-37ea-9cf6-bff46e5ae557 | -11.42132 | -51.45165 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd06b04-3509-3cc7-a878-1b2051688dda | -12.35062 | -50.69654 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3970676d-2a52-38f3-a284-12dc27b42a8c | -12.98274 | -46.97897 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3b56e37-bac8-3a33-9995-12f6d7f0e4fc | -10.92743 | -47.85513 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f93ddc3b-353d-3824-a160-57180ae47924 | -8.87906 | -50.7819 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 475ed95a-450f-3f0a-9ecf-bae085a44f6a | -13.23345 | -46.91134 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 500b77d4-2b3b-30d2-8a3d-8e64e1655bca | -15.02379 | -48.55788 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22900854-927a-35bc-9704-e58c839b1573 | -12.16146 | -47.005 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 082d2358-622f-39f3-8991-d4b5174eefa2 | -9.94122 | -46.52425 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 800818f4-0aaa-3a05-9315-244b2a7e6ad5 | -8.60717 | -54.59861 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2aa72a5-ab9f-3ae6-a13e-fe88003469b4 | -9.59977 | -45.37063 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 892a7956-e249-39d6-9924-66482478f512 | -8.78107 | -48.6811 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f784ccfb-7639-3572-91a1-f400ec00d1aa | -10.86215 | -56.20158 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 648a5907-c868-33ab-9c10-a952090ed5d7 | -10.26806 | -49.99901 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79e0ddf1-0d40-3855-a654-d358e010ca4f | -9.96049 | -45.4523 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 149007e2-f9e6-3946-9fac-7d0ead2fc36b | -13.59884 | -46.93614 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0dfd708-cb7b-3516-9f84-3e2f1212036e | -13.01452 | -46.95097 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ce2208e0-86a5-3fcb-ab57-a664cdce7699 | -11.33578 | -47.35385 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e9918a5-4f3a-37dc-bd3d-812810cf6024 | -8.42419 | -54.73279 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9b4de62-ea0f-3b7a-90a3-4da980662cba | -9.76548 | -46.07556 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22bcdd0d-8cac-33a9-8bd8-a02d17068ae8 | -9.80609 | -48.32731 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 102ed4de-5798-3095-b7a5-99181b6fe9a8 | -11.81996 | -48.83394 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20cfb67d-4773-3967-84cd-ebbf04f7a7f5 | -14.10197 | -44.82846 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fb41daa-5c0e-3761-bcd5-6fdfaab280f1 | -10.86919 | -56.19289 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d6f0180-b517-32da-856e-5a8fc0620d83 | -10.85639 | -56.20351 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c60e909c-15fc-320e-be4c-9d31851be6d4 | -13.59491 | -46.93925 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f1ced7-fff5-3bea-a7de-c0efa56221d9 | -9.74256 | -46.09025 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7917880b-2f95-3948-b06e-9c7e88223c6d | -7.5729 | -57.69202 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa7b087c-918c-3d27-b88f-034a6567d237 | -9.03171 | -48.72534 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README58.md)
