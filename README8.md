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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d27fffac-2941-30c2-a4da-1c8a124ef882 | -2.68977 | -48.20378 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1beaf7d0-28a2-3177-9111-09f3b41a6819 | -7.6017 | -42.75507 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89e0f679-5e6c-330d-b149-0fedc9039070 | -7.60996 | -42.74562 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7f88243-2b56-3f22-ba1d-77525804f97f | -7.19687 | -44.3661 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a551d6d1-5fd5-3d8b-8e2e-47b93906c363 | -4.98087 | -37.2378 | 2026-08-12 04:14:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c84b0ac7-e535-32bb-b634-968859a9643b | -6.53895 | -43.11718 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c55be365-1139-3270-8313-30ee19b688fc | -8.4841 | -45.41793 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b92073d0-fdea-390e-bbee-bbe43703a3de | -6.9958 | -42.62825 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 35d19aa3-22ab-3a7f-88fc-eecd0191df35 | -4.65933 | -43.13212 | 2026-08-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6fbdd3a-af13-30bc-8a34-621ee04f09c3 | -6.89432 | -41.94014 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 753c07bf-86aa-3fe0-bdf1-9507340c038c | -6.54941 | -43.11526 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ff41f27-20d4-3ea4-8ab2-4e6f79beae35 | -8.36515 | -47.75346 | 2026-08-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee3d333c-1d9c-3ac8-9713-d97527fe4cbf | -2.77247 | -49.46976 | 2026-08-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e104da05-c685-317e-a1fd-40a1ba2f780d | -7.62764 | -42.74119 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 153631f4-0f19-3cf1-aa65-736ec1c5581a | -7.0279 | -42.13552 | 2026-08-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7281eb25-7784-3785-a57f-067bbfc91274 | -6.99912 | -42.62877 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 01194e96-3e12-3f44-98f9-c3d22250a47a | -6.04087 | -43.86563 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c48a1161-3be2-3f7b-832d-510b34348e29 | -8.60174 | -45.40662 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e350e305-0ac4-311f-a124-d02653f61904 | -7.27494 | -39.32107 | 2026-08-12 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3387a4f6-a86e-37b4-ab7b-5015819a4add | -7.621 | -42.74017 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcb33526-e382-3d91-a9f1-9abd2f4cf8ce | -7.39431 | -42.86535 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 157050e5-4b95-3024-b4f2-a6fefd5eef7a | -3.48508 | -47.68775 | 2026-08-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da5499ea-b7fb-35c6-868c-6c67c06de259 | -7.60224 | -42.75158 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f3b8154-51a5-33a1-a282-bac76082f085 | -3.05253 | -46.92756 | 2026-08-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6073f2f-6f48-3184-9327-366a0a8b43d7 | -5.73519 | -43.27699 | 2026-08-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eb1dbc1-8365-394f-81d2-8e2ec85f8a93 | -2.69006 | -48.20755 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e58b2aeb-7c27-3227-b209-0d4ac5e73362 | -7.38105 | -45.11042 | 2026-08-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a8ead6a-1234-3ba1-a815-d5a91e07bf72 | -2.76782 | -49.46904 | 2026-08-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5e8228b-037b-3ccc-9c13-56104ec30138 | -6.343 | -44.06402 | 2026-08-12 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b464a8c6-c8f5-36d2-94b1-0ae5b4f1ebf0 | -7.00077 | -44.82979 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a7fab21-25f5-3ab3-bcef-7099e8ec7eed | -4.72298 | -42.76802 | 2026-08-12 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f52ecbe5-e0a2-36a5-8350-d75a4eb3b8d9 | -2.41607 | -51.83686 | 2026-08-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3940531-df7a-31ef-a689-b340da944c93 | -4.77168 | -41.79911 | 2026-08-12 04:14:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd8bd555-6223-3540-b4e1-a56c56a56783 | -6.54503 | -43.12165 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f297aae-51df-3c74-b614-19f407fd6970 | -7.18964 | -44.36858 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f8f3ec9-c53e-3026-8817-63470787557c | -6.04364 | -43.86964 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3232d5b-235b-32a8-aaee-bfbc701defa1 | -7.0303 | -42.13618 | 2026-08-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 949a5d19-c1f8-39f1-aaa4-302b577fd34f | -7.45656 | -46.15126 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06e62cf5-6300-3653-bcd9-e101fe2c37d4 | -6.89149 | -41.93613 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a71471e-49e4-3e39-8a85-92db9cd1bf48 | -3.0573 | -48.74007 | 2026-08-12 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dcfde69-544c-3872-bc85-fa3462eed11b | -7.92546 | -45.11064 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8627c153-be72-3e5b-8e98-7306e6afa409 | -5.67924 | -49.82563 | 2026-08-12 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d84b412-18b7-3611-a8df-5be1d36af130 | -7.60503 | -42.7556 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2bcdc26d-59eb-3cb2-9c01-e4fb00ae3e71 | -6.54226 | -43.11769 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42ff676d-aa2a-3f4f-b873-547985ef7fea | -6.51824 | -45.64992 | 2026-08-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd2305e7-c649-3711-8e42-2612df3d0feb | -7.60117 | -42.75856 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29220cf3-39a3-3fa5-9cd0-f1dbbd70bac2 | -4.46915 | -45.90092 | 2026-08-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3546fc39-1ec5-3930-82cf-9672a0981211 | -8.47612 | -45.42415 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3326661-4cd9-3fbf-9ffc-ce031e0f59c0 | -2.69403 | -48.20445 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a94ecfc0-2a4b-3f4c-ae92-99501a410672 | -7.73931 | -44.55078 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa2b70f5-8ebd-3111-888a-a7d52e10df74 | -2.96147 | -49.26311 | 2026-08-12 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d7a3aa7-c8e0-3e25-9ef3-80f65a85574e | -8.11004 | -47.18518 | 2026-08-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0344685-8f84-3f49-9128-d556ec66ea7d | -6.53841 | -43.12063 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0709070d-4259-3d34-bfb2-29e742df2a73 | -2.80542 | -48.59425 | 2026-08-12 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e8c07ad4-c001-32ab-86e1-0ddcde40152e | -3.96489 | -43.11485 | 2026-08-12 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4d46067-0226-36a9-88c3-3f6f5bf80d87 | -7.74891 | -45.02637 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb5a0e69-6b9a-3e86-8259-ad5cc3112186 | -6.77264 | -42.66462 | 2026-08-12 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fbddfb88-f880-36b6-8115-51803578db0f | -6.89377 | -41.94369 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3132ebdb-c021-3f01-a274-22724b3172ee | -6.00943 | -47.40896 | 2026-08-12 04:14:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb9e749d-22ea-3eb3-bf56-4b408fc1e6c4 | -8.08102 | -44.83907 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a0f2ac0-524c-3586-bcaa-b5e33a0e69d6 | -7.62432 | -42.74068 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ac490fa-9773-3eb7-b5f2-4a2722360cb4 | -3.11493 | -47.91169 | 2026-08-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bca9fac-bdb8-305b-b9f8-29f0189a31c1 | -6.5428 | -43.11423 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf23938b-a69c-319f-81fa-d0323fad8226 | -8.35807 | -45.98179 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| e8e9675e-a586-342b-86b7-67264d1f3d02 | -8.6241 | -47.45875 | 2026-08-12 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5f5c23b-410c-3b62-a6e5-7889b0d83626 | -6.95444 | -39.72591 | 2026-08-12 04:14:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0399e4d7-834c-3dda-913a-377bb043ca52 | -7.19354 | -44.36557 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fb7876e-5909-3de2-af55-ba7830cba5f1 | -8.07191 | -46.51994 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48a99997-0b1b-3d44-a998-eb9252998cbf | -7.63105 | -42.76322 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67ccb192-b0fe-315c-a8d6-d99318864fed | -7.92208 | -45.11009 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 530c14e7-fffc-3bdb-8b11-7de759ce39ff | -7.38876 | -42.85735 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f7d28f8-7d84-32e6-9bca-08b7cf758dfb | -5.92652 | -39.46631 | 2026-08-12 04:14:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd8e8619-0992-395b-b8aa-c0cb39502b0b | -2.2991 | -47.88282 | 2026-08-12 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42de3c1-6372-355d-afc9-aaa768fa3107 | -2.68943 | -48.21153 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 815cee9a-a561-3d22-8739-3463b5e978bf | -8.83285 | -45.9511 | 2026-08-12 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4fabd1f-1c63-33f6-a5be-219f2da4a797 | -6.99858 | -42.63225 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85e98b99-273e-3a8d-a1ca-944b252d2a21 | -6.8555 | -46.00887 | 2026-08-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8b36043e-e0e8-3f04-a421-4ea6c8aeff6c | -6.34022 | -44.06001 | 2026-08-12 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c98a678-330e-3868-b41f-99b00e391b2d | -6.10371 | -44.3307 | 2026-08-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebcbbedd-42fc-3cc8-9669-fb4e9e1efd5f | -8.49548 | -45.41231 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7032931-dd5c-3431-b5d1-a04c775c3767 | -6.8904 | -41.94325 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5d797e71-50c3-37aa-97fe-004f33c23fdb | -7.72479 | -46.22067 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d93814f-8e6d-326a-9318-949db8c917ef | -8.07321 | -46.51181 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 684db6d0-07b8-315c-bda2-d28334caf7a3 | -8.35522 | -45.97739 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3171588a-71f3-3b71-bf23-a03e84f1dd2a | -7.74611 | -45.0222 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4970a7e-2c29-3c21-bf0f-d2edad3445f9 | -6.34355 | -44.06052 | 2026-08-12 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0636f398-273d-3e32-8794-c345e94fde2e | -7.92884 | -45.11119 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 693f4e0c-8af7-3c58-a0e6-2f5319eb0eb5 | -3.02436 | -39.97928 | 2026-08-12 04:14:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa8983db-ae33-33f3-a5ee-d0620dffe8b8 | -6.553 | -43.11642 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| add50f9c-438f-374b-b4ed-4481b2567f21 | -2.96083 | -49.26377 | 2026-08-12 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56ee2649-38e9-3e78-9eb3-95f92430ef6b | -7.62172 | -42.77963 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f7eb3d6-442a-3f0b-8de6-b132d3277e8c | -6.05084 | -43.8672 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dd5dd99-c07e-3f79-b92b-df0bd7376efd | -7.38213 | -42.85633 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9305564a-421d-37b3-a4dd-0b8f392aa6f0 | -6.34244 | -44.06752 | 2026-08-12 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6ee98d6-5cae-38d9-8883-2d717a4f930a | -8.78523 | -45.79179 | 2026-08-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1db1e1da-bb18-3950-a34e-3d9539b32b28 | -9.52929 | -40.34032 | 2026-08-12 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b66dc030-3683-301b-b97d-52261decd31f | -7.37048 | -42.84383 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc929aca-ba46-327f-ab0d-2c0ae1bc4445 | -6.09533 | -41.814 | 2026-08-12 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a6682b0-cfcf-3d58-9ae2-7300c2a75db3 | -5.72873 | -49.14436 | 2026-08-12 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beb8fc93-18e0-3e8d-9ebc-fb3ddd1210a7 | -7.6061 | -42.74861 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
