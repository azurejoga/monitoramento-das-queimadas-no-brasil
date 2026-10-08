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

## Dados Diários - Página 266

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d17b7d6c-019f-31f9-8878-739ef9a23e79 | -12.22704 | -44.76298 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ae1ee087-012d-397c-8ee3-c82869f769e5 | -13.64646 | -47.67475 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4a400df6-374c-3c34-9e8a-bbd80dc16b5c | -9.78225 | -44.78328 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6bdc23f-428e-3f42-92c0-bb049f6af79e | -11.63888 | -43.59386 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| adb56ccb-d8f4-30c6-b06b-66f39f7b736c | -9.77719 | -47.82092 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c0e5fbf-4a31-358a-8d04-f11d1012447d | -11.83909 | -43.52816 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 57705160-b5dd-34bd-ba71-b5a861c29f68 | -11.32176 | -46.65858 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| da442693-4970-338c-9242-6297e1534287 | -12.83698 | -44.62973 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 65e5c36b-5a1c-32d2-8dc0-7ac07d07d065 | -13.74309 | -43.51794 | 2026-10-08 16:18:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e25a983b-afab-36e6-8c73-c17ab414f808 | -11.76467 | -45.49203 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| a62daf59-59a2-3fc7-a864-154e045b52a4 | -11.2515 | -46.26059 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 99488ffe-afe3-3030-8554-36adf535ff77 | -8.58109 | -45.68771 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ffb77c86-6c77-3181-8193-87196a8a2ef7 | -10.50508 | -47.31556 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ffd75eea-1978-32e5-8258-9da96dfde42a | -12.51511 | -41.94234 | 2026-10-08 16:18:00 | NPP-375 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 417e1711-a132-3227-a765-85be7dd752d2 | -13.61358 | -48.19409 | 2026-10-08 16:18:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a8330ba-726a-3223-9c04-44c013c85cb0 | -11.85907 | -47.39058 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3bf95b2f-1515-3f8b-b7e9-ebe69a4918aa | -10.68973 | -47.83004 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 558e0866-29e8-3be4-9ee1-e6fb05f62761 | -11.7392 | -43.64597 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| a8d4b9fe-cf7b-3fb3-a0ed-1890de5c1fba | -9.8786 | -44.86581 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 440.1 |
| a72927e5-b89c-331c-90b0-befb6e07ba69 | -8.9386 | -45.14559 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 42f82d9b-48c5-3fa1-8a95-94fcfd9d8c43 | -13.59395 | -48.59082 | 2026-10-08 16:18:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 427dfd4a-2599-3fe9-9f6d-e028de4c6b16 | -8.95559 | -45.14429 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 75800b90-847a-35ef-8334-9c5db5a7c1e9 | -9.3442 | -37.20898 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c2d127f6-8f41-314c-b462-6857b26fe79d | -11.39144 | -46.71662 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49e0ce29-a27a-3f8d-9117-303fe13a2f6d | -11.2237 | -45.26406 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ab3b7fec-d46c-3b12-afe9-579a69a13077 | -10.44835 | -47.29011 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8a511d72-09e6-3070-be62-3a0f979e4caf | -10.60224 | -43.83986 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b72208d-76d4-3f51-828f-6a014cee5497 | -14.37293 | -47.07354 | 2026-10-08 16:18:00 | NPP-375 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0436c615-9953-365c-8c8d-dadb11db24cd | -8.2926 | -45.72329 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fb1ee9c5-1562-3e8c-bf14-c18cf4cd17ab | -8.60111 | -44.86885 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd9d4a00-d50c-3758-be3f-36804b3e20b5 | -11.35281 | -46.69922 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afe3f185-4070-32a9-956a-ba28996d9613 | -8.61172 | -45.6373 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f9ec8cf3-f07c-3351-a046-3e048720c6d4 | -11.4022 | -46.70323 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7f26ff5e-c2f6-3c52-982a-52b0fadb15fc | -11.40123 | -44.96105 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed0a30d9-cd7a-34c1-94c7-7be571ea52d2 | -13.58497 | -43.16976 | 2026-10-08 16:18:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b6053aa3-67c0-3601-b0e4-cf09691610bf | -11.07685 | -44.01371 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 43911164-cfd5-3b28-b69a-59cc85738834 | -13.12532 | -46.36418 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7a149532-f2d2-3a09-8edb-2fa8b670235c | -11.76056 | -45.49737 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8b021454-2dc5-34c4-9979-f8d65a4b0b28 | -10.67138 | -47.81942 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 134d123d-fd4f-3ded-aa70-3c5521d8a863 | -11.20282 | -45.21377 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| be8b8429-577d-3164-b10e-0767d7728f8d | -13.97799 | -44.83749 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c9809bf4-858a-3c1a-9b4a-cbbe93c0db31 | -13.64345 | -47.67439 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc2851f8-b27f-309e-8972-48707d6c5d40 | -8.60773 | -45.6422 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7387d46c-704f-3eb9-9341-555c980d6a0f | -11.21584 | -44.85926 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0aca7200-f88a-3704-96f6-c26e3059dc1a | -10.48127 | -47.21436 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 639cee78-5037-34c1-bd1c-3a465a856257 | -8.94104 | -45.16297 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eabdbb8c-7b87-3373-aa87-781598cd9169 | -10.4583 | -47.20109 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edfa4b30-96b5-3f8f-b503-bc690490fc18 | -8.28661 | -45.7122 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 03916618-49b4-3ce2-9d3e-163e00a6a05f | -12.1922 | -44.64447 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d55dc8f2-e51b-3a8d-a492-13ad2eaa00ee | -11.0885 | -44.00403 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 8fa6da95-1ca5-3548-b9a1-92666f378e8e | -11.84114 | -47.3335 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| accc568c-48ae-30a9-8aaa-523dc1e57819 | -9.13274 | -45.83567 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 36c133ed-8cf3-3287-8794-84ae570250a0 | -13.14275 | -46.33699 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3de82cbd-db7d-3f4f-a1ed-6cde7231b28b | -9.73995 | -42.24473 | 2026-10-08 16:18:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a79e00dc-4c38-3534-92d6-bf08dbb497ad | -9.07802 | -45.12584 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| f3a6278b-c9a6-3bcf-beaf-0649204e3d87 | -9.84243 | -47.84675 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bdadb46f-0dca-3064-8135-03db7684e089 | -11.35195 | -43.14658 | 2026-10-08 16:18:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 37b733d8-49f4-35bf-98e3-bc11e08a8f3c | -11.07896 | -44.02956 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| b9e14db0-e037-36b1-9ef9-63bcfe3f153b | -13.11907 | -46.35562 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2dac52cb-ab20-3917-a8be-5b2cdd1f733b | -9.39916 | -45.8934 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0899ce93-e563-3ebb-a9f8-c2380ca20f6a | -10.82225 | -47.33766 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66a00eda-7a25-322c-b633-1a8df9d41324 | -8.18648 | -45.76269 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d4e83877-2b57-3e60-b582-f931db6af9cf | -11.24305 | -46.27357 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d1c885a6-fbdd-3613-b5ae-0b00016fb292 | -13.88181 | -47.97238 | 2026-10-08 16:18:00 | NPP-375 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 47f8d52a-12e1-317d-b959-31e41307251f | -8.75118 | -46.84382 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 44215883-92ed-3f0f-869f-bf8a45c39b1c | -11.08585 | -44.01651 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1ed80f84-0bfd-3b21-8310-e262c5382255 | -9.37006 | -45.935 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 19c437bc-76fb-3696-a1f1-280ad7bcb0b9 | -9.8272 | -47.46738 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 434da978-51d6-3d3f-8c37-ecdc856cb31e | -11.72562 | -43.6399 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 98c5049f-acad-3c9a-bd8e-61466600b14f | -13.34247 | -43.96507 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c871e736-6712-31e5-9376-14e086dde58a | -9.84919 | -47.8569 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4df70dec-2a69-3cdf-a365-0bd941f99f71 | -9.26252 | -45.63184 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39bb9d9c-35c9-349a-b1fd-f2cbb71bfd6c | -9.73493 | -46.9503 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9a99797b-cc4c-3897-9caf-bc07c1b7bebd | -11.59343 | -43.67368 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 293ff333-9a9c-3b9b-9387-05391c54dbc1 | -9.73196 | -46.94971 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1ddc580e-1c94-39a9-a04f-f7aefc0e0b56 | -10.95039 | -45.38445 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 81e1c518-3b68-3be4-b848-5e94bdc6540a | -11.40041 | -46.70555 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6db87324-9de4-3fb0-a504-50ae97937505 | -13.34683 | -43.96449 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 910b1aaa-821e-388e-a0d8-aa6351df78d7 | -11.59869 | -43.64978 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f789cb54-58b5-3fc1-b85f-f4b5e2fce51d | -8.28206 | -45.71291 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 96cb00c0-2110-35a6-b793-76d8d418d269 | -11.77193 | -45.58405 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 046aeca5-98fc-3cc2-b6c5-5207bd113165 | -9.88739 | -44.86441 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 682bd9df-499e-3d00-98ac-0e1feb9b1218 | -11.40905 | -46.69212 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 052d89a5-c31c-3eca-8db2-3101a9739101 | -13.69863 | -49.08492 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 025a3296-b3a2-3062-8baf-ae6567f0a4a3 | -11.21983 | -39.07497 | 2026-10-08 16:18:00 | NPP-375 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 8db2f5d0-c45a-31bd-b640-f3dcf76c611d | -12.61294 | -42.17039 | 2026-10-08 16:18:00 | NPP-375 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 10413e8f-2216-3569-b0ea-561f95cce23b | -11.40317 | -46.68686 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4db9a8b4-e668-3320-ba4a-52fa0181c12d | -11.76654 | -45.54295 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ac8a4574-f2c2-3ce7-8560-4118ff380d9c | -11.58191 | -43.68285 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 3070c959-3155-37ad-8221-7892e4b7352a | -8.68814 | -45.27802 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 63b78378-7ce5-3f83-b34a-ba1897a2ea00 | -8.84325 | -45.45857 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b7c60364-afbb-33db-97c0-8cb415824087 | -13.12456 | -46.35795 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| bb389503-9ce0-3ad4-a565-5efa39b3f814 | -10.4467 | -47.27715 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3600e8d0-73ab-33aa-82ce-5250999ceb67 | -11.26902 | -45.19172 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d0515f8-befa-38bc-9258-565c19616e54 | -13.70691 | -49.10394 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78c55c2c-2239-3019-b881-7fae09138845 | -11.58458 | -43.6711 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 053a28f3-ff0c-3cbb-9550-a7799d4b7bd3 | -9.89178 | -44.80368 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 0ef387ac-29d9-3b98-abe0-80bc5fb64497 | -8.94364 | -45.14928 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 72d2dbcb-1d0f-3541-ac8e-683987a58b0e | -8.95733 | -45.15735 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 6e9e3a0a-0cfd-3a5c-9518-4e0c1ea4f629 | -12.19483 | -48.41756 | 2026-10-08 16:18:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README267.md)
