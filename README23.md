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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a89ed86f-f674-3509-a479-d8cd07e4290e | -8.49555 | -44.73175 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33ec4bbf-3df3-33bc-b78c-e0adef2cba12 | -6.73397 | -42.08119 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce63fa25-909a-3e25-9ce4-3f1adbf5cd77 | -8.23905 | -43.35485 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc3bc7d5-e9e5-3909-ad3a-8800ae6ce4c4 | -7.51569 | -42.16558 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 480392aa-202e-39ed-8588-5cd9f7686a40 | -6.94427 | -44.41935 | 2025-10-13 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61138582-d12b-31a3-9e1d-55203433a25e | -5.21781 | -50.95473 | 2025-10-13 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8d09b56-4878-3570-98aa-ed20a4a42846 | -8.23562 | -43.35433 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad2a0e7a-62f3-342e-94f0-859f94e82c49 | -6.78933 | -44.52734 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4701ea37-cfb7-33c2-8dcf-cb66f9058445 | -7.34446 | -44.08701 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac4776f7-8c09-3aef-8ce5-af1d28c7ce9e | -6.58291 | -44.37677 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bf23f36-cd38-3ec0-91bb-baf22da92910 | -7.14183 | -42.49741 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e7b31188-ac3a-351d-b185-c15c669cb376 | -7.43327 | -42.97037 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c0b9efb7-1614-3155-a302-33f362e42ee7 | -7.15957 | -42.19463 | 2025-10-13 04:23:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5fb66b8e-36a5-3058-94e7-bd2fbdc4d39f | -15.02637 | -48.75077 | 2025-10-13 04:25:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cd59ea2-0139-3ac0-9715-3f2d70df21a3 | -13.84801 | -45.54264 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5824d9db-3823-32c9-8a58-621a1f7eb7d6 | -13.49772 | -51.31281 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e460866-3d16-3917-9f6f-32ad14c76656 | -13.8318 | -45.53635 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51b4b57b-3ba6-3f05-96d7-ed11dda19c07 | -10.97924 | -59.02042 | 2025-10-13 04:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9b56a7c-a49e-3ba8-a3cf-a9ab9f121d81 | -14.80711 | -48.39271 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d3176d1-6ede-39d3-b27d-954626ab605d | -13.82169 | -45.46791 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b83c6cd-60f5-3684-a488-c8fa138559c6 | -14.30674 | -51.54503 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b246c5cf-c1bb-306e-a1e9-2894ffa8bf37 | -12.7645 | -50.67659 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c0de5903-f604-3e9f-ab97-a54c3d18529f | -18.40372 | -46.39162 | 2025-10-13 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ace34934-2cdd-3277-8fc8-e77642208d87 | -15.79946 | -42.51599 | 2025-10-13 04:25:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4db807b6-4608-315b-ba82-33efa4d15602 | -12.75849 | -50.66528 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5beafe13-10ae-3578-9b46-ae6f914ed107 | -15.65937 | -43.90203 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b9e1586-d0c4-33d0-baa9-a56ea7369ec4 | -16.47802 | -49.67536 | 2025-10-13 04:25:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f94f3ebd-e8d2-33e6-8465-7d047734f214 | -12.93845 | -46.99832 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4b8097e-4662-3139-9845-1a76f8d0b223 | -15.66234 | -43.90678 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25eb357a-199d-3248-9bbd-fd15e66deceb | -14.264 | -51.5027 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e821efde-e3af-35a6-b3a7-f1087f88fe16 | -14.21863 | -51.5187 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eb025a28-fb2a-34ec-b51e-5ec4d8b5a085 | -14.25641 | -51.54507 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f4655e0-4231-35cd-9626-f231d99dac87 | -13.83571 | -45.53325 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 681ff4dd-95ce-3951-978b-6aec05cd5a9c | -15.6642 | -43.90544 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9a7b560-05fa-3625-8ddc-610c314179a1 | -14.44611 | -47.95253 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb79aac5-006e-3a7d-a42c-ec6360a943a0 | -13.84186 | -45.53795 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f4ed4df-2664-3475-937a-720bb6d72c52 | -16.12646 | -53.96601 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 26204000-524c-3f6d-a0e1-7ae1039e6751 | -13.24995 | -47.76668 | 2025-10-13 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d83f05d-2532-33c8-b949-4d51cd4af372 | -17.89295 | -45.02235 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 974621a0-9835-38b9-bdad-cf3dd2228382 | -15.66062 | -43.90485 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d91c19c5-f691-3433-ae23-0869f1920ab8 | -14.27103 | -51.5095 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db6c82c2-d936-35da-8fc4-da2b2bb679bc | -13.83851 | -45.53741 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f2da01d-fdf6-318d-9772-3ea1720ef6a3 | -15.84465 | -56.75412 | 2025-10-13 04:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 374d84ad-bced-307c-9edf-464d197b7cf6 | -12.95354 | -46.98987 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc5a5847-57e4-3f06-b8a6-e84da14a1ac4 | -12.74319 | -50.66062 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea0c057b-937f-3cac-8837-c014f67aa6b2 | -14.29424 | -51.54129 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd9edb81-8bfc-3e60-b00d-b015d10c63dd | -14.21158 | -51.51188 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6cf1d9a1-3de6-332e-9a60-5598131cc9e6 | -16.48085 | -49.68009 | 2025-10-13 04:25:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c511bf26-efbe-3a7b-b3eb-60ae7e01dd2a | -15.84538 | -56.75058 | 2025-10-13 04:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43cf0cd-d282-32fa-920f-019319f036c0 | -14.31085 | -51.56776 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd3d0fbd-a0e1-384b-a4ac-3fc17e93dedc | -19.79544 | -42.37067 | 2025-10-13 04:25:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2b358207-704c-376f-a942-a7866e31a6a8 | -16.19441 | -43.67434 | 2025-10-13 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7ad3874-b08e-3237-b51f-302d79a6160b | -14.23628 | -51.51931 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e703485-6a59-3587-8861-7f9a7428fea0 | -13.85525 | -45.49562 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b58df5cd-74d1-3d37-94ae-69000e6b00ad | -14.24938 | -51.53824 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c7581dd-4944-3ee7-97d7-6e3e5b32063f | -14.80772 | -48.38902 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86cea653-0c66-360b-a20e-882c1234451a | -13.82786 | -45.4949 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 652d0254-796b-38b2-a828-fa575c42af71 | -11.74288 | -54.72218 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bb54700-0af0-3f1a-bd61-981378439205 | -13.86754 | -45.4828 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0080e240-9dec-3878-8ed8-750612f26295 | -13.82731 | -45.49852 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13905d93-0dd8-350d-bfe0-9bd71f47d04d | -13.75012 | -45.65603 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71e7ecb5-340e-36fb-a4fc-4324b94a9984 | -14.19375 | -51.51945 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af799333-1b68-353a-b47b-d9ca49460dac | -12.92696 | -47.04816 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8810a728-9852-3686-ada8-32be92883498 | -14.29916 | -51.53674 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ce062e6-bb12-3728-9d57-abf612dd42e2 | -16.31386 | -43.10009 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d03ed7-a3e3-37ce-8c8d-4cf56113ca4b | -13.8441 | -45.54572 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c07f0182-c6ef-3a25-bdaf-7a18f3061b91 | -16.31763 | -43.10062 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db560dcc-0feb-39cd-aee8-ba0bf4bc69f7 | -12.74773 | -50.65821 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 809def14-b463-3283-8e54-50390462a907 | -13.85633 | -45.44391 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b18a541-f17b-3ee9-93e1-d91a937d0aeb | -13.88208 | -45.47775 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae62eda7-3399-3c9c-98f6-c88323f0baf4 | -13.76182 | -45.64693 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c10cef34-1a9a-3022-9d90-14ef41d7ceb9 | -16.30195 | -43.0773 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a01b7450-d3a3-3ecc-bdc4-47b3cb2eb16a | -13.6413 | -43.61908 | 2025-10-13 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8cfa50a-d29a-3f28-bc1f-4fbe1fe27c08 | -16.35072 | -42.38396 | 2025-10-13 04:25:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ed493a4-4e1d-3026-ad9e-3a8f3e4ee29c | -13.84463 | -45.49764 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39766263-67c3-3682-ad7e-c567723985b0 | -14.86662 | -47.12812 | 2025-10-13 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7c1e375-05ef-3657-9c8a-264c39c90486 | -16.48083 | -49.67962 | 2025-10-13 04:25:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7972356-3d29-3d29-8899-4002f0a9e70f | -14.24027 | -51.52007 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a45d212-301f-3bd3-b7ea-3e654af67441 | -12.75461 | -50.66457 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e940c5e-6dcf-3114-a365-cf13ffcfd507 | -15.6648 | -43.90125 | 2025-10-13 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4656c2ab-2506-36bb-a3de-cda46c0187e4 | -17.87897 | -45.02011 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3b0583e-b978-3866-8a3d-60ad284481c1 | -11.87521 | -54.67498 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26d6cccf-6c6e-3ba6-9547-acc7dd484fc5 | -14.20932 | -51.50874 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1ced989-744a-368d-80de-cf682effe149 | -13.75346 | -45.65658 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc888839-c6a1-31df-a53c-e8bf03fe9529 | -12.77226 | -50.678 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 949c2696-976a-3b25-af32-40367b4345a2 | -11.73833 | -54.71808 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e77f1ed1-b6c4-386b-b7de-882b1320c845 | -13.65177 | -43.34924 | 2025-10-13 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0dd5d5ba-ffff-3f51-8086-b863c84d610e | -12.95848 | -47.00179 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93990d54-fcd3-306d-a2e7-8a6c6d293d97 | -14.26002 | -51.50195 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a550073-a23c-323d-b848-80183e6b356e | -14.21331 | -51.50949 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04422593-c24d-35d9-8e81-0273047d3db6 | -11.73775 | -54.72119 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 435bf39b-4d00-3009-bb43-1cebefbb6bca | -14.31073 | -51.54578 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c6e719f-eaa3-3013-9e41-f66054208ff0 | -13.65538 | -43.34977 | 2025-10-13 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bebedf93-95ee-39cf-814c-24aee496d030 | -14.21464 | -51.51794 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 33631e2b-17a4-36ce-af24-4f3beda3c299 | -13.85582 | -45.51427 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a772eef-de94-38ee-bb62-95dc79e7fc6f | -13.82395 | -45.49798 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1548cb61-1b1d-3202-b86b-d8003c5ab160 | -13.83962 | -45.53018 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1474924e-89cd-3375-98ef-47339667bcdd | -17.87955 | -45.01611 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffdb882d-cb6e-38e3-9e9a-ff15fb6d3195 | -15.027 | -48.74697 | 2025-10-13 04:25:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ee554b-f10f-33b7-8680-d36689f3a4a5 | -19.86707 | -42.44993 | 2025-10-13 04:25:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
