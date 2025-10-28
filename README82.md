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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b283b9b7-02b8-3945-a9bc-a8c2de0656e2 | -13.21481 | -47.09851 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bade4b19-0737-35d8-b2ea-8810f9102a97 | -9.53633 | -46.9765 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da465e3-f243-3527-ae83-1e1520d8e90c | -7.90033 | -45.68948 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fd35ed4-eadf-3510-8647-1a75866d4d95 | -7.80589 | -46.46139 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b8cfe29-ee03-3e01-ad97-a9257862245b | -7.97685 | -46.74217 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4401ad2-200b-361c-8faf-01d1420f72e3 | -8.63344 | -44.80054 | 2025-10-28 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06eeb1f8-1b7a-3f60-82d0-a7c7a9c8b387 | -7.78509 | -46.44325 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5716fcab-d5bc-310d-94e3-3e4145fcf437 | -8.70355 | -47.98679 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c05e840d-b00b-34d8-9300-05a1cdc73bb6 | -13.24181 | -47.06483 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd263dc-16ae-378b-abbf-4d6ce54b523a | -12.55355 | -44.93711 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e3ed8ab-2828-34ab-afa9-325ea4cb370b | -7.97053 | -46.74851 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae826714-23aa-347d-b677-db83caea5152 | -9.97854 | -47.15748 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8cd6020-794f-38ad-9e68-f7bfb26be489 | -10.88512 | -48.37853 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ca06545-ad29-3f9b-9ef0-44bb772c65b3 | -7.80635 | -46.45796 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8986144f-3be8-3448-bb9e-d7b3276704c2 | -10.93023 | -47.60935 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e6f2fb7-bed1-37ad-954f-5950e08b20bf | -10.58114 | -49.80761 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6497db6-dca5-3529-88f5-945ae29c74e7 | -7.89236 | -45.70485 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1670b22-b90b-3784-b705-160fd200f5f7 | -7.98226 | -46.74273 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ccbaa39-140d-39c5-bbd7-809e0da5426b | -8.17381 | -47.30922 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91c5c6cd-33d3-3ce8-9c7b-878e42d312be | -13.35841 | -47.3943 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f01976e-94cc-37be-978e-aabaf1ae0f59 | -10.52414 | -47.73361 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34d2fd84-e680-3683-b8bd-683ab292a67b | -7.26316 | -45.01144 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67303363-d928-3cb4-afc6-831252957f0e | -13.3642 | -47.39302 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 554e64be-1497-3d96-8054-5d6094a83db6 | -10.88438 | -48.38434 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c6a6476-ed31-36fc-bea0-f44616435e44 | -7.97325 | -46.30016 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f88b9a8-fff8-396d-8d95-3af611ca6747 | -5.6161 | -51.78512 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd5d679-79e9-3dfb-9b42-6c8221fda067 | -10.56877 | -49.79643 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be15ee2e-c47b-34e9-8313-ade8952922c1 | -7.44978 | -47.16136 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a78205-c7ef-3c75-8845-0eba45505b69 | -12.97562 | -47.92952 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc2c3e0-2f3e-3617-abd7-3f8d660f00a0 | -10.5619 | -49.80326 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ca540b1-7468-3c59-876d-392b822b6f47 | -7.25602 | -44.99914 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 671d51a8-cd94-3b88-9e78-accb2507b757 | -7.31502 | -47.20947 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b008058-e1a6-3034-94bd-c1330a82d74a | -10.60236 | -46.62075 | 2025-10-28 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83b032db-b00f-33bb-87b2-4cd529d359b8 | -9.37182 | -50.81202 | 2025-10-28 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb6dd57-0d31-31af-a3aa-f1bfdd83d1fd | -12.16242 | -46.56664 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83fcd5ad-9109-32f3-9d3b-5deda4bdcae3 | -12.20515 | -46.50868 | 2025-10-28 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 230e4c70-9171-31c0-83eb-cdf002af250f | -12.07731 | -46.39503 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8406b6e-87f3-36c8-86d8-85540c9c7054 | -7.60142 | -43.58541 | 2025-10-28 05:04:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6c078c1-fb72-3537-bb14-cd1131c91763 | -7.97368 | -46.72451 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49b45683-192d-3f94-86a4-6be8caba6f8e | -7.94325 | -45.50314 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c5dafd9-cbc3-314f-8ad1-8c278134f154 | -7.27706 | -46.90244 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e71819b-6348-31e3-94e1-a9619bc203f8 | -7.95274 | -45.5215 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 197b73ba-e02f-3d57-aac7-e89c13bd8318 | -6.08972 | -53.50146 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ac4533-0163-3e39-ac7d-e8edaacc5022 | -8.55966 | -47.73391 | 2025-10-28 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f77c9cae-c04e-3f4f-a756-5aa6c39f6ab7 | -8.63863 | -45.29298 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b839e11a-2b97-301d-962e-9758fa76690d | -7.81591 | -46.46992 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e20a746a-f6b6-3448-91b3-83c59892253f | -7.94369 | -45.54527 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2c8900c-7bb8-3bd5-a4fe-934c2808313b | -7.89293 | -45.7087 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52344447-ee27-3c59-ae6e-6bd58fdfdd70 | -12.18869 | -47.02333 | 2025-10-28 05:04:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8121a46c-12a2-37fd-95e4-a3d65a2ee0ca | -7.94584 | -45.48331 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25f068b7-5772-37ed-ac35-c2e34c6edd2d | -7.83036 | -46.40335 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab05eb06-9f6b-3440-bf33-e6eceb92f460 | -7.98456 | -46.74566 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d638fa1-ce45-37d3-b92a-b046e78a8a01 | -10.56643 | -49.80388 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c49eea87-e24a-3d8c-8faa-dd0c7bd2834d | -9.88177 | -44.88976 | 2025-10-28 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a776f365-d786-346a-bfb6-e4d6255d358b | -13.56692 | -48.54903 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8288f928-819c-3dda-b6b8-c1a5c9ba9a26 | -12.65516 | -52.62447 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8ffbc62-562b-38d4-a772-8e40fd5c2530 | -7.96643 | -46.75761 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91792a76-ee7c-3d61-b2d1-c839e4e52d61 | -13.61934 | -47.02649 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46155b92-c883-329d-a07c-effec36c74c7 | -10.95236 | -50.24702 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1483420a-adca-3f9a-bec9-90d5558c4db2 | -7.38488 | -45.1254 | 2025-10-28 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a00741c-55e8-3647-9a7c-097034cac594 | -10.0262 | -47.17042 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 988cbfef-6692-303e-8327-c82d076a0989 | -12.09122 | -45.67845 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d2b0c3b-53af-3293-b855-2dba5cc63d9e | -10.9723 | -47.82014 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2351e901-845e-3764-803e-c0e4f44eeb4d | -7.99816 | -46.19914 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60530c0b-755b-390f-905d-876c885193ee | -13.22556 | -47.10453 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 814db533-4c80-3633-b946-2e5ff400fd11 | -9.01145 | -43.97606 | 2025-10-28 05:04:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb3a14c8-a704-3080-8136-3335c14564ed | -10.56239 | -49.80973 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1741c74-6a36-3da3-b254-1e1d9e0603f6 | -8.70572 | -44.41885 | 2025-10-28 05:04:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b0bf0f-c412-3506-ab28-b32b0bba04fb | -9.4654 | -46.87095 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0970f40c-6882-35f5-bcd1-2482d5cb56c9 | -13.2529 | -47.96529 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5c9ff76-8549-3f02-8666-c829b4722f35 | -7.96703 | -45.45811 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffcec94a-94cf-3f71-92b9-3f62ea43eae5 | -10.36082 | -47.14646 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d06483eb-7a65-3046-8b5e-764a567d1909 | -7.89348 | -45.6966 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2454da70-7ff2-37d6-bbc9-283eab257e26 | -8.07914 | -45.96024 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e06c80bb-5dba-3206-93df-c14892da9676 | -7.94272 | -45.50727 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 838843e2-8f9c-3af3-891a-2300068799da | -10.3635 | -47.16799 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d05eaae-2bf3-3e06-9b01-eea80409d7f0 | -11.28763 | -45.51867 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62a90938-4d4f-375c-97d8-975109abfca1 | -10.67794 | -47.27245 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eba29e0c-0215-364c-b8c7-f8ba21080ad1 | -7.81342 | -46.4404 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72f36a5a-44dc-3ce1-882a-4a7d767b458c | -6.06445 | -49.82767 | 2025-10-28 05:04:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b7d795-d4f5-3ed4-9c40-77c8bbea5d4c | -9.54091 | -46.97039 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4252abea-3745-3ecf-b40b-4b3661cb440f | -10.95708 | -50.27894 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3df62f1-ae72-352c-97f1-73468e365653 | -10.56124 | -49.7748 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0e216bfd-fab8-3c05-9e73-c7f6621f62e1 | -7.97188 | -46.7382 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6f8390f-f9a0-3958-bc18-5f87741986ea | -7.62132 | -46.69627 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6edc4e8-140d-3fd2-bb82-90b1cee12f96 | -7.31374 | -44.1117 | 2025-10-28 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 816a239e-72f6-3ba3-a35d-c6aaf9fb3a7c | -7.47053 | -47.16452 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e1e344-a3c9-36ee-9396-7a90fe467a26 | -8.1565 | -47.00748 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c00e977-4d5c-3c71-b44c-95021c0cf4f4 | -13.22475 | -47.11135 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741a2cda-d14a-3e48-8abe-4ec605e964cf | -7.37144 | -47.79375 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e47a73ee-f065-304c-911a-225a3d0325de | -11.80065 | -52.49857 | 2025-10-28 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea68a54b-49ba-3241-b073-109ef69261e6 | -10.03339 | -47.15748 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97764328-8f28-3f06-be8f-41ebb067609e | -7.9522 | -45.52561 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2e90dc48-169f-3f43-ab7f-07c7d89d3746 | -10.67646 | -47.26453 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06329fe3-0a8f-338b-a0e2-40a9a28718ed | -12.07706 | -46.39624 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bead846-6c21-3d52-9170-24bccd4ead0f | -10.56815 | -49.80109 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87660389-2333-384c-86ab-977ad5a5d7db | -9.21755 | -46.35164 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3cdb71f-9553-3bcb-85c2-5283e648ed84 | -8.10592 | -55.07927 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd721224-a8d1-3a33-b8c4-76ba5650d510 | -13.57976 | -48.52985 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf007daf-d901-3f04-9c31-7a3e64e34783 | -10.95267 | -50.27832 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README83.md)
