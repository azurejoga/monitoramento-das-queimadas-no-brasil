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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2228683-378a-3442-8aa8-8433319c25bf | -9.1154 | -65.7886 | 2025-08-29 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4df3c98b-43bc-3fa8-a181-cc548747b076 | -13.5576 | -46.8972 | 2025-08-29 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 158.6 |
| aae56e03-1675-3b69-98e2-442f499329bc | -7.6033 | -42.6995 | 2025-08-29 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 3ce0332e-be2b-3d64-8024-b0be57f2e9d2 | -10.0247 | -48.08 | 2025-08-29 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 4d46fa35-30f8-3092-9616-35e5a659442a | -15.0835 | -48.1367 | 2025-08-29 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7d196e3b-84ed-347c-91f8-dc1965351df2 | -5.7156 | -45.5388 | 2025-08-29 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| da61cb31-8743-3432-94a0-c6bf873a2e5b | -10.3626 | -57.8061 | 2025-08-29 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6cae4c99-eb23-38f8-ad74-de0b8869d868 | -8.7511 | -47.3985 | 2025-08-29 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 16b0c9cf-c4c0-3a3f-8387-577e7bf6f302 | -7.6222 | -42.6975 | 2025-08-29 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 181.1 |
| e620da53-0e04-316a-a076-9a4e8a33f731 | -12.8216 | -48.1934 | 2025-08-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c3b2ea17-733f-3314-98dc-d9f98333353c | -11.3713 | -43.5394 | 2025-08-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 604c5a84-cad7-3871-b386-a8afc0d8ec25 | -7.415 | -44.283 | 2025-08-29 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 524a63b5-db4d-3b6f-97f7-1bd8aeecd498 | -9.7728 | -64.2657 | 2025-08-29 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d4748140-28fb-3dae-83f2-bfef23bc50fa | -7.9735 | -46.3854 | 2025-08-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| dd05f41b-d4f8-3a80-8090-757d2f2e47bd | -11.876 | -46.4007 | 2025-08-29 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 0bc15854-1035-3a9b-924b-b6e8be105334 | -14.3299 | -53.3108 | 2025-08-29 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f03b2f71-530e-305a-b061-5b7b4ca7f089 | -9.1338 | -65.8067 | 2025-08-29 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| bf54a266-cbf0-3aea-b1d2-65e49928cf70 | -6.1975 | -43.998 | 2025-08-29 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 4843337b-5c76-31cc-b7c3-9bb85a7b56ce | -12.9382 | -56.9856 | 2025-08-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d3e83236-5817-3c93-8360-08632a9ba848 | -12.9385 | -56.9655 | 2025-08-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d473e3f7-d5ac-3e90-b57d-c116d059bef3 | -11.3856 | -63.2653 | 2025-08-29 14:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 259be50a-cdb7-37f0-b563-c8a04458ec8c | -7.9737 | -46.363 | 2025-08-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 04901523-5a25-348d-9566-6e4cf530d9a7 | -10.8607 | -60.8191 | 2025-08-29 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| c265b03a-0138-3c61-953d-dfe727603a0a | -13.3543 | -54.38 | 2025-08-29 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 1c3d985f-5f6b-30eb-aff8-8e8adf4cd974 | -6.2741 | -43.8299 | 2025-08-29 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e6b5180a-2c6d-3f68-a527-79c068df98dc | -11.3521 | -43.5423 | 2025-08-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 9c99844a-8227-3fb2-83af-9546662f2ffe | -10.3628 | -57.7863 | 2025-08-29 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 85ef573c-d233-3b40-bd1f-04ee2938e18b | -12.822 | -48.1712 | 2025-08-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 5a791775-4c3a-3c79-93e6-efd478a22424 | -12.8413 | -48.1685 | 2025-08-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| c96561a4-fab9-35b6-86c6-065d8844fedf | -9.3238 | -56.9064 | 2025-08-29 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 967264ab-14e4-3983-9dc4-a6d69d137468 | -9.5447 | -45.8842 | 2025-08-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 72e83bf5-a567-3c7b-a6d9-3b70bdd74257 | -10.4736 | -57.9563 | 2025-08-29 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bad567de-de86-35c2-b549-db45c4a52eee | -15.6749 | -52.7552 | 2025-08-29 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 7f2d2b12-6bc3-3aaf-9290-13b83300f4b3 | -14.0328 | -44.487 | 2025-08-29 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 5aa3ba5d-fbab-38a7-b777-1e5fd8897003 | -12.6742 | -60.255 | 2025-08-29 14:20:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b23c6bab-3bce-3c44-a403-c3fa11776740 | -6.3918 | -45.2175 | 2025-08-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 287db4c3-d043-31b1-8a1b-90db9628de61 | -12.4345 | -63.9173 | 2025-08-29 14:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ff2e3f29-61f0-3cc6-ad59-0f3581ef2810 | -7.1108 | -44.587 | 2025-08-29 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3938a897-105b-3506-b962-327682b49984 | -9.1339 | -65.788 | 2025-08-29 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 7552b01d-c694-3736-a706-812969629b63 | -13.3555 | -51.7855 | 2025-08-29 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 99f4416f-b633-37da-9fef-efeb9f934853 | -8.7714 | -68.6898 | 2025-08-29 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8a7ae3e7-7909-3b67-b55c-f8fac21a34cb | -14.3296 | -53.3318 | 2025-08-29 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5c52343e-7ffa-3101-a235-c49add58c122 | -6.9867 | -59.3354 | 2025-08-29 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 51147691-798a-3838-832f-c489f783785b | -6.3916 | -45.2402 | 2025-08-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 09c2f7e1-220f-33e8-b62d-7ac8834197dd | -8.8854 | -45.7314 | 2025-08-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7329f750-60f9-30bb-95b0-273515d7f336 | -12.9194 | -56.9672 | 2025-08-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b8317fc4-57d1-3a32-b0ee-9dc36329a9a1 | -7.6219 | -42.7212 | 2025-08-29 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| aad4d231-2646-3d2c-968f-d987d76d8c2d | -11.3325 | -43.5689 | 2025-08-29 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 2fa5fc07-294d-3263-8df5-7ee14e311556 | -9.7915 | -64.265 | 2025-08-29 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ac24f235-850e-3c1c-9691-9827885ba75c | -9.1155 | -65.7699 | 2025-08-29 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 23f6873e-adb9-3110-99d9-1966328c673c | -11.3667 | -63.2853 | 2025-08-29 14:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 819b5618-1ce0-3e18-9225-374ad0ee2fc6 | -11.3325 | -43.5689 | 2025-08-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 57da3a2b-25bb-38da-ab80-9196ffe6bb39 | -9.7915 | -64.265 | 2025-08-29 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8a599684-f1d2-3cef-8629-f2214ba67abe | -13.5967 | -46.8684 | 2025-08-29 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e8caefb9-d713-386c-8058-8dc28be51312 | -12.8216 | -48.1934 | 2025-08-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ed33e483-d105-340f-9e06-d224bad13ec7 | -7.6219 | -42.7212 | 2025-08-29 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| b9968302-9631-348d-a0ad-fdb54ba31da8 | -6.1558 | -44.4385 | 2025-08-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b91197b7-421b-3833-bd89-c91e335b4c15 | -8.7714 | -68.7082 | 2025-08-29 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7fada4c4-0223-3e0c-9e80-41e66acfe5a6 | -9.1719 | -59.5017 | 2025-08-29 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c6f2fbf3-31e0-3d25-9489-8ad299710433 | -6.156 | -44.4155 | 2025-08-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9e167d4f-a385-3bc2-9244-5b1b8282b896 | -8.1775 | -45.056 | 2025-08-29 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| cca68736-fdbf-335e-9482-ad22f9c0a016 | -10.8483 | -47.4768 | 2025-08-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 13015d46-7f51-3fbd-a666-35d79e23e73a | -7.1106 | -44.6099 | 2025-08-29 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 462b4fa1-c08f-3aa9-bde0-85cdc7d2abb9 | -8.4599 | -43.6411 | 2025-08-29 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1b1c2641-57cf-374d-8d5c-25e2638fbe5b | -7.415 | -44.283 | 2025-08-29 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 837dfcac-1de2-33a2-87c1-0cf50a184427 | -7.1108 | -44.587 | 2025-08-29 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0210f321-c970-3d26-b0e5-380f4ff99989 | -9.3238 | -56.9064 | 2025-08-29 14:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| deef93af-9888-339f-bcae-a9a7835c817e | -10.0247 | -48.08 | 2025-08-29 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| db137a9f-6d21-33b3-8fc3-6abc1dec2e63 | -7.6033 | -42.6995 | 2025-08-29 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 197.9 |
| 5b3b2b6c-4c32-36b6-951c-b2a2f6ea1fdd | -10.8607 | -60.8191 | 2025-08-29 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f934e637-1c2b-3fa7-96c7-fa5505c2ef4a | -9.1714 | -59.5793 | 2025-08-29 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 07f173c4-ed17-3208-ba22-1f6e9e5757fd | -14.3299 | -53.3108 | 2025-08-29 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 46733b34-d2a7-3645-8f33-339a92c508e6 | -10.4736 | -57.9563 | 2025-08-29 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6cba21b3-7d2b-352c-8b3e-a0d1b93eae26 | -13.3543 | -54.38 | 2025-08-29 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e55a504f-fe32-3249-a8c3-ac836a0c23e4 | -12.4345 | -63.9173 | 2025-08-29 14:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d1061ea4-5059-3662-90f4-e332242089e6 | -9.5447 | -45.8842 | 2025-08-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 10611a16-391c-3074-9497-6e59363eae4e | -15.0835 | -48.1367 | 2025-08-29 14:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 830af035-1e5d-3c4a-bd91-db8e22664505 | -6.9867 | -59.3354 | 2025-08-29 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ebeb6fd5-7a0e-30c0-b291-4e361e1d9337 | -6.0431 | -44.4702 | 2025-08-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 39f86d81-dc27-336a-a6bb-ec1ef35713dd | -12.9382 | -56.9856 | 2025-08-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 005544d9-37ca-3a67-88b0-66e3a36b1f49 | -7.6225 | -42.6738 | 2025-08-29 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 4950e725-c7a4-3eb4-955e-2a9b696f3003 | -8.1964 | -45.0541 | 2025-08-29 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ef00794f-a81b-3711-bcdb-4b383344514a | -12.9385 | -56.9655 | 2025-08-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 324ba105-56ff-34d2-917b-00aa66447c33 | -9.7916 | -64.2461 | 2025-08-29 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 3e4ba722-3b41-36d6-99dd-9de1c069c7f7 | -10.848 | -47.4991 | 2025-08-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ccce08a5-3335-31aa-bac2-bc17a699c902 | -14.0328 | -44.487 | 2025-08-29 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 56416fdb-58f6-36cd-ab12-6bf58c8883c8 | -12.0553 | -50.6425 | 2025-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 38dec7d8-3773-359d-b972-663eb7b53a2c | -9.1906 | -59.5007 | 2025-08-29 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 62a96c51-35e8-308a-a938-4b08bc8bc1f2 | -11.3521 | -43.5423 | 2025-08-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 1d979b6a-2c4a-3a69-b464-d769720ad0e1 | -9.4432 | -60.5692 | 2025-08-29 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 225.8 |
| c9de4e4f-1f3a-3a58-8e59-9fcbbb8640e9 | -6.3916 | -45.2402 | 2025-08-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| e197e083-6405-3ef1-b6e6-d2d95ecc91ef | -14.505 | -52.0634 | 2025-08-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| db804c83-567a-3a91-8932-b218e4fcd66f | -14.2917 | -53.2945 | 2025-08-29 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d4aa65a5-2308-3dff-9a67-c860deeaec87 | -12.822 | -48.1712 | 2025-08-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 78db2e5b-4323-38bc-b13b-937696b86e27 | -11.3856 | -63.2653 | 2025-08-29 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 696e265b-0fd4-32da-9c25-bd4e4f35f4e6 | -6.3918 | -45.2175 | 2025-08-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 447f729e-e3cc-3871-b0a5-95abf2390b91 | -8.8919 | -62.4487 | 2025-08-29 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 00514a37-eb1e-35b7-9ca5-831fc0222c1b | -11.0826 | -44.7503 | 2025-08-29 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 160c6c9b-3827-37d8-9488-99f5f83e8cd3 | -7.6222 | -42.6975 | 2025-08-29 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 186.8 |
| b40e2901-a17f-37ca-8979-acfacf6de86d | -14.5445 | -52.0156 | 2025-08-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |


[Clique aqui para ver as próximas entradas](README99.md)
