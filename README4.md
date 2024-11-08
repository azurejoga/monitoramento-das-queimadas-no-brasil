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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11828b9b-b287-3135-98d9-853f28799f19 | -3.4948 | -43.782501 | 2024-11-08 00:14:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75776beb-9a56-3271-a1f1-d1a756e2e522 | -4.5012 | -45.685902 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78e0e1fd-21c0-3e38-8907-989160a58450 | -2.169 | -46.423199 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0bd6d5-72e3-3517-b7d4-783344ede947 | -4.507 | -45.666 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25b24476-1b0b-398e-8763-56c831609715 | -2.1773 | -46.459599 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca4212fb-7e5d-39b9-9299-56216145a323 | -3.8761 | -43.1483 | 2024-11-08 00:14:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7094fffb-9844-38af-9693-b5879841c150 | -3.7945 | -44.013401 | 2024-11-08 00:14:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d76e431-be56-3948-a64f-3d4846641719 | -2.2056 | -46.358101 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 396c70e3-e097-373e-bed3-9ff51ea36688 | -0.635 | -52.362499 | 2024-11-08 00:14:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dca83700-a907-3848-b958-4ccbd3279214 | -4.6721 | -46.450802 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 511a8a5b-5647-3549-b6de-4d948e103898 | -2.1498 | -53.616001 | 2024-11-08 00:14:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f032fcb-e9ba-3940-94ec-5002f6fa0610 | -1.3777 | -47.509701 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c03d08-c8b9-3d34-8d83-c36de218f61b | -1.815 | -46.359501 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f38284f-ec34-3741-8e0d-a0ee28ba5f4a | -2.1731 | -46.441399 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff1512a-dca8-3fb0-b8d6-f1c7ae05efa4 | -4.6124 | -46.505199 | 2024-11-08 00:14:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 108018b9-1f91-3da3-b1ed-bca2b88fe493 | -4.6677 | -46.431099 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6693aee-a4de-3971-8733-b78a4b91fe87 | -1.4745 | -47.212898 | 2024-11-08 00:14:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1d6d56-2a54-3c7f-80a3-a08e40451c3d | -0.9187 | -47.120998 | 2024-11-08 00:14:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c35cb0cf-c1e5-34c8-a613-1b714c016262 | -3.4606 | -52.592098 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa56859d-df4f-3b8f-a99d-a8037c43cf36 | -3.719 | -40.709301 | 2024-11-08 00:14:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e0c540d-8755-3e75-84e5-78c45edd75d9 | -2.6039 | -51.708401 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2da24f8-2268-3f55-a379-8d80ee71b396 | -3.5829 | -42.857101 | 2024-11-08 00:14:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c40ec1f6-cb86-3116-9ab1-31ce387863b6 | -4.6775 | -46.429001 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e568d732-bd2c-3206-a6b9-c838db650034 | -1.6725 | -47.179699 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2009a44b-3af7-3cd5-8480-2b5db13f21f7 | -5.4391 | -46.346901 | 2024-11-08 00:14:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc9ac0f-03dc-326c-9835-5551841a4db7 | -2.7993 | -52.944599 | 2024-11-08 00:14:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d189c83-c245-397b-be83-21d471f94920 | -1.3753 | -47.4995 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f986e7b-19e0-3c64-98b7-24142692ee90 | -5.4413 | -46.3568 | 2024-11-08 00:14:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9e8b8b-350e-330c-a72d-fd7be377eed3 | -1.4966 | -47.355 | 2024-11-08 00:14:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc4beeee-55b4-3b4d-8658-66344b38db9d | -4.6709 | -46.399601 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6802fa5-e00d-31eb-97e4-79846a6a23e1 | -2.8033 | -52.917099 | 2024-11-08 00:14:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911545a7-97ec-365e-accf-7480068aa8ae | -2.2036 | -46.349098 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a91fd8-37df-3cb9-9ccb-c5c7436c55ce | -4.6797 | -46.4389 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d952ebd-990c-331f-8962-a15e8c3b8b26 | -2.3181 | -46.173901 | 2024-11-08 00:14:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34d812c9-d641-3262-abbc-04877ec67221 | -1.3875 | -47.507599 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82792ecd-6217-3989-a7e7-1a503ef59baa | -2.7783 | -52.895802 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45393301-82f0-394b-affa-961d90909748 | -3.7157 | -40.695202 | 2024-11-08 00:14:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 68d7ea1c-852f-35bb-85ef-e79c329920bf | -2.2073 | -53.691601 | 2024-11-08 00:14:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83a8919a-dc72-33cc-877c-602141866a06 | 0.0415 | -49.427502 | 2024-11-08 00:14:00 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6279be7a-a3c9-3fb6-8be6-ad9468ca4210 | -3.6525 | -42.259701 | 2024-11-08 00:14:00 | METOP-C | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d64691ae-4a46-3062-8b9d-80a5e58d3f88 | -4.9144 | -44.0467 | 2024-11-08 00:14:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e32dc570-7e1c-3ed5-91d9-0121597a8834 | -3.5391 | -43.615002 | 2024-11-08 00:14:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3e5e3ca-8974-3c1f-b2cf-ce8a01bb69c3 | 0.0347 | -49.4123 | 2024-11-08 00:14:00 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cccf4407-91d2-3a15-a45a-ab036cca420b | -2.1613 | -46.434399 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca566ebe-23cf-3f19-9bba-b794ecdb08b7 | -4.215 | -45.739101 | 2024-11-08 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5d41372-6fbb-3377-a788-7af4164e6cbd | -3.7173 | -40.702301 | 2024-11-08 00:14:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f5dcf7ae-d828-39b8-a6aa-f2e776e995fe | -3.8278 | -44.114399 | 2024-11-08 00:14:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 932e418c-7a60-34e8-847a-d35ecee04083 | -2.496 | -47.231201 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c740ccd-2837-3449-85ad-734b148d066d | -3.6005 | -44.383999 | 2024-11-08 00:14:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 971dcfb3-449a-3d97-a01e-efa5b87f66d4 | -2.809 | -52.9426 | 2024-11-08 00:14:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba630cd8-af24-36d8-9cd2-d02328d74512 | -2.1065 | -47.3708 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bff9194-91c7-34a9-9cf4-f6e29dee10e6 | -4.6819 | -46.4487 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 885266fc-1395-321c-9312-8ae58a275641 | -5.1265 | -45.633598 | 2024-11-08 00:14:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99b82d61-d0d7-306b-934f-79a38f90de99 | -2.6132 | -51.750198 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96d51e0-a230-3fcf-8c45-105723a3c3e6 | -2.1711 | -46.432301 | 2024-11-08 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7c038fa-0d0c-3d10-a0cd-8e61ee80d1c4 | -3.4703 | -52.59 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0adda1b-4025-3575-bcfb-5e3b8c77a46b | -2.3201 | -46.1828 | 2024-11-08 00:14:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5aaa9125-50e3-3c92-ad51-d705e377985f | -4.77 | -45.739498 | 2024-11-08 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71b052ea-3649-3459-8192-cf5b52b3bbf2 | -2.6085 | -51.729301 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb60521-b6c5-33ec-88e6-339d6b7b81d9 | -2.5988 | -51.7314 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67e9384-0b26-3775-aa27-e6bfe80cf285 | -3.7847 | -44.015499 | 2024-11-08 00:14:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cddac08-83c1-3b1c-bef8-c348fd9dfbfa | -3.1437 | -54.446701 | 2024-11-08 00:14:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d93b9f-992a-3fb2-8110-18b824071173 | -1.3828 | -47.487 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2ca1a6-6865-3b44-8efe-94ac152da09c | -1.7231 | -54.100201 | 2024-11-08 00:14:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f21890b-d05e-3d52-83ed-86044fbadd7a | -3.7864 | -44.0228 | 2024-11-08 00:14:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 682c6255-654c-3e46-976e-e9311115b10b | -2.6108 | -51.285599 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8909c1fc-2d34-3183-ab33-4e79b5045702 | 0.0445 | -49.414501 | 2024-11-08 00:14:00 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 020e4202-8c13-35cc-b094-464c10b6015a | -4.5149 | -45.701401 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7e2baa2-942f-3eca-840c-0a3ff9a28f7c | -2.7839 | -52.9212 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4468d5a1-ea7d-3a2d-a022-f5d0acc0dbb2 | -4.8243 | -47.320499 | 2024-11-08 00:14:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15618d0e-5c97-3c0d-95c5-ce62834611d0 | -2.7879 | -52.8937 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f61deb-435a-3923-ac26-d5c1aebe46c5 | -2.7896 | -52.946701 | 2024-11-08 00:14:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565e7ca7-3c79-3a72-8bc7-186d7a254a6e | -4.511 | -45.683701 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da5f50b0-7f78-3680-9c83-21bdd1c4b7f8 | -1.7229 | -52.4468 | 2024-11-08 00:14:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf45fdd8-fce4-3fba-98b6-2a2a38dbec7a | -4.6699 | -46.441002 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0c801b4-b131-3fc3-84d0-5a91539953a3 | -3.7962 | -44.020699 | 2024-11-08 00:14:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1bdb6f-fff8-388a-beb7-bd2b59293cfe | -1.6702 | -47.1698 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f147a9c2-cc61-35e5-a394-6c1ae2c69b35 | -0.9209 | -47.1306 | 2024-11-08 00:14:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd9d661-8532-3f81-ac53-f5f25817496c | -4.5565 | -48.007 | 2024-11-08 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7c698a1-2ad2-300d-85e3-917638e4b28e | -5.1245 | -45.624599 | 2024-11-08 00:14:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 028e09f0-a4ec-3629-8f34-5dcf0f45a532 | -3.4932 | -43.775299 | 2024-11-08 00:14:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65dc3632-fc56-3dfd-b0e4-509fd9f5c803 | -2.1041 | -47.360401 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11180331-d40d-3e4f-8739-bdc32f7312a6 | 0.0317 | -49.425301 | 2024-11-08 00:14:00 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab28eea1-ccad-3400-91df-7a9e10bb9ed8 | -4.768 | -45.730499 | 2024-11-08 00:14:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c97cfc58-7f32-328f-8444-39524cfd3f07 | -1.373 | -47.489201 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a46325cc-46c4-38f1-ace3-c82237285518 | -4.6731 | -46.409401 | 2024-11-08 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dac5c453-042c-3106-ad4f-0b12264d5687 | -4.6146 | -46.515099 | 2024-11-08 00:14:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce34c065-d9eb-3f95-8a27-e2e8fa87ab1b | -1.3851 | -47.497299 | 2024-11-08 00:14:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 307fb7c3-ba9a-3cb5-a556-b5a621382caf | -4.513 | -45.6926 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9e43240-7c0c-3f4b-a109-4949a916d82b | -3.7831 | -44.008202 | 2024-11-08 00:14:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed65fe7-e177-3bba-9df5-296e3c433378 | -2.4937 | -47.221001 | 2024-11-08 00:14:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1419ffd-acd1-3309-a6d3-4b40ea544ba3 | -1.7134 | -54.102299 | 2024-11-08 00:14:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d627701-4079-3783-9255-71385aae0227 | -2.7936 | -52.919102 | 2024-11-08 00:14:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc05b792-1a37-3737-8432-43e1e08a3c55 | -3.1993 | -44.1143 | 2024-11-08 00:14:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42a96c8c-d93a-3821-9cc8-1660ab6579d7 | -4.9127 | -44.0392 | 2024-11-08 00:14:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4dec784-7166-374a-b078-446db3e13ad6 | -2.6759 | -51.802799 | 2024-11-08 00:14:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ad41ec-bdbf-33fd-b17b-d228f7caeb24 | -4.509 | -45.6749 | 2024-11-08 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e032045-31e7-3a56-8054-81ca46c1fe75 | -16.114201 | -43.812099 | 2024-11-08 00:14:00 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b3a0d3f-4d67-365b-9bb2-3c0c7d51766b | -4.7332 | -43.2458 | 2024-11-08 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38195ffe-1aa6-30c7-80f3-cf92d88128a7 | -3.4328 | -42.2015 | 2024-11-08 00:14:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README5.md)
