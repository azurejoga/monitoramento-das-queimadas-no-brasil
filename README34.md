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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0364cef6-f3c5-323a-8c74-3ed24e2dfdaf | -13.447 | -46.88724 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba42f9a8-28b2-3a12-9d1c-fdc935861820 | -11.18705 | -55.0274 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e3fc7b-0d61-3882-b3ad-fdab67648fa0 | -22.01255 | -44.28971 | 2025-08-25 04:17:00 | NOAA-21 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a154032a-eb40-3719-89c1-c4bd26f68365 | -11.46474 | -55.47165 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 633c2ba9-7cb2-3c0f-9200-e82c29b81db6 | -20.3735 | -46.75854 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab66a088-d870-3719-a72a-40c03281c0cd | -12.74933 | -48.10778 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72b60142-eabf-363a-828a-391ac593fe01 | -14.70612 | -55.92888 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19473a86-7bb6-3a86-ba86-5584fd5b1fea | -14.71188 | -55.93001 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7fe206f-f086-396e-aef4-2927cc2e75b4 | -11.60658 | -46.2339 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 116ee6c5-557b-39f4-9b3c-65c03578dbf1 | -14.65291 | -44.07806 | 2025-08-25 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc017ff2-8809-31ad-802c-63e0c676d8ea | -11.63188 | -46.2336 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88f7c386-6bbe-3f89-8773-126a2cd130c8 | -10.71743 | -47.12439 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26dd9203-074c-35e2-941b-db46d846dca7 | -12.18286 | -47.20135 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21a61f30-98a7-386c-af39-d1951c33fe48 | -13.43895 | -46.89342 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de0bcc8a-52b1-3fb9-b78c-de2c8412ad40 | -20.37524 | -46.74752 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f492a298-ade6-38f1-8aa3-d7b59a3c296d | -13.43546 | -47.02245 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ebd454c-6199-38df-a0e3-ff4adae2da60 | -9.47422 | -57.83227 | 2025-08-25 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08e291b7-5a2b-34c0-804b-71d0eb8db9e4 | -9.84016 | -46.46133 | 2025-08-25 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c69e97e5-22cb-3e9a-bfd3-7e84c29c3731 | -10.71111 | -47.14027 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1850c4a-9999-3189-a854-2f34b473fa3d | -11.0947 | -44.77131 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35bb083e-937a-3a37-97a9-0f202ff2a292 | -11.92803 | -46.74163 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1dac1c3-2445-3df8-96f8-918ecaf3d2e9 | -22.69259 | -47.34451 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cc0a9be-00e1-32a6-8c7f-6fdfab783335 | -20.27439 | -46.65408 | 2025-08-25 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3bbef57-d484-3354-8cf1-7b40f9b1d1e0 | -20.92752 | -46.84764 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdc42593-72ac-3158-923e-e58193d44798 | -22.00088 | -46.59197 | 2025-08-25 04:17:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f52571d9-2e7f-3eb7-ab70-272cf95ae30d | -11.93211 | -46.73836 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 889deb29-c5f5-3776-ab5e-ae455f95535f | -11.63649 | -46.22675 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82b425b2-8239-34da-92d3-a8eb7f3a2b0a | -22.54062 | -46.81573 | 2025-08-25 04:17:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| bd6c4ef8-464a-35f5-859a-12a5e0988075 | -11.62046 | -46.23938 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fd02dba-0bb7-3cee-b13a-13ecef01452e | -10.98706 | -47.3997 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2688fe3a-f1e5-351d-95cf-4eb9ec5005f4 | -13.43533 | -46.91555 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edeff5ee-4cad-39a0-8fe2-dce84db7fd11 | -20.37737 | -46.75547 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20bc34e6-b53f-32a9-a1ef-8ec882b95d18 | -11.18126 | -55.02634 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19da3277-9ec9-3f9f-94e9-c0ed1bb45ed0 | -20.3583 | -46.72533 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 305e37bc-dcff-3d0b-b84f-42297f9ab8e6 | -13.43837 | -46.89702 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11e437ed-a945-3b6f-acbe-2059f8eededc | -11.60475 | -46.35603 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93e34372-2fb8-3143-b569-e4cc1b05f542 | -11.473 | -55.47313 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d17c1b07-b175-361d-b4f2-03d1228c9fed | -14.26165 | -48.04016 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45357955-345a-342e-8083-0e28c4e07ac3 | -19.71816 | -49.13033 | 2025-08-25 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d30f677d-f3e3-30cd-a119-dec3941b4b66 | -13.45913 | -46.87752 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97a35515-d0d3-3287-a861-e8db24a78553 | -13.62018 | -48.1588 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 958afd76-7264-322c-a3df-96b8f81d62d6 | -9.69357 | -48.34221 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 882269b6-900d-39f8-bd5f-f2f1c76242ce | -20.02555 | -45.5558 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 028ccc20-047b-30bb-9e69-f432c5f1d514 | -13.66673 | -47.97174 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2def0e5d-e770-3a7d-9e7e-fadc693fb806 | -14.3867 | -51.94435 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3acaef67-7daa-38fc-a936-f72fbc25fd14 | -13.3943 | -51.81063 | 2025-08-25 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ae1de2b-fbb8-3b7e-85a3-ea177a549b1c | -20.02611 | -45.55209 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8304900-c3f7-3278-b4e4-141b480ef3db | -14.42557 | -56.46297 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c5057d7a-0f4e-33d4-965d-77155825a833 | -13.43377 | -46.9036 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae25b91c-32d9-3033-bf7a-f604c6896588 | -22.53731 | -46.81514 | 2025-08-25 04:17:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 773030bf-b5d9-3985-9d7b-b95547ab9ba4 | -13.48159 | -47.0181 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e96f00-5da1-310e-b9ea-924e50cc8977 | -10.8394 | -46.41357 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a3f3cd0-e00c-3b7d-901b-399ab97049a7 | -19.96881 | -47.52209 | 2025-08-25 04:17:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f765ec0-0c3a-31d0-bf6d-0ee93bd120e0 | -20.36995 | -46.71643 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9786e22e-59c7-3776-b373-b6f2cc82028e | -15.10654 | -48.69818 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 923cf4c7-8b6c-369b-bfea-eeb77e6d350c | -10.71535 | -47.13675 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bccc31c-e618-30d3-ae36-4f5057bc798c | -14.43376 | -56.47143 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa4293ca-4cbe-311e-a9e5-293b763dd775 | -20.2956 | -47.18328 | 2025-08-25 04:17:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ab3c5e1-487a-303e-b479-a6d05f6520c7 | -12.96019 | -46.34001 | 2025-08-25 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a84f3b9-45cd-3953-ba13-f346c00a8fd4 | -14.43644 | -56.47047 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 675d2e43-4889-35a3-8898-263b3e690c78 | -11.11234 | -44.78856 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17b941d9-684b-33ba-a4ae-543b92cc585e | -21.12895 | -48.92242 | 2025-08-25 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92759ff0-bebf-35eb-96c3-3e42a0fe299e | -11.59886 | -46.37052 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a29221b-47ce-3702-a913-4c8bd34d8f3e | -9.68689 | -48.33511 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7eaa835-9c50-3730-8210-9a569b9f546d | -10.98635 | -47.40387 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42534ce1-a572-3777-8b9f-e6a645dc8d8f | -11.58174 | -46.27961 | 2025-08-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13a65594-c7b3-3fc8-838d-9aa7c035e1ce | -15.98686 | -48.06728 | 2025-08-25 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3821785-4e86-3640-b1a3-80239d52661c | -22.54393 | -46.81633 | 2025-08-25 04:17:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38f0b5bf-3a13-3e32-850a-5041aefb01d1 | -12.95804 | -46.33192 | 2025-08-25 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38647f53-8bd6-3117-b6e3-bf16870c1db9 | -15.1131 | -48.68159 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d35c762-005d-3ad4-a526-1757381e0f62 | -17.57836 | -45.38642 | 2025-08-25 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ae69d3f-db4c-308d-8b36-198b7eaa972d | -11.59225 | -46.36608 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e10d3caa-05a2-38be-9325-92f2d96ebbf7 | -12.99975 | -56.8921 | 2025-08-25 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802adf1b-d093-3b5f-88c7-0460cf60531d | -16.429 | -42.63468 | 2025-08-25 04:17:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b5ad146-06f0-3d25-ba6b-89a57fe34fac | -21.94864 | -45.58435 | 2025-08-25 04:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da73d013-9dd5-32f1-9590-434d2bc0b45d | -16.48694 | -46.76 | 2025-08-25 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c45afdb6-ac91-39fc-99c1-1da925f2fde3 | -14.92391 | -45.53236 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6afdb258-636b-3017-89e3-19a7128930f4 | -11.14324 | -44.78633 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd55c272-1552-3238-a158-54c6804b9ef3 | -13.44154 | -46.9206 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcdf21d7-10f3-3020-8b39-8602f3fd42e7 | -19.9153 | -50.41572 | 2025-08-25 04:17:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42ecb753-4f2f-3146-a635-fde10a39c56c | -11.60113 | -46.33269 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 718d63a2-dad1-3795-8699-5b0c0105ab39 | -11.17465 | -55.02945 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3defd643-a7fb-333d-9f1f-dc5895a00446 | -22.88409 | -46.4381 | 2025-08-25 04:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9be5775f-cb71-37e2-ad77-2bf42b16482e | -11.19651 | -48.46875 | 2025-08-25 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fb5124e-2063-3c49-b835-bb6585a579fc | -13.51295 | -46.91373 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7785678-2b4f-30c8-b4be-5fff4833c0a9 | -12.74425 | -48.11564 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e751a14-2549-31dd-8d68-c83d7d9abfae | -13.46983 | -47.00389 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 43032d4f-fa61-3bbc-bb5b-62848ecefd3e | -22.86022 | -52.08272 | 2025-08-25 04:19:00 | NOAA-21 | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 481630d6-769e-31fa-ae80-7d5fd297d5b2 | -19.92502 | -44.04029 | 2025-08-25 04:19:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 02ec634f-56c2-36ad-8905-f58818506412 | -17.79934 | -44.48601 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2faab68b-56a8-3988-b035-7dffe0601267 | -18.23309 | -49.26117 | 2025-08-25 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9893568e-1d7e-3bf6-8ce5-4cc5253da6bb | -17.79596 | -44.48555 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 354c8718-19fa-36dd-b56a-018df51d333e | -17.84412 | -44.41689 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 500c08a7-2fc9-3160-9672-78ee013d4a07 | -19.57111 | -41.61173 | 2025-08-25 04:19:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c4667033-ec5e-3e65-9e8b-c85ad9ed234c | -17.91404 | -46.09125 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bba18afd-b186-3a93-8793-1470c36f9934 | -17.34429 | -47.8524 | 2025-08-25 04:19:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1260ea7-2739-34ce-ae8e-2b7be3d54960 | -18.53866 | -44.76432 | 2025-08-25 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d7c96ff-0020-30c1-b293-57b331e11972 | -20.54412 | -41.68716 | 2025-08-25 04:19:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0652dcb2-cd44-3fe7-8e62-57370ef2e931 | -18.41818 | -49.20681 | 2025-08-25 04:19:00 | NOAA-21 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d1fa58d0-c0f9-3d3a-8261-9bf03cfef322 | -17.32956 | -48.29714 | 2025-08-25 04:19:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
