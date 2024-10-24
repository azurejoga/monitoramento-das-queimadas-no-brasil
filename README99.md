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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cebf639-5473-3356-8422-d7ab262cd5b4 | -4.19905 | -55.55609 | 2024-10-24 05:21:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3c4784f3-ab13-3942-9603-7934a52cb121 | -3.94144 | -56.07052 | 2024-10-24 05:21:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265ce74c-56cb-398e-b6ee-a58570f93c9a | -3.90226 | -55.39867 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75ea9d3-4efc-3bd6-834a-1fdc30716970 | -3.90207 | -55.40106 | 2024-10-24 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b3bcf45-9e91-3b57-8376-71e6cb771104 | -2.10493 | -56.59072 | 2024-10-24 05:21:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73f3ca24-d9e8-33a9-a5a5-ff09c25c6d57 | -1.43596 | -57.92251 | 2024-10-24 05:21:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5840339-8eb2-3481-b3aa-d9cf6637c33f | -2.60058 | -57.8535 | 2024-10-24 05:21:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a8b3cb4-6ae6-3de5-8c6e-715f4ccfd46c | -2.56708 | -58.11292 | 2024-10-24 05:21:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05cd84a9-1f59-3574-bafa-f7b6fbfd83b7 | -2.5637 | -58.1124 | 2024-10-24 05:21:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11058ed2-ec1c-3d9a-8e88-4c3136cc4e8e | -2.5018 | -58.13241 | 2024-10-24 05:21:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2557fd15-0183-373b-98f9-8adc6a8d6fdd | -2.34667 | -56.90142 | 2024-10-24 05:21:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 634dbe5b-a3c6-366d-86db-113dffd3bcc3 | -2.25468 | -56.81925 | 2024-10-24 05:21:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77b0c5a5-a812-32db-9a24-0af49d989967 | 1.12401 | -59.44121 | 2024-10-24 05:21:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9270646-3537-3afa-baaf-d09eb367caa2 | 1.1207 | -59.44172 | 2024-10-24 05:21:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42a2c4a1-aeb6-33f4-9e2d-7ae9c74f47da | 1.03397 | -59.6042 | 2024-10-24 05:21:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88fd1941-b469-3233-a51b-f25d4cb8129f | 1.03065 | -59.60472 | 2024-10-24 05:21:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 010c8ee0-fd76-31c3-9c6a-2528b8ab6505 | 0.99406 | -60.47342 | 2024-10-24 05:21:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c1e131a-10f0-32db-a9d6-fce0ce1b4b2d | 0.86927 | -59.61601 | 2024-10-24 05:21:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 163df6c3-c09b-3120-8939-cf17f3729197 | 0.74678 | -59.80907 | 2024-10-24 05:21:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eca6252d-dd8c-3b42-aef7-714877f919d1 | 0.72793 | -59.81912 | 2024-10-24 05:21:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ca52060-9862-311b-a253-3ba61d70f3c0 | 0.71283 | -59.87497 | 2024-10-24 05:21:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ef26629-74f8-351d-9fd9-f16e51b6db19 | -1.41887 | -60.40671 | 2024-10-24 05:21:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde4e6c0-f9ad-363e-9eac-a8dc38d35e87 | -3.60366 | -60.36539 | 2024-10-24 05:21:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0793b74-a3f1-3554-afda-8391e709a52f | -3.15897 | -60.38394 | 2024-10-24 05:21:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d60a089-d5af-34f5-92cb-0ac41737fa15 | -3.15843 | -60.38739 | 2024-10-24 05:21:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d05993-88dc-3e12-93f9-ec724e0d1977 | -3.11839 | -59.92947 | 2024-10-24 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5953317c-e12a-3a45-9904-e334589c8430 | -3.11509 | -59.92896 | 2024-10-24 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33f03ed3-20d3-3419-a332-67970fcd0d3d | -2.95486 | -60.01673 | 2024-10-24 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b7c13c1-fc37-3bd4-85bd-93a33bcfdea7 | 2.66084 | -61.54142 | 2024-10-24 05:21:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1760e7c-3cd5-36f9-ae29-76d0412d3c72 | 1.89025 | -60.48197 | 2024-10-24 05:21:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e0500b6-4068-3b05-b7ed-cd1829dcd277 | 1.88934 | -60.48143 | 2024-10-24 05:21:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d046040e-5465-323c-9c32-bbba10e56221 | 0.6464 | -60.6447 | 2024-10-24 05:21:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4cd233c-f392-3672-b3fb-d77db5fb572b | -3.01641 | -61.70073 | 2024-10-24 05:21:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dbfadf4-b3aa-3652-b407-1dc070cc86f9 | -2.98779 | -61.44117 | 2024-10-24 05:21:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f312ef6c-796e-3c9c-b573-20f05ec73b43 | 0.12017 | -62.55507 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47c3516-f820-39ea-b6be-1b4f33cb8409 | 0.1165 | -62.55564 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 587fa510-8247-3b58-9900-bb6df21a7d92 | -0.76821 | -62.88404 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d536a34-b22f-3e9d-8a8e-a5bf919467f6 | -0.77547 | -62.87934 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e7c6ae-4584-3a46-9a80-0a5da16b1974 | -0.77477 | -62.88369 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc5b976b-59e1-3e88-bf52-6de896cfed7d | -0.77191 | -62.88462 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb96d2a-be99-3f1d-9793-912525dbd34f | -0.77108 | -62.88312 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dfb7657-0adc-32d9-b13f-ee369fe15f7f | -0.77038 | -62.88748 | 2024-10-24 05:21:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec4f02e-ded2-3ca4-80cd-49a5344f3b28 | -6.51568 | -47.2661 | 2024-10-24 05:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21d9e596-663c-3ded-975c-4d8470a6dd8c | -6.51483 | -47.27243 | 2024-10-24 05:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4fc95a8-be22-39fd-9ed7-78d57959befd | -5.84489 | -47.28638 | 2024-10-24 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb168b49-1d0a-383f-9f64-03f591b80138 | -5.84469 | -47.28605 | 2024-10-24 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4669facc-3bdb-3bae-bdb5-5586f4ebdc4d | -5.8438 | -47.29235 | 2024-10-24 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec30b6a3-b737-3f5d-ab2c-f26b1b5f553a | -5.838 | -47.28553 | 2024-10-24 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82eff788-d072-36f3-9d2a-01026179ed4b | -5.83779 | -47.28521 | 2024-10-24 05:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d623ab95-2576-3658-9089-e99501ae5be7 | -9.24082 | -48.32156 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ddcf40b-2ac0-3b7e-a565-a4ed136b1677 | -9.23482 | -48.31465 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff3fb6e-6f1e-3fdf-b0db-e9f2f136197e | -9.20956 | -47.95133 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 322f7254-36f2-30c7-b9b5-3fc81eafa25d | -9.20882 | -47.95759 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7b6fd85-7302-3aeb-a6db-3e71dd131af8 | -9.2086 | -47.95573 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ceb64d8a-634f-3d9c-9c7f-97c7dc9f8fd1 | -9.20268 | -47.95028 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ad13cd-da15-362b-a28f-be64c9eccfb0 | -9.20192 | -47.95672 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0ad48c1-1819-3e4c-916a-a4ccc249594c | -9.20171 | -47.95489 | 2024-10-24 05:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0205e71-5c08-3640-be93-4ff68391a681 | -10.92241 | -47.81374 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3d07da0-f514-380c-9831-7a65d8457ee2 | -10.88296 | -47.90572 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7e65bef-abfa-31b9-9d8e-edfbe6a6e599 | -10.88212 | -47.91294 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1549cc10-2b57-392f-8f12-4f18a91d2776 | -10.69321 | -49.11308 | 2024-10-24 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea5c0441-d06b-3a50-aac5-1f287bb2a9ff | -10.68667 | -49.1122 | 2024-10-24 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15700a9d-16b6-3598-8eec-b026df0a1531 | -10.58889 | -48.02924 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d625a050-9087-3149-b5a2-512bbfad1bdc | -10.58767 | -48.02903 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91d4129a-b033-3840-9fd8-e2439f786449 | -10.58185 | -48.02886 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57dc06ff-47a3-34ae-b027-c042cca42bea | -10.58064 | -48.02863 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a92d08a9-1f43-38fe-a246-fce954a014b6 | -10.47445 | -48.28425 | 2024-10-24 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94dd1fda-e963-38da-9b77-c1489c4b7705 | -10.46755 | -48.28369 | 2024-10-24 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc36ca28-306b-33f6-933e-c52ca4d171e9 | -12.0576 | -48.34051 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 242419d1-df71-3794-a4a2-65be5e241267 | -12.05062 | -48.33989 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46afadc7-4dcb-3f97-8d09-e4c5bc013d05 | -12.00305 | -48.27077 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03664a12-e3d2-3308-a035-5e28fd132fec | -12.00197 | -48.2669 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6674b484-9732-3e66-bb1e-ab4cc484322b | -12.00124 | -48.27375 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 876263f3-1632-3f11-8108-a4c1753798a3 | -11.6608 | -48.80239 | 2024-10-24 05:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d57581e6-a41d-3fa4-9837-eeda5ce48e5f | -11.65653 | -48.80424 | 2024-10-24 05:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a06dad06-9947-388b-87a1-fa3bfa19a47b | -11.65405 | -48.80158 | 2024-10-24 05:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07672e80-6a69-345d-ba24-69a5c9621233 | -11.65332 | -48.80779 | 2024-10-24 05:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f007539-a439-3f89-a22f-428b6588f712 | -11.60715 | -48.55066 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76a03ef8-e935-372b-80e1-aae0fd976de3 | -11.60031 | -48.54982 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a3138b9-6eab-3015-91f8-1bb5f6981e88 | -11.5996 | -48.55615 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bda24d30-34c8-393e-94e4-df3fb8469125 | -11.59473 | -48.5996 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34fb1c11-386c-3014-89d8-bdff0d2a8a06 | -11.59275 | -48.55538 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fae52fdb-c28c-3c0e-9887-69d8012987a5 | -11.59206 | -48.56158 | 2024-10-24 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52517bd6-9c86-36fe-b660-99b20937bd43 | -11.02846 | -48.279 | 2024-10-24 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c10cfe7-2d42-3e70-aecf-2d1b271cecbb | -11.02155 | -48.27812 | 2024-10-24 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fbdd0c3-81cf-3e93-a07d-30d80cbf5aae | -11.02076 | -48.285 | 2024-10-24 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a365a4a0-8bf2-3329-ab28-6e5072506fcc | -10.93659 | -47.8154 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20c5a522-70a0-3690-a163-cbd2a21a9696 | -10.93583 | -47.82176 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f4fbcc-107a-3ff5-b4c6-945fc79f9109 | -10.93379 | -47.81658 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05384bf5-1b8e-31e6-83e6-da77ab4dcbc2 | -10.92949 | -47.81465 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9da74ed1-9dc6-3460-aac4-185fdb17e11b | -10.92665 | -47.81616 | 2024-10-24 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6431440e-094c-34a9-9ed0-8a17d05c9b2f | -12.95832 | -48.87314 | 2024-10-24 05:23:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86e6632d-1bbe-3017-ad9f-089f44f14bb9 | -12.95763 | -48.87951 | 2024-10-24 05:23:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac4a0de4-6947-3f24-96a6-63cd5de14e10 | -12.88498 | -48.51423 | 2024-10-24 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a5736a0-c696-3ad3-b4c0-8e853ddc58de | -12.88432 | -48.52042 | 2024-10-24 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e555204a-ddd6-3498-ba8f-0b0acbf8fa75 | -5.56179 | -49.4121 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 395209ea-5485-3801-9d31-b47095865678 | -12.59025 | -48.77635 | 2024-10-24 05:23:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cc83434-5817-3db7-9068-001e29d2e26e | -5.56839 | -49.40877 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bd3c0cf6-5fe3-3f76-8a1a-caae58831b12 | -5.5678 | -49.41308 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 67b12ad5-3d21-316f-ad7d-68473edb0854 | -5.56237 | -49.40791 | 2024-10-24 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README100.md)
