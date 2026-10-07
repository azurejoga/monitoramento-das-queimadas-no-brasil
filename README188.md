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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a82b3324-e6ff-30af-811c-b946e240f602 | -4.288 | -43.02435 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b3480fd3-93bf-3387-a29a-6ede7de6b9a6 | -5.85778 | -45.20001 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97441d3b-0ad4-38b2-b02d-7013ab76f447 | -8.20106 | -35.39078 | 2026-10-07 16:37:00 | NPP-375 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1e4e110f-13de-3945-8684-91f48bc1e3ce | -9.9734 | -43.50164 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ae8e2edd-b38e-3aac-97b0-e52b533b6108 | -15.46453 | -41.20346 | 2026-10-07 16:37:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a18504db-6b66-324d-bc44-1d8c72b3872b | -10.9942 | -45.47849 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 26f504d1-a0a3-395e-99d1-1544cdfc047b | -6.43166 | -38.14117 | 2026-10-07 16:37:00 | NPP-375 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 9ad6a6cd-4088-35d9-9d3f-6342430cae63 | -7.86905 | -44.15514 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b4060398-f45a-36ab-9afa-41e505a0aad1 | -4.58111 | -40.77343 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c44b8d18-ea8e-31a2-a4f4-9156135972ed | -7.87605 | -54.97074 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 855ec1d8-2f1d-39b9-bad9-d8240f2de858 | -6.04762 | -42.59789 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 95e27849-3e42-3520-80a5-bc9ecc4dc01d | -5.98379 | -40.92359 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| acbc8837-80c4-3226-9910-0c2ca2e5c5a4 | -5.69298 | -45.2907 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7b9c4f1e-81ac-376b-8410-95fde230e72b | -7.59449 | -37.31107 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6bf6f36e-c2dc-3b46-a909-b3740df6b5cb | -3.87936 | -44.10713 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| faf06ece-c424-3ce7-8e91-bb1a2a71fd65 | -3.66523 | -41.44871 | 2026-10-07 16:37:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d4bbbc2b-a50c-3754-ab75-873f6b9f43a4 | -9.53477 | -46.85884 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9b025d74-5f0e-33ec-8a85-c6e56cec845a | -8.99621 | -45.93751 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 623dc455-3578-3161-b1af-6bc241c7e53a | -7.8693 | -54.96685 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 26769d4b-5625-309b-afe5-62975ce35006 | -4.97713 | -48.66113 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f291a2a1-6624-340f-9a2e-129db2dc23c3 | -4.84331 | -40.40135 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 26.9 |
| b96a6b33-783e-3960-8107-9816b496a947 | -16.05353 | -39.85836 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| f04a8ec0-a525-36e1-90b7-d1939a12e12a | -10.07895 | -45.98798 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2234dbfa-c1f3-3470-a641-16cd427fa9ee | -7.07664 | -35.29367 | 2026-10-07 16:37:00 | NPP-375 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56f3885d-c41c-3cf7-acd0-f60741a4948b | -11.32082 | -46.68484 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f263101a-e391-38b0-be0d-f23210f77dff | -3.75853 | -40.74432 | 2026-10-07 16:37:00 | NPP-375 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| ad95e40d-6815-370a-95c5-fbd90a6179a1 | -10.52609 | -47.28542 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e1ffdf0b-4155-3d1c-96ed-6a659f4fe94f | -9.37713 | -45.93428 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 35358756-7334-3a6c-927b-c6ca64ab18da | -8.39052 | -36.73328 | 2026-10-07 16:37:00 | NPP-375 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 0b3e126a-c004-3e6a-98a4-6dfa046f46cb | -6.94618 | -45.27161 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d5c0b8e-efd4-3918-a7ee-4813ed809354 | -3.8085 | -40.45564 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 088b2201-9b7c-365a-a107-319b4e860e60 | -6.04649 | -42.5906 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0d40d1c5-bce8-33f7-9bfe-b0a741484de8 | -10.39778 | -47.52634 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3d8bb863-53b9-335a-8470-523ffcdbbc4d | -9.92493 | -45.74269 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0ff64084-f90f-31a7-8919-8f28d16c9781 | -6.21161 | -52.81202 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5a9a1bb-9653-3fb2-afcd-4b15c236e369 | -3.94354 | -42.33036 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3fdfc5d6-5d8b-3a04-b9cd-6be5abea7ce0 | -6.15152 | -53.75554 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 79e9d8a3-088a-3c52-9294-b31a64482057 | -5.95955 | -55.34529 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 71d90dab-f3e7-3c42-9ad5-018b376e77c6 | -7.00374 | -43.69151 | 2026-10-07 16:37:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7d154922-6c0e-3511-85c2-b839c9499a7b | -6.60377 | -37.88572 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e88b5965-416d-37b3-9cd0-f05106d666cd | -8.40288 | -38.84893 | 2026-10-07 16:37:00 | NPP-375 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e21ee127-8d27-3560-abe7-92233b355d83 | -5.17444 | -42.68322 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c52fb3bb-bbc3-335c-872d-73345e1fa7ac | -10.99478 | -45.48243 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ba3f6b57-ed37-3f91-8819-c6cf831cb08a | -10.79412 | -46.54355 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 444c27ce-95c9-3c5f-8961-b5928d998fd2 | -9.71032 | -35.92508 | 2026-10-07 16:37:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 60bd86cc-8a9e-37cf-9867-8b50931bd3db | -6.48537 | -52.82516 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 20bb5b5b-ef25-3305-b8de-6ef69b218710 | -15.39599 | -41.69899 | 2026-10-07 16:37:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 6845a670-c993-35db-a3e5-2fe002fdbfe8 | -6.48582 | -52.82833 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 12f18e80-2d11-3633-8d08-62595318d978 | -6.6504 | -43.76606 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78f8c567-1006-3f22-a319-fa2021af3115 | -7.59931 | -55.73344 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 433867bb-a76b-3821-babe-bf2c885a94b2 | -6.93286 | -43.67051 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 56adb70c-fc0a-3255-a392-701ef22aa9ca | -8.03106 | -47.96261 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8b314f1-0642-3d52-be9c-172ea35a57f5 | -7.53517 | -50.76002 | 2026-10-07 16:37:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d5a11f4e-f28c-3d5f-8adf-bdc227485223 | -9.94659 | -43.54881 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b139545b-1b2c-3f49-af2d-cbd484f50dde | -7.75029 | -54.9571 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b0f6b66c-2cb9-371f-aab7-c37332d6c7b6 | -6.18662 | -44.3157 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92558e5c-9cc0-3a21-b3cb-4b54eb522ed1 | -5.95743 | -43.87942 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b22d05c-1f71-3545-8012-24b93833febf | -6.47588 | -51.23297 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 91a943b1-6b37-3625-a7b3-33ab69e3ea12 | -15.53189 | -41.24752 | 2026-10-07 16:37:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.1 |
| 5ea19403-7017-3018-9b95-823969e3b4eb | -5.67952 | -42.5885 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 5d92e6d0-d406-3670-8c18-a52cfe37c497 | -3.75419 | -40.83821 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e020d9e1-747c-38eb-ae3b-b67705bc8039 | -6.09851 | -55.72659 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aff244ec-8076-3412-91b7-d3eab77a6acb | -8.19527 | -46.33876 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91075bd6-597d-3034-95db-e42fde3f89b2 | -4.59009 | -40.28992 | 2026-10-07 16:37:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c00aeabf-206a-3c01-99f5-ba64ca089869 | -11.04935 | -45.80827 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 72228cd5-cbe9-3f79-a9df-ea63372db855 | -11.44366 | -47.65648 | 2026-10-07 16:37:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 737f24a8-6066-37b7-bbc9-4bec2639f126 | -6.3365 | -55.3241 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28e27639-7291-31e5-bced-b3308a4b29c7 | -7.04007 | -44.30449 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85691e71-e891-3d0f-a597-55dcc4e5c0f7 | -5.82049 | -53.83685 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 725795f6-2ca7-30eb-b9da-5f7fad42b4c9 | -6.05179 | -53.4893 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e15c4a33-abb5-3434-be71-8726ea7ac8b6 | -17.52713 | -45.46293 | 2026-10-07 16:37:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1eda2f88-ea50-3c93-8f57-d221ad5e9634 | -9.0362 | -46.90216 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 36c2b467-f151-3db1-9dea-f29f301a76fa | -8.52804 | -54.61572 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b659867c-4bb2-305d-b555-1e6788e0367b | -9.93839 | -45.73672 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 00be43f6-abd5-3160-a111-67987f2838dd | -6.88025 | -43.68217 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1dd22354-c0f0-307b-8912-fc71eedee0ec | -6.48355 | -52.81239 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 939cb786-5dd4-3371-a486-592473744a03 | -9.10376 | -45.10815 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 078b4875-8ce0-3dea-9d74-20be310564b9 | -14.70247 | -41.26156 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 166.8 |
| b3e5c795-3dd2-32d4-a3db-e9bba40d204e | -9.86343 | -46.0644 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d6b04102-026e-391a-affa-f6056a0f36eb | -3.53524 | -44.84109 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 869e1b30-39f0-3412-be5c-1ae26533bdc2 | -6.33523 | -55.31464 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fe0bd0cd-98eb-361e-95e5-5edf41afdc72 | -5.95003 | -46.36802 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 639693fc-92ca-30ca-9a36-a46fb743c010 | -3.98527 | -45.71145 | 2026-10-07 16:37:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 769a6a2c-7635-303a-acd8-784d45238220 | -7.459 | -43.20376 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a9203942-826e-3ceb-a771-a82a33664846 | -7.41181 | -35.08875 | 2026-10-07 16:37:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c0108efc-167d-308f-b2ee-35d232daddad | -14.85237 | -41.16555 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8f49b20d-3b92-302f-87be-6711efa8960c | -3.20255 | -42.6168 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cd3c88c2-d824-36e3-883a-ab7befc9271c | -9.02856 | -41.46509 | 2026-10-07 16:37:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e5f12ca0-d9db-32f9-ab10-39e38bfb38a5 | -16.13048 | -43.74382 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f15ec43c-d5ff-3c49-8379-ec50fce14b8f | -4.61864 | -45.51897 | 2026-10-07 16:37:00 | NPP-375 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e668da3-1028-3719-a445-08288755b16a | -8.98514 | -45.93525 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d8e076b-2052-3a94-bf17-1a5e586b56db | -8.53733 | -54.59157 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b0aa0c75-d83c-343e-9ec6-e113b312a0f8 | -15.46396 | -41.19983 | 2026-10-07 16:37:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cc5ac15e-6053-3b77-9f47-796d4d7f1fbd | -9.39637 | -45.81965 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ce2d3d7e-0439-397e-bc1e-a856b8570469 | -8.97682 | -48.93715 | 2026-10-07 16:37:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4dd67206-9cd1-394e-a766-7dcd62f4ed8f | -6.58587 | -41.58516 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 92edc5d5-c713-3280-8e41-a20e9f0e962f | -15.41125 | -39.25005 | 2026-10-07 16:37:00 | NPP-375 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7940af02-b3bd-38c5-b87b-24302a0f83c4 | -11.39235 | -47.54834 | 2026-10-07 16:37:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d85caf3c-666f-336d-9adb-364e5acf4ed6 | -4.7852 | -43.34181 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e00c9b18-e943-329b-a2aa-a80279ec690f | -6.90476 | -45.01894 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README189.md)
