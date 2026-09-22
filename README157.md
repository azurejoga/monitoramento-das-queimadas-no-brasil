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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b5f6284-d022-3969-85cb-ba617817c7ab | -3.6264 | -58.9228 | 2026-09-22 17:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 6655ab31-d2e0-32ec-b88f-f290412711b1 | -2.5689 | -57.4163 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8d2cc129-57c4-322a-8687-3cd6ef7f2676 | -11.3813 | -44.0554 | 2026-09-22 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 52e5a8fd-e0b0-39c2-be4d-d4b6c3367ad3 | 1.9977 | -50.8605 | 2026-09-22 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 14372324-74e8-3a8d-bf92-3ec40fb766fb | 1.5469 | -55.8058 | 2026-09-22 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7e82f3c8-be15-31b8-9d6b-0053d35e2d93 | -6.8985 | -41.6976 | 2026-09-22 17:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 199.7 |
| 6f9b4521-725f-3b3b-bff6-91292ec4582a | 1.5286 | -55.8257 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 80d5fea6-82a7-3a49-a05d-78f908ea898a | 1.2056 | -50.9766 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5e236464-8997-3add-946f-6c567204ba74 | -3.0352 | -61.2581 | 2026-09-22 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 56251540-db70-3294-8c53-3b0063c0c37c | -3.4463 | -57.9424 | 2026-09-22 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8efb3b9c-bb06-3676-8db8-bdf12cf876bb | -3.6066 | -59.403 | 2026-09-22 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6898dec1-7abc-3ded-9574-056e958b6815 | 1.4269 | -50.7657 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6349d211-274f-35ac-a7fa-e753c72b6955 | -3.8874 | -63.7191 | 2026-09-22 17:40:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 1d1d2807-cdc5-36c1-b733-459503eae754 | -3.1462 | -60.6506 | 2026-09-22 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 97726a89-27a3-3a4f-aa7f-11e4bd3df7ad | -10.4475 | -50.3499 | 2026-09-22 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5d4c1b4e-7046-3f65-a903-f365be7a082c | -3.8265 | -59.3215 | 2026-09-22 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9256d188-4fd0-3316-9739-c52213da5ae2 | 1.3634 | -56.0638 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a107fe9f-1cd8-332e-97f2-5112cbb6569e | -2.9525 | -57.7394 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 94839d4f-1c51-3eb3-a819-a351347e658f | -3.6264 | -58.9228 | 2026-09-22 17:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| a9c12579-c485-3a7b-a2bd-bd088f2f9ffe | 1.0213 | -51.1447 | 2026-09-22 17:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 82.8 |
| e3934c29-7ff6-368e-9495-59de76bf891e | -2.5873 | -57.3965 | 2026-09-22 17:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 07e9fff7-b69a-311c-bec1-35926a509c6c | -3.6078 | -59.0193 | 2026-09-22 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ba1dff4f-ec57-34ad-937f-5b2bd1ca4f16 | -3.1278 | -60.6889 | 2026-09-22 17:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6bcdb367-9561-3f6c-b742-a742f63158d5 | -5.4549 | -60.1582 | 2026-09-22 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 8a6aa396-cdce-3016-8781-8a7ccb24eca2 | -11.3813 | -44.0554 | 2026-09-22 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| aa069eb6-921e-38b8-9312-ece85635b46a | -2.5687 | -57.5135 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 278efcd6-94e4-3b56-8d99-e047c59d08c0 | -3.6998 | -58.8634 | 2026-09-22 17:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5c2b2533-63b1-3b24-9133-b0e6d4bd27f7 | -8.5989 | -44.5531 | 2026-09-22 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3c39ff17-22ec-3ebb-970b-47f3c8d1d12a | -3.1851 | -59.6982 | 2026-09-22 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 285b14de-7c74-3c32-ac75-9be7f784496c | -3.3678 | -59.7521 | 2026-09-22 17:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ee5ebb1c-61fa-325b-8b52-4d71d90c9968 | 1.0212 | -51.1654 | 2026-09-22 17:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 55e76b2b-8667-3219-9050-0f5dd3ec78ec | 1.2427 | -50.7472 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 11abd43e-5599-3dce-9fbe-09bd3f2a28d8 | 1.5836 | -55.7856 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 77b37b91-dc5f-35e6-b6d5-fa86c5aa8a40 | -2.5687 | -57.494 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 378e66f1-c502-31b4-90e6-881479d3bf28 | 1.1319 | -51.019 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9895397d-88a9-333b-ae51-e67fb5b61cf2 | -4.278 | -56.2602 | 2026-09-22 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7b7ab411-0a8d-3a09-b9f5-1501fb900063 | -3.4032 | -60.19 | 2026-09-22 17:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8923a457-0cbf-397f-96f3-14dca6f75c68 | -3.4974 | -59.1944 | 2026-09-22 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 24ca1294-d007-3dfa-aad0-b332c2ab5b6d | 1.2612 | -50.747 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f8674f12-087a-3fbb-8217-aa8c03e5e701 | -2.9525 | -57.72 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 4d2f1f70-11f0-3ee8-86af-776cdf54aefe | -3.4031 | -60.209 | 2026-09-22 17:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a83b52d9-5a75-3fe6-a125-1c08d87a53e0 | 1.5469 | -55.8255 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 841a216a-f4dd-3db4-945e-820f19511790 | -8.8146 | -45.3762 | 2026-09-22 17:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ca23d0f6-8c34-327b-82e2-95c6b7541d1b | -3.0535 | -61.2578 | 2026-09-22 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 46515918-fde0-394e-b613-fb7120509205 | 1.547 | -55.7466 | 2026-09-22 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 08e8b695-04a3-3c79-8115-0fe2a8a09183 | -12.8 | -44.2073 | 2026-09-22 17:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d8b94f79-9a7d-34e4-8237-3140602b92e8 | -3.7364 | -58.8626 | 2026-09-22 17:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 5601a439-6bd7-3004-b66c-c3d71e223e47 | -3.0582 | -59.2797 | 2026-09-22 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e7ea8342-84d1-3bde-bfbf-d172da654b00 | -4.2177 | -63.0789 | 2026-09-22 17:40:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d638e42c-f707-3617-b9bb-21d33beb2c19 | -2.7332 | -57.5883 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a53e4f96-98f1-3912-b0ca-b878042236c1 | -3.7707 | -59.5909 | 2026-09-22 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ddd17ead-54e6-3a71-8bda-eac13101dd11 | 1.4453 | -50.7655 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b9b0ff6b-1e4e-3515-a75e-8216444ce388 | 1.0397 | -51.1445 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e1307537-fda8-35ed-bd30-13faac55dee1 | -9.8118 | -48.453 | 2026-09-22 17:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| d5a1e337-d2fc-381c-ae57-92deffa30bb7 | 1.5469 | -55.8058 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e5f81836-19dd-3d83-9ebc-a62b1eef6162 | 1.5287 | -55.7468 | 2026-09-22 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f8481268-bcc8-3f9c-8257-a40dc58c6fca | -3.4648 | -57.9032 | 2026-09-22 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 42182be8-a5dd-3e97-94f3-c51aa742aa91 | 1.1503 | -51.0188 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c9bba5bd-6c13-35dc-bbcc-bc1d849b9b53 | -3.6449 | -58.8647 | 2026-09-22 17:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0504486f-74b4-3199-a643-28196595e38e | -7.8967 | -72.9507 | 2026-09-22 17:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 132.5 |
| f51987d2-7716-30ec-b3b6-bfd9cd260bb8 | -3.0352 | -61.277 | 2026-09-22 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8b99b856-12d6-33cb-8461-260575ea0790 | -10.7715 | -46.3001 | 2026-09-22 17:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d7694308-3a14-332d-a353-16842f0eac55 | -2.6966 | -57.5889 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 375b3635-4965-30b0-95b0-51cb78328c5d | -2.5689 | -57.4163 | 2026-09-22 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c8ad6c80-23c1-3767-bb9d-1575c88f6c49 | -3.4599 | -59.54 | 2026-09-22 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 48a1da4c-503b-3b6a-921a-b3a6b57a2bf3 | -3.6216 | -60.547 | 2026-09-22 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ff834f54-667b-3a09-b3b3-273a3cde2981 | -10.5748 | -46.7296 | 2026-09-22 17:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 12e1e8a3-6f52-3a12-8f5f-71bb4aa4b08f | 1.2055 | -51.0389 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 15a53bfe-aa1b-3726-bc2c-bad82d537397 | 1.2055 | -50.9974 | 2026-09-22 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 99c291a6-6b2c-3dcd-a49b-3d4e821fd482 | -2.9528 | -57.623 | 2026-09-22 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |


