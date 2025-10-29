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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 377db343-94ad-3261-87f5-2973faa9ac17 | -13.57414 | -49.59081 | 2025-10-29 04:25:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4065ccd7-a84c-36f5-a3ad-810f9daf23d3 | -13.65049 | -46.46275 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b6cc276-e9d7-3385-83db-048ec77fcc60 | -10.85946 | -50.12794 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb782197-c3cb-39af-b1e0-27e3a66d5f20 | -13.9174 | -48.45686 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc7594b-12f1-3606-bfa7-15191c2809ab | -11.02523 | -47.84404 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4047d0c-cbc0-3781-b4ec-6315de3570fe | -13.43082 | -47.37238 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2321e6f8-dc13-3900-bad5-9291372de15c | -13.01594 | -48.77294 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b8195b0-48dd-329a-811f-190dbd3fe3f8 | -13.74121 | -48.39548 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b0f005a-a7c6-3941-9b67-2cf8b98279db | -12.52925 | -47.54467 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7325cac1-583d-3916-9574-cd2593d4eba5 | -16.90068 | -42.92286 | 2025-10-29 04:25:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1bfe923-6c9e-3f81-880a-dcd8c62e53de | -13.64328 | -46.4652 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4921038a-c0ec-38b8-a539-0c06151fb507 | -13.6082 | -46.47786 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da86cf33-4b9a-3bb2-8df0-241660673d95 | -13.17373 | -48.45111 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3102382f-2e27-3fc8-8ab6-64d9d85142f8 | -11.00889 | -47.846 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2237b3-e121-3de5-9b10-0b552213a666 | -13.23687 | -47.72624 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00427966-cf9a-3033-b8eb-11f0152115d0 | -12.96356 | -49.9655 | 2025-10-29 04:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cb96215-2cd4-3a36-a046-06e599cf79ed | -14.23243 | -48.11364 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0627a29-7e6f-3bc3-9aee-0b2861f6742d | -13.65381 | -46.4633 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85cecd29-dd30-30bf-b91b-376beec188af | -13.66839 | -47.17946 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca5101cd-47b5-3db5-b4d7-84982e227ab1 | -14.51558 | -47.96407 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77dabe11-f833-3622-b8a9-cf34553d45d0 | -13.56395 | -47.15402 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caff72ea-635b-34e3-b330-1c50f06e6793 | -13.86732 | -48.50248 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fe2375e-08d4-3bc9-ae9a-43e1d1c381e9 | -15.16393 | -47.22295 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e74db7f-7396-3411-a4b2-01bb56a0f174 | -13.67276 | -47.19497 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07d18f6b-5e44-39ed-865a-b52163150032 | -11.02929 | -47.84089 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46658b8e-9049-316d-88f5-c65f36c215c2 | -13.24375 | -44.10988 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e08303c0-fd37-301e-9417-5d84d2f1c69b | -14.26234 | -48.12281 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98f4b18d-7afa-38db-b809-4d7402938f6c | -15.15946 | -47.22951 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30197358-b09f-3948-97e7-2ff054c91665 | -17.93227 | -44.27605 | 2025-10-29 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79eb3da9-9e29-3fe5-88b3-317d81d4da23 | -18.54852 | -41.57696 | 2025-10-29 04:25:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8efa4a21-5d28-3f72-b1be-c623d6778ea6 | -13.9155 | -48.46832 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12db5c9c-2cc8-3614-a549-84af92b30b0b | -11.8818 | -44.43114 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f2479987-328e-3cf5-8d08-6ddc04798634 | -12.14239 | -45.21108 | 2025-10-29 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d383cb-e0ac-3561-9ce6-e75356814708 | -13.87107 | -48.48003 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3ece60e-1bb2-33cd-97f3-0e1a5f308703 | -13.92272 | -48.44604 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5601b9c4-5187-3f4a-8132-81407ea3837f | -13.21538 | -47.06728 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c48ad10a-5818-3b4a-9e6d-f781e651fecd | -11.61076 | -46.82391 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 270fc63c-abfa-31df-885d-4405c2e6c072 | -13.63573 | -47.04858 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbbf97a6-11b6-393f-9f33-561c0ab97dd5 | -13.63597 | -46.51134 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3071533-a478-32db-b75b-44026e3a487a | -12.36304 | -44.067 | 2025-10-29 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cc07c91-6005-3661-81aa-3e84f6510e74 | -12.09189 | -47.25079 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44e162f9-82ce-3c30-8ef3-3df0fff528e4 | -12.05844 | -46.6272 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36c4b209-3f17-3a41-9e9b-c681bcba48f3 | -13.54259 | -47.35016 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48e1ce5a-522c-3c4d-a55f-883a68a9f1b1 | -13.68784 | -47.66201 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a73e8b-e06e-38cd-99dd-7509bf69e2d3 | -14.49464 | -47.88034 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5b70928-8bf8-3cf4-a245-092fd2885eec | -13.62667 | -46.46245 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee63a10-def2-3d4c-b0f6-f63a02b47b3e | -13.3015 | -47.6922 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f16057d4-c0fb-3884-bbe7-5088ffe25ea2 | -10.63783 | -52.18103 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d07de3d-cae8-3028-949c-c608f6e1117e | -17.688 | -43.95565 | 2025-10-29 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32fdd2e3-239b-38d3-88d0-29dfbca9bd22 | -13.63873 | -46.51544 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 242c219c-a37a-3852-bf94-2d148f6ef26a | -12.70379 | -46.31138 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11924fc3-54f9-3be9-bc9f-d34a7291637a | -17.25827 | -45.294 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f32af6c9-e173-3b97-941f-73caef23a6d1 | -13.56063 | -47.32372 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fac20178-ffe1-367f-af84-57e4037f5bf7 | -14.60674 | -48.42773 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57db2322-d3c2-3ca2-8d63-cf57ccf35888 | -13.94169 | -48.48126 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e168db6c-d2c3-3685-8d7e-824cce2eb451 | -11.03148 | -47.84907 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a468990e-75d2-32e4-96e8-8c5901240aeb | -12.00723 | -46.77581 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869ee97c-e1f3-3a78-aa1c-1e76b81d5214 | -12.01114 | -46.77279 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 218e899b-ed88-3bd7-8aec-022764192c6e | -13.91334 | -48.46001 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aef9346f-4648-3885-8fd6-2ffcb47ea2c1 | -13.23378 | -48.00031 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 084762fa-58ae-368f-875c-3e33519023d8 | -12.55754 | -44.96655 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| beeae1b1-5aa2-304b-aa06-ce74cc34739e | -13.27531 | -47.72501 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f3cc56c-d23f-3cde-86bc-84b1787e8fe1 | -12.14517 | -45.21519 | 2025-10-29 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1455f9be-7e0b-38c8-b393-2e576716834a | -15.15613 | -47.22896 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98d16763-ba80-3a34-8ca7-90365600fdda | -12.16152 | -47.91102 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 031d2f71-974e-3649-be64-f689a73fd47a | -13.42352 | -47.37487 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a23f18-bad7-3a5f-98e3-5bfbba18b457 | -12.14183 | -45.21466 | 2025-10-29 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6bda8a8-ac3e-3d76-8b88-ff81d4b3bb44 | -13.20767 | -47.05129 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e91dd309-95d3-35fa-917c-f3ce30127052 | -13.30987 | -47.70477 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 756caaad-c922-38d3-a6b4-ca746cd4c61f | -13.61457 | -47.59685 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31a8de0b-3b7d-3010-8ac1-01982d1ec38b | -12.15618 | -47.68744 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d65019f-a592-354b-b210-12fc576c6e0c | -13.60229 | -48.4166 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2397da0-f85c-3d77-a225-c3a4197ea797 | -13.60708 | -46.48496 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0d4c975-60c7-3e3a-874e-f08a042066c4 | -12.44382 | -43.75313 | 2025-10-29 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4e26442-3ebe-3aa7-b9c9-e0153822a13d | -13.94765 | -48.46654 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a92de9a2-8193-30b5-a7f7-1d0f6bacdf5e | -12.58442 | -43.36573 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89c14f56-4f4e-31fd-8306-b14b38c2cf4e | -14.93115 | -49.65236 | 2025-10-29 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1fbf30a-ef22-3816-83e4-567a52233472 | -12.53075 | -44.88763 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c59daea6-6a6a-34eb-a325-2ca2e1063a96 | -13.63878 | -46.49359 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2980635-06d1-3bf1-a2bf-e209142b518a | -14.60168 | -48.4199 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60b7ba99-d24e-3c58-b209-50d8a632d343 | -13.47748 | -47.45404 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 151d1007-5dea-3f1f-8f5d-3d99fc3899a3 | -15.18343 | -47.2079 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f485c59-44d7-3f99-b165-8db1e1c8b29d | -14.26078 | -48.1111 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6766f971-2cf6-3440-b0da-f7b3de467c85 | -13.30548 | -47.68907 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d55a8984-4deb-3cdb-ada3-602e03200c29 | -16.30092 | -47.81532 | 2025-10-29 04:25:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b1500ec-3744-33f3-a05f-e4038719f876 | -12.85632 | -48.62609 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e74567-21fa-3c45-a70a-5059628fe9c9 | -13.63816 | -46.51899 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10054e14-f7e4-3fcf-904a-ee124c2d32d7 | -11.03272 | -47.84157 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 403a5fd2-9e75-35e2-8bf5-7818bce96234 | -14.73801 | -48.18437 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce079a3d-fdf2-3fa6-b9a8-0dc6343778a8 | -13.63095 | -46.52143 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca179259-79f9-3b3d-b8ae-569258f80654 | -12.98548 | -47.91587 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 935ffe9e-8806-323a-bf68-ee760a20a60f | -15.19903 | -47.19583 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b61ec439-d0dd-32d2-a0ad-803559b61095 | -13.82164 | -41.69318 | 2025-10-29 04:25:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e22b90dd-2112-393f-be64-bd0ecb6d8840 | -11.97337 | -44.03485 | 2025-10-29 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 872dbfdd-8724-371b-82fd-17ce11cb9beb | -16.04864 | -43.70725 | 2025-10-29 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1809c4c-df3a-39cc-83e3-f975ae353fb4 | -14.96858 | -48.18878 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9996fe3-0d8a-3d61-84b5-f0734301a2a2 | -13.36179 | -47.38367 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989a0b43-b496-3e5f-a296-5937b58cadeb | -10.95953 | -49.66409 | 2025-10-29 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdbe9cc5-1529-3d53-a3fc-336d181c4445 | -13.2254 | -47.06894 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8f71224-9ec0-3a5b-8200-6f3830136137 | -13.78733 | -43.25604 | 2025-10-29 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
