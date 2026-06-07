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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54942564-2776-33d2-a239-e3ac71d00968 | -11.5499 | -52.7867 | 2026-06-07 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 84d00e85-e3f7-361a-818f-10cd87107fbc | -11.5499 | -52.7867 | 2026-06-07 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b6380d45-88d1-3869-996f-ec6c99280037 | -11.5499 | -52.7867 | 2026-06-07 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| dba25103-ad7f-3013-b87e-1681d390b5bc | -11.5499 | -52.7867 | 2026-06-07 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b877e423-cb93-3f56-b2be-df4900f48b3d | -11.5499 | -52.7867 | 2026-06-07 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6e145f39-a428-3550-bc1f-89963c05e871 | -11.5499 | -52.7867 | 2026-06-07 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b052112c-3942-339d-a1e2-58e0c3b77807 | -11.5499 | -52.7867 | 2026-06-07 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 12093dda-8af5-3905-a120-0bf8c0c632d6 | -11.5499 | -52.7867 | 2026-06-07 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e79c3f70-4fd4-3a24-86e6-e97da07d94d8 | -17.51331 | -41.92049 | 2026-06-07 03:15:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 883a5105-39ac-3836-9708-42e32b97e9a3 | -16.49758 | -43.50396 | 2026-06-07 03:15:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e417720a-6268-39dd-ba6a-94255b374a22 | -16.50456 | -43.50511 | 2026-06-07 03:15:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 771d6abc-c980-3a33-b87e-b327b71b763e | -17.5144 | -41.91557 | 2026-06-07 03:15:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30fbaad9-8da2-3120-b456-2bf870103698 | -15.66262 | -43.3154 | 2026-06-07 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ca63363c-03f0-3751-9d11-2cae5ed3be5f | -16.6095 | -43.36345 | 2026-06-07 03:15:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 718617c8-0a61-3afe-aac3-41e0d33ed43b | -17.51431 | -41.91746 | 2026-06-07 03:47:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0dc84fc6-57b3-3910-b314-c4ae337a4fda | -16.49953 | -43.50693 | 2026-06-07 03:47:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 312dd088-cd15-3b18-9771-54881d165e52 | -10.39881 | -46.4396 | 2026-06-07 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1fafec9-2593-3cfa-92c6-21601c3ae024 | -11.03246 | -44.32235 | 2026-06-07 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49751cc4-f462-3826-98c4-5185e847784e | -5.81253 | -45.12278 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbefead0-3272-3a99-8fe6-c5ee3a8301e3 | -17.51648 | -41.91679 | 2026-06-07 03:47:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5d9b8731-8427-3b4e-9c40-a7865ddd2ff9 | -15.66016 | -43.31449 | 2026-06-07 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e10f052d-93ec-3478-8cf7-731ed25df065 | -5.94248 | -45.5029 | 2026-06-07 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 713d3ea3-565b-33cc-8ecf-1316028c6cfd | -16.50418 | -43.50772 | 2026-06-07 03:47:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e96227e-b494-3ea9-b135-e23ecbe76eac | -5.80845 | -45.1196 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7955f259-5804-3bc6-8e2b-67611ebe0efb | -5.93615 | -45.5018 | 2026-06-07 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ece3a49-7fb1-3dff-8c71-1567dc20221e | -10.39158 | -46.44358 | 2026-06-07 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dd1e49d-d1f2-3c1a-a6da-b868c2b3d516 | -6.98376 | -42.88269 | 2026-06-07 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a96cf900-3c0f-3c2f-b6e4-a36ff3b779ed | -8.94468 | -45.67159 | 2026-06-07 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a759c27-b848-38a0-ae02-560f7ee883f9 | -17.52835 | -46.54314 | 2026-06-07 03:47:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20553b9f-4fb4-3268-8b29-4caa559ba2e1 | -17.53463 | -46.54066 | 2026-06-07 03:47:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 778b73fe-a24f-370d-8331-e2294a416fd9 | -5.80143 | -45.12312 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c70f8ee5-0ec1-347f-9622-c661da52ac49 | -6.98433 | -42.87951 | 2026-06-07 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98c06184-0078-34ea-852d-98c6f70a8c6b | -6.99673 | -43.86493 | 2026-06-07 03:47:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd31a51-da3c-3254-b6cc-6e8bc6552eb4 | -5.80548 | -45.12632 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52a356de-ef5b-3f36-92a2-e363c20c0ca3 | -5.73916 | -43.96134 | 2026-06-07 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e50518b0-3174-3d63-8484-9cac82a21e2e | -5.93968 | -45.50603 | 2026-06-07 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f61a092-4531-3187-bafe-58aaf51f46e3 | -11.03313 | -44.3189 | 2026-06-07 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f3dea8-e493-375d-bf81-def8986c7b3d | -10.39256 | -46.43852 | 2026-06-07 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d1e6f61-e664-3fe4-87cb-66989cb1e174 | -7.11044 | -48.13066 | 2026-06-07 03:47:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6223418-fc28-3c0a-bbe5-3990cfd0c21c | -15.65919 | -43.31945 | 2026-06-07 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59a2aaef-b8b4-353c-a01a-d1df5955d39d | -6.99969 | -43.86498 | 2026-06-07 03:47:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b8bb911-4d5c-3074-8806-bfbdbaf5f0de | -10.39525 | -46.44258 | 2026-06-07 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 810b5157-2b9b-32af-8c97-4cca0d56655b | -17.52915 | -46.53933 | 2026-06-07 03:47:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c91c2ba1-3bbc-3b4b-8635-f04023741d2e | -10.39626 | -46.43753 | 2026-06-07 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42d81aaf-d7bd-3118-b0ff-b9715aecd5b7 | -5.81458 | -45.1211 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 168b571b-13ce-3a1c-9a4f-ad2aaed2f991 | -5.8064 | -45.1213 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee847962-5e6e-3859-b662-8e43cfe16b1f | -5.94602 | -45.5071 | 2026-06-07 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e698728-885c-3e00-b402-c27fc7d579d3 | -16.60701 | -43.36487 | 2026-06-07 03:47:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c61bc03-0d90-3300-be4b-d11864859749 | -5.9406 | -45.50092 | 2026-06-07 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e336a6de-b0ef-3e5e-bdde-0f6af2cebdc3 | -7.00234 | -43.86599 | 2026-06-07 03:47:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a8a0ff8-04be-3131-bb66-cb0b3e15f638 | -7.11765 | -48.13215 | 2026-06-07 03:47:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57736886-83b7-32ef-96b5-820f9e8f2618 | -8.94379 | -45.6762 | 2026-06-07 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db6c34d9-eaca-3c38-ab98-77d715a79209 | -16.50049 | -43.50201 | 2026-06-07 03:47:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9bba114a-60ca-34c0-9aba-fb26718eab73 | -5.80756 | -45.12459 | 2026-06-07 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f7c4403-dbd0-369d-9598-ac3a28f2a83c | -23.76825 | -47.44304 | 2026-06-07 03:49:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c75821c1-5ad5-366e-8a91-ef26b38d77b0 | -12.04305 | -45.27641 | 2026-06-07 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a307d1b0-8294-3340-9b9b-60b6cd0bb47f | -11.47919 | -47.34376 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0308cb51-3aae-359d-ad55-245ffabc047c | -13.36414 | -43.20388 | 2026-06-07 03:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 319d8f44-dd1b-386a-a844-ba1bfeb8bf8e | -12.49787 | -46.2594 | 2026-06-07 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c45ae86-7b27-3954-97ae-693d2b6963c9 | -12.06936 | -48.43582 | 2026-06-07 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d1d3827-0dc1-3850-9562-b1f966311615 | -11.46904 | -47.99118 | 2026-06-07 03:49:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd90fd60-1907-33e9-bfea-7774513edaaf | -19.68674 | -46.02833 | 2026-06-07 03:49:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ccad825-a028-39c8-b419-7b7c5dc7f1cf | -18.84425 | -49.08989 | 2026-06-07 03:49:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 513db5f8-6868-3fd3-89f1-317bd439303f | -12.50383 | -46.26048 | 2026-06-07 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef5196ba-0b42-3e59-a4e2-e4a757b36e74 | -22.41412 | -46.79564 | 2026-06-07 03:49:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72f907da-bea8-32a7-8b0b-73ddc1be91af | -23.7675 | -47.44645 | 2026-06-07 03:49:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c34c801-d704-3c37-b7f1-d57dd1e2f407 | -12.06454 | -48.07684 | 2026-06-07 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 781ae1f5-5167-32ce-9e9b-d0c94a83df6b | -12.40551 | -47.49445 | 2026-06-07 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa126b7e-3a07-353b-a11d-7a56bde62ee7 | -11.47214 | -47.34267 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02d8b732-6e11-332c-b063-d1ae57d0e08a | -11.87405 | -43.90209 | 2026-06-07 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d120efd-4ff3-325e-bc2a-982e602bd61c | -11.87466 | -43.89896 | 2026-06-07 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46186b1f-47d2-3aa8-8eab-f9be870f679c | -18.85035 | -49.09193 | 2026-06-07 03:49:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdf37af4-1dea-3225-8d06-306657536e18 | -12.06262 | -48.43415 | 2026-06-07 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df476570-a1cb-3fbf-9d65-b5522a5f6531 | -11.97683 | -47.36082 | 2026-06-07 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 947c808d-4ee8-335c-b4fb-2056273e325c | -12.0599 | -48.08227 | 2026-06-07 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad921538-45d9-3cdc-bb0b-7e3322d57d89 | -12.04382 | -45.27254 | 2026-06-07 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e06aa5a-82cb-30e5-9d81-2c50ef29d1ca | -12.49665 | -46.26546 | 2026-06-07 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74beb15e-4718-3a60-ba5a-9b63acda87e9 | -23.10335 | -46.5396 | 2026-06-07 03:49:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 562620e8-b83a-3a4e-a597-723b84041c19 | -13.36303 | -43.20058 | 2026-06-07 03:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6ee6793a-c87a-3058-92fd-c7c6a3a510de | -22.41219 | -46.79565 | 2026-06-07 03:49:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3247d95d-8678-30c8-a9c7-4d8cf8fff788 | -23.81906 | -48.71354 | 2026-06-07 03:49:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72661202-040f-3180-81be-eef306c8a48f | -11.47319 | -47.33762 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5175f4c9-84dd-360a-8b50-29919e0f099d | -13.36199 | -43.20592 | 2026-06-07 03:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 203960fc-c6c1-30c6-bb5c-363062ab9bbd | -11.47025 | -47.98518 | 2026-06-07 03:49:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea97b11-32bb-35ef-9ebe-0823d24cee30 | -18.96433 | -41.97068 | 2026-06-07 03:49:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8861aa29-2c91-3ed9-baac-decfbe353f94 | -12.06112 | -48.07652 | 2026-06-07 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f38bf48-11c2-3d42-9c19-74a3cbe22929 | -23.37725 | -47.75766 | 2026-06-07 03:49:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4bb926ba-c319-3192-82ee-526574dda49b | -11.47187 | -47.34678 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7d4b2f2-1826-3a32-9938-099df819cd21 | -23.82456 | -48.71505 | 2026-06-07 03:49:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8818b516-3933-37c5-b6f5-942f56a44060 | -20.6886 | -47.52464 | 2026-06-07 03:49:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ad8e956-5465-36c6-86b8-e3d815a0316a | -12.49417 | -46.27775 | 2026-06-07 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2686df90-511c-31fb-8006-c5300cafa72f | -23.82047 | -48.71489 | 2026-06-07 03:49:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9625568a-4240-3edd-8bc3-b7c5682b01bc | -11.47284 | -47.34198 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fc6808d-09d0-3f05-9232-f281dbc3becd | -19.96397 | -47.20836 | 2026-06-07 03:49:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c306ef97-f6c1-3bb9-ad6d-896026fd7209 | -12.4058 | -47.49699 | 2026-06-07 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 427270f9-841f-30f5-b872-0d9cda506721 | -11.47849 | -47.34444 | 2026-06-07 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1ab0c3e-8f77-3944-a603-7fd254ccdd6b | -18.84745 | -49.08936 | 2026-06-07 03:49:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6939a248-9dbe-397b-9746-5378bcebfec7 | -12.06335 | -48.08261 | 2026-06-07 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f199c6f0-b351-3c40-8d9b-28fb0cf023b0 | -27.12755 | -52.65182 | 2026-06-07 03:51:00 | NPP-375D | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f191ba97-3eff-3342-b66f-13cda6c4bcb4 | -7.15457 | -44.05957 | 2026-06-07 04:04:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README3.md)
