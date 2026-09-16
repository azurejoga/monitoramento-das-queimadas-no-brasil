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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 534772d9-268a-31b4-9b2a-b2cbe3ac9ebe | -12.7518 | -51.2426 | 2026-09-16 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 523976f1-6b0b-3036-807c-419f11f11b08 | -18.2265 | -41.2303 | 2026-09-16 00:40:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.6 |
| b542da9e-d6b5-3ad2-bf42-571d6752bd64 | -9.4102 | -62.7113 | 2026-09-16 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 70260532-31a0-3ba6-bb61-65cb57798439 | -3.3806 | -50.8458 | 2026-09-16 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 87341833-1cd3-3923-a4b9-33054179c0bb | -2.1051 | -52.0575 | 2026-09-16 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3b508ae3-b3cc-3b74-841f-01250d668f7f | -12.5337 | -47.1189 | 2026-09-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ee736daf-6c35-3bee-993c-208274ef7907 | -9.0931 | -45.7314 | 2026-09-16 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c737db96-59a0-3016-a3ab-34daa529b523 | -9.1123 | -45.7067 | 2026-09-16 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| eed74044-5805-3d83-8483-0e734d599db0 | -9.7136 | -64.9074 | 2026-09-16 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 09538d50-104f-3688-8559-99fdddbb4727 | -7.651 | -67.1824 | 2026-09-16 00:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 68591300-d8f6-3d6b-baba-7b56e449d255 | -9.3893 | -60.3022 | 2026-09-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 8395e40c-213b-36cf-b160-cfbc57f5db18 | -12.7521 | -51.2213 | 2026-09-16 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ea0f087e-8636-3cd0-937e-4ce8b0a1e6f2 | -3.1174 | -57.6779 | 2026-09-16 00:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0b210614-e3de-3958-a4d6-511cb24d87dc | -5.1215 | -47.6146 | 2026-09-16 00:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 987d4aaf-4152-353f-b5be-c2bed8fd4f13 | -9.112 | -45.7294 | 2026-09-16 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| b6e071d9-f23a-34fc-99f3-5100da706e96 | -5.1401 | -47.6135 | 2026-09-16 00:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| be7afa30-57a8-3d18-a7fc-70c3ac3ec3c1 | -16.2569 | -49.9419 | 2026-09-16 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6d90a0be-b285-31cd-b6ba-06a6dbe0b01f | -12.6054 | -50.8334 | 2026-09-16 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f81fee00-368e-328d-950a-273dc61c95ba | -3.1634 | -61.1048 | 2026-09-16 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 05235033-c0bd-3889-b0ce-5cc95a9c5736 | -12.6057 | -50.812 | 2026-09-16 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| fea6e0b0-be1b-34ec-a1d1-51dcaf510ae1 | -11.9906 | -52.4695 | 2026-09-16 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e15a99c0-64cc-33b4-9569-88e8a5dfdd48 | -18.2257 | -41.2559 | 2026-09-16 00:50:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| e9417b47-544e-3dcf-adec-b2bc5900e87a | -5.1029 | -47.6157 | 2026-09-16 00:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 84ab6e1c-8262-35a4-9995-476c53ebe571 | -8.8396 | -44.917 | 2026-09-16 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 0f8ea1ac-ba87-323f-a8e7-dd5100bcec7f | -8.5431 | -44.4902 | 2026-09-16 00:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e56b6e04-875f-3e85-abb0-4774d2ccda53 | -9.7136 | -64.9074 | 2026-09-16 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 34b8b58d-d41f-35b2-af22-1d559504022c | -2.1051 | -52.0575 | 2026-09-16 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1f26aa56-4a33-3ece-87e7-cfa9c1fd3b58 | -18.2265 | -41.2303 | 2026-09-16 00:50:00 | GOES-19 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 1fee3319-435b-3302-9b18-eaad7131e1a2 | -5.1215 | -47.6146 | 2026-09-16 00:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 62dd02b2-5838-396d-a251-79ad78086b24 | -9.4102 | -62.7113 | 2026-09-16 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 39c73ca8-1db5-3477-b083-db56cdccd298 | -3.3806 | -50.8458 | 2026-09-16 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 80381654-40bd-3ce3-a7c4-367c1f9a32ea | -8.8399 | -44.894 | 2026-09-16 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 430.1 |
| b09b67db-4223-37ad-b770-69f83ffe05eb | -9.112 | -45.7294 | 2026-09-16 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 6ba0f21e-91eb-377a-b9d5-ead6e7d33fa0 | -5.144 | -55.9345 | 2026-09-16 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b7d2269f-7206-3cab-bc0a-41357f4f9b3d | -9.3892 | -60.3215 | 2026-09-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cbde2de4-96ee-34af-83d0-d6389f49cd17 | -3.1816 | -61.1045 | 2026-09-16 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dfa9bce6-9f4c-3d6d-8345-20f04fc37b9f | -9.3893 | -60.3022 | 2026-09-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 2ff523aa-0614-3239-830f-c2b9d935610a | -7.651 | -67.1824 | 2026-09-16 00:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d4dcf4d7-fc0a-3d6e-9a8a-fc10c0eb4bba | -4.2951 | -49.1234 | 2026-09-16 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f3802370-951c-3cb5-8646-3a31c622187c | -12.5337 | -47.1189 | 2026-09-16 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 316deab5-4f2f-3f00-a15f-c0ab9a69d003 | -9.5152 | -40.331 | 2026-09-16 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 20936f2d-f586-3c3f-b6cb-13cd519c0eff | -11.4849 | -45.7965 | 2026-09-16 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 6899d0a3-6d82-3b76-b74e-f35b9c8ddf09 | -15.2821 | -42.8075 | 2026-09-16 00:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 69b29855-3601-3f50-b9ac-1b794e91ab38 | -10.7015 | -54.1663 | 2026-09-16 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3b456490-9aaa-354d-8fd6-85c7e57f4692 | -5.1401 | -47.6135 | 2026-09-16 00:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3b36ad29-81de-3665-99fa-e01deba8fcfa | -7.6511 | -67.164 | 2026-09-16 00:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 77e4176e-c8ba-3f79-9edc-0ee96f35ee57 | -3.1816 | -61.1235 | 2026-09-16 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 45bcdadf-414f-3d16-b49f-273dbcdefa04 | -8.8778 | -44.8898 | 2026-09-16 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 693dc95b-0c56-395e-af88-17154bfb570a | -9.7322 | -64.9067 | 2026-09-16 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b597efdb-a4cd-3c59-b933-b3d4690f7593 | -9.0931 | -45.7314 | 2026-09-16 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 66405c82-45bc-3739-916f-b1b2fba4f450 | -8.8588 | -44.8919 | 2026-09-16 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 363.7 |
| bd9561a4-f0ee-3164-8fa0-13a393c57bb9 | -5.1217 | -47.5928 | 2026-09-16 00:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0b3def95-6f3a-357b-b6ab-ef7555995a7e | -8.8585 | -44.9149 | 2026-09-16 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 703e6d12-b3b7-3aee-b0c2-f13b0e9d75f9 | -3.1816 | -61.1045 | 2026-09-16 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a38b9361-3c09-3ee4-91f7-6d15eddc0eca | -3.1174 | -57.6779 | 2026-09-16 01:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9e72c3a5-253f-3d9a-8d51-6975a079b921 | -8.8396 | -44.917 | 2026-09-16 01:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 168.8 |
| d0bcaeda-bbfa-3183-9003-e649a22a9ef2 | -8.8588 | -44.8919 | 2026-09-16 01:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 498.4 |
| 3c53f8b1-9b5e-3192-a813-7a343296f621 | -9.8012 | -46.4854 | 2026-09-16 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 3e9fdac1-8e04-328f-8ef7-46afc5994afd | -18.6453 | -50.1845 | 2026-09-16 01:00:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| 6f29f4bf-452f-3b1a-8117-86f4c9ad9784 | -9.4102 | -62.7113 | 2026-09-16 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 05035bf7-fead-3a40-96e0-b7aa79d8ba6e | -9.112 | -45.7294 | 2026-09-16 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 3a5bb020-1bfa-3b4d-9a20-c03ea7887a7c | -8.8399 | -44.894 | 2026-09-16 01:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 296.0 |
| 854cd76f-ef31-3ad3-8a28-a1152f0343e4 | -5.1215 | -47.6146 | 2026-09-16 01:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 169d5a86-4e2d-3a55-9cbb-9357975f3ac1 | -7.6511 | -67.164 | 2026-09-16 01:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 815ae152-67b6-31ec-a85c-22cfda48c204 | -7.6327 | -67.1644 | 2026-09-16 01:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c1ac9144-a070-34c9-a3ea-045e91cc898c | -5.144 | -55.9345 | 2026-09-16 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d76b4b04-2056-3934-86fe-666784c60ae8 | -2.1051 | -52.0575 | 2026-09-16 01:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| aec49b0b-a1d9-3d87-bd53-7e2a38906cc0 | -15.2821 | -42.8075 | 2026-09-16 01:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 838a82dd-2345-322a-9a68-3636aa2751e2 | -5.1029 | -47.6157 | 2026-09-16 01:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a37370c4-a24e-3ea9-88f9-d8bb1e1d4965 | -15.3018 | -42.8033 | 2026-09-16 01:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 7933dcc5-e8be-32a6-b880-e40342017aaa | -9.7822 | -46.4876 | 2026-09-16 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6423618a-b355-38c1-b6d8-2f86d005ca3e | -4.2951 | -49.1234 | 2026-09-16 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3a65b2de-7d5c-37bb-b713-6ce1d8c582e5 | -11.9715 | -52.4715 | 2026-09-16 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0baf6328-c111-3883-ba10-b0cf66dc189b | -11.4849 | -45.7965 | 2026-09-16 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 908fe6db-4b26-3481-b602-92d3b1438c2c | -9.7322 | -64.9067 | 2026-09-16 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 24f34a15-023f-39ca-acf1-1bb78ca49f01 | -5.1217 | -47.5928 | 2026-09-16 01:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 97f72ea1-aebb-39ed-a4d6-6318038fa2e7 | -9.7136 | -64.9074 | 2026-09-16 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e137f97b-4eb6-370f-abb9-9e170e2cb424 | -9.0931 | -45.7314 | 2026-09-16 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 319ae15b-27f4-32a0-9e81-176ada4bdcec | -11.1401 | -40.4748 | 2026-09-16 01:00:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 3faa1804-fc37-3284-8c89-333e09f9b56a | -5.7756 | -45.0826 | 2026-09-16 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4674e15b-5fae-3e4b-acce-26104cbe96d8 | -9.3892 | -60.3215 | 2026-09-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f56ccaf1-e28c-3c61-839b-caf784bfcd05 | -9.3893 | -60.3022 | 2026-09-16 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 14122487-32ff-3e73-95bf-39a5fd0727f3 | -8.8585 | -44.9149 | 2026-09-16 01:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 4f88bb66-3562-317d-95cc-58b70a62d197 | -8.8585 | -44.9149 | 2026-09-16 01:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 307.3 |
| 2dba3ef3-1bfa-3faf-a95b-20420b40d983 | -5.1029 | -47.6157 | 2026-09-16 01:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2f4c5a1e-1b63-31a4-b63b-6fdfd330737d | -7.6511 | -67.164 | 2026-09-16 01:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d81c9eab-ab82-386f-a5c4-e438dc8bcba8 | -2.1051 | -52.0575 | 2026-09-16 01:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 809c3464-57f6-32af-bdb1-7ef24c7b2928 | -11.9033 | -43.8112 | 2026-09-16 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fcc28b4a-1152-3848-9ed1-41b4b6860f66 | -5.144 | -55.9345 | 2026-09-16 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| cc52927f-1979-3bde-a508-48b5bc0396a7 | -11.4849 | -45.7965 | 2026-09-16 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f5d348bd-f4e5-3669-984c-dac8a560036d | -5.1401 | -47.6135 | 2026-09-16 01:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 71333e67-0e4c-3577-9391-92c55e374051 | -15.3018 | -42.8033 | 2026-09-16 01:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 39918b45-e9a1-3c74-9d0a-02ac716d5ace | -9.7822 | -46.4876 | 2026-09-16 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f2ebe66e-2a67-3555-89ef-7daba339d776 | -8.8588 | -44.8919 | 2026-09-16 01:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 301.2 |
| b348ad83-c416-3fd9-ad65-060ebb73fab8 | -9.8012 | -46.4854 | 2026-09-16 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| c1f5b171-3827-3531-a4fc-d884a3151daf | -8.8396 | -44.917 | 2026-09-16 01:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b7796537-2cbc-352b-a0b2-9847ba7dcc73 | -11.1401 | -40.4748 | 2026-09-16 01:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 62.5 |
| c79f9684-4635-3f29-8386-db88481990ad | -9.7322 | -64.9067 | 2026-09-16 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 094c9f9d-774b-351c-aabf-6cf39bc9f533 | -9.3893 | -60.3022 | 2026-09-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a540b31d-2f88-39af-8192-1943d2744352 | -9.7136 | -64.9074 | 2026-09-16 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README8.md)
