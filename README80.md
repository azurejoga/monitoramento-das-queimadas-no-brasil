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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c039e5ae-40dc-3971-9b86-488e93caa236 | -16.70681 | -54.94766 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 460be139-bbb8-3637-8127-a5631967adbb | -16.06011 | -59.42849 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88bd958c-320f-349c-a7d9-b28a0a153a6d | -15.99926 | -59.43281 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78cf4f68-a9f0-3f4b-93c8-ea90709702f4 | -15.86333 | -59.42716 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04aa150c-56a5-34a5-b19a-f4011286c963 | -16.05144 | -59.43225 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a15df08-9a99-34b3-b1dc-fd0fac1e3ce0 | -16.6979 | -49.78202 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| def7e348-c5db-384c-ac69-1a76cf02a2eb | -15.77692 | -53.45166 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f70c645-6417-3954-8ea6-dd58ffd8bc6d | -16.00837 | -59.25003 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4714395-f295-3600-a386-981b7b1a683e | -15.99275 | -59.26119 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 108d8ca2-5bdf-3bce-a507-b3fafc73ef04 | -17.07575 | -45.82294 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1774c08-9600-38fe-b8a9-dbdba7b6f6ff | -17.07997 | -45.83345 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5c9c9b3f-893f-364d-af5d-a68acd957a1d | -16.59589 | -42.90567 | 2025-09-16 04:53:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ead2e35-48e8-3ecb-ae55-e6cb29efd675 | -16.06915 | -59.42799 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7354d00b-df77-314b-97d7-fe69523df9d5 | -17.16533 | -49.37871 | 2025-09-16 04:53:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc80f320-19f6-3c23-a707-d9536682aeef | -16.06573 | -59.41927 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f283541-4dd7-3236-947a-5480bfd9e48a | -16.00925 | -59.24513 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89e4d31f-6c63-34b3-8602-f7b9609efb1f | -15.82627 | -53.46712 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23bcfcbe-e58b-395e-a525-512ee16cc5b7 | -16.70285 | -54.97282 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 668586ef-11d3-3dbe-910c-cabd24870279 | -16.51813 | -43.55058 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f922afbd-1f12-3c25-a7c1-7bf1cb49b564 | -16.93471 | -44.07299 | 2025-09-16 04:53:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fd12898-6b9d-3082-84cc-ee2041705880 | -15.79869 | -52.17463 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dcec231a-521a-36ab-a306-7c45f89714d8 | -15.01726 | -55.34103 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d426a060-b265-3161-abd5-8b52fe871d33 | -16.0204 | -59.4267 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f1ac82e-dd88-34f5-9a0d-752beb28e81a | -19.85617 | -49.0782 | 2025-09-16 04:53:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a3a6a4d-37e9-3e7d-ace3-de4e8eef3a21 | -21.2016 | -44.37362 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 72de226f-4482-3802-b971-a113020ebc58 | -19.00822 | -49.93144 | 2025-09-16 04:53:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e4b95ca-aeb1-39db-b07a-2c55ce099679 | -20.86225 | -46.21212 | 2025-09-16 04:53:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8060c0f5-595c-3458-a8db-41fcbc059682 | -21.9234 | -48.245 | 2025-09-16 04:53:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f9be9ba-1598-3b0f-98c3-3cd2c35d9d7c | -21.58459 | -46.80158 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4554b62f-559d-30f8-b29d-9d1a38eb25a4 | -18.56046 | -49.25849 | 2025-09-16 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9926ab2b-8a37-36ec-a06a-35879d97c32c | -22.08794 | -46.65477 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8a2287aa-3dde-31b1-a30d-127cb5b512ff | -21.21819 | -46.94845 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a81ffe5-d4e8-3360-bb8a-700b69745458 | -20.38336 | -46.02765 | 2025-09-16 04:53:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2019c2ec-4338-3905-aa8c-5789c95d9e0a | -21.92309 | -48.25092 | 2025-09-16 04:53:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48071f73-a2a4-3e4c-8c21-3fdaedd0cbe7 | -19.87007 | -46.74224 | 2025-09-16 04:53:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7de8e94-e80a-34f7-88c7-9a2a403d249e | -20.20398 | -45.37129 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6d57bedb-5876-33c3-89a0-5d96fda99903 | -21.20203 | -44.3688 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e1e0d35b-207f-34a7-a6ca-c64e24b8c849 | -18.13991 | -51.79087 | 2025-09-16 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 021ffed8-02c7-3026-8a58-73ef09a47585 | -18.13563 | -51.79473 | 2025-09-16 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a6475cb-d8f1-3ad4-b228-74be91300168 | -19.84071 | -46.45877 | 2025-09-16 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5930cbc-064f-3c56-b40f-13733f1fd07f | -20.85967 | -46.21587 | 2025-09-16 04:53:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9fbdf82-0820-3942-8777-955aca7c79a8 | -20.20437 | -45.36748 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| cdbf87e5-ab90-3a14-a4ce-77a3e7f86203 | -21.19599 | -44.36784 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f58028ee-54bb-34bc-9cf7-aede48cc2be2 | -21.26542 | -47.01243 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1131f1dc-a0a9-3c23-8602-786ce407d6a2 | -21.22339 | -46.94873 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 501cd635-621e-3a38-ba6d-0a4599f8cc0d | -18.55617 | -49.25794 | 2025-09-16 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 30aeeacd-8cda-3685-9d4e-5146715d9a4c | -19.45198 | -45.31074 | 2025-09-16 04:53:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c72ac5-7a8d-3b07-bbac-b28facb38e8a | -21.21884 | -46.94232 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1ba1c12-fd4f-38c5-9be0-9951116c0955 | -22.0826 | -46.65435 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f7f6ef8-9327-3a96-85d8-89fea90eb2c9 | -21.92281 | -48.25067 | 2025-09-16 04:53:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f214083a-e8f5-3559-b6d4-ca65c581088c | -18.58889 | -48.14817 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9779e1-9d20-36f0-9ab4-e4cb04b16c86 | -18.4143 | -49.35989 | 2025-09-16 04:53:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71f7d1a1-663f-35ab-a14f-acd54742eb46 | -21.92372 | -48.24525 | 2025-09-16 04:53:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0781777a-0f29-3443-93a2-7e2418f21131 | -19.84105 | -46.45557 | 2025-09-16 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e47a6d0-84ab-3042-8729-4973de2e7b53 | -20.20722 | -45.37096 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ba9370a2-62e8-3816-879e-f2d205c9ebd8 | -20.60592 | -50.14352 | 2025-09-16 04:53:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3a83f231-aa26-361d-ba99-8fe292adaae2 | -21.22488 | -46.94901 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74cdac0d-4d62-3366-90aa-da2d0d754ef7 | -19.84173 | -46.44914 | 2025-09-16 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c37bf65-f1c5-3051-a8d6-1c31141b8f04 | -18.90686 | -49.57867 | 2025-09-16 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d3f8a0e-9e77-3719-ba1a-afdc006713d8 | -21.21851 | -46.94542 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b11c037b-3ba3-36e2-9867-22ec326f5727 | -18.13929 | -51.79531 | 2025-09-16 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aae1f1ff-12bb-3d80-8fb7-cd62f8790f70 | -21.94104 | -46.57619 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2a774895-fb3b-36e8-9c37-3bf77e8fe4fa | -18.60974 | -48.20801 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 22999f17-0d49-3b75-96a5-ae43653ed6fa | -20.2019 | -45.36682 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41cf73b8-d303-3c5f-b4de-2ce66700c565 | -19.84696 | -46.44991 | 2025-09-16 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86bd1595-83a6-39b3-8b76-fc13a0773bd7 | -21.22306 | -46.95179 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ede58c18-41a5-3036-8f1a-95ab5c56f215 | -21.94137 | -46.57288 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d691e51-c5de-3fc0-83a2-0e55af250dcf | -21.22372 | -46.94566 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71f21ee7-954b-30ba-91c6-1013e48d5bb5 | -21.22029 | -46.94266 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79f94610-11fc-39cc-a970-bc1a09d2a59b | -18.77571 | -47.63554 | 2025-09-16 04:53:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 934a7f8c-5399-3411-abea-65a72ba064c7 | -20.34648 | -48.78629 | 2025-09-16 04:53:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c54c5117-9f97-3751-9219-3695d22c39ad | -18.5843 | -48.14739 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb3a02a8-348e-3f81-b215-9c68b7737844 | -20.86536 | -46.21362 | 2025-09-16 04:53:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c69bc576-276c-3e20-bb89-99ed4bfe14ea | -21.21968 | -46.9488 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c894e654-4df1-3f6b-b816-09481ec7292c | -20.86005 | -46.21225 | 2025-09-16 04:53:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 740dd19a-2c97-32cb-a01e-8425f5e31e68 | -21.27057 | -47.01294 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d7f174d-2d66-3f82-9d85-5d507d11b2b3 | -20.60642 | -50.13947 | 2025-09-16 04:53:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 04840dfc-ab1b-346a-b2d8-ee8850ac76f6 | -21.93571 | -46.57557 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ca2ba650-9208-3aef-947b-6a97e42a6d79 | -18.90262 | -49.57824 | 2025-09-16 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77d7412b-bb62-3b23-aa9e-cc04a8d39f02 | -21.77011 | -45.48099 | 2025-09-16 04:53:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c8634e8-aca3-3f23-baab-4f57a0d66700 | -21.21998 | -46.94576 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83a1baaf-64fc-382c-ae4e-619ce01049ab | -22.08758 | -46.65833 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47030f7f-1a0f-3a73-b9ca-556f3fd3a3b3 | -19.85563 | -49.08278 | 2025-09-16 04:53:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6240bc72-a5a9-33af-8a98-d3423de4511a | -20.55539 | -46.37503 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99f27838-8e64-3e6f-8638-1d4b317ebd3a | -21.93603 | -46.57224 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9edaed27-d7de-3973-92c1-619f650c76d3 | -20.86191 | -46.21569 | 2025-09-16 04:53:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79929b59-30f8-360e-9eb6-c37bab7f2874 | -21.58426 | -46.80486 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfbc1e7a-3c63-3abf-87dc-116d70927177 | -21.22519 | -46.9459 | 2025-09-16 04:53:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c4670fa-586d-3dab-b674-e296ea685663 | -20.5606 | -46.37676 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f6af0f7-75f6-3c3f-9124-b2eae83493b4 | -18.58953 | -48.14281 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178bcd29-f276-3032-a8ed-7a04f253745a | -19.15722 | -48.72778 | 2025-09-16 04:53:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c276f779-cb09-37d7-a557-a598d0813c67 | -21.19556 | -44.3727 | 2025-09-16 04:53:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ddc127b6-ddbd-3913-a05e-c27d9049590d | -18.55564 | -49.26212 | 2025-09-16 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02df3021-ca6d-3ca3-aca4-38ade4b68e8b | -22.08224 | -46.65785 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8a277955-8d4c-33d2-af0b-cc0fdf37e021 | -18.57909 | -48.15182 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc86aeb6-5607-3fb8-9df7-6386789333c3 | -18.61433 | -48.20862 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0631686c-b351-38fd-af47-b26ee3d67ba6 | -19.258 | -51.43046 | 2025-09-16 04:53:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7793cd4b-10c9-3ef4-8594-f81350d07762 | -20.20758 | -45.36715 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 94e45f63-415f-3661-88fc-bdd3ceba9aab | -18.6144 | -48.20613 | 2025-09-16 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7aae351-cb74-3c88-bf13-2ee126f9675d | -18.55669 | -49.25375 | 2025-09-16 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |


[Clique aqui para ver as próximas entradas](README81.md)
