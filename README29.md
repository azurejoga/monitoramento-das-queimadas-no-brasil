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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53eed5fe-fcbd-3d94-a981-9c861c84a739 | -13.08937 | -56.91174 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c001d543-6dfa-3b33-8df4-02b4b1197194 | -13.07243 | -56.8786 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f368d580-797b-3861-861d-f07837b35167 | -13.05882 | -56.87729 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f81bced-f484-32e1-b08f-1767f108de28 | -13.07365 | -56.88503 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4636eb8-173d-3a40-b0f5-114ff7d00da1 | -13.08188 | -56.91732 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4dc4c23d-3a01-3c13-a5d4-a21d960b9b4a | -13.08463 | -56.91143 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ebd0983e-b90b-3a85-a2ea-bbd6b87fdba8 | -13.05203 | -56.87643 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 100cf749-ed4e-360f-9be7-d6e58f289b88 | -7.57977 | -72.50021 | 2025-08-05 05:57:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba34e462-1db6-3429-afbd-83f85073648d | -13.08325 | -56.90506 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e8bf44d-4652-3350-89c0-cfeabaa0be77 | -13.0561 | -56.90205 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acedfaa3-19f2-32e6-8b66-02e78163e714 | -13.08528 | -56.90527 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b3e432ef-b383-3740-a916-1b4ad2aa2968 | -13.0595 | -56.87109 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 217d653a-2c39-3dd4-b81e-c8649140eba1 | -13.07431 | -56.87869 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 689b3f71-78e9-3a2f-b810-6a6edef2c95d | -13.08399 | -56.91755 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6b1d1179-e2e4-3cf0-88c9-e8418460ba62 | -13.06562 | -56.87802 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2eaea16e-0ab2-36d8-a3d6-3d9fcd76f6d6 | -13.07299 | -56.89133 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c19b15dd-6663-3fcd-a8d3-5a52a83338d6 | -13.08594 | -56.89901 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 184efe15-82ed-3255-985d-32d350cf24ee | -13.06286 | -56.90299 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e971bbc-736c-3a8f-8766-d80af0bf8278 | -13.05271 | -56.87025 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb924346-7576-3036-af9f-c0a6677c8c9d | -13.06492 | -56.88433 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b69c5c84-6fd4-3d10-8b6a-6a2b6bda5d47 | -13.08255 | -56.91126 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bddd1e2f-01ac-3180-9e40-cdb2443b1b0d | -13.05812 | -56.90226 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e940dce7-6119-3a60-b546-817c28dc993f | -13.07173 | -56.88495 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e293ab40-e093-3876-88ef-5ba9b138a3a0 | -13.07856 | -56.88543 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2052fe07-2db0-3981-af19-1d3e4cd5523c | -13.08395 | -56.89876 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35b3287c-f14d-3332-9da1-e7ba3dfd4382 | -13.07786 | -56.89169 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad07f9ba-7908-3a15-8254-bf50e0b5973a | -13.04526 | -56.87544 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd8f2ea4-8ce8-3495-bd72-530be7c3d6cd | -13.05136 | -56.88256 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44fe9c99-d0c6-3830-81a1-c39986c8991e | -13.09006 | -56.90561 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a0cd557-3561-30bd-84f1-0c2d3e39fb18 | -13.06749 | -56.87809 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62a1118d-126a-3262-b5bf-b36bf62e614a | -13.06489 | -56.90316 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a784763b-1203-3e53-8c81-0126fc9e3128 | -13.06684 | -56.88443 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 378999a5-5d03-35ab-ae2f-63496fe0cd7f | -13.07981 | -56.89185 | 2025-08-05 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feb2d09d-1a94-36c6-b8eb-f6914349262f | -13.0723 | -56.9131 | 2025-08-05 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 811f9f75-7088-38fa-9ad3-9b18bc8d0f8b | -8.9478 | -46.7354 | 2025-08-05 06:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| dbc4cd6f-9ea6-35b2-8352-c9417e8f0006 | -7.994 | -43.1534 | 2025-08-05 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| f4ab3474-ad23-3862-a0b7-55eac058f8af | -13.0914 | -56.9114 | 2025-08-05 06:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1355203f-912f-3809-b0f0-00a69cbb35f5 | -4.77622 | -45.33341 | 2025-08-05 06:08:00 | AQUA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7d03b37c-b0dd-3906-8137-4c2d4dae7a48 | -13.0538 | -56.8746 | 2025-08-05 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fb1cfc18-9bce-301e-9d6c-71881e1a9cfd | -13.0723 | -56.9131 | 2025-08-05 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f6ba1088-0b87-31a0-a074-356bce17b5cd | -13.0914 | -56.9114 | 2025-08-05 06:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 660ba398-7fdb-384c-9891-fd8adc06738b | -8.9478 | -46.7354 | 2025-08-05 06:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 275361f7-97ab-3e6a-bf99-0a07fe74cc92 | -11.78434 | -44.99129 | 2025-08-05 06:10:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 54b20dbf-4d03-3e38-8ef3-be7370017ea8 | -8.93496 | -46.73074 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c61f8c10-3355-38fd-a820-f3f746822037 | -13.05162 | -56.87589 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| bf03b65a-3608-3053-816e-fbe7d2f81603 | -12.68262 | -48.125 | 2025-08-05 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 4e8d7128-3ced-3667-928c-3f01b4466898 | -7.99639 | -43.2165 | 2025-08-05 06:10:00 | AQUA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 00d88e80-ee5c-3a45-a98d-5814263de689 | -10.3224 | -47.8281 | 2025-08-05 06:10:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d0353560-3595-310b-b6dc-37bccdb38c7a | -7.75392 | -45.22477 | 2025-08-05 06:10:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f07258fc-6f06-3c3f-b62b-8235e692955c | -8.933 | -46.74555 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d0c237d0-3905-3fd7-97fd-a7b5b7abdcef | -6.96718 | -42.84706 | 2025-08-05 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.4 |
| e8216738-6ddf-349d-a029-f341cc06b947 | -11.91695 | -44.95105 | 2025-08-05 06:10:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8776a417-8a76-3683-8918-94accaf22ccb | -13.06245 | -56.87774 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6e4f2240-c4f6-3856-9d97-fe1e34d8d369 | -13.04078 | -56.87413 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e27daaf3-783c-3dd9-9ff1-00a0d43242e5 | -7.75733 | -45.23059 | 2025-08-05 06:10:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2018a1e0-3a30-3594-8927-6c8831c85289 | -8.93541 | -46.72379 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ad950629-34f0-3394-9a64-aaa2a9ff207a | -15.69164 | -48.97702 | 2025-08-05 06:10:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0cae691a-5c56-3f93-944f-c49066a25694 | -6.96633 | -42.8422 | 2025-08-05 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| fb7b4087-dd26-322e-a75f-a77210dbacfd | -8.9461 | -46.73227 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 88bb70cb-569f-32fe-aeec-1bd749ab316c | -13.08171 | -56.8956 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 2cf6153e-164f-302b-8db4-217df4688461 | -13.04842 | -56.86959 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| cfa5af81-569f-3d7f-9467-addea70093d6 | -8.94656 | -46.72527 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e57b7d71-27d0-3a59-9891-4dd03132820f | -12.67204 | -48.12326 | 2025-08-05 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1ab5d0ba-1e6f-30ee-a421-410af0f93519 | -8.93334 | -46.73859 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6b4d5249-2bfc-36ca-8e59-499744c412d1 | -7.9922 | -43.13413 | 2025-08-05 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 370433f4-aae5-3e83-8056-c6e387498e84 | -13.07325 | -56.87971 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3de6792e-e2be-368d-85d9-84644a2efa62 | -13.07936 | -56.90954 | 2025-08-05 06:10:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1d2d0f88-d126-34ee-8550-d88e90a51f78 | -8.94446 | -46.74014 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ddf7d9c9-3c60-36d5-8b23-1897e6fce296 | -6.67535 | -49.79061 | 2025-08-05 06:10:00 | AQUA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3d89deb-0e46-38f7-a4f0-1d3ce991ed18 | -6.96262 | -42.86985 | 2025-08-05 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| fc1ed1cd-b22e-307f-b87a-b1e2086ccf94 | -7.98873 | -43.16099 | 2025-08-05 06:10:00 | AQUA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 0b1dde69-49ba-3d7d-b50b-77aebe631963 | -12.68453 | -48.11102 | 2025-08-05 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 26333ecd-c4a1-3cd3-ba0b-fc0152d4d9ea | -6.96366 | -42.87482 | 2025-08-05 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 3648d036-ab5c-3406-8651-1e1d86c10417 | -11.90978 | -44.94237 | 2025-08-05 06:10:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7738c1d2-9466-39a8-ba17-c96c4be59f5e | -8.94411 | -46.74719 | 2025-08-05 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 28b690da-f6f1-3b3f-ba7b-594c812f9657 | -13.0723 | -56.9131 | 2025-08-05 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9a264912-87bd-3fb3-a305-9799ac11a7e3 | -13.0914 | -56.9114 | 2025-08-05 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 244e01aa-3253-3be6-a139-4aa3a5bb993b | -8.9227 | -60.5568 | 2025-08-05 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 98ce29ea-8e7b-32d2-957e-203ffccaa8c7 | -13.0538 | -56.8746 | 2025-08-05 06:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1c18f9b5-33e8-37cc-a301-2512917ad184 | -8.9228 | -60.5376 | 2025-08-05 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 37f40dd3-c512-3d49-be2b-77196c339886 | -8.9478 | -46.7354 | 2025-08-05 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f40b7fb2-443c-30db-bd66-e12a37b703fd | -9.63552 | -67.51512 | 2025-08-05 06:20:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db71c5c6-f977-3750-94f6-12bb406df3c5 | -7.58148 | -72.50008 | 2025-08-05 06:20:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 440f2dd9-bab8-36ea-88d9-6f70a338d7e1 | -7.57795 | -72.49955 | 2025-08-05 06:20:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a15e9bde-0f9b-3f2a-82bb-26c3e6a3c85e | -8.9227 | -60.5568 | 2025-08-05 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 58c87ed4-49af-3424-b85c-1a0c92ed8206 | -13.0914 | -56.9114 | 2025-08-05 06:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| e4d49ea2-800d-3840-93b1-11a6120a2f57 | -8.9478 | -46.7354 | 2025-08-05 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0a5aaed1-252c-3169-8184-4d95dc24f427 | -8.9228 | -60.5376 | 2025-08-05 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 98eb5a6f-cd66-3b19-a379-2310d86051a7 | -8.9478 | -46.7354 | 2025-08-05 06:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ac882ec4-362c-3da7-bfc3-f48e80b81d37 | -13.0914 | -56.9114 | 2025-08-05 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2d92fc64-a4c5-3d93-9b60-710b36428914 | -13.0723 | -56.9131 | 2025-08-05 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7933500a-611e-3f47-bd2d-f585312ec780 | -8.9478 | -46.7354 | 2025-08-05 06:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 77488f45-f5fb-39fd-a528-ad7cd15fab6e | -13.0914 | -56.9114 | 2025-08-05 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3f3a9f57-ed0e-3d9c-8e9b-c75595bc9983 | -13.0538 | -56.8746 | 2025-08-05 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c4d7dd69-483e-3b1a-86ac-f9762c375f6f | -8.9478 | -46.7354 | 2025-08-05 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d4b45508-7275-3c94-adab-801089eeac60 | -13.0914 | -56.9114 | 2025-08-05 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 92b88568-eaaf-3527-894f-1d21ac4a6ef3 | -13.0914 | -56.9114 | 2025-08-05 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 387d069b-bfaa-3bc8-8cc1-335d0acda864 | -8.9478 | -46.7354 | 2025-08-05 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9a32bae8-bbe1-3b88-ba3a-291d58f42ed4 | -13.0914 | -56.9114 | 2025-08-05 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 53ca1918-7c74-317a-a833-f5cf81c2f452 | -8.9478 | -46.7354 | 2025-08-05 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |


[Clique aqui para ver as próximas entradas](README30.md)
