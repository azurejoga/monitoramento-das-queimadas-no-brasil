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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5850dc-d590-39f8-8a87-39f978f274c2 | -11.55273 | -46.36219 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9020aa94-f7d8-3064-81b2-76644b8337a8 | -10.97836 | -46.90013 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0aad313-61e9-32fa-bb06-ff91bc4fc665 | -13.33475 | -40.34179 | 2025-08-29 03:49:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5ee6fe8-a68b-3806-9856-19e16d12a8e2 | -14.30923 | -51.89613 | 2025-08-29 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e22e9d43-bc20-3adc-891d-c17785298f25 | -5.61668 | -45.00539 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b29e4654-5b45-3af9-9f27-ec2ffbdc6984 | -6.13645 | -44.42538 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cf0afda-0124-3ecb-876e-85ae69815183 | -6.08587 | -43.99887 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22127b2a-0d0a-3ea3-afff-c055caf2d66d | -13.99208 | -46.33084 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fe7ebc5-930f-3843-b894-c758b1a5e7c7 | -12.08989 | -44.7284 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5902e098-304c-300a-8438-ec45ee32c422 | -11.16374 | -47.15354 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a46000f5-60c7-360a-a76f-b7ad4f6dbe0c | -11.08304 | -44.75373 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 649c88e0-00b2-3a71-bc02-c111ed6d7900 | -13.56214 | -46.90276 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64611fb3-9c6c-3244-af9c-bc8867dfdd47 | -13.3669 | -42.50453 | 2025-08-29 03:49:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0319c3ee-6d25-34d5-8e1c-ac395c75f525 | -10.69635 | -47.07555 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c8e42f8-50d5-3c55-8f7c-9a3a6fb334ee | -11.57534 | -46.37929 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68cc6dde-75e3-3465-8a21-0bc68d088f11 | -5.78293 | -42.60651 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53fe07a4-f7f8-3fbb-9962-ecb9cc2da24e | -6.48969 | -43.53239 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 620a5a44-b991-3819-a514-92d571eb4d9b | -17.85217 | -41.54411 | 2025-08-29 03:49:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 570f8455-2187-3372-811a-82215dbca000 | -6.30097 | -42.48975 | 2025-08-29 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cab594d5-5f26-3053-ae56-b765074d8765 | -6.20393 | -43.00689 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a68fb253-8b21-3a3b-80b4-1f64b2af3e72 | -6.12531 | -43.30447 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c8e47bc-25dd-3747-9998-a258516976b0 | -13.63841 | -48.21077 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf31dc6a-5cea-30c4-b0b2-610e8c052e0f | -13.52863 | -46.94215 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72ee4ba1-025c-3044-9755-22351ad39f44 | -15.82485 | -45.76748 | 2025-08-29 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58d627cc-f2e1-39e5-9661-9778d54b5d7b | -11.29971 | -43.54562 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5b52693-d588-3f67-b620-660962d11420 | -11.12136 | -45.122 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1b449e7-ed32-33d3-b235-52064ace65c1 | -5.78721 | -42.60725 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a5cf7aae-8bc3-33e4-9b17-9a19c57130b7 | -11.09177 | -45.12698 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05135eaf-98eb-31bb-939a-c5d15d2aa326 | -15.82399 | -45.77199 | 2025-08-29 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6d3d8c-8d0c-304b-a65e-af130ef67d2b | -5.17539 | -46.07451 | 2025-08-29 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74a81a2f-f55f-355d-913f-6ebe7b512558 | -10.0203 | -51.1175 | 2025-08-29 03:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8abb311a-93b2-3e39-bbd0-e8d28d9e49a9 | -14.902 | -46.45562 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e2687d5-8059-3ef8-a732-751c25f20426 | -11.29209 | -43.54031 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4165c676-95d5-3f63-ab54-6c8348fc4b64 | -17.48308 | -43.33488 | 2025-08-29 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa1ba3b7-73d8-3dac-b3b0-0fa67eb9d340 | -12.83875 | -48.10344 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65a5519f-10b6-3f66-b674-8a47177393b7 | -5.60077 | -45.20735 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f233386-6a54-3c15-999a-29c454654ae1 | -6.04516 | -44.47271 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92d5f26d-2f08-370c-aa73-fb9f9d2dd334 | -11.55513 | -46.37674 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12557635-3df8-3b39-a515-8a7b76cd2a52 | -10.05905 | -46.60917 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63ad0629-c046-368b-b3ad-369b4b8c18d4 | -11.24223 | -44.97282 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9917454-a922-3cc4-b126-6f7ccd406b85 | -10.93701 | -46.86143 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c9c221c-5b49-38ec-ba7d-8fadc17a594f | -10.97596 | -46.91299 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f194a6d0-3738-36e5-825b-05ec6c8f1550 | -5.61618 | -45.00838 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c4b2ee89-97e3-3ce3-be0a-421b2d7af1cc | -5.85786 | -42.9414 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8952f8bf-b4b2-315b-bb8c-1b4651bbea0b | -6.20399 | -43.32711 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1db1ff9-3885-361c-a845-914177d71271 | -11.34115 | -43.52947 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea9a211b-b2f3-30a4-a35d-d97f443c97d2 | -11.92791 | -46.69619 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f82ca6c5-f8ab-36d3-9bea-bab140a6fd72 | -13.50474 | -46.85213 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c94494c-1d1a-33c2-9a59-281453ffcc86 | -4.10782 | -48.01477 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba04b411-de8a-306a-8967-e0004d11afe9 | -12.9118 | -48.13785 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48dfb081-f7ab-3655-8bd0-b3bf43d03a6e | -12.81586 | -48.19114 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f5d6750-6ac8-30bc-857f-68c673cec71a | -13.55137 | -46.93188 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7db5197-12d7-35fa-bc2e-f98ee1976bd7 | -12.86217 | -48.10156 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc65406a-ca54-31f9-98a3-b7ca6d1b0a7a | -13.40544 | -46.99139 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5f3a131-c0f6-3401-b6a3-aca094d63ab9 | -17.4868 | -43.33562 | 2025-08-29 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fb9465b-0b33-3a3b-8f9e-220fbc7900d1 | -6.48347 | -44.40662 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd8ec62-18af-30c7-98ad-17c7032abb1c | -10.01888 | -48.08022 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b2753f1-1709-3578-8a40-93479548558a | -6.26627 | -43.82003 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d32cf46-2017-3009-9d4c-2ddca9561f1d | -10.03165 | -48.07543 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0ffbf95-c574-3bb3-98dd-c1f559909361 | -11.57516 | -49.51457 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 759c598a-d3bb-33c9-92a2-8cc23f950bb3 | -16.30388 | -42.04102 | 2025-08-29 03:49:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a06160b4-4bce-3a03-b7d2-f32ebd20a7b7 | -10.02098 | -48.06903 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f10d35b-9512-3130-9210-c75e03219625 | -6.43108 | -44.56966 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03357e0a-3cc3-30c3-8fd6-a6aaac333a7d | -5.80117 | -42.57587 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| de1d102c-7a1b-302e-acb1-bbe08ef49157 | -13.56545 | -46.91251 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d3677e-9807-3bb8-a6a5-4ea7ad2ea327 | -11.31564 | -43.5524 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cd604aa-b788-3855-9ffc-ac1d56cb40c2 | -12.68529 | -48.16074 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92266bb5-af83-3fe6-8b21-7e57a1f76c77 | -14.24101 | -48.06069 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f751c8d9-a6d3-3718-820a-0966a63c895d | -12.8773 | -48.13997 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d068e216-4800-3329-9e90-fedc30f2ecf1 | -11.32192 | -43.56532 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6823bec6-367f-36d4-adb2-06d5612031ba | -5.86731 | -38.28164 | 2025-08-29 03:49:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6fb6801e-18cb-388e-841e-f75ac1bc0c73 | -5.86819 | -42.96363 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bb9fc143-222e-34b9-9a51-cff04fbbac27 | -5.18082 | -46.07563 | 2025-08-29 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5cf857a8-429c-32d4-8525-27129da31385 | -13.42229 | -46.95816 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8666b0c-0ebc-3ca5-851f-b96a5dc40ca3 | -12.57049 | -43.78469 | 2025-08-29 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 688b34ef-02fe-3f4f-a151-031e26f75e00 | -5.61633 | -45.00008 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5c9dc78f-2184-3a94-a1a5-ed706e5a8479 | -11.08991 | -44.74766 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34d3ae19-3369-3c98-94ff-69daa0cf0ec8 | -7.2604 | -39.67327 | 2025-08-29 03:49:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddcff587-c98d-382e-895d-0c13ee7c5d80 | -10.94353 | -46.85551 | 2025-08-29 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6758200-cb2d-305c-93c8-9dbe338bf043 | -11.56993 | -46.38054 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96b648ad-bedc-3084-ac80-7efc79754686 | -11.07889 | -44.77726 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aced765-e7e1-30cd-a07f-2ffc9732f503 | -14.33695 | -48.6545 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07fc7244-a82d-36a4-85b5-46a0c1052030 | -11.6195 | -47.31396 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01aa53c9-4992-37f7-a3d7-5a4be7726033 | -13.55084 | -46.93465 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb97eade-1468-36d3-9c99-678f66cd5865 | -9.67398 | -48.325 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41c449ca-8ca0-3b51-bbcd-0562758cc712 | -4.06614 | -47.95687 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb4165b-1e85-3752-9efa-febd5d12def5 | -12.94684 | -46.14257 | 2025-08-29 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31d4d04b-c4df-3308-8014-73f856646d4e | -13.54479 | -46.88541 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2cb1cd96-0a12-3206-b92c-aafbf13c8dc8 | -13.43228 | -46.96035 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7e59cd4f-7046-3501-8f81-15b16ab13be9 | -6.19221 | -44.01029 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9652441b-74d6-3519-8804-62bf53c93c1c | -13.49008 | -46.84775 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8489a3f6-b7af-350c-82f5-5b5fe02583fb | -13.1836 | -45.278 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36755850-0bc8-342a-8287-911ee45d2275 | -11.56015 | -46.37755 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bf40628-6350-3420-bbed-e0491fedf234 | -12.70466 | -48.14913 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e4899ae-364b-3ef7-bc07-aef992a8f48f | -12.83981 | -48.15694 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f8e55bd-49fb-3078-bbc8-51bbf55bc8a6 | -13.41169 | -46.9861 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4da06ba-ab80-3001-83e0-89be70b04b47 | -6.48248 | -44.09796 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69751938-6ef1-3ba5-a041-dbfd1ff22902 | -6.54131 | -43.92138 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| fb4c4963-756a-3c51-888a-8b002b7e9fe8 | -6.49751 | -43.40488 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ba06aea-61ce-3b8e-864f-0279560af73a | -5.97263 | -43.36048 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README36.md)
