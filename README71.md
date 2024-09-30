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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a2c587f-525f-3c90-8930-5f9a0145c6cf | -19.13543 | -57.47312 | 2024-09-30 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dd803477-439b-3777-8498-43ea8295a232 | -19.12691 | -57.50769 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a7f12012-0f97-34bb-ad63-ff28afeaea21 | -19.1265 | -57.511 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 213a6218-931a-3dd9-bdaf-0985130f1f04 | -19.12227 | -57.51047 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 11308085-83b7-33c8-bcc4-98c35af7fa28 | -19.15231 | -57.47574 | 2024-09-30 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7670a2a5-4956-3e24-b7e7-7ec2c8366119 | -19.11428 | -57.50568 | 2024-09-30 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ea1b903d-6841-33c2-941a-51c67380fbac | -28.51283 | -50.66511 | 2024-09-30 05:29:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b5df1c80-879e-3e84-967c-9f4711d9cf46 | -28.51249 | -50.67268 | 2024-09-30 05:29:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 099547e6-f696-36c1-a57b-fa082d6576a7 | -11.15 | -45.74 | 2024-09-30 06:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4617168-77f9-3537-8753-2c986e1f4984 | -11.15 | -45.79 | 2024-09-30 06:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c12efffa-26c2-39d6-89e3-6ca840552072 | -11.12 | -45.74 | 2024-09-30 06:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b96032e-6902-3cab-9ce7-4f107db08b3a | -11.12 | -45.78 | 2024-09-30 06:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8c7307b-d8da-3775-b55d-c783943a97d2 | -9.98746 | -67.56889 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c63b067-04a0-3240-a99f-00590fbb18cc | -9.98684 | -67.57327 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86c48830-6484-3926-a386-4ec096ce27da | -9.549 | -68.59922 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 340b36e2-8d17-3706-a086-e6226ae07eb7 | -9.54441 | -68.60233 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4d8e72e-1755-344d-91a4-ba1fb91153d8 | -9.54033 | -68.60176 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2db31fcd-0481-3d2a-aeb9-a24044954296 | -9.53982 | -68.60543 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcc91f7b-f204-3903-9c10-606c44781809 | -9.53574 | -68.60484 | 2024-09-30 06:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7381de8d-d7db-3689-9984-8c7350e015e6 | -10.60869 | -69.50647 | 2024-09-30 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bc3e853-42d0-3291-8d54-224e48e4986f | -10.40102 | -69.22702 | 2024-09-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1da8275-144b-39a4-a775-a3024c54f04b | -10.39948 | -69.22849 | 2024-09-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59bf958-c558-3b0b-b2fa-c2f387fa46d2 | -10.11353 | -67.88913 | 2024-09-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ec2a965-0f13-3a6a-bfb9-a44c4e14f532 | -10.10921 | -67.88853 | 2024-09-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a22ac19-bdb5-3720-ab7e-1c3acdf794fe | -16.77 | -55.86 | 2024-09-30 11:03:50 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5622289-36c6-3ed0-8680-62882b7b2699 | -11.15 | -45.65 | 2024-09-30 11:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d958cb49-4d12-35ba-9028-c024b72e33ae | -11.15 | -45.74 | 2024-09-30 11:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe2cb98f-2ef0-3498-8428-8aedf74e234c | -11.12 | -45.64 | 2024-09-30 11:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3e8ccf-29d8-3923-a02a-1c24df9c5122 | -20.17 | -47.83 | 2024-09-30 12:03:28 | MSG-03 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1fdd150-dbbf-335b-a778-72741b738cea | -18.88 | -49.17 | 2024-09-30 12:03:36 | MSG-03 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9792327-9f91-3500-8665-20944b0ed8cf | -13.22 | -46.33 | 2024-09-30 12:04:07 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45f3710a-fde7-358d-9405-d275a42751ba | -13.19 | -46.32 | 2024-09-30 12:04:07 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7be16265-bd90-37eb-9c6e-1f55a3aef8b3 | -11.15 | -45.69 | 2024-09-30 12:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e56b54be-28cc-384e-bc5d-ae48499daf07 | -11.21 | -45.71 | 2024-09-30 12:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8a72bb0-7711-321d-baac-835662bb59e6 | -11.12 | -45.64 | 2024-09-30 12:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd1a12d4-4180-3f23-bead-cce18db35f8e | -11.12 | -45.69 | 2024-09-30 12:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4488c3-339d-37fa-afd3-b3fd241adb9a | -11.15 | -45.65 | 2024-09-30 12:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34d32cba-55ea-382a-865d-342a556609a2 | -5.1728 | -37.95978 | 2024-09-30 12:32:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 31.0 |
| fd6efab1-3ce9-3b45-91fc-741ba86c9581 | -5.17053 | -37.97707 | 2024-09-30 12:32:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| ede9d368-150f-3f0d-af4f-6dd677dfa08b | -5.16608 | -37.96994 | 2024-09-30 12:32:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 1238e226-741e-31e3-90b0-7df71d395646 | -5.45706 | -39.0925 | 2024-09-30 12:32:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| cef992fa-020c-3660-b7d0-a3f89dd378eb | -4.34223 | -41.50948 | 2024-09-30 12:32:00 | TERRA_M-T | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 499fda9d-7a3b-388c-aa2a-731afc4c2398 | -3.33147 | -42.51849 | 2024-09-30 12:32:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1b46c50a-33db-3a31-8ced-f5c147428c25 | -3.26499 | -42.72714 | 2024-09-30 12:32:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 454e49c4-1972-3439-a1b7-8970952b6827 | -3.78484 | -42.31868 | 2024-09-30 12:32:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f798b9a5-6f44-305a-9a1c-bff510d82822 | -3.78354 | -42.32774 | 2024-09-30 12:32:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 223c5d13-52e1-30e8-b105-83f76e07ad3c | -4.91075 | -42.69456 | 2024-09-30 12:32:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 01bcb4fa-3001-3bef-8ced-050666ef2ade | -4.90945 | -42.70359 | 2024-09-30 12:32:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3aa742a5-402f-3bd2-b31c-eebde638efec | -5.70297 | -43.14456 | 2024-09-30 12:32:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 0c8be3bc-4612-37f2-b12b-3f428644c794 | -7.91313 | -42.76319 | 2024-09-30 12:32:00 | TERRA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 4c01cf47-d29f-3a3c-8ef9-17b957327147 | -7.84999 | -43.08049 | 2024-09-30 12:32:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7fe87f18-bf0e-3b61-a441-1e3535a94512 | -7.84868 | -43.08965 | 2024-09-30 12:32:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 4e0c35e8-dc02-381c-a42e-8150ea9cb97f | -7.28616 | -42.24709 | 2024-09-30 12:32:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 4fb1b0e9-622f-37c4-9584-b405ba45b9dc | -7.2848 | -42.25679 | 2024-09-30 12:32:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 3e3d1744-cda4-3d69-9b56-af1fa9c12079 | -7.04246 | -43.38009 | 2024-09-30 12:32:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a1e55326-0944-3f0a-958c-60f45fd65d2c | -7.29189 | -43.37855 | 2024-09-30 12:32:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b53f5ce2-ab21-3459-91a6-c52dac463b14 | -8.17375 | -43.65653 | 2024-09-30 12:32:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e1f87624-5ebc-3355-a7db-93683d302918 | -8.17247 | -43.66552 | 2024-09-30 12:32:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1a252be9-b489-3d5a-8f58-c9f9b3ec59fb | -8.16484 | -43.65527 | 2024-09-30 12:32:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 17f66283-25b7-3aea-9ee2-77f2e91b7589 | -2.9021 | -43.70901 | 2024-09-30 12:32:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6d5f00e9-cf15-3710-b4fa-8a39ebbb154d | -6.39615 | -44.78546 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ea96eadd-6271-3f65-b2f7-bbbaa7ac26d6 | -6.38852 | -44.77515 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 2c6ccc60-1e22-39c6-b469-24ab463103c2 | -6.3872 | -44.78418 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ac823f51-923b-3a41-b0ec-89e7e67dfe58 | -6.01247 | -44.51264 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7c539aba-5049-3d90-92fc-3b897eb92986 | -6.00222 | -44.52039 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2d4c6d76-bc2b-388b-aaca-36316282311f | -7.82694 | -44.20774 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 51e4787c-9cbc-31f3-b3a4-f20f8728e962 | -7.81808 | -44.20648 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8e1035a0-82eb-3767-ac61-52c1d0228650 | -7.59689 | -45.02711 | 2024-09-30 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a7db86a6-18c1-3de5-b060-b959ac6f5aed | -7.59213 | -43.85622 | 2024-09-30 12:32:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1df88509-5872-3d64-beac-ffbb7f139e45 | -7.56875 | -45.02623 | 2024-09-30 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 761b73d6-8c18-3415-b648-0e9e0583408f | -7.49367 | -44.97201 | 2024-09-30 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56e55d0f-9d80-30b1-b822-3521e7494c8d | -7.48229 | -43.8527 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a3b594c9-116f-325a-8251-e29ad8e77236 | -7.48101 | -43.8616 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 095b2871-b8bb-3da1-8d71-f7f3049cf97e | -7.45999 | -44.2574 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 3cf022ba-99f5-32a2-b828-e12c4cad5dca | -7.4587 | -44.26628 | 2024-09-30 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d6410342-f13f-37cb-9b44-8ba27a037540 | -7.27775 | -43.99263 | 2024-09-30 12:32:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 56323d88-fb00-3cc6-9cb3-f13fa55ff18e | -7.25044 | -44.99867 | 2024-09-30 12:32:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 61acfb49-e8ed-3ca5-9dba-0575e45ef5d2 | -7.2491 | -45.00777 | 2024-09-30 12:32:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a15d3b72-2475-3db2-bc47-3911a5e9327d | -7.24148 | -44.99737 | 2024-09-30 12:32:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8842e547-f805-3730-97a1-4dbee43b897e | -6.6993 | -44.72804 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d4ddc081-cf61-365b-b0d2-d6496fcac278 | -6.69799 | -44.73705 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 6e1f74a4-eb75-353c-b50f-b43ab3bcc68a | -6.68906 | -44.73575 | 2024-09-30 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 95b88f18-d482-3890-bb0e-a9c806f4d392 | -8.82336 | -45.21179 | 2024-09-30 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7112ac5e-70d9-3f80-b0b3-63a04ab3ca59 | -8.8207 | -45.22994 | 2024-09-30 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0f62bb3d-3b19-3dc7-8053-62b7b3e49206 | -8.77596 | -45.2235 | 2024-09-30 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c374914b-bfb3-381f-846f-525c2824da68 | -8.77462 | -45.23257 | 2024-09-30 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 66490805-554b-3641-a6b3-de9ca2bc591e | -8.52748 | -44.71223 | 2024-09-30 12:32:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3b15f1a5-bbca-3854-b542-9153f560a275 | -8.52618 | -44.72117 | 2024-09-30 12:32:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bbf55919-2225-3bbc-815b-8541793e2792 | -8.5186 | -44.71096 | 2024-09-30 12:32:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ee4874ee-fbfc-3a61-a4ac-74c610b7a075 | -8.07601 | -44.01062 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f58d30aa-9120-359b-925b-eafb84ce54dc | -8.07473 | -44.01953 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3b962427-660e-3fa5-a6ed-0a6971a03ffc | -8.07344 | -44.02843 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2a13e864-9525-3ca4-9e3a-d5e5d4023f0a | -8.07216 | -44.03733 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ad2d9601-a964-3e8e-91fc-bb28098950b0 | -8.06084 | -43.9903 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3e049316-61f7-37b6-9a1f-d8db8e9bb089 | -8.05956 | -43.9992 | 2024-09-30 12:32:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ec22bfb3-a42f-3065-ac8d-e520ea81927a | -7.819 | -45.51984 | 2024-09-30 12:32:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fedee83f-fd1d-3dfd-b5a0-78a6aefc5fa9 | -7.02647 | -45.32907 | 2024-09-30 12:32:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ef1790a4-e819-38aa-86a3-8673c1af0865 | -8.81976 | -46.77718 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f23e6bf1-1d70-3778-ba50-753d7aef28b7 | -8.8182 | -46.78742 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 23463503-6a38-338c-bee9-785a66b23134 | -8.81664 | -46.79768 | 2024-09-30 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README72.md)
