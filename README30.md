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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74799e3f-628f-3566-b73f-119209c8b5db | -9.46901 | -51.58597 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25eb1a1d-41a1-3c95-893c-3633ddf71034 | -12.90281 | -45.85204 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 373fd2ae-0a6a-3f13-94e9-6f9051bbc33a | -7.10734 | -42.21033 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 868554fe-cca1-3853-99f4-34474eeca65c | -12.38402 | -48.181 | 2026-08-30 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3ddb917-6e61-31b5-b907-ed3274734d8c | -11.79636 | -51.04968 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fce10e70-befc-3be0-a9dc-0aea35cf72ae | -9.42268 | -51.58886 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7ec56fe-6f9f-3533-a0a1-76bb7f5e953d | -7.09331 | -42.23136 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ae77f9d-d1da-356f-8852-07056ef66ac8 | -11.65895 | -46.75671 | 2026-08-30 04:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b27896f-815d-3425-850a-4bf1316bbe0f | -9.66332 | -55.11361 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe8ff8d7-dd33-3127-81c6-6279a370714c | -11.79425 | -51.06057 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 462fa623-ed79-379c-af4d-b0dd52f9571f | -10.79211 | -45.32172 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 76591749-f76d-3b3b-9019-2f6508a7d5f1 | -12.77733 | -46.4571 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a74f991-fa9a-3b05-ab25-d323b0f72076 | -7.2541 | -45.39011 | 2026-08-30 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aba37b23-058e-3d64-8313-191441c447f2 | -10.74755 | -50.8446 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b144c065-b2b1-398c-9ab6-ffa7ab0bcec0 | -11.49752 | -50.27625 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4659353-c876-3007-bd60-5a73d811e1f3 | -11.02507 | -49.68882 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a1d32f5-0d60-38a5-927a-6c95cb600af5 | -11.24512 | -54.00887 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc7a6bc2-d615-3e05-b4af-820bae088d22 | -7.04529 | -42.20024 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f569173-6270-3bef-a0d2-1beeafe60f5a | -12.43446 | -42.88766 | 2026-08-30 04:14:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d743d2ce-05cc-3c71-8679-fd5c964374db | -11.2439 | -54.01472 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bf87e9ef-ed05-38e0-baef-8c6848d8aae6 | -13.35818 | -46.92009 | 2026-08-30 04:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e2559f6-b34f-3954-96d3-c6671b519628 | -9.20158 | -51.55885 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25a23e31-c781-30f5-9f84-1afb5be3b107 | -10.81816 | -45.33146 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f07d3e8e-03ea-3f9c-b88d-9aecbecb95e1 | -7.10754 | -42.18723 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a094fdf5-171c-3394-b523-0d2c6f899582 | -11.20618 | -45.07243 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbf63c16-aef4-34d4-94fd-2f8c50ee687e | -9.21793 | -46.06681 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a963ab93-e5bd-3052-9833-f46f01725f47 | -11.82587 | -51.04443 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 12b13259-b7aa-3f8c-a346-c5afc5dea30b | -11.29987 | -54.04517 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead59ab9-f508-3f94-89ed-00cba6d3dc06 | -11.36303 | -45.17213 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7c7ec789-9aaa-3533-9517-27405af8fa3e | -11.02451 | -49.69186 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a8bed84-3327-3529-bf5b-1ac66fb4b6d0 | -7.0993 | -42.83936 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 73126d0f-5217-3f8e-9d0b-65ce39463758 | -9.21729 | -46.07047 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdf9907e-3a09-3578-8f40-11122172a615 | -8.61226 | -54.79166 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc194bea-12b0-34b5-89ce-87321827b0a2 | -11.48718 | -45.05881 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05a809b4-502f-306a-b96e-512b7bfe4b89 | -7.60766 | -45.83986 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8936ad76-ce6a-3f53-acaa-0077cee22563 | -11.62905 | -54.59079 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0922809a-d497-35b7-9670-f05727dd2e01 | -7.1012 | -45.76984 | 2026-08-30 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cbef4ec-6044-3f6e-9ba0-44d1dbe5e9f9 | -7.30966 | -43.01145 | 2026-08-30 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26866955-8738-33ea-9a10-f294c8466a3a | -6.95833 | -44.23262 | 2026-08-30 04:14:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 723005ca-875e-30c3-aa42-ef5577bfd6b9 | -11.21604 | -45.08207 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 434acb11-a12a-3b9f-8848-93fa2233cb8c | -12.89931 | -45.87825 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa772cfd-4e60-38b1-99f6-9849fb322d10 | -11.16516 | -51.31865 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c0de554-508b-362f-ada9-e34b4e8e4c33 | -9.76038 | -48.16698 | 2026-08-30 04:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b333de4-ffb3-321f-8714-daf0b2b661bd | -11.2408 | -45.09604 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddc66f75-75d3-34bb-9cc4-45d6ba6e20d5 | -12.78032 | -46.46355 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8309f57-af7b-308d-aa1a-0edcb9e8de4e | -7.1305 | -42.75909 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2988cdc9-8bfa-3ea0-8e54-313ae7f9feef | -11.02169 | -49.69213 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba738d56-0119-3dc6-a3c7-700ba333b622 | -11.53609 | -45.49534 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83ab378a-cf63-30e8-826e-7c898f441934 | -11.35117 | -45.15056 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1f900b7-ac98-363e-818f-081b00321f18 | -7.21742 | -42.75611 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ef808c6-3e09-3956-843b-2303e2208b4c | -10.7348 | -54.04673 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 443913b0-aa5f-3815-bb0e-c7a703761900 | -10.13013 | -45.70166 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 008fa4f4-7b34-3956-bbf0-1da6d1b06f7e | -12.9045 | -45.8493 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 98082c25-3667-3bc4-9cd0-5db8a2389c42 | -10.35717 | -49.97863 | 2026-08-30 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4283f14-1010-360b-a3d7-f0ac1ca8d87c | -9.78371 | -46.41877 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2a827a-8471-337c-8e14-64097bbcc8ef | -9.6649 | -55.10596 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| efe046a3-84ba-3e5a-b0ef-de90a094f0eb | -13.93622 | -43.99574 | 2026-08-30 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c2f9cc9-75a7-346f-ba38-0f0848175f01 | -9.20076 | -51.56308 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3f83558-925d-3242-8920-bdd1acd6459c | -12.8028 | -46.45876 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2410b9c7-9a39-3f37-915f-1983e5820992 | -7.94607 | -44.26942 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f20021eb-1b3e-3b4b-9af0-adf7991f327c | -6.49798 | -53.25927 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d6b7268-465e-3f66-802e-5b7084ffefea | -7.21033 | -44.01986 | 2026-08-30 04:14:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f90627c-bfb2-31bf-8631-6a810601c207 | -10.99111 | -50.52235 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e6719d2-fc7a-3091-9d03-a11647d41f91 | -7.60065 | -42.99495 | 2026-08-30 04:14:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2abef30f-a616-373e-ba2b-377f6177d9f1 | -8.13939 | -45.47065 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 346e378b-0ecc-3e9b-b029-b42eaf78daac | -7.37726 | -45.08168 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ced4303-de1a-3c42-bbf0-53055a4a9a40 | -7.10186 | -45.76607 | 2026-08-30 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6fbd524-624c-3e83-8a09-a86efb10c5a9 | -8.25309 | -46.50389 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e819e98-437e-346f-8bb5-d728565cc228 | -11.68712 | -47.61877 | 2026-08-30 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8d8c3c3-7cd0-3bd4-9859-f45260bcc941 | -11.35706 | -45.16153 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cdd4346-33b8-3009-817f-3c964ddf9196 | -7.16437 | -48.21308 | 2026-08-30 04:14:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 166d90b7-4d55-30b7-a4b2-bad827c707e6 | -11.83551 | -46.76486 | 2026-08-30 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3f885be-70e5-3256-aabd-3be4538833b7 | -7.13465 | -42.75576 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a95c08df-3409-3ba0-a6a6-e93f34e265e6 | -7.16535 | -48.20746 | 2026-08-30 04:14:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 249167ba-e1bc-3afe-b858-f52166ba9087 | -9.31696 | -40.22079 | 2026-08-30 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d600bae7-0992-395b-9dbc-d53a2cb6ecd5 | -12.78526 | -46.45889 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7740f5b-ba0a-3560-8dcf-7e8164bd9193 | -7.61248 | -44.84943 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7687678-7745-32a1-aa07-97f004edf4fd | -10.74826 | -50.84093 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f0f08e9-bc1f-3588-adb2-0613f16c17ca | -11.35329 | -45.16085 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4619b53f-8c51-3c1d-89e6-2c81a8191f57 | -11.20996 | -45.07306 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3a059ca-fc96-3965-a2e6-99daaf6ed4e2 | -10.75848 | -50.87738 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecfbb2b4-6edc-35c9-b477-2b5737f3208c | -11.23732 | -54.01307 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8ad38e52-bb58-3f31-8b07-61efdae1bedc | -11.16332 | -51.29819 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 103ce43b-0a5d-36ef-819c-b52ab4553e70 | -11.20916 | -45.07777 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d18abf75-0222-3a62-9a06-dd7c62179089 | -11.27373 | -45.338 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8439c6eb-ee2d-30e6-b9e4-5ac5f2c399d5 | -10.75295 | -50.87627 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36834d31-695b-3508-a972-67169be52f76 | -9.10041 | -50.60686 | 2026-08-30 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee7edda-912c-38af-be58-01be4016913a | -7.21454 | -42.7516 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c92c821-c1a4-313a-9b01-4a8da9064f0a | -12.89844 | -45.88311 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6e21601-b76d-373a-9340-7505d9e77181 | -10.79128 | -45.32654 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e2141377-b4c9-35da-a12c-fdd82ba11a0b | -10.80829 | -45.31966 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 437aa7e9-01ae-30cc-b653-9fc49cce60e7 | -7.25818 | -45.39076 | 2026-08-30 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dda1725b-2378-3305-a7d4-cd17d4dfbcf8 | -8.20692 | -44.81581 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32d147af-deb6-31c6-b7d6-c1a4e2f09651 | -10.74337 | -50.6597 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1b164d-c640-315e-8abf-ba220da2b1d0 | -7.61638 | -44.85016 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 279beab7-2f0a-3d4d-a6b3-4c99ab53649a | -11.24002 | -45.10057 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e725611b-138e-383d-a780-c355955eeda0 | -11.25924 | -45.05657 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc4d9bc5-5607-3cca-8926-28f8d19328f8 | -7.11098 | -42.18781 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be8b2ae1-dfa5-30fd-958e-3617b55d3599 | -10.14453 | -45.69866 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a17e464-7fbc-3891-9e3d-6603a8c90f78 | -11.80733 | -51.05193 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |


[Clique aqui para ver as próximas entradas](README31.md)
