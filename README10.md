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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71b4bf16-fbcf-33ff-998d-c62fab55a841 | -4.09006 | -54.28581 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 797e77a0-993b-33c4-a98c-6b16e6676204 | -4.08721 | -54.26543 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2eb55323-5314-39dc-834b-7c52a7825c56 | -4.05102 | -54.2808 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 915a992f-6b7e-3706-86c6-33f7b6ea5c02 | -4.01651 | -53.73869 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2b8271c8-3dc9-38f8-87a1-151f0a38398c | -4.0118 | -54.3844 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| feecf2a4-7e82-3b10-aa08-1cb62c0f6466 | -4.00244 | -54.38574 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ad249a7a-ed3c-3dd3-bbc0-a7cf18704f47 | -3.99493 | -54.46754 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 28673619-7e95-3363-a0fd-db1bdbe84cc4 | -3.9856 | -54.46876 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b719432b-9665-3ac0-997c-daa03bbf2b32 | -3.9781 | -54.3485 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3948efa8-c576-3611-ab52-a2546861e1ad | -3.96271 | -54.44155 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b61bcea6-d424-3896-84f1-b7791fc1f951 | -3.9383 | -46.44991 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| e45e3c20-f8d6-3eee-90a1-7a1d783c9971 | -3.93199 | -46.41015 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| c4e94e24-4045-3f8f-9272-d7e17a6c2860 | -3.92415 | -53.67024 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aceee864-f6a3-350a-81f7-6c7cb7e877fa | -3.89104 | -54.1438 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 547094d1-285f-3842-af6f-cb251c606745 | -3.88552 | -54.1405 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f5238b45-1a59-378b-a81a-bb0e348e60c0 | -3.87145 | -52.1367 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bc886cef-638d-3189-8283-cd8a9050ed00 | -3.8695 | -52.14271 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5465cd1d-548c-34eb-90b8-eed3919aa891 | -3.84432 | -51.88645 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 125c9fb3-9d12-389c-93a4-bf47525ab0fb | -3.82543 | -51.35818 | 2024-10-24 01:26:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9e8d6286-7808-30df-8fac-ddf4867ea333 | -3.76289 | -50.38778 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 844661d8-bc1c-3fa5-9b8b-10b6124f2669 | -3.67088 | -54.26742 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c680f15a-b400-38c1-9e02-1173b4b98781 | -3.66288 | -54.27887 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4c795233-a533-36dc-8ed1-2751f8a03913 | -3.66145 | -54.26883 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 9609c11e-3f72-382d-a700-2c5b5c6f54dd | -3.65931 | -50.13155 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| a172780f-5cd3-3202-9e81-464c1376b605 | -3.65823 | -50.12519 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 78b1daa6-e08c-313b-a37b-085c47fb1f48 | -3.65635 | -50.11124 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4b13c780-20cd-3f60-ae7f-52a8cb63a7ef | -3.65415 | -54.21782 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5c2093a-fcec-3f83-b277-f79594a2859d | -3.64512 | -54.80011 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 16a35c01-f058-317d-9d7e-860d92d7ff50 | -3.64376 | -54.79057 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a249382c-a83b-3cb0-8e17-27003c9ee307 | -3.63791 | -54.68306 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8c086bf6-7d40-37fa-b2c3-d53b04741d20 | -3.63772 | -53.96643 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2e9cd47e-aa0d-3e50-809b-235b85d37732 | -3.62809 | -53.96771 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9cfa9beb-782d-345f-82b1-7f465b31f201 | -3.62628 | -55.51241 | 2024-10-24 01:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 432cc6be-54a5-305c-9e60-1b2df3b27d65 | -3.625 | -55.50333 | 2024-10-24 01:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ec51ade5-f0e6-3a0c-bc83-fe57d20a8d48 | -3.6085 | -55.52084 | 2024-10-24 01:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| babb051e-c0a4-3f69-aaa7-144f3093986e | -3.60723 | -55.51174 | 2024-10-24 01:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f3617ed6-4c29-3990-aae3-79ad5b5725bb | -3.59053 | -54.66622 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 25fb7540-8007-3715-a2f4-5b225894139e | -3.58266 | -53.78895 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ef9b7467-cc6f-39a6-84c0-ff184946dc2b | -3.55853 | -53.75965 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cca0227e-b32b-3433-b32b-f8abf1999493 | -3.55693 | -53.74871 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f400c916-816d-38fa-b875-9361abd43e6a | -3.54462 | -54.74218 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2966db20-11fd-36ff-96cc-f87cb1aacd8e | -3.51145 | -50.28704 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1450db0e-3931-3f0b-884b-566b729f6624 | -3.51128 | -50.28027 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2e7f60a2-df79-3fe6-8b1e-f23a5b9a97da | -3.48122 | -54.67802 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4de3c158-8765-366f-830e-992643b580a7 | -3.47117 | -50.10375 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6d24e39e-b7f6-327d-8f76-d4d10fe43725 | -3.4704 | -52.7975 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3cde7f20-d7b7-3520-9695-ac842c5cd948 | -3.46976 | -50.0899 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3c1ded6e-58c8-38e2-928f-253d51d5871d | -3.46804 | -50.08332 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| bffd74e4-7a94-3d99-a05a-90fca3a05599 | -3.41949 | -54.57694 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 074aba11-3ca4-3942-8f74-7827843c6421 | -3.34973 | -51.64978 | 2024-10-24 01:26:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5de6d759-8040-3f11-9956-b31922a32b63 | -3.348 | -50.15495 | 2024-10-24 01:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| af54b41d-8f4c-3ea5-a496-b8bc28f07020 | -3.22041 | -50.18079 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 34a82f28-2f5c-3abf-a2de-99ece91c03e7 | -3.21902 | -50.16608 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| be3364c6-0ee6-31da-8c5d-70ad91d19e70 | -3.21736 | -50.16069 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| da8c3132-3840-3542-bf0a-19793365509b | -3.2142 | -53.36429 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d7f5157-feb5-3c49-8fb9-fb8a3dafa074 | -3.16037 | -50.47578 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5f3fe93c-3169-3c43-85e3-462d99d5a6bd | -3.15977 | -50.48223 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1f51cb10-c82e-3498-aa20-651fd3bb0880 | -3.15746 | -50.45667 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3024dfff-170b-3265-8dba-4f8847aad890 | -3.15701 | -50.46313 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| db6fbfeb-217b-30a8-9c45-92e91d6e4fc5 | -3.14437 | -50.46504 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| da181cfc-77d5-351d-8e9c-62e0b6f41099 | -3.13867 | -54.2767 | 2024-10-24 01:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e5c50a9e-56c2-3b3a-b28e-649a54d3a2d6 | -3.11302 | -54.1642 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 32c0b25b-7809-30c0-b950-1d45ce8320b2 | -3.11152 | -54.15364 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6540c08e-284c-31f0-a69f-8fb6f87a32c5 | -3.11004 | -54.14315 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 53abfd7e-ad34-372b-b8e1-b2061c48fda1 | -3.10932 | -53.13831 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a6e8ebb1-a217-3c54-bbef-a4985578ddf3 | -3.10752 | -53.12604 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01221ed5-ecf7-3db7-8108-893f46c7070f | -3.10495 | -54.17608 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b975d215-e068-3b7c-894d-2c2e169cca5e | -3.10378 | -53.73263 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6faccf43-f2ab-322a-aaea-16fbd6a81f89 | -3.10346 | -54.1656 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 42d499ba-fefa-3b60-96a1-8e3397f930da | -3.10218 | -53.72159 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4fc6a60b-da9f-3ca8-bd93-6578b8d5ab66 | -3.10195 | -54.15501 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5aeb9dad-224f-3005-b6ef-e5cd03f0e3d7 | -3.10046 | -54.1445 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c1704bc4-c8b3-39fb-8c88-99a593094d7b | -3.09239 | -54.15643 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7e6647e6-8511-38cb-8199-cb819dfc66db | -3.08556 | -53.83052 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1eb77df7-cc4d-3a47-8067-5f196e3b79aa | -3.08404 | -53.81974 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5a347cc7-a74d-37ff-81a3-b51123e6df9b | -3.07579 | -53.83189 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e86ddfc1-6099-34df-bf66-d4dd952313fa | -3.07452 | -53.24647 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e3b6395e-4a98-39f0-aede-2c65cb903d99 | -3.07426 | -53.8211 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| cd234c92-a188-3a06-8daa-ad60c64a3159 | -3.07279 | -53.2344 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d37dc0b3-5301-38c4-8169-64a6d8dd42f5 | -3.07088 | -50.50134 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3afcf525-cf47-300e-bc16-5a0fd960dcc5 | -3.06448 | -53.82245 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4280e13d-0325-3e03-a4de-e76c5c9468ca | -3.00013 | -53.44269 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc3e2528-81e2-396b-b486-0ea7b436bd86 | -2.97083 | -50.43762 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 34605dd7-5d79-30c2-a1eb-748b3f2902c8 | -2.97077 | -50.44429 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 610b11b5-77ea-30d9-a81e-ee54dc651581 | -2.96798 | -50.4249 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| de57f653-ceb5-3c02-a558-76480f900d3a | -2.96788 | -50.41823 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fbbd3319-1417-3689-bc01-03dd44e8404c | -2.95662 | -50.52498 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5262ab46-5398-392e-b795-e9378abad4a4 | -2.94373 | -54.20081 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 75486618-589b-36e7-92c4-5b1235c6693b | -2.93582 | -53.91395 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cddebd7a-8fb6-31be-9f6a-644f5bacf3d9 | -2.93394 | -53.92059 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b099d400-af43-32df-91d7-c0622ec5bded | -2.92944 | -53.87014 | 2024-10-24 01:26:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69494a7b-4a0f-3a96-a136-68fb27e30d23 | -2.86936 | -51.59283 | 2024-10-24 01:26:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2eb17142-e91a-3544-8a28-3615286881b8 | -2.86124 | -51.59967 | 2024-10-24 01:26:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| abbf1cff-4fda-3df6-a124-6893b7f03fde | -2.8591 | -54.59259 | 2024-10-24 01:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fd7861df-2d99-3f13-a07f-2af5567b4171 | -2.84028 | -53.32341 | 2024-10-24 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d7606e7f-ed43-32e0-8693-2110206d4b9b | -2.83043 | -49.14172 | 2024-10-24 01:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7c2eb3da-37d6-3779-be91-368b3c5d5260 | -2.75591 | -54.03529 | 2024-10-24 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 35df92e9-d5c8-3c8e-8e78-f32531578bb2 | -2.73379 | -54.15759 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58a84295-093a-3cff-8744-e7894829b475 | -2.70772 | -54.55525 | 2024-10-24 01:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 53f5db22-6745-33f8-be73-70834ece1082 | -2.61422 | -52.0427 | 2024-10-24 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |


[Clique aqui para ver as próximas entradas](README11.md)
