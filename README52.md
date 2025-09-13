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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd97a91f-754e-3328-b50d-15ea18b103a5 | -9.2532 | -51.23964 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4948928-e9b8-3021-87f3-ddc4749db3da | -11.40564 | -43.53069 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1755274a-b044-33cd-ac0d-d1da9562f47c | -9.90875 | -51.88933 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9751ed77-28ca-3194-adde-e22be3fc6a31 | -10.70751 | -50.51231 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 310638d7-8f49-3f6a-b0cd-dedb8d733a2b | -11.18011 | -51.42908 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da1c61ee-4c97-3571-8d67-1190bf18283e | -10.7417 | -50.50298 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 33ff627e-90c4-358f-b81a-01a6a303cdcc | -10.70198 | -48.65642 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71170a2f-f669-3f01-9e6f-2c272079440d | -14.45842 | -47.32758 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f34a0e04-e02a-3176-8a57-ecb7dc7bd85e | -9.06252 | -47.03442 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 976672cd-efb6-3cc7-8e06-8146f419297e | -8.95203 | -44.44389 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7c5e8cf-9a26-364d-bdd9-23a5381ff58b | -11.20481 | -48.42559 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1a6a65-7f03-3851-abac-e97f0f58435b | -11.45383 | -43.57155 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37135030-5454-344a-a3f8-be3d5bd12cec | -10.92449 | -47.20979 | 2025-09-13 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34c837e1-3ba3-3271-a779-f748efa027aa | -8.09085 | -50.19659 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4472c3e6-42f6-30e7-a8d4-eeedee23d787 | -11.8658 | -46.76846 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fb4f6a4-aa1e-3b40-a681-5bb72b2efec2 | -11.84159 | -50.57996 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 489a8d72-2543-38be-8ff0-56947fa920bd | -11.2115 | -41.59489 | 2025-09-13 04:08:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6dd73da5-1caa-3b3e-b314-3a1813fc004a | -15.77972 | -41.52013 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 397ee118-2955-3310-b57f-5e05928c42e5 | -12.80979 | -47.96517 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 164e9903-d583-31a6-a416-12888d29fa86 | -12.82353 | -47.95726 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e79cc3f-ca35-3043-a68b-41349aef75e4 | -11.85502 | -50.58814 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37b7ca39-a1a0-350c-b75a-f2da2f4054f4 | -14.4577 | -47.3317 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c2a0b9a-62ca-3c99-8e2e-1e6069cef6f9 | -9.79562 | -48.89532 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84a0d6bf-ee90-3af2-b9da-53d3bb8fa2b2 | -10.65783 | -46.28779 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 39ec4647-5581-3571-a996-642432fd606c | -9.52006 | -54.64597 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 5157a5ee-896f-3808-8280-a13b181f1f79 | -10.50426 | -51.54815 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a34d481-942d-3a20-a0e2-2fec802ca8c5 | -11.43831 | -43.56166 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a1f505a-1af3-31dd-8057-b70271767043 | -10.33881 | -48.81118 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2efc4646-e2c3-34fe-a042-d6531676db04 | -14.22094 | -46.26776 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d45a540-d270-318f-aba5-483b082b32c0 | -12.95057 | -47.99288 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b95cec0a-cdbc-32a9-8b98-3aca779944ac | -13.40553 | -46.80323 | 2025-09-13 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74e1eaca-9503-332f-9e68-3c12451afca1 | -11.43576 | -45.62391 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 298562e0-af01-3848-9ecc-37e581e83fd2 | -9.23328 | -51.22966 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8df9827-39a3-34c6-be2b-6f5ca6efc9d4 | -9.79527 | -47.79463 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 500be14e-2f75-3c2e-9d75-09c90986ab18 | -12.94395 | -48.00718 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1e75480-8809-36f9-8d3c-dce141a46743 | -11.18299 | -51.422 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 50543ccf-cfaf-3288-a2b7-3874eb195a68 | -10.50489 | -51.54146 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7092c269-43c8-3c99-87d5-9f380885c4f9 | -12.8104 | -47.96172 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74e52c18-aa46-39dd-9d73-0a07ccc9c165 | -14.4599 | -47.31913 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62a8879f-b514-3c9b-b7a8-1a3ab586ee4c | -9.73676 | -51.01356 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcecccc1-2cbb-31b1-b29d-d291281cc9a7 | -14.75125 | -45.2611 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2af3d3-6c41-32af-a5c4-4625c33445cd | -13.08657 | -48.26547 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3592d6d2-5470-3ef9-8937-999b4087d535 | -11.26565 | -51.12538 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7791b2f3-797d-317e-8a4f-aca49fbebe1e | -9.02683 | -47.05071 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1316fe34-798a-3f0a-8269-c4ebcc60410a | -12.9615 | -46.74362 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 155b82a9-f297-3a7b-8fee-b7729d3d5cd9 | -9.88896 | -51.86709 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aad8e030-5bd1-32a4-9d03-465080796b59 | -11.71009 | -46.56343 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e61000c2-bc30-3b62-bd07-ab2436dba4c0 | -9.00328 | -45.78223 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5ab841c-5da6-3bf1-8d25-344fe86b6e9f | -11.4448 | -45.62875 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbc35118-2cd0-3fed-95ed-7061d566712c | -11.57479 | -50.57989 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed7203ed-5827-37df-83f3-f047acba4e94 | -11.43888 | -43.55809 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08f554e9-08c7-317b-8c3e-95b88b09f369 | -9.85851 | -43.13614 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb871c2a-52c7-3d91-9f28-950ec3ca6f83 | -11.83015 | -50.56109 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe0372ca-d672-3e9d-a2a8-2b3908016997 | -9.80205 | -48.90166 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31b5df59-bbb6-3b5e-8ec9-52253b583107 | -11.86758 | -50.56942 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b17c6fb2-d66f-392f-b7af-da46e48ff47c | -11.56616 | -50.57261 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bac8ae9b-a613-3131-b80a-058648c37d26 | -10.36934 | -45.43129 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07f32682-5730-38f4-84a7-2a4cadd32736 | -14.19187 | -46.24485 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53316804-4b61-3c75-981e-afe8482ee1a0 | -10.242 | -48.64085 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26d6a171-17c1-39cb-9a08-66bcff1803e6 | -10.45881 | -50.61253 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17c54a71-9496-354b-947f-ce6ec4266c43 | -11.76621 | -51.51174 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dd2f53ac-f6ab-3f9f-82a6-49e7d4c87875 | -13.7742 | -46.29163 | 2025-09-13 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a690b7a0-38f8-33bc-bf8c-1604d8213d46 | -11.40615 | -50.73894 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d01538b-54a7-3782-a093-c50baa7395a4 | -11.99556 | -44.02507 | 2025-09-13 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08fbb20a-4957-3efb-9f63-42823c5f3e6f | -15.06249 | -47.98869 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04438a72-04ba-32c8-87ad-2674f02945e3 | -13.1472 | -47.13382 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e772455-72a7-395d-a1ee-55c7df500138 | -15.10925 | -42.47127 | 2025-09-13 04:08:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4cac948-48a5-3905-9907-e5d6a8e220a6 | -10.39304 | -48.60229 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efcb8c6c-f31c-3bc1-afa9-7fc9b29fd87f | -10.76304 | -50.52425 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c6a8d10-69b8-34a8-9209-60037814b099 | -9.05609 | -45.82068 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afdb8aac-1fbe-318f-b543-16bbe7528116 | -12.81901 | -47.95954 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5a9742e-b408-3858-b783-a6e78d3e7df8 | -11.7403 | -44.21536 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1393235-c95c-3d40-9657-8097938da1b3 | -11.86656 | -50.57475 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 829695b6-65d7-3843-b5fe-650083372cef | -8.40469 | -47.26406 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a29089b-4207-307f-979d-9264172ff783 | -10.08974 | -47.19901 | 2025-09-13 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b425770d-944f-3639-9752-8ff0bba9cd20 | -8.94443 | -44.44667 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 767d451e-b965-3dce-974e-d9fbee0d54c7 | -10.6586 | -46.28325 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e7205405-1d90-3bb9-9f52-06b38e97b0b3 | -11.74186 | -46.60975 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 466cab95-74f2-3fe3-83de-33dbb3664715 | -11.42777 | -45.60576 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbf905e0-5907-3dfb-9a0e-f210abe9c8d1 | -14.19759 | -46.27565 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6eb19256-b930-30af-84e8-073522d06882 | -11.81675 | -50.55294 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ac04b7cd-3e55-3098-b019-4f5a2331c678 | -15.82794 | -43.1392 | 2025-09-13 04:08:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8cfd5df3-39c2-39c3-baa4-042c70f47e0a | -14.01068 | -44.77421 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dcf0a60-12a4-3f8a-919b-c619cdc027d4 | -9.71397 | -46.87523 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b912509-b1a3-3296-982c-b7d66ecea818 | -12.13283 | -44.83797 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec935ec0-1276-3b15-8efb-e6b11e36562b | -12.56501 | -45.67747 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f251c09f-9a49-325c-864f-8e35ebf86ce1 | -11.45864 | -43.57887 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d006392-c021-32e6-92f4-b5036306bad6 | -9.95964 | -50.38334 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6172d80-4209-3169-a732-dbfa0f646033 | -11.4284 | -43.5381 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba70c55c-ce9c-309e-95e9-90029e42bcbd | -12.79933 | -47.97765 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bdf026d5-1cfd-33e9-acfb-81927716f97e | -14.20111 | -46.25506 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fd00df2-3f74-3974-8fd0-ece606ac9522 | -11.41821 | -50.74499 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41426d57-48bf-359e-b906-637bd0b1e618 | -12.10397 | -44.88889 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5cb06f4-a062-3cfe-89e0-bea072c3bf2b | -14.18118 | -46.26442 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| acce4619-2c4e-313e-91e5-b3eb1af8d66d | -8.9514 | -44.44775 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34b9cae1-d421-3e27-bb92-d28501387ff7 | -12.91562 | -54.76488 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9bcae06-ae0b-34b6-ab12-fc9050558cac | -12.81501 | -47.95896 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 356bad4a-f11c-32e8-a41d-f1f670b93572 | -11.70491 | -46.54865 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 180583db-5a0c-3c9c-80b6-4bcf52164329 | -10.35547 | -50.50454 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae3c3d2-6169-33fd-9a0f-173a8e47a745 | -14.16598 | -46.16494 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README53.md)
