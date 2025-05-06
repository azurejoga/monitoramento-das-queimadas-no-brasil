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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5d0f706-8306-3bf0-849d-2ef1cd9d2544 | -8.201 | -48.98386 | 2025-05-06 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c16bec26-369d-3589-b80e-5947977ab55e | -6.70168 | -42.13072 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| b1de9748-a912-3b9a-999e-b25d95633b80 | -10.97502 | -44.43614 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28adf294-f498-3d4e-afa6-9a3b362b531a | -8.30593 | -48.0508 | 2025-05-06 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f9d6d8-90c2-324c-a81a-40035129d472 | -10.98458 | -44.43736 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ba881b4-72c7-3d36-8a74-c5d406df5b8b | -10.97909 | -44.44199 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8951a1c5-6937-316c-9f0a-3b137a64ef0a | -10.34453 | -46.63994 | 2025-05-06 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c19743f9-0e5d-3268-85a6-b1f06e0113e4 | -6.78656 | -47.59604 | 2025-05-06 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 055e2efc-a80a-3b53-b1ed-ee3563ab665c | -6.953 | -42.7911 | 2025-05-06 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa736dbb-607f-373a-8087-9975632b1c22 | -6.94753 | -42.79346 | 2025-05-06 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a1a8874-4b39-36fb-83d2-ff724c49510d | -6.78721 | -47.59167 | 2025-05-06 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fab36e9-1dbd-3f02-b7b6-72a76483a0b0 | -11.39743 | -52.94679 | 2025-05-06 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b01b790-341d-3b57-8537-eb4a2561e070 | -10.9749 | -44.43773 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ce97b15-4b90-3656-a82d-a98710066ee4 | -11.96669 | -44.15784 | 2025-05-06 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8db5ce17-88d6-3b86-8f00-fd0714e368ff | -6.64615 | -55.19329 | 2025-05-06 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca550346-dafe-3504-a8ed-3836699fc60a | -10.98102 | -44.42791 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf9b589e-700b-3d58-bcad-0cdfe49bfcc4 | -12.17689 | -44.34002 | 2025-05-06 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd1e9e03-641f-3b73-866b-addc74fc5671 | -11.39686 | -52.95034 | 2025-05-06 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ba003b-3e12-3937-937a-c3c57c218df5 | -6.71213 | -47.59452 | 2025-05-06 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abbefa1f-959e-3546-9306-888e30fec47e | -8.07528 | -43.12949 | 2025-05-06 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c83ea972-b751-3d39-bc08-d457debc8c46 | -6.70092 | -42.13599 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2d43b3c5-2a44-3ec9-a807-13d9eb70d4b9 | -10.99335 | -44.4454 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baf81d95-6962-3e4d-b11e-83d0a55e020f | -8.0749 | -43.13234 | 2025-05-06 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 97a100fb-1e74-381a-9b13-6203af69f0e8 | -6.69566 | -42.13531 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bb0e9203-d7cc-35c7-8e02-1332f0c2bfe2 | -7.55509 | -45.83678 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5a9e4f0-d3dd-36e9-84c1-095b487ecd2c | -8.2039 | -48.98829 | 2025-05-06 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75d5c310-e28b-356f-a83d-8dc73298e61b | -6.19621 | -48.04287 | 2025-05-06 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb13d792-57a7-3c46-8add-da7e1f4f39f5 | -10.99344 | -44.44376 | 2025-05-06 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c24fd74-5ba7-3711-acf9-e5658372f1a7 | -6.71579 | -47.59512 | 2025-05-06 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2a920f0-14e3-3f6b-83e1-f9cb38965897 | -8.07027 | -43.12881 | 2025-05-06 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 532456fb-78f4-36c2-bd88-c8e777eda675 | -11.97163 | -44.15851 | 2025-05-06 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab040da-3f04-3971-9510-bc44bd51ce21 | -6.95341 | -42.78814 | 2025-05-06 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa05f4de-d64b-39ae-9c90-619c4fbe34b9 | -6.69598 | -42.13324 | 2025-05-06 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d3029ffd-0df4-3023-aeb1-5e6a859a9a29 | -7.55371 | -45.87455 | 2025-05-06 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b52315e-63d8-3007-8a9e-ce3e41056f0d | -12.17615 | -44.34559 | 2025-05-06 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63cd4fe9-0448-3ce1-af47-224cd49c0e90 | -11.3941 | -52.94624 | 2025-05-06 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22ed6f49-1afa-346e-8381-7a22295f04f1 | -14.2169 | -45.47828 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12e23e4a-2f7d-3188-a651-27561b726b1c | -13.04596 | -53.72466 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb4bd343-8daf-3248-8c12-0eaf21e93b3a | -12.03745 | -54.24947 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aae242d-054b-31e3-8644-3065afc6a424 | -13.04931 | -53.72523 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea4871c-7090-3d43-8381-d43650497b45 | -19.56787 | -49.68359 | 2025-05-06 04:46:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9b4d249-06b8-3ae0-a0de-fb5ac1dc3d73 | -12.04087 | -54.25006 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2fbb878-3d25-3b7b-8b84-2a3987ec081a | -14.20945 | -45.46207 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd748d26-e479-3dc0-88c2-6af0936edda2 | -18.87257 | -50.64915 | 2025-05-06 04:46:00 | NOAA-20 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e221688f-41e5-3829-8661-90a99f810914 | -14.21941 | -45.45835 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 246fe9f2-fecc-33b4-87de-ffa1001285a1 | -13.04201 | -53.72772 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79fbe977-b3b1-315c-8619-7d86fe5d85c7 | -14.22747 | -45.46959 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e85f3c99-47cd-31c7-b9b0-e4655d3fbfbe | -12.17224 | -54.24082 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 033cb139-33f2-343b-88e7-f8744e05bc16 | -14.21815 | -45.46833 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68f81c39-f9dd-347f-8088-7cac134bbf70 | -14.23277 | -45.4652 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e36fb01e-4ab1-3693-a459-90c219e1500d | -20.05555 | -49.3675 | 2025-05-06 04:46:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f97934d-1ff0-3858-853d-6fc65fcb9bef | -18.87527 | -50.64661 | 2025-05-06 04:46:00 | NOAA-20 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc9f8fb2-b4c8-344c-95fd-ee0d96fda881 | -13.05107 | -53.71434 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2de8d6c1-de7b-3c2b-8a89-90f7f4149a69 | -13.04654 | -53.72103 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99af546-ba87-3301-91c4-d870a8af3182 | -15.82985 | -46.57773 | 2025-05-06 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 160efc1f-6ba6-3a86-96b1-567d3c877138 | -12.90939 | -55.04051 | 2025-05-06 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c655947b-3b7d-3391-b852-fa16dcc0e60a | -13.04772 | -53.71376 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5d2a61d-b79a-3ae1-9779-42f9c295ed0d | -14.2281 | -45.4646 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6f06148-12b9-3c3a-970f-2dcd824648d0 | -12.71703 | -54.97593 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fcad41a-1d1c-3eb9-a4d7-6fabe22fd09b | -14.2315 | -45.47521 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc71db76-acfd-3feb-b2bd-797b4c9c7699 | -13.62546 | -54.87587 | 2025-05-06 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4606a56-a3c6-3e1a-a741-6e7996ac66ff | -14.22344 | -45.46398 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5235cde0-199d-3f54-abd1-452a04e3ecdd | -14.23213 | -45.47021 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 264ae5c2-8407-3742-b2cb-6ef0667cffcb | -14.23341 | -45.46016 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 310e8b0a-8e68-3687-9621-8e29ccdd2c2f | -14.21474 | -45.45772 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e8e015d-4286-372b-9b94-f093648c19da | -14.21878 | -45.46335 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1832bfe5-ea2f-310d-a2c7-39acea15a3f3 | -14.22407 | -45.45897 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d71d3626-abf7-3879-b0bd-16fcea1ff7bc | -17.15169 | -54.01249 | 2025-05-06 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95e928a7-709b-31eb-96e0-7f596b5e7bfe | -20.05947 | -49.36808 | 2025-05-06 04:46:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d952ddcc-d16e-31b1-9ebc-a9ef9e2d04c3 | -13.66681 | -47.84175 | 2025-05-06 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c737c7e-5204-3696-ab6a-1e908f19c19a | -14.21752 | -45.4733 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bab6cfc-0317-3fd5-ac10-475e3d92ade1 | -14.2368 | -45.47082 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a51d8f00-5414-36a3-9114-b4de5dcfa93c | -14.22937 | -45.45454 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d762e2f6-7bad-3c69-9227-671197bd00b5 | -13.0426 | -53.72409 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed75f946-5f92-300d-b841-11325d28aada | -13.03925 | -53.72351 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e36181e7-2da7-3ae2-ac26-7ad119766c34 | -17.62497 | -50.91402 | 2025-05-06 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a77b9955-aca8-3b3a-bf8f-8a3a065b7d42 | -12.17286 | -54.23706 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5197f73a-a9d3-3b36-b184-9502474cc64f | -14.20821 | -45.47203 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca1ce8d7-a293-3415-9d72-4aeebe9969cb | -14.21287 | -45.47267 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a65f70a-8ab0-30a8-9d20-0270c8151624 | -13.04537 | -53.72829 | 2025-05-06 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b490ea8-795c-30fd-a635-3b9ac0139486 | -14.21349 | -45.46769 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c556c7c-278b-3e4d-87e9-ce51508a22c5 | -14.21412 | -45.46271 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1805e419-b92a-3e2b-a6fd-f0c547de43a1 | -14.20883 | -45.46705 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd65893a-2447-3e03-ac84-6578fee048a1 | -14.23743 | -45.46579 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94fe3655-07d8-336e-ad40-418147a7eaa5 | -17.7808 | -42.80843 | 2025-05-06 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e885743-ba14-3d09-a9b3-4e74097439c3 | -17.77457 | -42.80772 | 2025-05-06 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6351f43-b660-3dc5-baab-17c514ebe057 | -14.20759 | -45.47697 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90fa3ff8-db29-3178-855a-2e19ab43efaf | -17.15227 | -54.00886 | 2025-05-06 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beedbd7e-1306-377f-945e-f9d2327fb7a5 | -12.35732 | -54.52265 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bfde0685-6560-38c6-a72b-3706be22a82d | -14.21224 | -45.47763 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdabc088-e109-3dd6-893c-e936ae62eeec | -17.77499 | -42.80767 | 2025-05-06 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8793652-281f-3ed5-8f09-5ab5d2e61dbb | -17.62146 | -50.91344 | 2025-05-06 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba6e03b-77fd-3355-802c-e66bd4744be5 | -17.15501 | -54.01306 | 2025-05-06 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524eea49-4ffd-3660-ba20-0a3b1214a565 | -20.0588 | -49.37329 | 2025-05-06 04:46:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b8803e3-3ecf-3002-b756-2999d6feb271 | -12.35387 | -54.52205 | 2025-05-06 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 239475ee-738a-32e1-a0c6-a3c5a35163f1 | -17.78038 | -42.80851 | 2025-05-06 04:46:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4c08092-0556-33e9-8025-76c0af84dbb0 | -12.9129 | -55.04111 | 2025-05-06 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7b686e-6d4e-3ff2-803c-40c1ac01b32e | -17.62437 | -50.9181 | 2025-05-06 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df66814d-6387-30ce-9ada-6edf2f919bfe | -19.05273 | -53.45273 | 2025-05-06 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0936b6c1-ac4b-38c8-81e4-2b481381d229 | -14.22874 | -45.45958 | 2025-05-06 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README8.md)
