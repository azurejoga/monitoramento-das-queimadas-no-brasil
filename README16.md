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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd4a765-9beb-3aa0-b401-e077d12db4fa | -2.41024 | -47.70895 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b1e951f-b2c4-377e-a8b3-7da9dcc695e3 | -6.08695 | -44.01134 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4ebdd3b-1a6f-32c9-a201-1b8c0174656f | -3.4872 | -43.34392 | 2024-12-18 04:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e7d975-26ee-3f0e-b383-e4c0606452dc | -4.00646 | -46.93467 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23122c4a-fdd5-3b93-a8f1-36e053587e32 | -6.08592 | -43.97139 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd7d2ac-581d-3e47-8119-15c3057528f1 | -3.14962 | -44.45613 | 2024-12-18 04:25:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d46fcfd-71eb-32db-a13d-9203c3e658eb | -3.77789 | -43.00198 | 2024-12-18 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9257e226-a59e-3ff6-94ec-3d600be68469 | -6.44059 | -40.62191 | 2024-12-18 04:25:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30ef5810-02e2-3d34-8ed9-8bbb737e00ce | -3.14347 | -44.47332 | 2024-12-18 04:25:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c844d97e-8657-3ebc-88d9-b1c54f2c9a2d | -2.96943 | -39.84277 | 2024-12-18 04:25:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc2fc29f-32d3-3758-a5f8-c2398c435703 | -5.94366 | -43.76916 | 2024-12-18 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb6f410-68db-35cf-b6ea-2227e120bdfd | -6.08754 | -44.00751 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7092d043-fd3c-33ff-a7ea-e67ccaaeb597 | -4.39076 | -44.19886 | 2024-12-18 04:25:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd9073d-5492-3087-82c5-59d255b9835a | -5.94283 | -48.06554 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f31611-a812-3c9f-b3d4-5b3a81feb09e | -1.57333 | -46.04246 | 2024-12-18 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a767b7b6-64d5-3be7-9369-862b80e6e52f | -4.00983 | -46.93518 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7de6141b-b601-3e6e-8e6c-750d22c9f0e5 | -1.6992 | -45.78076 | 2024-12-18 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b28c3bc-1729-3eb4-993d-51cdead7fccc | -5.71045 | -41.41175 | 2024-12-18 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21e7dceb-958b-3cae-9893-e0ae05b4e2aa | -3.92334 | -48.08815 | 2024-12-18 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f8b06c6a-aa21-3fb2-9a4b-f352b9702a3e | -4.03113 | -46.90952 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b88c34a-cf0a-3d1d-b323-386df1163cf9 | -5.29799 | -44.94251 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ee0b8c1-ee66-322f-8cf2-7902e2515d38 | -3.90517 | -46.67624 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7ce079-042a-3350-bd12-4ba825e29a27 | -6.44154 | -40.62344 | 2024-12-18 04:25:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12c4d14d-7ed7-3145-926d-f720707c22a9 | -1.99306 | -46.59496 | 2024-12-18 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 44ed57f0-5aed-32cc-8505-c5c1913e8c70 | -5.1349 | -46.15757 | 2024-12-18 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fe825d1-f7e8-31d6-8319-7f3dbf195c67 | -6.1913 | -44.42414 | 2024-12-18 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20f2c56f-fbf7-3a10-9093-a00a957cb35e | -3.79423 | -46.71297 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 529bbed0-8cb1-389d-90e2-e9668e300a6d | -5.94 | -48.06128 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4890a2d2-ab97-3cc2-b142-0604b6b35aac | -2.23777 | -53.74546 | 2024-12-18 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7045bd1b-508a-3232-a8a5-39be40c429fb | -4.15057 | -43.57112 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fd42a35-aa33-3086-932a-9fa1738e5bbe | -6.63207 | -47.33803 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93e9c207-e9be-3b3c-a250-4bc350529851 | -2.92648 | -45.25167 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50229d00-eb92-324c-a44f-20d3aff04f6e | -5.94744 | -48.05867 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b94fd9e-998f-37ef-badd-6522bededce7 | -3.14011 | -44.47281 | 2024-12-18 04:25:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0309e4fb-94fc-3f8a-a4da-cabf6f2f0ac0 | -6.06024 | -44.04644 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b33bbceb-54c9-3b99-a286-3b8f3b5d74d4 | -3.8015 | -46.71045 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385cc182-e0d3-361a-ad7d-a4f280396c12 | -6.08242 | -43.97089 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f934f72-3144-36bb-bad7-aca4a74d0aba | -4.03837 | -47.01614 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f33412e9-7e0b-38e3-98ea-d800d591bb6c | -7.1982 | -44.9255 | 2024-12-18 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 819b85b3-da32-3db0-8852-069aee680131 | -3.90573 | -46.67273 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f93cb8c-54e2-33b1-88ce-e94f65d27442 | -6.63542 | -47.33857 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a07f1c6-ed76-3203-9bd4-0c688c2ccd57 | -4.03218 | -47.03343 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9464a3aa-4144-3275-9925-ceacc48de4fc | -3.86552 | -47.0327 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ecbfe8-4173-3d1c-9620-7fe6eb991d1a | -4.68191 | -45.31211 | 2024-12-18 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e52b36c7-1005-36e5-a4f0-6279723aa901 | -4.0603 | -47.10369 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f2cb41-e9cb-3cfb-b218-943d95184a16 | -5.29854 | -44.93896 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20192377-0da5-3211-9ee3-0d43f675c8e4 | -4.00841 | -43.16386 | 2024-12-18 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 686c663d-c2a0-3b79-b589-afc0b3a1ba73 | -2.69638 | -51.64569 | 2024-12-18 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f3593b4-21b9-35e3-b166-ac709d090238 | -3.86158 | -47.03574 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec219a6-7370-3fb3-b155-5f9350b2d227 | -4.04341 | -47.02793 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09ab0cd2-98df-3039-9e00-0bbcca1d2a58 | -6.19532 | -44.42095 | 2024-12-18 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5657bd95-1f36-35d7-824e-a06f8a6c5d89 | -4.12389 | -43.55924 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d94970a-c527-370f-8176-056c530ed7c6 | -4.93214 | -45.09607 | 2024-12-18 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bee2c73-3d0e-3b6f-81fe-8284ded6220e | -2.13892 | -46.46545 | 2024-12-18 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edb3c83e-7f14-35f3-a20e-2d5e3a3eadbb | -5.89391 | -42.3299 | 2024-12-18 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c37ab571-fba0-3c58-9f95-89fbbba8b65a | -4.11692 | -43.55816 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 939a3b14-4e00-3fea-96cd-bcc5b1b8aeb8 | -4.04566 | -47.01371 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81eb80dd-3512-391d-986e-e84288be03c1 | -3.90852 | -46.65519 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8d08d74-a7c3-3b08-8d17-d528bcd5b6cf | -3.50575 | -45.37397 | 2024-12-18 04:25:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a837d8e-a8ab-392b-a63f-5e11bd9e685b | -4.04005 | -47.02737 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb2c79f5-4b2b-36ed-9b84-2ef48a5c0f30 | -8.87674 | -41.10476 | 2024-12-18 04:25:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 624699b3-28ee-3963-a53a-10088da6b27b | -3.16272 | -45.98232 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 090dd188-7ac3-347d-8fa2-ba19b2e2b56c | -6.2149 | -46.21749 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb1a6b1-1c42-309f-9eb1-0208eaac3c11 | -4.1227 | -43.56691 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f3ac73c-0416-347f-bf68-0cc6decd3db6 | -6.98554 | -43.566 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc714d71-58f5-3321-a1be-7f9c9fff5751 | -4.39113 | -44.199 | 2024-12-18 04:25:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06d02aaa-7fe3-3622-b730-fcaf0ec54f44 | -1.61569 | -45.83873 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97edd132-e7e5-3311-83e4-2353a2c9be10 | -4.01095 | -46.92813 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee37d75c-27f0-3a3a-9194-63d230737ef1 | -4.38428 | -42.14349 | 2024-12-18 04:25:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80f7a432-1f4b-3588-8c1f-dfdf4575d242 | -1.62186 | -45.86458 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23408e7-599b-35b0-a4c0-166bc749abd1 | -5.93539 | -48.06818 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b921b1f-9498-385e-b009-318997ce94eb | -2.55192 | -45.80109 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e886b5d7-4f6d-37be-a798-a5ab539ed2ad | -5.94717 | -43.76971 | 2024-12-18 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53f5733f-0ff1-33af-9213-2ed6400a389f | -3.24065 | -46.87698 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 83f2b081-9dec-3a30-990f-20d76d60440c | -2.46968 | -47.08854 | 2024-12-18 04:25:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 428d7258-23c5-371d-8cc8-6117a8a03093 | -6.98256 | -43.56136 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5439b0d-959f-3217-8b7d-abf0617ec668 | -3.90797 | -46.6587 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df3434d4-834a-3598-8ea2-301c4045a805 | -6.08184 | -43.97475 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 260d66a0-54d5-35b3-aaa9-d7cc357656aa | -2.09137 | -45.28708 | 2024-12-18 04:25:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0422976-b543-31a2-9208-357e76d519f6 | -7.15364 | -46.69662 | 2024-12-18 04:25:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de912223-0186-394b-a5ad-8ca4a85a9ce7 | -9.11285 | -49.46794 | 2024-12-18 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cd35ef9-5cef-3db6-a5fc-5f5980d0d901 | -15.87693 | -53.27169 | 2024-12-18 04:27:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83b08d1e-8f52-3b95-8ed6-ca3819548417 | -9.37247 | -47.72224 | 2024-12-18 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 218999ae-86cf-34a3-9cad-db1f78006ee5 | -11.86246 | -43.82721 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01c93a8b-1e43-3c69-bc25-ff1d30acecd8 | -15.45474 | -51.81278 | 2024-12-18 04:27:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84415bcb-d13f-373e-af6d-dc44f20f25ab | -12.33457 | -43.676 | 2024-12-18 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a82230e3-545c-3298-a726-f0862b2d5d46 | -14.812 | -42.84655 | 2024-12-18 04:27:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39aa34a-65f3-391e-86e7-266f82f4a532 | -11.8618 | -43.83173 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ae7b56b-68e1-3140-8f41-33db70ee20be | -12.41245 | -43.80382 | 2024-12-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffe101d5-c68a-37da-b919-8f2929e16f8b | -11.32208 | -44.49615 | 2024-12-18 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8941d1b-c382-3dfa-abba-3191d2895699 | -12.90482 | -55.04662 | 2024-12-18 04:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a6fe83-0bca-3120-896b-066b7c15461f | -9.36913 | -47.7217 | 2024-12-18 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 621c44f1-0873-355d-aaab-3c6dc5b9bb4f | -11.85872 | -43.82665 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf0caf41-4f33-3983-ad56-8846606d6e0a | -11.86554 | -43.83229 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b001ef1-65db-36a2-961c-473f0b3c773c | -12.23048 | -54.31221 | 2024-12-18 04:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b05dc598-c5b4-389d-a06e-c7aa7146fd99 | -12.33837 | -43.67656 | 2024-12-18 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c0364c91-a621-3e02-9799-52877faefe31 | -11.87012 | -43.72131 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fab84def-3d4b-3821-ae07-59d19b402fd3 | -15.45549 | -51.80844 | 2024-12-18 04:27:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 024777ab-4c02-3848-825b-44567043c039 | -11.85497 | -43.82609 | 2024-12-18 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c848ef21-0ded-3c8b-8f64-52fb00b128ae | -12.34217 | -43.6771 | 2024-12-18 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
