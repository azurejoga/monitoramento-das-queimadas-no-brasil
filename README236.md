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

## Dados Diários - Página 236

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 380f19d8-aa58-3208-8f78-883437795dd6 | -3.01974 | -54.06618 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8d048b87-19ba-33f7-9074-e5247fcdcec9 | -4.13134 | -54.25109 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3d69f6b8-bb70-316b-8e6c-2c913f026908 | -2.49443 | -56.24297 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 27b7f500-6f6e-33d2-9274-8610ee94ba30 | -3.47361 | -50.09162 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13ad01d3-f4f9-3782-825f-674ffb63a60a | 1.33773 | -50.83719 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 750c6403-31d3-3390-960a-cc4745791307 | -2.90577 | -54.0213 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f92df581-7397-3c84-8e2e-a0bdff1c66e7 | -2.45803 | -46.02057 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 27d02d24-71ef-3a31-99fc-ecb4ad1a5ffc | -3.30563 | -53.87481 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| d16d61d0-1252-380e-a16b-b865e679b5ec | -2.99754 | -42.87153 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 706fabc8-192a-39e1-88cd-5fdff45d693b | -3.21421 | -53.88485 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0e3d60e2-7d1a-304f-bebd-6f133fd80691 | -4.93384 | -55.81113 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 78edbcc9-60e3-38f1-9f41-1a1d413dfd50 | -3.48078 | -50.08307 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 7ec57c39-9d73-3b1a-8813-9e9bc8f5119d | -3.28108 | -54.04391 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fce2b97a-fe78-3358-90fe-d10f2ccbafed | -3.03512 | -57.48785 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5cb812c1-2aad-3b6a-9424-ac358d48edb1 | -3.03782 | -53.91442 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 564d7ca7-8ae7-33fa-8099-4a335422e545 | -1.87668 | -53.9705 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4752f8ff-c1ce-3064-af31-a6d9f1042b71 | -2.77818 | -54.06355 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 99fd32a5-a8f5-37cd-a303-7c61d096a7e0 | -3.00369 | -43.84099 | 2026-10-07 16:39:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 344f7479-590c-3790-9223-6fdc1cd497fe | 1.46811 | -50.74976 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2c7b3c78-d561-3162-9123-0c8c9734a962 | -3.54458 | -54.64515 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 319fbabf-2577-3885-846e-a744bf32d881 | -3.30512 | -53.87141 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 11e8ebcd-b99c-38dd-88a2-e1bbb7786769 | -3.28244 | -56.98674 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| eca80bb1-4b9e-3806-9edf-7fbcc324d791 | -3.19126 | -50.56907 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8817ba3-9d05-37c5-83ae-13f4ffff2a61 | -2.87902 | -54.17509 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 075c1604-4d87-31dd-acac-3c45b3e04629 | -1.8912 | -56.25203 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76175f4b-5705-37a4-a8df-cebf214128e5 | 1.76098 | -55.55815 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| af2c812e-574c-3459-b7a5-7bb3b554e8fc | -1.28056 | -55.87097 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 691ed22b-a2dd-3af6-bc4e-c9dbac974929 | -2.56651 | -50.67922 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8297c9a3-a8e7-3fc0-b3fc-77380b5da261 | -2.85296 | -51.5721 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 20c45166-f8ec-3bcb-8990-b453e2251cb1 | 0.37692 | -50.98741 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 4209d10d-213a-3e54-aa7f-2557ca71d78f | -3.15879 | -54.08616 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7b0912f-b5b8-3b8c-b908-75b80b6805d8 | -3.47611 | -50.08004 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 90bfd0f1-0985-3b7d-b578-df16a294ad5e | -0.226 | -48.96786 | 2026-10-07 16:39:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3635b507-de1b-3b44-a0a5-d6197e0371d0 | -2.65779 | -54.31463 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7e25205f-cc38-3b71-8fd2-cd70fb7b04ef | -3.30076 | -54.02738 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ce16e3c5-5cf2-3bdf-a6d0-171a3ff59917 | -3.96896 | -55.82375 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dc479e63-dfc9-3325-bfed-dc86fa40c769 | 1.34512 | -56.13012 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86fb2c43-5846-3635-aaba-41488906519c | -2.77279 | -54.0643 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c4636050-d3b0-3c64-b2d0-d337971be99d | -2.37395 | -48.02384 | 2026-10-07 16:39:00 | NPP-375 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b38f3aa5-f6f4-3a81-8405-aad13e508987 | -3.44726 | -56.94165 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 1dc64bb3-3712-3fda-9ea9-a5207206d842 | -4.10871 | -54.02195 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd347e94-d024-3ff5-85f5-74855f39a4be | -3.22211 | -57.88648 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1456afa2-c01b-3205-866e-e90e4e804df0 | -3.08265 | -54.29826 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| abe70b7a-e0ee-3ba0-a4b3-1f33bbc7993a | -2.89814 | -54.1545 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 348f41a3-6c95-3860-80dd-54252d734126 | -3.02424 | -53.89602 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1fce7d42-64b0-31ad-a9b1-87315997ef64 | -3.05927 | -54.14466 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fd16135-140d-3238-95b2-316b189832fb | -2.77683 | -54.09143 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 726eae98-9790-3129-9d5d-a5c5df10011c | 1.16433 | -50.03884 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 32f080d2-a1cd-3cc0-838f-6f95de0436f5 | -1.71127 | -49.83861 | 2026-10-07 16:39:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4d88772c-0a09-332c-9550-8513fd5e1d70 | -3.05613 | -44.45014 | 2026-10-07 16:39:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5293e549-1b1e-3654-bfc3-50dbc9215c0a | -3.11516 | -53.78421 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d23b1dc6-3941-33dc-883c-a1661b670c11 | -3.81143 | -51.03906 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6420dd00-3668-3afc-9a6c-3ea8b45cccbe | -1.28729 | -55.41828 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9886c25-c60c-3bc5-93e4-ee5a9f5ae7d0 | -2.94273 | -54.10525 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 22df45f3-fec3-3c14-b728-b891f448ab65 | -1.27395 | -55.86748 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 592fd1b1-4a64-3633-844f-b36c0c113816 | -3.27377 | -54.0697 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 63608558-f642-3957-8650-4da8f4359a91 | -2.96243 | -54.21278 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f588712e-e665-37c3-a1a2-384f1d55ad04 | -3.07684 | -54.1445 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4191510c-cdbf-39bd-8426-2dfb4be479df | -3.65397 | -54.06106 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eb0fcd68-9482-31d6-8491-953bb641c941 | -3.63636 | -55.50764 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0cb808da-ea07-3703-8e5f-278c096bfc6b | -3.37348 | -58.05328 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9abb04ec-f2b6-30e3-b1e6-058187442a81 | -3.51902 | -54.66761 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec8412ad-4a7a-3e2d-a4a7-79487da7e4b7 | -3.54469 | -50.10376 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| c0b0a41c-4f5a-3da8-bbb5-b9702c24faa9 | -2.3651 | -56.90797 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 29a8efbc-03d5-3da2-9cdf-09be45aa21ca | -3.30947 | -53.86392 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| da9a0ea8-39e4-3290-bcb6-b8eccc5bb9c8 | -3.43529 | -56.94061 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e6d6fe1c-3d1b-3084-a9e0-08b0efff7f50 | -2.87167 | -54.20063 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ef633d9-9222-3f5b-9787-46d10750e610 | -1.86552 | -44.91052 | 2026-10-07 16:39:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12ec8164-8260-3e67-82b3-bc2125b20462 | -1.56157 | -55.7136 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b3de652-e22f-3f65-b08e-907d6c532974 | -1.79888 | -57.10606 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 00c100e0-09a1-307e-92c8-4de35ebd74ed | -1.46737 | -54.76814 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 09515edf-d87b-303e-976b-369020f1c1b7 | -2.78406 | -54.06616 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| aa05997f-1301-3f4a-8cd7-7cb1181f7de8 | -1.4141 | -53.23246 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2081e209-f577-3e2a-a47e-9a429699dd67 | -3.04996 | -53.92277 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5ce29af0-6649-30b7-8181-13b3a566d660 | -2.99834 | -54.10772 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f5df9aae-8dcd-3dfe-9445-cd73d5353158 | -3.10369 | -54.29038 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a24dc915-b705-3b68-bc2b-15a049b1290d | -2.76554 | -54.08955 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52762267-a775-3798-8e1f-093cc1d0208b | -3.81466 | -52.19346 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e9d2fe13-1cc9-321d-8b9b-38676c13b16c | -3.08826 | -54.29986 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 90b8bc9f-0df8-3353-b2e2-8789da8334ed | -3.22277 | -53.8865 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc9b890b-73f8-3516-80f9-820a5faf8e55 | -3.44491 | -50.62299 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f3ec79c0-6230-3a71-aa50-79e259d1d707 | -3.00629 | -54.12401 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 12cfe9e2-edd5-3a4d-8173-b0a416a718b6 | 1.16744 | -50.04419 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 26fed845-758c-3d82-ab26-1ddf032657d4 | -1.2964 | -54.5613 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d8def6d-aa50-3986-9a03-00ff213e09f4 | -2.78995 | -54.06878 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 8b13457b-72b6-384e-9440-f55f1af1ef90 | -3.54115 | -54.66092 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9295cbb9-ea7f-318c-a0c1-6a9c475c26b4 | -3.05385 | -53.91201 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e03918ec-51ac-3466-85d7-6a30f8dee5f2 | -3.68917 | -55.95584 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 635616db-daef-3da0-b8a5-07ebaf1cb711 | 1.719 | -55.60762 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4b1c72e-5d3e-3444-8216-8e64600330eb | -1.21102 | -49.03719 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b402d0cc-8fe4-3160-a3cb-a34b6abfeb55 | 1.90681 | -55.69859 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21285bce-f6b1-3860-bb89-2d2df2c3b47f | -3.04464 | -57.48369 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 68d9e3a6-33f4-3e7f-a30b-5937cee231cb | -3.43918 | -56.93161 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 95b08480-5b62-3ecf-9925-8307f72fe719 | -3.50098 | -54.66289 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6bb26f76-5b38-3984-b017-b8254c66239e | -2.18758 | -56.1088 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 48986abc-a65d-34e0-abce-2a5b7fd66fe7 | -3.48545 | -50.08606 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 29f1e030-4139-3289-879f-53259d060d26 | -2.58485 | -54.6184 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b19ba3e0-d2b4-311d-ae4e-d05cff5e43d6 | -3.04269 | -53.91034 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 698cfa1d-c6bc-3b44-8db5-ce182aa45ef6 | -3.0565 | -57.51802 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 48134bdb-4da8-3212-91f4-33bae1d91deb | -2.03354 | -54.30853 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README237.md)
