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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12abde11-d7da-3b11-ac80-e1561fa9cdbf | -8.03365 | -47.68975 | 2025-08-18 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 214c49c1-f083-3fe9-9d94-2d5e3c07f980 | -3.3826 | -47.598801 | 2025-08-18 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0929567-8476-3876-a139-ae9de93b63f7 | -7.5478 | -45.425098 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0601480-6a80-3496-86c9-5996c0021ebd | -4.9188 | -43.230301 | 2025-08-18 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bf10179-e977-3880-841f-4e68bfaf4698 | -6.429 | -44.771198 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96bccf25-39f6-31c8-b5bb-77498a9adbd9 | -18.264799 | -44.9804 | 2025-08-18 00:09:00 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 85ad3a48-8ee6-39d9-ad88-44307562378f | -22.5308 | -46.8839 | 2025-08-18 00:09:00 | METOP-B | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8704f083-e7e3-3197-a3e1-448e4174bffe | -13.9806 | -48.092098 | 2025-08-18 00:09:00 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7ceeb270-1f64-3d05-8023-fe46346d3382 | -13.2316 | -50.749901 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abd752a7-99f5-38ac-b618-b3d917dbef91 | -13.5796 | -46.9846 | 2025-08-18 00:09:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 887bba23-88a9-3aed-84b9-bce3aabdfe2a | -16.796801 | -50.086399 | 2025-08-18 00:09:00 | METOP-B | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b93643d-c72b-3999-917f-3352d39bba63 | -4.909 | -43.232498 | 2025-08-18 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 673bbb4a-77d3-3b97-9c26-f81a88e55a16 | -6.0295 | -44.334099 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38585e1c-1b00-33e9-ae4f-ddc1ce6535de | -12.9775 | -56.789001 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9a8cfd0-26c8-3663-a8c5-3c6726303cac | -12.9968 | -56.7854 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6ae410c-8c8f-3a29-adac-04127bd1f9c9 | -11.8066 | -44.932301 | 2025-08-18 00:09:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5b8865-6d89-3230-aded-1f2a576b2d15 | -6.564 | -44.462299 | 2025-08-18 00:09:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eff0c474-9459-3274-aff3-754236190638 | -8.7975 | -52.060501 | 2025-08-18 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f050232-64b4-32b5-8ea7-93bd59d67399 | -19.3654 | -42.925499 | 2025-08-18 00:09:00 | METOP-B | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a259bb0-c0ac-3488-9428-23b9358a014b | -13.2554 | -50.766602 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee6d9bd7-eecc-383f-b7f1-7213ad64793e | -8.0437 | -47.673 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8221c77-a3a8-31a0-9029-2975cf54f194 | -23.181499 | -49.515999 | 2025-08-18 00:09:00 | METOP-B | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dccf7032-b67e-3e8c-90e7-1e73667d5536 | -15.4942 | -48.525101 | 2025-08-18 00:09:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37962e1a-3ef1-3365-a588-f7a68b93cc52 | -12.9919 | -56.8134 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3db707d0-00db-3afc-80f2-b555fc5c66c4 | -13.5676 | -47.789501 | 2025-08-18 00:09:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b65b3618-7550-3992-bef3-b533203b914f | -2.9586 | -49.057899 | 2025-08-18 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141a9ed7-44f1-3346-85e2-e8cd91db13ba | -4.9135 | -43.252201 | 2025-08-18 00:09:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 972352b6-e11f-32a1-a0ad-8793e59a71d6 | -5.6552 | -43.385502 | 2025-08-18 00:09:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac32cd6c-75df-3cf9-8bcf-ee403388447f | -7.5153 | -45.463299 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80ea8aca-515b-3c92-a50f-7e90fa0d803b | -5.9866 | -44.103901 | 2025-08-18 00:09:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89204ef6-abdc-3fd3-b4d5-3be0eff42376 | -13.2358 | -50.770699 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7024b0de-27c6-3cd0-92c7-28ddacd167ee | -3.1617 | -47.532299 | 2025-08-18 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b52dc696-3e48-3d0e-b6a9-c5872933037e | -7.5576 | -45.422798 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6470ce-24a7-3d63-aa4a-54cf00d1b1a9 | -4.7837 | -45.326401 | 2025-08-18 00:09:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d70c092e-f083-3a8a-a09c-03b6a932ada3 | -5.1431 | -48.099201 | 2025-08-18 00:09:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51dc2658-5251-38cc-9c3e-3f377bd38494 | -5.7892 | -43.874401 | 2025-08-18 00:09:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06d85ea5-7327-31b6-bff3-443775f677fd | -23.679399 | -47.403099 | 2025-08-18 00:09:00 | METOP-B | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc76f7c9-bdee-3631-bea1-0c376b7ad2ce | -19.1462 | -47.0247 | 2025-08-18 00:09:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1604595-4585-3ded-9c9d-5ed49967ef86 | -12.547 | -48.4874 | 2025-08-18 00:09:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcf84ea-7894-3def-b13f-f05b00a1f7c9 | -6.1177 | -46.662102 | 2025-08-18 00:09:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40324084-0227-34f3-b3b7-1becdd6024c1 | -7.5136 | -45.456001 | 2025-08-18 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c16471fd-e7fd-31f1-b228-b669c0c32554 | -5.6747 | -43.380901 | 2025-08-18 00:09:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8d2bb36-dde5-3e61-a991-47bd1fa4102b | -20.219999 | -47.025002 | 2025-08-18 00:09:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5038b6ad-2585-3f3e-bce4-1be692181739 | -17.0965 | -49.848598 | 2025-08-18 00:09:00 | METOP-B | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 502dd21f-472f-3f10-b49f-4ac013fe15d0 | -3.1632 | -47.5392 | 2025-08-18 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb7c2e79-53b3-3368-b58e-fbffdd895846 | -11.847 | -51.561699 | 2025-08-18 00:09:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b59de573-3b59-33e7-8d9f-9b08884a92eb | -6.4272 | -44.763302 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cdd7c71-1ea1-37c9-99ab-1deb6fcb57bb | -3.9859 | -42.5378 | 2025-08-18 00:09:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f45eca47-f2f0-3eb9-b5d2-62683f31c41b | -4.1356 | -49.3498 | 2025-08-18 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e0faa1-666f-3fa4-b3aa-21decfa31b0b | -3.9736 | -42.5289 | 2025-08-18 00:09:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94ec9e5a-1f60-345c-9481-e3f713568cc4 | -5.7572 | -46.662399 | 2025-08-18 00:09:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 912d697e-32d4-3658-9146-cadbc83360d2 | -22.532499 | -46.892601 | 2025-08-18 00:09:00 | METOP-B | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64f7138a-24a0-3efa-b9b9-a784b77417c9 | -5.1544 | -48.103901 | 2025-08-18 00:09:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71dc3592-c3e7-3e35-bbe9-f1eb5afea6e8 | -17.628201 | -44.283901 | 2025-08-18 00:09:00 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb5f6e05-fc83-3a05-bb99-bb1754e419ea | -13.2282 | -50.7831 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a74378bc-ffba-3c05-8d04-1713a38fb4c6 | -7.8059 | -45.1563 | 2025-08-18 00:09:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 029400ec-4977-3fca-9c20-b33b41a5fce2 | -12.6339 | -46.889801 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f464a368-3c8c-31d3-968a-2e3896ca0ab2 | -4.7721 | -45.3209 | 2025-08-18 00:09:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85d8aba5-92d2-39a1-88b7-942a3b69bb62 | -5.6574 | -43.395 | 2025-08-18 00:09:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8762b794-640a-3ab7-a85c-471f04b2b96b | -6.4308 | -44.779099 | 2025-08-18 00:09:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98994711-4547-3920-8105-c058f2f8ba07 | -10.8592 | -48.464001 | 2025-08-18 00:09:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5306591a-8b2a-3f33-a906-895c2af8eaee | -14.1662 | -41.585701 | 2025-08-18 00:09:00 | METOP-B | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a5410984-790e-368a-83f0-9f0da0087461 | -13.5976 | -46.973 | 2025-08-18 00:09:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cffbd3d-d8b2-3cb1-9431-0c82e62051c6 | -8.2386 | -47.8559 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71a815ed-1836-32e1-9d99-c027409d25ac | -13.5961 | -46.965801 | 2025-08-18 00:09:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b7a0057a-906f-32e7-8f6e-cf9e5308a9e1 | -22.716801 | -47.426399 | 2025-08-18 00:09:00 | METOP-B | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a97b9074-f350-3bbc-95a9-e1c81051136f | -14.9975 | -54.776699 | 2025-08-18 00:09:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2fe1c4e-7ec9-3575-b3ae-e396f59b9abc | -13.0112 | -56.8097 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19e47ffa-9f62-3733-baf9-9d863b5283b2 | -12.6287 | -46.9133 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8b1fb50-f4a2-3660-af83-8c431f35d87c | -12.6324 | -46.882702 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 951dec5a-7ea7-3595-b0c4-542bffbf4048 | -12.4503 | -46.990501 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f90ada98-27c2-3124-aefc-62c3797c2fdd | -11.1416 | -46.8857 | 2025-08-18 00:09:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc6bb5a-1920-3ee3-baa6-d64b7e205d12 | -15.9639 | -43.894402 | 2025-08-18 00:09:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| decd17e9-c085-3554-be64-5f4c7e75b62a | -22.1444 | -44.8158 | 2025-08-18 00:09:00 | METOP-B | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31b24004-db33-3883-b50a-a27c6815f6d8 | -6.1898 | -53.490101 | 2025-08-18 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ac79fb-7ab2-35d4-81e3-90f2a04f6f57 | -13.1692 | -54.8964 | 2025-08-18 00:09:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 524ce73e-637d-386d-8838-4c9f842b8a10 | -13.589 | -47.7453 | 2025-08-18 00:09:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5e0076f-055b-3927-89e8-eaed8aff8b8d | -6.5542 | -44.4646 | 2025-08-18 00:09:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45e6c04d-107d-3536-bfad-677a9ec37e9f | -19.154301 | -47.0144 | 2025-08-18 00:09:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 45420365-96d0-32b6-b0d5-c3a914b4df67 | -17.164101 | -46.218899 | 2025-08-18 00:09:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2399382d-598e-391c-bf08-98b2c07a4cf0 | -11.1333 | -46.894901 | 2025-08-18 00:09:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de485e77-f1da-3085-95ba-24f4be8f8f39 | -20.218399 | -47.016602 | 2025-08-18 00:09:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64dbe69c-6bc1-39e9-a637-deed54c91550 | -13.2337 | -50.7603 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1be636dc-6562-3699-bdb6-825c2c057e35 | -13.2512 | -50.745899 | 2025-08-18 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbea7d39-8190-3c05-bbe4-f604d850247c | -19.156 | -47.022499 | 2025-08-18 00:09:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4897e8c-3d7d-3e90-b38a-ed856c35cb0a | -12.9871 | -56.7873 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09dab973-3979-3f0b-942a-96d7226d27e7 | -5.1416 | -48.0923 | 2025-08-18 00:09:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3ac96a-857a-31c9-a22d-b534e8dba0f0 | -15.0035 | -54.754601 | 2025-08-18 00:09:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2f250e4-245f-3b59-8bbb-76512469d504 | -8.0421 | -47.666 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40dfcde2-e1c6-38b7-ad46-28dae327bca9 | -14.9938 | -54.756401 | 2025-08-18 00:09:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 795e554b-feaf-35bc-9737-a5379326f72b | -8.7868 | -49.9888 | 2025-08-18 00:09:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2ba2bf-03e9-371f-be19-cf3234edcc06 | -5.6628 | -43.373798 | 2025-08-18 00:09:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 063bc533-1f40-312b-8aca-185a19e28e84 | -13.566 | -47.781898 | 2025-08-18 00:09:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e169bed-bc69-32e7-b013-27c081aa4727 | -8.0339 | -47.675201 | 2025-08-18 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5f60ded-bfd0-35b5-9ec9-21ee83d78278 | -13.0016 | -56.811501 | 2025-08-18 00:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad9f9c1-f5a7-3676-b346-1cb82d46b4c9 | -12.6241 | -46.891998 | 2025-08-18 00:09:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9025db80-1ef5-372d-ad8c-bce0c01fe5ab | -3.3842 | -47.605598 | 2025-08-18 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49e8fe36-4b2f-323d-aab8-f437545a95e0 | -9.874 | -44.687 | 2025-08-18 00:09:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e296dc1-8f15-399a-a2a2-cecd68805a6a | -13.5811 | -46.991798 | 2025-08-18 00:09:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 983d8117-2dde-3068-abc4-d573517b6604 | -20.2265 | -47.0061 | 2025-08-18 00:09:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
