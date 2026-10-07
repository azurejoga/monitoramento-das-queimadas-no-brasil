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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 471f6cb1-161f-33b5-90eb-31249da4e082 | -5.9835 | -40.9367 | 2026-10-07 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| e5f0415d-6878-35d7-a680-f9dceb6273c7 | -5.7376 | -45.1533 | 2026-10-07 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c0bd2d71-398f-32a0-8783-84182eec21b3 | -2.9447 | -54.1702 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c2b304ae-30d2-34a6-8f05-a454d246cc3f | -9.1517 | -65.9554 | 2026-10-07 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 28938c44-f3c8-30aa-aa8c-4dd81d48710c | -3.8566 | -55.9967 | 2026-10-07 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1d4d3a5d-5c34-3c89-911a-8b069c11b336 | -3.019 | -53.9272 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f410275d-d10c-3c76-9369-3c499f3333e2 | -3.0184 | -54.1282 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 23d28f17-bb9b-34c3-8ac7-2081d01bc869 | -5.7376 | -45.1533 | 2026-10-07 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0314548a-f059-3082-a8c6-12365d01cbab | -3.6762 | -60.6219 | 2026-10-07 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 26cc2009-88ab-3830-ba47-6c31c76943bc | -10.9949 | -45.4298 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e017b5ca-54c6-32e0-adc6-3722dc9f19c5 | -2.7613 | -54.0941 | 2026-10-07 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 253.3 |
| bca48303-310b-3e85-a87d-88a7c5e9c4f3 | -2.9448 | -54.1501 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4c035822-67c6-355d-9c31-91fc73361621 | -14.2537 | -41.6007 | 2026-10-07 01:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 7b5a4339-5696-3363-af77-17d08880a091 | -3.0001 | -54.1086 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 54b297d5-660d-3b95-9b65-a5c4ade59019 | -3.1115 | -53.7637 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 26b8730a-23ac-31e3-af48-751b9bfb5b5c | -3.1787 | -50.5807 | 2026-10-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ccbb230d-14f0-35e2-8662-ba44ef68d370 | -3.4963 | -59.5775 | 2026-10-07 01:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| bf5788f0-a29e-306c-bb92-57bd1d83bf66 | -11.014 | -45.4272 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 10b27f5b-95a7-3725-b4fe-80861f773598 | -8.2865 | -50.2731 | 2026-10-07 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| fbf9bc8c-862e-321f-ab53-25df8574d3fa | -3.4762 | -50.0883 | 2026-10-07 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 40a32696-fab6-3263-a7db-9f36f731965d | -14.2334 | -41.6296 | 2026-10-07 01:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 1a9d712c-2650-3c55-8f76-37100a78a4f4 | -3.8567 | -55.9769 | 2026-10-07 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9fb0d606-daa0-3cfc-991b-c0fad631634c | -5.9647 | -40.9383 | 2026-10-07 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| ca9de535-45b1-328d-a6b8-341494f9c271 | -2.7613 | -54.074 | 2026-10-07 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e32d8b3d-2f13-33dc-b654-5f31e4e17d1e | -2.9447 | -54.1702 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a08f070c-ca39-31b3-8ce8-f7052a076de1 | -3.0 | -54.1287 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d38f6f2a-964e-3f82-a2ac-cdf0e55b8dd8 | -11.1047 | -45.7119 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 0e67730a-f684-3c7f-b0d4-28f5be6ebb2d | -11.7335 | -43.649 | 2026-10-07 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 9a594b59-8872-3cf5-a1da-3c90ed5863bd | -3.5515 | -59.4807 | 2026-10-07 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e81bcc21-2567-3d5e-a7e0-a85076f39f46 | -8.7228 | -45.1812 | 2026-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 38d9ad5c-1fe5-3ba8-bc21-bad540913936 | -3.5061 | -51.6924 | 2026-10-07 01:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 724b42b8-dcce-3070-9731-43d8996f14d7 | -8.7036 | -45.2061 | 2026-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 311.6 |
| 5e9704d7-e24f-3685-bc48-95d9a6fa13a6 | -3.1114 | -53.7839 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ba28412e-cd9e-38ec-b5db-4ad3a7fc7081 | -5.7189 | -45.1547 | 2026-10-07 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6ce00439-8bc6-35be-b8e9-4f0cb237e46a | -1.801 | -57.1161 | 2026-10-07 01:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0e4e5515-7c95-3e47-8c49-235c434175eb | -2.7796 | -54.0937 | 2026-10-07 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 526a9391-0f3a-3095-960c-fcdbbd74da4c | -4.8397 | -42.911 | 2026-10-07 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ac617caa-3671-316a-9568-1b5d5d3aa3c8 | -3.055 | -54.1474 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 74f89886-73de-35b2-a5cc-588e73b40179 | -8.7225 | -45.204 | 2026-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 50b83c59-5d1d-3712-aac4-dca890c8d44b | -3.0558 | -53.9263 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 778d7622-0ed0-395e-983a-a9e2fb2200f5 | -3.1101 | -54.1661 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3f3869e7-0f28-35aa-991b-e30495b9ab90 | -3.4577 | -50.089 | 2026-10-07 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0c3c3dbe-571f-3077-8a5e-2ceacc4071a2 | -2.7612 | -54.1142 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| b7e4f495-ed68-3cca-961c-027e7daa947e | -3.1787 | -50.5597 | 2026-10-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| ca0c74d6-c962-3ad3-9769-710e91f8fba1 | -8.7033 | -45.2289 | 2026-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8270356d-0505-3627-9c4b-5bedb9b307c2 | -11.2333 | -44.8678 | 2026-10-07 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c3d1f5fd-977f-3404-8008-513a149691a9 | -3.658 | -60.6222 | 2026-10-07 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 5ffa0f6b-6763-3024-a145-ba4fc658ad56 | -11.0137 | -45.4501 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 51ad4b17-50b8-3334-a96c-b2d11ae408fa | -3.2728 | -50.1372 | 2026-10-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| fa529ebe-194f-3150-8a50-7840fa75c687 | -5.7187 | -45.1773 | 2026-10-07 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b81edca5-a8d6-36e3-bb9d-657ada711322 | -14.2727 | -41.6215 | 2026-10-07 01:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 98286b8b-b12e-3666-9c20-338fc375e9e7 | -3.6205 | -55.2907 | 2026-10-07 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ac7f3c89-72e2-311b-bc4b-e7f9c2f0efad | -11.1238 | -45.7093 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c5b3b54a-3ee7-3e4a-aa3d-e337520ecf40 | -2.7797 | -54.0736 | 2026-10-07 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f18879a4-7829-38fe-96d8-f65f9bd67120 | -3.0374 | -53.9268 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 7aee7e7c-34ae-3ec5-9f75-baa7fee601de | -3.6579 | -60.6412 | 2026-10-07 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b564e73f-5d68-3fc5-bfdd-25da65840915 | -2.9264 | -54.1505 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8abecf77-a8e0-3a97-8aea-831a2ed64661 | -3.2913 | -50.1366 | 2026-10-07 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5e4cd69d-2a2c-3c77-93a1-4c182d941b83 | -3.1972 | -50.5592 | 2026-10-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7d7442ae-4901-3bac-93da-d26f6f11cc59 | -8.7039 | -45.1832 | 2026-10-07 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| d1c78aa4-4e23-3f14-aadf-c3f55ad00382 | -11.1051 | -45.689 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6d4a2430-a345-3e72-b656-9478b1290db0 | -3.4963 | -59.5967 | 2026-10-07 01:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 07c14671-79b4-32a9-9fae-ed73ba8ef814 | -11.1043 | -45.7347 | 2026-10-07 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9a95f7ac-03d6-35e4-af09-f5018c7f6d18 | -2.7796 | -54.1138 | 2026-10-07 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 9aaebfc2-eb08-3f18-9e10-9ffbfbac5d3f | -3.0375 | -53.9066 | 2026-10-07 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 995ecaa5-e02a-372d-8cda-df2dbc997a1b | -14.2531 | -41.6256 | 2026-10-07 01:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 279.0 |
| dc5cf1fc-0413-3274-bc73-8cf948a3ebfc | -5.7187 | -45.1773 | 2026-10-07 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1a9d7c06-d46b-34db-8775-f01d8c2571ac | -14.2537 | -41.6007 | 2026-10-07 02:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 847fa0a5-70d1-3c30-879d-f6244fa8f12f | -1.801 | -57.1161 | 2026-10-07 02:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c98a8a38-4d09-3fc5-8e71-da8e9973c432 | -8.2865 | -50.2731 | 2026-10-07 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e0f86485-4b2c-3188-91e6-1b7318ab7f0f | -2.7613 | -54.074 | 2026-10-07 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d6def9ea-fdcd-3a4f-8360-0767f0a4b575 | -3.0184 | -54.1282 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5508901e-58dd-34e2-965d-00784cc4cd49 | -3.5127 | -54.6562 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| f9ffbc37-9f18-39f4-a004-e5b74333d56c | -11.7331 | -43.6727 | 2026-10-07 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e8a958c7-0172-315c-9fae-04e4af696c12 | -2.9448 | -54.1501 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 62a56883-2557-3c5a-af30-43c2ac251737 | -3.6205 | -55.2907 | 2026-10-07 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 77a3b845-69c4-39ec-9fe3-ce4b4e0f7450 | -3.0 | -54.1287 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 853913af-50c5-3fbf-8d67-6dfe2e1f9712 | -3.6579 | -60.6412 | 2026-10-07 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5bd050ea-394e-335a-b7fd-5cfc94d6c08a | -3.1115 | -53.7637 | 2026-10-07 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| dadbc813-aaa5-3019-ae3e-7ea2b64a2996 | -3.658 | -60.6222 | 2026-10-07 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 5f653dcc-18a9-3b73-9eef-e5b203916341 | -10.9949 | -45.4298 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fcd23fb1-4ebb-39f6-91df-0fc0d66c3695 | -11.7335 | -43.649 | 2026-10-07 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 93168a61-e48a-30ac-9964-4bdccf861152 | -11.0137 | -45.4501 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4d68e79d-663e-3d74-9a15-75dab5f7ac28 | -11.1047 | -45.7119 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 6356d377-eddd-36e2-aa60-118f3ddb1a10 | -3.0375 | -53.9066 | 2026-10-07 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5105c1bd-524d-3e75-ae15-5e2905c097eb | -11.1051 | -45.689 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2fbf618f-fbc6-398e-8fb3-2414d8888f6e | -3.0374 | -53.9268 | 2026-10-07 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4e75f377-da31-3d63-a8e3-e4c54601cd8d | -11.2333 | -44.8678 | 2026-10-07 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cc3d3a22-c1a9-3349-b5e4-9a95e3c53dac | -8.7039 | -45.1832 | 2026-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 25942c72-99f9-317c-9c52-adeb186effbe | -5.7189 | -45.1547 | 2026-10-07 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 64756d09-6a96-3106-bc24-5cebf056e2c8 | -8.7225 | -45.204 | 2026-10-07 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 318.4 |
| d4548932-eeea-3487-bc3e-d983b374e25a | -3.531 | -54.6557 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 115d1956-a7b2-3a12-9202-012bbefb4a36 | -9.4621 | -67.0817 | 2026-10-07 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| fad6a23a-5cc4-3f66-b9e2-9c6ae4ab1dab | -3.5126 | -54.6762 | 2026-10-07 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c71024cf-6b00-3f43-b64e-ab6a1dc18e63 | -3.6762 | -60.6219 | 2026-10-07 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 63ef1522-5f94-3473-8e92-8cd8a218979b | -11.1238 | -45.7093 | 2026-10-07 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 764a6b33-119b-378e-9e4c-7500ca0ea809 | -2.7612 | -54.1142 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 056dab3c-d9c7-3dbe-bcc2-30790938496c | -5.7376 | -45.1533 | 2026-10-07 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c14220ea-db87-3345-bb7a-dc146b4537e3 | -3.2728 | -50.1372 | 2026-10-07 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6120fcdb-781e-3b17-8c2a-ff81627aaf5d | -2.7796 | -54.1138 | 2026-10-07 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |


[Clique aqui para ver as próximas entradas](README27.md)
