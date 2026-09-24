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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 540c629f-b8e6-350c-ac26-7dfd372f7789 | -6.21749 | -47.49606 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4897e24d-493f-3e3e-b43f-94903d84796a | -6.5449 | -43.08302 | 2026-09-24 04:44:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a13f3039-4fa2-383c-811c-65168780c726 | -6.31539 | -43.34291 | 2026-09-24 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b5f8aa7-4e6c-383d-8dbf-f6a0f7bb3868 | -6.57717 | -44.14164 | 2026-09-24 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc7ff1a5-6679-35f4-8e02-7ace31ab0d59 | -2.94381 | -54.08722 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ac9e919-ce2b-3b03-8848-fd71179eeea0 | -1.27115 | -57.03646 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef6c7dea-4824-34cc-af85-c6c822e0a889 | -3.00821 | -51.53629 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca2ba163-72fa-39ca-810e-07608a323027 | -4.99388 | -45.54708 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 138ffb5f-40b3-3995-80e5-3a6118c88ea1 | -3.0437 | -46.9245 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7526084-63ac-3dd5-bac1-e3ea75da4b1c | -1.07942 | -49.21217 | 2026-09-24 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0a6a800-2a96-3571-a781-35ab41ca8287 | -4.75563 | -42.73815 | 2026-09-24 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4d92884-bedc-3598-99d4-e41a0781abed | -7.1983 | -47.45406 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 474fe848-a677-30b2-b963-eda99e3f1d99 | -3.21052 | -53.37304 | 2026-09-24 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f36ec3-eb08-36ab-ad45-d26f984f8c20 | -6.21084 | -47.49501 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a729387-6745-366f-86ee-47ab88c78620 | -5.85214 | -49.77439 | 2026-09-24 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b50a00d-c4bd-3645-a0ac-c565692eef6c | -7.67758 | -45.47091 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4b50672-8472-3560-865e-6d2448ea3f77 | -3.71727 | -49.04691 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b09246-995a-30d9-8fb5-532061981d9b | -5.84594 | -49.87819 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce67dc75-705a-3ce5-9ac3-195015f6c397 | -2.73875 | -51.5437 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0495456-9653-3886-973a-aa03032cdf06 | -4.02698 | -52.06683 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00da64d5-acc4-36c1-a5c5-7e89c08455a3 | -5.8556 | -49.77494 | 2026-09-24 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb9641e6-a971-35ff-9312-ccd191e656bb | -6.27387 | -43.27099 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f7e4653-235b-38df-a37c-46b6a073f489 | -6.19976 | -47.5004 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74bc405a-3840-3f8c-b09a-9682663ade15 | -4.44066 | -55.06398 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e180d917-5042-38cb-9d35-a4d9bde9fa7b | -1.19641 | -54.14351 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f43993f2-cfef-3a3d-8ecb-9983bb353cdc | -4.4508 | -55.03344 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db24428c-c094-3164-9c7a-5693fee0a436 | -5.83071 | -50.21611 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27aab7b7-c4af-3ee7-88ef-767b03d8da4f | -3.70686 | -54.19334 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1f428d0-3152-3673-aaab-3c30e64ffd9e | -6.05279 | -53.28572 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e230f08a-4b20-341c-b546-66a037934d05 | -6.60819 | -43.72915 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a06e4dd-1861-3166-9ab7-aee180d6a53f | -3.4494 | -50.08588 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2752b5c5-ef69-38ae-bf8c-a31af101924c | -5.72055 | -49.83144 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3d18f20-facf-3ae1-9231-72c9a1d438b1 | -6.77347 | -42.36692 | 2026-09-24 04:44:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 49b6de4a-8047-3060-b322-d46fb8419db7 | -3.16125 | -57.68972 | 2026-09-24 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 242d4e18-a533-3bb2-ac51-d93dd5be5ce0 | -3.18103 | -48.01686 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f45e7e6-0df3-3388-8da9-9ab62385f15c | -3.71149 | -54.19402 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6839bafd-80cf-319c-8d42-74ef4a127b2f | -2.94086 | -50.49026 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4cf2dd5-2349-320e-8690-66bd8b75c10b | -2.94308 | -49.19553 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09c286f4-b892-3aa3-8812-1dbe6d3e94d4 | -3.00507 | -51.53085 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6825a567-080b-33af-b22d-b00c4bd5245e | -6.12725 | -43.74802 | 2026-09-24 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5d026d6-0b0e-3ee1-aa53-2245ae75046b | -4.98985 | -45.55031 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 828df893-db5a-3c70-b807-4d011c21cb20 | -3.45298 | -50.08648 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66b7352c-e249-3402-bf23-417120a8755e | -2.88203 | -40.02001 | 2026-09-24 04:44:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe3aca96-2ba1-34af-8758-98f9eaa337ea | -7.12632 | -41.72287 | 2026-09-24 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 35c95c2e-9dd4-383d-b9ed-79a116d75a88 | -3.68922 | -60.55947 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 506e1414-91bc-3b65-85b4-850c8e100f98 | -4.42337 | -55.07776 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdef10ea-212a-3ce1-bd8d-0cbe957141b5 | -2.70941 | -57.51444 | 2026-09-24 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f09fe0c-3586-361f-a0ce-36e60a92fa6a | -3.71919 | -54.20467 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4e665de-880d-3206-90dc-5b4c4e2b24ac | -1.2721 | -57.03387 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f635a398-ca02-3759-81c1-cd2bb5e10921 | -1.60245 | -49.81601 | 2026-09-24 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e97e98-8ec7-31db-a1df-48bc3475651b | -5.78625 | -50.20086 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe9790f8-4920-32e5-a14c-95244498eef3 | -3.15899 | -54.5998 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 68460f1f-724e-313f-8be0-72cc356fe224 | -4.02616 | -52.07192 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fea4045a-551d-39fc-acd1-0a514b2468b5 | -7.68992 | -45.48529 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e2f747a-4495-3337-8ad1-52160847c418 | -3.55565 | -43.46102 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8531c980-04b5-3040-ba1e-6b68684c23de | -3.44711 | -50.07722 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4bdc6b0d-f892-367d-be55-ebbd50fbabe3 | -1.21846 | -54.5534 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f507d974-c4c1-3a0d-a0b4-fd2d813ef12a | -1.79722 | -53.74397 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfce01a-8a94-378e-9c90-0f01f0fc90a2 | -4.9933 | -45.55083 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b98c921f-6638-3c18-bda0-7a3ac9852776 | -3.04703 | -46.92502 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02dbc12c-05df-3d88-8b52-c58bb1751ccf | -1.52148 | -48.03564 | 2026-09-24 04:44:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01a5f667-8389-30b1-a27d-c5ab37a2df15 | -6.61587 | -43.73027 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f287bbee-ad6c-3048-b84c-de5ee743d92b | -5.22901 | -49.22422 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eab4b3b8-f303-333c-9451-2637092ddbb2 | -3.5519 | -43.46045 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2a23ae2-8453-358d-8297-910dcd42023b | -7.42168 | -42.63668 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c3f3834-147e-3dbb-9963-907b9495df67 | -6.43298 | -48.46459 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 00747adb-0f80-3f2c-9668-26f03da97f89 | -1.62578 | -54.91224 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1af37c31-b461-3941-84cd-a07b8e3bd62c | -4.5396 | -54.96821 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f527214e-847b-37a6-ab27-038f4c78bbef | -6.89346 | -43.74891 | 2026-09-24 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a115261-c61d-347b-aeeb-3a03a0625c19 | -3.1799 | -48.02389 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b332914-c435-3547-b6be-92246638b270 | -5.77244 | -45.10046 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6be5d9e3-fa0b-329c-afb8-da09dee4016b | -5.86546 | -51.95566 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5823fb6-2ef5-3fbf-ac1d-371edd92b8ef | -5.77024 | -56.52079 | 2026-09-24 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9ff97a-ef34-3666-ba4c-e32a97b38ac6 | -6.41456 | -44.49208 | 2026-09-24 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91a2c369-011b-3254-a810-5ead5e910903 | -7.67221 | -45.48259 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed1e3b4b-0e88-3422-bd9b-fc397884495d | -1.27764 | -57.03338 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 817f492a-1669-3a5b-9a42-061c2047f210 | -5.87616 | -51.9386 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04bd8787-cbf1-3657-8210-43e97437e162 | -3.71786 | -49.04321 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d6fcb2c-7186-34b0-8128-30164f48ddc0 | -1.27662 | -57.04294 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1db1860-a26c-3b19-ba66-f81912044a98 | -3.03567 | -50.43423 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 880b8f24-7291-37ee-9fbc-39f3adf757c6 | -3.16322 | -54.60263 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e26dd6be-e736-3372-8da0-c2980019b5e2 | -7.61892 | -46.7933 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9159ee3-eef2-377d-b355-893be040f5ed | -1.19536 | -54.1447 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2bc9aa72-1e1b-355a-9ee2-db8501826343 | -3.26876 | -49.14567 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d454d67a-1731-3060-8904-934a13f8ef60 | -7.4603 | -44.53964 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0153e405-bb6e-32ae-86db-667e4646ad88 | -5.23435 | -49.30035 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2580889f-7afb-359f-bf28-3799fe20028e | -7.47787 | -44.57344 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b1ab0cc-a24f-3915-b57d-806430ac24fa | -1.63067 | -54.91779 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c9158b7d-eee5-3a43-852c-3cfaf9d5824e | -7.19611 | -47.46805 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe2d0b1d-ac0c-3271-8434-2933636af2a4 | -1.83649 | -54.71717 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5ccfd012-74d3-347b-bbc4-175510f01465 | -6.6669 | -52.31669 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f77542-cff8-30fd-98b5-e73277411e0c | -7.29041 | -45.41564 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a54eff38-7a45-3160-85b3-1d3551587fd2 | -4.41855 | -55.07681 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 205dc08c-82f9-3c2e-b097-4b2b2266f231 | -1.26012 | -54.67931 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81df26d5-786a-31c5-816c-052fcb334161 | -4.81514 | -50.73016 | 2026-09-24 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b065d130-726c-3452-bdfc-98f9f9b30cdb | -7.5047 | -39.27681 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90a01574-aead-3add-9f43-52dd80f4aabf | -5.78959 | -49.18937 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2600c548-7527-34e4-9cfd-5732754da892 | -2.79936 | -51.36794 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d46933de-62d7-37f8-938b-b31df95a8d99 | -2.83187 | -46.70733 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7a8113d-6a85-3706-adec-bdd58946c196 | -2.63396 | -51.69985 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README45.md)
