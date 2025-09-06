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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fc8bc0b-3e7b-3c06-a818-0301a21f10b7 | -13.00216 | -54.84158 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8c2cf23-01dd-33c4-8d55-bb54b1e03595 | -14.71549 | -60.25862 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d734fe7b-046f-30c2-a469-eee546974831 | -9.09095 | -47.00741 | 2025-09-06 05:31:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 873337cd-ac60-3f17-b98e-3e2672727cdb | -10.16786 | -61.13829 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b148c84c-74a9-38a9-a4d5-022ba016229e | -14.18463 | -53.0294 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1dd5c3e7-7311-3b12-b51f-fb429aea37fb | -9.99441 | -60.01778 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66eb9af0-6996-3e14-b0f8-2576737ea52a | -12.48248 | -53.85375 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45348986-af4a-3668-80bd-625f7ffa08b1 | -12.96811 | -54.80863 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3552f286-c7ed-3424-ad32-35db5fbad302 | -11.16426 | -59.14901 | 2025-09-06 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de65c7b8-757c-3505-a96b-91282bf72f36 | -12.99141 | -54.79188 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7176fd4-9aa4-3e0b-a616-f2bf99d4cd11 | -12.99784 | -54.82584 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28023614-34f0-3d37-9a1c-1697e7296133 | -11.21771 | -55.03287 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9970e46-4d53-33e1-8a77-c6b65f57e779 | -12.51625 | -53.85286 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7235ccb0-1b3a-3c01-b04f-389917677408 | -12.97621 | -54.82921 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0531aa61-9198-3405-a9dc-7423b59999ef | -12.96643 | -54.77871 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 622d5356-9e81-34b5-8287-1ab03b1058a4 | -14.18163 | -53.02817 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e467bdc-45a3-30b2-9556-defef3e7865e | -10.16444 | -61.13773 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d691d7b-67ed-31d3-9ce5-44dae45c4c5e | -13.00068 | -54.8457 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71cb71dd-9fd3-3690-94eb-ebc854f883d6 | -12.49216 | -53.86642 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d36c4300-9879-3f5d-9760-c4562fa19947 | -12.41494 | -63.90252 | 2025-09-06 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc2f0094-acca-34a9-8470-1eaceef58c6a | -7.33932 | -43.94402 | 2025-09-06 05:31:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 397306b2-af2e-3ae1-942a-89fe117934f3 | -13.00736 | -54.84237 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8c7437e-b8ee-3d91-9314-2c8c2d223239 | -12.98142 | -54.82997 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f0938c3-8c4a-3f5e-9dcc-cb868264a589 | -12.48158 | -53.86114 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bb7074b-56ca-3984-bba4-9e0223de45a3 | -10.16731 | -61.14188 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c91c15ca-a8ee-362c-bf34-35e7e0e7f00b | -12.17029 | -60.74089 | 2025-09-06 05:31:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3eb76a-88f3-39bf-8f94-f2056b206a7c | -12.96656 | -54.82133 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39cb7417-f81f-3e20-85ae-2c44802b6405 | -14.18513 | -53.02473 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 64f971d2-eec4-399b-86be-a7a65470b479 | -13.046 | -56.86246 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c627620-ce86-35ed-9d8b-74329a491880 | -6.59572 | -44.5501 | 2025-09-06 05:31:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 23a59f60-5ffe-3a8c-9869-8a73d9c341ad | -15.17817 | -52.40124 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 940866cf-842d-3071-b904-546cb1b0473d | -12.96172 | -54.81749 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54e92799-6038-3062-8524-2dfb1d4801fb | -12.95282 | -54.80333 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c78e838-4c8b-3069-95ff-8e62b91cc778 | -13.00107 | -54.7998 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97107717-b210-3b20-a42b-5cce2bbb4c08 | -12.98102 | -54.83323 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d306b78-64d4-3b3a-af05-5bcebbf716e7 | -12.95166 | -54.81291 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb2bced0-3288-3f60-a5a6-3135ef84790a | -9.31051 | -45.41094 | 2025-09-06 05:31:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4a83a152-51bb-365e-9ef2-c7cc05024554 | -10.50508 | -57.77638 | 2025-09-06 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13f1c68b-e581-3919-bc63-9a20b1789412 | -12.97334 | -54.80931 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d8095cb-7545-3398-abca-1b8a42087160 | -12.96683 | -54.77539 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b208af14-a60d-36a0-be2e-9451c524a584 | -10.5788 | -61.24922 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ccdceb-1b57-3cde-8588-f73a44bf3ae9 | -13.01892 | -54.83428 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58d9d916-3e30-3f46-9da9-55799d6302eb | -13.04146 | -56.86176 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d926caa-2924-32b6-bec9-ba66cec9fb72 | -11.47783 | -55.55331 | 2025-09-06 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 55db5168-6d21-3537-b1d0-569f361261de | -14.34409 | -60.33476 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 324695a4-d3b7-306b-b9af-985f75ec91e8 | -12.96249 | -54.81119 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c023ad2-ad7d-34ec-b04a-c2dd94cdc2b0 | -9.08808 | -47.02465 | 2025-09-06 05:31:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 05a7ecd5-96bd-3901-90d2-4e2650222a53 | -12.96443 | -54.79519 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b385026-f2b6-3c6f-a332-376873b3497e | -16.3047 | -58.10921 | 2025-09-06 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f4372018-bab6-3496-abb8-89bdda0f8fb9 | -6.8714 | -45.55063 | 2025-09-06 05:31:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 3023a133-915d-313b-a4c9-92858dd5fb2d | -14.34407 | -60.32246 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a4c5718-8630-350a-8f7e-97dde494e05b | -12.95881 | -54.7977 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a5bc579-7e2e-3881-a304-fbea6c2ddb61 | -15.12704 | -52.34254 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57a548d4-1494-3569-b366-193dd9ad14a0 | -13.01295 | -54.83997 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2385167-bc29-3a84-ab38-622c800f9af0 | -12.98624 | -54.83389 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5f42054-cc48-314c-b5cf-3a808b57cdb6 | -16.63631 | -51.86461 | 2025-09-06 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a23f9737-ed82-31aa-afab-68fa2fa8f18e | -8.10537 | -45.33168 | 2025-09-06 05:31:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d2961fa9-e69e-3e1a-8058-7edf1ff7bcdb | -14.18253 | -53.07328 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 998f8a39-7774-3d3b-88a3-16bbf975068d | -12.51028 | -53.85584 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24171111-6d3f-304c-8729-5506f60040f4 | -14.26003 | -52.18876 | 2025-09-06 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3c29df8-fc28-3285-9f67-4d338b16a86d | -10.59669 | -44.33826 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7dc281ab-f845-35a3-8d88-5939303f38ec | -13.92412 | -53.98925 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69a26e2a-a861-34c3-9b03-85d75455f31a | -13.93482 | -53.99473 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 987455c7-9934-3cf1-b89a-799f492ec34b | -14.18947 | -53.06529 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5beac01d-0617-3a4a-b72b-2f4e0b5f20f2 | -12.49768 | -53.86723 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 424e791f-a288-3ae5-b23d-50cb4e3c2d33 | -12.97738 | -54.81968 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 387765f4-d7ed-38fd-8641-3380d3a99135 | -11.21378 | -55.0236 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11f7cb33-d90b-305a-81ef-fc1ad2c0e69c | -15.84572 | -52.2834 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c5008e4-8afc-37f2-b7f7-12405d68c1f1 | -15.84312 | -52.28324 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b56f444-b9b9-3e74-b876-21a79e25cca9 | -13.01815 | -54.84077 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8006596f-26c5-3a32-a175-0abb96e0d409 | -8.10755 | -45.31789 | 2025-09-06 05:31:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b8176b05-0a60-309e-8bb5-d5f1cab709c1 | -12.98882 | -56.91187 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c321097c-7ff3-3edd-8559-8642445cf3b9 | -15.21504 | -52.35357 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a442451a-fb3f-3ab8-8fa6-95c55ebf100a | -13.00027 | -54.80629 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e9ef92d-44b8-3064-b683-62d9f59c1c30 | -13.01853 | -54.83754 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 226736ce-3563-32a8-9b4a-1ac8960d1421 | -9.89553 | -60.24738 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 204e6a10-7ab7-3e06-b9d4-c41efd68f8ef | -14.71924 | -60.25915 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 747cec9b-05de-32fb-9ccd-9e4628ac461f | -9.93407 | -60.10564 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d61ea0-d4cb-3e64-b8c5-4fbe60124090 | -12.99865 | -54.81937 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 837757bd-72b0-32e2-b4e3-2695cd7c18ba | -13.00178 | -54.84478 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e15ad6a-ad09-3d89-b4f0-98dcacad0922 | -14.17216 | -53.05838 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7e8d7aee-dd37-3560-a8f0-0fca7ae150e8 | -15.22132 | -52.35439 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cdc2a83d-d894-37b6-8c77-cdee8dba1c65 | -9.998 | -60.01831 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2dd392-9304-353a-b698-adf886ab0267 | -12.9906 | -54.79847 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14f75d3c-c212-3d12-a9b2-2fc6a1f173d8 | -12.95436 | -54.79053 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 279906dc-ab82-3a28-ae3f-7e0a052f448e | -11.21956 | -55.01838 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f0a08f3-1932-3ed6-a93d-bc2f67f2d03e | -15.69204 | -53.59094 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d64422e-cd5e-3bb0-b9dc-df046ac61e42 | -12.19056 | -53.90253 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6b0fd23-3fd2-311e-a721-406ec863eb70 | -13.00887 | -54.82956 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1659bf4-0a3d-38eb-8511-76565cdd4537 | -12.49923 | -53.85427 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e9e1d752-46c5-3159-b395-efa30636fb71 | -13.0137 | -54.83353 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8acc900d-350c-3ed3-9937-1df202e7c955 | -13.00148 | -54.83931 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 801d8f92-15de-3a71-9937-cf7c0ab4564c | -15.21093 | -52.36922 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f09c713c-0e2b-3f46-8b6c-fa905141d9d3 | -10.15758 | -61.13675 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544916da-7004-3209-8b4d-765680f05ceb | -12.49242 | -53.86454 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca5206a3-f532-3488-a606-44c8f83f3ebd | -11.20765 | -55.03161 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66f077be-a15a-3a5d-8520-e10816ccd5e2 | -13.79582 | -52.74502 | 2025-09-06 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30128f84-5017-30bf-8981-8309e2999079 | -12.96772 | -54.8118 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29e7bfb6-a4d4-36c2-8d88-7cd840c9dae5 | -12.51072 | -53.85212 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19dde1a6-6103-3082-ab73-2efccf960ebf | -12.49352 | -53.85538 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README85.md)
