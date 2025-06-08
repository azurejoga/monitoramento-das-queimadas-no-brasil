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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44116712-e256-3264-9099-86701df2bfcd | -7.85946 | -47.89401 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bbffd273-7185-3b45-9841-1d8cb321b940 | -5.57251 | -45.20232 | 2025-06-08 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9937e546-b1f6-3ba1-a2fc-8aa77c2a078b | -7.02408 | -44.58432 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1810fd9c-2947-394d-8ec2-123f3f644347 | -7.00991 | -44.59535 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bab28299-06c1-32f9-9f82-a23d2fe50f29 | -7.02096 | -44.60142 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0ddb7b82-44f5-361f-ae11-efd3652ee030 | -7.73501 | -44.17096 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 943490cc-d691-30b0-8213-7e56cba8106c | -7.7406 | -44.17237 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 01603948-d950-3bf8-908c-7735b6cc58a4 | -5.57554 | -45.20715 | 2025-06-08 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15550ccd-631f-3f8d-b1ce-f84e29f8c494 | -7.02018 | -44.60572 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3dc2d169-5d4e-3b87-9f2e-c7817af7c66b | -14.87201 | -48.10886 | 2025-06-08 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 499642f0-bba2-3ad4-b76b-77833a8ee10e | -16.06733 | -43.65905 | 2025-06-08 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 803bb99a-47ad-3b4f-94ce-1e9f7ad3e707 | -9.40741 | -48.43852 | 2025-06-08 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b085a924-221b-3989-91fd-a4858924080f | -9.07415 | -47.14072 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa445d78-c628-3e42-8a14-a142f406914f | -10.75188 | -48.58067 | 2025-06-08 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bbaf25b9-133b-3a06-8d44-d0d6c49f6c7f | -11.79148 | -48.09071 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 790acfc7-3412-311a-86ce-38021e351a98 | -12.96679 | -46.75364 | 2025-06-08 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a87ebd62-a39a-3246-ac32-3ebdb0604939 | -11.8035 | -48.08587 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 31ce56d2-720c-31f8-b12a-f05a68905f36 | -13.41882 | -43.75449 | 2025-06-08 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb9528b-a6b2-31d6-9c62-1d5e64c665f9 | -10.75651 | -48.58245 | 2025-06-08 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06f7cf87-67bf-3300-b8ae-9ab2662f63f5 | -15.52678 | -42.62636 | 2025-06-08 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 553d256f-267c-3b98-ada9-9a9ac96f03bf | -13.49909 | -39.92225 | 2025-06-08 03:38:00 | NOAA-21 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6703a01c-1b2a-3007-b4e1-2e4d0bef2b76 | -15.52321 | -42.62082 | 2025-06-08 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 10df5c05-3bc1-3c2d-b1a0-73ad758669cb | -16.06836 | -43.65383 | 2025-06-08 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1a5d02-3f1a-3df4-8b3e-d1897e445a94 | -11.62791 | -48.49056 | 2025-06-08 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d838baf3-7d80-3117-af94-123cedd36753 | -13.54192 | -44.1415 | 2025-06-08 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e270cb0b-a418-3a1a-b427-1705f260f0e5 | -11.79278 | -48.08456 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a0d657b7-a3e8-3977-93b4-e85ef2a0be59 | -11.36939 | -40.42391 | 2025-06-08 03:38:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38f9e248-8534-3ed9-9918-9260d285973e | -14.87989 | -48.10314 | 2025-06-08 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e356151-bb0a-3936-b9b2-d8a39ef05971 | -17.50236 | -42.2885 | 2025-06-08 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f0a02f5-7236-36c1-ab5b-b668b012b9b2 | -9.40597 | -48.44569 | 2025-06-08 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1674a2da-f139-3e85-989c-87a3c719397b | -12.96772 | -46.7491 | 2025-06-08 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7afdb26-5935-3240-b5f6-083ac0fea2ad | -9.07738 | -47.13947 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 591974db-8a17-34a7-9b3c-575572831a17 | -10.6463 | -44.48973 | 2025-06-08 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0f11ee1-3a1e-3290-b62f-1e4ebfa121e2 | -9.06964 | -47.14391 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36c750a2-37be-399f-8efe-721e14ef10a7 | -11.7888 | -48.08948 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ce0eee-5d88-331a-a106-8c3e38217186 | -11.8062 | -48.08716 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af7a9bf2-2bd2-3a0a-9bb6-d093ac061cd0 | -9.073 | -47.14651 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 87259753-30d0-38f3-95a2-3a173b5e6691 | -16.40121 | -39.35785 | 2025-06-08 03:38:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a462afff-b768-3f98-8808-56631689ed61 | -9.06848 | -47.1499 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfeee8e6-37de-3b4e-ab99-24b08a3688e9 | -13.54131 | -44.14467 | 2025-06-08 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac3d7e79-f465-3aa9-a3bb-ce386f575ea9 | -11.62823 | -48.48959 | 2025-06-08 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5fea7357-d23a-3b76-b137-e2c8292cd49e | -11.36876 | -40.42747 | 2025-06-08 03:38:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d29ada13-6655-3a8b-9560-2159a4c66c26 | -9.4131 | -48.44696 | 2025-06-08 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 362e85e3-c99e-3a3d-9c63-a2a349e28ab6 | -10.64147 | -44.48512 | 2025-06-08 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eabe51a4-928a-35fa-a7e7-5a5e20af2776 | -9.07627 | -47.14523 | 2025-06-08 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37513f73-2189-30ec-9b32-d2a43c5b0ee8 | -11.7995 | -48.08582 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f7786a3f-0c85-3fcc-a526-91023d36b111 | -10.74957 | -48.58072 | 2025-06-08 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc149789-c782-3230-893f-f42b452babb8 | -12.94732 | -46.75595 | 2025-06-08 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c27fb8c-4234-3ae5-99ed-1f3e09be7ce8 | -11.80488 | -48.09345 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e1dff5b-8ac9-3bba-ba0b-7c3a6bc0d719 | -15.52234 | -42.62539 | 2025-06-08 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| edeefb6c-3c8f-3f13-b7b7-56443eeb7cf1 | -13.8849 | -43.78191 | 2025-06-08 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84eac81e-80cc-376e-8ec8-e6bc41dbc7d2 | -10.64215 | -44.48152 | 2025-06-08 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6687ede2-f0bd-3287-8e7d-bd48237c820f | -12.94631 | -46.76087 | 2025-06-08 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2b71830-3d8e-3477-8811-a7aa1f3b480d | -15.52763 | -42.62184 | 2025-06-08 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e09b7e89-2fe6-391d-b615-809fd8775c28 | -9.41163 | -48.45427 | 2025-06-08 03:38:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 825f89d2-ade3-313f-80ca-d3a1a8531891 | -15.49727 | -44.41471 | 2025-06-08 03:38:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57f2cc4b-51b7-33f2-b0be-95492edee4bb | -11.79678 | -48.08459 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b1735d7-5059-32f1-aa83-d6804e436b6c | -12.97267 | -46.75579 | 2025-06-08 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 971b4f79-5973-3351-81ca-d6647f0557a8 | -16.40007 | -39.35923 | 2025-06-08 03:38:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b1148364-7046-38ab-ac06-04311b25dc69 | -11.79551 | -48.09079 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 83f128ba-751c-3105-be90-9ae8bf6adaf4 | -14.88252 | -48.12191 | 2025-06-08 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d30056e3-7c79-31d6-a703-ecf486e4cd24 | -11.80221 | -48.09218 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c87f3f87-2964-3c82-85ea-19e728ec95da | -12.96073 | -46.75235 | 2025-06-08 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b49e621c-96a7-32c6-ba86-9a1b80436194 | -11.79819 | -48.09206 | 2025-06-08 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 17530937-bdee-3d0c-bd0e-f85a639d661d | -10.64562 | -44.49337 | 2025-06-08 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d7a2d5b-5286-3211-a095-44a1270d295d | -14.88119 | -48.12812 | 2025-06-08 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9044e199-45b3-333b-9ada-62b49e784e28 | -17.09551 | -43.80575 | 2025-06-08 03:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8afa995e-95fe-3584-ba4b-aede251ab802 | -6.5631 | -51.1126 | 2025-06-08 03:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0046c1ec-d55f-325d-89d4-ddc1ccf790aa | -18.02457 | -47.38778 | 2025-06-08 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03e77a9b-555e-388d-a82d-4d9a6956b4a3 | -18.0255 | -47.38354 | 2025-06-08 03:40:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8fa39a1-230c-357e-bba2-d8f8a9c7cc60 | -17.75318 | -42.89667 | 2025-06-08 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13e7daa4-8726-3644-8e90-32924875d2a3 | -21.38645 | -48.64066 | 2025-06-08 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f74c913-c532-3731-a341-4c6cce6b0547 | -4.60811 | -38.52877 | 2025-06-08 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 6055d5c6-e32d-3f4d-878b-8e9a91c5ef72 | -5.57345 | -45.20096 | 2025-06-08 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a278c0a-a18e-3615-9bd7-cba9ec486c18 | -7.01818 | -44.58881 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdec3799-5785-3ca0-9dc4-1e9ad34cf145 | -6.87736 | -47.2415 | 2025-06-08 04:02:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6d9657d-b4bc-3b3b-82fd-18580eabda84 | -7.41521 | -44.61005 | 2025-06-08 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381a9094-d95d-308a-afb6-f74d493286ea | -7.73734 | -44.1874 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| babbeccf-7f9c-322c-aca5-edfca6d12922 | -7.73132 | -44.17696 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee0d34a4-42e9-3d68-bd58-6182874ad01e | -7.01265 | -44.59796 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52a644b7-6cc2-3a79-8245-cbccf51554da | -6.6385 | -47.3487 | 2025-06-08 04:02:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12583037-4c3e-373a-bd5f-6f9b24c6ebab | -7.02289 | -44.58455 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e40868d-03ce-3247-acde-679b9b1c0b91 | -7.02208 | -44.58945 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 01af44f1-0b8b-3c67-80d2-0a7f278c137d | -7.7381 | -44.18282 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c78a60d-c78a-3cac-844d-c2d0fbf1ccad | -7.73508 | -44.1776 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9398601a-d620-3d54-bc94-e3f849466a98 | -7.72906 | -44.16721 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd5be1e5-d0e4-3f83-9f7e-8a5d9209be42 | -7.73207 | -44.1724 | 2025-06-08 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4889b0c-0e49-325d-83ab-2af5ee43d435 | -7.01655 | -44.59861 | 2025-06-08 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b340b03-6aac-3e1d-953b-14ed3e5e82f4 | -5.64388 | -43.71505 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b22df4c5-9ad6-318c-840b-b037c858b5da | -5.63482 | -43.72301 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f3f5597d-a75b-34a4-90f0-de3b6f200522 | -7.36905 | -39.06012 | 2025-06-08 04:02:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45d2107f-8659-3afa-9480-a2d010e91646 | -5.6484 | -43.71107 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b16fb336-553a-3965-97a7-fee3e45aa9aa | -6.19973 | -43.32442 | 2025-06-08 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a6dd969-621b-37e5-b87a-75b819c1ad16 | -4.91557 | -41.99906 | 2025-06-08 04:02:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 811378c9-bdda-393b-8278-a156f9ae3fa9 | -6.40947 | -43.64128 | 2025-06-08 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8c21e46-8b9f-3197-acbe-41bf17b92fa5 | -4.48535 | -43.77802 | 2025-06-08 04:02:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c85ac8e5-e0c3-3155-ac43-95743200566c | -2.91872 | -48.23899 | 2025-06-08 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e129f14-403f-34f2-b384-c24e5f14c573 | -4.48456 | -43.77595 | 2025-06-08 04:02:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bd53e57-fc1f-356a-83c8-eaa727a2d94b | -4.60475 | -38.52826 | 2025-06-08 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 76c7703d-9a0a-38c5-8009-093502f05bcc | -5.64313 | -43.71963 | 2025-06-08 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
