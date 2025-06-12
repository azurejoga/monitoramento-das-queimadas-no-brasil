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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c6cb22-47e9-330e-a795-56881c580b65 | -15.37896 | -47.88546 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dd1b2a4-794c-36c3-a47c-f5c995136f69 | -18.38015 | -44.50859 | 2025-06-12 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43fb4843-f270-31b8-b131-f7fcb6e04c6c | -20.44987 | -46.40566 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 446f3219-4d00-317f-80fa-937a2b50007c | -13.97015 | -54.42452 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0ad1f24-8534-3417-afd6-f5930804f02f | -19.93141 | -44.00674 | 2025-06-12 04:04:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 636b558f-af40-318b-ab7b-669268e3cda3 | -13.53027 | -47.86214 | 2025-06-12 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76aa2de4-df6a-3beb-b64a-b2481a270498 | -20.43501 | -46.40673 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ec74d64-24bc-3c87-83cc-632c1f43f584 | -16.37731 | -46.87545 | 2025-06-12 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 875d6d08-fd61-38a5-a46d-60d6d4805664 | -14.17093 | -45.49348 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bc6afe7-080a-33ad-a571-30a5cf579264 | -12.21055 | -49.63826 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65c68ad2-93ef-3c68-82ef-3b48233eebbf | -14.18079 | -45.49789 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ffd43b8-b1dc-33eb-87a2-4019430cfc29 | -13.89746 | -54.64042 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 14edc31e-9dd8-3fec-97e8-aadb5ef36c54 | -15.2907 | -47.15982 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb8bb036-c085-30ad-9ec5-5fe7f7e4d1fe | -19.43806 | -44.33924 | 2025-06-12 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7535885d-d5bb-354a-ae41-82aaa86db5a9 | -15.57076 | -47.85651 | 2025-06-12 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b8b6df-66f5-3869-aea3-1b764acbc40a | -15.93003 | -42.90833 | 2025-06-12 04:04:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e3bfffe-757a-37a1-b738-d18761e398b6 | -18.38353 | -44.50919 | 2025-06-12 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c962cd06-6317-3e4c-9404-dc67c4397dcb | -13.90038 | -54.65884 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42cf0d53-8028-3202-bedc-33dd8ae7dc1f | -19.50975 | -45.07532 | 2025-06-12 04:04:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 190cf966-a105-35c6-8993-c0ad296cbcfd | -14.02915 | -55.1324 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 076ba538-9bdb-3024-82ce-2a4844a52404 | -16.78724 | -49.11756 | 2025-06-12 04:04:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929d9279-7501-3f79-a31c-ed06085109f3 | -12.13377 | -54.66037 | 2025-06-12 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f9c6cf-a558-3c35-adf6-105e9af93f03 | -13.89093 | -54.63899 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 122b3005-0326-379d-af02-4192be230ace | -14.17789 | -45.49276 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 497e5e68-06bb-30d3-be0b-845e53c0cb83 | -15.37901 | -47.87757 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff1b719e-806e-3a24-a757-f74e34f49f58 | -13.89821 | -48.7382 | 2025-06-12 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 343001cf-0b50-3ce9-9d91-8219b8e0e526 | -14.1926 | -45.49537 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86a244aa-909f-3e2e-b6f6-750da0445296 | -13.88719 | -54.65656 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 252eecea-87f9-3e35-b6fc-b933b2bcca28 | -13.89624 | -54.64615 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0a7644f8-fbab-3649-aa37-11a1f3c26350 | -13.5431 | -44.14514 | 2025-06-12 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f12d6d98-8175-3229-8e46-f19189238eae | -15.0809 | -48.94436 | 2025-06-12 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f5899f4-f61d-31f2-b48f-8dcdaa59dc4d | -13.65872 | -53.9404 | 2025-06-12 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ac2704a-4012-3cf1-8b8d-a16c43ce0b4d | -12.83216 | -47.37881 | 2025-06-12 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6eafd10a-d05c-3b39-81fe-381294550d46 | -15.15902 | -47.46518 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ea49fa5-bdac-3730-8c7f-43124046459c | -13.64844 | -53.94042 | 2025-06-12 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c45531dc-cbe8-35be-a87c-66dd34f54568 | -17.28822 | -42.67076 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0224df6c-d423-309c-98ce-676c3d165f0a | -14.03294 | -55.12799 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bbc4fb65-da6f-30e7-8966-1cbe9b325b53 | -13.65477 | -53.9416 | 2025-06-12 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38f67a6c-33c3-34e7-a927-83fec1934b81 | -17.28991 | -42.65999 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45b3649-800c-3fb4-83a4-0921822b0428 | -14.17343 | -45.49659 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be823ff9-7fde-3312-b114-9450eec4adaa | -12.20941 | -49.62344 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb7a6a2f-ed67-3db3-8f73-8d2e126b8fea | -12.21323 | -49.63018 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e918705-f9b3-37e2-97ef-a8a8921daa43 | -12.82725 | -47.38199 | 2025-06-12 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4f0ac17-f728-31de-b125-fcb5c8a51fb0 | -12.21162 | -49.63244 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| af04ad9a-77e6-34f6-87f6-d6db92f86763 | -20.44137 | -46.41238 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dde1e19d-fb78-3f88-8810-752519a367be | -13.89377 | -48.73694 | 2025-06-12 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db1fdd58-9d05-35a7-815f-c3d7649e5e0e | -14.17711 | -45.49724 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81f1457-0e25-31bf-b80e-ee7534720ae1 | -13.52598 | -47.86133 | 2025-06-12 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 992b6c50-4e3e-3247-b214-fab10b49b44e | -19.57813 | -49.10684 | 2025-06-12 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0b3466b-e549-3c67-b17a-0f7d0d2407f5 | -14.0383 | -55.13549 | 2025-06-12 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae12874d-d845-3dc2-b1a3-d569f5077bdc | -19.99685 | -43.98002 | 2025-06-12 04:04:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d843e9d-839a-3596-95b0-a114470ba63e | -20.00005 | -46.4401 | 2025-06-12 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7dacac1-6490-3dd5-aa30-dbf698c03e1f | -19.08327 | -53.46507 | 2025-06-12 04:04:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0098a92c-024f-351f-8b1d-ab597aeeae67 | -15.07878 | -48.94305 | 2025-06-12 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6bf17d8-cb13-3c8e-a672-54555b8c1f52 | -15.38723 | -47.88725 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0357b9e6-9ef1-35d6-b4df-cbb67bcc1c4a | -19.8819 | -44.76508 | 2025-06-12 04:04:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c893ab0a-abc6-3ed7-a9b6-9282337df6cd | -17.29208 | -42.66773 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2981fb9a-66a7-30c7-9fbf-1f35c141a8eb | -17.28605 | -42.66302 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1e52abd7-8931-36e6-ab93-3e1fa386120f | -17.29264 | -42.66415 | 2025-06-12 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dce31907-5de1-3c1d-a72b-1f6e5df21a95 | -12.82376 | -47.37719 | 2025-06-12 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c9122be-dd96-3ac9-9f64-e4119b981bf8 | -13.97654 | -54.42616 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a655e24-8cad-3dc9-824b-333f280b1374 | -13.90077 | -54.65124 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca256e23-18f6-3bb4-8fe7-bf7e927c088c | -11.8703 | -52.2522 | 2025-06-12 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ddd881e-9710-30a4-a57f-3def5da0cb6a | -13.56835 | -44.27283 | 2025-06-12 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab24640-dfb1-30ab-abfb-e66cb2ff3a62 | -19.6844 | -46.46657 | 2025-06-12 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed0f2ebb-9660-394c-aa59-54a8e385af12 | -14.18369 | -45.50302 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f153c428-0654-34c4-8679-ae5f4d1962e9 | -15.92665 | -43.98293 | 2025-06-12 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f70a8a6-a21b-30f5-a4c2-9a7438a27d15 | -13.89952 | -54.65696 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19712e39-76a8-32ab-8b99-17c4042b2244 | -19.85181 | -43.84469 | 2025-06-12 04:04:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 748651aa-ad9d-34c7-8fec-145b5ed2947a | -20.4343 | -46.41084 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99c9f88d-b746-3e31-8eff-76f12568582a | -12.82305 | -47.38118 | 2025-06-12 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a400cc49-0f28-3d4f-a0df-93342c281826 | -14.18892 | -45.49472 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6da3908-b619-34ac-91fe-264dca9c22ba | -14.82564 | -54.65871 | 2025-06-12 04:04:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7db4ec1b-0e27-39c9-a8b2-1310655ad119 | -13.90161 | -54.65303 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 678bfbdd-00c6-32d3-b68d-664f122e7d34 | -14.64046 | -42.71259 | 2025-06-12 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f67b84b-1f5f-3a40-a1bf-7d27fc78999b | -15.36999 | -47.87988 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 36b824d3-e42b-377a-ac69-02af37a0edb4 | -15.38241 | -47.88258 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef967724-bafe-3fa2-8d0f-88060a6af374 | -20.43784 | -46.41155 | 2025-06-12 04:04:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 160e912c-8dee-353c-b15f-0365524ea724 | -15.67381 | -47.5874 | 2025-06-12 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06ed6b53-cf28-3abd-8aaf-d9376e264a77 | -11.769 | -54.3777 | 2025-06-12 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c9a0591-b81e-3ded-9d32-46ee2db163fd | -16.78741 | -49.11565 | 2025-06-12 04:04:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 689855e5-2be9-388b-821f-b9f7bd13c8e4 | -11.77686 | -54.37335 | 2025-06-12 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c00fef8-4b34-3149-bef2-7dc41a124a79 | -12.82796 | -47.37801 | 2025-06-12 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c5b65da-581c-3ad4-8042-6b424b458bff | -15.38309 | -47.88636 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 173eaf67-e2e0-356c-b325-efe7febbd8d3 | -12.21211 | -49.63596 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b0261c3-8049-3c1c-adf1-d1cbe4b17d3a | -15.38387 | -47.88222 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30aa7eb0-5f77-3a70-bd29-6f14010ef869 | -17.91792 | -46.69814 | 2025-06-12 04:04:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1652a795-ed23-31ad-874e-c903b2b06848 | -15.37635 | -47.8764 | 2025-06-12 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a867b8a-6090-3368-82fa-e4b08b48643d | -13.89503 | -54.65186 | 2025-06-12 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c83ec736-f8bd-3ba5-8ed4-0bc9914f9969 | -19.83904 | -40.08229 | 2025-06-12 04:04:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16935931-bed0-39a3-b3d8-c6358f4bd1cb | -14.18525 | -45.49407 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe851ffa-d276-3756-a0ca-b90bf3ed59fd | -14.17168 | -45.48899 | 2025-06-12 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db11df1b-8f14-3725-afa2-7f83f652f21a | -13.37171 | -44.1012 | 2025-06-12 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 340d0441-a1b2-3e0c-b81c-d9f52ac5a47a | -13.66106 | -53.94296 | 2025-06-12 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d97eaac9-7886-3d16-a722-205f4b715ac1 | -15.09846 | -47.31262 | 2025-06-12 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d40a56e9-8936-3e5d-9b28-39ac6044e0a7 | -20.7335 | -56.65958 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47ccd05d-64f8-3449-a58d-7838d9da1511 | -20.73342 | -56.65867 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 53eba5e1-e027-3b20-9c8a-a2ce30d28f2b | -22.77312 | -49.31749 | 2025-06-12 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1d748df-2754-3696-af60-07b183ca1ce2 | -23.23645 | -51.28505 | 2025-06-12 04:06:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8a49afd7-577a-3d19-8e46-b7197315ac7c | -20.73458 | -56.655 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README10.md)
