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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24a470a5-a146-3183-bdd5-fe6866e81318 | -11.95392 | -54.67731 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4a2d41d7-5d6a-3e5f-a9d4-4daf19879c9f | -14.14644 | -52.88686 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efd56cb2-68c2-31b6-855f-42305e812304 | -11.9555 | -54.66477 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b8a981-6642-38b0-9cab-167f80c06d27 | -11.74095 | -54.24874 | 2026-05-12 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96a16408-94b3-3b57-b949-92a9bff0cd7d | -14.55386 | -58.7929 | 2026-05-12 05:33:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a77ca63d-ddb7-3de7-8f80-6a9fad18491b | -13.18553 | -52.70971 | 2026-05-12 05:33:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79edb268-03a6-3b57-9d67-6f44dd763f18 | -11.95471 | -54.67105 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13602704-d86b-36c9-b99f-f958a6f90eee | -23.54816 | -55.4548 | 2026-05-12 05:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 781975f6-aad3-3f1d-91d5-6e548bf6785b | -23.54852 | -55.4507 | 2026-05-12 05:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e0313254-36f1-376d-b9c5-a151f8dd4265 | -10.55425 | -56.32636 | 2026-05-12 06:54:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b70be72-e9ca-35ae-85c1-40c8c65efa02 | -11.95587 | -54.68109 | 2026-05-12 06:54:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a8b99aa9-647f-3d29-a764-2661267ac360 | -14.14512 | -52.88865 | 2026-05-12 06:54:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 581e86bd-8475-33b0-8526-4e625d24161c | -11.29754 | -54.02085 | 2026-05-12 06:54:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9eaa98cb-c50f-3ceb-ac97-128c0c0d46ef | -11.95721 | -54.67219 | 2026-05-12 06:54:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25480ee0-9b2a-3330-872a-581cacfa2963 | -14.53893 | -58.79799 | 2026-05-12 06:54:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e538bed0-71ed-344f-8d42-b4e33fe3985f | -11.73437 | -54.2462 | 2026-05-12 06:54:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c143f36d-8221-3978-b445-9ad82a8733e5 | -6.25879 | -42.57665 | 2026-05-12 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 11bdda0a-d712-3950-a8a8-e3f10faf028a | -6.24773 | -42.57502 | 2026-05-12 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 5eac3eaa-0693-3f12-a649-871636f93666 | -11.70438 | -44.73458 | 2026-05-12 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3d7f7a7d-6911-307a-af89-4666f3319080 | -16.76553 | -45.81767 | 2026-05-12 12:00:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c28a5cf1-edc4-3493-b416-f6048292f708 | -14.13888 | -45.39404 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ab533791-482e-3da2-907f-5e927f3363ad | -10.1323 | -47.92432 | 2026-05-12 12:00:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9716ffa9-440e-3336-9b2d-b873cb1e6cf6 | -10.13102 | -47.93324 | 2026-05-12 12:00:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e441c9e4-f74b-36dd-a861-42ed089da946 | -13.73503 | -41.92477 | 2026-05-12 12:00:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| cad572ba-dfe1-3618-ac4c-015fe844d48c | -14.12629 | -45.33088 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| f273f3a1-6d72-3fa5-a496-45765076c5bf | -8.52424 | -44.32648 | 2026-05-12 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ecdb2347-5ea5-3b45-b4d5-a550c1ba41f7 | -9.42331 | -50.73474 | 2026-05-12 12:00:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a0c10fa5-b5dc-3117-a84f-5bb35e372f08 | -16.10423 | -49.22916 | 2026-05-12 12:00:00 | TERRA_M-T | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b8565b55-993a-3922-acd5-c8530d8d434c | -11.78508 | -47.38123 | 2026-05-12 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 49c89567-279e-3294-82b1-53cc83d0c483 | -14.149 | -45.39532 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 60b4d7bc-dbf3-3a21-9ff8-770a6eddef64 | -11.93966 | -43.39072 | 2026-05-12 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a80507bf-360d-3794-a489-a3e55bbcea21 | -16.10694 | -43.81342 | 2026-05-12 12:00:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cc48f6c5-b1df-37cf-879a-0d999f0e1a05 | -14.30414 | -46.93626 | 2026-05-12 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c0b0295e-217a-338f-bb34-7c32d6f46898 | -14.31341 | -46.93755 | 2026-05-12 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3d840cc-3738-3a56-b406-91f7f05bc3fd | -14.15055 | -45.38329 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b98bafc2-f039-3f0c-9c47-c78738c2f7d9 | -10.0876 | -50.61349 | 2026-05-12 12:00:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2816f97-19c9-3a1d-94bb-cc027b7e822d | -12.41583 | -49.67021 | 2026-05-12 12:00:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5ca69214-180a-3f16-b663-b0e411d8650b | -13.97282 | -46.04327 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8cd3f48d-3053-3608-83b0-b53a6770e13e | -11.97909 | -46.78331 | 2026-05-12 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 77c6878f-7f02-370a-8079-5876c8d0a517 | -11.94156 | -43.37565 | 2026-05-12 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6cfaaadd-2a90-3fb0-81d4-d6c99b5cf4c9 | -14.88278 | -50.95289 | 2026-05-12 12:00:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a523c71d-15fc-3b0a-9ece-58ec0b6cd182 | -10.9985 | -46.48273 | 2026-05-12 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 98dd5509-403c-3f71-a374-187ac17e7910 | -14.40152 | -44.58971 | 2026-05-12 12:00:00 | TERRA_M-T | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| adab272c-0374-341b-9429-423d9fea60f3 | -11.96005 | -54.67875 | 2026-05-12 12:00:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| be470901-4a05-3426-8ecb-e3748b8d3df5 | -16.10495 | -43.83007 | 2026-05-12 12:00:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 470348c8-c491-3109-9c78-a47b74406541 | -9.01314 | -46.12277 | 2026-05-12 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0740ea66-adb9-3b65-b21e-2a7ae7f77bb1 | -13.97426 | -46.03237 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 55f2ca14-4e91-3c93-8f44-065256f49e9f | -13.45972 | -47.72669 | 2026-05-12 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aed79297-7bf0-3eda-aa2c-ecdb4f971e5e | -14.13645 | -45.33221 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ad0566dc-eb23-351c-978a-e1832210dfc9 | -14.88128 | -50.9629 | 2026-05-12 12:00:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 20e82a64-9e11-3c36-a021-5cd19c40ff9f | -8.05168 | -43.74509 | 2026-05-12 12:00:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 68791375-a456-36d2-8fc5-d20eadb36a8f | -15.15547 | -41.28477 | 2026-05-12 12:00:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 1e36d7d0-f2f4-30a9-a391-1f48c6fb8925 | -14.14043 | -45.38193 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 025a3567-a331-3bae-bc0c-244ec8a6f0cf | -15.66582 | -41.29437 | 2026-05-12 12:00:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 0bb89f58-c8fd-3e61-b3af-6b95f7ed8f4b | -11.93762 | -47.876 | 2026-05-12 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cc971fa5-9f39-390b-8c5e-d16538bfb607 | -16.74686 | -50.70174 | 2026-05-12 12:00:00 | TERRA_M-T | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e55ee70-3ceb-3ac8-bc8c-45e9d6fb5d24 | -14.13799 | -45.32004 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 67489402-ef09-31a7-97ac-281cb0ea388a | -14.12782 | -45.31871 | 2026-05-12 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 038d6f0b-f633-3519-8eb0-86448525b99d | -13.08963 | -49.72939 | 2026-05-12 12:00:00 | TERRA_M-T | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7fcbd588-b6a1-3215-813b-0c82fde500da | -11.78637 | -47.37203 | 2026-05-12 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0079080c-3db7-37ce-bddb-f29323f34579 | -14.4032 | -44.57597 | 2026-05-12 12:00:00 | TERRA_M-T | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| be773c3d-9a5e-3df1-89c7-33aad691253c | -15.8566 | -46.53793 | 2026-05-12 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0b85ee39-dfa9-3626-a1e5-4eff10a7965b | -10.13357 | -47.91541 | 2026-05-12 12:00:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e5c4a1e2-f799-391d-bc8a-babc9cc6b24e | -12.16202 | -51.33787 | 2026-05-12 12:00:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 37cd72a9-ec52-3750-8956-9b549208d022 | -9.4565 | -47.82124 | 2026-05-12 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f5824b74-cbaf-347f-ab98-dbdfc84847f9 | -14.14265 | -52.88821 | 2026-05-12 12:00:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c7342dba-cf22-37ef-a0ea-08eb9e6f5d9b | -17.36042 | -52.00835 | 2026-05-12 12:02:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 531954ee-0ae1-3f9d-ae36-4871a18fed01 | -20.49277 | -50.43644 | 2026-05-12 12:02:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 8aa90354-0e6f-330b-be7f-1ca9aa107264 | -13.9615 | -46.0334 | 2026-05-12 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 887fd0ad-e381-3bd6-9e39-637d77ff05ba | -13.9615 | -46.0334 | 2026-05-12 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 86d12695-999d-3fcb-9e76-7ed23ecae4e0 | -13.981 | -46.0301 | 2026-05-12 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 78915f33-c7f5-3c64-9218-c809a4656c00 | -11.9498 | -43.3781 | 2026-05-12 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ec31f7ce-21b2-3db5-82d7-14da123b97ca | -13.9615 | -46.0334 | 2026-05-12 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ea47a6fc-4bea-3307-9821-7d0d928c7de8 | -11.9498 | -43.3781 | 2026-05-12 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 265e688d-bfe6-35c9-b93c-5b2ca89f900d | -13.981 | -46.0301 | 2026-05-12 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e3385e04-33dc-369d-9279-b50172eec33c | -13.9615 | -46.0334 | 2026-05-12 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 994e419f-b493-3fa0-bc64-8ad0e4b38e92 | -13.981 | -46.0301 | 2026-05-12 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4d778e82-1505-32d4-9395-73573f204107 | -13.9615 | -46.0334 | 2026-05-12 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 93080028-fb8c-3df7-b81a-87067e278ef9 | -13.9615 | -46.0334 | 2026-05-12 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| ff851052-6958-3912-b636-5e9875cae8a6 | -13.981 | -46.0301 | 2026-05-12 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 5866f503-9e8c-3c4c-8084-e4029d416314 | -14.1312 | -45.3344 | 2026-05-12 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bb5aaf03-3769-3b6b-a63d-659f55870e6f | -14.1312 | -45.3344 | 2026-05-12 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9e4996b4-c8df-30a0-b055-e520da3f8ac1 | -11.9498 | -43.3781 | 2026-05-12 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9d8750fd-77f7-3366-ab7c-00fa82720f97 | -13.981 | -46.0301 | 2026-05-12 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c6d30886-8c4a-316a-bc51-2ed730f78c9b | -13.9615 | -46.0334 | 2026-05-12 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 99c6f634-2e61-37ff-876f-1bb312d0a054 | -11.9498 | -43.3781 | 2026-05-12 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 15268e6a-9911-3366-96fb-79a4a28c8c49 | -14.1317 | -45.3111 | 2026-05-12 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| f10ba8a5-52d9-3498-a7ad-55c740341396 | -11.9305 | -43.3812 | 2026-05-12 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1b6dd62a-ed95-3472-8d7b-6f7e7ea9037c | -14.1312 | -45.3344 | 2026-05-12 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 96aefec4-8495-33a9-82a0-3192f3133972 | -13.981 | -46.0301 | 2026-05-12 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 443cf75f-356d-30da-b1a0-5f97a02311ec | -13.9615 | -46.0334 | 2026-05-12 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| d8f89ff5-f088-31cd-acd6-dcf2dcba138d | -13.981 | -46.0301 | 2026-05-12 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7a9a64d3-5958-3fe9-8742-1c8f79442456 | -14.1312 | -45.3344 | 2026-05-12 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| cc53256b-e410-36c8-b98a-2d0c67820f3e | -13.9615 | -46.0334 | 2026-05-12 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| a5064c1d-67f1-3de8-b30f-7d6e20f2b152 | -14.1317 | -45.3111 | 2026-05-12 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| a3a376c3-13d9-3ede-aedb-50bc32bb8377 | -11.9305 | -43.3812 | 2026-05-12 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 0c3c77f2-894a-38e1-8041-c2d284f3c255 | -11.9498 | -43.3781 | 2026-05-12 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 8bf89498-b9b7-3070-b8bd-3b7d962b1218 | -11.9305 | -43.3812 | 2026-05-12 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2261e5be-60be-3d7f-b135-53107232e31a | -14.1317 | -45.3111 | 2026-05-12 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 5155232d-4b82-3b3d-8e64-0893b123580a | -14.1312 | -45.3344 | 2026-05-12 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |


[Clique aqui para ver as próximas entradas](README7.md)
