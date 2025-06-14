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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 106d29b6-08e0-3612-949c-252d1aa27eed | -10.64616 | -44.48329 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 364510df-7ec4-3e83-b441-c112c25711cf | -6.6006 | -43.902 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6b441262-40bf-3d36-a390-ef76f254e45c | -8.07924 | -43.11034 | 2025-06-14 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 59165324-6938-352e-8743-0d0886a84447 | -6.96091 | -42.8103 | 2025-06-14 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3c66ef92-38c1-3d16-8c60-95ac67b08b69 | -5.90031 | -43.45957 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be5d35df-050b-3253-90ef-6471b2c9876f | -16.19431 | -46.4673 | 2025-06-14 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 10d51a12-ebeb-3446-ba88-48f5d840321b | -17.97928 | -44.26402 | 2025-06-14 03:25:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45834866-e325-3b58-a192-7a03636a9c19 | -17.58162 | -47.49038 | 2025-06-14 03:25:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f45c12fe-cabf-334a-acef-443d537df212 | -16.1962 | -46.46581 | 2025-06-14 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 148eaf29-a92d-32af-8a20-6ab4e79bd45b | -17.5826 | -47.49424 | 2025-06-14 03:25:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d9fa6c2-dfa3-311d-8815-b968edc3a2d0 | -16.19476 | -46.47211 | 2025-06-14 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 3291bac3-56fe-3fbd-939a-42a082b2a57a | -17.9852 | -44.2646 | 2025-06-14 03:25:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c115286a-f493-35be-a98f-2dfe7389713e | -14.99574 | -41.91744 | 2025-06-14 03:25:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faa495b3-3568-328a-ab3f-1212994b0e41 | -16.19292 | -46.47357 | 2025-06-14 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 527c2ac3-89c9-38f6-b6ed-f95ac6692cba | -17.58006 | -47.49693 | 2025-06-14 03:25:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 544c0dcb-b4a0-3359-9b8d-ec500315db1d | -12.76692 | -44.41328 | 2025-06-14 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97f76f37-0668-395c-ab7c-177b35851fe9 | -19.52382 | -46.08871 | 2025-06-14 03:28:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70de3a1e-4c51-387d-afc7-26720523bf3e | -19.68355 | -43.9273 | 2025-06-14 03:28:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aab175e-81f5-3c12-8e95-38550608c976 | -19.52071 | -46.09015 | 2025-06-14 03:28:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 719710aa-3ce0-3e3b-8965-6746fd1056a8 | -22.67649 | -42.85778 | 2025-06-14 03:28:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2c64880c-01cf-3d5d-9c1d-529efb980ec9 | -19.52268 | -46.0937 | 2025-06-14 03:28:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17af25dc-4282-3fbb-b36e-8a1267d36185 | -19.92422 | -43.90424 | 2025-06-14 03:28:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89c7ec71-fcc0-3eef-b6ef-7ea23dcd1ded | -22.50527 | -44.56794 | 2025-06-14 03:28:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ddf722f8-1293-39f1-993a-81fd2b9de288 | -22.9004 | -43.75301 | 2025-06-14 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 71f36b4a-b38f-3c0e-a233-f6ec8570c0c5 | -6.9602 | -42.9052 | 2025-06-14 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 9dc979d2-23ec-383c-a5d9-6503de3d058b | -13.9062 | -54.6084 | 2025-06-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 0391ce32-c77c-32a3-8ea1-3f249e13f7bb | -10.9355 | -56.8322 | 2025-06-14 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c9cc578a-459a-3720-b412-eaab347e08eb | -6.9414 | -42.907 | 2025-06-14 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| e654e012-6a82-3a44-a12c-55ddbd5c4ac4 | -16.1967 | -46.4589 | 2025-06-14 03:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 34b43545-ff82-34ce-9777-5829f75c5367 | -6.9416 | -42.8834 | 2025-06-14 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 96528bca-614e-3500-a9c7-c28b8446c277 | -14.2121 | -57.4098 | 2025-06-14 03:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b666627a-77a5-3567-a71a-b8dc26c3f7c5 | -10.9353 | -56.8522 | 2025-06-14 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6de40714-5574-3d9b-8311-afb97ac2ad37 | -13.887 | -54.6106 | 2025-06-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c44d0006-1f73-3c5c-8613-80099f1df16d | -6.9605 | -42.8816 | 2025-06-14 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 45e1637e-3780-3d5d-9280-168e0ffc753c | -29.72592 | -51.12165 | 2025-06-14 03:30:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 1311713b-ce0e-3715-9f90-3fa7e589a950 | -16.1967 | -46.4589 | 2025-06-14 03:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 42dde4d7-32c7-3092-8a2d-a9a5e9dfb898 | -13.9062 | -54.6084 | 2025-06-14 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a384a77d-aeda-3e8e-81f6-d94fdef3c804 | -6.9602 | -42.9052 | 2025-06-14 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| a3010599-1da9-3237-a116-097823b8bd88 | -13.887 | -54.6106 | 2025-06-14 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d34ae4ee-220e-3c46-ad4d-787b26678471 | -6.9416 | -42.8834 | 2025-06-14 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| abcbbaef-4820-3b1a-90db-3d1e6d4c96d5 | -10.9355 | -56.8322 | 2025-06-14 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bbefb7d2-4056-31f1-9997-2379c8258c70 | -10.9353 | -56.8522 | 2025-06-14 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b441a5a3-3c67-35c6-8316-23c6bfe397d1 | -14.2121 | -57.4098 | 2025-06-14 03:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9196b577-4dae-3d6f-a42f-0646d8363417 | -6.9414 | -42.907 | 2025-06-14 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 57c655a1-b0cc-33bc-b8e2-7e6a03937e5d | -6.9605 | -42.8816 | 2025-06-14 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| eb0b41b7-181f-3d8a-be94-7e72dda132a2 | -6.67973 | -43.76091 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| daaeeace-0719-3ca4-b622-faccedcef8eb | -6.95625 | -42.81049 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 78ad8fa4-9dba-3f6a-b905-4e94156e4b2d | -8.55838 | -50.07912 | 2025-06-14 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6580df68-bb16-3d5d-9743-eb89bf8dcf4f | -6.21027 | -43.33249 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e5c7027-af76-3bb7-825f-f33415f7ccb2 | -6.55625 | -42.41151 | 2025-06-14 03:49:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfc1cbb1-832f-32cb-9faf-e3c4f2549c52 | -6.94879 | -42.89171 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 818f3346-f446-3d6d-8d03-81aaafb3037c | -6.60494 | -43.89589 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| af77ba46-6785-3114-aa7b-508a9f52e8d0 | -8.56467 | -47.04762 | 2025-06-14 03:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62c45e52-76cf-348b-8daf-23754601e595 | -7.23513 | -43.5854 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20f12e14-4275-35b1-835d-e467a9e05c39 | -8.07062 | -43.11512 | 2025-06-14 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 731347b6-607a-3bff-bc76-8f4fe36a38af | -7.22213 | -43.10853 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 77e27f80-df5b-345f-9ae2-95e2fa628d78 | -7.00927 | -43.53637 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6129d7-9675-34ee-bf3f-4783fb822210 | -7.21234 | -43.10815 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6ac9cd56-050f-3947-8822-1e5a5dd0ba3d | -5.12212 | -37.78963 | 2025-06-14 03:49:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7ab1428-6e57-3f31-ac3f-9ca933c16066 | -7.19043 | -43.55024 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aad142bc-bbf8-39f7-958e-9c34d7049779 | -7.22607 | -43.10617 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac78436e-90f1-323d-ba27-02ffb847f650 | -4.60932 | -38.52991 | 2025-06-14 03:49:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c6f1187-500b-3d25-ac4c-df47bf813ee7 | -5.77678 | -43.47669 | 2025-06-14 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 691ec44c-ef8b-3727-b16a-95b2b03fec07 | -6.9538 | -42.88834 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| d0404b72-f4a7-3744-a2b3-3abdbf7ae39e | -6.60033 | -43.89501 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff99ab83-6d1c-3219-9bcb-9dca58cbc090 | -6.21106 | -43.32797 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c15559b2-70d0-373d-82b7-986a0fc45b5e | -7.23064 | -43.58465 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74cdce96-95ae-3d23-ae86-2f6f06fe1739 | -7.41015 | -36.69892 | 2025-06-14 03:49:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c4d1af20-2069-34d6-ad94-00e2b2073d81 | -5.78009 | -43.62197 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8cbdd5d-9770-3729-bf79-5d5bce48d1a1 | -7.24093 | -43.10326 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 271d2c2a-420d-3143-b1f9-eed5785859ae | -7.23659 | -43.10249 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae3d9361-b3e2-3e86-bedb-c6eb1a3a386d | -8.56501 | -50.08062 | 2025-06-14 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbf938e5-fc8d-3b9c-8d55-0579d619161c | -6.21553 | -43.3288 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d606911d-702b-3dce-9410-e7c0ab1a2243 | -8.0749 | -43.11589 | 2025-06-14 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 1ca89c1b-a186-3512-b9a8-a3cb2217341d | -7.23613 | -43.09943 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1cda14e5-7343-31a4-88fc-d09efff45783 | -7.17037 | -43.53315 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| edad9040-1bec-3643-863b-6ed8e7ea1e79 | -6.60411 | -43.90071 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9fbbceae-db22-39af-a16f-a2badd57028c | -7.07158 | -43.5588 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af1855ba-1715-3c88-8589-77bc68c78c09 | -7.46192 | -45.50496 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe898753-7ed0-3e3a-b97a-80cc8e0b24b2 | -6.94737 | -42.89991 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 30a0892e-fbd3-37eb-bced-c32443fe9bcd | -7.46351 | -45.50891 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e6f107a-7558-304d-85ac-9280f9f3bcf7 | -7.45736 | -45.50115 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 568f7b8c-a32d-39a6-b20e-13a71106583d | -7.45629 | -45.50704 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4d40e63-b8ea-3f00-96ac-d5c9fa2606ea | -6.9592 | -42.80643 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 144fb76a-b3e1-3e7c-8c23-56f22ae6aeac | -7.22615 | -43.58389 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6b226b13-6c72-38e7-9f6d-a940d9b87a00 | -8.39496 | -46.92784 | 2025-06-14 03:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 679b9b5b-99d4-3b65-8a50-4a662e8a4a39 | -7.47592 | -37.41554 | 2025-06-14 03:49:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a20c4d4-4f69-3119-8ab8-b530b25d3512 | -6.94779 | -42.88793 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5be9d55c-8b7e-3ed5-8933-07e4961fb038 | -7.45575 | -45.51001 | 2025-06-14 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50f967a3-b578-3031-a554-bac56f6cada8 | -6.21361 | -43.33097 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6b1e2329-67b3-3705-8a69-0949110da426 | -7.11017 | -43.44222 | 2025-06-14 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44255c70-ed69-39a9-9c88-9293c871e257 | -6.96053 | -42.8112 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9a0fffbc-7560-33e3-9017-230ab6d96dd8 | -6.9495 | -42.88764 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b10da873-c0a6-3cb7-8fe8-77bb42cb249a | -7.21669 | -43.10888 | 2025-06-14 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4acef803-f8d3-372c-89e2-f41ea5965161 | -7.63838 | -43.67141 | 2025-06-14 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad60b88b-514d-3486-ae73-a4519b3f3b7b | -8.64458 | -39.59953 | 2025-06-14 03:49:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80e82e61-46e0-38f2-aa4e-01d5cf2cfaec | -6.95851 | -42.81041 | 2025-06-14 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1d8385c7-61c1-3206-bdbc-9a24eda2832f | -6.69018 | -43.97292 | 2025-06-14 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af53c758-f643-35b2-99fe-f0f1fe5d58a5 | -4.81847 | -44.35545 | 2025-06-14 03:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd27b94a-0fae-3dad-b50f-1e6d84db678e | -6.21475 | -43.33325 | 2025-06-14 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README9.md)
