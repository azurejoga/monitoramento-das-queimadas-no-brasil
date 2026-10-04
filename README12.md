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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0661692a-98b9-3f57-b798-c0f503c69365 | -3.8053 | -50.854599 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61310801-43eb-3976-bc00-7d4341820cf3 | -3.0976 | -53.729 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d084ed7f-fbaf-3371-9a1d-d96813f86d1e | -2.8814 | -54.133499 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85c9ccf-4b6b-3437-b6db-3942d758de4b | -3.0497 | -54.153599 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf9cc1d-6e39-302e-8e05-64ef06eb14a0 | -3.2045 | -50.744701 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d294b1d-3775-3544-8680-d36d13482636 | -2.998 | -50.4692 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4216bd26-8ebb-35ae-a891-cbcb259fe96b | -4.8183 | -49.8736 | 2026-10-04 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58047c55-f8b1-3302-852d-1dc22eab5476 | -5.1865 | -45.4846 | 2026-10-04 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee070fe-7b85-3054-93ad-487a383cc474 | -5.7376 | -45.146999 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f43c985-b175-3622-8238-9d73116ee7d9 | -2.5825 | -51.856602 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5ed3530-579b-3267-a96a-06f3e6f36b1b | -14.57392 | -52.88213 | 2026-10-04 00:35:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9ab7a9de-dba4-343b-b943-3bbdf0962b5c | -14.57179 | -52.86846 | 2026-10-04 00:35:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b3b46be8-2aa2-3988-998b-cd4e68cca30d | -15.91508 | -56.34283 | 2026-10-04 00:35:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 1b0d87c0-aefb-3669-9fba-1505f4c8c20d | -12.77174 | -62.05277 | 2026-10-04 00:35:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9f44b92f-4731-34f0-b543-653c19271f23 | -12.19127 | -57.11794 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a3b2bb17-395c-3edf-8f56-11447d2e17d7 | -12.16055 | -60.74662 | 2026-10-04 00:35:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b76208e5-dab2-36b6-8a06-e9ef5d3c7f0a | -12.17985 | -57.10109 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c44c777e-8f17-3d04-a37e-19c523b41bbb | -21.5667 | -56.74183 | 2026-10-04 00:35:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 077822d7-d3af-3652-a99a-fcb281167bc1 | -12.18113 | -57.11016 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 76ca3b79-1841-3030-911b-4af3d0883ded | -15.61538 | -52.81242 | 2026-10-04 00:35:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13d96609-95b1-3c3e-b80f-620d42af27bd | -12.19 | -57.10886 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 302397ae-6c20-383e-938e-06eceb897e19 | -15.91637 | -56.35204 | 2026-10-04 00:35:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3eb7b791-4b37-3a57-bddb-42c98c2a3bbd | -12.1069 | -57.1738 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 08bba13f-eb67-381a-90fb-560bb8510d99 | -12.1309 | -63.17304 | 2026-10-04 00:35:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7217acd8-93d9-33cd-8f62-e2f6ba546e96 | -12.95157 | -60.87193 | 2026-10-04 00:35:00 | TERRA_M-M | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd31a70b-9f56-3b7f-b812-32dc3a723acc | -12.88216 | -61.72184 | 2026-10-04 00:35:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9df247e2-8a72-3867-a4b7-872c08c998bc | -12.89276 | -61.72047 | 2026-10-04 00:35:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5f5acdc3-3acd-3e62-83aa-01386d90c6e5 | -21.56542 | -56.73214 | 2026-10-04 00:35:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf921d26-6b08-38a5-a4d7-4f1fd8ee1126 | -12.20014 | -57.11662 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e7fd1a01-e9d2-395d-b849-3504ceb26ea4 | -12.13812 | -63.16645 | 2026-10-04 00:35:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 11f0c6dc-a0ad-3edd-92f1-316c7410fb1b | -12.95115 | -60.86629 | 2026-10-04 00:35:00 | TERRA_M-M | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc491394-ef5d-3c1c-95c9-9f0d9c63d03c | -12.20141 | -57.1257 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2306056c-7250-3dd5-964a-39a2f9dadcb1 | -12.77004 | -62.03881 | 2026-10-04 00:35:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7a28c46b-d314-3b62-80cd-f155b046c120 | -12.14005 | -63.18302 | 2026-10-04 00:35:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5c44c4d9-e9c6-32ba-b515-80d33d189749 | -12.10563 | -57.16474 | 2026-10-04 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ac1b660-1e98-3e81-b60e-efaa0bb95e4f | -2.81583 | -54.09156 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 31a0f3aa-619a-30c9-9fe8-283ce466fc3c | -8.54423 | -67.03053 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2525ec64-d858-3ea6-b577-1c5d33d2d25d | -2.84734 | -51.28364 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| b03b64b4-b3aa-3f8f-99bb-e9dba7a6ffe5 | -3.06529 | -49.53389 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 4c6274cc-02d5-398d-be27-1cbd83e735f5 | -3.12812 | -53.76386 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d5e62c99-0359-3730-b40d-6f0d31dcb41b | -2.58843 | -51.90036 | 2026-10-04 00:37:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 93961706-4ee9-3e1a-9ea1-7ecce5f7640d | -3.1749 | -54.07869 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| ec73d5de-3c45-3eac-8b74-74adbe4db93a | -9.70405 | -57.46035 | 2026-10-04 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3f6a407a-0680-3a3f-8b25-26dba7348434 | -5.87156 | -55.70626 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 0fdd4dae-978a-36fa-a6b6-82c6af5a37c4 | -10.83912 | -57.20576 | 2026-10-04 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d284dea7-7280-3c8d-b2a9-3b80909a2f39 | -8.54773 | -67.05978 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| fe2a0211-1fc1-3d69-a953-2d44ff534a94 | -9.37898 | -59.04712 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a45ad1fa-abb8-3285-805d-95bb9a592962 | -4.46419 | -50.98751 | 2026-10-04 00:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 204e815f-0f24-329a-bcf4-e727b92a7b3e | -9.08007 | -61.15488 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1c3899be-9fe0-35b2-ad9f-46fefadd9217 | -3.77844 | -51.39272 | 2026-10-04 00:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 95706797-1644-370e-8df6-005ab6ba4b08 | -3.97495 | -59.34508 | 2026-10-04 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 498d2ca3-cdc6-39a0-b203-b6a3e3144bf3 | -3.89697 | -49.69763 | 2026-10-04 00:37:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8a19faef-2828-3137-9dde-d088cdd4f9d4 | -3.06763 | -49.52847 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 97bd9ead-9ba0-36ef-a127-574380fe2d65 | -9.46949 | -64.34014 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 41c4a6ee-7dcf-3ec1-b70d-ca11e90cfcee | -4.81891 | -49.29188 | 2026-10-04 00:37:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 1653db6b-796e-3c9f-92d7-2b6d6bec1015 | -3.51892 | -54.60814 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 8f343ff8-2760-3379-b251-660a4e7e3d85 | -8.5943 | -66.81598 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 952bd18f-a76f-3291-b109-91b6e5cfbb01 | -3.038 | -54.23152 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| bcf575db-987e-3870-8762-c32e00607e61 | -2.9798 | -54.08482 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 00fbee6c-191c-3461-8ee5-ebe5d31e2b3d | -2.79417 | -54.11225 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ca533fce-7d0b-3172-8292-b67a655bdc02 | -4.29628 | -50.2927 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ba3cefd1-aaf1-31be-b753-6d6f891f8c87 | -2.83236 | -54.21019 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 36892122-0283-3ca9-99ae-d712e071697e | -3.27942 | -53.82646 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| cf3558ff-b4a6-3608-a452-6b121daf6b94 | -6.00319 | -53.51848 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| db40ea03-cc66-3f00-a7d4-e106052fdd32 | -10.22328 | -59.09515 | 2026-10-04 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 248b59a2-e2ca-3b5b-9d96-92fda51964db | -3.49955 | -59.17299 | 2026-10-04 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b834d721-c347-3a94-8df0-67a97d6f01d1 | -3.07104 | -49.57327 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0c7675e5-ae46-30b1-ac63-603b82107be6 | -9.88881 | -65.1347 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d445a79b-62f3-3f92-a172-9642f67fc754 | -4.78669 | -55.71354 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f61433d6-6c61-37b7-94f4-950636c59620 | -4.96298 | -55.86507 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d348cbe-9ed9-3831-a931-cd09b777efc8 | -5.54379 | -49.77009 | 2026-10-04 00:37:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| c94ddc42-791e-36a4-8253-ee88e330394d | -9.69516 | -57.46165 | 2026-10-04 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef188a57-d505-3c6b-8c45-c7a97e714010 | -3.05448 | -54.17779 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b57836a4-d703-323b-9eb0-a243558bc211 | -3.10785 | -53.73575 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 245.2 |
| 765a8051-481a-31e8-b0ef-ae508579fe0d | -2.59508 | -51.8457 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d16fc5c2-1546-384b-b0bb-d48e560f755f | -9.89016 | -65.0108 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 043ec950-3bcc-38ee-8228-0620932767cb | -10.34511 | -58.48993 | 2026-10-04 00:37:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5f75a96-8add-38aa-9d30-e9de64e3d4d1 | -9.08148 | -61.16568 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2f0b47b4-34bb-31de-a64c-510f092d2d99 | -2.599 | -51.87205 | 2026-10-04 00:37:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 33141c75-2358-326f-8ea0-dccbe1b22de2 | -4.29125 | -50.25994 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 191.4 |
| 98c69e6f-1769-32f9-86dc-bf6678ba8d95 | -9.12148 | -65.89095 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| dcfa4727-67b2-383a-9615-54dcad5fd300 | -3.51901 | -54.61717 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0922f41f-0465-3c77-9704-2cd9425c0d58 | -9.48522 | -64.6855 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6f5876b1-0c2b-3821-9277-3b6b269ecc17 | -10.9576 | -60.90818 | 2026-10-04 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 78cc8fce-a75d-32fc-8a18-d2bad861b555 | -3.18172 | -54.08345 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fa19fa0d-e1b4-34c7-96cd-07b6fc38f6dd | -10.53866 | -57.96792 | 2026-10-04 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1b3b8dce-33bd-36d4-902c-1c64f3ba0c5a | -9.13371 | -65.4603 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 98b1e3f3-717d-3e42-aa79-bf00d28723c0 | -9.12548 | -65.46681 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dc069297-bcae-3574-8d82-a1b2e63c13c8 | -4.28039 | -50.2952 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a1c2bbbe-a4b0-3b45-a9e9-cb9903f48c91 | -2.90237 | -54.14325 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1009a3a3-89ce-3c69-b4f5-80a4f4da83c3 | -10.99369 | -59.13751 | 2026-10-04 00:37:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f9fb9396-2fe6-33fb-8c52-2a3d26b39bc6 | -2.79894 | -54.10597 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 881bafec-52b4-3260-92ce-a8fc6a17fd8f | -9.08973 | -61.15357 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4e4de3e0-ad5a-3cd1-819a-68973fb10c86 | -3.11582 | -53.76564 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 728e69c6-a372-3821-9d2f-507ace3dcd20 | -4.12912 | -54.14926 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 398c5bc4-3618-3bc4-9e4e-a40390bed659 | -3.0848 | -49.52584 | 2026-10-04 00:37:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| ca17e65d-1f15-3267-bb9f-c6a21589c4af | -9.02079 | -65.69386 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7bad6717-9f1d-3564-a843-e41c23dd0a57 | -3.11311 | -53.74759 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 314.4 |
| c684315d-788b-30af-af6e-0d7e3a217e86 | -3.93748 | -55.84846 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acdeb1b9-0564-3208-b3b0-ae4145dec098 | -5.99687 | -53.63908 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |


[Clique aqui para ver as próximas entradas](README13.md)
