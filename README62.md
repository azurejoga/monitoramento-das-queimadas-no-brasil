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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ea80dd-273e-34a2-8fa2-c725826a5dd4 | -11.8416 | -50.49695 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 361f03f5-003b-39f1-b2e5-6a77fbf7d6cf | -11.39312 | -47.3386 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1890010-b516-3c23-b6c8-e44dba963168 | -14.17159 | -46.16015 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1013e28e-d065-3fbb-8a3b-163f0cbb7d90 | -12.68076 | -54.66665 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 01e80026-bcbc-3a13-ad90-30316fa92903 | -14.37357 | -52.93465 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1045d0f3-6799-324d-a502-cc4f7939f4a7 | -8.17867 | -46.77262 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fe42fa4-5844-3a62-8c9a-1c66436200aa | -11.44333 | -50.47649 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12f1c627-5ffe-336f-9dae-9dbdf50092a4 | -12.61698 | -57.006 | 2025-09-14 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22ce62dd-6219-32b7-b1a5-167421d4dbd4 | -11.86063 | -50.49057 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 8949e5a8-1039-31fd-a51f-d7527490fd71 | -13.90324 | -48.30553 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca169ffe-1dfc-3dbc-a027-8216cbb55e5a | -12.66489 | -54.67653 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b60b20c1-6abf-3c9d-9f4b-46a3470ac73a | -18.14189 | -49.18963 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50688f61-12cb-3343-8833-51cb4a1d16ee | -16.33413 | -51.51925 | 2025-09-14 05:10:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 906e8d2f-c88d-385c-a42b-8b05481c9ce2 | -20.9094 | -55.18364 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1707a2a-ac47-3b16-b0bc-37a6e0ba1779 | -18.95442 | -46.31601 | 2025-09-14 05:10:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0054c126-df07-3276-a87d-27098f053a7b | -17.2538 | -49.26258 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa16b2f8-5372-3057-9870-64d8d7da05b1 | -15.76196 | -53.48205 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db31f7b3-fe11-315d-a301-499580578100 | -21.65195 | -50.12174 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f81342f-6ec2-3554-96e6-02ef1a099b78 | -18.91547 | -48.01057 | 2025-09-14 05:10:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d18cf60f-4337-354f-a16b-0a46c5968051 | -16.32861 | -51.52718 | 2025-09-14 05:10:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41f25db-fd7a-36a6-b2c8-842d3ccf5852 | -18.14622 | -49.18689 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca883287-e5b9-3d64-b291-a65effd541d8 | -16.86792 | -49.35235 | 2025-09-14 05:10:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427435c8-7de7-3141-a188-be681421e2cd | -15.93724 | -49.97403 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a603c48-a4bf-3abc-9e91-5561543be3b4 | -20.78825 | -56.96372 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc77e3e-e3e8-350d-9b27-bacabcf5d75e | -15.92676 | -49.97872 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e78e4cbc-996b-3060-b312-0c0247c4ae28 | -17.30453 | -46.11002 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00862482-c48b-3b72-ad32-77fc4dfceaa9 | -20.79404 | -56.94833 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a84016df-627a-35ec-b198-d2eaf1742daa | -21.65718 | -50.12231 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf3ab133-d050-3804-b611-408f71f2702b | -18.16077 | -49.20189 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d3fa106a-3e0a-3262-a54b-90af703f0552 | -15.57802 | -54.73647 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d43fae6-400b-3baf-ac3c-bdef5fc0a547 | -15.28725 | -53.77551 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 615843b4-a923-37b1-b2f0-9f48c10a6be6 | -22.17741 | -49.61893 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 642feb46-2881-3003-a2ec-50aed1db1ee5 | -15.76902 | -53.48825 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e28c2e6f-746d-32e1-8125-631434d3bfa1 | -17.25535 | -47.25011 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c1c1916-9469-3653-9ace-42fbe11cc258 | -17.44683 | -49.24294 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22911be7-bdd6-3885-a884-386c90d8fbdd | -14.95764 | -55.95212 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 305be98b-9818-3ea5-819b-e51f973f07af | -22.17197 | -49.61848 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e8035c5b-8362-3270-8769-54f975f9cede | -17.36637 | -52.90817 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b931c94-1146-3f00-92fc-f5c00faa4130 | -15.76228 | -52.23684 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab4a6c32-90b9-32cb-a362-1d2f98cba56c | -21.6571 | -50.11894 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0f0343b-dbd7-373c-b3f6-36f27e40502a | -17.3211 | -46.08318 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abca27c0-5c8f-36b7-8a92-7f9dd6ca67d0 | -17.41536 | -49.23915 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2930fa6-ee9c-3596-b0fd-33d69bb1877e | -15.77747 | -53.4844 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0a2b44ce-e0cc-3203-a01f-cea2fea7dd1a | -16.71268 | -54.95503 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85911995-e1da-3b22-a7c3-9b27d7b8b0e8 | -17.36323 | -52.9003 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a11dcad7-1513-3f31-80cf-0f4da529d9a8 | -18.14648 | -49.1967 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23ca9d09-8cfa-3b0d-ac2c-cd7e9c8e6b68 | -20.09434 | -46.8859 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5bc1d51-d57b-344c-ab9d-aef134744e01 | -17.31378 | -46.0822 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 969a1f3a-a1a5-3ebe-849d-95680441ec5e | -15.68844 | -54.34407 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f82d36-c59c-3a5e-b6c5-7eac6795179a | -15.28452 | -56.02471 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c17862d9-e2c8-3168-baa6-e11b65a5a73a | -18.14495 | -49.19895 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b2d1041c-3180-38ec-bbc4-1d33010660c4 | -15.34659 | -59.18787 | 2025-09-14 05:10:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 482a2364-482b-3de8-812d-ecd61aa32601 | -15.76152 | -52.24335 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2be661a2-84fc-3917-80e8-a069ab91cb68 | -22.20775 | -48.35193 | 2025-09-14 05:10:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cec17181-e5d7-3a6e-a9f9-07baae2d65dc | -15.08282 | -52.46952 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07dee9e7-bbb5-3d16-8f60-5c4373ef62e6 | -17.25415 | -49.25949 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fb6ed86-afef-3ad7-876d-9e016d5db6a2 | -18.9151 | -48.01439 | 2025-09-14 05:10:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb5d5fea-5c49-3bf3-a3ab-dbc686e4d12f | -15.59423 | -54.7522 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eeb24439-55cc-3887-bfcc-01ffb224d5f0 | -15.18094 | -52.31828 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a041d774-58c1-3043-898d-be08fd8f05c9 | -17.45214 | -49.24298 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52c31700-c5dc-3c8c-afbe-95d8714b305b | -18.91479 | -48.01274 | 2025-09-14 05:10:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 904abd5b-27d4-3501-947a-253b0b5fea59 | -15.20311 | -52.48624 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca88324-37cf-3e16-bd7e-ecbed395254e | -20.09391 | -46.8908 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd9091ce-2e56-32c1-9ab7-36dd2859d53c | -15.27027 | -56.02622 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5167531d-efa7-3657-b3a6-10e1380407bc | -17.26176 | -47.24636 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7a155ad-f868-3f19-b63f-87f250a68d86 | -15.15198 | -52.47086 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 313c5fcf-02ae-376a-928c-c609cbfb28e4 | -15.3426 | -59.19101 | 2025-09-14 05:10:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0188b7b4-cb4a-3e23-907c-209c7f71d6c4 | -18.15089 | -49.19363 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 793c8a7d-617d-3bf4-b030-dbcd9b561fc7 | -16.71206 | -54.9594 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bddae0a8-e29c-3fbf-8c4c-2b14c512fcf1 | -15.34321 | -59.18728 | 2025-09-14 05:10:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d9430e45-a2e2-38fd-8adf-cbd4c713c83e | -18.14682 | -49.19369 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3bff9eee-544e-3980-99c5-9b91ea67331b | -15.08494 | -52.47279 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2cafd0f-5fa0-3284-a8af-f6054b9e5dd7 | -17.27706 | -46.12687 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81974946-7864-3457-b45f-01e80deb58a0 | -14.7141 | -55.64939 | 2025-09-14 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e52ea820-e909-38c1-a3bb-eb3a2397c9d7 | -15.57246 | -54.77524 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b12c33c-d69f-3478-9fc4-5d05ddbe6a92 | -15.9357 | -49.96706 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a41c69d-26a8-3515-890b-22e5117c555d | -19.25872 | -51.43151 | 2025-09-14 05:10:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8ce99f2-2dda-322f-94d5-ccedac5a2d0e | -17.82899 | -50.42202 | 2025-09-14 05:10:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15c6d114-b38e-3641-b997-eb04a73aa45e | -15.43498 | -47.35445 | 2025-09-14 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d53c8c6-006f-3782-b84a-f54340f5eee4 | -15.15657 | -52.46782 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| face4e3c-1d92-3cb1-973f-6e201816390d | -14.75011 | -60.21564 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 659a9ccd-2fe0-32d8-a7f5-082e943ad31b | -15.26398 | -56.02135 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215608aa-08e4-3d2b-995e-0e46744527b6 | -17.31933 | -46.09127 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aa6e338-d4f4-30f1-8a63-ff9e6d68158f | -20.10041 | -54.60756 | 2025-09-14 05:10:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d80e5071-99b5-3cd6-b5b5-fa7e9b85088c | -15.67592 | -52.24398 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 104dc89e-2663-3f50-898b-f5dc95b900d6 | -15.76469 | -52.25193 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ac422aa-b092-33d8-8881-f68c4098e166 | -20.57084 | -54.59351 | 2025-09-14 05:10:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e959a7e5-e96c-30bb-b091-7ba1e4754149 | -15.59778 | -54.77875 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d46e61b-e566-3fb1-90e6-f6bc5e1cbaca | -18.16109 | -49.19893 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 91e257bf-f149-384c-96de-45fa22587cbe | -21.65152 | -50.12178 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bbdd16c-9e87-3d2b-8f87-0d6534e30796 | -15.76175 | -52.24082 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb04d52b-301e-3b62-b62b-7e1618aadf22 | -15.18967 | -52.31612 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08894f4c-dfad-39c7-99af-8364948f1112 | -15.42415 | -58.77446 | 2025-09-14 05:10:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 818290ad-21d5-39b8-a1dd-8920752865d0 | -15.80525 | -52.20292 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78942fa2-57d8-34a7-a98c-eda36ce028a3 | -18.00767 | -46.97303 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c94ec33-fe8a-3415-b873-cc2d7d34e82a | -20.13326 | -46.87585 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc392e2d-9e58-30a3-bbee-aa3e6d509a41 | -21.59118 | -50.96985 | 2025-09-14 05:10:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 653ad35b-36d4-3db2-a4cb-1c669791c0f9 | -15.58889 | -54.73801 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1824bd8-5c92-31a2-94ab-cc34cad8f637 | -16.70476 | -54.95867 | 2025-09-14 05:10:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa7d8919-1002-35b5-a063-16bb0caaad7e | -15.16466 | -52.46978 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README63.md)
