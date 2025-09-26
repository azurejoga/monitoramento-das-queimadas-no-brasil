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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4504fca-c593-3c1d-b085-d4e420effc63 | -14.77525 | -60.19114 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c4d5da6-fd54-3394-9ba2-b1df77c80bff | -11.6116 | -44.43877 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 247da68e-0137-376f-ab48-94c0a0a02c81 | -14.82648 | -52.92731 | 2025-09-26 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41c17b9c-7144-3612-9e34-342c75c82e2a | -12.13787 | -47.95629 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b54602e-d9f9-3830-9633-192398e3e90d | -13.40114 | -49.46949 | 2025-09-26 04:44:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f638b20-039e-3e0e-9575-7c0e70749ff3 | -15.53846 | -44.33138 | 2025-09-26 04:44:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 064326bd-601a-3765-9ae8-8d0a975817a2 | -16.85688 | -50.50752 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 51183de4-8fca-3b3f-bee0-240d3684ef5f | -10.43906 | -48.20666 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91b02754-9eec-329f-b6ab-e5c5a4c26f88 | -14.60016 | -48.25808 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4601df46-472a-3002-8887-e3c633c89dbb | -13.64126 | -48.10149 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f31dd7a0-68c7-34c7-83fa-a196957ae8fa | -15.72971 | -59.49707 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 851f9aff-b61d-3104-81a9-9df79d819c78 | -11.61217 | -44.43452 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| befe0076-85ba-3013-a79a-d68577f84792 | -15.92102 | -57.49894 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25275422-bf9e-38ac-af3f-2f8451054dbd | -12.1456 | -47.95338 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f67c8be2-c046-376c-aff5-acba953391f3 | -13.63764 | -48.10103 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b827a351-5c25-305c-8494-381cf5b5e286 | -15.89301 | -59.33842 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3970db2-f66f-30a0-8a86-654f594201f5 | -11.7885 | -44.91067 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4601e2e5-a19a-3852-9548-aedfb298e042 | -14.04265 | -45.49261 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c2c5eb7-ddf8-331a-bc6c-43f92fd0c850 | -15.40127 | -47.06232 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea5a304a-c81a-3246-8bc1-4bd5036cd039 | -10.60516 | -49.6414 | 2025-09-26 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e039c4-5bc2-3917-8097-0c4e21ba41cb | -15.35019 | -49.61594 | 2025-09-26 04:44:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd4002fa-3911-366c-afe9-1aad97ebaf23 | -11.00371 | -44.34735 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 157e7bb3-012e-3f5d-8455-bbf9d992d237 | -11.66844 | -44.44683 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70127444-1410-3872-897d-57eec9b0481d | -10.93347 | -44.30445 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b51643-ae1f-3690-a5e9-9cde1e3afd67 | -15.73447 | -59.49823 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4662aded-f3bd-3b66-bf6c-aea944454e1d | -18.24954 | -45.01072 | 2025-09-26 04:44:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcf6c0c2-c726-3b24-ba9e-c5451de8fbe3 | -12.7733 | -47.50898 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb401f37-acb5-3988-ba61-264ad20037b6 | -16.85745 | -50.50377 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 01b051e0-9f7e-3e32-bed4-d0e2004f05bc | -11.42262 | -44.97937 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5338edc-b635-308a-bf90-bb9588326a0f | -11.48391 | -47.32711 | 2025-09-26 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68f85291-a233-359c-8146-df1d0930feea | -14.75752 | -48.3507 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86e8449c-177e-3cfd-ac5c-998a1bef2f63 | -11.24611 | -45.54754 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 68b96cc3-0467-3280-a3a4-38667e3b78a8 | -15.92186 | -57.49447 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83e4d620-78ff-38a5-a78a-1ce027f86205 | -15.72595 | -59.49071 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b647a152-6614-3afe-9a9a-5f60ceeba01d | -17.9915 | -48.58663 | 2025-09-26 04:44:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31f5bbf9-987b-3629-b27d-7d9d62fb2d61 | -15.07142 | -44.97824 | 2025-09-26 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c13be7c8-174e-390e-bde7-46a5781c39ad | -13.25741 | -50.66867 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 538a5d2b-3e39-3b33-a272-0228b2ecef57 | -11.2466 | -45.54398 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5cf5e53f-a110-3b13-9cc3-15d892677cf6 | -15.72798 | -59.49769 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 977464d3-63da-376d-b113-793ad004a0cd | -12.14203 | -47.95283 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0920aea6-05a2-3039-81a8-b64349ad2a72 | -11.65377 | -45.35113 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90daf976-84d2-3a06-8ede-1ed4fa116e7c | -17.59729 | -48.55664 | 2025-09-26 04:44:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0259eea7-b04a-38bd-87e8-5f1c30a21731 | -15.63832 | -58.46692 | 2025-09-26 04:44:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66c11aa2-f85b-3efb-8663-6ebfcaf2cabf | -11.69786 | -44.45963 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 329514dd-444e-3c98-8fb1-c1968dbc1e79 | -15.76882 | -49.93635 | 2025-09-26 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 34.0 |
| bb25fbc4-68e0-3567-ae1b-3ee95a1279f4 | -15.63023 | -53.6249 | 2025-09-26 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55840fce-31d1-397a-933e-ae7f1f9ae41c | -15.74391 | -59.51794 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dcf9ef3-e025-333e-80fe-600be91a71e4 | -15.87863 | -59.33414 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053b0138-1927-3a7d-81b0-c23a4fc0eae4 | -13.8883 | -43.92043 | 2025-09-26 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51ac6e86-d192-31e1-8178-e479b2ce57b6 | -15.36927 | -59.16976 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a836fa9-b232-318c-a9a0-50c41ec5c34d | -11.65077 | -45.34264 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e314f31-22ec-3314-ba43-0eea6492def3 | -12.06479 | -47.98236 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee219f50-0481-3504-9200-6a3b8d75218e | -15.59632 | -46.45577 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1ad8989-980b-3e65-9b74-cf371e6ef95e | -13.40925 | -48.55044 | 2025-09-26 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f13c8f7-8e97-35bf-a050-bdc7b8de310a | -14.10612 | -51.15751 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295e961d-8b10-3fda-a53f-634c8b59d02a | -16.85122 | -50.5219 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a27a2664-3230-32fc-ae41-2f92d38aabb8 | -16.8484 | -50.5176 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a74bde51-3973-31b6-baf3-17bdabb9356f | -13.24797 | -50.66348 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8c48441e-ca45-3eea-a448-540955b3e819 | -11.69991 | -44.40976 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a99d3130-f4bf-392e-98ee-e786954c31cf | -14.87928 | -45.54081 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b100100-b748-37da-906f-df8aedf5490f | -11.78732 | -44.91934 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e1e915-b05b-30a6-a310-9a4e9bd04cb3 | -13.92208 | -46.85453 | 2025-09-26 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea9d8602-2447-3fc7-92ac-3336cae41a6c | -13.84643 | -45.61202 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f506c7a-f41f-3336-a5bd-ba17582f111a | -14.10945 | -51.15806 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b85312-f250-320b-80d7-f8de01769609 | -15.92522 | -57.49978 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cffaa363-6f76-3c41-b71d-ad47bc00f961 | -15.06641 | -44.98225 | 2025-09-26 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26039879-cf1a-328a-8ed4-23a578aa4847 | -13.27913 | -46.97351 | 2025-09-26 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 197dbdb7-51c4-35e5-abe3-70f2d2349ff5 | -16.85349 | -50.50695 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c94d3597-a1ec-39a5-a586-56db410ba9b4 | -11.00257 | -44.35571 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc9a0cd1-b729-3e6b-beef-685b172a7864 | -10.43793 | -48.2142 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6c0d284-2dda-350b-9e7b-aad66dd3ad1d | -14.98758 | -50.05755 | 2025-09-26 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6853d410-8ba4-3c63-b530-3cba3be869ca | -11.66785 | -44.45108 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17bb18ae-b481-3e80-b685-23a8cbcd7bca | -15.02046 | -46.93954 | 2025-09-26 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4538107-bf1e-3035-80be-b166e4561002 | -15.02832 | -46.94025 | 2025-09-26 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6dfd42e1-e0da-35c3-a02f-55da65ad6abd | -14.98396 | -50.0576 | 2025-09-26 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2da95e2f-f38e-33ec-8627-032e4a8d02bc | -11.68628 | -44.41461 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41df668b-dc5f-3b08-b009-692080446d37 | -15.27125 | -46.42218 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| add0d9ca-9458-30d8-9479-401379f1ed2e | -15.94053 | -59.50056 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ac3bee4-7182-3c81-a385-8ec737f1c30b | -11.96172 | -47.87606 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a601815-5686-3383-a44e-49f087eb2691 | -15.7728 | -49.93311 | 2025-09-26 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de8da108-4135-3b25-96c2-902e9ae0eccd | -11.02058 | -44.354 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1c91098-bf77-3d0f-807b-6365c41c0fb7 | -13.85477 | -45.61322 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d16c6cb-cf56-36a5-a86c-ffcf18d43423 | -11.22086 | -45.57607 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f85da45a-b430-3a8e-9e04-85c520a5e8a9 | -10.93843 | -44.30083 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9cd085f-79f5-3416-b636-a33033f707a8 | -14.82432 | -45.40556 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eedafef1-7054-34f4-ac7f-aeb3d35f7c1b | -10.17212 | -55.39208 | 2025-09-26 04:44:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9bc9e2b-6695-30c9-9f2c-dea3a7011d1e | -11.66903 | -44.44258 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b9f54c3-a808-3053-9143-9306da3d4b09 | -10.48903 | -48.04036 | 2025-09-26 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97e8dc84-2469-3744-af1e-2e481a41db75 | -11.21384 | -45.56769 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 961361b0-7a21-30f8-acc3-9fb064296eeb | -10.43503 | -48.20981 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dea4d95-88b5-3d08-ae8f-54593d5b0ff0 | -13.24517 | -50.70316 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b63621fa-e175-39e8-99eb-8078b37e98e7 | -11.21798 | -45.5723 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 36ed3738-8b1c-317c-858c-5757a02c6990 | -11.4127 | -44.92554 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c998bdde-996a-3754-98c6-865737a38a6e | -11.79736 | -47.64996 | 2025-09-26 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea1d7e11-49a9-395a-bab8-d7d44ce1c7a4 | -11.43558 | -47.79876 | 2025-09-26 04:44:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8dacff1-e396-35ca-a59c-5a000f279586 | -10.1802 | -55.39347 | 2025-09-26 04:44:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed4ae9ab-204c-3a3f-8b4f-72b7d633aaf9 | -15.58679 | -51.69911 | 2025-09-26 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fad189d-670b-397d-81d4-bb95b0d624f7 | -10.80894 | -54.13159 | 2025-09-26 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07601f4-3ae9-308a-aa85-1f7798f2018b | -15.99537 | -49.02902 | 2025-09-26 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4eb29db-9bce-33b7-9cd8-5d70c1898436 | -15.99826 | -49.02858 | 2025-09-26 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |


[Clique aqui para ver as próximas entradas](README37.md)
