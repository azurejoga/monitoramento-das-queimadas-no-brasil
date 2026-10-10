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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae95d34c-ad6e-3a0b-a15d-8bb3c68e2f67 | -2.5485 | -58.03531 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 884cdc06-d96d-39b1-b4bc-944525889651 | -3.17453 | -49.45629 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8be53f4-574d-3852-92b0-315d9ca644bc | -4.11215 | -54.01253 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fcab2b8e-e00f-3e70-b846-29f03a475913 | -3.21774 | -50.55578 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31bf8b9e-7998-3719-bf0a-bbdcc68141e0 | -2.43171 | -55.99172 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1026f62e-9698-3ae1-b7a9-9c24504f1de6 | -5.95937 | -55.36528 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f1d8b4-053e-3acf-a36d-05766288c765 | -3.59689 | -54.69046 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85cf49fb-3071-3a22-9e7d-c6615351cdd1 | -3.47859 | -54.72989 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e8309c-f4f6-3376-8c6f-9e415fbfe646 | -3.3016 | -54.00409 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0472938-7fa4-3d45-bc92-a678046aaefa | -6.33766 | -55.31367 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f9c9363-4375-3e90-8d5f-b733efe9dc65 | -5.87564 | -43.41306 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76baf690-65bd-3310-80fe-4a64c57ad730 | -1.26812 | -55.74843 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec3ead5a-2554-3d0a-abf8-bb32152c2488 | -1.21129 | -55.64824 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3452e64f-2ef8-391f-a235-fa35a392862f | -4.52973 | -54.87102 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07f410c-129c-3ce3-8916-dda1a73e6629 | -1.27324 | -55.76125 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f61a842-342c-398f-8bce-31bccb7b9f37 | -6.15588 | -47.9606 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8450f686-803d-315b-86b8-f4b53f961202 | -6.81042 | -59.32083 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7927e2bb-339e-3657-8520-81d0d4ffb662 | -3.27257 | -50.39373 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1120ab4-0f63-3216-8ef4-a538d6678832 | -3.06234 | -51.13326 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84503a6f-9f36-316e-9f19-93885e6ddc9c | -3.54522 | -54.69304 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5837b7b5-6372-3dff-bca7-ce139ced0edf | -2.56699 | -56.18541 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00df106d-4b1e-3f90-ae29-bf74cce02ec5 | -7.02756 | -47.68155 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbc71f04-9ed4-3163-8579-5b5cde8f6e12 | -3.25218 | -50.42923 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa5735d4-f0d9-3dd2-b394-821193d9fe08 | -4.58975 | -55.72688 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fae61da4-5ee5-301c-bc2a-d88f41687907 | -3.31209 | -54.0234 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beb8e38d-7be1-3839-8cda-590b946ef625 | -3.51516 | -59.94947 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f5c61b9-6afd-31cf-bfa7-5de8bf73c1b4 | -4.38206 | -55.15822 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9c706bb-5823-3dc2-b4a1-b5e274339960 | -6.36914 | -55.16045 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c79f0de4-8d44-3903-8178-ed4ca0deffbe | -5.95161 | -55.34955 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 083e6a43-09b3-3d18-9ffb-1d6335cf0ef3 | -2.20782 | -58.1284 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0c696ca-2ac8-3ea4-8560-0ed5d132a09f | -5.83703 | -44.92763 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bad846fe-1251-3983-b51b-b55dd07c7c51 | -3.85545 | -51.10885 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2fd17fe-3fd5-3cac-9acb-46d49ab9c3c6 | -4.13493 | -50.81959 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9178750e-d74f-358a-a2c0-10f009dde994 | -4.13241 | -50.83601 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de946ef8-17b2-3096-9302-cfd49834737b | -2.51894 | -58.09467 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1b59df1-ffab-3db0-b0f3-f45a5271ad10 | -3.21902 | -50.54752 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 904836a7-10c3-34b1-bddb-bc5780933610 | -2.57349 | -57.78602 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae80c340-c491-3d1d-bcdc-13b418f6ee1d | -7.24483 | -44.17227 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e064352d-5f77-3660-8ede-3df36bd5dae7 | -4.55067 | -54.97063 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc955af-b1cd-3a0e-aa13-f70b896c9fce | -3.06166 | -58.79747 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd3f1ad-0504-385f-bbf8-5a68fc2bd4ca | -3.56356 | -54.68517 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a46893b-1c4b-3140-b16d-20aae14c8596 | -6.49095 | -55.2913 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373daddd-ce0c-3c25-8140-44d839b179a0 | -7.4271 | -55.5787 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd51889c-400c-38ba-a2a7-d89f80e4c1b2 | -5.68558 | -53.47133 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a657be3-c313-343e-9acf-ed4b02f012a9 | -3.27957 | -54.69461 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86734ecf-d305-36f3-a006-80c94f90ee64 | -5.74154 | -45.13506 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db9d7558-df27-3059-88b3-3c9bfca5d901 | -5.6017 | -47.28247 | 2026-10-10 05:04:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a300c85-050f-3a9f-b6fe-620c2b81f769 | -5.95047 | -55.35665 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 155649c3-0726-34bb-b7bd-31bb69f6c901 | -7.23984 | -55.15649 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa68808c-ff7b-3f9d-b458-309d6c8b8043 | -3.85737 | -58.90576 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2b3077a-ac3a-38c7-af2d-c82638ec3ff2 | -2.47341 | -56.09037 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28eb4725-6092-3864-bc6f-92240aafa784 | -6.45734 | -55.05639 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e554783-d245-3465-bff4-555893aca608 | -2.47465 | -56.08259 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f361483f-f23f-3d16-8c72-f9324a722b99 | -1.52579 | -54.50928 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed7b0081-ba96-336d-b2ff-4d9c771536ff | -5.09383 | -60.21983 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c408da8e-b520-3ddd-b7fa-80bab96cb3ac | -3.62668 | -55.45613 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20cc8e88-df07-36f9-84b9-e38f485f992a | -6.46865 | -55.51569 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8d8fdc4-ea0e-3f9a-bbb7-991506cf41ad | -7.50007 | -54.99534 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c99a6458-998a-3427-9855-e153a115e5bd | -7.19999 | -55.1505 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e159aeb7-aa85-38cd-8c91-4a133e4a0bfe | -8.18931 | -46.35069 | 2026-10-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce01766-9139-3e83-bffb-244e29cff459 | -6.50691 | -55.36242 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bd31a73-6928-378d-999a-900e16449c5c | -6.36305 | -55.1559 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d084808-b14b-3f72-ab56-947db7dc9c9d | -3.19012 | -60.05802 | 2026-10-10 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46de4986-22f0-3385-8c98-dba054d694af | -3.11513 | -53.78752 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed470348-f3a3-327b-bf52-f61f747c91ee | -3.59412 | -54.60035 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 37d04ce4-3135-3800-a068-b162e572f522 | -7.23743 | -44.18382 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c16c9c09-1c1a-3eeb-a757-ebd2b3e7c285 | -3.50524 | -54.60488 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 987ca798-c18c-3e5b-9fb7-a59f7bc8f106 | -3.28459 | -53.87411 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7ac0bec9-91b5-3332-b976-3a51bf6526a7 | -3.10287 | -51.36311 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0cd89a3-ad1a-3daa-9dee-36d2f0a04665 | -4.40662 | -49.77229 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b21a5abc-42c0-3a5f-a35e-6769f3ab40f8 | -3.47221 | -50.09211 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c08c9832-f943-32ab-bc7e-8f9c00e84432 | -1.3699 | -56.93175 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 173ba909-4ec5-344a-bd2a-5ec28136f2e9 | -3.86345 | -55.83688 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f54098b4-b71a-3460-9d9c-0f87a0393183 | -6.70711 | -58.71296 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08621547-e27d-3ffc-9b97-ec5e94580c7f | -4.8928 | -49.05223 | 2026-10-10 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23f1f473-96a1-347c-a49c-484c44222662 | -3.43646 | -54.54394 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 557e3304-ce39-3f50-9f0b-a0bb7b32b545 | -3.00566 | -54.24043 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686dcd15-f6b5-328f-b05c-8344b2a4276f | -3.16902 | -50.45596 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1c03752-898d-3f3c-8998-ffb589ce53e5 | -3.30269 | -53.99721 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09a0aa7f-b17a-3896-93ea-0e668597fc27 | -6.12799 | -53.05668 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 340d08f4-9faa-3a84-b0bc-357f847f51ed | -3.48526 | -54.62325 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d78fccf3-590a-38a0-9590-149501ef3400 | -5.75269 | -45.13309 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fa80705-5a50-332a-b021-7b3d3e55bf4b | -6.35916 | -55.15886 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6a90868-378d-3cfc-8b4e-df2779c4c56e | -3.78086 | -52.06672 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 299f1f6e-94cd-34f4-8338-47394b73b1be | -2.96795 | -54.07153 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051978b2-2207-336d-8539-8ca1e86c25bb | -3.56413 | -54.66016 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e369a36-2777-36b5-9075-6dbf54b16c6b | -2.81663 | -58.29344 | 2026-10-10 05:04:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 455006b0-b66e-3c95-8790-76ffc0815194 | -1.21005 | -55.65598 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8f7625c-f727-352f-860d-e4f6a9502fe2 | -3.66502 | -55.49965 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f72c6ed-7d33-3009-96e1-56a39045a59e | -3.00993 | -54.10642 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32a55ffb-dc34-374e-a34e-cc7ba1683066 | -6.33489 | -55.30962 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c859af6-d1a6-3b18-9077-0fbe542d8fea | -3.55911 | -54.69164 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d18fd23b-39af-3b62-a1fa-29ce260ffd71 | -2.92707 | -54.05087 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d75fbd6-8f6b-303a-8a05-133b48ba61ca | -3.95884 | -55.33368 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2871ae-0313-3a73-9085-dbab2098d23e | -2.73769 | -54.13045 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fca5a6-1fef-39ac-bf15-bf56b22b7256 | -3.58191 | -54.37738 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e88c857-78d4-3856-8f6e-c44a5ca52474 | -3.62991 | -59.31854 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c70198cc-c964-354f-befc-53e205dbc484 | -2.74209 | -54.10279 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 119e3e98-dc70-3218-8ce5-fc8e7cefad8f | -4.73857 | -55.67167 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63f723c8-a90b-3752-9f55-2d3f23a29ce3 | -5.9281 | -51.81489 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README114.md)
