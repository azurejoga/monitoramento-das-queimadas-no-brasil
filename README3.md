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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebd87be1-fc38-3bc3-a52c-cf8f3f789910 | -11.3701 | -43.6104 | 2025-09-01 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1c90b37d-51ce-3f17-9e69-a90072442a40 | -9.1336 | -65.8627 | 2025-09-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 64ee0154-5a07-3aef-9a35-e233e5a93eba | -9.1522 | -65.8434 | 2025-09-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| eb8af737-1134-3854-9161-9c14584dcb0d | -7.076 | -44.3376 | 2025-09-01 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| f96cb805-49aa-3e55-9263-2b0e306eaacb | -8.7253 | -62.4177 | 2025-09-01 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 19534e7d-877f-3ba2-a36d-a19765ea83bc | -19.0516 | -48.3421 | 2025-09-01 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e2bc248d-51c9-32e1-9ee4-1e461625f94b | -6.8095 | -52.8154 | 2025-09-01 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9be5db2a-8986-3f39-83a6-6182943b0be9 | -6.8281 | -52.8143 | 2025-09-01 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 4191ec12-346f-3ca4-98dc-0e36c68fdb37 | -15.6058 | -48.3402 | 2025-09-01 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| a7dd352f-0997-38d2-a9de-ccdfc60150eb | -12.5722 | -48.2059 | 2025-09-01 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 56a5e1d2-25e1-3e68-9856-b7526795b4f8 | -10.6128 | -44.3284 | 2025-09-01 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6015a75f-58ff-3538-9589-4392fa91e06f | -14.7618 | -46.7667 | 2025-09-01 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 92f94958-4802-3dc9-8e41-0795dfe8f450 | -6.8279 | -52.8348 | 2025-09-01 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 844adcea-606a-39a3-8168-bf7e56dcd7b7 | -8.7575 | -67.3043 | 2025-09-01 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e00a15cb-8dae-3ad5-9e8c-15d630c86c5b | -9.1521 | -65.8621 | 2025-09-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| ce06ad74-9899-3b6e-b6a1-1e1602f9d044 | -13.1644 | -45.2897 | 2025-09-01 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 61c5c2ac-f31b-36a2-83bd-8c712323ad67 | -15.5862 | -48.3435 | 2025-09-01 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 2c1232a3-8fed-3acd-862b-67f84ede1daf | -7.0757 | -44.3606 | 2025-09-01 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 782da939-9c71-3398-8e72-3a4f93430350 | -6.7438 | -43.7898 | 2025-09-01 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 780381cf-7c93-3bdf-bfab-d7e1e32a8e32 | -4.9124 | -43.187 | 2025-09-01 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fb1dacfa-a816-31ab-8dbc-1ced79582d05 | -15.5867 | -48.321 | 2025-09-01 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b6686456-5a06-30c3-812a-9936e60d7f92 | -11.3696 | -43.6341 | 2025-09-01 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8fa37699-d298-36db-baee-46a9e253217e | -11.026 | -47.0538 | 2025-09-01 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9d26be95-97d2-3687-96a1-d1aa0a37ff67 | -6.7626 | -43.7881 | 2025-09-01 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 71f8e780-48e6-3481-ae9d-6b420f9f6b4a | -7.0948 | -44.3358 | 2025-09-01 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 032cce33-ef46-3c8a-930b-aa3b53ae1b90 | -10.0434 | -48.0998 | 2025-09-01 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 905eb331-380e-3b05-b0d7-e14cb8b2e165 | -19.0522 | -48.3191 | 2025-09-01 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 4122b993-40a8-3f98-aa1f-777208b81fab | -15.7112 | -48.9032 | 2025-09-01 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 40c3329b-b72a-3cc4-9395-76372d6f2edd | -13.1648 | -45.2665 | 2025-09-01 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 350062d9-456b-3684-a582-7e7a808ffa6d | -7.0965 | -63.0437 | 2025-09-01 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 78e30dad-8d54-3685-933b-a8457f58b07d | -8.6468 | -67.2515 | 2025-09-01 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 50438dc1-e893-304b-8884-c190fa7dfdcb | -6.8466 | -52.8132 | 2025-09-01 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| e767170d-2ffa-3951-ac36-6c81ead4052f | -15.6063 | -48.3177 | 2025-09-01 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a897b775-9b9e-30a6-951b-121ebff22260 | -19.0724 | -48.3148 | 2025-09-01 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 07facae7-b7f1-31a1-90b6-455b9837a61d | -7.0965 | -63.0437 | 2025-09-01 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6b22bffa-93b1-3a8c-9a37-4fcfe3bd38db | -13.1842 | -45.2633 | 2025-09-01 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| caa4a1d7-55a7-3a84-8b14-6f0103e1779f | -7.0757 | -44.3606 | 2025-09-01 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 6017776e-951b-3871-9964-a16c57517bc3 | -9.135 | -65.5453 | 2025-09-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a710130e-c1c3-3340-a605-6d325d0b834f | -7.2744 | -60.6677 | 2025-09-01 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e5de2f3d-b35d-3ffc-b069-7555c5e726aa | -15.6063 | -48.3177 | 2025-09-01 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d8fa911c-957c-3552-a1fa-1b711393fb8f | -15.6058 | -48.3402 | 2025-09-01 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 27a70d59-5bcc-387d-8563-57edd2d66f5d | -6.8466 | -52.8132 | 2025-09-01 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 43367716-73c0-30c7-8239-42a84c4400f0 | -11.3888 | -43.6312 | 2025-09-01 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e6853913-2d1d-3fc0-98f8-da3ec164e1d0 | -11.026 | -47.0538 | 2025-09-01 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 8ec7d419-a34c-33fd-95b9-92ada2a3a9ab | -23.758 | -51.8917 | 2025-09-01 00:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 0b7b5614-395b-3a07-91d9-3c6e9af7a9c7 | -9.1165 | -65.5459 | 2025-09-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a7836684-3089-38c1-9efb-9998d99ab3ba | -6.8281 | -52.8143 | 2025-09-01 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cc62c148-3b05-33e2-bc1c-2bc03e43e4e5 | -6.7438 | -43.7898 | 2025-09-01 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5888b450-8dea-3d26-ba19-f53a73bb3e87 | -19.0516 | -48.3421 | 2025-09-01 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c015e157-399f-3d70-b62a-9358c5af324e | -7.0946 | -44.3589 | 2025-09-01 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 140f4229-3f8a-3847-b744-ad30f027e4d6 | -15.6906 | -48.9511 | 2025-09-01 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e2fa2322-0d67-33f5-976c-482157be7f2a | -14.7618 | -46.7667 | 2025-09-01 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 73829101-85f2-3914-9d54-e1b69ab4f8af | -7.076 | -44.3376 | 2025-09-01 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 28dd5dfd-a34e-3115-b735-2d66deaacb86 | -9.1337 | -65.844 | 2025-09-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0cc0b9c0-8b11-35b5-9c80-811b09262789 | -12.5914 | -48.2032 | 2025-09-01 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f76aa865-8a47-350b-8c9a-bf9c1b76c592 | -8.6468 | -67.2515 | 2025-09-01 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8567fa90-f2f3-3959-9a1e-06cdd5f55439 | -13.1648 | -45.2665 | 2025-09-01 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e4a1f7d9-e30f-367c-b38b-3845d7fbeb6a | -13.1644 | -45.2897 | 2025-09-01 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 512e61d5-a211-3a29-840f-1e058b9edc8a | -10.6128 | -44.3284 | 2025-09-01 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| cc9ff849-ce19-3816-a8f1-5bc1130a649a | -15.6916 | -48.9065 | 2025-09-01 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e2560aa6-c7c2-34be-a58b-1b23e8923d85 | -7.0948 | -44.3358 | 2025-09-01 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| b27eef9d-5c68-3d0e-9017-46729bea6664 | -7.2929 | -60.667 | 2025-09-01 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 25d8006f-1ddb-3b78-abf5-b173ccdac146 | -9.4432 | -60.5692 | 2025-09-01 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7a89ecc9-bc19-3d66-bb5c-003ca6605f5e | -14.7427 | -46.7472 | 2025-09-01 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e91ac527-f8ff-33b1-b581-d5f48cdfee18 | -15.7112 | -48.9032 | 2025-09-01 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 00ef90d8-e44f-3b5c-8c36-bb7585bacc91 | -10.0434 | -48.0998 | 2025-09-01 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 469058af-ee66-3b3d-96f8-8c0e900ca57c | -13.1837 | -45.2865 | 2025-09-01 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4e9f7380-d48c-3529-9ef0-8cbcc2b202f5 | -15.5862 | -48.3435 | 2025-09-01 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 961021c4-8067-3bca-a1fd-3b503b40e889 | -19.0522 | -48.3191 | 2025-09-01 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 063c05a0-0d0b-3cac-b074-8ce7ace7998e | -15.5867 | -48.321 | 2025-09-01 00:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ce0e9642-9a4d-3ae2-bfa2-f6bb8863f3ec | -9.1336 | -65.8627 | 2025-09-01 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| a5494eee-4427-3f87-87ac-3532c93555b8 | -19.0724 | -48.3148 | 2025-09-01 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 63098b7c-d7fb-3868-9755-c84ff3415c27 | -14.7622 | -46.7438 | 2025-09-01 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e6b8f35f-13df-35d7-978f-6933849b37d0 | -22.3757 | -52.1229 | 2025-09-01 00:50:00 | GOES-19 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 5902752c-0f33-3d15-bcc2-ceb64248723c | -19.0718 | -48.3379 | 2025-09-01 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b10e0829-e1ed-372c-a0b1-7c01b22c0636 | -12.5722 | -48.2059 | 2025-09-01 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3b0d738a-4eed-3a3a-97fa-7dcf712c5b8f | -6.8095 | -52.8154 | 2025-09-01 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8edbb333-0b4c-3735-867b-2714af96261b | -11.3696 | -43.6341 | 2025-09-01 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 257fc990-6fee-3972-ac22-1807ddc5b340 | -7.2745 | -60.6486 | 2025-09-01 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 88eca443-df51-3585-8509-8012fa676b48 | -15.6058 | -48.3402 | 2025-09-01 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 019a2cdf-0d76-31ab-a2e0-fc45372bd0a0 | -15.5862 | -48.3435 | 2025-09-01 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e2af4b7d-2403-3ab4-8912-974c3831b53e | -14.7622 | -46.7438 | 2025-09-01 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4328549d-ca1f-300e-a8db-752e2c3db5f7 | -7.0965 | -63.0437 | 2025-09-01 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f11e25a3-6424-3535-9d0f-6a4ffdfc450b | -10.6128 | -44.3284 | 2025-09-01 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ac0a78c2-abed-374e-90c2-02ccd612baca | -8.6468 | -67.2515 | 2025-09-01 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6483f2ea-a805-333b-801a-d601fb9d2bea | -11.3709 | -43.5631 | 2025-09-01 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2e9f379a-81e6-3cb4-a7b6-eb051aedcca5 | -7.8726 | -46.9952 | 2025-09-01 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1551ab81-4e94-379d-b4d3-863c18f0860b | -15.5867 | -48.321 | 2025-09-01 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5a945a15-d1f1-3d31-891d-587bd61f6eac | -11.0263 | -47.0314 | 2025-09-01 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 235.6 |
| f69f17b0-c203-31a1-9e63-1fac9fa05438 | -11.0256 | -47.0762 | 2025-09-01 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d6ab51ee-58e6-3950-bd13-e26ec571fd73 | -7.076 | -44.3376 | 2025-09-01 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 20929d30-f67c-399e-8e12-bd63ce9ca94f | -7.0948 | -44.3358 | 2025-09-01 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 8adc402b-463b-331b-8344-449e474f4c78 | -17.5956 | -46.6648 | 2025-09-01 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e23962da-d35b-3cf9-8af3-107d823e5768 | -7.2744 | -60.6677 | 2025-09-01 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 75b4fdcc-0d1e-3046-aad9-4afc53595f4f | -9.1337 | -65.844 | 2025-09-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b9a67462-ed1d-3d9f-a888-b687ca31f1b6 | -19.0516 | -48.3421 | 2025-09-01 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 02ba6bf7-d47c-3aaa-9292-cb88a9ece884 | -7.8914 | -46.9935 | 2025-09-01 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e887e2b1-fa42-39e7-8d75-2266de0e56e2 | -12.2287 | -43.8772 | 2025-09-01 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2fc55cd7-b1a8-3584-a4c2-40ec968981eb | -9.2825 | -47.1007 | 2025-09-01 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e903ff91-f027-30d6-b217-366065f6a4e2 | -14.7618 | -46.7667 | 2025-09-01 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README4.md)
