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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8a90ebd-ecb7-38d9-b652-8eeabeb2ec48 | -8.73072 | -46.68408 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba979562-fb46-3396-be0d-e8d4779fc88e | -8.81636 | -46.25859 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0036dc01-7064-3978-a1c3-3e3a2286168a | -12.64494 | -48.15614 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37d36d5-517a-3091-8d72-2cc2f83968de | -8.72674 | -46.68716 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 847e5f44-8f9b-34cb-ba0e-0f81fb485117 | -11.42522 | -44.92208 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc68b962-2408-353d-9703-5cd939022c01 | -11.42944 | -45.0179 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5517cc9d-91b7-3303-81a0-9478b559d59e | -12.26158 | -44.0626 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14b96478-81d7-3b4f-8321-cb7cca0b74e5 | -12.36808 | -44.14106 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f734e96-81a3-3e0d-b7f3-e6f77b4bcd4f | -10.11954 | -45.33514 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1919911b-6972-36ea-84e9-5e88b6d5f6a4 | -11.2443 | -45.555 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 534f9ed8-4be4-3129-91f5-8f366725a6cb | -9.05141 | -45.50545 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cef36403-afa3-38dd-a0e4-eb1fd502090e | -11.38054 | -44.94431 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6906b2db-9038-3d62-8250-d4fa1e6fd681 | -10.59785 | -46.28489 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2817e808-a2c4-3a85-9150-b649fddd217a | -7.67238 | -47.42468 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e6030eb-6831-3106-981d-310c89d6c0dc | -10.8133 | -45.37785 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c89ddf98-1659-307b-b8c7-34bf06d83e0c | -11.40823 | -43.51045 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b921d5-944e-39f1-8807-a8161c7e2503 | -9.96827 | -43.60776 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1719d8d8-4305-3583-bd97-b5965191cb2d | -10.11957 | -46.48021 | 2025-09-27 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56a89ce2-8051-3eeb-ba70-976a8facac74 | -12.9776 | -46.25195 | 2025-09-27 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acc776ab-6aac-33a6-9d01-b08fd41d4c3b | -11.99562 | -46.62235 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 110aa383-9f37-364a-9cab-214c962c7934 | -10.18245 | -46.93008 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d20e6a15-3a5f-31ad-9b02-e2fcd5ff0693 | -11.37441 | -44.96169 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77228e4f-5771-3bbf-91c4-93d24538fd60 | -8.72335 | -46.6866 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d010af14-e16f-3118-a615-ca31ebe6d77e | -10.59842 | -46.28135 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fbc2546-3eb7-399d-8512-a8e46b9c2d1d | -7.72143 | -47.30157 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0a64075-9250-3ae8-ad52-4fc657d51826 | -8.52567 | -44.63685 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92569da2-26c0-3f81-b106-99a2e22b8a41 | -10.592 | -44.06395 | 2025-09-27 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d81f12a3-5251-33e1-b594-491b7a28c19d | -10.12342 | -45.33216 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d99c93a-eec8-3bf0-9dbe-670f3acfb9ab | -9.69699 | -48.9432 | 2025-09-27 04:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac54c68-548a-36de-88b0-022e61e5f976 | -11.60997 | -45.42485 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d92676c5-aa3d-3483-9496-ca027f80f9dc | -9.11059 | -45.87789 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e143667-b13e-3ad6-8f10-af3c453ceba6 | -12.05652 | -44.85793 | 2025-09-27 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbf8a178-72d5-36b2-a12e-1613be5cb75e | -10.59508 | -46.2808 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 095c9f46-7e40-3cf0-a2b7-60450a745739 | -11.37998 | -44.94791 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c90b90b7-4d2e-3052-84ca-d196084018b2 | -13.1718 | -47.42942 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59099115-1209-3d76-82ca-77e4e968f2f6 | -12.5406 | -45.84999 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5890ff3c-0133-3061-a027-15bcd2d2331e | -11.51021 | -47.74711 | 2025-09-27 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e56f5e7-e4d6-34ed-844f-31c3baea3819 | -8.2591 | -44.80292 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cc5e132-05d7-3d72-af2e-0c35aed69d42 | -10.81052 | -45.3738 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfe95ac3-0dbb-37b4-9f9c-7bec338599c4 | -8.49328 | -47.85326 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5bb26068-0d6b-3f22-877b-43aec0675962 | -8.72616 | -46.6908 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c28e376-14d0-32fa-a462-c536af4b6dd1 | -12.06511 | -46.6301 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0778f7-8b55-3aad-9591-c187f8ba70ce | -12.28112 | -44.05008 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50b5d328-08fc-34ad-8c86-b4330929a912 | -11.04945 | -47.65581 | 2025-09-27 04:23:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c07a388e-6914-38db-9bf4-5be6d8338d25 | -10.40435 | -46.14068 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4df524b8-129c-3d44-8cfe-d9d71c1789f1 | -11.62746 | -44.42879 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8190647-2984-3763-8255-fcea72a32487 | -15.1972 | -50.09994 | 2025-09-27 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95427cee-088d-322f-9e24-cf05ec2f3be1 | -15.27098 | -46.46227 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1479404e-ef74-3e0b-b904-5a81287e6525 | -15.39036 | -46.10586 | 2025-09-27 04:25:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aa03907-2f6e-3cb2-b2e8-ba6f42a316ec | -19.69715 | -45.89451 | 2025-09-27 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b5e0dfd-e014-3e2b-bfcc-1e32de7b7d9a | -14.95217 | -47.50711 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fc0256d-014a-3e2b-899c-8fbce12248d8 | -14.59712 | -48.24514 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 921137bf-8fde-343b-9cc3-aa7d4d8d87b8 | -14.829 | -45.62875 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| afe7a7d6-57c2-3dc5-a0f0-7935b53b09ca | -15.21994 | -49.83818 | 2025-09-27 04:25:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a8ce20-3ece-37f2-ad03-46b69403559d | -15.20003 | -48.46661 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b334c38a-b461-300c-8020-adeec02e5031 | -14.84412 | -45.61998 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28b127b7-0b1d-3659-8ce4-b531522b213c | -13.6305 | -48.08608 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9b8c307-5b91-398c-aeb5-fa763bcbee12 | -16.6284 | -49.48359 | 2025-09-27 04:25:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38f29378-b2e0-3168-9539-17edfa8d3519 | -18.21155 | -48.49125 | 2025-09-27 04:25:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7ef87cb9-a7b8-3c57-87f6-e0c45ec43ef8 | -15.91224 | -59.33363 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b11f31de-3e7a-37a4-8932-e31078b830e5 | -13.80506 | -47.91993 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0498a7a-7d82-3ee4-a846-d2aaeaac88ac | -17.17931 | -56.37797 | 2025-09-27 04:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bb002d68-7cbf-36cc-9321-516bef40a633 | -19.459 | -48.92539 | 2025-09-27 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d6e9032-81e8-3356-a231-1118c9dc0162 | -13.62493 | -48.08144 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc5e50c-5580-39dc-9e5e-8bf3adb06a80 | -13.78328 | -46.93144 | 2025-09-27 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e9c144e-6dc8-30b8-aef2-7d2e31193b9c | -13.83068 | -47.95525 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b022a567-3652-3ac3-a7c2-3362d1398fda | -13.62834 | -48.08201 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63333043-1ade-3184-b676-388455edd692 | -15.90505 | -57.50025 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efd44cc8-f596-361e-b1c8-7bc357f50011 | -14.06797 | -48.81512 | 2025-09-27 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a098f336-61d0-3212-96c7-4d595aae886a | -14.63458 | -48.2941 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 185c7534-4c62-3fef-9c66-f8ac9d0071d0 | -15.42131 | -48.22694 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74ba8ff9-3442-3db2-867c-048746678e17 | -16.75664 | -53.36089 | 2025-09-27 04:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 56e99a4a-1e26-36b9-acd8-1f57de990b16 | -13.51083 | -47.40718 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4210c1d4-a380-341c-8f34-aa3316cd6fa6 | -13.60408 | -47.30696 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46ddca86-4854-36bd-9a15-f1f8aaf45526 | -17.54897 | -44.81016 | 2025-09-27 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 354b8d8d-1f66-35e6-9fac-50eb0a35048a | -19.47652 | -45.80827 | 2025-09-27 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27908002-cab3-3e4d-99e4-313c1c6308c5 | -19.18421 | -46.04107 | 2025-09-27 04:25:00 | NPP-375D | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df68cbd6-a7cf-3a46-88e2-bdf1b54d15fa | -14.843 | -45.6273 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae7f2e2b-9e65-36d6-b75a-48a791b96957 | -17.02755 | -52.24195 | 2025-09-27 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef3e1c04-f5ba-3e25-991d-ba7e454d4d2d | -14.06383 | -48.81837 | 2025-09-27 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65bc95c5-ff79-3318-a5c8-cffa82949b16 | -13.50747 | -47.40657 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 956d2c9b-f8bc-3016-9316-348ac5001687 | -15.03832 | -46.94911 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fe96c47-5ee6-3f60-b7b5-2d32cb06a530 | -20.00473 | -48.94153 | 2025-09-27 04:25:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c339196c-471e-3008-b673-2977b103e5cd | -13.64267 | -48.07621 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10d3ff75-73c6-3550-9a16-2b0c322c21af | -15.03661 | -46.95985 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1697fda4-b0b5-3f89-a1a8-c43a6d9ac002 | -14.46387 | -46.84312 | 2025-09-27 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d950be51-867c-3d26-a7f6-ef9b490f4f1d | -18.25124 | -47.00333 | 2025-09-27 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b3372c2-80cc-3a1e-ab5b-40bcda53d3ee | -13.62771 | -48.08587 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0ea3e35-c405-3d72-bc28-5e66f6dbb422 | -21.11667 | -42.91977 | 2025-09-27 04:25:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69066e9a-e31e-3aba-87b7-d7f105276507 | -20.28175 | -46.00927 | 2025-09-27 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 315b495f-75fb-3066-9e45-5f6a19ede12e | -18.3257 | -57.12057 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fc186576-feeb-3870-bf78-93cea4fabc20 | -18.31595 | -44.87253 | 2025-09-27 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a4d56e4-9f07-3066-bd5a-67dd1a19991f | -15.26989 | -46.44739 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75cfa731-c51f-37e0-9af9-2f28dff5ee87 | -13.62554 | -48.07766 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e4a6fb-67b5-3b89-97f1-13b4a4d6194c | -19.05254 | -48.13699 | 2025-09-27 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4aeaa862-f65f-3e8f-9d6e-cf79bf6156a5 | -15.03167 | -46.94796 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acc0f918-eaa1-3470-87b0-d9c3223f9d44 | -13.51697 | -47.4119 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b161e8f-e501-35d0-b013-686d06c00ad4 | -14.83795 | -45.63771 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f637fe4b-698d-3fb2-afe1-8db75690001c | -21.11619 | -42.92355 | 2025-09-27 04:25:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 28c37942-1184-32d6-9c24-6bf17cefe65f | -15.03913 | -47.13706 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README39.md)
