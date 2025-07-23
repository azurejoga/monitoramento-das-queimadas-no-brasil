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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2d41937-a614-3289-9b6e-e38b5ed1a997 | -21.44525 | -54.57785 | 2025-07-23 05:04:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28b1c8c0-37c3-35a3-a389-bac17a801985 | -21.44165 | -54.5773 | 2025-07-23 05:04:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8287d8ac-4781-3c07-ad25-dab1988c4523 | -20.5619 | -54.65383 | 2025-07-23 05:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 277bb52a-420e-380d-a983-7a187474c210 | -23.05963 | -49.69055 | 2025-07-23 05:04:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e39f6611-0646-3a0f-82de-b7313f92b22c | -20.5613 | -54.65803 | 2025-07-23 05:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b401045e-b562-31c7-bf68-6f9f23e7f52b | -23.25084 | -52.19954 | 2025-07-23 05:04:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| a1e6a2cf-2c7f-33dc-8bf4-1f2b565757fd | -22.84479 | -49.17754 | 2025-07-23 05:04:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80d8e7ec-e59e-38ac-bad4-eb7e80789a41 | -22.15789 | -52.68385 | 2025-07-23 05:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f40fc03c-44d0-343d-9e0c-716230e52767 | -20.64527 | -56.55317 | 2025-07-23 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21afc32a-cd88-3f0c-a3c1-fc19e3b68dc7 | -25.09921 | -49.51035 | 2025-07-23 05:04:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 94100fb2-3d08-3c7c-8e7c-c87667464cdb | -21.01594 | -56.00654 | 2025-07-23 05:04:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 750a0320-5c22-386c-ab2d-055b26ad7b9e | -20.29722 | -54.07864 | 2025-07-23 05:04:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edbfff81-4bbb-34fe-8a28-4bf70c853926 | -20.28695 | -55.49208 | 2025-07-23 05:04:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fc7b941-6656-3c29-a9d8-90285337206c | -18.66051 | -55.7267 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4a8b5371-3f8b-372c-9b45-efb6795803e0 | -18.66445 | -55.7235 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| af91a306-8f2a-3d19-a8d4-fa190390e5dc | -22.39763 | -49.79242 | 2025-07-23 05:04:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f00872cf-b7e8-357f-841c-d7a9bcb67673 | -23.59287 | -54.32816 | 2025-07-23 05:04:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5db028b-16c5-3e2c-8b07-16b7d07291d4 | -23.25132 | -52.19552 | 2025-07-23 05:04:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 895da404-4fd2-3157-bfac-e4ebe037e420 | -18.50245 | -56.42531 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4f5570b6-8bad-3224-b411-8cb6392c80c1 | -23.59351 | -54.3233 | 2025-07-23 05:04:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4e56138-7de0-38e9-9447-180a1ad340ad | -18.66332 | -55.73101 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e40d266f-05a5-353b-8df3-db77b97e4931 | -23.25504 | -52.20009 | 2025-07-23 05:04:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 4e39264f-217d-35c9-bf7b-63c0eb3f88af | -23.00763 | -48.62117 | 2025-07-23 05:04:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| febf5592-d665-3a0c-a4d7-2c1587430751 | -20.28352 | -55.49154 | 2025-07-23 05:04:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27fafdae-7db3-3751-a782-08f577e5d422 | -23.0547 | -49.69001 | 2025-07-23 05:04:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44890350-3d30-390e-858d-b0bea2baacb1 | -20.64249 | -56.54883 | 2025-07-23 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 862d5c64-7fb2-3238-aea8-2109a167e8e8 | -21.87694 | -56.70087 | 2025-07-23 05:04:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19057466-3fe1-3a18-aa10-25deda33b007 | -22.01253 | -56.02634 | 2025-07-23 05:04:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fb1e99e-82c0-3a4a-990b-547425234c20 | -20.29096 | -55.4887 | 2025-07-23 05:04:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 581aea20-fa66-3224-98dd-04b72de4b25d | -18.66388 | -55.72726 | 2025-07-23 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a1073cdc-1dad-3caa-8eb6-4dff0d9e0877 | -22.15388 | -52.68319 | 2025-07-23 05:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f524bb47-4b1c-366d-a95a-ba44dc085b9b | -23.25553 | -52.19604 | 2025-07-23 05:04:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 5d5790be-533e-3300-a410-519a2eeaa1a7 | -22.91504 | -53.14605 | 2025-07-23 05:04:00 | NPP-375D | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d310497-5c29-38b8-8737-93b7fbf57804 | -23.21002 | -50.2836 | 2025-07-23 05:04:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 68495544-7256-3df3-8553-a08160a74320 | -21.36897 | -48.60651 | 2025-07-23 05:04:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4c7bd11-aac2-3a95-87e4-739218c6ee9a | -22.15343 | -52.68223 | 2025-07-23 05:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dbed9c0e-e93e-31ce-a5a1-379ce7505302 | -27.08542 | -48.64033 | 2025-07-23 05:06:00 | NPP-375D | ITAPEMA | SANTA CATARINA | Brasil | 4208302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a388b28-57bb-395d-9532-600f176d755f | -3.03969 | -47.86043 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e425db74-2273-3b2f-9268-100c38c38f87 | -7.29515 | -60.16716 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a177beb-3a0c-3de4-aea2-2880cdf75503 | -8.91047 | -47.35947 | 2025-07-23 05:23:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0644a1c-f97d-3e7c-83b3-3045981d5fd8 | -7.26201 | -60.18343 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d019033-279c-3c18-9830-338a250a56f6 | -7.24765 | -60.18834 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 112aeb3c-3a4a-3fa7-9726-0b2482c73e58 | -13.72108 | -52.00684 | 2025-07-23 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53fd58b9-1bab-3104-b012-8d14d4173d37 | -3.1165 | -59.92886 | 2025-07-23 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81a13a78-3159-3274-9d50-670ff465f69b | -12.34524 | -63.39711 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1043759-e74b-3b24-a141-b6b2ed8e3858 | -11.45785 | -61.14989 | 2025-07-23 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46f6746e-8522-399b-968a-13f320c84f94 | -12.35297 | -63.41339 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45ce1385-5c46-3171-a638-0b1155426bd9 | -12.49979 | -57.77639 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71faf4f8-7240-3bb0-8eb3-60c25f87515a | -3.87056 | -54.23132 | 2025-07-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d6a399-3f43-333c-bfb1-9a9addac21db | -7.25483 | -60.18588 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 896927de-ce17-3329-9ffc-1d17b4bcfde5 | -7.26255 | -60.17994 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a3b1e5c-0788-3709-9897-63c6b7aca833 | -7.28356 | -60.17606 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7da35937-64d5-328e-b779-1326d5b01ce8 | -12.50501 | -57.76714 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060cd173-463b-3953-8be6-5aef7c1164f1 | -3.41185 | -49.53513 | 2025-07-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a8ec422-c428-3bcd-adcd-f6e7d5d27ddf | -4.09204 | -46.92975 | 2025-07-23 05:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a57f31cf-1afc-333f-b357-861cf24ab1c4 | -12.35461 | -63.41331 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83dfb260-bd7d-33ce-902e-dc7a44350803 | -12.35738 | -63.41752 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03166f2c-4e47-3eaa-a224-6181a11365a6 | -2.91736 | -48.23864 | 2025-07-23 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94739249-5f14-3f85-a09e-ad43f1a21977 | -3.04002 | -47.86207 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd2750ca-6bad-3155-80fb-e4439d6e1a08 | -7.27306 | -60.17801 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48ac487b-8ec4-3a71-a6da-1f37c5c6aa1c | -12.50815 | -57.77258 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aebea723-5d71-320b-b803-8f6e197a959e | -12.47516 | -61.63819 | 2025-07-23 05:23:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a85689ba-a2f0-3cf5-8ab1-15b02969a958 | -10.02925 | -67.74451 | 2025-07-23 05:23:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08255700-1804-364e-940f-47885b6709b8 | -4.29858 | -48.10531 | 2025-07-23 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 582fa309-2d4f-3524-baa6-ead9064d5ed8 | -7.25815 | -60.18641 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de343e7-a3f1-3487-b271-939c9aaf109d | -3.40602 | -49.53427 | 2025-07-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91b967ba-fe3b-39e0-8cd2-2d71a2a12286 | -3.74999 | -49.04652 | 2025-07-23 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2729ca0c-2636-3140-8ec3-c20ce2c2087d | -3.18906 | -49.43695 | 2025-07-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54820095-bf2f-30e1-ad0b-240afb74dd48 | -3.04521 | -47.37986 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2a359e0-6548-38f3-98f3-2e03b68514da | -12.49212 | -57.77525 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6272487e-f566-3784-8936-fe8ec624c386 | -12.49595 | -57.77584 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49b0c7fd-3a63-3809-8707-344436ef98ad | -12.50363 | -57.77691 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a21f507-27df-3892-b57e-85de12b66f29 | -12.49664 | -57.77097 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5838c206-e36b-3db3-ac95-8804560738a3 | -3.04441 | -47.38527 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3201f0e7-6513-3302-86ba-90823203577c | -12.35342 | -63.42059 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4dac5566-192a-3652-ad15-89e51ad2f591 | -12.3518 | -63.42069 | 2025-07-23 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b4bf15e4-9543-36b3-8c94-8f173ce19c64 | -12.50431 | -57.77206 | 2025-07-23 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 678f9f84-2075-362f-8378-a3214d8b01f3 | -10.03358 | -67.74529 | 2025-07-23 05:23:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5189b7b-0cfa-3f08-a395-352a0a7af393 | -3.03325 | -47.85942 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a31c249-82ca-314c-9ec3-097d95f78441 | -2.91661 | -48.24363 | 2025-07-23 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 263b8a58-e2ec-3ff7-906d-e511300b8fe1 | -7.22179 | -49.59602 | 2025-07-23 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbdf70e9-2925-34ac-82aa-89f86b78d55c | -6.55411 | -56.24821 | 2025-07-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0cdd0ac-78f7-373f-a135-7dd704024ed5 | -3.03889 | -47.86562 | 2025-07-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6645eab-280f-3cdc-940d-0ef945d67108 | -2.58597 | -51.92498 | 2025-07-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58cfa36c-cac4-3340-a758-c77bbaf474dc | -7.27692 | -60.17503 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a37447e-7e52-358f-b700-f58ae27e095e | -7.26642 | -60.17696 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ea9c66c-e365-37e4-88bd-e408a3cebae5 | -13.72275 | -52.00561 | 2025-07-23 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8f21357-a285-353c-ba75-48e7191c70d1 | -7.22186 | -49.59634 | 2025-07-23 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff2b77e8-58fb-34c6-b5e6-e96682f4c430 | -7.26587 | -60.18046 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49b03ea7-12e4-3ea3-b39f-c30d4da50b0a | -3.41135 | -49.53353 | 2025-07-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b0f30d0-64d1-302e-a976-c614ce1c4e60 | -7.29183 | -60.16664 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26dc7a5b-4417-3775-bcc1-c5652c33ea2f | -7.2794 | -47.53803 | 2025-07-23 05:23:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 39bcccaf-647b-3135-a6e2-a3abea21d049 | -7.28079 | -60.17205 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 132f1e90-5d2b-3299-861e-b9f4b725e5db | -7.25537 | -60.1824 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78664779-50fe-3cfb-9a2e-2f2822fb0839 | -7.28033 | -47.53808 | 2025-07-23 05:23:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3729ec13-855d-3ce2-9ec0-8a74a2000ebc | -7.25869 | -60.18291 | 2025-07-23 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbaa5fdb-2825-31e7-aa8d-1b87e0c7106d | -7.2812 | -47.53156 | 2025-07-23 05:23:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 11343055-0f34-37f6-839a-7d70833e8ef6 | -5.92045 | -61.30262 | 2025-07-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e44641d4-dcce-3d06-95ae-a31c4595290f | -13.72677 | -52.00776 | 2025-07-23 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fd9f99b-07bf-302f-9dd9-5b1714072c51 | -12.57825 | -56.97672 | 2025-07-23 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README19.md)
