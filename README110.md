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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a608d4f6-2a2e-3994-9fd8-f3409e33d807 | -3.77937 | -47.49534 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05209c61-af11-3af3-81a4-a9140ea8b7fa | -3.45686 | -54.57042 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b934769c-8859-3a55-8235-831c5595cf5f | 0.97567 | -50.1253 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 26c73b49-6090-3ba5-a1ef-d69109ad9213 | -2.61416 | -54.20799 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c80986c1-5ba6-3b1f-a830-6c2761fc8f5c | -3.27569 | -50.19096 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2b1bba56-bd89-38e3-9b5c-6586a847fcb5 | -3.24275 | -53.92545 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 05013857-0524-3c15-80b4-07df1406475a | -1.14238 | -54.05735 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84443a43-c214-39c2-8f43-0d862bb38d4c | -2.78831 | -51.66903 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d84981a-68fd-3023-a443-b23bc678140f | -3.07975 | -53.75865 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4bd3c79-c435-379c-8408-9da0c99fe8ec | -1.48942 | -52.32374 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eeb5b2dd-9146-3288-a998-7e3ed4c34361 | -3.08467 | -53.28062 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00b8d11-59e8-35c5-baf5-d7c07779a690 | -2.75636 | -54.12365 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8be1c0b9-cf21-32ab-ad85-d5bd596f9c25 | -3.78372 | -46.69088 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 547a14d3-61ba-3a6f-b747-b35ec21bda43 | -2.45134 | -53.99722 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5df0e447-dada-3715-8e34-8295143504e8 | -3.1404 | -53.84464 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b004e46d-ca8e-3c7c-9bc5-816db0cb421f | -1.72364 | -52.49045 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4341fa9-86c7-3e38-bcc6-5582cafbc442 | -2.57533 | -49.99471 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ed22fb1-6bed-3727-b319-98f96be0ab28 | -1.99795 | -52.0932 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 011ceaf3-c804-32fd-b23a-c7d54cdd4a8c | -0.19361 | -51.36137 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b0325b6-c50a-36bd-9612-136bdce1a1d1 | -3.03005 | -54.03304 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e52c9d96-47f9-3442-859e-df9cc1bd9b9c | -0.26843 | -51.62318 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be92061c-3c20-3634-82c3-8ea9d732472e | -3.24745 | -50.59223 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 977198c7-a9ec-3f6a-87a2-5812033d861f | -3.22792 | -53.39184 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea29ecdc-3a5d-3648-a11e-7c84dbc2dc8c | -3.14149 | -53.8376 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22adb51e-10db-3a85-bb2c-232a58feaa13 | -3.76193 | -50.17844 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea106507-7dc7-3dea-b7ea-53992804a7d3 | -3.52503 | -50.4764 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60a2caac-f5d1-3f97-90ab-2beee310ee97 | -1.62542 | -53.88729 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8e8cad4-b04b-38cb-8a23-af34066cbe61 | -3.27421 | -54.70171 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 545b5a14-fe27-3c6e-bb51-e6e4d827deda | -1.06836 | -53.38449 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f50e9329-5cea-3a53-81d8-2a9a7acb19e5 | -2.8384 | -52.91462 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62db0c56-6735-3b60-8ce2-ddf20acc9c0d | -4.05666 | -49.05931 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38eacb57-9c6c-391c-bb8c-537ceea526a5 | -0.57768 | -51.69603 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fed6c512-d98d-3913-a121-3fd76b89609e | -1.11094 | -51.74535 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06fa796b-3867-3817-ad6d-1bedbd43ad43 | -3.85906 | -50.5383 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d96b2f6-f9bc-36ab-a4eb-d21cc2271b66 | -1.25498 | -54.54488 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d19f13a-49ed-3b08-86df-30b1ee99c976 | -0.72217 | -51.69768 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e997f2dc-ffb5-303a-a26d-d28cc6f47373 | -3.60161 | -49.98024 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce1265aa-caae-3d16-9ee5-ac51cc886199 | -3.04847 | -54.04668 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ea890d-27cc-306c-ae1f-2bf1a4d688af | -1.42073 | -54.47898 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e3a3e6-3281-3ec6-ae8a-bb72de1cd37f | -2.23215 | -53.62084 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d533af64-4094-3bff-b08e-61d787cb6e09 | -1.93512 | -53.4449 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82189499-a724-3f41-a519-8e4da1585536 | -1.48957 | -52.41339 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d69fb79-4179-3d7f-9947-057b5f5f77e3 | 0.93305 | -50.74694 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e862c5c-6016-3c47-ab3c-85278e6988d5 | -2.7965 | -54.0546 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b875a62a-2d35-33d2-8ff0-e4153029c747 | -2.01712 | -51.19178 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bda730dc-3563-3c6b-817c-ace7221b1097 | 0.99123 | -50.27113 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c766cec0-3c2c-3e2c-b9e1-87f7440adc6e | -1.66471 | -53.81105 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d86d829-9b20-3c05-9941-83d5ad5a59fb | -1.59121 | -52.24874 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4cd2c11-b7ba-36b5-aa4d-5ca08230bb13 | -1.701 | -52.6372 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e5a731b-559d-38f1-8338-bc6768115961 | -1.37467 | -52.43148 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a76abf95-07e2-3474-b1d7-4325e01e6ecc | -3.34325 | -50.74714 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4d66f7e-cb3d-3dfa-bcf6-66bb46033955 | -1.10195 | -53.38965 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a917dd-872e-3610-ab61-83b9994045fa | -1.31032 | -52.86232 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91110036-c85e-3ee9-bcbb-1048729dc614 | -3.02445 | -54.02499 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69dd8c48-1bbc-3ace-b018-fb882b18ba85 | -3.80948 | -46.53865 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98b7b34e-4699-37f2-8569-b1fe37a9d57d | -0.90406 | -47.70274 | 2024-11-30 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2e6fd61-e301-3e3f-9a80-cd1cd09d4195 | -1.28404 | -51.72551 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fda61918-3399-315c-a326-da16e1c1ef72 | -2.77127 | -52.86981 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30930065-e899-368e-abfb-835e465af418 | -1.62774 | -52.37998 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11626bea-c187-3892-a1f0-8f41c37b39a3 | -1.15609 | -53.73229 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2950e7e-8e0e-3b9f-bd4d-5867ddee5915 | -3.31012 | -53.71409 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dee77730-a2be-3271-9730-9f0862ae6a0c | -3.65186 | -50.21824 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fbbc947-a3b3-3774-ad4f-cff49e394214 | -1.66938 | -55.79791 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c5c0d97-c6c1-396b-9dac-d1fd0565f3f0 | -3.06907 | -54.56367 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdbaadb5-21db-3a59-ada1-0cb840de8a31 | -3.33789 | -53.28873 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c89aa68-d529-31fd-bc6a-cd8baca56461 | -3.51265 | -53.78134 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c32825e-3d03-3105-ad8c-17aaa4d4c54e | -2.61884 | -54.06953 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ee239e-8b5e-3a9d-b789-8fd28930d718 | -1.19314 | -52.00382 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a6ab517-04c3-3cbd-bf10-f296c0e83614 | -1.66459 | -55.23124 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5a98631-acff-3a9f-bd98-b0dc60aae814 | -2.45946 | -55.27712 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b573ac0-cec6-31b5-b3e3-e52270a14cc4 | -2.71745 | -53.17211 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26c5ebaa-3e59-3233-bc8a-8a49c9afb3c0 | -2.19461 | -50.57638 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de81c766-79ed-3738-a4fc-1d3586e67c76 | -1.62106 | -52.45607 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c29654ed-60f3-3298-8f12-a1915e1f7259 | -2.46804 | -53.97115 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49631cb2-0331-358f-8f7a-70a1a9a54dbd | -1.38637 | -55.02071 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48c2d976-000f-3565-b531-989a159cb151 | -1.69679 | -52.47165 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb276e5d-c7a0-3f6e-97fc-e48e6e4492e4 | -3.1134 | -53.27326 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8ffa3f0-5cd4-3fee-9774-1f19a733009e | -2.82427 | -54.03021 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f002f7c-3ee7-3ce4-bf64-751e1e6e8df2 | -2.53726 | -54.05346 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c14c64ca-aa7c-359b-9862-9a3a79e401bd | -2.83246 | -48.47547 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6557bce3-fc80-341e-abe7-a653458bdcd4 | -1.14321 | -53.70544 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25074ce-8562-3f93-ae02-37965ef54a4f | -1.36913 | -52.86724 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 560f76a0-2425-32bd-8d09-04c0c17a01c8 | -1.39852 | -55.00847 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce36e899-b777-34b2-a406-0cdf9ac1dbdb | -2.87214 | -54.00892 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c413e8b2-d84f-3f17-8752-adba5cb08311 | -1.06638 | -53.22063 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 315cfe1d-1c3d-3309-948c-a8080e864b08 | -0.26887 | -51.64359 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a782ed8-8cbc-3058-8780-e2176f164e4b | -1.44551 | -55.20375 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b787e23f-be36-3f69-8a7a-e3415f36ee27 | -1.6905 | -46.78511 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 5e9c7bba-6c2d-3eb2-9f0b-f425af4164be | -5.22468 | -44.91 | 2024-11-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cdd4cb5-e063-3baf-8eab-28db5760f331 | -2.79947 | -54.12307 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e448aaa0-0fe4-3580-b0c9-7d776ce2d0d2 | -2.77239 | -54.06535 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a283af6a-6fed-3c8d-800e-3a2997ead297 | -1.19455 | -51.76101 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1540be6f-537e-3b94-a015-935c80662ce3 | -2.84552 | -54.06937 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0acf67d7-73c4-35fa-ab25-0358686d806d | -2.13615 | -54.88033 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9efccc9a-952f-3391-9046-9b5dfbfdd1a8 | -2.6075 | -54.20695 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1369622b-fc54-37f6-900a-7b99499439b0 | -2.2442 | -48.25409 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d293ee19-f0a1-3e1b-86b0-b7238bb6d4ec | -3.24669 | -53.60569 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c202ab39-fefa-3f4f-bc91-2789ae6fcfe4 | -1.25113 | -53.32531 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33525db2-1b40-3a4b-9201-c148d2f308fd | -0.2409 | -53.7608 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b036b39a-c86b-3614-a6f0-05ede07bc1d7 | -4.11477 | -54.41292 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README111.md)
