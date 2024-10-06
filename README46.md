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
| 0d4cbcae-6f28-30a9-9967-e19ed0a3c1ce | -3.8039 | -41.60049 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4ec3d43-17fc-355e-b012-3bb32ba2aa51 | -3.8016 | -41.59067 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a65fefa8-dff4-3c09-b65e-82727bc8efc6 | -3.80086 | -41.59525 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cf41d5e9-1147-3016-8fcf-5398a815d12d | -3.80011 | -41.59985 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 60c20054-c4e5-3bbb-ba86-b26e1a949a1b | -3.79856 | -41.58547 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e09c9bed-fb2c-3976-9c15-ff142864dc4f | -3.79782 | -41.59004 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5113c1df-77da-382f-bbe8-4558dd3ed05a | -3.79708 | -41.59462 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 374a77f9-aa4d-3305-af66-f79836c79613 | -3.71763 | -41.68421 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 45b34cea-3200-32d9-9449-efb154abaec4 | -3.71382 | -41.68357 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 947cab3a-ebf1-3f94-8ee8-31d5cde6706d | -3.71001 | -41.68296 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 36d2cf43-7bc6-3ec5-a298-72f58aedffa5 | -4.04567 | -43.24505 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f31a9cf-8ddd-3454-b2c9-64a181d5813b | -4.04503 | -43.24885 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2310b4d7-2cd8-3cd0-acbe-8628fac4db53 | -4.01933 | -43.24446 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9643a209-5988-3bab-9d7f-515051383807 | -4.01871 | -43.24829 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5473a509-a4a7-38e2-984e-a1827e1fdcc5 | -4.01514 | -43.24377 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ba640b0-3982-3910-966a-8d8c3c110be0 | -4.01452 | -43.24759 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6945da5f-df1b-3b08-9f7b-0ded37d36905 | -4.01094 | -43.24308 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b24cc65e-d8eb-3279-855c-6726c02f35a6 | -4.01033 | -43.24689 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 721ff093-ced3-3a16-a9ea-dbdd332f6f19 | -4.00971 | -43.25073 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1e3c1c-1e80-3405-a9b7-b0c57278dfab | -4.00614 | -43.2462 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7502ac4-da25-34c3-848f-3590be66666d | -3.58004 | -44.06591 | 2024-10-06 03:51:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0afba81-307e-3629-9ee2-c43d293e1ea5 | -3.57833 | -44.06339 | 2024-10-06 03:51:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce68b888-0451-3ace-9d37-1c2bd51c6a6d | -3.57762 | -44.06786 | 2024-10-06 03:51:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87204d8e-00a6-3404-8ea0-47f7343e315e | -3.90761 | -44.57707 | 2024-10-06 03:51:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ec72882-0642-3d8b-b152-78e1cc6caf3c | -1.76678 | -47.18981 | 2024-10-06 03:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 807df436-e86b-3123-97d1-888a8c8d0da0 | -1.76613 | -47.19365 | 2024-10-06 03:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c9fc99a0-53a0-3376-8266-4408ae5330c4 | -1.76507 | -47.1912 | 2024-10-06 03:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 135b87e3-d8cb-38ef-aa8e-728e0a4bca5c | -1.76446 | -47.19506 | 2024-10-06 03:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d50d0fff-fe25-3419-b1c3-e57ad0c17b8c | -1.76045 | -47.19272 | 2024-10-06 03:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8511b62-9479-3181-b0f7-d56d120dd7ce | -2.72096 | -46.80982 | 2024-10-06 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cae563c-91b6-31f4-a023-7755c8f46f4a | -2.8217 | -48.60347 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a1a8389-8c00-39d0-809a-4fbe3fb18e8e | -2.82095 | -48.60806 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a1d694b3-8917-3c0c-8754-c7799264cf22 | -2.82077 | -48.60461 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d2e1742-c480-33ed-87f4-362a26ef7db3 | -2.81998 | -48.6092 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 679b7bf1-6574-34e6-a932-aff7c3eb228f | -2.81559 | -48.60234 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f049dbc8-dbad-3883-bec2-0fc1d9410dfc | -2.81483 | -48.60697 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 53ab2571-35c2-3fff-9393-6c7067d6f80e | -2.81466 | -48.60351 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 160adfb8-8ce1-3206-beae-3cc8fa1f3310 | -2.81403 | -48.68873 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 83281e58-9b7f-37ff-a270-7aad722aed7a | -2.81386 | -48.60813 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 29f0de4b-8788-3e25-8c53-7693a2dab406 | -2.8133 | -48.68499 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 006891b6-dea8-3671-a9fe-2edf3f627d9e | -2.81325 | -48.69346 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a95869a7-d7f1-3f16-9120-5b2d63f502ca | -2.8125 | -48.6897 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 47b7965e-26d6-3af9-8bdb-5763eb7fe34f | -2.81248 | -48.69817 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 30d5d522-4b59-3a16-84df-1d72a93bf51c | -2.81171 | -48.70288 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2efb44b4-3d3d-3d0d-98af-a48b111203f9 | -2.81169 | -48.6944 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 18c41a94-bc44-3b4e-b510-59996b4dc1ed | -2.81089 | -48.6991 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d5fc62c4-a90c-3ee4-babc-3f28383ecf33 | -2.81009 | -48.70379 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 936ec4c3-f589-359a-83b6-e8610af339f6 | -2.80787 | -48.68767 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 46cfe4bb-a516-33d6-9129-dd67f8678ad9 | -2.8071 | -48.69239 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 21080787-98d8-3695-aec6-0ee6a57d5047 | -2.80635 | -48.68866 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 3c8f6527-2a9f-30ba-b01a-1c954e1fc938 | -2.80633 | -48.6971 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 6e044bc6-ab9e-37ec-8144-4d011ac98a96 | -2.80555 | -48.70182 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a24e5bd-09de-3ff6-abbf-80e61c9a0a14 | -2.80554 | -48.69334 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| c2331cf5-0291-38d8-bf0c-0f52b4ed4c25 | -2.80474 | -48.69804 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 62b69c42-c5ef-35ca-a0e8-15b970e9d28f | -2.37444 | -48.60997 | 2024-10-06 03:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f6ace56-8820-3c39-b721-aee3dd76d6c0 | -2.37212 | -48.63324 | 2024-10-06 03:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46216645-f8aa-3001-a7df-19cbd54b8ba2 | -2.37133 | -48.63806 | 2024-10-06 03:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de3171a5-242d-3198-b683-b9884783b196 | -2.36746 | -48.61368 | 2024-10-06 03:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd01c9f5-4253-3377-98c2-e421cd35d466 | -2.20551 | -48.1609 | 2024-10-06 03:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2024c25-be58-3a3e-9ce1-01a86dfa183c | -3.1282 | -48.60425 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 86cbbc41-6ddc-3b6a-a83f-db836e12373f | -3.12785 | -48.60863 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5134289f-75b9-3d68-9827-4b2b4200a90e | -3.12743 | -48.60891 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fd6abbbc-bd0b-33be-a6f0-6a8bba38e895 | -3.12704 | -48.61327 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fac86d06-ff83-3a06-9d46-2b1334b34fc0 | -3.12666 | -48.61357 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6a904531-607e-3b97-8c96-fa62a7e88ac0 | -3.12624 | -48.61789 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c4fc836-3bd6-3543-a3c3-d7636edee252 | -3.12589 | -48.61819 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a78d2131-dea1-360e-8018-3044fa63ce49 | -3.12513 | -48.62278 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98fbc2c-0727-3e57-9f38-ffed15eb2266 | -3.12418 | -48.59361 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ee5d8f8-57a6-357d-aaa7-22267c194f10 | -3.12367 | -48.59383 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cb028f4-f3e5-3da5-89f7-b658b363c5a8 | -3.12338 | -48.59821 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 843f7531-e73d-3a83-96cf-43e874050cf9 | -3.1229 | -48.59845 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c442616-4a6d-3225-b161-723ff0bda2c7 | -3.12257 | -48.60287 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 22068dcc-dad4-314a-8fe8-e9f448a6dbc2 | -3.12212 | -48.60312 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 02d64939-5610-32f3-b100-9468e30e0a9d | -3.12177 | -48.60751 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5900e2f2-8894-3f6d-9a15-7e21e59b8daa | -3.12135 | -48.60777 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0dac0498-f8eb-374e-b9d6-89b59a7f707b | -3.12096 | -48.61214 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b03aaaba-30e4-3247-a49e-bf1377a1702e | -3.12058 | -48.61241 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f354b626-6545-3dc7-80d8-e8acf818c92b | -3.12016 | -48.61679 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1b5eb820-b3f4-3815-812c-2aa9248e1df7 | -3.1198 | -48.61707 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 106604e2-aeef-3321-84b4-77491da6cd67 | -3.11935 | -48.62144 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 286e7cbb-21e7-34fa-b740-f7ce2821eac8 | -3.11903 | -48.62173 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7689024a-4a36-33b6-9f46-39dd5b248dd9 | -3.11855 | -48.62601 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fbeac76-57a7-3349-b887-7cac8d28e39a | -3.11827 | -48.62631 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 194eab96-28a9-3a22-a3d1-ffdb8819c613 | -3.1181 | -48.59259 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8532edcd-95bd-382a-b07c-d853ad39820d | -3.11758 | -48.59279 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2c14643b-3b5d-3289-b9d0-863dab911979 | -3.11729 | -48.59719 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edd14e0b-cf3e-38eb-bcdf-f9892fbd6e6b | -3.11681 | -48.59742 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ebd9414f-3597-3b7c-9246-173e61afe802 | -3.11648 | -48.60186 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f541715c-2cd6-3df3-bd7a-0ff6c9bb6ce2 | -3.11603 | -48.60209 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bda3d2af-35d3-38c9-ab62-d46f3522cdfb | -3.11568 | -48.60648 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0590b12c-4ec9-316a-b9dc-4ad50d60fc19 | -3.11526 | -48.60672 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f720b31-ec2a-353c-bb1a-bfe60a518d35 | -3.11488 | -48.61107 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dc83ed7f-57ba-3cfa-a2f1-f26ddf580c67 | -3.11449 | -48.61132 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ca43b35-acde-31a0-8536-a28347ffc5e2 | -3.11407 | -48.61569 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d13b8311-1bcf-30ea-8cac-b9c445914bc3 | -3.11372 | -48.61596 | 2024-10-06 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acfdad88-0a4f-3945-a41b-81930612fd9b | -2.14086 | -48.90449 | 2024-10-06 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5be2629-92b4-3b63-96e9-04beb0022d9d | -1.04619 | -48.70243 | 2024-10-06 03:51:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8871d4c-315a-3718-92e2-6bd2a9cae511 | -1.04538 | -48.70746 | 2024-10-06 03:51:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af37932e-53ed-3f2b-b612-0390538edb67 | -1.03987 | -48.70134 | 2024-10-06 03:51:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21e5c02a-4420-3232-9172-5f9f167bd4bb | -1.03907 | -48.70632 | 2024-10-06 03:51:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
