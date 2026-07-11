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
| c54b9fac-3ca2-3f64-af0b-aee33f819bad | -12.66841 | -48.22977 | 2026-07-11 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adba9de3-db66-3f60-aa32-e00a96d604e9 | -13.36199 | -54.37501 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 502ff686-95bf-3b91-ad1a-c6b4be4919c6 | -10.54011 | -54.8647 | 2026-07-11 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b0b8332-b70e-3094-a1b5-08cf8bdd40e5 | -10.73762 | -47.26503 | 2026-07-11 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a835c0e2-cdb8-3be8-8482-6fe442ea1a4a | -13.38789 | -54.35772 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ceef2c0-7f29-3cd1-88d0-fa6d75c92c13 | -16.39042 | -43.85488 | 2026-07-11 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71f7ff61-73bb-3dd2-918c-544d0596ce4a | -13.96697 | -53.92377 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f591302d-bcb0-3d9c-bbfd-d9093141d515 | -13.36705 | -54.34945 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eeebfd2-b851-3acc-a364-a109394b6cec | -18.02245 | -41.83509 | 2026-07-11 04:17:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e4b01d5b-403c-376e-8add-0824beff90bb | -12.68401 | -46.50786 | 2026-07-11 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85d8457f-5743-3264-b108-af2c729638c6 | -13.25499 | -45.10412 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c6d95af-3cd5-3428-9971-6692913576a1 | -13.55226 | -39.91912 | 2026-07-11 04:17:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e97cddea-e81b-31e7-b0cc-e78ddc5e004c | -13.25885 | -45.10112 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a869af-9b5f-39cc-adc5-07d9d07b8361 | -19.83633 | -40.27487 | 2026-07-11 04:19:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e0e05328-b8d5-3a8d-b89b-bc6260de33f8 | -19.30303 | -47.44158 | 2026-07-11 04:19:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a368df4-d1fc-3b04-85ec-7d90c3b76146 | -23.99761 | -51.385 | 2026-07-11 04:19:00 | NOAA-21 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0eed2f54-781e-3a0b-9482-85c9aec795bc | -19.94085 | -41.49795 | 2026-07-11 04:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc6bc7b9-8575-331a-a14d-ebeeb1bd2e50 | -20.55889 | -43.2632 | 2026-07-11 04:19:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34d74c04-93be-3bc6-bc79-7a9c4702a116 | -18.31444 | -47.20179 | 2026-07-11 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e37ec25c-9412-3a44-9d05-5dc21edcf3ab | -18.26997 | -43.69253 | 2026-07-11 04:19:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df1899c-88d0-32e1-9f96-6eb74e05ca1e | -23.82375 | -48.70995 | 2026-07-11 04:19:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c72ab45-d953-35f8-a8cc-60d798a83d1f | -22.23024 | -56.69603 | 2026-07-11 04:19:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d7f1159-f59b-368e-a323-e5dd3ea827b4 | -19.1942 | -46.2335 | 2026-07-11 04:19:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49fe3413-e837-38d3-bbb0-8eb4106fcb6d | -18.2694 | -43.69643 | 2026-07-11 04:19:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b51946e-de67-3cd5-a24d-fbbc45f665fb | -20.35314 | -41.51779 | 2026-07-11 04:19:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2c1bdb20-c6db-3d37-8b4d-713398c7f0d3 | -23.82038 | -48.7093 | 2026-07-11 04:19:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 428453bf-fcd7-3324-ba0b-b0204463ed68 | -20.35352 | -41.51888 | 2026-07-11 04:19:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d4f01ab-10c3-3400-a64c-471def4cf15a | -7.01249 | -45.41533 | 2026-07-11 05:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58097f43-08de-3b74-879c-f23b12adb4fe | -2.9643 | -48.99023 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 021ed484-7a75-3e25-a3bd-7096e3b17d8d | -3.5479 | -54.71808 | 2026-07-11 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2031ecc-2037-3955-b2b8-89116d763f6e | -6.08093 | -44.00519 | 2026-07-11 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ffd621b-7616-3e82-b4ba-b1c22b76987e | -5.82691 | -43.48551 | 2026-07-11 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29e68be9-232e-316d-b213-7f0321badea3 | -3.20925 | -49.06333 | 2026-07-11 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6f39eb1-2319-3f53-b9e6-8100706cabe1 | -7.0127 | -42.77737 | 2026-07-11 05:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5063a7cf-1daa-3570-9b02-ae0082370e30 | -4.33899 | -47.76657 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57557fc5-f472-3bef-af1f-360902145151 | -2.96708 | -48.99158 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c1dc78a-e396-3fb7-bbb2-63c9905c8aea | -6.48316 | -42.22273 | 2026-07-11 05:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b96fbf9c-42f2-341a-b954-95a7a5d001ba | -7.01353 | -42.77107 | 2026-07-11 05:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 767e3889-bbaf-3577-b399-972f0ef7cc65 | -7.00662 | -42.77002 | 2026-07-11 05:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0cc6566-7bfa-334a-ad43-e12ccfc56401 | -5.82839 | -43.48164 | 2026-07-11 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0e0a832-18b7-3906-b796-61a435a11fe6 | -2.76585 | -48.57568 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 323a14f8-fff5-3ad1-bfa3-3661f37d6f46 | -2.77031 | -48.57635 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33cfa19e-96c5-347d-bb67-b339277431cc | -3.97926 | -48.43243 | 2026-07-11 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b285839-bf81-3926-a573-b432f3a01492 | -5.82767 | -43.47993 | 2026-07-11 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c511f493-77dd-390a-8e53-45fd5a5eee01 | -7.01047 | -45.41765 | 2026-07-11 05:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f56ab76-0453-378b-9f26-f430a4b0de6a | -4.8176 | -42.97852 | 2026-07-11 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6bbfe3c-032e-310e-bde7-1fc78cd44460 | 0.1966 | -60.49938 | 2026-07-11 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83dc2e69-a5cd-37ac-8138-22ae078d703e | -1.87861 | -54.68145 | 2026-07-11 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d68cbb9b-b4b7-3302-b4cd-50717f7e8623 | -6.08181 | -43.9987 | 2026-07-11 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b60598f0-b237-37b5-9d9a-6fc843fd212b | -4.34726 | -47.76943 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d8379914-7c19-3513-9e4d-f0356889e4c2 | -3.97997 | -48.42775 | 2026-07-11 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 111a9990-7817-3dfc-8ec4-024d78426412 | -2.48597 | -47.09243 | 2026-07-11 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8cfb161-de86-3d21-8202-474fea49043c | -6.48223 | -42.2296 | 2026-07-11 05:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b58eaf9-6309-3343-8f72-d12701a9ed5d | -8.11247 | -47.57866 | 2026-07-11 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a705854e-1cf5-3721-b422-53fdd766022d | -4.61389 | -49.05219 | 2026-07-11 05:08:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f74ba8d-d5d6-3e9b-ab6a-7835cf8a1243 | -4.34321 | -47.76333 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bb601c0f-5d15-338b-8685-3726cb09c7b8 | -6.48756 | -42.22123 | 2026-07-11 05:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| be39d2e1-4759-3ecb-bb23-ebdb80c79c72 | -5.41786 | -45.29482 | 2026-07-11 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| caacc405-b926-300f-898f-6ebc984702c1 | -2.01816 | -47.57264 | 2026-07-11 05:08:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6932a358-333e-3e75-8439-08e052859bf4 | -2.96273 | -48.99092 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03895d1a-c2bf-3a63-8ed8-418686ed5fe8 | 0.19725 | -60.50352 | 2026-07-11 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4279019-9fab-35b1-ae8d-6b420611a69b | -6.49552 | -42.21557 | 2026-07-11 05:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 868b2222-8924-3d1b-bf35-0c5aaaff1c4e | -4.343 | -47.77264 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cb16481-5f89-343a-827a-c6b522778a3d | -4.82015 | -42.98093 | 2026-07-11 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43428cf2-4ad8-3480-87d1-fa176acfb0e6 | -4.821 | -42.97507 | 2026-07-11 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4f16007-5935-370e-84f4-f42a3d34ca3f | -5.56626 | -43.82853 | 2026-07-11 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b2e1b76-2625-389a-af96-d96c52fa1162 | -7.01189 | -45.41959 | 2026-07-11 05:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d9a9062-d18f-3426-8057-d59176ae73c0 | -2.80284 | -48.59338 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ade756-cceb-32a3-b52f-7bbc05f0e3c7 | -7.01187 | -42.78363 | 2026-07-11 05:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 80cc9741-8877-3d95-8cf5-b6d9f7148c54 | -6.48674 | -42.22757 | 2026-07-11 05:08:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d55c4280-fdbd-375f-948e-74e2f21afb5b | -4.36688 | -55.77152 | 2026-07-11 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cdf9d3c-0e95-3166-9353-de21802e5b04 | -8.11766 | -47.57929 | 2026-07-11 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 727001e5-c2b4-3316-8016-a036c678bba3 | -7.0566 | -55.45771 | 2026-07-11 05:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10806b9-e226-3b84-9e8d-37c4b510633e | -8.11626 | -47.57779 | 2026-07-11 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63913b09-4403-3a63-b6ae-3b67d78a666c | -5.41845 | -45.2907 | 2026-07-11 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1214c125-bc9a-3fd5-9cfc-1d3bf3ecf705 | -2.80391 | -48.59495 | 2026-07-11 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84f3863-417b-3b8a-9674-8035a2f1aa0e | -4.61834 | -49.05278 | 2026-07-11 05:08:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6eb41d3-402c-386f-9f1b-5e775fad3004 | -4.34382 | -47.7673 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 0e23c899-92b4-329d-85ee-9de7c6bcfa39 | -3.2136 | -49.06398 | 2026-07-11 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0aebbb0-7d92-37aa-b84b-598995d64768 | -4.34243 | -47.76866 | 2026-07-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bffdf68e-49f7-3b7b-9d6e-90d676e0b19f | -10.38343 | -49.58454 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e367cb4f-9285-31e2-adc9-35b9d5fc5e2e | -12.45681 | -49.5838 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5cfe6c20-5cef-3aa7-a400-3fa03f30eaab | -12.46083 | -49.58571 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2513ec00-bab2-3a85-8076-ea0122cf95d7 | -14.74242 | -48.19989 | 2026-07-11 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25bc4ede-03ed-3a30-b202-55b8560fc850 | -12.68812 | -46.50839 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c87c42-cae6-3f31-9a8c-4fb14096eeab | -10.54074 | -54.86706 | 2026-07-11 05:10:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3f0ae1-4fc1-36b5-8574-df29bb55c8e2 | -13.97905 | -53.92698 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13499d3a-4a6d-3b08-8576-182454de46aa | -8.72486 | -47.84161 | 2026-07-11 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84d01e67-ccdb-3304-92e6-17096546db5d | -10.3841 | -49.5796 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fe52d3b-faf4-3868-be83-00d9baf642bf | -10.12329 | -50.17537 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 709c7409-e414-3a7b-b03a-912d4f90a4de | -12.82328 | -44.34533 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e0525165-105a-3a46-ab44-8a177d92daff | -12.45199 | -49.58321 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 51a11f67-fb31-358d-a1fa-7248fdc6a8bf | -10.09528 | -47.98238 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80f69e5d-16db-3077-b57a-7bc83b368d66 | -15.68341 | -47.5138 | 2026-07-11 05:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a77727d-a465-3efd-b748-a9026bfcdba7 | -12.68116 | -46.51645 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5356d49a-5c0c-3e65-b3bb-4b86eadf7292 | -10.10091 | -47.97977 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17a62655-a212-3d69-83e7-86cec0e6d1ee | -12.84896 | -44.36087 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2f784de6-f14e-3e26-a1d0-c7fb81ee8265 | -10.37877 | -49.58385 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6050f0a4-3aaa-3894-a132-7573ec2d52ba | -15.22718 | -52.68581 | 2026-07-11 05:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 313fd653-f319-3efe-859b-745fabeb4f42 | -10.10202 | -47.98039 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
