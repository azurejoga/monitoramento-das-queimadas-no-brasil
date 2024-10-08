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
| b27105cd-3abf-38fe-b2f0-507568aef01a | -17.1584 | -56.1429 | 2024-10-08 00:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| a25d37a1-826d-3d2c-8268-2fd89cb87ec8 | -17.1588 | -56.1222 | 2024-10-08 00:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| c2656fa5-cb06-3891-be2d-144edf033af0 | -17.3353 | -55.0156 | 2024-10-08 00:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 63bc1753-37b4-3df6-88a6-b84881642144 | -10.4083 | -49.386398 | 2024-10-08 00:06:43 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f521c0a5-de40-3a06-84a7-f007c4bedef1 | -8.3718 | -40.419399 | 2024-10-08 00:06:45 | METOP-B | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 81750ba4-77c1-361c-9860-87ea60aabcb6 | -8.3734 | -40.426399 | 2024-10-08 00:06:45 | METOP-B | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1a330d05-a8af-35b3-8e3c-2a3d439076ca | -9.2765 | -45.3013 | 2024-10-08 00:06:48 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cae051ca-2fd9-36f9-a701-5bb36a136274 | -7.0312 | -35.498798 | 2024-10-08 00:06:49 | METOP-B | MULUNGU | PARAÍBA | Brasil | 2509800 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 7e68dcf2-3864-3ca0-97d2-6d8b17adc3ca | -8.4227 | -41.933601 | 2024-10-08 00:06:50 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f3892be-43e0-35de-9dd0-f2c5383eea21 | -8.4242 | -41.940601 | 2024-10-08 00:06:50 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3bf8e729-4380-37ea-bd9c-554c996a365d | -8.4129 | -41.935799 | 2024-10-08 00:06:50 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f9e3c86-fdcd-342b-b5ec-f5e60f31217e | -8.4144 | -41.942799 | 2024-10-08 00:06:50 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c9f3e3a-4e38-36c9-9a21-c0950f875977 | -7.9715 | -40.017399 | 2024-10-08 00:06:50 | METOP-B | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| dfb121b7-3617-3524-8578-ee6d3e81f309 | -18.6192 | -57.2603 | 2024-10-08 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| fd815300-fce9-33ae-9cbc-9ebd4fe6faa0 | -18.6195 | -57.2396 | 2024-10-08 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 1f352342-79a1-3953-8fb9-4987c97feeb3 | -18.6394 | -57.237 | 2024-10-08 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| d8cd6b27-b0dd-3778-a93b-628b4334d9b5 | -18.7183 | -57.2682 | 2024-10-08 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| aca2fd3f-59ea-36eb-ab32-d30e0f33b6c0 | -18.9038 | -50.247 | 2024-10-08 00:06:51 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e5075023-9281-3822-808e-fc9d1eee6435 | -18.9044 | -50.2246 | 2024-10-08 00:06:51 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 79fbf27b-4b1c-3140-b8de-6f91fcb75e65 | -18.9239 | -50.2431 | 2024-10-08 00:06:51 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 00e34c45-6de6-354e-bd85-eede9402c64b | -18.9245 | -50.2207 | 2024-10-08 00:06:51 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 77995d22-a182-37b6-a179-4b1bde3d9cb9 | -18.9441 | -50.2393 | 2024-10-08 00:06:51 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| dda7e176-58dc-33d8-82ed-0c6df5332d61 | -9.126 | -45.508499 | 2024-10-08 00:06:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07aa7200-f677-3827-b4e3-77992373c3d0 | -19.4218 | -41.176 | 2024-10-08 00:06:53 | GOES-16 | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 5cbd8b90-6832-3546-a893-e9b934a5ebd7 | -7.9685 | -41.6045 | 2024-10-08 00:06:56 | METOP-B | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dfd784f1-6b2a-3168-8920-ec32bcc03928 | -20.3732 | -43.9468 | 2024-10-08 00:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 247.9 |
| 530bab23-2c03-336a-a5f8-9f45afd71eb9 | -20.374 | -43.922 | 2024-10-08 00:06:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 4d91b005-5211-35fc-9178-8c44c0dfc4b0 | -20.3938 | -43.9412 | 2024-10-08 00:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 269.6 |
| 612fa5d3-44fe-3e7a-836b-db2008254f8a | -20.3946 | -43.9163 | 2024-10-08 00:06:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| 462d8dcd-7eff-34e4-a6d2-76b635dced15 | -20.4251 | -47.6688 | 2024-10-08 00:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3b2b1321-5a46-39e3-895c-8fac17235525 | -20.4258 | -47.6453 | 2024-10-08 00:06:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 0583fc46-6cce-380e-a175-2a97387f5b72 | -20.4264 | -47.6218 | 2024-10-08 00:06:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f954a209-37d0-393e-a6aa-97bba3dd1733 | -8.2438 | -43.738998 | 2024-10-08 00:06:59 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63603f71-6338-330d-9b13-1ca649fa38e7 | -7.2431 | -39.3559 | 2024-10-08 00:07:00 | METOP-B | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e8dc9f59-e806-3ff2-a772-4ec7f856e6d5 | -8.3108 | -44.094299 | 2024-10-08 00:07:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a03be431-df1a-3b10-961b-5034757518e1 | -8.309 | -44.086102 | 2024-10-08 00:07:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b50e79cd-623f-3718-a4e2-a07823baca4f | -8.1918 | -43.594501 | 2024-10-08 00:07:00 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7134aee2-d14c-34f8-8a70-28d7a748b6f3 | -8.2921 | -44.055599 | 2024-10-08 00:07:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b2bb08f-c34d-30e3-9ac3-1a8c36ed93bc | -7.9284 | -42.442699 | 2024-10-08 00:07:00 | METOP-B | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2103aa8-cccf-344a-aad2-5282e2caf37e | -7.8245 | -42.2062 | 2024-10-08 00:07:01 | METOP-B | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d77cc71f-7e2f-3eb9-b39e-bde65753e2fa | -7.8261 | -42.2132 | 2024-10-08 00:07:01 | METOP-B | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0e5451c-3d0f-36b4-8433-bfc4fd7a67f6 | -21.0712 | -47.2331 | 2024-10-08 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 82f9ee7f-ab73-3d7f-847f-fbb4b363ba8c | -21.0719 | -47.2094 | 2024-10-08 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ac671c0d-1cf6-3745-a8a5-c8c41680cdeb | -7.5989 | -41.7015 | 2024-10-08 00:07:03 | METOP-B | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24ca507c-cc1b-3ac4-8cd5-4f067677936e | -7.6004 | -41.708401 | 2024-10-08 00:07:03 | METOP-B | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b2c64e6-1582-366b-9076-88fc28802bfa | -8.1411 | -44.400398 | 2024-10-08 00:07:03 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3184ec7e-fb06-33fc-9464-8401c9e0a53e | -8.1429 | -44.408901 | 2024-10-08 00:07:03 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f29720e4-4f9b-3efc-aacb-bbf18a4d8c45 | -7.6514 | -42.399799 | 2024-10-08 00:07:04 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d71b3c03-376b-3a6e-ae0b-c236d8663240 | -7.6588 | -42.4799 | 2024-10-08 00:07:04 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d344349-e2d6-3611-8257-23b9417fff49 | -7.6604 | -42.487 | 2024-10-08 00:07:04 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e161899-7b84-355d-9f1c-f6ad59b0081a | -21.3865 | -55.6774 | 2024-10-08 00:07:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c4d09769-b260-3497-b1d5-00aeb2f918a7 | -7.6522 | -42.4963 | 2024-10-08 00:07:05 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca943f66-721b-3aa5-af15-5fbf905ab493 | -7.6302 | -42.397099 | 2024-10-08 00:07:05 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49e83b34-74ad-3759-a384-c4bdccfb6917 | -7.6318 | -42.404202 | 2024-10-08 00:07:05 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8a3029f-a1fd-3dee-94a2-f91abf33f944 | -7.6506 | -42.489201 | 2024-10-08 00:07:05 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d164ce65-bd5d-3a59-bf3d-fe1a9b690cb8 | -7.6538 | -42.503399 | 2024-10-08 00:07:05 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad2457b9-43bc-30ff-87ac-21f7821a9b3d | -7.7799 | -43.0746 | 2024-10-08 00:07:05 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 266e9ab8-f033-393e-bb66-c40cfa858c89 | -7.7815 | -43.082001 | 2024-10-08 00:07:05 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10146399-1575-343b-928f-3302ccca9f4d | -7.622 | -42.4063 | 2024-10-08 00:07:05 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72981942-6f9c-3952-8dca-b81421f66c0a | -7.6235 | -42.413399 | 2024-10-08 00:07:05 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43dbee3c-c99e-3dac-92cd-e81ef890d827 | -7.644 | -42.505501 | 2024-10-08 00:07:05 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d0f9229-d308-3189-b42c-5431dbaad4ad | -7.6455 | -42.5126 | 2024-10-08 00:07:05 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 573f0bff-22d4-3919-893b-6f4786fe7588 | -7.7717 | -43.084099 | 2024-10-08 00:07:05 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c627a0ba-931f-3fcf-ae2d-2f55522cc53a | -7.6153 | -42.4226 | 2024-10-08 00:07:05 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20f36ab7-d614-3cdc-b8ab-9f4a3f1fa745 | -8.009 | -44.3587 | 2024-10-08 00:07:05 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 41d54bbf-b320-3963-be28-fcdbf560cbf1 | -8.0108 | -44.367001 | 2024-10-08 00:07:05 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c257008-7671-3f34-897b-323b6bee18e3 | -8.5321 | -46.5681 | 2024-10-08 00:07:05 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4afaeed-a4c5-3bb8-8c64-ca36b25d89df | -7.9992 | -44.360802 | 2024-10-08 00:07:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c360a5b2-e006-3de2-8dff-a97f4b8e9fa3 | -8.001 | -44.369202 | 2024-10-08 00:07:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c78b023-58a5-349e-aac3-6538c15b982f | -7.3246 | -41.994999 | 2024-10-08 00:07:08 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f362cea-5639-3d54-976b-e056f63539ea | -7.3056 | -42.233101 | 2024-10-08 00:07:09 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0130523e-1ead-358c-a749-f96b70dde7a5 | -7.3072 | -42.240101 | 2024-10-08 00:07:09 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b834601-761c-3758-a1af-7baff03ffa29 | -22.8035 | -46.7612 | 2024-10-08 00:07:11 | GOES-16 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| b14f1ed0-f6df-31ca-b029-14dba8447b21 | -6.4272 | -38.812 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 49dd6b8d-40c1-353c-afb9-55efca1da320 | -6.429 | -38.819901 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7ddfcfcc-0b89-3132-b684-4f717549a9ca | -6.4308 | -38.827801 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d8f9c1fd-edcb-35b3-9a8e-edb31c30cb90 | -6.4156 | -38.806499 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3bc5ea75-ec80-343b-a195-b4e557b118b3 | -6.4174 | -38.814301 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a6b33fdb-1b53-3bcb-a6e7-00d1a134c871 | -6.4193 | -38.822201 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 19bee6bb-6fd5-38ab-8e5f-136df9e3aa49 | -6.4211 | -38.830101 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8a96bc24-ae87-3658-b2ed-b7e56611fc33 | -6.4229 | -38.838001 | 2024-10-08 00:07:11 | METOP-B | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2852029c-be44-34b7-9a60-d75742ce1059 | -7.8604 | -45.333099 | 2024-10-08 00:07:11 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f374709-e779-3e85-9d20-39d16df7b9ad | -7.8624 | -45.3424 | 2024-10-08 00:07:11 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6f9583b-2916-3588-8549-b4ada01deb3c | -7.8506 | -45.335201 | 2024-10-08 00:07:11 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42ca1e75-40ff-3f01-b405-1795e594bf60 | -7.8526 | -45.344501 | 2024-10-08 00:07:11 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1a55521-2c40-364a-9a25-76307cca4620 | -7.7501 | -45.153599 | 2024-10-08 00:07:12 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8353a394-117a-3a92-a59f-e705f0975f50 | -7.1438 | -42.616001 | 2024-10-08 00:07:13 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3255826-edcf-38b6-a4c2-f3425314ebb7 | -7.1355 | -42.625301 | 2024-10-08 00:07:13 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d618c7c5-f256-383a-8450-ea42603556ea | -7.351 | -43.648701 | 2024-10-08 00:07:14 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 07b0f5d7-4d79-34f9-b56b-d4d4a31134a5 | -7.3527 | -43.6563 | 2024-10-08 00:07:14 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fae0444-a2ae-3dd5-bece-703b810666e4 | -7.3429 | -43.658401 | 2024-10-08 00:07:14 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e41e94d3-7159-3a7e-87c5-90db34336f26 | -23.9049 | -54.2392 | 2024-10-08 00:07:18 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 7328cc6a-f084-30ee-87db-9e910429e414 | -6.8324 | -42.7892 | 2024-10-08 00:07:19 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bba68374-505e-32a0-a6eb-7e10fb09ae8f | -6.834 | -42.796299 | 2024-10-08 00:07:19 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| df8dc1f0-e77d-3c56-ae54-e856be16c325 | -7.2884 | -44.962399 | 2024-10-08 00:07:19 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0b121e-59f7-3184-9407-4ca2e8645106 | -7.2748 | -44.946899 | 2024-10-08 00:07:19 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fefc82e-09bc-3d33-bf9d-bb1c9fda878b | -7.2767 | -44.9557 | 2024-10-08 00:07:19 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf5db35-eb0a-3bcf-ac87-a06e3cff3fc4 | -7.265 | -44.949001 | 2024-10-08 00:07:20 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3110133-a9e7-3a3b-ae94-66848505ab75 | -7.2669 | -44.957802 | 2024-10-08 00:07:20 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be3b8557-3314-353a-a30b-f0e9a0818eb4 | -7.0993 | -44.564098 | 2024-10-08 00:07:21 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
