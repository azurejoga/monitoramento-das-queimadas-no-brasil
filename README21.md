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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ab9abd7-5157-3b55-a1d8-37f441f87840 | -9.3493 | -63.5846 | 2024-10-15 02:45:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a21943b8-e4bc-3276-bac3-c1de3eb49eb6 | -10.3711 | -61.1935 | 2024-10-15 02:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 1aefdbfb-a44b-3964-840a-b81fa0646031 | -10.841 | -49.2539 | 2024-10-15 02:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cbf22883-f9b8-306f-a817-876c14e04285 | -11.6915 | -65.2432 | 2024-10-15 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cf56a98a-a5a7-3cd0-bdc3-27fec36eb24f | -11.6917 | -65.2243 | 2024-10-15 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6e327194-a93b-368e-8506-d0290f3704c3 | -12.099 | -50.2728 | 2024-10-15 02:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| aeeb4770-062e-3562-933e-a51f21af5b2d | -12.0994 | -50.2512 | 2024-10-15 02:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7021f45c-7d55-3456-ad9f-cb3d61a40e01 | -12.1181 | -50.2705 | 2024-10-15 02:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7b4bb8e2-42a4-30ef-a2bc-417aa5e48a4a | -12.515 | -63.263 | 2024-10-15 02:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 266f0c9f-4684-3450-ba9e-cc7ba7f91e38 | -12.9728 | -62.7951 | 2024-10-15 02:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 091c97ef-d5aa-3730-a261-1caeae44987f | -13.9075 | -45.8355 | 2024-10-15 02:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cfd542c2-e5ed-3232-952d-925af4542566 | 1.0199 | -52.2162 | 2024-10-15 02:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 37168f0b-8e6a-3a4e-a2c6-0c4af4c2e599 | 1.0016 | -52.2164 | 2024-10-15 02:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ebdcebd1-39fc-3851-b907-ee7cbc8be411 | -3.1099 | -54.2263 | 2024-10-15 02:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| cefeda79-4ec9-3872-b439-f12984b0ec80 | -3.1283 | -54.2259 | 2024-10-15 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2566394f-59fd-3101-87fa-aa020765d07b | -10.0816 | -44.2133 | 2024-10-15 02:56:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e3eab66c-6cc2-3843-b6cd-e8166883596e | -10.3711 | -61.1935 | 2024-10-15 02:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 089cec37-ad4c-37f2-8389-fe5db8a3f42f | -10.3713 | -61.1743 | 2024-10-15 02:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 74732805-e2a8-3dd7-9d34-49ea49cbb054 | -10.822 | -49.256 | 2024-10-15 02:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0747b7e9-d3b1-30ef-a078-a8a0b33d8fba | -11.6915 | -65.2432 | 2024-10-15 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1c23f1db-3153-3331-822b-f31347abd8e1 | -11.6917 | -65.2243 | 2024-10-15 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f1fd5837-9fa6-3d1e-8bf8-c1f75d4d26d7 | -12.099 | -50.2728 | 2024-10-15 02:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 5d405daa-4f7c-3406-b4a3-248f22f0afce | -12.0994 | -50.2512 | 2024-10-15 02:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d510a4e2-5b2b-3e87-955c-a80a466ef1bd | -12.1181 | -50.2705 | 2024-10-15 02:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d8bdb9f2-ed67-3e61-928f-d1f79b1bb52e | -12.1185 | -50.2489 | 2024-10-15 02:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 93579286-ff02-32ad-a92b-26f7000c37a7 | -12.515 | -63.263 | 2024-10-15 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| aa80f7bd-eed6-3648-87bc-dcb3655bf659 | -13.9075 | -45.8355 | 2024-10-15 02:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8921cde0-0fe5-38a7-ad32-de79f43eb928 | -17.8648 | -57.4171 | 2024-10-15 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 592acc8a-db66-3083-88d6-9412382b0315 | -17.8447 | -57.4401 | 2024-10-15 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 7ab9dacf-2b39-3a1f-b45b-99de41000825 | -17.845 | -57.4195 | 2024-10-15 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 556bdf45-aef0-3416-a6bb-03d88ff90033 | -17.8644 | -57.4377 | 2024-10-15 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 769f7648-83ec-356c-9d43-bc87508f4acb | 1.0016 | -52.2164 | 2024-10-15 03:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1263ef7c-db96-3f05-beb6-b35241206de8 | -3.1099 | -54.2263 | 2024-10-15 03:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f2ccd201-4744-3187-8713-709d6dffa9d0 | -3.1283 | -54.2259 | 2024-10-15 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c1ea42c2-fd84-3c05-9d68-ce626e178be3 | -3.1282 | -54.2459 | 2024-10-15 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 89a350fc-f887-36aa-96b3-52f553c86189 | -3.9396 | -46.4229 | 2024-10-15 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f71b98e3-8b34-33e1-aed5-8cccee28a8e8 | -10.3713 | -61.1743 | 2024-10-15 03:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3801d0e5-9fe8-36d9-930d-a0c9169fb948 | -10.3711 | -61.1935 | 2024-10-15 03:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 8012ca5b-3545-3b80-9266-00021cbe2c6e | -10.3524 | -61.1946 | 2024-10-15 03:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 15107fae-7285-3cae-b8d0-47bdc6edcff8 | -11.6917 | -65.2243 | 2024-10-15 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6938def5-ab28-3513-a0c7-64366c3f90b3 | -11.6915 | -65.2432 | 2024-10-15 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 3c5edb68-744d-376b-9975-3b63e1659b5e | -12.0994 | -50.2512 | 2024-10-15 03:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ca15b0e6-160c-35a1-9646-a67dc809ecc3 | -12.099 | -50.2728 | 2024-10-15 03:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9239eca1-cff0-3b02-b084-e76b9f680f1a | -12.515 | -63.263 | 2024-10-15 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 1cc537f1-585f-3b36-b038-615b73be5a97 | -13.1475 | -62.3215 | 2024-10-15 03:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8d327f06-a53b-313c-8a89-4cdbf720cf9e | -13.9274 | -45.8091 | 2024-10-15 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a66cdfd3-607f-3ef0-9a79-ba81810333e7 | -13.9269 | -45.8323 | 2024-10-15 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4c5c3f44-5f83-3ca8-ba78-4363ad4f54be | -13.9079 | -45.8124 | 2024-10-15 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 519deed4-66af-3372-a769-0f172291d010 | -13.9075 | -45.8355 | 2024-10-15 03:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f1f2ce2d-6fd9-30d7-a387-0155357ff10a | -9.37377 | -40.42098 | 2024-10-15 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a4151649-6f46-39ff-b87b-3110e3457f87 | -8.23781 | -40.2933 | 2024-10-15 03:10:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6887a632-8308-33ff-b8f8-fc8d341898c4 | -7.92468 | -35.24726 | 2024-10-15 03:10:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 71cfdacd-1a4a-3917-bbef-de29b3a63648 | -7.92375 | -35.25254 | 2024-10-15 03:10:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| bf5a1692-e2ce-3faf-9fae-3de876857332 | -7.15203 | -39.3145 | 2024-10-15 03:10:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84492a04-230f-3bec-b8f4-557f8a7322bb | -6.39644 | -39.91268 | 2024-10-15 03:10:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a6b221a-40b5-317a-baa6-ee40a71d19a8 | -6.39535 | -39.9185 | 2024-10-15 03:10:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0704725-6681-30cc-80b8-d0d27c5cee89 | -19.64512 | -40.47911 | 2024-10-15 03:13:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 27cba502-891a-3e97-8f92-1944b008df61 | -19.64432 | -40.48286 | 2024-10-15 03:13:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62c69c04-1835-3b75-a9c7-4d1a522b5e64 | -19.64041 | -40.47453 | 2024-10-15 03:13:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 154e0ff6-c0ec-31d3-bdca-9d2481f467a9 | -19.6397 | -40.47784 | 2024-10-15 03:13:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1c0b5d6-491d-3122-b403-95406601b46d | -19.63893 | -40.48143 | 2024-10-15 03:13:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4347f3ab-158c-35b1-932f-34824bde0120 | -19.22003 | -40.14003 | 2024-10-15 03:13:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 778878c8-ee3c-340e-a4f6-e96250646009 | -19.21926 | -40.1436 | 2024-10-15 03:13:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d393870c-feea-3b1b-a6b5-10dba502d047 | -16.18129 | -43.86598 | 2024-10-15 03:13:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b3c5b98-f9d1-3ece-84af-7444c5560b7d | -16.17746 | -43.86355 | 2024-10-15 03:13:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5ebe156-dd2b-3181-a258-002eaa1bad24 | -16.17598 | -43.87 | 2024-10-15 03:13:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f02d820-8caf-3a54-82d1-667bc2cbcb8b | -16.17428 | -43.86433 | 2024-10-15 03:13:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e592d26-a246-3302-a50f-e360b6222887 | 1.0016 | -52.2164 | 2024-10-15 03:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0536a90c-9375-3908-90c6-e41e273154f9 | -19.70928 | -44.06142 | 2024-10-15 03:15:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c6254e-14f5-3489-aa2e-79ef930a0489 | -3.1099 | -54.2263 | 2024-10-15 03:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a056a835-80f6-3cd5-b0e7-af2fae583a44 | -3.1282 | -54.2459 | 2024-10-15 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 8766a186-1281-3f5a-a855-de1bff90241b | -3.1283 | -54.2259 | 2024-10-15 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 79f122c6-1d33-329e-ab03-1952ca4031b9 | -3.9265 | -42.4246 | 2024-10-15 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| c75cb715-cbad-38b5-bb34-274c190b1f04 | -3.9267 | -42.401 | 2024-10-15 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| d7b6b607-4607-3d2d-a704-844df8a993c0 | -9.4556 | -44.1763 | 2024-10-15 03:15:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c9df4ebe-2476-3b31-a120-bb34c3f34a18 | -9.4366 | -64.5795 | 2024-10-15 03:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 40a8ac73-5d50-306e-99b2-5d4d7c6e911e | -10.3524 | -61.1946 | 2024-10-15 03:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 82bd3941-9e33-3513-8d5a-6ea7df61cb83 | -10.3711 | -61.1935 | 2024-10-15 03:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 97b84d22-1bb9-38f2-8780-bd4201343817 | -10.3713 | -61.1743 | 2024-10-15 03:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c06b8eb9-ef83-32a5-bfbc-8b28e644e7c5 | -11.6915 | -65.2432 | 2024-10-15 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4ecb53c4-c3e6-313c-9551-8edc4d2bf1f3 | -11.6917 | -65.2243 | 2024-10-15 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 90c6da61-d023-3669-b621-56b2d6c9fb8e | -12.515 | -63.263 | 2024-10-15 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d268d9b6-f832-386a-a629-afeee6d2a5d1 | -13.1285 | -62.3227 | 2024-10-15 03:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| da153224-4b62-3c29-a975-8a54bb1792c3 | -13.1287 | -62.3034 | 2024-10-15 03:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1777eae4-8e6c-3cc9-940f-1b1c0c9badd3 | -13.1473 | -62.3408 | 2024-10-15 03:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2d02206d-1a46-3dd0-8efa-71b66c240d6b | -13.1475 | -62.3215 | 2024-10-15 03:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e0a4e011-a76d-3562-9629-f07df0bb3b83 | -13.9075 | -45.8355 | 2024-10-15 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c974e1de-24c6-326c-aa77-76ef2eaf5804 | -13.9079 | -45.8124 | 2024-10-15 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3b8a1a5b-12f7-3883-8ce0-d5d725de931d | -13.9269 | -45.8323 | 2024-10-15 03:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 47987c6d-f755-3307-aa87-c90fcd5f4534 | -17.8644 | -57.4377 | 2024-10-15 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| ac1710bb-f1dc-3f44-a4f6-5d888b040e0c | -17.8842 | -57.4352 | 2024-10-15 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| ab7934a9-39c7-34a6-b26c-a6b4d7e1709c | 1.0199 | -52.2162 | 2024-10-15 03:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2a069cdf-9fa8-360c-957a-c8bb7aba2f67 | 1.0016 | -52.2164 | 2024-10-15 03:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 97d2a539-63a6-3070-a24e-b63bbb081f15 | -3.1283 | -54.2259 | 2024-10-15 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7f80a5d9-7cc4-3ca1-b583-8d8cbaad0450 | -3.9265 | -42.4246 | 2024-10-15 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 5dcdddeb-98c0-35ec-bf46-929088adf16d | -3.9267 | -42.401 | 2024-10-15 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| c1e9124c-46d3-3a1d-974b-4dd78f7d8be7 | -4.5334 | -46.5927 | 2024-10-15 03:25:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| acaad732-bb48-3616-b30a-68c4f6bf36dd | -4.5336 | -46.5706 | 2024-10-15 03:25:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| fbab6534-73fe-3d88-9c3e-d159222a7e71 | -9.4556 | -44.1763 | 2024-10-15 03:25:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| fbc4e9af-ef77-38b5-b6fd-58fad2242312 | -10.3711 | -61.1935 | 2024-10-15 03:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 164.9 |


[Clique aqui para ver as próximas entradas](README22.md)
