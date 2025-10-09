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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faba5b8a-43bc-3bff-aa5a-0c108015da4c | -18.99388 | -43.0908 | 2025-10-09 03:34:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5531c3d5-5f3d-361f-8d2b-7a189603e50f | -19.71787 | -44.00683 | 2025-10-09 03:34:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9118618e-7beb-34c6-885f-126a5dd64d90 | -19.55373 | -44.04802 | 2025-10-09 03:34:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acce0347-9241-3c7a-82e0-7be12b96441b | -20.29788 | -49.69707 | 2025-10-09 03:34:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8055a3d3-7734-368c-ab44-d60a7a007b9e | -18.24961 | -46.99285 | 2025-10-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c1333e5-2cfd-372a-b59b-eaf5d757c5a1 | -18.78132 | -44.61626 | 2025-10-09 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fadfa8f3-838f-3a40-b41b-f8b6ef3d8d6e | -19.50385 | -43.83632 | 2025-10-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70a6f795-5e0f-3da2-813a-425508c32a25 | -19.54483 | -44.04024 | 2025-10-09 03:34:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13e85e9b-e2a7-31ff-b252-df32284747d4 | -19.50314 | -43.83825 | 2025-10-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 268531ec-95aa-3ef6-99e8-de9655372fda | -20.29949 | -49.69054 | 2025-10-09 03:34:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ce1c9bd-4c37-303c-87de-5d466931a3f3 | -20.11119 | -49.54251 | 2025-10-09 03:34:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6f626122-019f-3072-a8c9-39abda684d1a | -18.78659 | -44.61749 | 2025-10-09 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| accadc38-21fd-32db-8da9-4d6d1b995a2f | -20.12632 | -49.53989 | 2025-10-09 03:34:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bfe1105a-4124-38d0-82f0-eca5bd99d00d | -18.78205 | -44.61276 | 2025-10-09 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4967afd2-81ce-3f56-81c2-60e5fab3c929 | -20.30634 | -49.6923 | 2025-10-09 03:34:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9da0894c-3b09-3819-aca5-8c2070dcd644 | -18.54278 | -45.06909 | 2025-10-09 03:34:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93858b12-84c2-3963-b04c-dad0dc17ab7a | -19.5032 | -43.83939 | 2025-10-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32eadbc2-d6ef-3e99-a830-7f60ee407b3e | -19.50875 | -44.08713 | 2025-10-09 03:34:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6be699e7-341d-3b68-b62e-41576b64514a | -19.33904 | -43.90339 | 2025-10-09 03:34:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6bd4a58-ec1d-3d6c-bbaf-4ebdffa230f8 | -19.71855 | -44.00361 | 2025-10-09 03:34:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc8dd1c2-c672-3c62-bd27-63d0a74e3dd5 | -8.521 | -46.2201 | 2025-10-09 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 327c5481-f47c-37ad-8732-8a91af1b11ab | -14.4138 | -43.9672 | 2025-10-09 03:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c2095d8c-3485-3bff-aa6e-58c6088ec192 | -17.8413 | -57.6459 | 2025-10-09 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 187cab2c-3cd3-3942-b7cc-2a451c430301 | -16.7518 | -43.9645 | 2025-10-09 03:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 1a7346e8-88f4-3596-b37a-5d590d52104a | -8.5398 | -46.2181 | 2025-10-09 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| eb8b6c77-d66d-3861-9b6d-f48a3b9d2b76 | -6.6995 | -46.2946 | 2025-10-09 03:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 1d077369-b433-3dba-ac21-22b9db0954a4 | -8.1993 | -43.3424 | 2025-10-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 54fba36d-7524-372e-a568-03024f0fc23e | -6.6808 | -46.2961 | 2025-10-09 03:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 481bf38d-3cbe-3245-8e68-0fb26d828d64 | -18.4118 | -45.2394 | 2025-10-09 03:40:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4fde0761-2914-3838-8dab-f281fc8c0fb9 | -6.6993 | -46.3169 | 2025-10-09 03:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 844875f2-e8a2-3fca-b782-6b53947b09f7 | -8.5398 | -46.2181 | 2025-10-09 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8f608d23-937c-347f-93cf-2fab4d34a230 | -8.5212 | -46.1976 | 2025-10-09 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 98b8d6a3-04f7-3089-a869-a5f7457e607a | -8.1993 | -43.3424 | 2025-10-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| a7ab8823-ce3c-3d1e-944f-5a158c3adb71 | -6.6808 | -46.2961 | 2025-10-09 03:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7cba02b6-e3ff-34d4-bdcc-3582f7070fac | -8.5024 | -46.1995 | 2025-10-09 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 41c6c8eb-9fa1-3257-ad99-c72a1a3fcd79 | -17.9227 | -57.4922 | 2025-10-09 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 328b5239-0c28-3d66-bda7-7baf50ac6ba9 | -6.6995 | -46.2946 | 2025-10-09 03:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 61648963-bdaa-3672-8d33-39a227030d56 | -10.5275 | -50.0208 | 2025-10-09 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 5571a6ce-93bd-3333-bb30-1547ece080cd | -17.9224 | -57.5128 | 2025-10-09 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.2 |
| c3c149e3-c020-33d4-abfc-2d4ae770bc4c | -8.5021 | -46.222 | 2025-10-09 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 36678a21-c31e-3313-bff3-3c4955ec4520 | -18.0013 | -45.6174 | 2025-10-09 03:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 0a3b99bd-ce25-3ddc-b082-40c660597ec6 | -16.7518 | -43.9645 | 2025-10-09 03:50:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9fb153bb-1150-3653-bff6-6e348a286c40 | -8.521 | -46.2201 | 2025-10-09 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3323edad-edb3-3f64-94fe-64e3ee51a1b7 | -1.40289 | -46.7115 | 2025-10-09 03:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f9ab5e9-03fb-3751-a658-ead355c553ea | 0.33237 | -50.95815 | 2025-10-09 03:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08146532-0297-305f-9017-e9027e6ee83b | -3.25737 | -39.42171 | 2025-10-09 03:55:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48e92ea3-80e6-3bfe-ac29-3281fc18b85a | -1.40837 | -46.71242 | 2025-10-09 03:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b376850d-e75d-3e44-ab14-220a09f918f3 | -1.40894 | -46.7089 | 2025-10-09 03:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a595df77-c8ef-3820-a3bb-e78b8a4c0719 | 0.33966 | -50.95691 | 2025-10-09 03:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 219cfea5-d48b-3f40-a13a-bfff8d6ed5f5 | -3.09837 | -47.01971 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53e382ee-9275-3a8e-a036-a2340787e134 | -4.50913 | -38.82117 | 2025-10-09 03:57:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b463718b-e16c-37f1-9cfe-e516e46e7335 | -8.5952 | -48.24376 | 2025-10-09 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aab49b3-a660-371f-bbe6-8942228da33f | -7.28256 | -41.97294 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 661e9009-8dbd-3337-84b9-62360892dbd0 | -7.55947 | -44.30299 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cb9a99c-4937-37fc-b6da-da70e17a4388 | -7.76995 | -44.03377 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14064bcf-7651-3570-a478-cf0c93fcc25d | -8.29248 | -40.6815 | 2025-10-09 03:57:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 287013cc-e963-3857-b2d3-ce9b211f4c6f | -7.68474 | -42.39641 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 858e49f2-eadc-369c-9200-14482a7f90e9 | -4.89083 | -42.25059 | 2025-10-09 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e3180090-8cc9-38ee-bba9-1363ccc28f71 | -7.50132 | -42.73104 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| baaf3da3-ad6c-3a46-aadc-caaa873e9dae | -6.73497 | -42.22462 | 2025-10-09 03:57:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1206d17f-1bf2-378b-b5ff-db8802c65a78 | -7.76647 | -44.02936 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a363c6b8-b305-3bfe-9e49-99b67af3867e | -8.6006 | -48.24464 | 2025-10-09 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2039044-1076-3348-98d7-85bf0d59c15b | -5.01211 | -45.32225 | 2025-10-09 03:57:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf619d26-fa0e-3e7a-af5c-149973260da5 | -7.79191 | -42.60714 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 025c6932-9235-34b2-b051-54d1dc138693 | -8.53043 | -46.19524 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c1f9842-1b0e-3ab1-a059-575ef19f30c2 | -4.43971 | -43.22723 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70b9bcaf-9263-3bfd-8ed3-0ea94b79ae34 | -7.02309 | -42.74807 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 79523773-7d40-345e-918d-9a5d1a096b6f | -5.44695 | -44.82474 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8055e96-3d7a-3556-b74f-c71f1f751c17 | -9.08547 | -47.95504 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f501b44-0ca2-36fc-ae58-fd90c04d1512 | -9.76502 | -47.71082 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4f31701-086f-3111-972f-a9a6c9f970e5 | -4.84869 | -42.76776 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1f654e64-205c-3d48-84fb-f7120d8a0fb8 | -8.51899 | -46.17753 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c3d4a97-9124-3dc7-8ded-550c7e0f80b6 | -8.52774 | -46.21071 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 98856252-98ed-3b4b-8456-4b63eebb77a4 | -7.81934 | -44.16928 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8983bbb2-8d30-3d08-aae0-e71fb675dd9d | -7.52664 | -42.0048 | 2025-10-09 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 871c1ae6-13cb-30e1-ae28-12160b8b0dea | -9.21662 | -47.85748 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 879afdda-e042-3df7-8c47-3f476c5435f1 | -7.83365 | -44.14495 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6230767-7ce8-3232-969d-af828b998ebf | -8.17248 | -43.32157 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 15bc1d44-64aa-32df-864a-7883733ea578 | -4.90362 | -45.942 | 2025-10-09 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f14b57da-f83f-31a4-b0eb-b6ce3ec43f52 | -7.27748 | -41.98095 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce6aae17-7572-326c-8c13-d2322a0bcf9a | -9.76211 | -47.69783 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deb67bc1-4ba6-3083-acd5-cd3e5bc4182b | -6.92711 | -45.05532 | 2025-10-09 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1db652c4-ee45-3077-bd6a-520847f30f2b | -8.43785 | -47.19025 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 713dec69-a83d-3f41-9953-4429a03b5aba | -7.78844 | -48.0415 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16c105b1-ad37-36fd-a59c-2f529bf7f374 | -6.68758 | -46.30341 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| d635774e-3644-3177-96fd-59417b823f09 | -6.41801 | -43.77357 | 2025-10-09 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cedf24a1-31d0-3c6d-aa59-61c67100a806 | -8.7202 | -47.10252 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cab0b0ad-71ba-318c-a7bb-e9df0deb72c8 | -10.03306 | -42.31514 | 2025-10-09 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d6720b8d-30f5-3aa5-8c2d-ea8e5e6175cc | -8.6781 | -43.9052 | 2025-10-09 03:57:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6df72bc6-d2ac-3fae-aa78-a3e497793c7c | -4.7264 | -43.35023 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| edc7d6d1-5e18-32ab-a7cf-d28cc70d078c | -10.19119 | -44.54329 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe264ccb-4b64-3f9b-946d-8c1ce3ef5467 | -9.6591 | -43.84174 | 2025-10-09 03:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99d91cd8-6f03-33f2-b576-6c029b778718 | -8.61295 | -45.09526 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a51da9f-c7ae-3985-84f7-5ef7e0bc2af3 | -3.95551 | -44.29707 | 2025-10-09 03:57:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb36c57c-437c-3f97-a440-d3e321e8d349 | -5.40333 | -40.97896 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf4d69a5-0dda-300f-a392-83fc3a601927 | -10.19811 | -44.55211 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b92ac1fa-c33a-3ce8-8809-725a63bbfc7c | -5.31119 | -45.37969 | 2025-10-09 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08edf520-66ea-35e8-b3fb-8f0cf854bcdc | -9.03376 | -40.63801 | 2025-10-09 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0c9d501-6607-3ca0-b39c-49b632da162e | -7.83649 | -44.15318 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11809bbc-2f17-359e-8b03-8e85e059c0e9 | -3.44605 | -45.59656 | 2025-10-09 03:57:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
