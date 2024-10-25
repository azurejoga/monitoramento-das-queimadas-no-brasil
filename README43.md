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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10f3615d-24d2-3ef9-8ca1-7c7618dafd25 | -9.63099 | -47.71897 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dee29fe0-b003-394d-894f-2cfd773322ae | -9.62871 | -47.71659 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd120e2d-16e8-3395-b79d-f039560a4a33 | -9.55605 | -47.72954 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8724b181-d642-3c29-bc08-ca17374c58fd | -9.53821 | -47.62125 | 2024-10-25 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2824c016-077a-3cec-8adb-4c9c289c2dbe | -10.17934 | -47.90912 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba45da17-0b1f-3b03-9a8a-218ad5b2820a | -10.17559 | -47.90849 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d6300d7-a4fc-3c6a-8319-9d8aa12eb7c4 | -10.10793 | -48.1891 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82cb89ea-6610-35f0-a1b2-69ba90440c14 | -10.05587 | -48.06237 | 2024-10-25 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8624685e-8e48-398b-9241-15ba0247bc97 | -10.05208 | -48.06172 | 2024-10-25 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df91123d-4f67-3d75-b9ff-ccbf377521e9 | -10.03614 | -47.46859 | 2024-10-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b52c4b4-8ec2-3b77-9627-8208f37badba | -10.03173 | -47.47237 | 2024-10-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 959b8bba-9306-30c0-a8b9-b063ef06a5e5 | -10.02145 | -47.46618 | 2024-10-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0fc1718-83d5-3d87-86b9-71da0a737efa | -10.01461 | -48.23508 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d5c618f-fbbf-3c28-ab03-27945697ee72 | -10.88857 | -47.89815 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c3f7572-b56c-3e7e-b744-74502c03fee6 | -10.88709 | -47.92976 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60db5c4a-cd5e-3e7f-adc4-5135ce25ed83 | -10.71061 | -48.0564 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11413214-eb98-3f1e-98c3-3fafbc335e01 | -10.65395 | -47.92989 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76a0c520-0c1e-3a42-aee4-1453133e2c48 | -10.65177 | -47.92004 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2d8d1ae-5208-3d32-93dd-8835f2a24777 | -10.65099 | -47.92469 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7e0989f1-9b80-3f1c-bee3-32de9ef4a226 | -10.64803 | -47.91947 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87f618e5-5ddd-3a83-ae79-dbbb5c2df3ac | -10.64724 | -47.92416 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c59fd79d-d3f4-38eb-975d-970d7d50a1c8 | -10.52516 | -48.14001 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f03f6fa-4fb5-391f-9f2e-a5bfa93a8335 | -10.47757 | -48.28304 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5d5d8f9f-eab1-3716-9a57-90caf3b1655b | -10.47376 | -48.28232 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8860219-f13d-3f09-aba3-ec04d8fca1d2 | -10.47295 | -48.28708 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3d58ff1-8a12-379a-9da9-c5f7e73d0835 | -10.46994 | -48.28161 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf2d5eae-1757-3f1e-bcd7-80cddb7699ec | -10.46913 | -48.28638 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d033787-1af7-3ef6-af88-beb1ebb747a9 | -10.44198 | -48.08034 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 940092e2-a33f-3f8a-9fff-476703cdb221 | -10.44156 | -48.08237 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c4cfbbab-fd08-3ced-aa24-660e6597bf7e | -10.44117 | -48.08499 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c761a6ed-795f-3295-b453-1e656de4421f | -10.44078 | -48.08702 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f58ec03f-f5df-3dc5-9d1b-49bf5408a161 | -10.43778 | -48.08171 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca3f1957-9695-3101-858d-2ee199197395 | -10.4374 | -48.08432 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1fc214c7-efd4-36dc-8db0-c5049310ed15 | -10.43701 | -48.08633 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef0edb36-499f-3ef4-a2e0-60fc5036d0d1 | -10.4 | -48.05242 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fca1b43-1b51-3121-a2bb-49aa6d3f99c7 | -10.90808 | -47.82697 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faa88663-3a05-35b8-93b3-09c03d6c6884 | -10.89992 | -47.83031 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ce39316-0ef3-36c0-967b-eb1efdcf4127 | -10.89699 | -47.82503 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5be4947f-eaaf-3d01-9230-d7567e43aaf5 | -10.89328 | -47.82452 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da8a8203-d9be-3208-8572-f8194c88934a | -10.86587 | -47.80654 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37eddf35-6f0d-3fa2-95b4-4b6f2b7158a9 | -10.86215 | -47.80605 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5a73192-88b7-37c7-bafb-cdcaa89d6c61 | -10.68682 | -47.82509 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4fc8d81-f3e4-379d-8aac-b322c05f376c | -10.67197 | -47.82261 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3764339c-42ed-3df9-8333-433dbe50918b | -10.50999 | -47.67034 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f1ac2f4-ca6e-34ae-8c36-21b6a711e20d | -10.50918 | -47.66853 | 2024-10-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cbc89b3-2f02-32d8-ac3f-d5be4be204f2 | -10.422 | -47.52076 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 362a6653-8ad7-384d-9323-74859bcd89e3 | -10.42198 | -47.51981 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bb7ad1c-0099-3cf2-8460-84cb9061510e | -10.41906 | -47.51577 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3f227ff-79f1-35bf-b741-f572db0f04be | -10.41834 | -47.52015 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5a54d72-444c-37e3-bf0d-b563c9b8e049 | -10.39196 | -47.5202 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe2ca740-b45f-3756-9374-a1578633783a | -10.36193 | -47.5195 | 2024-10-25 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69868129-a5e9-3f6a-b497-0465ec981c98 | -9.92777 | -48.69216 | 2024-10-25 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e70176-b7ef-3b40-b255-108f8478472a | -9.89484 | -48.65215 | 2024-10-25 04:17:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91497793-f585-354b-9fe7-eee631e8ea7f | -9.8519 | -48.57168 | 2024-10-25 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d16a4028-03d5-3178-a2e7-18e34e897210 | -10.8047 | -48.61533 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5f15ea-20e8-3fd3-8cdb-d398684c9dfc | -10.55243 | -48.74425 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36424269-4957-3627-8c28-61976fff6fa9 | -11.54974 | -49.29073 | 2024-10-25 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 434762cd-ebce-34d4-a77c-8a78e39983b5 | -11.54574 | -49.29 | 2024-10-25 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10a6a096-39ad-3389-b377-92b207ab9cb6 | -11.52741 | -49.07747 | 2024-10-25 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71b3b7aa-bf74-38fd-b111-edc4125ce09e | -11.28012 | -49.01279 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b367d39-df11-392a-8bca-4d6a9808b647 | -10.88018 | -49.13663 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51161b3d-541e-337d-854f-7c7cb2691d6a | -10.87956 | -49.14019 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d83e06ca-c76d-3dd9-83cb-5362e8205c81 | -10.87895 | -49.14375 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb4d3dbf-3843-3ecc-a1c0-9eac5b9e64c7 | -10.87558 | -49.13941 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c5e8db-49f5-313a-aa7b-2f669399f0a5 | -10.7759 | -48.99065 | 2024-10-25 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a36b058e-fa35-3024-be46-3a89fa0f2fb1 | -10.77134 | -48.99332 | 2024-10-25 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac1b0911-350a-39cd-8f4c-7c74119dcb23 | -12.07936 | -47.98695 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 676c348d-26fc-3a3c-a8a0-d6ac4060cbd1 | -12.07568 | -47.98632 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48403432-9cd6-3685-b2ee-05000a3a99f8 | -12.07201 | -47.98569 | 2024-10-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b0197e4-9943-373f-a274-e12f1da39168 | -12.05961 | -48.33948 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8bbb0e6-7281-3a86-b90e-309b364d091a | -11.85619 | -47.92839 | 2024-10-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f4fcfa1-6dd5-350d-af82-fe256b26dd7c | -11.72906 | -48.3591 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd15c94b-59c2-3132-ba13-e853f932b770 | -11.62998 | -48.39222 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9c1f0e4-22f0-3c5e-85c0-85333d1794b1 | -11.62917 | -48.39693 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bafd2be9-a767-3da7-a8c9-186edd7eae10 | -11.6262 | -48.39156 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f90dece4-72fc-3ddc-b89c-fde06d48a3aa | -11.62538 | -48.39627 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 640c194c-9888-3591-b4c8-48dbd3f7e6f8 | -11.62241 | -48.3909 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f3ae6c5-5d00-3be6-80fb-8cc3702cc4b2 | -11.61945 | -48.38555 | 2024-10-25 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f92dd9f6-15cb-3a8d-b3f0-8735896d0041 | -11.42812 | -47.81501 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc4b9c2e-ff55-3e48-9149-7ab13346a71f | -11.42445 | -47.81434 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bf2bb17-8c95-36fd-baa6-0eef06051983 | -11.42371 | -47.81876 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e940b911-8406-3ecb-9f33-02075076be51 | -10.94543 | -47.80039 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23426d88-19f9-3214-8fa5-0e440db505f3 | -10.94468 | -47.80476 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3cc43ad-f0c9-3da7-8cc8-5366bf42c912 | -10.94176 | -47.79961 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c13e8ced-9c6b-3180-87de-691b60c2bb12 | -10.94102 | -47.80396 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21cc36e2-3801-38a9-b08f-b358e6bdfa21 | -10.93735 | -47.8032 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dcac523-e0fe-38f0-bfe8-76d8d5cac843 | -10.9365 | -47.83032 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78c1ae4e-cb46-39b7-8b1c-afe93da5cc94 | -10.93576 | -47.83464 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fb4a05d-f457-3da0-b241-af0e4d884d9a | -10.93365 | -47.80263 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd379086-eb9c-3dea-8894-cef675c1b1d6 | -11.63218 | -48.47026 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6761f6e3-c9f2-397d-ac17-fa531a62a85f | -11.63137 | -48.47498 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79a85a02-1e5e-348e-a812-d083d48810a6 | -11.60235 | -48.59807 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba928785-3b37-3042-9bb7-f197dadd8dbc | -11.59935 | -48.59256 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5bf5098-9393-3b0c-b7ee-c7b0138c8afe | -11.59852 | -48.59739 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d14fd645-af8d-3909-a16c-ea8484e34e73 | -11.59755 | -48.55743 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2686459f-10a3-3a1b-9fa0-48cb6ac8120d | -11.59552 | -48.47854 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 331967a6-62df-30fb-ae8e-c79f71a19b76 | -11.59469 | -48.59672 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c423025c-3e1d-3aac-b5eb-39ecab558670 | -11.59373 | -48.55676 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04dade69-8ff4-3494-8951-b9b85cc367ea | -11.59172 | -48.47788 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 030d0686-f785-322b-a98e-10588f3d3d2d | -11.43622 | -48.47938 | 2024-10-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README44.md)
