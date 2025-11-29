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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2aa2755-ef1a-3a6e-a243-1602e8a1c13f | -6.32767 | -39.253 | 2025-11-29 03:23:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fbd84fb2-5c3d-3d58-8870-143ddd37f55b | -8.03166 | -43.13408 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 2e4433a4-50eb-312a-943e-4bbe22935231 | -8.04348 | -43.14208 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e63fc731-495b-3769-b831-889fd5c54a4d | -8.16391 | -43.21397 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 5b178e9a-64e9-3179-8065-149328d7e9ce | -8.76008 | -40.98692 | 2025-11-29 03:23:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9312f78-6392-35d7-a426-a66875ddbcec | -8.03062 | -43.13949 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 9b7620e5-b0e8-3256-a0ad-7231c8849350 | -6.45927 | -38.86683 | 2025-11-29 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7dd02385-2b75-307f-894c-d214d7c5634a | -8.76566 | -40.98794 | 2025-11-29 03:23:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cc2aa2a2-0f8e-34eb-99aa-8bdc5d9a31fd | -8.04451 | -43.13665 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| df3a14ae-9193-3d69-ad3e-5febce06a3e7 | -6.57617 | -39.71235 | 2025-11-29 03:23:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37e412ee-6472-3641-a140-e09e121168c9 | -6.327 | -39.25076 | 2025-11-29 03:23:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 640b92e2-d70a-3fd5-8936-eab76c930de1 | -10.18614 | -36.33345 | 2025-11-29 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad1cc505-fbee-39ea-bed2-47a2a3c554d0 | -7.23476 | -35.10483 | 2025-11-29 03:23:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9675e975-d03d-32f4-aea8-1efd384ba8a5 | -4.62741 | -43.99422 | 2025-11-29 03:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 93419aac-4f00-396f-92bf-4a1ec8402a4b | -6.32825 | -39.24978 | 2025-11-29 03:23:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 028a89ba-cae0-3b0b-8f33-dbf0596375bd | -7.46414 | -39.96349 | 2025-11-29 03:23:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 48905d89-af7f-3687-991b-26903657c691 | -9.58978 | -36.1404 | 2025-11-29 03:23:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e579c13-2cd7-3210-af93-8cdf49d27449 | -8.03912 | -43.12993 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| af417de9-3d2f-33f2-87d4-908a13800f8d | -6.57559 | -39.71569 | 2025-11-29 03:23:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfc8a925-5c51-3d79-9e4f-bd3de6fca301 | -5.35862 | -43.02962 | 2025-11-29 03:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f111eb72-f80e-3e87-94a3-9aac84a23875 | -6.71167 | -40.82064 | 2025-11-29 03:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee93dfa8-bb05-3354-8c01-014e2ac26957 | -9.42914 | -40.35257 | 2025-11-29 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d18718c2-87a3-3965-80b3-0aec76cf3850 | -8.79399 | -40.43116 | 2025-11-29 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b1f1126-fe2d-37ba-96ba-f2bbb5dc0033 | -4.6233 | -43.99288 | 2025-11-29 03:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b50b297-a178-30ab-ac79-9b299fb360fb | -8.16802 | -43.19223 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0fba63ec-6a61-3018-aaee-2fc4668d37ab | -9.95826 | -42.33503 | 2025-11-29 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 324d8a00-2e1d-3325-8b12-7726dfaaa338 | -4.63046 | -43.99404 | 2025-11-29 03:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2de8c70c-c28e-3880-a033-bb9704e8ad3d | -9.95556 | -42.33308 | 2025-11-29 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b107a893-4617-366e-a3c7-948a40cb61ea | -8.04555 | -43.13122 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 842bfe56-5113-3f3e-90d5-b1bf648581d3 | -6.69911 | -41.46563 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d55fcda5-c76c-3e92-b54d-f386fc23f071 | -8.25899 | -35.82913 | 2025-11-29 03:23:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebe98f49-7d34-39ce-8142-7ce96d3c7245 | -6.56861 | -39.75598 | 2025-11-29 03:23:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 971ea0f3-1fa9-3b1a-b704-1aa652bdcb6b | -7.46354 | -39.96686 | 2025-11-29 03:23:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5759a720-4450-348f-a1aa-2ebd1597dc86 | -5.36252 | -43.02695 | 2025-11-29 03:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bfbc3f6c-c8ef-3906-8173-a023302f7554 | -9.58779 | -36.13959 | 2025-11-29 03:23:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7aae54ae-e776-39cd-99e9-a6bb4f837f43 | -6.24078 | -40.305 | 2025-11-29 03:23:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 365df946-734f-32e8-83d6-ab355c667626 | -8.17138 | -43.20984 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cdf637fb-3162-3cac-acea-f049b9dfbf9f | -5.36143 | -43.03292 | 2025-11-29 03:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b8d67381-a550-37d6-9422-304f6c5a7bec | -5.35755 | -43.03572 | 2025-11-29 03:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 271c1d02-91a4-3207-847c-269a34a3a3c1 | -9.95912 | -42.33067 | 2025-11-29 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 08bedbf8-f140-365b-868a-fd60d75201b3 | -9.58579 | -36.13975 | 2025-11-29 03:23:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d965949e-a360-3273-81b5-5b74e223dd86 | -6.59837 | -43.69065 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79d5cbd1-ba83-3dbc-b5e0-b542f8908d35 | -8.03706 | -43.14076 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5b764497-f0dc-316f-acb7-dc6f0b002643 | -9.96148 | -42.33435 | 2025-11-29 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6000d041-4b25-3b9c-8a29-fae3250981ae | -5.36521 | -43.03136 | 2025-11-29 03:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0f330e9-cbb2-31d8-a58d-0835525d75bf | -10.54161 | -36.72138 | 2025-11-29 03:23:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 851687c4-ec6e-3253-8295-316a67d3f533 | -17.61263 | -46.66864 | 2025-11-29 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 19d4c938-e867-3bc5-bea9-b749841e3941 | -12.39201 | -43.67671 | 2025-11-29 03:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3135de30-35c1-3023-b3c4-2b6682f1831f | -12.39051 | -43.67548 | 2025-11-29 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fedc1546-32d7-32e3-a99e-975e541cbf13 | -11.16813 | -43.57962 | 2025-11-29 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37c1d4d5-d03c-3fd8-828a-27ec2b025704 | -16.27968 | -43.91749 | 2025-11-29 03:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193e3c2c-1221-3739-9c18-61ec39ba59a1 | -17.60905 | -46.66464 | 2025-11-29 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e10c5201-28a4-3b51-aba6-5581e053dbe1 | -17.60601 | -46.66685 | 2025-11-29 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 049414f4-220c-363f-a76a-cf1dfdacfbeb | -17.60762 | -46.67077 | 2025-11-29 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ba2ce91-4284-3966-b251-e9008c65aa88 | -11.16184 | -43.57841 | 2025-11-29 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92d93eca-cab7-3adb-83f4-b123f1229a78 | -20.9831 | -48.63778 | 2025-11-29 03:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b087aac9-8d22-30e7-a5c3-a7a1ba97fac4 | -20.44199 | -47.51101 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ca5ae62a-e9fe-3be5-b02f-a3a3ed44cc15 | -21.12021 | -48.41547 | 2025-11-29 03:27:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20745df2-01bb-3c8d-a1c9-5b2addf2722b | -22.08101 | -46.825 | 2025-11-29 03:27:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 144facc7-86d8-3762-a2d0-e28b33e46bc9 | -20.44344 | -47.51825 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 151333e0-e00f-3fc6-b225-78797e17f529 | -21.05324 | -41.37103 | 2025-11-29 03:27:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1435b4a-4e8e-3e8d-a24d-27bd2f9ede67 | -20.75035 | -47.20805 | 2025-11-29 03:27:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d255f3e2-d7f2-3db4-99be-baede44de4d7 | -20.41391 | -47.22161 | 2025-11-29 03:27:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 31fc9596-08ff-34d5-9cba-4216d508b2ec | -20.21452 | -47.53628 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f10d7895-e205-3ea9-84e4-dcda752336c1 | -22.72638 | -49.34621 | 2025-11-29 03:27:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfab8f3c-83f9-35d3-8071-6680dbb53e8d | -22.76099 | -44.98777 | 2025-11-29 03:27:00 | NOAA-20 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 35831029-8913-33a6-8430-0cb7a79f24e6 | -20.98514 | -48.63928 | 2025-11-29 03:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5445a329-8ce9-3569-892b-2b9da3b2cfb3 | -20.45168 | -47.51324 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef1bf09f-dd6b-33e5-ae89-775e893a8ab8 | -20.98009 | -48.62989 | 2025-11-29 03:27:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 50257575-df16-3055-8fdd-291a0886e792 | -21.6827 | -47.9609 | 2025-11-29 03:27:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| befcf613-d940-3fed-8cc8-fe84d2208877 | -22.95035 | -49.06985 | 2025-11-29 03:27:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7281c39-6940-3938-a17d-c5e05aca1be6 | -22.75996 | -44.98836 | 2025-11-29 03:27:00 | NOAA-20 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 866c1070-6a3c-3778-839b-2a7fb6c265e0 | -20.21139 | -47.54907 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80798cef-cbcf-34ae-a5a0-44be144ee5cb | -20.44044 | -47.51751 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f44bcffc-ac46-32e9-97c0-96fb3ac5476c | -20.21605 | -47.53004 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7485fa24-e6a1-33af-af9b-670c213855c5 | -20.4383 | -47.51054 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 83df2bba-a38d-3ee7-82ad-219909c73f54 | -20.44714 | -47.51886 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae471c08-3ece-3e69-beac-fc793ddb5337 | -21.11856 | -48.42205 | 2025-11-29 03:27:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d7a94ec-27b5-308e-9ded-1af7f2e22685 | -21.68432 | -47.95434 | 2025-11-29 03:27:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d700191-a065-3f66-bb7a-58ca1e5d4b41 | -20.21206 | -47.53579 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e0a2015-70ad-361b-91be-46e26d8ab95d | -22.72431 | -49.35416 | 2025-11-29 03:27:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1273f5b0-3805-3b97-b1ae-3d4c0e5e6234 | -20.2186 | -47.53795 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9e6e285-13d9-33e1-910e-f83cbffb0768 | -20.9783 | -48.63707 | 2025-11-29 03:27:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c37b4e70-ab3a-3ca1-8fc2-de1a3ea31a8b | -20.20902 | -47.54856 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f651c412-c46c-31f6-82ca-e27fa0a1a5bd | -20.44503 | -47.51171 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e1e969da-73f5-34c7-9728-bbcd7a2b21d3 | -20.44868 | -47.51235 | 2025-11-29 03:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2b3a6729-80a9-3506-8c67-a942ceeca12a | -20.74888 | -47.21409 | 2025-11-29 03:27:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bf05169-7e3b-3e29-b31c-b9eacd2bf998 | -20.22014 | -47.53144 | 2025-11-29 03:27:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 514541bb-d6eb-305e-a6fc-d027597b8729 | -2.7845 | -47.4343 | 2025-11-29 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6dc4a171-ae0d-39d3-822d-fbbe3e65ff2e | -8.051 | -43.1237 | 2025-11-29 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 410ce3df-7732-34e1-b0ac-34b567cc9c5a | -2.7845 | -47.4125 | 2025-11-29 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9299a1c9-01ad-3813-8fb9-96433a58c78b | -8.0321 | -43.1257 | 2025-11-29 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| c6cbfb9b-adee-32a7-b4b8-2289b42a70e4 | -20.2016 | -52.3717 | 2025-11-29 03:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8c115075-38dd-303d-a25f-baf685d50f7d | -2.6322 | -48.542 | 2025-11-29 03:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| be53a0d2-f5a4-356c-ae00-c9b832c69ddc | -20.1813 | -52.3754 | 2025-11-29 03:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e43cf1fb-e85d-3d67-b3e1-8d4715e4297b | -8.1633 | -43.2055 | 2025-11-29 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 7e86d338-8a9b-36fd-aec0-1e885f4fe2e9 | -8.1822 | -43.2034 | 2025-11-29 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 17d93a56-b248-32b8-9e75-972bf7f5e4e6 | -2.7845 | -47.4343 | 2025-11-29 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 0cf24007-5b45-363c-81c8-a08c4e50abdc | -8.0321 | -43.1257 | 2025-11-29 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| a6fd33d8-0eda-3877-86e7-7b7dc56b5e52 | -2.7845 | -47.4125 | 2025-11-29 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |


[Clique aqui para ver as próximas entradas](README12.md)
