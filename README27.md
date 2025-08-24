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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2f7b41d-36c8-3f49-a29c-be36c92d34d7 | -13.13552 | -44.90693 | 2025-08-24 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1dc79c86-1752-3187-80f4-c1313df2d8ba | -11.1355 | -46.33797 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d51e47bc-c4b0-39bf-93d8-2f3e171f30c5 | -12.94358 | -46.29288 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9ce09fc-cd2a-3a20-ad91-5c9eef9c7add | -12.73028 | -48.11192 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4d93bee-533c-3a6c-8023-ae4bc96d3cf1 | -13.16465 | -46.93262 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 956884d0-03f7-3448-816f-e7ce3d30a149 | -13.16936 | -46.91814 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9622fce-dc88-34ab-af82-6547272289ff | -13.05424 | -40.94228 | 2025-08-24 03:45:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69848608-8755-303e-bca0-70ea88d5e444 | -12.72932 | -48.11673 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7b0a8c8-6ef7-3399-a418-1a56b16fd3dd | -14.22281 | -39.76932 | 2025-08-24 03:45:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1294a7d7-5cce-30b8-a2b2-8669402fdaec | -13.64359 | -46.87831 | 2025-08-24 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 246550d7-8b08-3151-8d27-fd2a96950343 | -13.47321 | -47.02261 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42b8f43e-103e-3442-8b49-98a7c86551f0 | -13.05059 | -45.22371 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e000fa4-bd01-3b4a-a24a-5ff1ea79982c | -13.49893 | -47.03043 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fa63c85-7be0-3cf4-a324-7743fb08b38a | -14.80169 | -47.92458 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f821a697-bf72-3720-b263-310557c4fda3 | -14.80398 | -47.91622 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47e6f426-9ab4-3a8a-921a-f9a734e522f9 | -13.16704 | -46.93 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 698931a0-51cb-31dd-9f50-7c7dc7bb770a | -12.0436 | -50.35945 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 483ad2ce-a385-3696-82a5-15ff8efd579a | -14.84428 | -48.3243 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd0b80b3-29a3-3ef4-b57a-1b1167d1674e | -13.04226 | -45.24038 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07a4f014-b6c4-3183-afc0-ec80fa723889 | -18.75282 | -45.0958 | 2025-08-24 03:45:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fd8fc90-5e90-36a9-8286-251c1b1e05ee | -18.89605 | -43.34053 | 2025-08-24 03:45:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b1e843d4-3801-305e-bc1e-96e426c0b04d | -13.04063 | -45.22162 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc9639c1-1a2e-3ecf-a6f5-275ab814defc | -15.12982 | -48.62758 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49a886ee-c946-3b8c-9b13-e72a98a9ed39 | -14.80646 | -47.93059 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0ca1357d-ee2c-3312-b832-3e9ef4460a9e | -11.31161 | -47.84985 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e674614a-e0f4-33d8-a48d-27d255b5769a | -14.8031 | -47.92036 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a7843ff8-daed-39a7-b9e7-b388b75522b5 | -18.39391 | -46.85042 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348f85ad-bd72-3823-b3c7-16ab35f636a3 | -14.84019 | -48.32617 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd8e0ed-d68c-3c57-89cb-c794276a53b2 | -12.73661 | -48.11161 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7adf2de6-7ca5-3f40-934b-b8552db1bc29 | -13.50291 | -47.03943 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccaa76f6-85ff-3a96-abb7-360f399e06d5 | -17.06052 | -47.15798 | 2025-08-24 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69ecfbee-c53d-309c-a25f-f02dfd7cf262 | -13.46217 | -47.01984 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 241ca93b-e5e9-35e2-badd-0bcf2456fcfb | -12.71986 | -48.1012 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62a6cffa-c781-3b76-8c7f-ece9ca19e250 | -13.04506 | -45.22558 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c3e99a7-58c0-3728-853b-29fa66fceacf | -12.95385 | -46.32634 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea6d8184-9459-3bcd-80d1-f6121ea0da12 | -16.79517 | -51.36368 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 77041724-bba9-3e00-9166-f07116378782 | -14.39816 | -49.77175 | 2025-08-24 03:45:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d210d96b-4ee3-34c6-a627-333689a33cd1 | -13.33101 | -43.19133 | 2025-08-24 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d3daf14-0d87-3c07-bf18-57629c402338 | -16.78853 | -51.36158 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 72178905-d9bb-3cd4-a820-d6f6bddeba0b | -17.03978 | -47.17854 | 2025-08-24 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee544a57-fd73-33f1-82be-bfeb590ded62 | -13.48917 | -46.90783 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b67eeb80-3231-3bc9-a054-52daa9b75902 | -12.73722 | -48.11351 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f36003b-183a-3b12-8b9d-ce7973ebacf9 | -18.70527 | -40.00797 | 2025-08-24 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 403aa35a-16ca-3678-8c4d-270c9112d098 | -13.46248 | -44.07785 | 2025-08-24 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61b7cae3-c1e6-3b0f-951d-7379d1dad7df | -13.47064 | -47.02699 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7fdad53-69a3-3fe0-87cd-c344a540260d | -15.73482 | -41.61721 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33fe22a0-93d8-3c23-bcd5-0bc2f266ef3c | -14.80141 | -47.92838 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da0d738f-afb5-3758-a379-3f4a8699c068 | -15.12899 | -48.63148 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abb12f76-9331-39b4-a5f8-5626372ea36f | -15.10716 | -48.66534 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1d91a3e-9067-3b8a-986d-e53b06287fd3 | -14.84599 | -48.32784 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b0c2323-5e1c-32e0-894a-05e3d9c1260d | -17.03908 | -47.18188 | 2025-08-24 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f6c5036-7443-3214-80e1-bdc0e1449d26 | -13.03064 | -45.21965 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65dcec25-51ef-39cc-9ab1-1aaa9e7a60f1 | -11.13688 | -46.33914 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79a0bb0a-5a88-3e41-9952-5d4b277536f1 | -18.40714 | -46.8433 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91e61544-b527-371c-a123-1ecc9c0b4c01 | -14.87547 | -47.60367 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb4eac84-85c4-35e7-868d-51a8dcc54db8 | -15.2345 | -43.85384 | 2025-08-24 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daa09315-67c4-33c9-b86e-b116c09aa3cc | -12.99346 | -45.22423 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d60e5d0-6645-3a90-93f0-f5d0442b71c5 | -12.95623 | -46.32598 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a9df3c2-10f2-3695-b996-df442c809382 | -13.05122 | -46.32544 | 2025-08-24 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a8f8f7b-2099-39d2-9f30-6ab0e9267a9c | -13.95773 | -41.85829 | 2025-08-24 03:45:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2304bbd4-da7a-3a77-bffa-6dca99f27a2c | -17.60451 | -44.29687 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 932231b0-c813-3978-bd46-5b00f6afa28a | -12.54669 | -45.62467 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8f696a-a352-3d46-b606-d947b0812370 | -12.96205 | -46.32483 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af1f21c6-56a5-3e83-bd8c-d51b0238555d | -12.55234 | -45.62772 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40f97b01-4039-3dc8-9205-c316cdde9953 | -13.16629 | -46.93387 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5094a10-e1b8-3b01-a887-7364b8f873f0 | -18.75562 | -45.09414 | 2025-08-24 03:45:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f418bc73-3dd0-3bc2-95cc-1013f8f7b494 | -12.99175 | -45.23311 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b1dd838-bcc4-38f9-a715-cc161412cad6 | -13.48997 | -46.90394 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 805b0932-956a-3a51-9929-facd3ce109e7 | -13.16701 | -46.92097 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb1b2e0a-1a28-3566-8f9c-53db117e904b | -16.7911 | -51.35556 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 045c1a8b-c140-3ecc-a59b-8700f326674e | -13.03507 | -45.22358 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3381edb-58a2-39b8-8c38-982c8e561abd | -13.04672 | -45.21678 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e82e4f5a-5474-3812-a3d9-c709318ef3c0 | -12.20223 | -47.10939 | 2025-08-24 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37de17b1-8179-3294-a546-bbcba8ca709a | -17.8291 | -44.54939 | 2025-08-24 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecd94f9e-2088-31a7-8048-7096c57edfe4 | -15.70974 | -41.93635 | 2025-08-24 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4bc046df-028b-32b9-b7f5-ce84a9855b9d | -14.84541 | -48.31893 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1238f831-77e1-35e1-b75c-22304f97cfd1 | -13.1678 | -46.92613 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2592da76-b206-33cf-90fb-36413243a660 | -14.16292 | -43.66882 | 2025-08-24 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a367e19-c130-3bf1-ac3d-798ab10dcf33 | -13.02951 | -45.22557 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a2e1495-421b-3f45-bcef-63713fad33c6 | -13.48432 | -47.02509 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1befabc1-c21e-3953-99c3-a727223eeefd | -13.1432 | -44.90406 | 2025-08-24 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f72de52-7370-312d-a4fe-1a91986a47b8 | -14.85097 | -48.3217 | 2025-08-24 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e466282a-943c-394b-bb58-b6594d84a9e9 | -14.80817 | -47.92218 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 21d3ee5e-fc6a-301e-98f5-d4c9c0d4ab07 | -12.72988 | -48.11861 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c1576d3-7121-35b5-a22f-450a29b47f79 | -11.13068 | -46.33311 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71cee62e-9f58-34bd-9f19-570ef8839350 | -12.73306 | -48.12949 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1f6ef05-3ff6-3590-83bd-510d442e8324 | -13.04282 | -45.2374 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b56b443b-9a91-3ccf-93d9-b1185c4c4f4b | -13.16856 | -46.92223 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56482aac-1f58-373e-9acd-2e343b535ea9 | -13.46687 | -47.02539 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9988c72a-a00f-33a1-a83f-78b91e69ed52 | -13.03951 | -45.22753 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8709ccaa-ed1c-3d47-b4d9-e42eff64bc9a | -12.95974 | -46.32478 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1945593-f2dd-3af5-a06d-2e56d12f55d4 | -13.04838 | -45.23544 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bb4d898-b766-37b9-abbc-3734f6eaac44 | -13.03282 | -45.23542 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e3c1b3d-20da-33a1-88bf-38f5d19ded28 | -11.28474 | -44.97612 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d93fc555-90f3-3cba-83a5-fc27632ad5c3 | -18.39531 | -46.85002 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bfc6874-d058-39ae-b982-22dd15f1ef42 | -13.64911 | -46.87936 | 2025-08-24 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a5f68d8-43c0-36ec-b048-31f3422bef73 | -11.28415 | -44.97923 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0efff4aa-de18-3469-8942-ed5fa986bce6 | -15.00475 | -48.48767 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5c418c-9751-3723-9140-9aec78f99420 | -16.42079 | -49.14505 | 2025-08-24 03:45:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1b071ef-98f1-3763-a0d2-74ddb4111545 | -15.00302 | -48.48062 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
