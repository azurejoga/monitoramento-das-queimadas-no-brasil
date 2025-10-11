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
| c07570ec-c576-3f99-b733-52a9da078474 | -13.45838 | -48.0989 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4268362-764b-3f1e-9fe7-5cd8c3c36f8f | -14.01937 | -47.05973 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d2f76ed-ee77-3f96-b6d6-4dc19480e9fc | -14.98982 | -45.559 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53bbd5a7-1cbf-3343-b1ae-d29516384bd3 | -13.28756 | -47.13475 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27d29e33-e424-32c6-a0e0-affd18077bd3 | -8.58563 | -48.74959 | 2025-10-11 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18f8f322-37c5-33a2-90de-716ab3b4bfd4 | -14.93526 | -46.75032 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4c865f5-6d70-3bec-863d-4766d0c79bc5 | -15.5962 | -48.49952 | 2025-10-11 04:34:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d352b027-2583-3792-8609-5e9e693463ca | -13.21025 | -42.35222 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c922c748-c9c0-362f-9e3f-6c6f386369ef | -14.95601 | -46.75849 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e0ac75-1ea8-32d1-b1e3-b2f0a311792e | -10.51597 | -47.35731 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 287231ce-a4fc-3494-aa24-3074084a569f | -13.31595 | -47.12634 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca4e8ca7-2728-302c-834f-d9812e2655dd | -13.84618 | -45.81166 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3188a2b4-2748-3d16-b5cf-bdeecdd4deba | -16.37022 | -40.75335 | 2025-10-11 04:34:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a668f99a-69b1-3857-af97-2382edd84cd0 | -9.83154 | -44.96091 | 2025-10-11 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63f32c3e-ab9f-3e48-a2ac-d222b6c09842 | -9.93433 | -59.91997 | 2025-10-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4ae5420-0bb6-3061-88de-bef817639c91 | -13.33064 | -48.49024 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10807bc6-d139-3633-bb77-64f2fe7001ab | -11.91587 | -44.17846 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 04702d8c-34da-3163-a28e-a86032a28d81 | -9.40127 | -42.66819 | 2025-10-11 04:34:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b3612f30-6f28-33f7-8859-2335391be253 | -13.30943 | -48.49751 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55accef9-da08-3c43-8a09-fde8e77dc699 | -10.38927 | -45.34546 | 2025-10-11 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8c1f2a0-4ff6-3e6f-b68b-cb905813662f | -10.6537 | -45.09766 | 2025-10-11 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc1288bf-307d-3631-b82e-5624359ae5ec | -15.70425 | -46.62458 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59d7151-8ed6-3b6d-9eaa-ca037b94b0c6 | -13.28657 | -47.99317 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ea06711-7e1a-32f3-b7d8-9b3c045127d3 | -14.71369 | -47.43588 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ead25665-31a0-3eb6-ae08-f9190ee0b9e0 | -9.11618 | -45.07342 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b4a0b73-94f6-3ba7-8faa-8b56c6bfcf54 | -14.92869 | -46.77078 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be5cdc6e-8e65-3376-823a-98e5907b67d8 | -13.01019 | -48.80699 | 2025-10-11 04:34:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcce411e-43ca-3573-b669-d8f9565eb7e1 | -13.31998 | -47.123 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d29956b-c2c9-364a-bd35-7ded58a3fda7 | -13.76689 | -45.40666 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4adabad2-5101-3521-9540-df9cd9d79ac5 | -11.77127 | -46.37597 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67c3073e-44e0-3009-b9b2-6f7f5dba4761 | -13.33628 | -47.75199 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ffebf7-7bf3-3a73-a1db-d7e2c21c0ca3 | -13.20747 | -42.33699 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ae3d47cd-d262-3b91-871c-6d88fd46a582 | -11.06448 | -49.5634 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 921325b5-ace7-38c0-852b-c0d1037be99a | -14.97024 | -47.26161 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fcf96d9-cddd-3262-9358-5a34998c3892 | -10.19074 | -44.60936 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e00551d-53b0-333e-ba7a-bf5776703ab7 | -8.71575 | -48.05292 | 2025-10-11 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69a10916-6b4b-358a-80f5-2ba33d42e715 | -13.30389 | -48.48921 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee0500b5-1a8f-3a05-91ff-579a3c75ba93 | -9.04593 | -45.11665 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc211cc3-da0c-36c5-b57a-39084c005376 | -13.30766 | -47.11858 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc89e0f5-8816-36d3-a2f2-7b9ef0ef6981 | -10.14895 | -44.6039 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1a18c19-a3ba-333e-8128-e5d60cfba78b | -13.0836 | -54.84054 | 2025-10-11 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 489ff6ee-fae1-3bea-ad30-efe603f49000 | -13.27835 | -48.01105 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5078524-94b9-3061-96b6-26a38f6ac1f9 | -13.20627 | -42.3467 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 6c092847-8bc9-304a-a789-f8ff20266922 | -10.1519 | -44.55627 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4084c7f-982c-3e93-ac6d-708b016dc81f | -15.25215 | -44.34244 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bec98f3d-e70f-3e96-ac2a-1b8dca0a997c | -13.37289 | -47.7389 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f9892f2-dc05-3c55-a48c-e2429b660897 | -10.51707 | -47.35004 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8ec29e08-1b98-37dc-865d-e3e12862e2c2 | -10.6174 | -47.45115 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d70c5bd1-1c4e-3f55-a6b6-6fd3b8110abd | -10.52882 | -47.3407 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22f2d852-c0a0-3f5b-ab2a-9b05fb19cc9c | -11.88263 | -45.48965 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58463107-f868-3645-ba7b-40e081941309 | -10.52435 | -47.34743 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc636907-7331-39bd-b051-0bbec7cb4334 | -15.39289 | -47.29015 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0244903-1c28-3ee3-b9d2-e7b67b03302b | -13.49082 | -48.10366 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac900f0d-35a9-3e48-a9dc-586e0b65e612 | -14.9471 | -46.74419 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c6465e1-f347-3b52-afd4-9bae11f9b37a | -9.08547 | -45.02847 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2028465a-03ec-3758-b81f-5c979c26cca5 | -11.87768 | -45.49792 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9101395d-1729-3ef6-86db-da69193afc22 | -11.4501 | -43.47667 | 2025-10-11 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2ac22ad-32e8-34c2-b984-02dce669a042 | -14.27833 | -45.8995 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 182faf21-2e29-3788-8bb3-7280684717c9 | -13.79992 | -45.39023 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fb3ba2f-b4c5-36ae-b7c8-c39d0935422b | -13.3356 | -48.48002 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 713fb482-e379-3cd9-8b9e-02ebfb40acdb | -10.19388 | -44.61442 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1accb716-9019-36b9-b621-a185f5d32597 | -13.41864 | -47.26377 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3012de7c-8549-37b6-8e22-04265f0a39ac | -12.75289 | -48.64599 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b51f858f-d571-3fb4-b188-d8c298d1b368 | -14.92752 | -46.75333 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77792faa-0b7d-3455-83d9-98177b0e0788 | -15.69998 | -46.62864 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a48e4e8-025f-3e0d-9737-1ca24b51ffd6 | -13.30502 | -47.98495 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d2fe173-d0fb-3dcb-b835-790a8411d676 | -13.2077 | -42.33459 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2e4ea01b-b7a4-3ac2-9174-547ab2a4a99b | -13.21726 | -42.33346 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 52d3dd60-f661-3c3b-b97a-fe557433903c | -11.53135 | -49.27969 | 2025-10-11 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7353fa82-29bf-3f96-b627-d9dd922fa07b | -13.21146 | -42.3425 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 3e8318bc-7178-34c9-8ba8-8da044150bde | -13.30499 | -47.74386 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| daf2d14c-09ab-3750-ab57-0f4480f10ac5 | -13.76757 | -45.40187 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56acdec0-e7ef-30d7-9109-5af479d5e241 | -15.32055 | -46.18895 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6848d9d0-a6c7-39e9-ad2c-98cb98e5e954 | -11.44907 | -43.48434 | 2025-10-11 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc5cdbb-39cf-3f9e-832e-45d068d1419d | -9.9334 | -59.92473 | 2025-10-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7e23a59-b138-34ce-8bb1-fbf04da50dbf | -14.44276 | -50.34705 | 2025-10-11 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb3eed4e-e01f-34c6-ae4f-868e27f6d3ab | -10.20214 | -44.61086 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e963b403-7da2-3229-a216-baf8813b8804 | -10.5467 | -47.31384 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5ea6bc4-8db2-37cb-a570-62b1daa7674c | -13.41463 | -47.26709 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 820a3aee-6512-32f3-be40-4221c9a8c9da | -12.74654 | -48.64157 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa4fbf63-bdc7-3b1a-a541-db4d28894453 | -10.20233 | -44.60805 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20249f50-848d-38bd-870f-dc99ad851db5 | -12.7568 | -48.6647 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c96477ba-f133-3776-8a37-088392fbf235 | -13.37659 | -44.34592 | 2025-10-11 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cf59698-d14d-36a6-b922-3074501783bf | -11.75588 | -43.31567 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 45e5eac1-d12f-3cea-9906-5b1bb63b3f58 | -13.41856 | -47.24018 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb47db66-6093-3f63-89f9-daa5e76f872a | -12.76342 | -48.66577 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f73d74b4-dcc9-3cfa-a325-1a3366840480 | -13.40774 | -47.26599 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e8cbb7f-0062-3c2e-9b5c-db967cd3fe47 | -10.62345 | -54.9534 | 2025-10-11 04:34:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 43066a13-db73-32b9-839f-cfb99c410682 | -9.53834 | -47.90137 | 2025-10-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1798fe6d-f24b-3f43-afcb-3c7a6d092987 | -14.94235 | -46.75184 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4579bb0-d3c0-38fb-885e-2b08dd91634a | -14.95661 | -46.75432 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f49cdcb5-0995-3282-9659-b83adadeeedf | -13.45903 | -47.70301 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c79dc98-66f8-35ef-a0e7-76d7c1da5bd6 | -13.53285 | -48.12124 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06891380-294c-3d97-9c74-2e98602cfce4 | -13.2565 | -48.01899 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b1bfe2a-964d-3859-869f-d601b24271fe | -9.53503 | -47.90085 | 2025-10-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40743116-ac91-3c85-b6f6-e6c8232fcfd9 | -12.8988 | -47.03405 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7187b7d-69a4-3551-bb07-72ba4c60ff73 | -12.14931 | -48.0135 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f444234-24f5-3661-9409-a2665643f9a7 | -12.75349 | -48.66417 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77f88d1c-ef47-3080-a36e-542438e8f557 | -13.42087 | -47.24854 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3849613f-2c4a-3740-afdf-b537a266615a | -15.91961 | -43.28736 | 2025-10-11 04:34:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README28.md)
