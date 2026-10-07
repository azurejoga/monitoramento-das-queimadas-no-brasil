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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 362fa452-afe6-35e7-8045-32b2064f7141 | -3.0374 | -53.9268 | 2026-10-07 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5c381747-5bb7-3cf5-ab4c-0c48702b033f | -3.0 | -54.1287 | 2026-10-07 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9ebd443c-ab09-3545-be1d-9f174d77197b | -5.7374 | -45.176 | 2026-10-07 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b87e1c15-bcb7-325e-a9a8-34c99adcdca0 | -2.9448 | -54.1501 | 2026-10-07 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c1eea0a1-1a9c-3e22-9e16-b44a59ffcbff | -3.0913 | -54.307 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 541e4ca2-1401-3185-a4c9-95eb59ef12b1 | -3.6206 | -55.2708 | 2026-10-07 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6c8fba25-cb3c-3aae-ac3b-528085ef9ed8 | -5.7187 | -45.1773 | 2026-10-07 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6cdce788-a1ab-3d9f-a5ba-ec80bae3bd1e | -8.7225 | -45.204 | 2026-10-07 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 549b9031-d4b2-3caf-baa3-b3bd6ca64543 | -3.6205 | -55.2907 | 2026-10-07 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| be072c21-8e7c-3908-af8a-0c799ac6f13f | -2.7612 | -54.1142 | 2026-10-07 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 341.7 |
| ed77fced-4bcf-3274-be32-9deeb8470647 | -15.2511 | -43.2743 | 2026-10-07 02:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 255ca23f-68a8-3f38-96da-e0242d46c768 | -3.5515 | -59.4807 | 2026-10-07 02:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 12cbe93f-e26c-3623-ab84-b6d483f4aea6 | -3.1114 | -53.7839 | 2026-10-07 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 68bd7925-e991-3520-b875-108df609dfcf | -3.0375 | -53.9066 | 2026-10-07 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1a1bfdd1-e330-3e80-a66a-8eef58e34f00 | -3.0914 | -54.2669 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 423dff42-ff9a-324c-b8ac-ee1bf5b5a734 | -10.9762 | -45.4094 | 2026-10-07 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| caaddc28-32c2-3bfb-b743-77c2cba59499 | -8.7228 | -45.1812 | 2026-10-07 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 47e1c4fc-66b0-32c7-b221-dde891a1fe75 | -3.0913 | -54.287 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| d0528e1b-1f1d-31cc-82a6-6d3d16b1f6e3 | -3.531 | -54.6557 | 2026-10-07 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 0ab123fc-bf68-3175-856b-732d8664676d | -3.4762 | -50.0883 | 2026-10-07 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2141164d-47f4-35df-9d3f-d781eabacc89 | -2.9448 | -54.1501 | 2026-10-07 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9dcafd75-970d-3871-81dd-4111c2250767 | -10.9949 | -45.4298 | 2026-10-07 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f241ab7d-39ce-3910-9b9b-c09ebdc903e5 | -5.7357 | -43.2682 | 2026-10-07 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 4a237237-f5b1-30ea-ac07-95e0b87a6d1a | -3.5127 | -54.6562 | 2026-10-07 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b06a5934-eeae-3d31-9730-9f228ecb51a6 | -3.0731 | -54.2473 | 2026-10-07 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| edf7c6ae-347a-3422-b37b-eb2687b5624e | -3.8567 | -55.9769 | 2026-10-07 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6e84e713-1f8a-3b46-93c9-26e75a6e5823 | -6.055 | -47.3155 | 2026-10-07 02:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0256988e-3bbe-3580-8f64-90c638bbd022 | -3.0913 | -54.287 | 2026-10-07 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 84e3d2fe-f239-3885-865e-e4ce54fedfb1 | -6.0552 | -47.2935 | 2026-10-07 02:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 1b2968db-015e-309c-8c66-d7d39bf34ffa | -3.8566 | -55.9967 | 2026-10-07 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e5b60ba0-a3c2-3535-ae0c-586475be7a67 | -11.7335 | -43.649 | 2026-10-07 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 47eb838b-9692-341e-b10c-341e72c793c1 | -2.7612 | -54.1142 | 2026-10-07 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 337.5 |
| f6d4e063-be9d-37e0-a7ca-5f31f4e1e802 | -3.5126 | -54.6762 | 2026-10-07 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 19c2ecf2-195a-33a6-8339-3cf5ba143a4b | -15.2511 | -43.2743 | 2026-10-07 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 75.0 |
| d57f1724-fc78-3b3d-8ae6-ca4b020231f9 | -3.0375 | -53.9066 | 2026-10-07 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7b2526ff-1f68-366f-877d-acd19909c0f0 | -3.1115 | -53.7637 | 2026-10-07 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 79695b2a-ab4b-3572-ad84-844990a2b1be | -2.7796 | -54.0937 | 2026-10-07 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 223.7 |
| c1ceb534-11d0-3e89-9502-f9a8c2d5ed2d | -2.7797 | -54.0736 | 2026-10-07 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 852866ab-3297-33c6-a274-ee722137ee2f | -6.0739 | -47.2922 | 2026-10-07 02:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 64a38556-8f28-383d-be63-12856a7d8b85 | -3.6205 | -55.2907 | 2026-10-07 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| be7de7c0-ba84-3414-aa92-aef31206ebd9 | -3.5494 | -54.6552 | 2026-10-07 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| accd15bd-d2bc-3306-bd64-d4e4e002c381 | -8.7033 | -45.2289 | 2026-10-07 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 73fa52d9-6b3c-3ddb-bcad-255c3e4284b2 | -3.0 | -54.1287 | 2026-10-07 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 79e003a5-4926-35d7-9c5c-47043614736a | -15.2314 | -43.2784 | 2026-10-07 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 65.2 |
| f9ad59d2-951b-3b7a-bdc7-e91c6158658c | -1.801 | -57.1161 | 2026-10-07 02:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 64ab6106-e17f-397f-964a-16f826d5fd65 | -8.7036 | -45.2061 | 2026-10-07 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 259.6 |
| b0790c19-dd25-34e6-9534-810457424514 | -3.0913 | -54.307 | 2026-10-07 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 79c278f7-b7ea-33fb-bfda-e93803492319 | -11.014 | -45.4272 | 2026-10-07 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fe64a732-5de9-3c32-9e37-037e63eedc53 | -5.7376 | -45.1533 | 2026-10-07 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 078cbb92-68bd-3435-8326-39770a9cca68 | -11.7966 | -46.57 | 2026-10-07 02:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b0acee7f-5a71-33e9-bf5d-da9c99207394 | -6.0554 | -47.2715 | 2026-10-07 02:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7bef9383-fa81-3994-944e-495e27c172a4 | -3.1114 | -53.7839 | 2026-10-07 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b5c8d163-c5e8-3a27-bad5-ce11f110d318 | -8.7039 | -45.1832 | 2026-10-07 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ecb9d8d5-749c-3af1-92f6-568813a43cf9 | -2.7796 | -54.1138 | 2026-10-07 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 235.1 |
| a7ce2bcf-25a6-3003-bed5-8d5c26daa3b0 | -2.7613 | -54.0941 | 2026-10-07 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 318.4 |
| fd9a5ed6-eaed-3de4-8cb3-abf8b800b98c | -3.1787 | -50.5597 | 2026-10-07 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 62c4f276-4c0b-3a1b-8b03-acf0266ecf78 | -10.9953 | -45.4068 | 2026-10-07 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2ca6a015-f630-3ed9-8477-703f5e394f1a | -3.658 | -60.6222 | 2026-10-07 02:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 8273c278-65e8-3af4-ad97-f8ca7074dcd7 | -9.4621 | -67.0817 | 2026-10-07 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 71e7f234-df18-371e-bd8d-4786f01ab01c | -3.6579 | -60.6412 | 2026-10-07 02:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 282a8d10-ef78-3ff1-b164-5975ee2d4159 | -8.7228 | -45.1812 | 2026-10-07 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a7625731-e3bc-37b9-8e13-015d0df9caca | -3.0374 | -53.9268 | 2026-10-07 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 18d2d5fe-2a7d-3e75-b674-4e31fd13bb2a | -3.5311 | -54.6357 | 2026-10-07 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d9bbb97b-03c9-322e-9be1-f93081c999f0 | -2.7613 | -54.074 | 2026-10-07 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c8a8e337-11d1-3e39-98fd-bf6b335f66be | -5.7189 | -45.1547 | 2026-10-07 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9b8e155b-9ad5-30a6-8d24-5e703e773591 | -3.0914 | -54.2669 | 2026-10-07 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e0d2be59-f273-38aa-a1af-5789713d475d | -8.2865 | -50.2731 | 2026-10-07 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| e9030210-5a91-3b7c-abd6-3e65f1a6c752 | -8.7225 | -45.204 | 2026-10-07 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| a6ebcf65-c7f8-30d0-bef3-8e5940e86d8b | -3.0184 | -54.1282 | 2026-10-07 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 03df599e-98eb-3bcb-810c-3bd7a6b668ad | -3.073 | -54.2674 | 2026-10-07 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5e9fe364-e280-3d5e-9061-8b36a48c3e7d | -2.7797 | -54.0736 | 2026-10-07 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f6f3b6e2-87ed-3e9c-adb4-4e159be827cf | -10.9949 | -45.4298 | 2026-10-07 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4055ab87-30ab-3deb-b848-eea5a6151683 | -5.7187 | -45.1773 | 2026-10-07 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 49e445a7-dd81-3f51-b7b2-f6b5ace131a4 | -3.6579 | -60.6412 | 2026-10-07 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 564bd9f5-d81c-300f-8e2e-ab29b3e59b72 | -2.9448 | -54.1501 | 2026-10-07 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 15bbd07c-d145-3897-84f0-b5ec65d042d8 | -3.6762 | -60.6219 | 2026-10-07 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0af23494-e0cb-3e68-b3a0-2f41ca725424 | -2.7612 | -54.1142 | 2026-10-07 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 287.8 |
| c953ac8a-b78f-3b28-8558-0fef4dddde85 | -3.5311 | -54.6357 | 2026-10-07 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 57f1720a-2e9f-3221-af5b-be51e39f3546 | -3.6206 | -55.2708 | 2026-10-07 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 80d3c55a-14b1-3a2b-b191-cd260b4c803a | -3.0374 | -53.9268 | 2026-10-07 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| de94a77c-a05f-3c50-b3d0-e70f0b9e9664 | -2.7796 | -54.1138 | 2026-10-07 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 251.6 |
| 8ff0e030-e51f-382a-bc5d-ba421dceef5c | -8.7228 | -45.1812 | 2026-10-07 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9eb28344-e88a-3034-8664-ce2513fbf9e9 | -8.7033 | -45.2289 | 2026-10-07 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| edff7e05-1505-35db-90dc-16ab25f56667 | -3.0375 | -53.9066 | 2026-10-07 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b7313543-aa07-37d9-9bfe-34327cd83a3b | -3.0731 | -54.2473 | 2026-10-07 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f9d637c9-582e-333b-a019-b8fef85063cf | -8.7036 | -45.2061 | 2026-10-07 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 7e280780-5f2b-30db-9879-8f7057a424fe | -11.014 | -45.4272 | 2026-10-07 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d1afe397-c43a-3dec-ae98-1330d58b16d2 | -3.1787 | -50.5597 | 2026-10-07 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8f2949e3-8f8c-3cc7-89c5-cb15155bc21c | -5.7189 | -45.1547 | 2026-10-07 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2475fb2a-b4ac-3e07-82ee-9b540e05ed88 | -8.7039 | -45.1832 | 2026-10-07 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 83f3e5f5-1b18-325a-8386-f171a07e6e71 | -5.7374 | -45.176 | 2026-10-07 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a50120c0-24ee-3f39-bdbd-49682548179c | -2.7613 | -54.074 | 2026-10-07 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 01532d63-fcdf-34cf-a383-9ee504edc4ed | -3.5494 | -54.6552 | 2026-10-07 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1056aa10-7470-3319-808a-8fa7b4bb4f5c | -8.2865 | -50.2731 | 2026-10-07 03:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| c3475cac-3db8-34d1-a8a9-f3a7197a8afa | -11.7335 | -43.649 | 2026-10-07 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fad6d8d3-f9fd-3a5e-a0db-a3b045600669 | -3.5126 | -54.6762 | 2026-10-07 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6625eed7-c2ad-3d77-beac-1493866844ee | -3.8566 | -55.9967 | 2026-10-07 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f54f203e-6ef3-3f6b-8f3c-f1ee7350c542 | -5.7376 | -45.1533 | 2026-10-07 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1a76e30b-1f8f-332b-8676-28db38db8df3 | -3.0914 | -54.2669 | 2026-10-07 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ecacd604-7ec2-372a-b619-77a4c00d85f7 | -3.073 | -54.2674 | 2026-10-07 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |


[Clique aqui para ver as próximas entradas](README30.md)
