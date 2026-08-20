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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f22ef414-227f-3548-b0e3-da7111d4ea79 | -23.571 | -47.02555 | 2026-08-20 04:23:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5af6fb1d-c884-33bd-933d-c1b9a939a286 | -23.62385 | -48.28333 | 2026-08-20 04:23:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2bcc197-3cae-3634-a36b-4cbb05779036 | -22.85622 | -42.55739 | 2026-08-20 04:23:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 670ab800-1acc-3bf8-ac66-e9dd61724bd0 | -20.26028 | -46.74558 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9b08ae0-14d0-38eb-910b-820c803fe108 | -20.80567 | -43.85823 | 2026-08-20 04:23:00 | NOAA-20 | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 0720a37c-1554-3327-9688-6b31e53cb872 | -21.61693 | -49.01847 | 2026-08-20 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09bd7981-ee99-3679-8195-5cb2a146d0ce | -20.88597 | -45.42554 | 2026-08-20 04:23:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e3f3944d-d7c2-3dfd-9717-996caf25edf3 | -21.61625 | -49.02245 | 2026-08-20 04:23:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9acb7307-b77c-3566-bade-0aee619f32bc | -21.377 | -43.74504 | 2026-08-20 04:23:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab46938e-1cdb-3eee-894d-536c9a1a670c | -20.88654 | -45.42175 | 2026-08-20 04:23:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 977f7215-8dba-360f-aeb2-2bd4a50abd26 | -22.34643 | -49.04733 | 2026-08-20 04:23:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08b74c39-5618-33f1-b84e-5196af2a5160 | -20.78525 | -46.30053 | 2026-08-20 04:23:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f140d1d-3f17-3abd-a987-1c09e96eca02 | -21.14052 | -43.90992 | 2026-08-20 04:23:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c9a0a981-3123-3a53-84c7-754a0af542dd | -21.14121 | -43.90689 | 2026-08-20 04:23:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 953ea08d-c29d-3cc7-b405-3b5b7504c25a | -20.52308 | -45.3781 | 2026-08-20 04:23:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| adc9b8d2-001e-3574-bf78-0ae1824c2dfb | -20.27586 | -46.73331 | 2026-08-20 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71678719-a12a-3638-8832-7642baf48a75 | -21.44911 | -48.51571 | 2026-08-20 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdce2290-f9f7-3992-8a58-ffd01c2fae9a | -21.14111 | -43.90564 | 2026-08-20 04:23:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0f098209-8bca-36af-8fa0-c851d0d00ba5 | -23.09937 | -48.74784 | 2026-08-20 04:23:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dde6cb54-56ed-38a9-b72f-577ff9e7eb0f | -21.10796 | -45.60977 | 2026-08-20 04:23:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 829a8065-52b4-370f-9324-9879f9d06b61 | -21.76926 | -43.33813 | 2026-08-20 04:23:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dbd5e7ad-8736-3002-aa3d-3088e0166423 | -8.6727 | -54.6492 | 2026-08-20 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 494b8d53-7cfe-3ea3-b2cd-33545e8f3f0e | -17.3365 | -43.6383 | 2026-08-20 04:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ab3b5327-f81b-3681-b16b-2d6f568b436b | -8.6729 | -54.629 | 2026-08-20 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| cc15565a-3aff-3f0f-bd71-98c3433941bd | -9.12 | -61.6011 | 2026-08-20 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cfeebc9d-5f40-3980-9062-d3006a1ff068 | -17.3372 | -43.6139 | 2026-08-20 04:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| f0645376-cdd3-37dd-b8a7-60e3e3ed76df | -10.3897 | -61.2118 | 2026-08-20 04:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cfccf426-05c2-3ddb-848c-3a22b29113b0 | -18.0487 | -44.6066 | 2026-08-20 04:40:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d32a6252-e29c-3fd9-a400-d9aa5a35067a | -8.6727 | -54.6492 | 2026-08-20 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 1132bedc-54c0-32e2-bb70-394b965b0da9 | -8.6729 | -54.629 | 2026-08-20 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3094064d-7f56-3ec9-ba63-1d8338603a87 | -17.3372 | -43.6139 | 2026-08-20 04:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a5761e83-380e-3b89-8235-7f8913c9a430 | -18.0285 | -44.6113 | 2026-08-20 04:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e1ebe48b-aca2-3250-b35e-b76c8a45090d | -17.3365 | -43.6383 | 2026-08-20 04:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f6788491-bf6d-3c82-ab03-40c99fb9972f | -11.4529 | -46.5717 | 2026-08-20 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9d4cfbf8-8335-35f2-926e-1661cd7fa716 | -18.0285 | -44.6113 | 2026-08-20 04:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4429d8c5-54c7-3a7d-8c5d-b068008d3969 | -8.6727 | -54.6492 | 2026-08-20 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a8f346a6-431b-3066-ba7d-f92abe862a5c | -11.472 | -46.5692 | 2026-08-20 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 80d11422-c40b-3f52-a31a-cd95166dede0 | -17.3372 | -43.6139 | 2026-08-20 04:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 25b9ba76-7005-3341-9b51-379da7dfb6d1 | -18.0487 | -44.6066 | 2026-08-20 04:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d731abe1-e82d-3609-a666-81409ff6eda5 | -17.3365 | -43.6383 | 2026-08-20 04:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| db1e5d76-0e03-3119-b7bb-b98753c0f9d4 | -9.4257 | -60.416 | 2026-08-20 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 765ae807-ac19-3cbd-a58e-b7c9f0401891 | -17.3372 | -43.6139 | 2026-08-20 05:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| df091991-65f4-3e3a-869b-71c9ea5fbc00 | -18.0285 | -44.6113 | 2026-08-20 05:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6cd099b0-9b28-3dfb-845d-06a390ab169d | -18.0487 | -44.6066 | 2026-08-20 05:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 90f9b4a0-fcdf-31b3-98de-5e7557deb66c | -8.6727 | -54.6492 | 2026-08-20 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e0244b78-662c-35b4-83e7-1d8f63d7f031 | -9.4256 | -60.4353 | 2026-08-20 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| aaacc45a-ee90-32a0-b375-41cf3a0806cd | 2.15893 | -50.7191 | 2026-08-20 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b20b079f-78bd-30b7-b5f3-facd07494b8f | 2.15465 | -50.71549 | 2026-08-20 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6529a11-22f5-3548-acdd-e36469cd03cd | 2.15531 | -50.71968 | 2026-08-20 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d11bd98-d3fe-3b61-bfa5-391fcf1b5f4d | 2.15398 | -50.71131 | 2026-08-20 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e71494ca-9307-353b-a903-e97e1d1a5bb3 | 2.15036 | -50.71188 | 2026-08-20 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c701d3d-b741-3e50-82f4-a7937c9eba26 | -6.68284 | -56.15721 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ab2b308-c295-3c65-a90c-e60b8a54952d | -6.32615 | -51.84945 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 848439d8-8f1c-3999-be7b-f6b8acec6979 | -7.25399 | -49.89611 | 2026-08-20 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ef8827f-e21f-3292-927b-18f527151aea | -6.70503 | -58.93911 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b29f5ac2-eeb1-367c-87d8-1ba3b9c8d8c0 | -6.3191 | -55.91574 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b99ea63-a971-37e4-bb90-565575b31b90 | -6.24507 | -55.40879 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a6eddf9-2a28-3afc-9800-de40f9afff8f | -4.39191 | -55.47434 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f867f7ee-6cd5-38c6-8be4-03589e9cccfb | -5.80748 | -55.7287 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d29c247-e328-3e2e-b4d3-b767c3f992e7 | -2.64654 | -47.98333 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad23d46c-9012-3afd-839b-cd01dedae522 | -4.44107 | -55.37623 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ca043d0-0b46-3926-8479-1de6a2e8399f | -3.10016 | -61.19529 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 748c3ef8-8b69-387d-ba0a-8fea4f4e0287 | -6.13397 | -57.8739 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 869fa145-cc0c-34f4-9dcf-7195937cedc0 | -3.61821 | -51.90535 | 2026-08-20 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0b26832-5718-39d0-b310-8d2f3a6a3bb1 | -6.88531 | -56.42731 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5840a63b-970d-3695-b604-383bbf882b57 | -4.9209 | -56.60992 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea1a17ad-44c6-3a44-aa94-6dc2347ce8b7 | -7.05377 | -56.611 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9674bd31-5e81-38f7-b053-66fe62ad2425 | -6.88477 | -56.43078 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4ce2a18-079a-34fa-b7a9-473604a06cee | -6.42749 | -52.75907 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a5651c8-627a-3bf7-a239-c5a36a3b9d83 | -6.83791 | -56.44832 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9642d04b-c005-3851-9bff-95e3923608d3 | -6.36103 | -54.90147 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2daad38-e7f6-3548-a9c6-39824f035494 | -6.69891 | -59.10213 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5a95541-40d4-3231-a8dd-785bb83ae25e | -7.05045 | -56.61047 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 422640d5-c903-33ab-8edc-b2bd18b1f569 | -6.6427 | -56.41342 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4a9562c-411c-35c4-be49-da1d8a99fbbb | -2.64122 | -47.98735 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aae9a446-c6b5-3eda-8a24-bd9114662a85 | -5.79703 | -55.73061 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74adcdd-818a-37b0-b09e-521d91911538 | -3.68381 | -47.65214 | 2026-08-20 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df6c3faa-6422-33dc-8743-dd1e216dea00 | -5.74201 | -43.27781 | 2026-08-20 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6292e23b-02b7-34b0-84df-177b2492c9c1 | -7.46496 | -45.14646 | 2026-08-20 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39bf543d-d42d-3e0d-b06e-94074d8039e6 | -7.35069 | -45.81901 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25879363-8f16-3bf1-adf7-548be55ee7ef | -6.31579 | -55.91523 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8854be-9f6d-3cf4-9210-86b5181de40c | -2.56715 | -47.25161 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 336f5578-f9fe-31bd-a186-d0bb9a613709 | -6.89643 | -55.72382 | 2026-08-20 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b22a36bc-1c5a-32d9-87dc-53925438fb92 | -6.43048 | -52.76377 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 81270130-e49b-3b2d-adea-0bab57cc6209 | -7.96722 | -46.91962 | 2026-08-20 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c876bf7-563a-3896-bd1e-3ffa302f0a61 | -6.70016 | -58.94663 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2eead769-4bd6-3fc1-9f93-e9e59e4e33c6 | -6.64216 | -56.4169 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73b47256-e360-3dd6-8f7b-4f4af41a62ff | -6.69593 | -58.95011 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1b3cc22-956c-3cb5-93f0-b4582916c414 | -6.44032 | -52.72258 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45016aac-c563-3685-a94b-2a10b71b887f | -5.80302 | -55.71387 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47d69a5e-19d2-34db-9416-54151c406a50 | -6.42819 | -43.06754 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d4baee41-24b6-32a2-8dc4-65f703f9340b | -3.89979 | -55.88091 | 2026-08-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59393d53-be7a-3532-a390-85a890a119dd | -7.25025 | -49.89104 | 2026-08-20 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8302b9b-86a9-340c-ae98-8989798682a8 | -6.83459 | -56.4478 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067a3d98-ce6e-3678-a7a8-d5d59729735e | -6.89085 | -56.43528 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91fcd777-22f8-35bd-a9fc-59cabbfa9aa8 | -6.69725 | -59.10296 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a78af3a-ce7e-309c-87fd-fad61433ddf0 | -5.7981 | -55.72371 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53d956e7-a6a2-3fe2-8bc9-0d1b4c7e32f2 | -3.10031 | -61.20693 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6190df34-0576-3122-b6e4-81c0a11555b1 | -6.59032 | -58.97593 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b535bc5c-3bd4-3f03-a996-405acd2eff38 | -6.58542 | -58.9836 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README41.md)
