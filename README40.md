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
| b16fe92e-dbb3-3c14-bcba-3398eb7f9f40 | -7.53602 | -44.93637 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9a3da4e-7739-3c34-ab08-f6577b3ad0b5 | -8.29035 | -47.22832 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c18e7cc-3a85-318d-99f7-99bd1eca29e2 | -2.98837 | -49.30408 | 2025-08-26 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c2b8d1-05aa-360e-a004-ced2d537acf8 | -4.95653 | -55.81994 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 995a4969-b734-3fe6-843b-111553ffb9e5 | -5.87515 | -43.4054 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3263a27d-d490-351c-93cd-9150c5f537f6 | -9.84495 | -46.45459 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c33ac26-9c8b-3e2a-a4cf-4ddebda81996 | -6.19803 | -44.15181 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4236a954-9a0f-3d2b-add0-e9c9438fda31 | -2.92513 | -53.69706 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12d86a2e-c41e-3e64-be89-22a4a78ed893 | -10.81791 | -48.31863 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8503cc-2fb4-3318-8210-cba069b62254 | -5.47149 | -42.6097 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| edb8c1d5-b970-3ca3-ba76-fd7c12f934c7 | -6.29495 | -43.77373 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 057cf734-2cac-3303-a2fd-824509defc30 | -6.02976 | -43.9968 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9277cc5-4637-3ff3-8c77-7e52e5adc5a5 | -4.95912 | -55.82367 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d8055ea7-138d-3081-b119-21d3c4a70123 | -10.78 | -46.38301 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efbd2cd2-aff9-30bd-b906-5e62406ec6aa | -9.0597 | -49.55658 | 2025-08-26 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db582eb8-72ab-3d1f-9983-eac5afbcfd8c | -5.55322 | -45.5739 | 2025-08-26 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2097e69e-7169-30cb-9022-d05ed1109d8f | -3.9825 | -51.06629 | 2025-08-26 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65718b24-2d5e-37d5-b2a9-459307f80e33 | -4.95827 | -55.80987 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 255695b1-110e-3fc7-a709-7da61341fe4d | -6.04031 | -44.22666 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68e8526d-0e7c-30f3-8aaf-46b37f368a6c | -7.53018 | -50.53622 | 2025-08-26 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b77f3932-ae87-3b27-89d3-f424d523d7a3 | -6.76557 | -43.82861 | 2025-08-26 04:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eacbccd9-9923-3144-8ac1-4366d7f6477f | -7.77316 | -44.95296 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f123fc-a2cf-3f1d-9163-44afb68120a0 | -10.8108 | -48.3175 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e490645d-9df9-3668-81ca-5262dc1ca818 | -8.32543 | -47.25395 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 523ec0ed-a9d3-378d-be31-f26a0f9784ea | -9.8102 | -43.94793 | 2025-08-26 04:21:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffe51db2-eed8-3d5a-92c2-306ee3c41c94 | -6.69989 | -48.37749 | 2025-08-26 04:21:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4efdd82e-e20a-3652-9418-b7dcec50ea3f | -8.29348 | -46.32978 | 2025-08-26 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea914c5-5b9d-3b48-99b8-6d96baf86e53 | -7.33075 | -46.09862 | 2025-08-26 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c7ac5ef-832d-37b2-bbb5-847a4c5bbd0b | -9.57754 | -48.63102 | 2025-08-26 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09185e8-e29e-3c5d-9e3e-761f9db38a87 | -9.85108 | -46.45931 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cdba8be-df34-3403-a650-c9c0837dd86f | -3.98701 | -47.8843 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 78f86626-9589-302c-b0ca-80af1c693447 | -8.48203 | -43.67048 | 2025-08-26 04:21:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 260cc620-5bf0-3163-8d5f-be8229f468f2 | -9.56546 | -55.37823 | 2025-08-26 04:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05c65faf-5b70-3976-a43e-8cc97eba7a0e | -9.32451 | -40.21749 | 2025-08-26 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b03a13c4-e12a-3d86-ad29-62887337cdaf | -11.14686 | -44.78572 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e1cb0cd-4625-31a1-9753-07a2d167c536 | -11.15292 | -44.74642 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56408577-7825-3cea-b7d9-c7638095679e | -10.77666 | -46.38245 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56ce19ea-a10c-342e-8cc4-4acb5a034255 | -11.14736 | -44.7602 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3df5964f-8651-3794-80f1-88564b827e75 | -11.25907 | -44.98198 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 824bb2a8-d3e8-3c1f-823d-dfda59910c36 | -8.12733 | -47.29431 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 440a1e5b-1a2c-34fa-91b9-fb6e52261781 | -5.37932 | -45.17685 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a522b738-08db-3c8f-a90c-e9312779f687 | -9.40349 | -48.24442 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cbf0ce3-1162-35de-ae5b-86c8d9027ffd | -9.16743 | -40.60194 | 2025-08-26 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f0899568-f1bb-31c5-bf7a-bbb038a86d32 | -7.89615 | -41.90972 | 2025-08-26 04:21:00 | NPP-375D | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10658f36-6a37-3ea4-82e0-6eb1f1e4c5fd | -9.69323 | -48.33789 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51913d90-0c23-3035-bfbc-69fb37b51a20 | -7.59067 | -43.95713 | 2025-08-26 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9995f9ca-0b8c-386b-bdaf-36773e935abe | -6.42688 | -44.56483 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4ce54d7-b90c-36eb-8d7b-c63c147fef09 | -3.20473 | -49.11972 | 2025-08-26 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eccdfc95-229a-32b4-a70d-8358e34e2cdb | -5.70919 | -45.53279 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c177e213-82d6-33be-aa8b-268e0f926495 | -8.06993 | -49.66882 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 405ad69e-32b4-36d1-89f8-68dd29c4c072 | -6.87444 | -45.65242 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a7749a-5f9c-3477-b3fd-250c6bc32295 | -6.65413 | -53.18363 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52c42e55-0258-3f1a-8e4a-9e332a065658 | -11.15631 | -44.76895 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5caee14d-32e6-3bc9-a817-8476c4f707c9 | -8.23782 | -45.11924 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a867eca9-910c-30c8-9364-ab3592faf8c7 | -6.3849 | -45.59618 | 2025-08-26 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86069868-b3de-3afb-9774-44504e12b95d | -5.90649 | -43.42477 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f05180-20f0-3516-a570-a992a443fd6b | -6.52515 | -44.43817 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdaeb2b8-23d8-325c-9818-802aeeded1e7 | -4.67888 | -41.02893 | 2025-08-26 04:21:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53bcf574-edc2-3f66-83b1-27cf1016b263 | -9.26216 | -43.4066 | 2025-08-26 04:21:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8289657-ef4f-3cc9-b90a-2502e90d466a | -10.60712 | -44.78037 | 2025-08-26 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acfa15eb-b450-3a7a-8421-a7e2506d386f | -7.53826 | -44.94025 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e405ed7-5002-3bd1-865c-80345bac8a9b | -7.6006 | -45.2283 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a5d4e31-ca04-3df5-80f2-c58f180e4ca8 | -6.88331 | -45.64991 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9ed6a09-c59e-3ef4-bd0c-d9f97173ef69 | -10.81149 | -48.31341 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d95dc03-1b19-3ff7-b25d-7b272fcfb6bc | -7.59553 | -45.22412 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4370397d-6787-3b95-a761-342a62623a23 | -5.74591 | -45.37864 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e63df6-1ae9-3b2f-8ad2-29d13c815e9b | -8.13037 | -47.12112 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 455c8733-217d-3728-b541-f5df864acbd1 | -7.74883 | -43.92373 | 2025-08-26 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e0ffb77-8aaa-3c84-af0a-5f99a395e010 | -6.28727 | -43.84438 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d402a050-45c5-3bee-b784-b342609ea35b | -6.9936 | -44.14819 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d8f49a5-773b-3d7e-a752-2d30312ae19b | -6.81216 | -44.996 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f077c25c-b926-3484-bd2c-f8bde4b0378b | -2.9314 | -53.69425 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b1b075a-0b62-3fee-83d5-666911901278 | -7.57562 | -47.48881 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d9eabff-19cc-3819-b527-54e8df781862 | -8.16354 | -45.05381 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09e7c169-8692-37e2-b2e4-0e3278e0b565 | -6.27416 | -43.68788 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d76507b4-b585-33b1-b291-189f585e4dc0 | -7.30849 | -43.66263 | 2025-08-26 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e90b4dbd-da92-33d1-986b-b52d62f3a612 | -7.15494 | -44.17329 | 2025-08-26 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba7cbc18-2f0f-3b7a-ab0c-00139bcf5ee4 | -4.69099 | -43.09942 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f22bd031-28bd-3345-b34c-56823aed13f8 | -9.25947 | -56.90763 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aabc37d-9732-337e-9455-f6ddf362f011 | -9.27197 | -56.9098 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15b66dd5-8459-3fcd-a4ce-022dfe530ff6 | -6.02921 | -44.00029 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3603c0f9-8cc2-3b75-92ef-e5d0baff05d4 | -5.55442 | -45.20074 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3768709e-f781-3abd-a9ce-80f6357be2c0 | -8.12975 | -47.12495 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e266bc80-f9b6-33ef-b590-bf5bc6b3b71a | -5.89694 | -43.39791 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b8a792-9a39-3296-a0bf-7adc04143147 | -7.45625 | -43.84913 | 2025-08-26 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f284431-5e67-39e0-9af7-1c5953b886b7 | -7.48074 | -45.02737 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb09c59-1183-3b28-a4c0-871ceb8579b2 | -5.55716 | -45.57085 | 2025-08-26 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d7156e8-07cf-320f-84b6-b6669fcb8a75 | -6.80939 | -44.992 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d837c6c2-65c1-3eab-bda2-4056f7be9f86 | -5.87472 | -42.41113 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bb4e62f-6220-359d-a1c3-a790a22f9422 | -7.82447 | -45.22506 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55974602-a14f-3a36-8905-dcd35d223ac5 | -10.4342 | -47.1751 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b46a612-9b20-3b05-8d3f-1406a35002f0 | -7.47297 | -45.01184 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a5e2dee-31b4-3378-bcf5-d61c664c7860 | -11.15851 | -44.75463 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 5f1c9a92-db4e-33e5-b01f-a796787d8674 | -3.98325 | -47.88364 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5f25a31a-d3ad-3fdd-a287-95b29a738351 | -5.49226 | -42.15348 | 2025-08-26 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30d9ff07-e3b5-3b1c-9b4f-e33eae32e731 | -7.65297 | -42.66999 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae31398d-87b9-37f8-a60d-9b661a219017 | -8.24611 | -45.10985 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 137f9640-e152-3587-932b-064bdb975bf8 | -6.49629 | -44.68248 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5865d3b-2d4d-30a5-ba9b-62279eb06e3a | -6.03666 | -42.7026 | 2025-08-26 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa9d0df1-db97-33f9-adc2-79a60093855b | -11.06185 | -44.59229 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README41.md)
