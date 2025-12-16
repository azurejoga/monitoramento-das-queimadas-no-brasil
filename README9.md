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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 605c5a3c-2e41-3e8d-b424-fc7d3ca5b062 | -1.36185 | -46.99755 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6cff137-f6a6-3cdf-98d6-030b310b4c3d | -8.42006 | -44.03399 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0321315-b1d0-3644-9302-ee4c12facfff | -1.84997 | -46.39549 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a3650660-8ffc-3ddc-bc4a-23ee8ac5f31e | -3.00566 | -41.87112 | 2025-12-16 04:25:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12cc5bdb-de31-3ba5-8b59-d70fca12c4f7 | -14.43402 | -44.8705 | 2025-12-16 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1fcbc9fc-f0c1-3200-98e4-8d5afb54bc78 | -9.55754 | -44.93447 | 2025-12-16 04:25:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f609b59-d666-3edc-b771-2a038069c3d5 | -8.98584 | -45.9402 | 2025-12-16 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84ab22f2-2988-3898-b065-8447bc6f4e29 | -2.66614 | -46.89045 | 2025-12-16 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5c87c1-a931-3929-81eb-96cec7043889 | -11.14446 | -43.32971 | 2025-12-16 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa98e7fa-7a0b-345f-b7ee-c0b482303661 | -8.06495 | -43.14687 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6020cb15-f615-36fa-b468-7c37ff18a14d | -12.57765 | -45.40654 | 2025-12-16 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0569653-3b75-3c54-af51-8900a5ccf5b4 | -1.6713 | -45.80122 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f62aab95-19de-3530-be46-36b1cc3edf08 | -10.76477 | -44.93727 | 2025-12-16 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fc700b8-667c-37de-8ea5-69868ece127e | -3.42613 | -41.65138 | 2025-12-16 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bff45eb5-e8c5-34b5-bb71-422659695515 | -1.92257 | -46.50389 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81524232-67e4-3065-a29e-d71468480455 | -1.91965 | -46.49937 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5411f19e-b062-3039-9aba-51303ab667a1 | -7.61658 | -47.04947 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb54819d-9b23-37f3-bd85-d9f281218c83 | -10.77701 | -44.45731 | 2025-12-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| add208ec-f7ad-3909-b3d9-3bc95e8a0dda | -2.3597 | -45.4281 | 2025-12-16 04:25:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08fbd3f4-f306-3e80-8ee6-c91bf5767a78 | -7.61718 | -47.04572 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e926a8-37ac-3a7e-9fa9-f0caa563becb | -10.54891 | -48.72097 | 2025-12-16 04:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc756c5f-1229-371c-8767-869188bb59b2 | -8.06896 | -43.14365 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43b3d858-1c8f-3e86-b872-6af30d6c7b2e | -11.04879 | -45.39066 | 2025-12-16 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47594301-d39e-354e-9f27-af62b214735a | -10.18317 | -48.84714 | 2025-12-16 04:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c88945e8-079d-31bf-8823-c73dd4596bd5 | -1.66785 | -45.80068 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f22d652-9fd7-30c0-917c-73a2fe39efde | -11.14897 | -43.32527 | 2025-12-16 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 58060522-bc2f-3615-9fc9-1eb54e4b0435 | -8.41613 | -44.03706 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6315e9-9757-30c4-98e6-7510b1d22319 | -2.66678 | -46.88642 | 2025-12-16 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7baa0c9f-eaf9-3a78-89b4-b03081f68036 | -1.34646 | -46.56256 | 2025-12-16 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8642ece-e7e6-3ea4-a73b-ec05830b53be | -3.08157 | -44.88531 | 2025-12-16 04:25:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80b102f-6078-3119-ab6a-596dfb423343 | -10.77646 | -44.46095 | 2025-12-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38b2891c-e146-3fff-8dc3-ede5aeccff01 | -12.0414 | -44.23428 | 2025-12-16 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c630fb9c-604f-3e04-a80f-957aef842d24 | -11.84709 | -43.73611 | 2025-12-16 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8be409f2-9c99-3412-857b-22b379b458ce | -13.2627 | -41.31003 | 2025-12-16 04:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0cdae3cf-e016-3705-bf11-035e18ddedcc | -1.72529 | -47.15507 | 2025-12-16 04:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d1be1a7-474e-3afe-8dcf-6e8eb860be51 | -13.25887 | -41.30657 | 2025-12-16 04:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1e4204b2-b05e-3987-88f2-8ece22f62121 | -12.16934 | -44.3579 | 2025-12-16 04:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34c48884-8bd2-3caa-98c9-b26930074881 | -1.33826 | -45.82757 | 2025-12-16 04:25:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392ab3c3-89a5-349c-951d-23a0f29ae38d | -7.61374 | -47.04514 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdf36745-bfa5-3f63-9693-4a184f4f04cb | -10.60435 | -44.83102 | 2025-12-16 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08aebc57-ad8e-3657-9ff2-46c38d86bf2a | -15.46057 | -39.15586 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 156ea7f4-ee51-30d2-922d-5ed1d861c534 | -10.99982 | -44.34542 | 2025-12-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c2c99d-622e-356d-aa7a-ee7b0495a7b0 | -10.36304 | -48.73134 | 2025-12-16 04:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2fcda0b-e350-345e-a2fd-4cac2b1e3aa4 | -14.43743 | -44.87107 | 2025-12-16 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6283a3c9-2ff7-31dc-9048-6306e8e116af | -3.15303 | -43.0204 | 2025-12-16 04:25:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 222fc888-4f4e-34df-b21b-ca6f8c6ee5b2 | -2.66973 | -46.89104 | 2025-12-16 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d19c38c-2fbd-3375-afa3-67194c87b30a | -12.89707 | -43.78901 | 2025-12-16 04:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72b7d56b-637c-3fcb-8407-07ee1e6956c1 | -1.16444 | -53.65956 | 2025-12-16 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64862d2f-fa1c-3821-aac0-5f2eec79da6b | -11.75855 | -44.0331 | 2025-12-16 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 846be467-3656-3529-8ff4-e66f246b18c5 | -14.438 | -44.86732 | 2025-12-16 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 840155e1-fae9-3705-970e-77373ac9b1de | -8.98861 | -45.94425 | 2025-12-16 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ce7614-2d96-300d-ad1e-de7a3c1fc2d2 | -10.95212 | -45.123 | 2025-12-16 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66c1ea10-e7e4-3810-bc2d-9857940a4ca9 | -8.42342 | -44.03451 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f931bb02-d538-36e1-b325-8d02b3ec52fc | -2.50575 | -48.03848 | 2025-12-16 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2014889d-04ef-3406-a469-ad725565cf0b | -8.4094 | -44.03602 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be799b3b-0560-3a51-a918-028453fc50fd | -2.03254 | -46.31434 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6660ed8a-349b-3491-8c93-189e5d88aea8 | -11.14838 | -43.32924 | 2025-12-16 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03df96ee-ed69-3c73-ac32-814209445456 | -1.67415 | -45.80552 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ddb6347-52d1-3212-827e-ca51b8d49c67 | -9.83354 | -44.72806 | 2025-12-16 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c7f94ff-1056-3c33-967f-dc505a40147d | -14.44483 | -44.86843 | 2025-12-16 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0625c927-cf21-30ca-b475-ddfafb4ab002 | -8.98475 | -45.9256 | 2025-12-16 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2eb88291-af24-3bd4-b2c0-a829b7eeaf3c | -3.24754 | -45.3568 | 2025-12-16 04:25:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0b26d53-a310-37da-9748-d5b6624cd1fc | -1.16504 | -53.65573 | 2025-12-16 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c94a4ad-7eb6-32f1-9a28-7dc2da20adab | -8.06552 | -43.14312 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a911036-1a45-3a71-8032-485d9b47e724 | -8.07183 | -43.14796 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dda9233a-600d-3e72-9f51-607e21f65c59 | -3.12618 | -45.48819 | 2025-12-16 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b1b178c-0b13-31eb-ac93-6650b460506d | -3.19114 | -43.44517 | 2025-12-16 04:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aaed1cd5-9fd1-3181-929a-79d7940331c6 | -2.50351 | -48.04085 | 2025-12-16 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3064fde0-9798-30d3-8303-c1885b98474f | -10.76812 | -44.9378 | 2025-12-16 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e10ef57-959c-3890-b60b-cf7a96fbf1d9 | -8.4195 | -44.03758 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52e4fd4c-5efc-36ca-a5ea-54f4f4864bb2 | -1.3354 | -45.82326 | 2025-12-16 04:25:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6213c6c2-b446-39f8-b3cd-751ceea556cc | -10.03034 | -48.1246 | 2025-12-16 04:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a205d92-a2ac-366e-85f9-59cb9ee7d5a4 | -1.67476 | -45.80176 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 561d5f5e-7b5a-3411-836c-450db5fb0348 | -14.44141 | -44.86787 | 2025-12-16 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e26a8ecf-aca6-3bf5-932c-316dd3379cf1 | -23.6079 | -48.34655 | 2025-12-16 04:29:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ee3a3c8-f15a-3dcb-8ce1-1344f7bde4ea | -23.5212 | -46.97383 | 2025-12-16 04:29:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bad129ed-df41-3478-98a3-08655143f568 | -2.78814 | -51.40842 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b30f89-60b0-3c35-8994-9c31be055379 | -1.33173 | -45.82269 | 2025-12-16 04:44:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 412489b7-f772-37e9-959f-710108232abc | -1.34388 | -46.56247 | 2025-12-16 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e001d0-e865-394a-845a-b50a982532a9 | -2.9666 | -41.58247 | 2025-12-16 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da307e0f-777f-38a0-b8ae-4eacad36216b | 0.67409 | -50.65856 | 2025-12-16 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e08645ca-f849-38f1-9017-c0ae411c0929 | -2.34475 | -48.42263 | 2025-12-16 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709ff54c-6900-309d-9406-d38966e9587d | -1.67237 | -45.79977 | 2025-12-16 04:44:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04b17db4-d9bc-39c7-ad80-a233e4526f35 | -2.48621 | -49.31554 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4bcfb67-bc74-3b20-8137-778f31987c8e | -1.60646 | -45.89618 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd18d587-0599-31af-92c7-73e72d389663 | -2.8119 | -52.38924 | 2025-12-16 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71afd569-d781-3096-a2fc-0f0b6d0f42f4 | -1.84592 | -46.39584 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 255750e7-b448-3430-87be-c2f88f7c5d08 | -0.8517 | -47.57461 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28a17e41-da5d-3016-8f95-f07a185f3f13 | -1.85035 | -46.39197 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1a3f4c02-884b-3c1e-9e93-9383d5150167 | -2.49009 | -49.31256 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d37fccf1-e8c1-344b-b44c-a71f93187182 | -2.28492 | -55.547 | 2025-12-16 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25288dcc-17ef-3ac5-bec6-761c0ea4f950 | -3.15282 | -48.13865 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b5d8b5b-73f6-358c-865e-6d4cbf7b383f | -2.96138 | -41.58165 | 2025-12-16 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2a2f005-d441-3f88-88b8-06504e69a287 | -1.60575 | -45.90086 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e71e64e9-1610-3150-b813-e2687d5ce485 | -3.18052 | -48.02945 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d1448a38-8b1f-31fb-b970-2d77d218ecb6 | -1.60192 | -45.90029 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b569443b-682f-3270-94ca-4a032e2ab424 | -3.43003 | -42.34385 | 2025-12-16 04:44:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b051e8f3-1dfb-3a80-bccd-5506f520c68c | -3.05282 | -48.46529 | 2025-12-16 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d99f79a2-c203-3ad2-b9cd-2f16de0d26dc | -1.1332 | -47.1655 | 2025-12-16 04:44:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6783b329-fdf6-30d3-a0f3-39d74fcd96fb | -3.42959 | -42.34672 | 2025-12-16 04:44:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
