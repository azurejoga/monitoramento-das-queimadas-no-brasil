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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ea0bfa5-43ee-39bb-8538-7cf297d4c700 | -3.3799 | -61.30086 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d337d8a-75ad-3c3f-9915-57343f1a99e4 | -3.3959 | -54.06359 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6935418-2e28-30c5-af7e-6323d304199e | -2.65884 | -59.76263 | 2026-09-20 05:59:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e12119f-553c-32fa-924a-322cf385b092 | -3.48245 | -59.59132 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a739a018-5c9d-3a58-bca3-b49e3227b0b3 | -6.45795 | -59.97825 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96fddc34-ec29-3ba2-9eb4-595759bfc411 | -7.57711 | -57.68661 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac15fba-ad69-3bc4-b4d5-ed1528e888fa | -5.84978 | -53.52625 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29ebe519-cb8a-3bf8-b819-091df016f7cd | -2.88516 | -57.79199 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73217d0d-ba43-35d5-bd1d-be4f2ff71c25 | -3.34375 | -57.86503 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90314e32-ab3f-3b6a-832b-cc45ab06f5e3 | -2.88164 | -57.81552 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df749c36-2c56-39be-928a-dba186d6a317 | -7.55681 | -61.33276 | 2026-09-20 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbcc75aa-3230-3137-9e9f-3ca5e77745a9 | -3.40954 | -61.30156 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e07aa202-a037-3d2e-8036-4410e7674b60 | -5.74159 | -57.58186 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 687f57e6-2f2f-365d-9813-4cf5f87e0208 | -3.40122 | -54.07031 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 007838d4-4cee-3877-a22d-7556c143bc3c | -6.44804 | -59.98161 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da888a83-6f53-3d33-a5a6-b232fc40acc5 | -6.10072 | -57.6295 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e47bcec7-a807-3fac-8cd2-c077c0054e9c | -3.69096 | -60.60186 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5920e40a-c4e6-3c61-829a-f5e31914c27f | -3.39476 | -61.07145 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 113e147e-ef81-389c-a018-148b3f261853 | -3.68857 | -60.61739 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d13f4e0-1b74-32d7-8d6c-1e4741379fbc | -6.45724 | -59.98306 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f73d6885-0ce8-3cdf-a67c-5f0e9ae6c27b | -6.49093 | -58.37966 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 034e5a74-8bee-37ff-aea9-51d43f6d823e | -3.37588 | -61.30024 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 997605c3-f35b-3af1-bd79-3c6311f5cb78 | -5.81484 | -57.54336 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d683fe78-f0e9-3ff5-84cb-2b9297516ff5 | -3.72218 | -60.62254 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b44c6305-2d57-34d6-a0e7-be039b2c5afa | -6.73291 | -55.07505 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cb136b8-1c26-39a5-a2e9-57da356fd107 | -5.84549 | -53.50563 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b225395-3d11-3cf6-b27a-d2023a4a13c8 | -5.8531 | -53.55387 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 711a2c81-72a5-3bcc-ab99-7140c239a3dd | -7.57692 | -57.68371 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7577ed1-f1f5-36c9-a1ff-319e5c3f3ab8 | -6.1012 | -57.62607 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a6f3bd5-87d4-35d5-90cf-2296ebfede6d | -6.94283 | -62.91846 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e10170d-fbeb-3c68-9460-0e4455152a53 | -6.07047 | -57.72913 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a831a37e-cf9d-35fc-9321-c6cf7209efe7 | -5.84799 | -53.53941 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efbe810b-5ca1-3c3c-9d2c-bfa52b7ba510 | -2.91561 | -57.79664 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60d31a96-1f03-3ef7-a1f7-a3bac2f70910 | -7.5574 | -61.32878 | 2026-09-20 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 769d1e6f-26d8-3221-aea2-ec769b0f2553 | -6.49609 | -58.38033 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddbd0a0a-9884-3da4-96b2-886ee5d34b09 | -4.51581 | -55.46817 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9ec30a4-d163-3df6-b9a1-25d8ab4956c3 | -3.34687 | -59.86583 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a851d06-b486-3a98-b20d-5fc5ff9081a2 | -7.00046 | -62.95109 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04031b9-1e46-3fb3-9333-1ab5aca07cfa | -2.58807 | -59.99393 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 073a44ab-ed90-3955-bb58-8fa9985955f0 | -5.83588 | -53.52426 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04700822-874e-3496-9a5e-b2cc98735025 | -7.59582 | -55.71244 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3c27c61-5bed-31eb-8399-652770441c27 | -3.00139 | -60.80072 | 2026-09-20 05:59:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8f9d5d5-1380-39e4-8be2-5f5597474282 | -8.42359 | -54.7289 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c030f6a0-bb82-3c33-9756-6e8dc076cd64 | -6.13173 | -59.94275 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bcb8609-a889-3fe3-82fe-67c90d9d608c | -3.23318 | -61.20744 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8305b977-0bba-3031-bb1e-e4c860f936bc | -6.19423 | -55.44798 | 2026-09-20 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 269af755-d546-3c9d-84b1-8672837d663e | -3.35703 | -59.8586 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 727f3ff9-6611-3627-b209-46ef6c3a734a | -3.68976 | -60.60964 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d925518-870c-3995-ad3a-e5224a97ecd7 | -6.09886 | -57.68221 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d977cb0b-26d4-3385-a160-d981e1f7cca9 | -3.08317 | -61.18425 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0fc13f3-3b61-38ef-9885-9fed1c03cb4e | -3.72699 | -60.61926 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d191f651-d59e-36a3-89f5-21c77e8d859e | -3.68553 | -60.60899 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef34835-38ad-3d6e-800f-91da7e10b8a1 | -7.57592 | -57.69075 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2742b950-a1d9-3ce0-9213-b6b20aa53d7a | -2.97026 | -54.76587 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6942059-eb19-3939-bcb4-d47b7f02aa24 | -8.18002 | -54.7465 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93da3783-21cb-3967-9f6f-067c788f36e7 | -3.39547 | -54.06399 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c6a2f1-1d02-33a0-8d5b-39cc30bf1219 | -2.97807 | -54.77139 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a6d3278-dd0e-3317-bc25-f0fc30810da8 | -3.33866 | -57.86426 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe49eba-f1d4-3dcc-ac3d-238a194b7f1c | -2.61069 | -54.75826 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3fd25595-8b27-36e1-83b7-6821f21168d8 | -3.38447 | -61.29799 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4acbdd7-25d3-3ac1-845b-4dc967232e73 | -3.12604 | -61.25547 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f231c40-72bf-3357-8974-ee965ccda523 | -2.88252 | -57.80964 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7070cd6-7f32-33ea-8b54-bfd16d119ac5 | -3.08665 | -61.18835 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba005f8-868a-3598-9026-7844a97de256 | -5.76578 | -57.45277 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 942a1328-771c-38ef-a3c5-808a18ad56c6 | -2.58373 | -59.99333 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10cda007-6171-3bf6-8530-1a0d602ba7d9 | -2.87833 | -57.80297 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b491c1a-5e7a-34a4-9fb7-3e163eaecb9c | -6.4448 | -59.97152 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06652007-a63f-375a-aac7-baa96f743ce0 | -2.79686 | -59.89017 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a65d9232-ace2-3724-abfa-3ad1aaebc207 | -5.75282 | -57.58015 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa09be25-4dd7-318c-bdba-2de789a85166 | -3.86446 | -58.89289 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a16a4e3e-20db-3d45-a59a-f5d13c33c5ce | -3.68732 | -60.59732 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1df5d53-c824-3bab-b445-33304e59f6a9 | -3.44563 | -58.23192 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da0c6088-ef2c-3c11-8f14-74337ada8a7e | -3.45367 | -58.21715 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f9fa1bd-8ac2-3d8e-b2fd-0751b167ecf6 | -3.4465 | -58.22633 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 712ab792-f897-3ef4-8ab7-bb3ac56bd963 | -2.88626 | -57.81921 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a4ea140-94cd-36ce-87a8-2c3ace8b8c11 | -2.91606 | -57.7937 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb230772-c480-35bf-a50f-184d0b47c79c | -2.88604 | -57.78613 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d98ce6db-2120-38c7-a0d6-8f7395e53d39 | -3.85968 | -58.89216 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ff30e7bb-c905-37b1-905d-72648720863d | -3.86522 | -58.89201 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c0ccb63-cb8d-3302-a68e-2c346b17238e | -7.56108 | -61.33339 | 2026-09-20 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81f1680e-bb9b-3438-9836-a205e99a917e | -2.50123 | -56.59984 | 2026-09-20 05:59:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afceea5e-d3ad-3fb0-864c-993c61f7a7bd | -5.84531 | -53.55906 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c8d26f7-2a79-38fe-bd22-e797ef81b1c7 | -3.6916 | -60.62579 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd607fb-8cba-32e5-bc0d-e112499628d4 | -5.76526 | -57.45641 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3dd025b-425b-38ae-8455-9816c8fe60d0 | -3.39799 | -61.29626 | 2026-09-20 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42149575-c57f-346a-84ff-bee01d611545 | -5.74207 | -57.5785 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1fd8324-b2a3-3302-a404-f1fbc6590d87 | -2.97881 | -54.76651 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 196d19ce-4da9-3aab-9de4-e9d1d1bbb429 | -3.00918 | -54.17675 | 2026-09-20 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2af9cca-3378-3061-8bab-c69a0c7e3a87 | -2.71246 | -59.76637 | 2026-09-20 05:59:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cbad6e8-91be-31f9-8652-f48852884e9a | -3.44066 | -58.23117 | 2026-09-20 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0b23b05-65ce-30f9-8cc3-dfdccdf09c9d | -3.68673 | -60.60121 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3da0859c-fa0d-3d29-881c-2a2040949d09 | -3.69699 | -60.59081 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 307de553-51a0-3511-8848-ce994072ef45 | -3.68916 | -60.61352 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15987568-d09f-3345-8c63-69b3bac0349b | -3.68434 | -60.61675 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8ed0a12-03ba-3d18-b2d0-b0ff1adfd620 | -3.36327 | -59.87705 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aee24357-cd2e-3709-9563-c91343ea4179 | -3.69516 | -60.57455 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4456ba35-0661-365f-8a86-c8fa79165c0c | -2.8792 | -57.7971 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cbc65b1-467c-398a-9af3-fb2cabf59ffe | -6.4402 | -59.97078 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9739b00f-0cdb-3bcb-a04a-340db41ede43 | -3.86044 | -58.8913 | 2026-09-20 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b854bf38-ce72-323c-aa72-b0988b66cdd4 | -6.43953 | -59.97543 | 2026-09-20 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README102.md)
