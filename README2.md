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
| 7d60de63-9ed0-3d84-bc7e-53ea72138e6a | -7.06188 | -44.38585 | 2025-02-14 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d3bb1c4-afa5-3892-9eba-6eb54d1feeef | -10.77356 | -44.74234 | 2025-02-14 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1f60f58-29ec-36d4-80f5-d1e3fd2ef21e | -8.12302 | -43.13643 | 2025-02-14 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b08c2a15-f43d-3b22-8999-cea8caa87aab | -7.13072 | -38.77883 | 2025-02-14 04:14:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7edeab3d-2c5f-35f4-8332-d7343fc9142c | -10.66051 | -44.40382 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c3eab84-bdde-3af6-b821-f96f63f0f947 | -6.60343 | -39.38713 | 2025-02-14 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 91553b58-678b-3d8d-97aa-81ac9b6c534b | -10.6572 | -44.40329 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12ccd548-d669-3b96-92f5-3fbd3f74e5a8 | -6.59972 | -39.38656 | 2025-02-14 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 839baefe-839d-3383-a0c5-932a585639aa | -10.49991 | -46.19047 | 2025-02-14 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba5ee972-2c68-3241-b49e-20b20625c408 | -10.64728 | -44.48769 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| badc4324-ff3e-3a34-9a18-839ac73af2d8 | -9.04219 | -40.07696 | 2025-02-14 04:14:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| db714b8f-c557-350b-b55a-97723aab3766 | -10.61418 | -45.1046 | 2025-02-14 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f15061d-b372-323a-b794-cfce9a06a393 | -12.19106 | -38.17241 | 2025-02-14 04:14:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1ad7ca3-d3e2-3c97-8673-6afe52f06ca3 | -11.63963 | -37.79074 | 2025-02-14 04:14:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 572fedd7-070f-374a-b2e5-b65e573623ad | -8.15006 | -44.3937 | 2025-02-14 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88247713-6dc5-3159-848d-7ef839b6207a | -10.64343 | -44.49065 | 2025-02-14 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f183bb0f-1277-3f6e-9719-273de58b3f1f | -7.59677 | -40.2654 | 2025-02-14 04:14:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 85a74f2d-507a-364e-bdff-25c18858c6f2 | -10.67739 | -37.072 | 2025-02-14 04:14:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e7950fed-822a-3b6a-9004-5a65f0a1d827 | -5.28588 | -36.05307 | 2025-02-14 04:14:00 | NOAA-21 | CAIÇARA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2401859 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e98aacaf-68af-30b3-907b-07d94514ca77 | -10.86709 | -44.79701 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e01ca0ac-fce2-347f-ba28-a4584dc1466f | -7.64574 | -45.23534 | 2025-02-14 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7047f8a-a49b-3cb6-b080-3fc8f143dbe0 | -7.54849 | -45.86709 | 2025-02-14 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 667176bc-65a9-3793-8b25-cb6b01764e90 | -7.64233 | -45.2348 | 2025-02-14 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38e90af6-2027-3c37-8aab-dff6de8e4b29 | -10.76969 | -44.74535 | 2025-02-14 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d86dc3-9f33-38a6-88e1-c256a7d69202 | -7.64633 | -45.23163 | 2025-02-14 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8209fb2-d610-35f6-90d9-9de869bddc0d | -10.53481 | -44.59547 | 2025-02-14 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 362d9abb-e4e3-3ae1-8eb4-015f3916f40c | -7.64973 | -45.23217 | 2025-02-14 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75b180c9-9dd6-375f-b7f3-e4d59b5e777c | -10.64673 | -44.49118 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2de160cb-8e62-380a-9a54-b5ec61f24f7a | -10.86765 | -44.79349 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0d921a4-f495-3fa1-b37a-b2bc8518dec6 | -10.65996 | -44.40731 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec1f071c-85ca-3293-80ac-0f3aaddaf669 | -10.77024 | -44.74181 | 2025-02-14 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdbccf3d-3c6c-3f8a-8411-5e89a4780621 | -6.60163 | -39.38399 | 2025-02-14 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3f51193e-5ca8-3b1b-bf3d-7c4095bd747b | -10.65279 | -44.49573 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8edcc414-82a2-3490-bb3f-eaa01bfdd7d6 | -10.64398 | -44.48715 | 2025-02-14 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4b87bdb-0873-3d78-9892-ebf18bc0a35c | -9.17249 | -35.65932 | 2025-02-14 04:14:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87b8de14-b9ef-36d4-ad81-c6087613589c | -10.6728 | -37.07149 | 2025-02-14 04:14:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b3018568-21d9-3309-ab56-febe8ddcb3c2 | -7.06522 | -44.38638 | 2025-02-14 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7042b2ef-b745-315f-993d-31237f644cda | -5.68231 | -42.20245 | 2025-02-14 04:14:00 | NOAA-21 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 002a5bdb-ae3f-37da-89dc-fc366922cb24 | -10.64948 | -44.4952 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2c3fa26-20c7-3fe1-961c-6e6744116979 | -10.61474 | -45.10103 | 2025-02-14 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b93f92a-8632-38b9-9e95-1bdcc681c0af | -6.60096 | -39.38844 | 2025-02-14 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eca68f24-002d-3c59-9ccf-04c0d145ead7 | -10.8512 | -44.31343 | 2025-02-14 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e12ba649-87e6-3257-8460-2c67f1b8628b | -7.30899 | -46.20488 | 2025-02-14 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57197efb-2e8b-3e82-8b09-716c85fede44 | -5.4963 | -37.25547 | 2025-02-14 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48ccbdbd-787a-3a66-9704-b2b1d976a065 | -10.51281 | -44.88448 | 2025-02-14 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2318baf3-95da-3b92-a582-27517d0a18e5 | -8.63003 | -40.44399 | 2025-02-14 04:14:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b341edc-121d-36f7-a049-c3223769de6f | -17.17516 | -42.8355 | 2025-02-14 04:16:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e485094a-0193-35e8-b58d-d578ed4fd332 | -17.61179 | -42.55714 | 2025-02-14 04:16:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82611fdc-b866-3a64-85ff-44abef4692c5 | -17.09533 | -43.8039 | 2025-02-14 04:16:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 035c9d8d-1575-3fd7-801a-750819fc1ce5 | -17.78192 | -42.80901 | 2025-02-14 04:16:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab6cb80-74bd-38d2-8649-6fd7393bcfe8 | -12.46753 | -46.34622 | 2025-02-14 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd4fbbf8-1df7-3bc7-ba96-3b7df099dab2 | -12.32513 | -45.64334 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3138c931-bab7-3640-b0d3-962223d48256 | -18.90669 | -45.03927 | 2025-02-14 04:16:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a361b5f-ce34-3cdc-950a-0a7443ce911d | -14.12025 | -41.67764 | 2025-02-14 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ff8c299-7f05-3ba7-a7da-5e9abda9813c | -17.62452 | -47.00481 | 2025-02-14 04:16:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8087940-be90-3996-b1b1-dd8a9645990b | -11.96377 | -44.6626 | 2025-02-14 04:16:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b881e92f-602d-397b-99fb-e2b9de801c77 | -16.10996 | -46.20174 | 2025-02-14 04:16:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48f03fd4-5572-3d57-b1b0-10eb483ae40f | -15.71319 | -46.44737 | 2025-02-14 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e09635e9-f8cc-3aa5-b02b-0a191ce6ab47 | -11.95991 | -44.66557 | 2025-02-14 04:16:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7817a8e-cf54-3a71-8628-ebbe1a44c38e | -12.33021 | -45.63307 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae8c0abf-552d-396f-ba12-26efb2c16a14 | -14.27507 | -45.17644 | 2025-02-14 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c68ca7ae-a558-312e-92a0-abb911e2806d | -19.22137 | -44.04039 | 2025-02-14 04:16:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cc18e96-3ce5-3677-8589-84e5ba5b4982 | -12.50064 | -46.34033 | 2025-02-14 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77fbdf49-fdca-333b-96e8-d909df0bfafd | -18.12726 | -42.58705 | 2025-02-14 04:16:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac969cf5-1bde-3181-b800-91d355c43d2a | -16.10704 | -46.20082 | 2025-02-14 04:16:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f665b171-e691-3fe7-b17b-c4206ca977be | -18.14643 | -47.8017 | 2025-02-14 04:16:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abeaee49-72bc-3b26-b6ba-b85203bc1bf6 | -18.18696 | -43.39631 | 2025-02-14 04:16:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fc27d13-8b19-38a0-bd4e-481ae5412947 | -12.33079 | -45.62946 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158d4187-5ec0-3c2b-aed8-a7367d724248 | -15.07844 | -48.9467 | 2025-02-14 04:16:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 837d126c-c23a-342f-8fe5-c294f118214d | -12.61804 | -46.60905 | 2025-02-14 04:16:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa276b85-a5f0-3576-a9f5-86ec8cb16692 | -12.33298 | -45.63722 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f11b9880-9aac-331e-9f5a-4170fe74164d | -15.59636 | -41.78116 | 2025-02-14 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 474651d4-4aea-3877-bf94-6b2e81e9d0c5 | -18.07532 | -43.00753 | 2025-02-14 04:16:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2911545b-4eb3-3e5b-98ec-a33328be5f45 | -15.54767 | -41.31916 | 2025-02-14 04:16:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3543253-ea32-3e47-aad6-51be29d4de8d | -12.33414 | -45.63001 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf2f4525-6f20-37d1-bb0b-be598d66be00 | -14.58918 | -42.69534 | 2025-02-14 04:16:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d03ec82-e812-38cb-a9ce-ad5a738d5ef3 | -14.27837 | -45.17699 | 2025-02-14 04:16:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7d7aec8-a103-3db2-9950-5d132b055d02 | -15.02778 | -42.4544 | 2025-02-14 04:16:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a1a9d68-76eb-3eef-9a64-7d240c4ec6f7 | -13.68174 | -42.36455 | 2025-02-14 04:16:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0221660c-abfd-344f-ad27-9a5ce321059f | -14.28116 | -47.41246 | 2025-02-14 04:16:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d899b40-4cdd-345e-bd08-6656582216da | -15.55884 | -46.28291 | 2025-02-14 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bc092d8-6914-36f0-9437-4bfe782792d1 | -16.74027 | -45.77229 | 2025-02-14 04:16:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11274f4-63cd-3b36-85e1-8e7f310e3d29 | -15.02427 | -42.45389 | 2025-02-14 04:16:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8caf161c-9ff2-3a2a-b665-aa669eb7d3cb | -15.56934 | -47.85453 | 2025-02-14 04:16:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fc0baf7-39c0-3cd0-8983-d2410858d758 | -12.65489 | -45.37053 | 2025-02-14 04:16:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97e1f2af-5556-35f3-9821-3e6393671b61 | -12.43648 | -39.89917 | 2025-02-14 04:16:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04323eb3-73e7-337f-affb-3217eb3ae07a | -12.49724 | -46.33978 | 2025-02-14 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a59b1703-8b93-3968-b1d7-0b75fee85bdf | -12.33574 | -45.64137 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a402abac-8fa7-375c-b77a-be05ca8f0f39 | -12.33632 | -45.63777 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7500a8b-6e19-31e0-90f3-8bed298dca3d | -12.32905 | -45.64028 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0d2cdab-1665-3711-8263-9e18c92a921a | -12.42867 | -39.49672 | 2025-02-14 04:16:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d78ae72a-5a80-36ca-ad44-b79199aadb3a | -12.3324 | -45.64083 | 2025-02-14 04:16:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a355d353-0054-3801-8526-805d4a7d1713 | -11.96321 | -44.66611 | 2025-02-14 04:16:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d10ac538-4687-3351-9de5-9ae976474953 | -12.47579 | -44.65297 | 2025-02-14 04:16:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90b28c0e-e09f-3f11-873a-8a3de8173681 | -22.67665 | -42.85337 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8d71985a-3d54-3394-bae4-0ca1491d3c87 | -20.20771 | -47.06033 | 2025-02-14 04:18:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c81a319d-5150-3bb4-8ddf-02d0c94ecb56 | -22.67509 | -42.85628 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 569f79de-ff31-3867-b192-97756b028f61 | -20.2083 | -47.05664 | 2025-02-14 04:18:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e70fdf8-243f-33cf-99f0-7c2be9665b51 | -21.61433 | -48.46194 | 2025-02-14 04:18:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be716a76-70dd-3585-bcbd-c13be4544743 | -20.56021 | -43.26359 | 2025-02-14 04:18:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
