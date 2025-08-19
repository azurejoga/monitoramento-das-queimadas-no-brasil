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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c0e00aa-8d07-3d63-b3d5-25d254c95097 | -13.38418 | -44.30873 | 2025-08-19 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584bf114-88e4-376d-b328-cb4b4be8c628 | -14.17128 | -45.3088 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff338c91-4e18-3d8d-b9c7-8084143f58ee | -14.16913 | -45.31976 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61b93ae2-32f4-3722-9ae1-f903cafd4089 | -16.71363 | -47.62452 | 2025-08-19 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c589cb-bf8a-3b24-8dc0-891f85381a07 | -16.7174 | -47.62847 | 2025-08-19 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2c7f25d-6b63-369f-a0c4-6f1c502c7514 | -12.91304 | -46.1095 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 422bc51e-e51d-3faa-9085-208fd99728cb | -13.00113 | -45.202 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ef52ccf-1247-3d96-821c-648a462be961 | -16.71037 | -47.63202 | 2025-08-19 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a20ce7c-d79d-3e17-892e-659b97721b51 | -15.80276 | -48.27316 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c91672c-9d75-3d7b-a733-c58dd1e85de7 | -14.87258 | -48.05551 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 280ad1e9-dbf6-3c12-9914-2f1f5a157975 | -14.86402 | -48.06417 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7245b839-066c-36a3-bbbb-bf5acb122bb1 | -12.99276 | -45.19024 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f3a7b14-b8b9-3ef1-8b27-97e66a0eef29 | -15.79801 | -48.27488 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7f6f6fd-f094-3cc8-bc3a-6d949a41f0b5 | -12.64763 | -45.82161 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c63bb14-ca0d-334e-b909-65018f6c3988 | -16.48947 | -45.105 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e1805cd-7bb6-3ce9-865f-79579758712b | -12.65498 | -45.81474 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86b21b4-f013-32d9-84cb-679651d55433 | -13.62182 | -46.89001 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a24f038c-03be-322a-915c-a4665a7b2ef3 | -17.39502 | -46.70719 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c755fb93-901b-33e0-aeea-88e742f684bf | -15.80169 | -48.27812 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0be3aa9d-387f-31f2-9ba7-6bc0edd3fda3 | -16.47361 | -45.09676 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a587178-779b-308d-ad3e-dfc65d6a5af5 | -14.86924 | -48.07068 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0245ae0e-18ba-35ec-95fc-343b3cda6c42 | -13.47188 | -47.06492 | 2025-08-19 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 322fdd9b-b100-3343-b94a-a0cde8a4e4bd | -16.57101 | -40.66892 | 2025-08-19 03:38:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1cf28db7-959c-3b3d-8d06-087fc05020a4 | -14.84378 | -48.05843 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb6043e-b44f-3db1-8f70-f78613b08b38 | -14.9809 | -54.8158 | 2025-08-19 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3a83b0e4-553e-3d21-b212-30f8147c315f | -6.9524 | -43.6083 | 2025-08-19 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 3a998656-744c-35dd-bfe0-df5befa8d345 | -14.9812 | -54.7951 | 2025-08-19 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 5395f9ed-c902-3a74-a590-b63002a6c446 | -6.9339 | -43.5868 | 2025-08-19 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 6d6a0a42-69ed-3e4a-8fd0-bf66f653246e | -6.9527 | -43.585 | 2025-08-19 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 18d04c10-8052-3d7a-9165-82d8bc9be406 | -6.9715 | -43.5833 | 2025-08-19 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 82dfebdb-fb93-38f1-8735-fb6d8c5fded3 | -5.7887 | -43.6134 | 2025-08-19 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b4ef60e6-2b12-3ca8-8e80-ee4df059534f | -6.9712 | -43.6066 | 2025-08-19 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 22153efc-cbd6-3762-8b53-406d64b047ca | -15.0389 | -54.8089 | 2025-08-19 03:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7e712fc8-2a14-3eaf-896b-4fcd951f0039 | -15.0386 | -54.8297 | 2025-08-19 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 31af3df1-7a70-3aaf-bffe-c954490a703a | -20.02514 | -45.64287 | 2025-08-19 03:40:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b28c812-4122-3948-add5-bd6410c6d833 | -20.85978 | -46.36589 | 2025-08-19 03:40:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e8fdec3-f0ef-3fa0-91d7-245a4650face | -21.88991 | -48.18937 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d97df4e-f4bf-35e7-8c7a-0ef8d9675ccc | -22.89777 | -45.38773 | 2025-08-19 03:40:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4949006c-88eb-30ab-bb8c-8d666adb9f91 | -21.87311 | -48.21146 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70fe0093-b25a-397f-b8dc-6de270540fd0 | -20.32985 | -51.7156 | 2025-08-19 03:40:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99cf7f40-9ce3-305d-9003-9d428753ea40 | -20.03012 | -45.644 | 2025-08-19 03:40:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cb5cfbd-68c6-373e-9f2c-a751c8c05cc7 | -21.87401 | -48.2075 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ea47ba-c6f2-3ac0-8d91-23cfdcf61bdb | -23.18121 | -52.00737 | 2025-08-19 03:40:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 88eb367d-fcd1-3fa5-8419-939d5954374a | -23.11624 | -45.27417 | 2025-08-19 03:40:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ec2d252-6399-371e-a2b6-01a41469032e | -23.1852 | -52.01424 | 2025-08-19 03:40:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4b3ef5e4-a4b9-3145-8dff-24ce61aca50a | -21.04781 | -43.318 | 2025-08-19 03:40:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41735b7b-ffb9-3d12-bcd6-3e5ecb9cd905 | -21.39015 | -48.10255 | 2025-08-19 03:40:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97e40fc4-62da-3cf5-ad6e-a69154aa626e | -21.23696 | -49.08614 | 2025-08-19 03:40:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a100603c-a31a-3aae-a69c-4aca66b1da83 | -21.39239 | -48.10911 | 2025-08-19 03:40:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64cf1823-0dac-3a8c-a776-2c933ad525b9 | -22.88097 | -47.48849 | 2025-08-19 03:40:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22d1f8ba-2bc2-330e-8678-0578485f141b | -21.0382 | -44.75091 | 2025-08-19 03:40:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 38e3360f-5951-33d2-95b7-5698d4817128 | -21.39812 | -45.00594 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| d6fd168d-223a-358a-a730-b74ad587c883 | -21.39012 | -48.57864 | 2025-08-19 03:40:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31190c5e-9630-3298-ac95-d79769ed996c | -21.40115 | -45.00515 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| a83d7278-ca14-3031-b1e5-543e47d8ebe1 | -23.18678 | -52.00799 | 2025-08-19 03:40:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 14985784-ac5d-3c81-9543-2e4fb41de1e9 | -20.33164 | -51.70848 | 2025-08-19 03:40:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 845266ef-eaeb-3ff5-8132-a9f53d9ee5d9 | -19.93637 | -45.06528 | 2025-08-19 03:40:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2512da32-f625-3aa7-8578-3d9c0bebeee2 | -25.03847 | -52.68084 | 2025-08-19 03:40:00 | NOAA-20 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 734b28e7-a666-3384-8359-54d777b4822b | -21.39547 | -45.00916 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 19ee9217-ae72-37f0-98d2-ca645416f3b9 | -23.18618 | -52.01596 | 2025-08-19 03:40:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d5238b72-8b98-3b0b-a8bf-fa3360745d6c | -21.40273 | -45.00718 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7dcced90-8d65-3b31-8c45-a0c72d7ee3e9 | -21.39332 | -48.10492 | 2025-08-19 03:40:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d67e4f18-c726-3cbc-9806-6631d2d518c4 | -22.797 | -46.35357 | 2025-08-19 03:40:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 686bbb14-52ef-30cc-9bfb-a35d0f2b1409 | -19.29217 | -48.43713 | 2025-08-19 03:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0040ecd-293c-35e5-8de6-9c5540c18dbf | -20.50085 | -46.38725 | 2025-08-19 03:40:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 606d1c24-7897-3f3a-b50a-107717a18212 | -21.38209 | -45.76615 | 2025-08-19 03:40:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 96edc04a-1bc7-32bc-ade0-226f991dbd2c | -23.1152 | -45.27909 | 2025-08-19 03:40:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57f0680c-7b7f-366c-82a9-d82832b5dd1d | -20.42315 | -43.69954 | 2025-08-19 03:40:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15c5e866-ca22-39dd-a130-7136de61374c | -21.37726 | -45.76481 | 2025-08-19 03:40:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2db21925-6976-3a30-bff1-e5b0e9edccdb | -21.39653 | -45.00391 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| c54c4e85-599d-35e3-b08d-dc57634bda0c | -21.12904 | -47.03852 | 2025-08-19 03:40:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85448655-351f-32f5-8bfb-53513274aab7 | -23.11064 | -45.278 | 2025-08-19 03:40:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 16da10dc-4eca-31df-bfee-e64cdf34e14f | -25.04032 | -52.67381 | 2025-08-19 03:40:00 | NOAA-20 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 24c1ad29-a6c7-321e-bb87-2e708b47e55a | -19.29324 | -48.4324 | 2025-08-19 03:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4683c6-a5c6-38e3-9628-a67ac58bd05d | -21.87585 | -48.19935 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 989d95d7-51bc-3c69-9850-cde7a13f709a | -21.64301 | -49.75581 | 2025-08-19 03:40:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0354aed5-f362-304e-aa1f-fc2802bd662a | -20.49635 | -46.38297 | 2025-08-19 03:40:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e9652c3-b35a-30d3-a287-b6889ee9c1be | -21.39702 | -45.01117 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 0672b506-a2e1-3819-8b82-82730bfb7e67 | -21.88338 | -48.19218 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7db12c44-679a-331c-92d5-4cdcf9faff91 | -23.11166 | -45.27313 | 2025-08-19 03:40:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4aaffc12-7470-3a1c-a73a-8e59d35ca179 | -21.88907 | -48.19309 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7fa1aaa7-01e4-3039-a067-ecdf5bd2bed7 | -21.23093 | -49.08493 | 2025-08-19 03:40:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6f166ed8-228d-3587-a790-4ca458c63053 | -21.40008 | -45.01044 | 2025-08-19 03:40:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 87a81a4f-b66b-38e5-b4da-650236a5c7b8 | -23.18779 | -52.00973 | 2025-08-19 03:40:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d005df0f-e212-3fa6-ae6f-0d25dba79624 | -21.87491 | -48.2035 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbdedfb-93eb-3054-ac88-c4ce97f86ecf | -21.39682 | -48.57594 | 2025-08-19 03:40:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2763c147-fe44-3f91-af60-6482c4664057 | -20.76919 | -43.46806 | 2025-08-19 03:40:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d312aff-1413-3d1b-a049-66167e7e699a | -22.88016 | -47.49212 | 2025-08-19 03:40:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bfae0708-33ad-3076-a2ed-76b7219dcbb3 | -21.87678 | -48.19523 | 2025-08-19 03:40:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1237846-cb35-3ca1-a9b1-e09dbc367a8e | -6.9336 | -43.6101 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b1288d7c-7cc9-32d7-9a2f-01ce8c605dba | -15.0389 | -54.8089 | 2025-08-19 03:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a301cb87-390b-321c-a5c9-e60658214089 | -6.9527 | -43.585 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 97977ca2-aecd-3b7a-9219-70500322aeba | -6.9524 | -43.6083 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 1c9fc08e-aafa-33df-9ca4-bd883da28ca5 | -6.9339 | -43.5868 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 606f9c1c-93e4-3d57-8e9b-70ce70b67960 | -6.9715 | -43.5833 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| b3fb0b54-a967-3f39-b910-eed0ecaaf834 | -6.9712 | -43.6066 | 2025-08-19 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4969cbaf-93db-3838-afba-4ba0166baf95 | -6.9524 | -43.6083 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0a572610-3577-37c6-b27a-a96a3c4d12c0 | -6.9336 | -43.6101 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 43b5c29c-2b5e-3251-9c63-2ee5347c1903 | -6.9715 | -43.5833 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 1a153be0-dc73-3dc8-a9c7-eff9318638da | -13.1555 | -54.9357 | 2025-08-19 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |


[Clique aqui para ver as próximas entradas](README19.md)
