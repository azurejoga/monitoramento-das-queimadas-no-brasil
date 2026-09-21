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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35e3f777-96df-3ef1-bee6-0dabed6703e0 | -10.21911 | -53.92348 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98c34a8-94db-330c-9d34-7a2137cf40cc | -11.07648 | -54.02396 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8247d5a-1703-38de-928b-43b14b24332b | -15.60252 | -48.09679 | 2026-09-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae2ecd12-6be8-3b9b-904e-78cc9336c97c | -14.6507 | -45.70194 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3719ed5e-f7f0-3317-8b60-27e435b38706 | -10.47839 | -50.29895 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7effdc5d-f329-3f61-82b4-278eaa092d2f | -10.45772 | -50.29092 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20638e9f-169c-3c68-8fa5-e4eb8d7047d9 | -10.90973 | -53.97115 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9925e98-746e-3658-a036-acee0c78751e | -14.22542 | -44.63568 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 01eeebee-304e-39f4-ba1b-ef585ed9ef22 | -15.45677 | -48.46572 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaeae281-fc28-333a-abab-39b21175f958 | -12.14516 | -45.13953 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5777a49-40b1-3a63-a2f2-747011d967c5 | -11.03954 | -54.15466 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b5b51eb-5af7-354b-abdb-2e6140270d47 | -10.45868 | -50.27073 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bb7875d2-9986-3672-99cd-52681c097335 | -10.4713 | -50.28918 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c6f0e08-bb09-3476-8d92-73e2a4f24559 | -13.0373 | -46.95895 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dd11dbb-b6df-35c9-b2ff-bafcfba6e41f | -13.03537 | -46.97051 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0621dcde-17cc-3e9f-ba84-5760c0ea763b | -12.27352 | -50.15783 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89164781-b6e9-3416-8343-b34a6c12a0a6 | -10.46009 | -51.33535 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05d763f1-af80-368b-b941-2c594e7e3657 | -13.59344 | -51.4703 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1590824-802c-381f-820d-a6eb400df169 | -10.81704 | -50.77873 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d273310-a107-3d1f-a7ec-0e410056d965 | -11.86101 | -48.97829 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d685a6ef-1e36-35ab-93b3-cf44b90489b5 | -13.27197 | -51.75939 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97597ca5-14a2-32a4-ac57-7f62851bb26a | -11.0435 | -54.16266 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fc84832-7ba7-39ab-b336-d41392ec02ed | -8.60476 | -54.62189 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daacef59-4815-316b-b68e-f1acc9000f3d | -11.03676 | -46.55672 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60f8ae41-239f-3200-b75a-13a1c0f936b2 | -11.35498 | -51.34684 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d692f584-2750-3dbd-8b17-ae4678e2cf80 | -10.98231 | -50.59092 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7f70efe-d37d-3663-aed2-b38be0d347a8 | -10.07166 | -50.24241 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ce5b969-bb9e-30fe-a86f-f2df6347ae77 | -15.45105 | -48.47772 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ef426d1-50be-3aee-9383-3323e99bc01c | -13.47467 | -46.92553 | 2026-09-21 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efe18901-9614-39ea-8440-c4ee4db6c5f2 | -13.89305 | -48.57035 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 436c84d4-6522-364e-8138-33c446f6079f | -16.05172 | -52.51707 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5a66d6d5-ae5f-3e11-9b53-76e3ab7460d4 | -8.17944 | -54.77864 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6980899b-5632-3f39-a23e-c5efa7b66302 | -10.91107 | -53.96417 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 810b934f-8002-3fa8-862f-d6eb0a49a531 | -9.97869 | -46.63648 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f10169-92c6-3fe0-a290-e8882f79b004 | -12.83137 | -54.0553 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dca9eb3d-a772-3de7-b6ef-daf35139f593 | -11.09414 | -54.02007 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef81fa98-8a7e-3afb-8a44-109772ae3891 | -9.67526 | -54.33491 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a4e3ad4-23a0-339a-9261-cc8529f0c820 | -10.13538 | -45.54882 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9952ddd7-11df-39e8-8fc9-ae64c6b5a82c | -11.04499 | -54.1559 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b30a1f5e-ee96-3dec-acef-69162e4f7395 | -14.67383 | -54.47503 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e60f3b-1cbc-3815-90e7-159b573f4356 | -14.66275 | -54.47598 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7257b9-4da7-3a98-a097-f53f9abb3402 | -12.82546 | -54.05751 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4db1c9c9-c96e-3b05-81cf-c17426b365c2 | -10.91783 | -53.95826 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfa6f05a-5068-3648-bcb8-13f448931762 | -10.30997 | -50.55447 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e895ebd4-8020-345f-8141-fe4e268fe4a0 | -16.01503 | -52.5312 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba86601b-036c-3cf0-b028-7e0acec7965e | -14.18436 | -49.59192 | 2026-09-21 04:21:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 252f08a0-0e36-3122-9c29-d8cbcff9375a | -10.80477 | -50.77322 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf175d16-a54c-3f26-aec9-a87c345486f3 | -11.85585 | -46.88653 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d350fa8-1a2e-3524-b342-4c48ec21962c | -10.74935 | -50.80346 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 909fc5e9-3c72-334b-a02b-0c4798c25082 | -12.53809 | -50.03585 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2fc2619-813d-32e0-aa8f-4f07dc63595d | -10.09591 | -46.09164 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200f17f0-4b0c-394d-8396-3aa59d3a4256 | -9.96823 | -47.98499 | 2026-09-21 04:21:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 885cfca2-1e0d-3c7e-be46-2474623979dc | -13.26338 | -51.80528 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c417711b-ec8e-3200-bfe4-52daca979e52 | -15.55029 | -42.62957 | 2026-09-21 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be9c2ca1-f731-3fef-b840-ef5a110ded58 | -10.47588 | -45.10152 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c69c69ec-0562-3678-8c5d-29165afdd54b | -14.53529 | -53.37558 | 2026-09-21 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e47ee0f-492b-3628-9597-592b4952d77a | -11.0292 | -54.14813 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3db101d-5ea1-384e-9f48-ab2545e47de0 | -16.02663 | -52.5192 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e1090f17-a096-3087-9d62-65a74a336715 | -12.82677 | -54.05086 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d98630c-acb5-306f-91c5-451cb3704895 | -13.17661 | -43.56543 | 2026-09-21 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ffa37e55-96e2-3586-9f1a-ca85016daa36 | -11.0805 | -54.03222 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77d3e9b3-3034-362d-8762-b083b8d0ac03 | -10.76336 | -50.80156 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25a474eb-2d1e-3ca6-8cb4-fb0e58210e98 | -8.60397 | -54.62621 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f249e5-cc56-3b47-870e-aed60bb0c0f1 | -10.69413 | -50.76013 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da5f3af5-3bac-38ca-ba70-fdd43dcc337b | -11.4653 | -47.75787 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eb6a7e8-eb0b-350e-a05b-344e2f800dd1 | -17.59017 | -43.68778 | 2026-09-21 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbc93a29-7568-3fa9-a0cd-a35206f35aba | -15.46679 | -48.40664 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee550643-4968-31c2-a7d5-f65937d5a3f0 | -12.53497 | -50.07731 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 289a0230-6aea-399c-9724-024403496d36 | -10.67447 | -48.71473 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff39db33-3fc4-3274-9c4c-bb2936aec5fc | -14.18106 | -47.8783 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa667983-9d53-31d4-aaa3-ff37ed373e4a | -12.1949 | -47.04722 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f34d0df-22b1-3de4-899d-99e129cec3e1 | -10.69127 | -50.75057 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2ab062b-55bf-361e-85c6-fe0f732a18d1 | -16.04185 | -52.5198 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2595d401-c612-3aac-a8eb-e03841ee87b4 | -10.87063 | -54.086 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b7a1877-2d38-3f04-96dc-d39fc33784fb | -13.86717 | -48.58909 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2ca1c75-ee61-373c-a7a2-7a469006e561 | -15.45894 | -48.43126 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93abfbb5-958f-347e-bd7d-4daa1a88ff0a | -11.09449 | -51.06782 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b8dac48-1ad0-368d-b2cf-41d25c3954c6 | -9.84739 | -48.39714 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c317209-f075-3d43-a967-85e0a0b4071f | -16.0347 | -52.50853 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d1980340-1218-368f-807e-c2d64715046f | -13.47124 | -46.92492 | 2026-09-21 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 322ca1e1-bdac-3bde-b51d-53f06011e13b | -11.04721 | -54.90278 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ee1aac4-08ac-3a85-b6c5-7a7ff9572a8f | -14.04615 | -52.06871 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6cec6069-0375-371e-9d8d-1430a0708005 | -8.18029 | -54.77412 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d12194e-16b7-33bd-8de5-d08ed2ea723c | -10.57709 | -46.53258 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e456157-f0e8-30ea-83d8-9e6516f3aade | -9.97326 | -50.2594 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d887ba10-dda8-3fae-ad9a-3407d59e82e7 | -10.36387 | -50.21775 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 481ce186-22a4-3ad5-8820-3c0590cc069a | -16.02658 | -52.52619 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4c5be56-a378-32cb-8e4a-0a481baeb21d | -11.01897 | -54.14214 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74048188-076c-3d96-888f-baf8f60aa965 | -14.65494 | -54.46024 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a7889e5-0d98-376e-98e7-10ecd20b61f2 | -12.53971 | -50.07435 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6451ade-0f7c-33d4-9568-346771099ad4 | -9.35172 | -50.09016 | 2026-09-21 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd94812-6989-31cd-abf4-670cf8cd45ed | -10.54048 | -54.49207 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e0f7e2c-3e14-3b0b-b958-cbb3cbe6434f | -8.19278 | -54.70754 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b676d63-6a35-3f81-97bd-d97e11e42d85 | -11.0795 | -54.03133 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4afda29-a0a5-3e00-b7e8-a03b9a69318c | -16.58477 | -45.35053 | 2026-09-21 04:21:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34bed47d-7da8-31e1-90bb-70cec3cf6e73 | -10.69685 | -50.76657 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21ad3ca0-fa18-38c7-a3e2-330131ca011f | -11.6759 | -43.44132 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e152c787-b684-3535-8512-1832cc23191c | -10.46924 | -50.27613 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d3d2c8e1-ad7a-3555-b562-e805dba02e29 | -7.57246 | -57.68077 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1c076a52-5e40-30a9-99b5-499aea333139 | -10.07092 | -50.24654 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README47.md)
