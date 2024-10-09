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

## Dados Diários - Página 231

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b095a310-71a4-3500-bbd4-1ec80d3f6df2 | -18.92123 | -41.02424 | 2024-10-09 12:04:00 | TERRA_M-T | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c0e622c6-894b-370a-8813-17c5ab54ea8c | -18.92286 | -41.0137 | 2024-10-09 12:04:00 | TERRA_M-T | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 8c2efd0a-b5b2-3409-a7e7-b3b5bd5dabcf | -18.98926 | -39.9737 | 2024-10-09 12:04:00 | TERRA_M-T | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 7309ba25-1a6d-3917-9cf0-7ccafb47a6b1 | -19.32858 | -40.87802 | 2024-10-09 12:04:00 | TERRA_M-T | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 5c769788-6dc9-3a3b-871d-890bf54ba8ed | -19.5768 | -40.17436 | 2024-10-09 12:04:00 | TERRA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 06173fbd-2b19-36b9-b7e7-b705e12a6425 | -19.65967 | -46.20728 | 2024-10-09 12:04:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| cff99084-552d-3b94-ba5d-cdbe952ae6c2 | -19.72971 | -42.20728 | 2024-10-09 12:04:00 | TERRA_M-T | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 4cc9c333-275b-3667-a959-c3589d29edf3 | -19.75666 | -45.97545 | 2024-10-09 12:04:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 921d5e8d-3d6c-3247-8e08-c2fe4c52eba0 | -19.7571 | -45.96083 | 2024-10-09 12:04:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5ae051a8-a3d8-38e7-8d7f-547756d45adf | -19.76027 | -45.95542 | 2024-10-09 12:04:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| e22f3a83-3930-3e07-a7e2-dba00c06ce3a | -19.83752 | -42.36277 | 2024-10-09 12:04:00 | TERRA_M-T | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 98e6be4c-2913-38aa-b36d-78983eff44b5 | -19.87538 | -40.6357 | 2024-10-09 12:04:00 | TERRA_M-T | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 2c518402-888f-302c-b259-ff40470c5b91 | -19.96822 | -42.44526 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 67de6999-f9f3-3837-92c5-133c0c049327 | -19.97028 | -42.43254 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 173dac5c-d5f2-3b4d-9dc0-416c5d66401b | -19.98035 | -42.43432 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 0b4db5c0-fc65-30f6-9cc1-7af6d7a9141a | -19.98232 | -42.42215 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.1 |
| 3b058713-41fe-3ab3-885a-f7e591ec1bf0 | -20.00052 | -42.43225 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| dd948df8-37ca-3c4c-8919-339c1d6a10a2 | -20.01056 | -42.43417 | 2024-10-09 12:04:00 | TERRA_M-T | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| ed879cd1-742d-3d9d-8d3a-6786103136ae | -20.04101 | -42.18839 | 2024-10-09 12:04:00 | TERRA_M-T | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 4c79c75c-4c47-318c-8846-9c4f46710b07 | -20.111 | -44.21097 | 2024-10-09 12:04:00 | TERRA_M-T | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 392ca93a-e034-38e4-b531-2cd33a947b2c | -20.27794 | -41.35885 | 2024-10-09 12:04:00 | TERRA_M-T | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 720af1c4-935f-323a-a6d8-85b5c6caf8cc | -20.40841 | -43.89838 | 2024-10-09 12:04:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| c35a09c8-9b12-38f0-98b2-36fa5623af13 | -20.63443 | -45.93505 | 2024-10-09 12:04:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c5104aaa-b794-3ba9-9da3-795b581ff3a9 | -20.63852 | -45.91281 | 2024-10-09 12:04:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 117c1243-486f-3482-beb6-67f2a6a5d255 | -20.64256 | -45.89082 | 2024-10-09 12:04:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| bd471336-4ca9-3321-89d3-9f7760730107 | -20.65242 | -41.2664 | 2024-10-09 12:04:00 | TERRA_M-T | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| f2e0730f-5806-3b19-bb28-b8585ca15e78 | -20.8711 | -42.75478 | 2024-10-09 12:04:00 | TERRA_M-T | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| bb4bffe2-c626-3400-8195-db70a3d841af | -21.05404 | -47.25003 | 2024-10-09 12:04:00 | TERRA_M-T | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a9c5b1ff-3871-3ce5-a686-746dbfa11d6b | -21.10843 | -44.98536 | 2024-10-09 12:04:00 | TERRA_M-T | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 56bab6a7-7cd2-375e-a90b-19fa6afa04fe | -21.11149 | -44.96802 | 2024-10-09 12:04:00 | TERRA_M-T | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.5 |
| 6161479c-a996-32b5-b96d-20750f6ac669 | -21.21521 | -44.2413 | 2024-10-09 12:04:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| b094e945-818b-37e1-bcd5-3e8691d855e8 | -21.20406 | -44.23924 | 2024-10-09 12:04:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 2163b00c-f23d-3ed5-9a2e-07775e50770b | -21.81861 | -44.94834 | 2024-10-09 12:04:00 | TERRA_M-T | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 0c3203f3-c384-3384-81d1-ac765b234f1c | -21.52602 | -45.54205 | 2024-10-09 12:04:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 323a7335-bc8f-3359-abef-73f26ee86f67 | -21.20675 | -44.22386 | 2024-10-09 12:04:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.0 |
| 2ffe5c17-4cdd-3ecb-b842-7856862dc9a1 | -13.94 | -44.53 | 2024-10-09 12:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4272ceda-6dfc-3d40-b898-fa5db731282e | -8.33 | -44.11 | 2024-10-09 12:04:36 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3d3ea3-1f26-3b8a-ab7d-7ab16e2d0cd4 | -6.7798 | -60.0552 | 2024-10-09 12:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 34c1121e-2458-3827-8b54-ef5d0903112c | -6.7614 | -60.0559 | 2024-10-09 12:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cfa3c399-846f-39d8-8c1b-67e108fb91f4 | -10.5746 | -48.0178 | 2024-10-09 12:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3c13afcf-07c1-364f-b4c4-1db4b34fa55e | -11.3235 | -51.3202 | 2024-10-09 12:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ddc4b378-9ed0-33b0-960b-c16f01b2ef27 | -12.9919 | -46.2359 | 2024-10-09 12:06:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bb7c6cc9-f46c-37c7-bb57-8c846b3fe355 | -13.3786 | -61.9582 | 2024-10-09 12:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 189f5a87-2828-3aa0-a509-1508f4d9359d | -13.398 | -61.9182 | 2024-10-09 12:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8746ac74-3325-3d47-93b6-eceb65c50027 | -13.3978 | -61.9376 | 2024-10-09 12:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e5456b27-e272-3344-ae13-02ba2a42cc70 | -13.9353 | -44.5046 | 2024-10-09 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 410.2 |
| 09f3392d-cadc-366b-968b-38f95435988f | -13.9348 | -44.5282 | 2024-10-09 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 200.3 |
| cef3ccab-a90c-3e10-8165-23bf805fc24d | -13.9543 | -44.5247 | 2024-10-09 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 72294493-a81e-344e-a3e8-c757319f7242 | -14.0971 | -51.1134 | 2024-10-09 12:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5f411382-3f59-3cfe-9385-8a2179015c20 | -14.0778 | -51.116 | 2024-10-09 12:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.8 |
| c1dc8e2a-c86a-3cae-9dcf-0b04fa482bec | -14.0975 | -51.0918 | 2024-10-09 12:06:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 95bdbf55-127e-3aef-a59a-09cb9af37473 | -15.7076 | -59.3726 | 2024-10-09 12:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| ef27cc3d-ce9d-3124-bddb-ee9b109cb1f0 | -17.1467 | -56.8463 | 2024-10-09 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.4 |
| d7f2dff2-fce5-3622-b6e5-6dd28b71aa86 | -17.1471 | -56.8256 | 2024-10-09 12:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.4 |
| f549de5c-d5d7-3a02-9f7f-dc9b4dcd3671 | -6.7798 | -60.0552 | 2024-10-09 12:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| e5d42acb-ef9b-3294-baa5-032438090fe5 | -6.7799 | -60.036 | 2024-10-09 12:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0dad5c71-a977-342b-b451-5a4b1cb5769a | -6.7614 | -60.0559 | 2024-10-09 12:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 139a62a2-eaeb-31a9-8ceb-66f0d282d2bb | -10.5746 | -48.0178 | 2024-10-09 12:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 1f00b6a4-df2e-31f0-b6c6-da870a80dff0 | -11.3235 | -51.3202 | 2024-10-09 12:16:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 10e466fe-1cf3-3c0f-bcfb-c860ba0ea0b3 | -11.992 | -51.0553 | 2024-10-09 12:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 4a363c23-fa8a-3abc-bbfd-7c01271e3969 | -12.011 | -51.0531 | 2024-10-09 12:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| c21a0e55-87fb-3191-b852-a310b99391fd | -12.1086 | -50.8926 | 2024-10-09 12:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 068b46f7-eb70-358c-bb69-b0e25c0e6fd0 | -13.3786 | -61.9582 | 2024-10-09 12:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1d4fd0d6-430c-3b31-a4f9-2b15f59024ec | -13.3976 | -61.957 | 2024-10-09 12:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c35ce750-3e03-3257-8ca0-d64de2a18fc0 | -13.398 | -61.9182 | 2024-10-09 12:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 26eb4af9-a273-31b3-ab22-77da53d6354f | -13.3978 | -61.9376 | 2024-10-09 12:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6f15d75f-caca-370e-baab-acfe561dfb8f | -13.9153 | -44.5317 | 2024-10-09 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ead7b884-5f19-30b9-9856-7b2621b44e42 | -13.9158 | -44.5081 | 2024-10-09 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 72520226-788a-3321-8352-2e3ec0e34de4 | -13.8963 | -44.5116 | 2024-10-09 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 20cad49b-8682-3aa3-a44a-6cd59d9ce7e5 | -13.8958 | -44.5351 | 2024-10-09 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c80d0432-586e-35b3-b1e1-1df59f8c17b5 | -13.9543 | -44.5247 | 2024-10-09 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| db194a34-2103-3902-b358-2e964dcebc36 | -14.0778 | -51.116 | 2024-10-09 12:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c4c0490b-0a74-30c1-a906-ea2bcbc6b27b | -15.7076 | -59.3726 | 2024-10-09 12:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 09689d7a-3a0a-3a2c-af98-e75cdd34fa47 | -15.688 | -59.3945 | 2024-10-09 12:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a7cf56a1-b541-3872-b2f8-b7c821f654e0 | -15.6882 | -59.3745 | 2024-10-09 12:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| ba28dd05-6c0a-3151-b9ea-d8968145153e | -17.1271 | -56.8486 | 2024-10-09 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| fe2c0169-00b5-3683-9944-d7bf3fa25001 | -17.1467 | -56.8463 | 2024-10-09 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.9 |
| e8680b07-64dc-380b-9d27-fcef9945fbcf | -17.1471 | -56.8256 | 2024-10-09 12:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 184.7 |
| c1c14ad2-bf73-3ec6-a130-af602f8b5bf7 | -6.7614 | -60.0559 | 2024-10-09 12:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| ed5a7b4e-4fdf-3d6a-b27d-19d436451d5e | -6.7799 | -60.036 | 2024-10-09 12:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| ad9bdc0f-05a5-31e0-a321-4947a97d54b0 | -6.7798 | -60.0552 | 2024-10-09 12:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 262.4 |
| ebbe1296-7583-3dbc-95dc-41a53dbf0690 | -10.5746 | -48.0178 | 2024-10-09 12:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 0254f5bd-f823-346f-b6bc-f4a05276812d | -11.992 | -51.0553 | 2024-10-09 12:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 5470c3ab-4de5-3972-9248-8de357173b77 | -12.011 | -51.0531 | 2024-10-09 12:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 399f7ce9-d1b6-3a48-a852-d66e5e13a89a | -11.9923 | -51.034 | 2024-10-09 12:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 4142f3c6-7100-3afb-bcae-6c70d6cd49b6 | -12.1086 | -50.8926 | 2024-10-09 12:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3aab1c87-73a4-3afa-8911-df8b18b1a750 | -13.3978 | -61.9376 | 2024-10-09 12:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ebaa77c1-dd7a-3ee9-8ccf-c54e8870f429 | -13.398 | -61.9182 | 2024-10-09 12:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 07807301-f289-341b-bb7f-591143d8e4dd | -13.3976 | -61.957 | 2024-10-09 12:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 20916978-1d08-38d3-a8ec-565f4b45b3c1 | -13.8369 | -44.5691 | 2024-10-09 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| db19de74-45c7-3dc0-a04e-d975750d7ce5 | -13.8769 | -44.515 | 2024-10-09 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 43265a95-bbec-354f-bf4d-b266e902a132 | -13.8364 | -44.5927 | 2024-10-09 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 96d1f37a-998e-3608-8e6e-dc87f640c8f9 | -13.8963 | -44.5116 | 2024-10-09 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 9df70816-8ba5-38f6-ad7e-2745eeba6599 | -13.8764 | -44.5386 | 2024-10-09 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 234c1bd1-fd6b-3cba-800c-40f66782c5c4 | -14.0778 | -51.116 | 2024-10-09 12:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3509ff09-b1e9-3086-ab2b-6af9dfe2996b | -14.0971 | -51.1134 | 2024-10-09 12:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 904c4af0-9bae-3f88-892c-db45415092d9 | -15.6686 | -59.3963 | 2024-10-09 12:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 91456f3f-ba15-3041-9453-8a6948e39652 | -15.688 | -59.3945 | 2024-10-09 12:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| ae22ee27-347a-3112-8ec8-de2831a9c1fb | -15.7076 | -59.3726 | 2024-10-09 12:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 6f58f941-e4ac-3c63-8520-68ec9fd4f0b5 | -15.7073 | -59.3926 | 2024-10-09 12:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |


[Clique aqui para ver as próximas entradas](README232.md)
