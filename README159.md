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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88162ea4-de7a-3e7e-9e32-448b615b3ade | -3.56775 | -54.68787 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d8bc3946-fbf2-3e63-9a2d-3f2b67b04ea1 | -3.43347 | -54.54163 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d770624-cc61-318d-b995-e7d5e1857b68 | -3.12168 | -54.17228 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 87dce578-b51f-3243-bd6c-992138fb0499 | -8.73903 | -45.13182 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59de1620-f8af-3adc-8d10-e6b10750a24b | -10.31344 | -46.25993 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78a3d3b9-3504-3b5a-9a78-a6e82cf2af07 | -11.72436 | -43.63393 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94d46f6f-baac-36cf-a375-d50e14d0830a | -5.70643 | -53.45439 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac495e2a-cf24-35ce-9d29-d7f4b9005c85 | -5.43789 | -43.44756 | 2026-10-09 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| efee0bbe-c7e0-3d13-91e3-0470cb2d1c2f | -10.02613 | -48.03244 | 2026-10-09 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31e7c155-dc28-3135-87ba-aa1be842c4b5 | -6.96015 | -45.27137 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3ae4210-6943-3df1-81ce-3b5c50cee21e | -3.59859 | -61.63816 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abe98f95-2be5-3852-a618-8f4811cf08c5 | -2.97962 | -54.11179 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a25e3f-8059-37bf-b3b6-cc81847e8a85 | -9.8499 | -49.03925 | 2026-10-09 05:04:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 020fe95d-62f9-3cf9-976a-f2189e819ad7 | -5.89947 | -52.04673 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26920fee-d155-3407-8e65-f8ab8e5bf14a | -2.62247 | -56.48343 | 2026-10-09 05:04:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 382fe91c-28a0-3099-ba5b-f4dee527f173 | -3.609 | -54.59179 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1164e2a-62ae-3d40-a37f-cb7e26d96e05 | -3.10466 | -54.27708 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e25dbfd-e1c6-3658-8870-7d1d86e40c85 | -7.51343 | -47.3347 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28611ec1-067a-302e-b3ca-50a7ae917a00 | -11.05225 | -44.04554 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e57667d2-163e-37b7-9635-50932915e377 | -3.8666 | -55.99858 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33cefa9a-4259-328a-bd0e-6c65a7e30c65 | -3.09002 | -53.94021 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1abcce90-66bb-3e77-b2cd-60b0d5e54a24 | -11.18306 | -45.32157 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdee96d9-7847-30de-a19e-b1b54e4db4c4 | -3.09983 | -53.94565 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ae3e283-4de2-3be8-b849-e43df84de037 | -6.13254 | -55.68244 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70ef66ce-86d7-3321-9ee4-b725ed784129 | -3.30094 | -53.71091 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d75223c3-800b-3df0-91f3-2a93c0f5d8ca | -8.33518 | -50.88231 | 2026-10-09 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 888fb011-4404-35a1-8557-74b9588cb4a6 | -6.10061 | -55.6945 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59374b25-63dc-3db0-b864-191ac4bbcf09 | -6.01174 | -40.9687 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 461e6bd7-b510-3846-9925-185522e2b4af | -11.86386 | -43.56153 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d31179b2-9b86-31d4-88c6-59c3d21fe7bd | -3.57066 | -54.69248 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d6a6ddf8-097e-3f11-b14a-b15e3c89f2bd | -2.92464 | -54.11882 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a9d37ac-d10a-31dc-8cb8-24142f1ef284 | -2.86981 | -54.16594 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04345d4b-6498-3de7-97ba-e068e6fe0b0c | -6.85666 | -52.83592 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beabf8eb-d5f7-3e86-a7f9-3c6a184e120f | -3.29293 | -54.00218 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96fe4ae4-0699-3e69-b16b-b984ba4ad0d0 | -3.08758 | -53.95542 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4186b070-4d5e-3fff-9ee0-ecadf8d5f63e | -3.58964 | -54.57651 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d239210-c69c-3db2-8e8b-7479cb8c199c | -7.51397 | -47.33094 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fe8f466-5d0c-35d0-b1d7-2da4eb662647 | -9.64021 | -47.72411 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8727b132-2054-3406-8f6c-c7bbb8337270 | -4.0491 | -46.90439 | 2026-10-09 05:04:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47eff9dc-d539-391c-b346-8adae641d52a | -9.01842 | -44.37563 | 2026-10-09 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd8c7485-f3a5-30bb-941c-fb4316c88603 | -3.20708 | -58.84557 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a17271a-93a2-3dab-9bee-349f6c75d3fe | -10.86935 | -45.53713 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 954b27a2-5eec-3629-bac4-292dbafa11e8 | -3.06652 | -54.1762 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f94a4b-6727-39bb-a957-4c0314bbed39 | -4.80535 | -54.66999 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70ab9696-a9fe-3828-a680-61d75842ac29 | -3.45671 | -50.58599 | 2026-10-09 05:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5f84e431-e002-3b45-abc1-4b8a0b23fdb7 | -6.92161 | -44.55967 | 2026-10-09 05:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 964e8456-8873-3948-a981-6fb3325b0415 | -6.13213 | -53.50727 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebcbc302-9131-3812-a4a8-456036b106ca | -11.0033 | -45.41004 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7197f943-0d28-3406-98e4-d4e2a307409d | -6.86911 | -46.4841 | 2026-10-09 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43a8fcf3-9620-39e4-a77b-9dcedf70ea27 | -6.11306 | -55.70959 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 507e5fd8-1be0-3cf0-9313-71994f9c2a75 | -9.69543 | -58.08631 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8be62535-2281-3f8b-b5a6-627f3b3bdd3e | -3.07457 | -54.26124 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e956075a-da0a-3cc7-9b25-f68010b6e622 | -3.00422 | -54.09502 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9af0dc6-2bc5-3c8a-90eb-6e79c2d0ceb4 | -4.63967 | -50.96164 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3ad321c-1845-309c-ae6c-10ddb34ac10e | -3.00987 | -54.06043 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31f2ef0-22d6-3489-9525-d7a9105b751f | -7.18198 | -52.61688 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4948f9f-2499-3ed6-94e8-0b4c00eb6267 | -2.84312 | -57.47242 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbfd198f-ea32-3c62-8f07-b43ac769eacf | -3.00202 | -54.08374 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233185c7-1dd8-3bdb-b6eb-fa80d855dcf4 | -3.40516 | -59.59744 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0820ab7-59ac-33f9-9a97-a0d851345d6c | -5.70239 | -53.48607 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a168044-3cfa-3453-b73f-38d0a27cece5 | -3.59318 | -54.5771 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59426df6-bed2-3453-a83b-8ed11aff6086 | -6.24427 | -52.85233 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aa16a98-2091-3f53-b8cd-0e1aa373868e | -6.2681 | -55.26101 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57799d21-963e-3e33-9941-dee8be9ad855 | -3.28477 | -54.07516 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1a8b6e-5414-3a71-a414-03ea87977938 | -11.22322 | -45.31636 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8fbe5f1-bb26-3ada-9460-cbdcff42bdfe | -3.57132 | -54.68845 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1750dda0-5f0c-32f5-b879-76236ac40b62 | -3.11151 | -54.19062 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2036908-5a0d-3f3b-9493-111e557508ef | -2.49172 | -58.08141 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aab68f0c-84cf-37e9-9a37-5fa4ecce10f3 | -5.75591 | -50.22773 | 2026-10-09 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f61f8663-7110-3199-9ee7-a5c1caea30b9 | -3.17413 | -58.62423 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cab7e6f7-73a0-342b-8129-e657350e4992 | -7.50927 | -47.33411 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 684000ab-68b0-3557-8bf4-5ea45544ac4c | -4.37042 | -55.32374 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4182476d-6e6e-3eab-8173-102c3c4e0175 | -5.88451 | -57.75033 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd17afd8-6105-3786-9456-f6ca58091834 | -4.95215 | -49.4162 | 2026-10-09 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a7107ec-7c60-318e-b6dc-ec1d4cf4f958 | -2.8814 | -54.18369 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ba043be-6ab1-37d1-ac7b-6aecb9062e21 | -4.12077 | -59.88832 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11a5644d-a515-30f2-b272-0f3580882e14 | -6.10221 | -55.72968 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73437459-23f1-3706-83b1-02bc6429ef28 | -5.37839 | -46.18563 | 2026-10-09 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14ac4b04-29d7-3751-8b15-1d2cc23adddf | -9.93734 | -43.55739 | 2026-10-09 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0de6f5b3-ddaa-3a62-808a-c1c25877b727 | -10.87909 | -44.79877 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cb8c48cd-155e-3119-9f7e-169286ddb233 | -5.61604 | -44.84233 | 2026-10-09 05:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba8ed257-1cc4-3cbf-970d-ae67f93e33c4 | -3.0941 | -53.93695 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9100e21e-373b-3db6-9498-c5b4035a845a | -3.10177 | -54.27263 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37dc5a5a-463a-32f3-93a9-b88013f55973 | -3.30155 | -53.70717 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 613820dd-13f0-369c-9719-da373ecec9ce | -5.75768 | -43.85251 | 2026-10-09 05:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c837b2f8-6e7e-3873-bad5-3afe0c8f437e | -3.46914 | -59.26408 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a687b3a8-8548-39b6-9c06-5d094e163f80 | -8.32741 | -49.12556 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f96e1e8-f633-3ab3-8f68-14b0c4b828b0 | -8.06106 | -45.63414 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ec55664-0382-32a8-a5f8-da3793a79735 | -6.48927 | -62.85389 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2e12789-8a94-3f3b-bc3b-95f411b2e3e3 | -5.99395 | -55.36748 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f4d6d7e-9dcb-35b1-8b33-24326d0251b1 | -5.10455 | -46.21687 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c56cda3-88b0-3835-8922-4d783d631fd3 | -3.01023 | -54.07716 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e718a92-6b65-347f-9038-34b1b342cd77 | -4.6214 | -49.20881 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8915b192-641f-33d2-ae9d-31c270346e45 | -3.01049 | -54.05659 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a79396-9f51-3bac-bc40-87310dcd086b | -4.51905 | -54.89735 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c11bcbe9-dcc7-36aa-8c33-0496d27d1ac2 | -3.07436 | -54.28527 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91906beb-1444-31b8-acd1-1274a30572da | -4.17356 | -55.50646 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4addaba9-8281-3554-b4f1-0eec5dcc4475 | -3.10164 | -54.18494 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82c173bc-1c61-364f-98ba-00bb6e494a76 | -3.03583 | -54.14355 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 706979c2-6ff5-3c66-8212-5312dfcb4bef | -3.74583 | -59.47732 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README160.md)
