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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f55e697c-b67a-3dfe-8471-737be415a97a | -14.43896 | -46.50691 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 028eee5a-2f07-31a8-b6de-3166881c2a52 | -9.3955 | -54.68361 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff8ed678-ef1d-3020-b304-aa3671320f62 | -12.2576 | -45.2899 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e656264-69b5-32dc-a49b-2fab4bfc3b45 | -9.18269 | -44.7661 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c4169c3-28c0-35d4-9557-3c919469d8fd | -9.39271 | -54.69884 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac196d1e-f63a-3177-9bba-00d74eff1ea2 | -8.85037 | -45.43149 | 2025-09-20 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa3f26f-7c86-3cdd-945f-1a0a632ea59c | -16.31244 | -43.06421 | 2025-09-20 04:27:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e8e0f79-756b-3a39-b5be-5934790dc2aa | -9.28334 | -41.04899 | 2025-09-20 04:27:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67f85ae1-286d-3bee-b0aa-fe4615d9c4e6 | -11.67436 | -41.74632 | 2025-09-20 04:27:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb33a3a4-f468-37d9-8e31-5713c6d3ff7a | -10.67089 | -46.4358 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff7b3035-7632-3598-a9ef-2e67abfbf273 | -14.7305 | -42.37054 | 2025-09-20 04:27:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b7c2ef6a-093b-3dc4-a89b-10fd856d7a9d | -9.39457 | -54.68866 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f10477e-3fd0-3e48-84af-f9bc35457fca | -14.44574 | -46.50799 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c1eba4eb-f68c-3e30-af81-d5de8c5031cb | -9.02181 | -44.88332 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d616b8a-34a1-3c43-93b3-489bf6dbae38 | -14.90643 | -41.65686 | 2025-09-20 04:27:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ac97711-410a-300e-b8bb-85423d17e65d | -9.40503 | -54.68518 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d41ec52-4a0b-35f0-9d80-924e14bd8978 | -8.1931 | -49.66924 | 2025-09-20 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 044318ed-3781-31f5-83a7-4570e43b815f | -12.09197 | -44.81022 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83d25c3a-ecf3-39a8-b41e-c1c483b9ab3d | -14.7268 | -42.36583 | 2025-09-20 04:27:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24d0f212-d243-36b0-9ef1-1182f712e8ec | -12.14518 | -44.9409 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe48114a-29eb-3f6d-8102-f09123638645 | -12.85442 | -53.00536 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5e9445d4-a232-3bda-83bd-c9658e9813f6 | -12.07483 | -44.82819 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0500ad78-78c8-3526-ba61-cbcf182e30a1 | -9.12246 | -44.65525 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3991456-10a4-3aa3-afa1-9a01fba37132 | -11.64656 | -52.86312 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc3fe118-1c00-3046-bdb5-b14f65d6cf14 | -9.01955 | -44.96756 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7aa49ae-aff5-33b5-8c1e-dea50e464b94 | -12.73185 | -47.79615 | 2025-09-20 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e84be52c-b744-3091-9948-5d7a271f2279 | -9.02412 | -44.89124 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5751167c-7dc9-331c-a2a4-0c24af26ead2 | -13.07932 | -42.14058 | 2025-09-20 04:27:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57cdb20b-9772-38ad-8b57-b405ad40ab5b | -10.26031 | -48.04107 | 2025-09-20 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec320909-6406-32a2-b905-3d79fcdc6cfa | -14.72628 | -42.36991 | 2025-09-20 04:27:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4946089f-e896-3040-8f93-9a5584fe4f0f | -9.18614 | -44.76666 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 208b8a2b-e3f2-370f-bf9f-e5e976195b0a | -10.6059 | -49.64514 | 2025-09-20 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc2f4448-6c57-334b-bf74-87666aa91c2d | -10.88042 | -53.74809 | 2025-09-20 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a565dc3-8150-3d35-880a-d63d676012c6 | -8.62858 | -45.30146 | 2025-09-20 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04a6e2b5-e5f5-3d66-bbb4-b96f17deffc1 | -12.07542 | -44.82419 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 831aa8ce-e88f-316a-ae10-3fe111763c81 | -11.63846 | -52.86162 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ec02b2b-13f7-3ea3-be99-2fda29d92065 | -9.39821 | -54.69252 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5647a385-9b39-3750-9044-3b25bef7907e | -8.19243 | -49.67329 | 2025-09-20 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e5c5a94-65de-3a92-a330-caf760051490 | -10.79978 | -44.0838 | 2025-09-20 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99db362c-9185-36f5-95c2-63aaced6db20 | -11.28223 | -47.41047 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f31e9bb9-e19a-3ea6-99d3-7a666ec13912 | -10.65324 | -44.24016 | 2025-09-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7e95941-d813-3ce1-9c3f-95c6cd526215 | -12.14105 | -45.01802 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd7c1a0-9889-37d3-bc5b-9254d3e0ce68 | -9.40863 | -54.68904 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20a90049-d76d-356a-b230-bc0c396b7dff | -10.8468 | -42.8061 | 2025-09-20 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 142ec1de-3b6c-3daf-8dd4-bc35b3b9a663 | -9.39346 | -54.69165 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0f1a7aa-541f-313e-9011-a3c0d9cc611a | -14.9038 | -45.18705 | 2025-09-20 04:27:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a86244a-a72e-3e79-957f-0b459cf16aa7 | -10.88119 | -53.74385 | 2025-09-20 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13803aff-1aa7-33f4-a6d2-de247e1e9f83 | -14.27212 | -54.60836 | 2025-09-20 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ee94ccd-2a0e-376f-a31a-2ba49b07847e | -8.71645 | -47.06548 | 2025-09-20 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da697ed5-a0ca-3422-80db-8914ca1e2f45 | -11.28883 | -47.41153 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca5dbc20-2062-3286-a72f-6973433158a1 | -10.87424 | -45.43217 | 2025-09-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e37040-c9dd-370f-9459-cbcef8a93006 | -8.42968 | -46.81028 | 2025-09-20 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51105628-3e9c-3873-8aca-9f75ac2fc5be | -12.07601 | -44.82019 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c4a0807-8403-3be0-b512-6644261c5b74 | -9.40885 | -54.69113 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb0c706e-5467-3ae0-a9fc-2431b468bc87 | -10.0393 | -46.25344 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17fbd02d-66bd-3034-89ab-87cd9e8ab4d2 | -8.96548 | -45.00104 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 484b6d6b-bcb7-3094-b9b5-78c6262d2cf4 | -12.16213 | -44.94823 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a696222-c5bb-3774-a4b5-2c4866876fb1 | -9.33066 | -43.70085 | 2025-09-20 04:27:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6542dcf7-43ae-3763-9a20-a6f300d36cc4 | -9.39257 | -54.69674 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2d0e185-cbe2-3ce4-a2a5-127c65120a1f | -13.78853 | -44.3317 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ae432bc-8da6-389f-8297-a605c303ced4 | -9.02013 | -44.8944 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15b8ce71-a490-3bfb-9a88-2124f8a34c8b | -9.40297 | -54.69339 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1959173-cc59-3e47-b359-7db4e4090932 | -9.90379 | -59.59918 | 2025-09-20 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da2e6e61-07a9-36e3-9a94-42fc0a7adbe9 | -8.8771 | -50.14244 | 2025-09-20 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88edd260-b103-36c2-8906-9429bc1222f3 | -11.33933 | -43.47227 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27c72714-bb2f-32b3-9ae9-c87ec1687d80 | -9.11437 | -44.66195 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62d40d4f-78d5-3079-9c4a-e0cf9f08623d | -11.33868 | -43.47692 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 598b352c-cc22-34e2-87fa-6ff18ec7ee2f | -10.27732 | -46.45309 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d47bfa48-f898-3880-b382-065255fec3cd | -10.23594 | -54.19233 | 2025-09-20 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71ad7058-0ad7-3609-8749-b892d30108b9 | -9.11554 | -44.67786 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cf2a0f80-8f52-322d-be4f-b017f3cacd33 | -11.62971 | -52.86381 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cea79355-2004-3334-93f1-56a542fa51bb | -14.27133 | -54.61269 | 2025-09-20 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 060dd3a2-3d4f-33c6-ab9f-520dbf5001c0 | -10.03629 | -46.2525 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef32389-b5e5-30a0-b346-12803c398f8a | -10.27374 | -36.34111 | 2025-09-20 04:27:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f421eef1-0e94-31f6-96ce-e266c260c8d5 | -14.46723 | -44.8616 | 2025-09-20 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f637ff81-3ecb-3fb1-b341-7f1f5c603c68 | -13.22762 | -57.13043 | 2025-09-20 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d196e78-2416-3b26-9835-a1e5a9b9987e | -14.44177 | -46.51131 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46a08efc-d1b3-3786-a03b-3316bc9c978b | -14.44235 | -46.50745 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c48f310-01ce-39ab-ad57-7623759e34eb | -13.78483 | -44.33113 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d9271754-24e5-3ff2-a192-1eee0f6270ac | -8.9696 | -47.68076 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 051984e9-6e77-3955-b9af-3bb52a2f3ad0 | -8.60843 | -45.34296 | 2025-09-20 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93781a13-a0b3-38c2-93fc-855c053fc7cd | -10.04752 | -47.25424 | 2025-09-20 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7afce8b3-5e76-3298-bc01-f875b6c8a551 | -9.40409 | -54.69033 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c053ab6-8b66-3cf1-a8b6-a767688322af | -12.08011 | -44.8415 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83413b97-edaf-3199-a22b-895dfc931e06 | -9.40026 | -54.68439 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3f1299d-b3c6-30b1-91c1-dd436863c7e7 | -9.01105 | -45.04636 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9de1d56d-eb85-392d-b416-17d29e7755d7 | -11.64314 | -52.85875 | 2025-09-20 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25b68574-1a03-39bc-b498-e9a7e4642335 | -9.17677 | -44.64796 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75e82018-6e45-3ec5-ba85-a241a00a111f | -8.19665 | -49.6698 | 2025-09-20 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5372445-2440-3e8b-a0bc-8d6738534fa5 | -14.43838 | -46.51081 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e2fd4e1-5aca-365b-aa48-e5dfd264fed5 | -12.14868 | -44.94162 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23706af7-c013-3222-80e2-4a47fdf81975 | -11.28556 | -47.47542 | 2025-09-20 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68767719-3a81-3f7b-b2cf-66e0ad7e71db | -10.4901 | -42.41459 | 2025-09-20 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93831611-4e07-3bd9-b88c-d87070f8ee24 | -11.66948 | -44.88118 | 2025-09-20 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64f7fdfc-c48c-342a-8dca-a1092e5a4eea | -11.42853 | -43.52644 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa6f4fb1-4913-3bd5-8766-ace50bc3b12d | -12.07954 | -44.82078 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a802e4d0-fc7a-3e1d-a550-d3b63dcda7f3 | -13.7082 | -44.6313 | 2025-09-20 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7da34965-0335-3a38-b473-d3f3aa3f4de7 | -16.32941 | -43.95923 | 2025-09-20 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43cddba9-f5d7-3c1b-92ae-44ed4803c647 | -9.11783 | -44.6625 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ab9459e-74c8-3469-8775-4e0810da9aee | -13.22892 | -57.12377 | 2025-09-20 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
