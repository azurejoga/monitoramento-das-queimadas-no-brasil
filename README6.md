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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa044e67-0d34-3588-bb30-dd9d87229b8e | -9.11318 | -47.96083 | 2026-06-12 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bad30012-e782-3f97-b24a-544179bdb043 | -11.25978 | -53.96221 | 2026-06-12 04:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13ae2897-4cc1-3fd7-90cb-9333849e4f6f | -7.33775 | -47.05608 | 2026-06-12 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 472f77e8-3ba6-39c8-bd8e-e2856d2d9b70 | -11.00041 | -46.74231 | 2026-06-12 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a919d643-66e6-35d6-bc24-a19dc91a65b3 | -12.03622 | -47.80302 | 2026-06-12 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37306039-3043-3112-a511-c37da794326a | -9.6967 | -47.69833 | 2026-06-12 04:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984ec146-0b31-3cd5-9fd1-76b6feba6ffd | -20.88698 | -47.93974 | 2026-06-12 04:14:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8e2882b-58e5-39a1-aed1-3bc3b7dbd894 | -17.79693 | -44.57217 | 2026-06-12 04:14:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab4990ad-547c-3560-afb7-b202bdc5eea2 | -14.69155 | -41.36037 | 2026-06-12 04:14:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fcaf8b44-284b-39fe-a18a-4143e1c64f4e | -20.22705 | -50.19284 | 2026-06-12 04:14:00 | NOAA-20 | PEDRANÓPOLIS | SÃO PAULO | Brasil | 3536901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bdb89b99-731e-380a-9e7c-50f4a95da1d7 | -20.88922 | -47.94334 | 2026-06-12 04:14:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50947394-4010-3670-bd63-522145b37ad7 | -13.46273 | -55.76168 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67dde11a-77fb-33ad-88f7-6cfa57c2e61d | -15.84956 | -39.03002 | 2026-06-12 04:14:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f739288a-9e8c-36d0-af07-2a4cd989d1b0 | -15.83811 | -41.99671 | 2026-06-12 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a390a58e-b670-3220-ae01-a918c64689e0 | -13.45631 | -55.76022 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e73ba1c-2aac-39f6-88fa-4730a0fc150b | -13.46393 | -55.75613 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8412a8da-6095-3a8c-9945-331ab39fc58f | -20.22775 | -50.18913 | 2026-06-12 04:14:00 | NOAA-20 | PEDRANÓPOLIS | SÃO PAULO | Brasil | 3536901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 865ba8ff-98fe-36a0-96d9-612f37b853e8 | -14.24259 | -42.7763 | 2026-06-12 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a700036a-d7c2-3f2b-81ce-1f6add03fa36 | -13.45024 | -55.75581 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 985afded-87dc-3995-915d-e255d6ada6c1 | -13.45668 | -55.75723 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8747483f-8114-3f05-bfd3-00dbd28c9d8d | -17.79304 | -44.57521 | 2026-06-12 04:14:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11294d42-c8c3-3b94-a190-a4eb10629f4e | -13.46309 | -55.75872 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1c9a3dd-1dc2-38a4-a837-cfbdf528f398 | -15.43355 | -41.37688 | 2026-06-12 04:14:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b71badd6-86da-3311-9a80-9f7a2c63dceb | -15.83877 | -41.89972 | 2026-06-12 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0144b8d-5b9a-3e8c-8ef2-13dd1c7fc38e | -17.25336 | -43.77969 | 2026-06-12 04:14:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f513bd24-643b-3adb-b766-63b16d5d9121 | -15.06838 | -41.97328 | 2026-06-12 04:14:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 471ce43a-20d8-33ca-b33e-3738c276a0be | -15.437 | -41.37744 | 2026-06-12 04:14:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00b187d5-79c4-39ed-9610-e6baadeca04f | -15.07064 | -41.98124 | 2026-06-12 04:14:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2bb05b2f-58cb-3d49-ae8c-28608a613cda | -13.45785 | -55.75165 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bc7fa95-0270-3ca2-8449-68b6e30ed6cb | -17.6609 | -46.10446 | 2026-06-12 04:14:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02bdd60c-ddea-3bef-bfd1-a0790538b84c | -15.84218 | -41.90022 | 2026-06-12 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0665b77a-b441-348d-b744-c62bcc4512af | -13.45752 | -55.75463 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28cd1231-d84f-3b7b-a7fd-b3c11aa7e914 | -13.45142 | -55.75023 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b95c1fe-94b0-33fc-ba81-40e70242cc25 | -19.7664 | -40.73202 | 2026-06-12 04:14:00 | NOAA-20 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bc2e2d5-3c30-3c9c-98fe-3bdf30e8da92 | -15.83754 | -42.00049 | 2026-06-12 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d16a825-765c-355e-a8e2-105b26dcf49d | -19.38206 | -44.79376 | 2026-06-12 04:14:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 981a1624-0e50-32f1-9f94-cbc4b63438e7 | -15.84275 | -41.8964 | 2026-06-12 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b7eda68-db6d-3dcd-ba0f-3a70ccb14337 | -15.19278 | -42.2883 | 2026-06-12 04:14:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92d7e227-1cee-3ac9-903d-40652277c61b | -13.45873 | -55.74907 | 2026-06-12 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d24d604-caf9-318e-8679-749e5a8b4e91 | -23.02008 | -46.67585 | 2026-06-12 04:17:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71f730c4-bc67-345d-b001-97644afe3cd3 | -23.40553 | -46.4227 | 2026-06-12 04:17:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5797b293-93a4-3472-ae1b-90e2ce5fc7d2 | -21.38848 | -47.01931 | 2026-06-12 04:17:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 360ea08f-e659-321d-9401-fdc1e77ec4d4 | -22.67504 | -44.39493 | 2026-06-12 04:17:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8c2dc7c6-b14d-3ace-8058-103e14478c27 | -12.8548 | -44.3625 | 2026-06-12 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 85b18eee-1b2e-3e9b-a526-3304e7723642 | -12.8548 | -44.3625 | 2026-06-12 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 95d90e3c-ed19-3710-b312-57dd88a6db63 | -12.8548 | -44.3625 | 2026-06-12 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 73b666b6-fb64-3eeb-bebd-828507692963 | -12.8548 | -44.3625 | 2026-06-12 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 20118435-95a5-3357-802c-41469d605316 | -2.10585 | -47.11076 | 2026-06-12 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e43aab37-ac6a-30bb-ae10-378297b3bc79 | -0.08902 | -51.27984 | 2026-06-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 347ae726-7779-34a9-9467-63ac60537a9a | 0.79074 | -51.96762 | 2026-06-12 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1208179f-a0ac-3f91-8da7-1c927c07e255 | -2.04611 | -50.79477 | 2026-06-12 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fc541f84-5141-3647-9ea4-423d77e3f524 | -1.01362 | -47.7813 | 2026-06-12 04:55:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 202405fd-98a8-3d5d-875f-3fd51aef2f22 | -9.00511 | -47.9982 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc249302-1c8a-3029-858f-268bffd83571 | -3.99165 | -47.93481 | 2026-06-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22612a6c-a05d-386b-95fe-cfcf09591477 | -3.5051 | -48.03788 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 711bc273-cabd-3061-8786-6fb56932fa03 | -6.57681 | -47.91373 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fc70d92-42d5-3777-a337-6f9c80231877 | -5.80045 | -45.10496 | 2026-06-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7259119-c2b8-3d44-aa9a-fb7e7fdef151 | -6.4447 | -44.56796 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feffc69e-766c-3e84-8eb6-157a06352a75 | -9.30873 | -48.97266 | 2026-06-12 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2a1e957-5405-390c-bc14-fe18805f533c | -3.50457 | -48.04142 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a774af5-1e9c-37d3-87f4-039d20db49eb | -9.00961 | -47.99877 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f9f29ac-a1e3-3885-bc96-d153e05ae995 | -6.43927 | -44.56693 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 724ec51b-4e64-3b4f-beba-8b3d57c0ae9b | -7.35032 | -47.01793 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e09a6c87-c527-3ec6-b90b-dab9a39b776b | -7.72532 | -44.16647 | 2026-06-12 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 076740d1-7d7a-30fe-b7d7-e392ac5f1233 | -6.44114 | -44.56227 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8acaca32-4a46-375c-860e-3012892a3c18 | -7.63349 | -50.04048 | 2026-06-12 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b29ef5d-268b-3932-9fa2-64bbd64c2030 | -6.57246 | -47.91307 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e81d2a1c-6bef-341c-bc60-3f3bb528469b | -6.18895 | -44.86103 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20c3c3c8-ad9a-374e-be91-af7b6b7976fe | -5.73123 | -49.10077 | 2026-06-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb86dc7-ee0b-3685-9a67-f3d114ecfe70 | -6.58116 | -47.91436 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fab4a3f-e973-3a34-b3ea-e1c15bf8a502 | -6.56754 | -47.91642 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8588f1e-5e19-358c-af18-82459f28ae17 | -7.37209 | -49.87215 | 2026-06-12 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ffb2b90-5609-34a3-86e3-a0b7fec33760 | -9.74263 | -47.87005 | 2026-06-12 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eb243fc-17b3-33c7-bde7-da680fa92e83 | -9.20855 | -47.91484 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0787fdbb-b78f-34b6-a734-5f6ec028d61c | -9.45977 | -48.38822 | 2026-06-12 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5912431c-9506-39e9-96ec-87d5f33e308a | -5.79953 | -45.11145 | 2026-06-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55fa7b58-d5cb-33af-8df3-301f069cf053 | -6.44519 | -44.56444 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c25c6958-0622-3add-8276-d06541758ba1 | -3.50565 | -48.03413 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dc0e7f84-169a-3abc-ac22-c9346bbaf9e7 | -6.39097 | -44.17522 | 2026-06-12 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3510439a-2b5a-3d02-a8ad-5ea65e1942d2 | -7.71961 | -44.16564 | 2026-06-12 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24a2dc20-c4ca-3319-ae71-bcef3700cf0a | -6.1938 | -44.86523 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc8daccb-16e0-3173-9488-af4a31d7959f | -6.44611 | -44.56682 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c2b7cc4-3572-358f-8070-d3af442aecc9 | -3.50099 | -48.03718 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5c05fc8-c180-3be2-9ce9-bd7e9bc6959b | -6.39881 | -44.17279 | 2026-06-12 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2aaf5c11-8a6a-3f79-b30c-2097c84e672b | -9.11093 | -47.96199 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17459720-4003-34ac-a100-c1379fbbd62c | -8.03244 | -45.0387 | 2026-06-12 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8fcf362-3e78-3d3b-965b-0e8530baf02a | -6.39708 | -44.17227 | 2026-06-12 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89ed32ef-763e-3f04-be73-d38d2868d0d8 | -9.21236 | -48.58205 | 2026-06-12 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5283beb5-ed2c-330e-ab41-a58c0e90f955 | -6.44068 | -44.56579 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f71ef31c-9ec5-3ad0-aab9-7f6d37d59d25 | -3.98748 | -47.93412 | 2026-06-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35cbee38-b065-3af9-80aa-a62c760881ec | -5.79999 | -45.10821 | 2026-06-12 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35f8d627-109a-370a-9f3e-a4497b521176 | -6.56811 | -47.91244 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11ff705b-eb1f-3d56-8843-2b32399a7f28 | -9.21308 | -47.91549 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f5651fa-36ba-3420-94a5-a1e5e88e08d9 | -9.07203 | -44.74603 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6f53c06-64ed-379f-bbc4-8617cbe1eb54 | -7.63883 | -45.30156 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f6aba09-5130-3fdf-9bad-9c921253684d | -9.74198 | -47.87476 | 2026-06-12 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45e115b6-7e89-303c-acd1-bc792dcf2c34 | -6.72443 | -44.37866 | 2026-06-12 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6bb67f5-f42e-301a-bd0d-c9a0129a760f | -6.18942 | -44.85769 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5bf50b3-b24b-35f4-b563-994ba3a1fc96 | -7.71909 | -44.1696 | 2026-06-12 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a312642-9f12-3575-b5cd-71193958a796 | -9.69553 | -47.69743 | 2026-06-12 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README7.md)
