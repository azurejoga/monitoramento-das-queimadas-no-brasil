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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebfa5f85-37a6-34fe-9291-4effb7178f08 | -14.8071 | -51.3809 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b2a01cf0-abe2-35f5-a1fc-c259119d5143 | -5.5771 | -42.1493 | 2025-09-21 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| cf2b9514-4685-3f3b-9fff-de2af1ea997a | -8.8801 | -46.138 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| cbf4c436-44a5-363a-b0ff-053de43d55a8 | -12.4361 | -45.1052 | 2025-09-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| e0fbe7be-a4ac-3e1e-9635-c3b13b457756 | -17.1179 | -45.9256 | 2025-09-21 14:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 353a7f96-f197-36e4-aa3b-0d4a3d8f4671 | -12.144 | -44.2899 | 2025-09-21 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| fd402d4f-e371-335e-8e72-8f68e7a20a47 | -8.8993 | -46.1135 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e2305fdb-8783-3675-9ae7-08ff7e2a2ffc | -9.8442 | -46.1205 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6f2bd58b-4106-3582-a9f0-7d9083ba87c2 | -9.771 | -45.9484 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 90da750d-aae8-319a-bebc-d99a073c33f0 | -12.1353 | -44.7576 | 2025-09-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f21f7832-8801-3311-a4e2-2d6896b90a9e | -12.3133 | -49.9881 | 2025-09-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 96501cb1-a8a9-3945-ae84-01710364775a | -7.5275 | -44.3182 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d63aa666-90e5-32f5-9863-6183f2fad4d1 | -15.4653 | -55.9966 | 2025-09-21 14:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5f454325-d8e0-3471-9595-60c79d50a056 | -4.4084 | -43.0551 | 2025-09-21 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 94d6a0df-3ee8-3b4d-8fae-7ca410f965d3 | -10.0547 | -45.9824 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 04e736ee-dfc7-349a-9395-03a01114e396 | -12.4169 | -45.1082 | 2025-09-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 97b88803-4b8b-36b0-b1cc-38efa21ac59b | -5.139 | -42.9376 | 2025-09-21 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 59c9b623-9c9b-35e5-8091-18b063d83616 | -11.429 | -43.5307 | 2025-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| c12094d5-a5ec-38c2-b6ac-c00b68734dbf | -5.5395 | -42.1522 | 2025-09-21 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 6e108c8d-29fa-3069-b40b-66323e740145 | -12.7337 | -47.7391 | 2025-09-21 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 39fd7b64-15f1-3f30-8d1a-33e3479b1a82 | -15.4459 | -55.9989 | 2025-09-21 14:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| eb2eb225-8a2c-395e-817c-7f76c5aade48 | -16.8727 | -43.8894 | 2025-09-21 14:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ac3b0642-418a-394b-b41c-7ff542290a32 | -22.7264 | -51.4176 | 2025-09-21 14:30:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 160.9 |
| bac05a4a-e26c-374c-a4ab-f3b5779ececb | -12.6921 | -46.8482 | 2025-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7655e027-8317-3a57-9b44-4ed907e4aa6f | -8.8615 | -46.1175 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7b6ef598-a738-3256-8c25-35c29be8aa60 | -11.4665 | -43.5722 | 2025-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 841f29bb-dc90-34cc-b2bc-53c22aead851 | -17.0973 | -45.9532 | 2025-09-21 14:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 3f1eb5fa-4b7a-314c-8c5e-5decf2ad4833 | -12.711 | -46.868 | 2025-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d3663756-8aa8-310c-a1d2-1d077df023e4 | -12.2941 | -49.9904 | 2025-09-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0c60e6a0-1ba8-3992-a279-7570b237aa4b | -7.6007 | -44.4952 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5e3328d8-053e-3c3b-b7dd-17c8da8020a9 | -14.3361 | -52.9318 | 2025-09-21 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e6476172-0c59-329f-b0a0-2b09d458d7da | -9.0078 | -45.0584 | 2025-09-21 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0d2844c7-6211-318e-8d52-a2f14a8fe9c0 | -10.0128 | -46.2583 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f9701999-b7b0-3b11-bf79-b7157ad9f406 | -7.62 | -44.4474 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4bb1254e-9a93-313d-9658-db68ff2e39e2 | -10.6741 | -46.4477 | 2025-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b24a893f-45de-307e-bdb9-a16bcf9b80f8 | -11.4853 | -43.5929 | 2025-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 4e7c757b-fa3f-3329-b645-4a5cb16cb0d2 | -11.2306 | -46.1722 | 2025-09-21 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| a0bb9fa9-188f-3169-bb18-e80be2398b00 | -12.1156 | -44.7839 | 2025-09-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 4b484d2f-62c2-3b24-a33f-fddaed5a92cb | -9.629 | -46.617 | 2025-09-21 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8ad02856-bbe2-396f-9cd5-8a4c4ab22d08 | -12.6088 | -45.1244 | 2025-09-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 581f3ebf-37d6-3315-b2f5-902c8c8823ec | -14.5107 | -44.8695 | 2025-09-21 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 51e15fbe-e257-307c-b381-21eb05f062cd | -12.4056 | -51.4113 | 2025-09-21 14:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0ebe7986-00d8-3949-8274-4348d06d7428 | -12.2921 | -50.1201 | 2025-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5aab9f14-fa82-33b1-80e3-de98260abe26 | -10.2621 | -46.0703 | 2025-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 1e7e4af3-a9e3-3ca6-b5f8-4aa9ab0476df | -11.4097 | -43.5336 | 2025-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e9e57673-e569-3ade-83df-7223097cbd42 | -12.4357 | -45.1284 | 2025-09-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| bdb987c0-d78d-394c-b39b-06ceb26433b8 | -9.184 | -44.6251 | 2025-09-21 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 9b08d732-e7b9-3b6e-9921-f66afceba482 | 4.3344 | -60.7406 | 2025-09-21 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| decc666b-eb46-381f-9227-c01bc771baa3 | -12.9157 | -50.5589 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4101f84e-f168-3b30-b6a7-aba008335403 | -12.1344 | -44.8042 | 2025-09-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 4ae04822-4814-36bc-8176-66c99a53deb6 | -11.215 | -49.6224 | 2025-09-21 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| d7f0edea-ce4e-325f-826c-87727c23e1b7 | -4.3695 | -43.2674 | 2025-09-21 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 794e9178-6b4c-3ac5-b461-163a8ce82a9d | -12.8589 | -50.5231 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f2f3defd-8de8-385f-947c-fc428fa02f0e | -12.451 | -49.7328 | 2025-09-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 425d9c68-8a47-3be7-b163-d46ac01f6a9a | -10.0314 | -46.2786 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4ece4abd-9bf9-3ec5-b537-53a319581c98 | -3.8228 | -44.1063 | 2025-09-21 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 469654af-0bef-3dfe-bc01-ed0970b4e325 | -14.2531 | -53.2992 | 2025-09-21 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 20f487fc-5e03-3e14-966b-c485f752a5fa | -14.7877 | -51.3836 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 158fb78e-5f33-3f06-9a45-ca3d8694d017 | -12.8777 | -50.5422 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 483e1fd5-6a4b-3d83-8109-d57a9210d237 | -15.0508 | -55.283 | 2025-09-21 14:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 6a2a366c-6410-38f6-a1d6-27e8796efc5c | -17.1173 | -45.9491 | 2025-09-21 14:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 153.4 |
| dd5b9c59-8873-377c-93f5-202c08424aa1 | -12.7149 | -47.7195 | 2025-09-21 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fb7a22d2-517c-34a8-ac18-a901f63f8c1b | -11.4482 | -43.5277 | 2025-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| e7c1c8a1-69ce-3052-9ab8-61ef35a14f39 | -14.2338 | -53.3016 | 2025-09-21 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 32b0b6fc-dd3e-3051-94ef-633a4b5444c4 | -10.2811 | -46.0679 | 2025-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1463e24b-af4f-3250-95fc-6a0fe72c901f | -12.7114 | -46.8454 | 2025-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| dd9252a6-ab7b-38b0-ad19-41bc97f43f52 | -10.7115 | -46.488 | 2025-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 53f97e34-e209-3bab-a4a5-7bc317c9d79d | -10.0507 | -46.2538 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b2d77dd3-ab45-3eac-ab9d-bb811a0ac17d | -12.0767 | -44.8131 | 2025-09-21 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 776e1240-a3a5-33ae-ae49-91eccd06eceb | -12.7302 | -46.8651 | 2025-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 05717bb3-36fd-3d84-abc8-473a94e59eb3 | -6.704 | -44.0017 | 2025-09-21 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 2075d2f1-b38d-3932-8e2b-d02a0cea9fea | -9.6287 | -46.6394 | 2025-09-21 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 61f1f3ed-c601-348a-90fe-25f5d0bbace5 | -7.7336 | -44.3902 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 3d778e12-349e-353a-a98f-1a0e3770f3a3 | -4.388 | -43.2896 | 2025-09-21 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b5df346b-51f7-3467-9d6f-227432629bac | -9.8439 | -46.143 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| dcf38143-b069-3dd5-8b47-576f6e4cbe2b | -15.0511 | -55.2624 | 2025-09-21 14:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b6ad8338-8d7e-3a2a-8921-6283b4ea8ca4 | -7.3554 | -44.5645 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c98d91ec-4922-3025-b763-0cdfee5c0dee | -7.5272 | -44.3413 | 2025-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4423fa15-9ec9-3729-9dc5-691f4780cfde | -9.8632 | -46.1182 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f57719a9-8bbf-3bdc-afda-02aeda1bf201 | -14.7682 | -51.3863 | 2025-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| da937c19-3b5e-3a4a-83a3-bff97eff4fc7 | -8.8612 | -46.14 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f83ba810-5324-3279-9e92-3b71ce9c2687 | -10.0317 | -46.2561 | 2025-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 02061317-b9cf-36c3-b7de-f2cf1249417b | -9.1744 | -45.3135 | 2025-09-21 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f3e9a51a-1443-3105-a19e-f7b54f714196 | -12.2983 | -45.2881 | 2025-09-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| f7830425-946a-36e1-9093-126590546dc2 | -12.2794 | -45.2679 | 2025-09-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8cc17c9d-135d-332c-91b5-e9677109c377 | -12.7341 | -47.7168 | 2025-09-21 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.9 |
| d255c8eb-b1b8-3b38-8ab4-955b5148b3f0 | -7.62 | -44.4474 | 2025-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0fc314d4-ad9b-35ce-89b1-65989606f796 | -9.1937 | -45.2886 | 2025-09-21 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7cf2c789-b3fb-355a-80f7-1d74f0b71c84 | -14.8675 | -45.481 | 2025-09-21 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 415482b7-a443-3bd0-b16e-a0fb4a6a367e | -12.753 | -47.7364 | 2025-09-21 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 409.1 |
| d3b55b3f-f303-3885-9e17-e6abe7e9d53c | -10.0131 | -46.2358 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4c2cd0ce-6954-3892-88e1-9223d5b8301c | -12.2987 | -45.2649 | 2025-09-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 0a9396a9-a4a1-3633-b1e0-8086a68474e4 | -12.7149 | -47.7195 | 2025-09-21 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1d9617af-fdf0-3848-8046-188957a46be4 | -12.7337 | -47.7391 | 2025-09-21 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 239b50ca-681e-3016-a0b4-387842d49c4e | -9.1837 | -44.6482 | 2025-09-21 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 14ae5d56-3b2c-3c4d-8482-f894931b0a6c | -10.6928 | -46.4679 | 2025-09-21 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2f6d843c-95a2-3ada-a0ec-ec75751ce980 | -11.585 | -50.2902 | 2025-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3e50f2ff-4c4a-3c6f-a51a-fea38947e168 | -14.7877 | -51.3836 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a31559d5-f4ba-3b6d-838c-10d57acc87b9 | -10.9693 | -49.5639 | 2025-09-21 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| cee6ce6a-2dff-349a-8153-58d0514ff992 | -12.7114 | -46.8454 | 2025-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |


[Clique aqui para ver as próximas entradas](README57.md)
