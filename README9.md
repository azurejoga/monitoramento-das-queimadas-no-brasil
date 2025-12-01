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
| 2447a6ff-7e55-3a68-8a4e-1dd74129d9b4 | -22.94551 | -47.38008 | 2025-12-01 03:40:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58cf55e4-3cd4-3f79-b5de-1f70ddbc992b | -21.06108 | -47.11553 | 2025-12-01 03:40:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d52fc7f-e65d-3656-b353-3111e8acd21c | -23.12132 | -45.29184 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd22fc69-8b6a-373a-8b46-5346f7e4cfbb | -22.73109 | -47.35993 | 2025-12-01 03:40:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a549d2e-39cd-30e9-9ccd-12a68bc0b889 | -20.93653 | -41.9043 | 2025-12-01 03:40:00 | NOAA-21 | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6b065bb-7dbe-3512-b58f-81ebed7b088d | -21.54856 | -48.89328 | 2025-12-01 03:40:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bcd0e08-fbca-335b-b75d-f7aee4d91d81 | -20.59298 | -44.28125 | 2025-12-01 03:40:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1b32b4e7-a640-3c53-ba66-10517a1df216 | -21.76404 | -44.30132 | 2025-12-01 03:40:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ffa0ca9-c15d-3db2-bc11-0959e6650df2 | -19.79634 | -47.80521 | 2025-12-01 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74f383ff-d38d-3341-8d60-535221f0f835 | -22.7299 | -47.35969 | 2025-12-01 03:40:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 05daf2ca-f2f6-395f-95da-6810bf5dd377 | -24.12015 | -50.14639 | 2025-12-01 03:42:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| eee0e2f0-d9de-35ac-a22a-ca7d1d572ddb | -24.12496 | -50.15288 | 2025-12-01 03:42:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| be5e8045-54eb-38a9-a89f-a4697ab5f668 | -4.369 | -43.3373 | 2025-12-01 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bfb1cc14-3c92-3c7b-b9a0-a59fe354394c | -5.3209 | -43.5781 | 2025-12-01 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a8156fe8-d5fd-3834-9a4a-4bc929dca74f | -3.7195 | -45.8992 | 2025-12-01 03:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 210025fb-addb-325d-8d2c-d76d5d5d5950 | -4.3703 | -43.1508 | 2025-12-01 03:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9f0077c5-2632-3267-b5dc-3e875565fdd2 | -4.389 | -43.1497 | 2025-12-01 03:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2203fd28-8ddb-3b88-9ba3-1e29f2af3fb1 | -3.2174 | -50.139 | 2025-12-01 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e82841ee-8b24-36b0-a1cf-bfcb9e47b59a | -3.7009 | -45.9 | 2025-12-01 03:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 051dac95-4281-38a4-8927-8bf6bef3bb75 | -4.4064 | -43.3351 | 2025-12-01 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| c1f5b175-f1de-3b1b-ae3d-525189400006 | -4.3877 | -43.3362 | 2025-12-01 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 313060a9-5043-34b5-9137-54904425b7d8 | -5.3211 | -43.5549 | 2025-12-01 03:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fb66ba45-a47f-3640-a73e-13e837547da1 | -4.3879 | -43.3129 | 2025-12-01 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7dbf0497-2d57-3f18-a4b0-5bc57317370c | -3.6008 | -47.2739 | 2025-12-01 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0882a142-e887-34d5-8d80-b76b3e0fa73a | -5.3211 | -43.5549 | 2025-12-01 04:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| aa6d5dc5-29cd-3f7f-a1eb-06c3d5740420 | -3.2174 | -50.139 | 2025-12-01 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5fc9e08e-dd70-3841-87de-7333d3bafc4a | -3.7195 | -45.8992 | 2025-12-01 04:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d87ff364-7e25-36f6-b852-fcbb4e971eef | -3.6009 | -47.2521 | 2025-12-01 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 791d8d74-36ae-3c0d-8dc3-88b4071d4c72 | -3.7009 | -45.9 | 2025-12-01 04:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 467de85f-4ba3-3d1c-91bf-f9e16eecd090 | -4.3703 | -43.1508 | 2025-12-01 04:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 67a8a870-2aff-3d1a-9c11-33fb8eb84da2 | -4.3877 | -43.3362 | 2025-12-01 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 654e0f8f-d92e-3c08-bd3b-1894aeec8d7b | -4.3879 | -43.3129 | 2025-12-01 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4da6547c-4caa-3c4e-9cf1-38bb1c67071c | -4.389 | -43.1497 | 2025-12-01 04:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ac8f3e15-9b06-3e7a-bc7d-9d672db2c196 | -4.4064 | -43.3351 | 2025-12-01 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1aacba21-a766-340f-9ddc-45b2ae480b23 | -6.08516 | -42.07677 | 2025-12-01 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c86e882-aea8-386e-bcc2-f512696ac65a | -4.3706 | -43.15263 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a1590065-f395-3289-9139-81d01d29ef74 | -5.52313 | -42.59947 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 961b9141-1ce1-3f78-a777-f99ca834d164 | -3.7024 | -45.90693 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aaef180-eb91-3066-8f52-600df8f18df1 | -2.34721 | -45.74318 | 2025-12-01 04:04:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24d12903-0367-3db4-8c15-59b3380c600c | -2.48607 | -44.15467 | 2025-12-01 04:04:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a74333a8-2d86-39c9-af11-05f72f6081ea | -4.38546 | -43.15508 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 548ee534-5586-3bc3-b02a-b3737e435a40 | -4.39158 | -43.33718 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3b9946fa-2bb1-396c-951a-4a2f8b1d979b | -3.56887 | -41.32669 | 2025-12-01 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8eecdf8c-5a27-32b1-8a10-6d932366cce3 | -4.40377 | -43.99287 | 2025-12-01 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d038751-4bd9-3f76-bdbe-aafd31a3fd45 | -3.93585 | -45.85207 | 2025-12-01 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f5c1fa-42d3-3ab4-873c-6190fadbc858 | -5.49567 | -42.16658 | 2025-12-01 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 01c39e74-b953-33c5-853f-9640e8af0022 | -4.37956 | -43.33993 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b5d9d35-7cb5-32ff-96f4-7a877dbdd40d | -5.75109 | -40.81591 | 2025-12-01 04:04:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96db23f0-fef5-377c-af1d-507cbe86fb22 | -2.2447 | -45.62187 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd9abab1-8086-3ca9-9828-54e8daedce11 | -3.32715 | -45.63969 | 2025-12-01 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b6acb50-3659-320d-bf41-4a5ad5d30992 | -5.4877 | -40.92604 | 2025-12-01 04:04:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cfdecf2d-2b9b-310c-bcd2-9b5c229a25d3 | -4.37432 | -43.15322 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1fa306bf-9a36-33e2-b99d-23ef95d71884 | -4.30984 | -45.37786 | 2025-12-01 04:04:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 541919bf-ba03-3b17-bfe1-4bebf3c2835c | -3.58604 | -40.42999 | 2025-12-01 04:04:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3862083d-cb0d-35b8-bbf6-ba51a75b5b01 | -3.50221 | -44.21769 | 2025-12-01 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144a2c57-8397-3c5e-a5de-e23a923d81b6 | -5.52087 | -42.59085 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e9ccdeb5-1de8-3b6a-b596-2686d5dc8ce1 | -5.33564 | -43.5655 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef0f3657-29d4-3d00-b5d9-db68e8fda13e | -3.213 | -41.56744 | 2025-12-01 04:04:00 | NPP-375D | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 92853065-fc08-3353-afc6-1d3ba1b42849 | -4.38856 | -43.33208 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| d81eb268-277d-3f8d-8d5d-863779a6ecf1 | -4.60013 | -45.21158 | 2025-12-01 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 645340f9-2f71-3054-8f0c-9fb04283432c | -2.24919 | -45.62263 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68866839-3f28-3c49-b00a-4827b48dc43e | -4.38174 | -43.88441 | 2025-12-01 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42642df5-2e8d-3c56-8746-c725b505f699 | -2.73984 | -49.32979 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d0687ad-5de1-396e-99a1-f25cf5b25afc | -3.50278 | -44.21423 | 2025-12-01 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33df8679-7caf-3603-9b0e-f8c5b0e38e36 | -2.92548 | -48.23099 | 2025-12-01 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e0537e3-1525-3635-b352-14c8c86a09d0 | -4.36245 | -43.15585 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34875536-71a0-3600-848d-40cb7107ed98 | -2.60307 | -49.26075 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9186c86d-f7d2-3b4d-a472-5cbf3657793a | -3.44699 | -50.15786 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f5c685c-65e9-3f79-82c7-6af650183a5e | -4.39681 | -43.32877 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c349ceb3-726d-3623-a9ec-506e09d3c736 | -3.21151 | -50.14209 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8efa386a-99c9-32b5-82c9-6321b8116eb8 | -5.23877 | -41.24028 | 2025-12-01 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0a51253-62d9-32af-a33c-e399d965169c | -5.36135 | -43.02416 | 2025-12-01 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a466195-4c61-30b2-8be7-921a10eb7cb6 | -5.14658 | -37.74863 | 2025-12-01 04:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1b3c366-0fb1-3686-9797-6bee3357edb7 | -5.52152 | -42.58685 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aef66049-c80f-3bad-b616-f14a0fa27874 | -4.36546 | -43.16087 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 05ece9a7-6e74-318f-9abf-b7203736b9a0 | -3.71219 | -50.65509 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f88f0f-7168-3b5c-bf40-98ec0bab85e1 | -3.57399 | -45.69916 | 2025-12-01 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 877902fd-3508-39ee-8708-e8c46c40d856 | -3.71426 | -45.90377 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5f281be-910b-3f41-91c3-3475521e66cd | -4.37654 | -43.33486 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8df561c2-c806-3718-b082-2b3e6009a126 | -4.37547 | -43.15608 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 550d62a2-5da4-3a80-9c46-81b1ea43d725 | -3.21527 | -50.14482 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16b4a8f3-0d39-311f-bc75-d11ea74508fe | -5.33115 | -43.56932 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14e337fb-0be3-3c41-9f7b-2eec920c8874 | -3.2175 | -50.14318 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e7dcda4-6bed-35b6-a32c-e6a91843a48c | -2.24612 | -45.61293 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d4af85d-d387-3eac-92e1-f7a2d3820d2d | -6.67363 | -39.89233 | 2025-12-01 04:04:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cfba3b38-ce5d-3d0a-9b72-adcb3f9d6f95 | -2.44168 | -47.08252 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5d76d44-8b93-3320-b4b4-c5ccd2690954 | -3.57308 | -50.29529 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8fdd37b-4051-343f-9a01-73027c353439 | -2.24675 | -45.62014 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c2fd9e2d-fe6a-322b-ae09-1b0872fcfd8a | -5.33637 | -43.56101 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37af39b6-0bc9-3f5c-9217-688ed651d02c | -3.59843 | -47.26943 | 2025-12-01 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6883c0c9-9462-3dab-9e2b-a4101ff19965 | -2.246 | -45.6246 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6aadb4f3-167f-3bdd-a34e-d127fb8a221f | -2.44819 | -47.07888 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17102557-5a26-3222-939e-2a51e374ad0e | -3.941 | -45.84846 | 2025-12-01 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 493e3201-da0f-34ad-8d2d-6a45b2d0b6cf | -4.38406 | -43.33601 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 2dfc9b42-d0ea-3d2f-9cbf-901380e468bf | -3.2614 | -48.5749 | 2025-12-01 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48d76abc-4691-37fc-a44b-4cf0346f6191 | -4.14629 | -43.73078 | 2025-12-01 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1857383-a6f0-339c-aab3-67573fd64ac2 | -4.3848 | -43.33152 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b374c8f9-7186-3ddd-a56a-e2511e1da6c1 | -5.51796 | -42.58626 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1959fab3-5080-327d-978b-eef5e74a2560 | -3.39399 | -50.24892 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7ba0b1-88d5-34ee-a345-a39d636a5abe | -6.67418 | -39.88887 | 2025-12-01 04:04:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README10.md)
