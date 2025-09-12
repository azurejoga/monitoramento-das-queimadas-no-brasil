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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e25f12a9-2981-36d2-9908-a7665c49fcfb | -16.62921 | -49.78817 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7508f54d-f7f9-3460-87f2-172995276444 | -20.2767 | -42.88825 | 2025-09-12 04:27:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| de4ddde1-1c16-3444-99aa-1adc1524aa92 | -12.24471 | -47.33279 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aada5dbf-f0be-3032-9151-653c76982f80 | -17.58645 | -42.16919 | 2025-09-12 04:27:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 65d2bf87-f4fe-3afc-bd01-2af1f370698d | -15.65842 | -53.89538 | 2025-09-12 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a153180-c680-3c10-84ba-d6f073e006f8 | -12.50029 | -47.43531 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bde790ef-3a40-3e42-9e92-0542f2fef7f0 | -14.47336 | -46.34981 | 2025-09-12 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1e30fc6-0dcd-3e55-b19e-aad952a52f95 | -16.48736 | -51.98893 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4958ccc8-8493-3fd9-855b-e1c338fba979 | -14.42312 | -46.4039 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4503895-b191-352a-b8c4-88fd2cadd834 | -18.75279 | -47.6213 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7acec835-752d-37d9-b7f8-8109e658dd75 | -13.44368 | -56.66824 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da3d05a6-6350-3033-b700-99e796ca37c2 | -16.49092 | -51.98711 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98bd2fa9-bf60-387c-9093-2190911a4722 | -18.6587 | -47.66391 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c46021f9-42dd-382e-88a1-61b57491e026 | -18.76104 | -48.19583 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40fa2bc1-a8f8-37d2-a1cc-0a8bc5e1c3fa | -12.93336 | -48.00472 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2f42ae4-312b-3560-b1f6-383cbbadc8a1 | -17.55604 | -44.55441 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3c70b7-b76a-3adf-90d2-6767ea0c4b37 | -15.09138 | -48.01381 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa57280a-58c9-3968-bef1-a3e5c4312d0c | -19.66105 | -44.90505 | 2025-09-12 04:27:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3918cc04-6b88-30e2-94b0-7f012d7084ff | -14.13645 | -45.41909 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79da2376-e65e-3602-95a0-5c6926301fec | -20.03447 | -41.74804 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOSÉ DO MANTIMENTO | MINAS GERAIS | Brasil | 3163607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a829290-eb36-31b6-9b5f-2e06e5cf830f | -11.86489 | -58.82165 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52918f09-ba91-33d2-9972-a1a5dd57041d | -13.91618 | -48.23257 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03ed2b1a-ef43-3232-87dc-12b73e88c8e3 | -17.90836 | -44.6016 | 2025-09-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ddb5769-c2ca-3b02-87ca-540d453c9424 | -18.81664 | -46.88086 | 2025-09-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d3ced5f-089d-3f15-b0f5-34b13f20d2cc | -15.60903 | -52.74274 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 843743b5-4305-3cfd-aa39-1ee496638da8 | -15.14766 | -52.47468 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 077636a1-d1d6-3f4f-8ed0-089ae3231ada | -14.17333 | -46.20469 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33e9aeef-1ffe-3e8c-9bb8-05d05f200e5e | -14.30677 | -44.86721 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd7975ff-be2a-37d9-bced-4e0d96b2aadb | -15.08256 | -48.00504 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0548b8b-6626-3075-b4e6-15b38330554d | -13.90505 | -48.25983 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5d02cb34-4622-3099-8c54-4b6407c0587d | -18.75224 | -47.62507 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b779005-7145-3ad1-afce-6a97b9bd6b51 | -14.41586 | -47.31791 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e85803d-6d07-33ad-872e-d57652ece943 | -15.10699 | -52.46458 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ab22783-8cc7-332c-af21-ee6a1ccf8ab3 | -14.32634 | -54.13326 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2228ef6-5cd2-3acb-b679-e2d43be79ed5 | -13.89299 | -48.22879 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19a4851c-9467-31ac-a193-4190fbda9ee3 | -17.33416 | -46.67342 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4132b0ba-a4d9-37ad-bc51-595a97f0092c | -12.83191 | -47.9597 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7125fe5c-1c9c-35c2-ae1e-1f7ebe01551f | -15.1161 | -48.09468 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08518eb4-f96a-334c-bef9-c4d92e475a52 | -15.60227 | -52.73641 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cdc709e-b290-39ad-9ae4-4771ee8654e7 | -14.41795 | -52.9283 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7133c2c-cd2c-3287-9bbe-71535edde2dd | -14.17676 | -46.20513 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6bfd23b-94c4-3b55-9d62-df5d214c7ccf | -15.8795 | -48.18453 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e17d5105-2319-39d5-8a59-80308783172d | -19.81502 | -45.00064 | 2025-09-12 04:27:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6553089-08cf-3d54-8bf0-24c39cb912ce | -18.05015 | -45.44187 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1033d21-406a-34a3-b0e4-c780fe97918f | -14.23741 | -44.24897 | 2025-09-12 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70429893-09b8-30d0-b627-65c143884e66 | -18.7697 | -48.54072 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd50cbbf-bac2-3d01-9793-d288bf6be70e | -12.95834 | -54.74335 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb60b2a3-4654-3cb0-b13b-1873f431a1c4 | -14.44692 | -47.31191 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d255d658-12c9-32bf-b370-4d4f6381373b | -19.18672 | -48.01087 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 620c2e3c-c3b5-3f07-824d-f4ba92807898 | -16.25838 | -46.78479 | 2025-09-12 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b3dbb9b-780f-3af9-bc0c-ea2210fa9eb8 | -17.26841 | -46.09097 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9fe2303-0445-324e-b896-e5b3475002c2 | -18.31328 | -50.41822 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40415a53-dd94-3f9e-95c7-2024177234cb | -14.56621 | -48.75665 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30ebb4b1-64c1-3d59-a4c9-b30b1a658a99 | -19.23877 | -48.04207 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7fd08522-e9d6-3103-ac7a-4b3c3aadf4e8 | -14.0394 | -42.1543 | 2025-09-12 04:27:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec690ff3-1b89-3cf8-a105-f2608a76c6d9 | -15.11615 | -48.61052 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9647569e-04f5-337b-a171-25c43bfe4d5b | -15.48706 | -47.34484 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca1aa09e-8bdb-3d9b-9a5e-b3164d2d36bc | -15.4904 | -47.34541 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d55adf-135d-3719-8024-f54185bbf8db | -17.38175 | -52.94916 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7c7a67d-5535-3ba6-a8e5-50e3f065ced8 | -11.18191 | -55.07964 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5704842e-1fc3-3c1f-9b45-4d8d797f77ef | -11.87268 | -58.814 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a2a32e7-ef14-35a7-aa74-22172400f7a5 | -12.97102 | -54.75078 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63bf1f38-ff2d-34d1-b487-89d91d481cdc | -11.95558 | -51.1727 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b6ffc295-e5ee-30f0-9fb3-4f46bf8be00b | -16.61847 | -51.81282 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aaaba5f-026a-3a6e-ad01-de6c9697fd8d | -17.7231 | -44.40546 | 2025-09-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 929dbc61-4ff3-3e61-ae61-1939aa1979f0 | -13.89686 | -48.22579 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db0cea70-6a91-3891-9433-553a0312972c | -12.90146 | -48.7961 | 2025-09-12 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1782340-08c8-3c72-8401-e058d2971b75 | -12.93061 | -48.00062 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5888ecb-cb03-38af-9ee9-59f95820b5f8 | -17.71706 | -48.19427 | 2025-09-12 04:27:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc1249f-40b9-3fd2-81ef-e16e833adcd2 | -18.05569 | -45.42919 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e3913d5-313c-3242-8ebe-5f838a0b651a | -15.12836 | -48.59797 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 813f82c3-8fc0-3feb-86d6-2916947b744f | -14.41972 | -46.40337 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d827794-f943-30e4-8652-d564b6a16494 | -16.49456 | -51.98764 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1151692-6957-3b0c-a3bd-5e976c32e928 | -11.1791 | -55.06814 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5497e08f-47ee-321a-a625-9a626cc11a8d | -16.07439 | -49.97012 | 2025-09-12 04:27:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5f198e7-1571-32e8-b13b-cd05c20341d4 | -15.52588 | -48.55418 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ca86164-2846-3c8d-a266-a2ae768c733e | -11.23065 | -55.00237 | 2025-09-12 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96b8199b-5214-3d95-83de-d2f827d36de9 | -15.52701 | -48.54703 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33db7c19-a622-376b-834e-41231d004912 | -13.03662 | -47.99659 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc6ef9f7-898d-3144-81f1-512e3695954b | -14.12538 | -45.37199 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fc81ce5-c129-3ad3-ba8a-7fe2164e8000 | -20.20904 | -44.55526 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2fe80233-91ea-319e-9c7f-303267e3572c | -19.07236 | -48.73434 | 2025-09-12 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5135f47-1d09-386c-b611-7ab6071e6d37 | -16.00652 | -48.08783 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f042b9b6-cd15-390c-80d5-0c0f84a3a0e0 | -14.26526 | -54.78331 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77c738d2-12d7-345a-ad97-6887664e23c9 | -12.45489 | -48.02427 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72e0cf78-8c78-381e-80c0-862cbd111078 | -16.44209 | -49.02801 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d803e4f-b072-34d4-aa06-26d057743505 | -18.62468 | -48.25024 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 846bebc0-9ca9-32f0-ab0f-b42bef248c01 | -15.23386 | -47.62276 | 2025-09-12 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b736267-5345-3c3c-9c1d-98726eab7650 | -11.18962 | -55.06474 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f02708c-d396-350e-8424-49d557a73a94 | -18.62555 | -48.26155 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49677d9b-f0f2-388b-91a4-e057df6017b3 | -12.81918 | -47.97572 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74429e4f-41ef-3934-b6ad-6489b7f722b0 | -14.41529 | -47.32156 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50b200e0-5f77-37b7-a40d-60b5e3b49694 | -14.32708 | -54.12925 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fc6c70aa-6121-3f5d-a996-c267b4f71240 | -14.50459 | -53.91793 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4be86f70-cdfe-3965-9eef-189479888c76 | -14.56346 | -48.75252 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab1885a6-4d9d-34d7-afd9-c15ace2d9f7c | -14.18702 | -46.20659 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ce41ef13-9580-3561-b562-2576b1c6151b | -16.30462 | -50.0827 | 2025-09-12 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92db11a1-57e9-33f5-a857-4303616c804e | -20.03981 | -41.7435 | 2025-09-12 04:27:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 82c2ddb1-0d08-35cb-81ef-bd7e80b6b771 | -12.99519 | -48.00039 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be33ce1e-7e9d-3225-a084-a43eeb3da975 | -17.91488 | -45.71025 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README86.md)
