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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c68d4b8-1569-3db9-b782-55c415fe651e | 1.7959 | -50.4886 | 2024-11-02 14:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8de572a6-a2e8-39ea-a41a-1ff5af517528 | -0.1196 | -51.3359 | 2024-11-02 14:45:07 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2ff1b367-e61e-37a2-8970-b2e07ad1e8ee | -0.6896 | -51.6847 | 2024-11-02 14:45:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 45acda30-aaf0-3cda-adf5-182c35411b44 | -1.2014 | -53.9184 | 2024-11-02 14:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8e8dc528-ae1e-3241-bd4b-0a9b1e2adcb9 | -1.1834 | -53.6771 | 2024-11-02 14:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8a984885-2fad-3b39-8a9d-d20fd196fc97 | -1.2756 | -53.3734 | 2024-11-02 14:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 91ae7438-7679-3c7b-9430-e7ada727402f | -1.2013 | -54.0188 | 2024-11-02 14:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b07c4215-855b-3043-9f5c-7674b12bd466 | -1.2014 | -53.8983 | 2024-11-02 14:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 91ba0c13-66bc-32cb-876d-bb476bb911dc | -1.406 | -52.1916 | 2024-11-02 14:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1b85eed7-128d-3a2d-868a-a540bb5620ad | -1.4244 | -52.1913 | 2024-11-02 14:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 24b030f3-baeb-3029-8c19-226e8350226e | -1.3846 | -54.1172 | 2024-11-02 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| bfd90c92-952e-33ef-9029-c695c1472714 | -1.3845 | -54.1373 | 2024-11-02 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e3f2ec5e-cc07-3b84-a5e7-564f88d11494 | -1.4029 | -54.117 | 2024-11-02 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f47a1023-cea2-3f19-ac42-8456020a4496 | -1.406 | -52.2121 | 2024-11-02 14:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| de4fca8d-0278-3849-a5dd-24ed6ae65fc1 | -1.5311 | -54.2759 | 2024-11-02 14:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5d3dbf78-7290-3add-b5f9-1087cbe66a6d | -1.5127 | -54.2761 | 2024-11-02 14:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e6842eaf-7353-3c68-a933-6ab1c4025e5b | -1.5352 | -51.9436 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4f1ece2a-b3e6-3bfa-a7b7-bc6fa1322ead | -1.535 | -52.0053 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 87d3f66f-36dd-3ea4-b006-fc4d64a6c2b9 | -1.5532 | -52.1076 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b4713f08-1fa1-348e-8d50-4059cc4ee6e6 | -1.5531 | -52.2101 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5d3383da-a795-3e3d-a99c-14c702f8c474 | -1.5351 | -51.9642 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| dd53dd68-4bf2-398d-9a72-ee44db5c4158 | -1.5127 | -54.2961 | 2024-11-02 14:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| f125c30b-113e-3e00-b0e8-3bb6745b2048 | -1.5651 | -55.8844 | 2024-11-02 14:45:15 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3e9af7f8-6ed6-3d2c-9b66-bb552d989d54 | -1.5533 | -52.0871 | 2024-11-02 14:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b46c2173-f096-3f89-a94d-b91cc678bee6 | -1.7837 | -47.8507 | 2024-11-02 14:45:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b4496a5e-cfef-381e-99e1-5a274bb3a78d | -2.1563 | -53.6838 | 2024-11-02 14:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2d9eda46-607a-3c7a-b7f3-302b9b8e8e3a | -2.0417 | -55.7005 | 2024-11-02 14:45:18 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1a7b65ab-9527-3033-9835-29a6dd61f732 | -2.193 | -53.6831 | 2024-11-02 14:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 211542dc-25d2-3dd6-9008-6e59bd9c698d | -2.3246 | -46.5041 | 2024-11-02 14:45:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| cf36345c-8797-3c7e-9b34-c648eeba40ea | -2.3431 | -46.5257 | 2024-11-02 14:45:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 8ecb7e07-f108-3d2f-a29b-bf40f7149f78 | -2.3444 | -46.127 | 2024-11-02 14:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9460c873-de71-3176-b940-ec6e46e9854c | -2.3946 | -53.8606 | 2024-11-02 14:45:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7099e69f-3f96-3f6c-8ebf-00d3c13978c9 | -2.4825 | -49.0807 | 2024-11-02 14:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9b72212c-49c2-3686-a523-56a780ce3f57 | -2.3709 | -49.3387 | 2024-11-02 14:45:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9c6e747e-2df0-3c24-adc0-8aff54f80d1a | -2.4251 | -49.6975 | 2024-11-02 14:45:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f7a18dc5-9127-32b3-9a73-5e663f5f8d21 | -2.4365 | -46.3241 | 2024-11-02 14:45:20 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 68345351-eda1-3ac9-bb4b-03bfa246e124 | -2.4742 | -46.1455 | 2024-11-02 14:45:20 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 64f722a7-7500-334e-be92-e214805d80f3 | -2.3918 | -48.5699 | 2024-11-02 14:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 83b60466-54f6-3046-ae2b-389045dfbbee | -2.4618 | -49.7811 | 2024-11-02 14:45:20 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 89749c19-c081-3959-a42f-3d7c7ceb8f5e | -2.3985 | -46.5683 | 2024-11-02 14:45:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 929ca8a5-6732-3236-b6b9-5a6769d57e1e | -2.4103 | -48.5694 | 2024-11-02 14:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1a19b46a-7a18-38af-8cc4-8c7d9bb54e2c | -2.3893 | -49.3382 | 2024-11-02 14:45:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 39fa5703-936a-322b-b531-982691de3484 | -2.3799 | -46.5909 | 2024-11-02 14:45:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c61ceeab-8c8c-3490-827d-9b5a3d1d25d3 | -2.6574 | -46.7591 | 2024-11-02 14:45:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| adaeee29-6baa-3ce8-81ee-107fd3e5e686 | -2.6322 | -48.5634 | 2024-11-02 14:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 96a0d2c3-55b7-3052-b3aa-cba1f480bf39 | -2.5881 | -57.0653 | 2024-11-02 14:45:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d206fb00-7acf-333a-a880-2914047e3007 | -2.7754 | -49.8362 | 2024-11-02 14:45:22 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b49dce11-ec7d-3a6a-9cbb-efb9097fad36 | -2.8361 | -48.4286 | 2024-11-02 14:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9d53fac8-f956-3a7d-8543-15c1587f202e | -2.9353 | -46.7942 | 2024-11-02 14:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| af50abfd-424d-34ce-94c4-b3f3e5b33c90 | -2.9802 | -54.5499 | 2024-11-02 14:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 454d2605-54a5-3a45-b4d3-af4a142ad57f | -3.0734 | -54.147 | 2024-11-02 14:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d365abba-c987-3d2a-bd0e-9d415acbadb6 | -3.1098 | -54.2665 | 2024-11-02 14:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 181d9dbe-e58f-3e7e-8cfc-e011016b3b1e | -3.6421 | -50.1667 | 2024-11-02 14:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 5987500c-6a81-3a6c-af59-46ae21ad8d0a | -3.8467 | -49.9061 | 2024-11-02 14:45:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 00b2632f-896c-3a07-bd27-04493239e2c6 | -3.8877 | -49.1194 | 2024-11-02 14:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| adc35ef7-04ed-35c7-9721-dc5512ff12ae | -3.9289 | -48.3458 | 2024-11-02 14:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| eb23b42c-809c-3f2e-a755-f62575c666fc | -3.9474 | -48.3451 | 2024-11-02 14:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f6de7e89-df4d-31a3-b673-62395235f76c | -4.5953 | -48.5308 | 2024-11-02 14:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 6409607d-37f9-3a13-a5ab-9e0224944053 | -4.8921 | -48.5588 | 2024-11-02 14:45:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |


