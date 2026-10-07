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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c4d31a2-cbed-3853-bd97-1450effdfec6 | -3.0447 | -53.905102 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6540564-a007-33dd-9f4f-bdea95cd020c | -3.0939 | -53.718899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dcf3e0f-f94b-3017-921f-8cbd33fed6ec | -2.7813 | -54.1026 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fed6653-1f83-323a-a936-937ffb7d9335 | -3.0002 | -54.1124 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9822b9f1-f553-3a15-88f1-72f25f392948 | -3.5894 | -54.2953 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f5acef-fcf3-35e2-a58d-5777dec39124 | -3.2785 | -54.023602 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccd3a9d-2b71-37ce-a7ac-53d1b2456cd8 | -4.1627 | -55.164101 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d39f32-8af5-37e0-bc50-466af3bd56d0 | -3.529 | -54.656601 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3c25210-6d82-3b60-bac4-ce5adcd50c85 | -3.5024 | -54.630798 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7e97bd4-0743-3511-ba42-2a01d19d2356 | -2.7832 | -54.110699 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0374ad2e-41aa-3676-820a-dfe8c655e1c5 | -3.7355 | -54.657299 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aafd8cb8-7681-38af-9881-6d8d9c2680dd | -2.5287 | -58.1022 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13b02c3f-0642-3a3b-bef9-7ae272dab562 | -3.071 | -54.239399 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df652fa-b41c-381d-ab5d-bdf8fa5e3b42 | -3.0776 | -54.179199 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc6b314-f79f-30bb-8e9e-a290ef6ee877 | -3.4961 | -54.648201 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c35e013-e457-363e-8f4d-fff5e3155542 | -8.7245 | -45.194099 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55fe7998-0dfa-3350-9a9f-45591b56f026 | -3.0487 | -53.878201 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f04642dd-68da-33fb-833c-f41db3528f6e | -4.4495 | -54.9771 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832c97d3-5f71-339c-92e7-da8f100a43d1 | -3.4859 | -57.779598 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bae175c4-34e8-3f09-aefb-efbebd63f565 | -2.385 | -56.1311 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d07e63-0abb-3abc-882f-556832283999 | -3.0129 | -57.740299 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab1dbb75-2509-3b83-be50-a4378f3f327f | -4.0888 | -54.889999 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362603cb-4cde-3b7f-bc2a-8aa6f85218a0 | -8.7085 | -45.2509 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce946de-b311-349e-be17-666e683fd208 | -7.187 | -55.1241 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c05d8e-944c-3ef2-81e9-48c6ad54f197 | -1.8051 | -57.106602 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3aa54ab-d9b2-3e8b-b274-14937b5a82a9 | -3.5336 | -54.631699 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7842a8-5b76-3374-8f08-54a945596d70 | -3.0612 | -54.2416 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04690914-51dc-3598-915d-8f4a6b778c91 | -3.0495 | -54.235901 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0416dfe4-7c96-3a5e-a63f-515ecce50e8f | -4.079 | -54.8922 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4c1b43-7a1a-34a7-accf-16db76b26a69 | -3.7332 | -59.453701 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b45758c2-47b1-315a-89fa-f293aded0179 | -8.6988 | -45.1745 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 063c33a9-319d-3cd2-87f9-81ba06ddd6db | -3.5567 | -59.492599 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 397d1683-b3fc-3c54-8377-79a302479a47 | -2.1584 | -59.231899 | 2026-10-07 01:09:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76eec32b-14a9-3178-a4f2-3f7ac7641eb3 | -3.3964 | -59.511902 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e56f0dfd-7a91-3cec-b6b9-8b02b0e1ba79 | -2.8009 | -54.098202 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc212989-5046-39bd-a949-b1894006ac7d | -6.3261 | -55.327801 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e023abe4-cac3-3ff3-beed-398ae53804b9 | -3.0425 | -53.9403 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfc31653-855a-34fd-917d-0c56d28c4103 | -3.09 | -54.276798 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e476c58f-5c5a-3276-ad94-1c7fda277a74 | -5.9798 | -55.391998 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22eb13ad-7fd6-3d62-ad3b-59b00dcab067 | -8.6956 | -45.201801 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb1890f2-0a42-32d6-b854-755ed4006017 | -2.9904 | -54.114601 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122bfbc8-3a82-3741-8a51-5d91209c3e83 | -3.6203 | -55.2719 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc02acb-6cf2-3c9c-80d6-35154461ddaf | 1.5296 | -55.967999 | 2026-10-07 01:09:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184eb017-6509-339c-8ed0-4820cec20e59 | -11.122 | -45.737 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d0f923f-1d12-381b-897b-aed5848c5699 | -2.8988 | -54.075901 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d097362-f815-3ba3-86de-f9408bc32147 | -3.1808 | -50.547501 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b059736-dbe4-3a60-b348-45398e0a238d | -3.0808 | -54.237202 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069a9f8c-09df-3121-bd15-1bf421d001eb | -4.1382 | -54.925098 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac96faa6-528e-3042-a8fa-15a87701ffb2 | -2.5776 | -56.160999 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2bf4bb7-5b4c-33d9-82c2-dcd387f594ab | -14.2464 | -41.603199 | 2026-10-07 01:09:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9d365318-6428-3fea-a337-cfaca414bcc1 | -1.2796 | -54.561401 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cca58ec-6250-3f37-9d89-83093760b0a3 | -3.0585 | -54.141499 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 964fa119-2d91-353a-b68a-5415dd72e411 | -2.7807 | -51.681301 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7006ac1c-1c97-39f7-a33b-e6eb6b6610e6 | -3.8552 | -55.975399 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0a07657-9f7f-3257-8c7d-19cb3e8c4887 | -3.2664 | -54.060299 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b7857d-2e34-37ca-b532-cf5bba9ff244 | -3.2781 | -54.066101 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ebea4dc-5e13-3e1e-8227-fd59b7abb9a4 | 2.4361 | -50.8624 | 2026-10-07 01:09:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 769916bb-699e-3a4c-af25-95af9e0a6adb | -2.0338 | -55.637699 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05d096ca-36a5-3099-9be7-6e2cbdca58ed | -6.444 | -55.034901 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db1cca4f-2c3f-393d-86d3-1a2a23e16f8e | -3.0487 | -54.1437 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d948cfc1-1c14-3f85-b783-a8732157223e | -3.6515 | -55.317699 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4ba97e-305a-3ee8-8891-209621c5a101 | -5.2476 | -50.926201 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cafb76e-6a63-307c-be26-039ae5ed45c3 | -3.8157 | -51.054001 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a84971-626c-3c98-95e5-086fadb34e39 | -2.3046 | -57.080601 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1020c51e-3843-3676-ba38-ba21d2f2cd7d | -4.379 | -59.898201 | 2026-10-07 01:09:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa3cc28-2d56-350c-9bec-b014b6faff72 | -3.0175 | -54.142399 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2e4741-4bdc-330b-a9ec-48b92c8c59f0 | -2.1122 | -52.077099 | 2026-10-07 01:09:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ea918e-42b3-3aca-826a-513b4af5975b | -3.9266 | -56.061298 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba0684d-83e3-3285-a8f2-24f0ee2289c4 | -3.1135 | -53.758499 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 079aceda-4fba-3d8e-9e66-e9743120cc86 | -3.1905 | -50.5452 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df6b0b1f-d8c6-3175-832d-97d9cc0f67a7 | -3.0538 | -54.209801 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7026293b-da6f-38ac-89f1-218af1953a3b | -2.8397 | -54.132 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce0f94a3-1d39-3189-a7f0-8d5154578490 | -3.5122 | -54.628502 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9a02355-ef28-3be6-837b-84b1032d30da | -8.2981 | -50.277901 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5053c533-cd1d-3a6d-a393-05f20acc118e | -3.8027 | -51.997398 | 2026-10-07 01:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e908b0ef-becc-3af4-b638-20893ef7f34b | -7.1854 | -55.1171 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51abf633-1db9-3c78-845a-26ddb8ae3754 | -2.9493 | -54.115501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4d94d92-23cd-3d45-8c2d-548c783ba956 | -3.0368 | -53.9156 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6779f966-5e6e-3fb4-824e-81a401dc66c5 | -7.7478 | -49.213299 | 2026-10-07 01:09:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fa282667-63c1-3d66-8ece-7d1765c2b3d8 | -4.5769 | -54.948101 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2f648f-a113-307c-b16a-77c0dd2403c2 | -3.0882 | -54.268902 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df2c60e-e89d-3a7f-a15a-930d5f68a110 | -2.9447 | -54.1842 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df743dca-7531-3668-9701-b6c45059040e | -3.3854 | -58.197201 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eee14902-36c4-3bf3-8696-49c62b6e7777 | -3.0747 | -54.255299 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99dbfef-b3e8-33f7-88e4-e7ef8f8d4942 | 1.7124 | -55.619301 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1481a5a-5ecb-3682-b997-050c51b72469 | -7.2195 | -55.175499 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d1e78c-de04-36db-a6fb-2f92b855dfca | -3.0739 | -54.1632 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7ac132-04fa-3d6c-8587-888af78bbba7 | -3.107 | -54.172501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1b42cd-1da0-3bbe-b4f8-edf14c5a3cd6 | -5.3109 | -46.689999 | 2026-10-07 01:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f095eaca-ed3a-3510-9258-1a748cd3206a | -3.6517 | -60.639198 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49df184c-69e8-3b4b-927f-afba7718e30c | -3.0039 | -54.128502 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6f1907-637b-3443-9411-7ae8d7a4a295 | -2.8664 | -54.202099 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797d0479-df2c-3391-a5ac-89c6a2bfccfb | -3.2419 | -56.806099 | 2026-10-07 01:09:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 303d407b-a4e1-348d-8d56-3989b061f48f | -3.1033 | -54.156502 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5107c2-d2ee-3bc4-a6c1-a1c13f625ee6 | -3.1194 | -53.783501 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e798a360-2648-3991-9c02-49ebc5365233 | -3.6706 | -59.6315 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 623ac657-7ba1-30bd-b11b-65ca8e6b1566 | -3.3884 | -59.521702 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 266dadc2-c78d-3491-a875-2cd4f70c2b90 | -3.0543 | -59.909199 | 2026-10-07 01:09:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d708bd9-5788-32d2-8e5b-0e1873c337db | -3.5238 | -54.6339 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7abb21e2-f0df-3bbf-9e46-42fc570050ab | -1.7985 | -57.122398 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
