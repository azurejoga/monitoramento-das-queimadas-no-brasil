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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b00bfa3-5916-3b9b-b203-d8d94fd22957 | -11.80729 | -46.45153 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6a066bc6-14b9-397e-ba53-03b92bac2a7f | -13.9731 | -46.3186 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c6bf3e-a488-3cdc-a937-b24d57b0d174 | -12.80161 | -48.09232 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6964991-74ed-3ce0-8bf8-2593b3589e1b | -12.85309 | -48.08384 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf87c41b-7d37-30b4-9a83-188e522c1ea7 | -11.83168 | -46.43037 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4985269-aa89-3719-8115-dbf6982d5945 | -18.66078 | -49.09653 | 2025-08-31 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 19e8f643-9c75-3b21-a613-3eb67c19c5ec | -11.84407 | -46.78882 | 2025-08-31 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8110da-90d6-3118-b78c-cd46e1efd504 | -11.89316 | -46.37254 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ddb4074a-3a0a-3c3a-a333-ba36fc578a4b | -11.89276 | -46.72821 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b34817c-18ad-304a-a3af-8abbe467c756 | -13.17584 | -47.18992 | 2025-08-31 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd4d52f-622b-307e-bd7b-4df138b5c406 | -11.8806 | -46.72557 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d14a36d-6dc5-3cb3-bd7e-4d94bc0972a3 | -13.66195 | -45.7514 | 2025-08-31 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f000ff53-28e9-3440-a0bc-dee655011423 | -13.57684 | -46.91978 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 032aa816-ffe2-352e-80bb-e474c5314485 | -12.09028 | -44.72561 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a55e4ff2-a872-3bff-a774-f78d1696497e | -18.44123 | -47.23728 | 2025-08-31 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68158ab8-06b6-3562-af92-0c31643a4fb8 | -11.86709 | -46.48893 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f7b6e24-af4c-3b16-8d36-edab19a65649 | -14.54375 | -51.97835 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a51802e8-3453-36aa-9ef5-d43c2ef192ea | -11.8205 | -46.44701 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e0113ca4-bdbb-3c4e-beb7-4633b4f4cbd7 | -14.45777 | -42.74908 | 2025-08-31 04:04:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d512c9a6-987b-3236-b1d1-0e437fb063db | -12.39781 | -46.47224 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 990ed1fe-4275-3943-bba6-f043b53e901d | -10.97208 | -50.86594 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4743259a-4009-3610-a88d-a52c48deb7a4 | -11.77861 | -47.40038 | 2025-08-31 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b24bca08-7f05-3296-bb43-93ac5a910c70 | -16.76881 | -50.29981 | 2025-08-31 04:04:00 | NOAA-21 | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bc8b157-a03d-3ff6-a827-b3080ad9b066 | -12.99229 | -44.85555 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 872e422b-6183-3eeb-8687-8932ee2f7fb7 | -13.33308 | -43.19796 | 2025-08-31 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8242104b-9f3f-38f4-a152-b210a4478f50 | -13.48488 | -46.96396 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 577127ba-2afa-3dad-b0c4-ef60602768c0 | -16.22032 | -52.6728 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 754f2b5b-c449-3cd6-85f8-e12fe34c1e35 | -13.31247 | -46.94543 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6bebc25-8b43-3e1a-bcb4-0edb3b4c923a | -11.90927 | -46.39776 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe52ee70-8026-34a2-8b4f-b6ce09f7a745 | -11.81128 | -46.4524 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8d64e5aa-d06c-3034-a205-d73782f5812a | -13.35831 | -46.94595 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e41e152-17d8-359c-9590-b6b3a7c93f1d | -13.35308 | -51.76538 | 2025-08-31 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c266db7-166a-3cc1-8a35-bed4488b856a | -14.34099 | -51.8771 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 914148f5-4238-3122-a11e-0cd5daa5a2b6 | -11.88873 | -46.72721 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a9d6e59-3a9d-3e64-a33e-ef2cd2c3603f | -11.86398 | -46.50708 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b81b1b51-39c8-339b-b5cb-4d17d0daf4f5 | -12.63288 | -48.19962 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 699b373f-965e-3fce-80a9-c77a2bcd39c6 | -12.40699 | -46.46664 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a33c0b69-82cd-369e-b8f0-2d2c16c148c7 | -14.23273 | -48.06252 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad79f296-7cf9-3692-ab45-ffc512285aad | -13.491 | -46.83583 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2e026b1-6cbe-3141-8592-f706345c6634 | -17.62436 | -44.25594 | 2025-08-31 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cd5d0a6-5241-3be1-b193-1261acc7dff3 | -16.41024 | -45.6512 | 2025-08-31 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e3464cbd-5d85-3e3a-ba98-0e531264cc3c | -11.90542 | -46.70396 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 093e90e6-73d0-3b57-bbd6-624311466021 | -11.88399 | -46.73019 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899166c2-ec12-3e0d-844a-4d8f25c76bd5 | -11.8566 | -46.45359 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9667d02e-9950-338e-b7af-a6b1e687e0a2 | -14.03708 | -44.55994 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7918fe12-5b9b-3861-b4d3-5d9673b89dfb | -13.48434 | -46.94352 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e1b17dd-bc05-3101-9070-9aa0ebd707ff | -16.3721 | -43.03562 | 2025-08-31 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67fa009d-e88f-354d-a80d-d1a4358a356e | -18.06068 | -45.95491 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00b0a84e-c339-34fe-b9ee-cb2ff22b808c | -14.26413 | -48.06013 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ad6f2a-705f-3f94-9ab9-5f03b1e1750e | -13.5082 | -46.8321 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 162dff47-b15c-3723-91a5-7f56bd825008 | -14.48658 | -42.26699 | 2025-08-31 04:04:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43faa97f-500d-379f-9196-984d5d7854f0 | -13.39838 | -46.83724 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a28c44-bd44-3313-94bc-e859b6d52b6f | -14.99934 | -46.70673 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d6a8c54-0231-36b3-898c-ea71ff147183 | -13.35146 | -46.86795 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a7f6f50-8e03-3c8d-8331-aed9f37ee761 | -14.8527 | -42.79013 | 2025-08-31 04:04:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfecfea6-bff1-3479-b736-0c400164a7e0 | -11.89211 | -46.73195 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3664bf07-a31f-38b2-8057-720f54e4342f | -11.90257 | -46.38909 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82f64108-3d77-38be-848d-816ea4596b25 | -13.34636 | -46.98946 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecc0beb7-5be1-3896-a264-26e5d0f799e5 | -14.28257 | -51.88427 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 131f7000-3b28-30dd-9b24-fd97a33b781e | -11.88739 | -46.73481 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15c1f026-e0f6-3a7c-b8c7-10ae17d7d853 | -14.99186 | -46.70848 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6eb44818-9ab9-3542-a0df-aae38500c6d6 | -11.82767 | -46.42966 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a9cc82a-076a-31ff-b508-15840988ac39 | -15.9635 | -43.89896 | 2025-08-31 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3924761e-e9cb-36d3-8b94-b534e7d33b6a | -14.04328 | -44.54436 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8a72c5-4c42-3bb7-98c3-67405c2021f9 | -14.35279 | -51.90529 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03e7aced-18fe-392c-9146-6457d726643e | -17.48495 | -43.33418 | 2025-08-31 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9038335f-c943-3131-b055-d63caf962461 | -13.31195 | -46.94557 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1172218e-1ed6-3e75-a66d-fc71a8c4db0b | -11.85599 | -46.45713 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 518da505-1092-303e-9633-4a17aa427362 | -12.5623 | -44.7986 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f667e0c-dea2-37e5-8560-ad938c5655c0 | -10.94886 | -50.83915 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9ddc578d-14b7-3af1-ae29-8c39e6ceef5d | -13.6816 | -46.87388 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab67ae6-98d2-3086-abdf-b7f192072d98 | -13.32277 | -46.88335 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12e59f18-156c-3280-8930-6e3c75208aa5 | -13.67509 | -46.9333 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58294eff-4296-31fa-a191-6c85dfebe945 | -11.945 | -46.69188 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03579bcf-503c-36da-a203-df2444ae40c5 | -16.33461 | -51.60025 | 2025-08-31 04:04:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab8ca114-ce15-37bd-bf42-021d0b3f9dbf | -14.35895 | -51.90306 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d723a3b8-76a0-334d-8798-b7bebf4622d0 | -11.87721 | -46.72089 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad5dd317-b630-30c7-ac10-c1966d2cabae | -13.51216 | -46.83303 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8361e6f9-8a2a-3e4c-8f7b-b05023657203 | -17.2052 | -46.07735 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 980d7c89-397c-3420-a7ad-ba8a32054e6f | -11.89525 | -46.38392 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c318e312-d63e-3a13-9b89-840aa6719088 | -16.22108 | -52.66911 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b9b2fe7-3ae9-39d6-92b2-6e10cd78114e | -14.0229 | -44.53656 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b02e8d7-733f-3d82-ab45-caf64624f6dd | -14.53675 | -51.98459 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48283603-eb93-32a8-a1e7-c858d6a2ed01 | -13.3343 | -47.00999 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c772e848-8f98-3bc8-8931-156779357fd3 | -16.98071 | -49.32472 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6de88c3-827e-3c05-97e5-9284452493c4 | -11.892 | -46.36751 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a17eb34-7742-30d0-9dcc-4755612a8c68 | -14.3557 | -51.891 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0360c6d3-2af1-3955-bdb9-a1ce96f42402 | -10.24335 | -54.97815 | 2025-08-31 04:04:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fce45b2e-db1b-3dd5-abf0-d3542318c67d | -13.34806 | -46.86375 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d2f7257-9f38-3b81-a023-2cc55466005d | -10.95313 | -50.85128 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2520712a-f97b-3b25-82a3-3976ee774eb1 | -12.62927 | -48.19418 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea7304d7-58f9-3f5d-a5ca-d25655a8bc95 | -14.02507 | -42.43093 | 2025-08-31 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e4ed2a1-440f-3f9b-bdfe-137c142639c7 | -13.31599 | -46.94631 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9314c16d-9e9b-35c8-87a0-3038e185558b | -12.31631 | -45.72363 | 2025-08-31 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 846b58d1-3f08-32cd-be22-c64e7aa1172d | -18.12446 | -44.98877 | 2025-08-31 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fee172a8-6974-3483-8a0a-a385585a1ba4 | -15.22581 | -56.07288 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52c2af15-7a4e-354d-9d95-79a6c721b33d | -14.66466 | -52.37297 | 2025-08-31 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d105a9e5-30dc-3b84-a7ad-e3db36147503 | -12.87046 | -48.08812 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ae35aa9-9fa4-386e-9e0c-7f09a8585d66 | -14.33137 | -51.87057 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2037322-ceff-354b-bc92-1db270c93cbc | -10.94819 | -50.84273 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README30.md)
