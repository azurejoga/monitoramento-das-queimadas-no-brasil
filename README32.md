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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 084dd9d1-0492-3780-959a-26efdcc6f8d4 | -11.15283 | -44.62796 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 695ed29f-9bfc-3aca-a638-3e1cfa2218ce | -11.60303 | -43.54356 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82f61f6b-5949-324a-85b1-c3a30a0402b1 | -11.46814 | -43.50517 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a28f237-7941-3f55-8b99-618b79b18e43 | -7.87905 | -44.18023 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ca51110-f6db-38b0-be34-940385400850 | -11.46936 | -43.42012 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a6ba3b0-eebe-3608-b016-cca59cbb7f2c | -13.86066 | -43.64317 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d16402c-946d-32fd-8b43-74fd3a891554 | -7.86408 | -44.17432 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 18bbe309-79ee-3d83-93fe-78ba6104e68d | -10.30194 | -44.65142 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 198df925-879b-3e5f-b4c3-fe7b07e6f020 | -11.22699 | -45.18036 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0b51a5-da7f-3218-a3e1-8172f792901c | -14.04745 | -43.84941 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e451c617-0f35-3cd4-8fa7-ac94dd45cdd5 | -10.30473 | -44.63622 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99ca88df-76de-39fc-a8f9-41082f619231 | -11.39774 | -43.40475 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dcb9a16-ec7c-333b-872a-37b2ecb93a1e | -11.46564 | -43.41439 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0d9be21-b85b-3ebb-8f6d-1752c1d29e26 | -13.86055 | -43.63589 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4082e8f-5f48-30b0-a0f7-8df8b0a6e656 | -11.76549 | -43.57406 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b3e97682-a3fc-39ff-974c-81f7b11b37ed | -11.73343 | -43.43818 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1930e7cc-0ae1-3ff6-9f47-b8bcd4dc1a01 | -9.78411 | -44.80269 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28d3427f-09e5-347a-8696-8aba25d24436 | -11.72599 | -43.43323 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc95354a-60a3-36dc-a068-99ebc1327fab | -11.75998 | -43.5779 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 428a88b0-5b54-3c73-a5aa-9af2e86e0ae6 | -11.71679 | -43.43146 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 542b8797-f710-36d4-9858-5f05884016c3 | -11.2407 | -45.19348 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5a31b83-9e5b-373e-888d-1be673eae5b8 | -7.8733 | -44.18246 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96231c22-6fe4-3661-8830-3ce5cee899ed | -11.24127 | -45.19047 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0ebc6d0-40d3-375c-afc7-548e5e4cc4ed | -8.35772 | -45.03377 | 2026-10-02 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf16736d-c1ca-3f7a-9336-3893f268b6a2 | -15.63667 | -43.22978 | 2026-10-02 03:55:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7c21dd52-633a-3a4b-836c-6e71f75ddb27 | -7.74406 | -49.21183 | 2026-10-02 03:55:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 46f7b8e4-e550-3f33-a7ea-33baeffbc1d9 | -8.02555 | -47.47898 | 2026-10-02 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be7712be-41ec-3397-9aaa-6cf6b1fb86ee | -12.32162 | -46.37988 | 2026-10-02 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6bdef88-9638-3515-9e39-d4cb5749acb3 | -9.79453 | -44.80472 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d1b41844-42d4-3b64-9438-a0ea23d832f4 | -11.42041 | -43.40074 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bb1e48e-14e0-3d15-b5c9-b9737a604615 | -12.85515 | -43.81304 | 2026-10-02 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36ac7d45-c1e9-392e-922e-ad62e22a60a1 | -12.98004 | -51.29414 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7bd81a25-e684-3349-9e28-68891f1e33af | -11.1489 | -44.62107 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ce2d5a5-29be-3646-9b03-7646d97f8481 | -11.72673 | -43.50834 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6896fba2-c5ee-34a6-a154-2d500ac8235d | -11.44258 | -43.40995 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a3ab9d1-16d7-3adc-937f-37a640b9b1d4 | -9.82977 | -44.84783 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4228da13-23a9-316e-b908-4aef5e44a83b | -11.15731 | -44.63189 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58b25c73-b36e-3074-95ff-7a09722e2c04 | -13.86504 | -43.63679 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc3ff660-9fde-3354-a584-78a116fafdcb | -15.11668 | -43.62127 | 2026-10-02 03:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7293f9a6-98d2-386c-8ec4-076eeb6a135b | -9.52397 | -45.33883 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afd2c3ab-a764-3e57-8fa4-09f529bb9a42 | -11.46581 | -43.43945 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d572424-251b-380e-b660-8b0ca1d3520b | -11.51391 | -43.50578 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1ed5090-4016-363d-b958-ddfad43476c6 | -12.9962 | -51.29 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 72473e6e-0e66-3e3f-8c59-e5b61b9ac988 | -11.47239 | -43.45576 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 067bd9c4-7529-3751-b1da-f14a39e40fe2 | -10.26231 | -49.6655 | 2026-10-02 03:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5245a437-77ae-3a88-a37f-f6e0a98b3d01 | -11.75527 | -43.57737 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 69a5d6d9-5332-35bc-a1fa-97c4044c4581 | -15.49915 | -41.55278 | 2026-10-02 03:55:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fe389fa-e4f5-3159-af76-ad3353402625 | -10.24898 | -44.56684 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3b03f7f-c238-3fdf-81b6-4b1b72965a3b | -11.4263 | -43.40522 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7084b6e-0507-340c-be91-df1b8be663ca | -9.1227 | -44.74099 | 2026-10-02 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abeac1d-c427-3618-b6c7-1967825f5241 | -11.65991 | -43.61148 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 035c87b8-054b-3fe8-8b1c-999f9a7cc4cd | -14.04684 | -43.85078 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df248525-0cc6-3a63-8d37-07ab1585c5fa | -12.98729 | -51.29586 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 06b094e0-5fa5-3aa0-abf7-3a1d5bd514c1 | -11.23944 | -45.22854 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e834560-f78e-3691-b0f5-941dbc52a88b | -11.67102 | -43.60354 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 56c1e314-fcd3-3ec6-bfbf-8cf0eb0fd742 | -11.74266 | -43.44637 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86be52b3-fb48-327f-ba33-de5039e357e8 | -13.8642 | -43.64137 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb7f4ad9-befe-37c4-9817-f00202f5356f | -11.79224 | -43.55908 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e27b2d30-fc2a-3af6-b531-cec864dcaa6b | -11.16059 | -44.61426 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 060787ec-b796-3454-aecd-24b6b2778921 | -11.76526 | -43.54937 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f3b94ad-2a73-34ea-9bf7-84be1f2616ca | -11.44719 | -43.41084 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00fb2d52-304e-30e4-8624-39db8b27a9f6 | -11.14552 | -44.61132 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5c7d6783-9f03-39c5-818e-55ca0f109872 | -12.56123 | -43.07637 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f2f2e298-7104-31ed-950b-e35a859ae16c | -11.75599 | -43.54763 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c71331e-ac6a-3a8e-a5be-cbe177ddc7ed | -12.98922 | -51.28529 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dd03c753-85b8-3ebf-9e71-66b2a286798f | -14.33813 | -44.73918 | 2026-10-02 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b46a6154-d51e-3f71-a9ca-1071a582dcb2 | -11.59838 | -43.54268 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11d905be-6e65-37be-b577-757b3da6f917 | -12.51494 | -43.10408 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37f784d4-6568-3c11-a13e-11bf9aa63934 | -11.47682 | -43.43154 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7e46879-0030-3cf6-8a0f-a29ea0ffbc39 | -11.14496 | -44.61428 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88ea4cc6-6e5d-3c02-a832-eed9606ff70b | -11.14945 | -44.61813 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38000a64-347c-3ed5-bce1-4d9f71a93a1d | -11.60015 | -43.54452 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a548789-5208-397c-bc14-a00c22a387ea | -11.13045 | -44.60833 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb6d6749-cece-3380-9386-2afa5a5d3cc0 | -11.73433 | -43.4334 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8aa3ade9-847e-358a-8feb-d2613d169777 | -11.7111 | -43.5154 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8eae003-779b-32b8-a7ca-7e1b53997e7f | -14.04291 | -43.8485 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6667b7f-78f5-3097-97ea-6001fbf8151c | -11.72702 | -43.4469 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f56c3e9-44fe-31ef-916f-91242aa47615 | -11.46208 | -43.43373 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ecbe5b2-4e24-3e7a-9008-423a6babdc09 | -9.32737 | -47.25185 | 2026-10-02 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 427d2954-ed0e-38e3-8e2f-b495bc8af67e | -12.52015 | -43.10071 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 569eb3be-c024-30c5-acfb-695c68bcf9a5 | -11.72973 | -43.43253 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbfe466b-99de-39a8-8a0b-cf0e2865a6f4 | -11.24528 | -45.19783 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8211e3fb-0173-3db2-9e63-49f00f253ac7 | -12.52381 | -43.1058 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9be48d8b-1495-39f5-b887-470700a1ec48 | -9.78933 | -44.80364 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a77a64a-4d11-322f-a7a9-00a6a422832e | -11.6961 | -43.5981 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae22a790-8795-3848-845e-27367afe2d05 | -11.6646 | -43.61221 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6c3db741-b1f2-358c-b81e-9c1e380be1f7 | -8.53703 | -44.05597 | 2026-10-02 03:55:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f7f73d-4a5e-324e-97fb-f08905fd8d33 | -11.72793 | -43.4421 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a40021c-bf7e-385d-b1bd-81d604922dd2 | -12.86066 | -43.80907 | 2026-10-02 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2cd15df-da38-3533-89f1-58c64fe695ed | -7.51208 | -47.33316 | 2026-10-02 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e42977f-f460-3189-ba2e-1fd7c26c3727 | -11.75094 | -43.44643 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aa529bf-8e67-37f1-9cb1-3c5d14ad89f0 | -11.12819 | -44.62033 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f09d617-8945-3fda-9f82-cb911a38e5f2 | -10.26361 | -36.54424 | 2026-10-02 03:55:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7dda1142-6ed4-3c56-881c-ff373d0ee31d | -11.13937 | -44.6163 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31ada517-7166-3656-95c2-38550406fac4 | -11.65701 | -43.60104 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cbfdbd1c-de74-3d11-adcb-533b9ed3cb54 | -11.79903 | -43.57445 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b49d6a1f-0217-3f2c-8c19-a97b94eda793 | -14.50344 | -42.22123 | 2026-10-02 03:55:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8e67a20-1002-3db1-a2bf-ec7255b21f14 | -11.75149 | -43.57187 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 10596e6c-ec03-3c59-baad-1da3202cdc5e | -11.46847 | -43.42496 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae903cb2-423b-3fde-a6e6-73d208bb47bd | -11.74685 | -43.571 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |


[Clique aqui para ver as próximas entradas](README33.md)
