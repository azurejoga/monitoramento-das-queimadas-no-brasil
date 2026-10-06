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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00fa35ba-8fd9-3c6f-baf8-b5094ce29a60 | -2.8763 | -54.14256 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1473cbe0-c3de-33a1-af04-a2ddd08dd6d5 | -4.14184 | -54.0287 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80574c4a-0597-39a1-9e54-88c57604cf49 | -2.88125 | -54.14071 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c407dac1-e9a5-3032-bca3-9f68f1f96c00 | -3.05012 | -54.22927 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7b453f4-a00b-37ce-a422-94715bcc1aa9 | -3.32849 | -53.3892 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a603f04-92c6-308f-a3f2-9966cfc0815b | -5.02949 | -43.56704 | 2026-10-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b35db152-d845-3e34-b2d7-4573a888c84b | -3.45789 | -50.10488 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 191e166c-b155-31ff-871e-f1b79b509b75 | -3.06083 | -54.22143 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d684ac03-4f41-3232-bb85-6df95fdfa143 | -3.10803 | -53.7631 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89cf1d1b-3f0e-3502-b5ec-35521865ce3e | -2.26551 | -47.43633 | 2026-10-06 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67ca20c7-37f6-359d-a68f-7aa5b4bc76f8 | -3.12177 | -53.70716 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 291314dd-8b71-391a-a67a-7bd1f92586cc | 1.79267 | -55.5733 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21f6af9d-3117-3423-b22b-d1c42c01b08b | -2.77959 | -57.67936 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 647050ea-cad3-344c-bd79-fafe1b596f46 | -2.99318 | -54.11622 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb9ee74c-c04a-3f0e-8ca9-0f52867ec804 | -3.9416 | -48.43415 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb66b07b-027a-3081-a296-d77aa60a0baf | -2.94147 | -54.14594 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7926a7ae-c322-3f12-93c4-b6a2395c230b | -5.06555 | -46.10801 | 2026-10-06 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3901ae36-667c-3d56-b058-142c00637bd3 | -3.67088 | -54.5436 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42bd35b2-30e8-34f7-b939-75f90727c5c0 | -3.12548 | -53.71225 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e1a919e-8916-3bff-ab7c-947af0a55f30 | -2.70395 | -49.04014 | 2026-10-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8291fd5a-6bcf-34d4-9581-57cba28a06df | 1.72433 | -55.64577 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1518ca-5f48-37cb-b277-9a677152c668 | -2.99147 | -54.04002 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0b51f4b-6669-3986-a968-fa681f3b8547 | -3.59835 | -44.35609 | 2026-10-06 04:38:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8886d8b9-4d3c-3a04-a050-3ddc5d03a2fa | -4.54461 | -48.51149 | 2026-10-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ebdbec3-4666-3285-b587-721b13cfd1a0 | -2.90347 | -54.12032 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9974ada0-9f99-3eb5-8d23-f0122cbe4852 | -4.05709 | -54.05215 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa3556c-e3d7-347c-bc12-f405a81164e9 | -2.95135 | -54.14289 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4b8a8f2-7b11-304f-905f-d0f74366fb95 | -3.09791 | -54.16738 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df631606-07bd-3941-9f69-7c4b882c79f7 | -3.07459 | -54.25289 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 46976509-52f4-3bca-968a-786c14db305b | -4.33317 | -50.4061 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec09c47a-fed6-380e-971c-94792d9f5b72 | -2.12899 | -56.70304 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4715ad1d-b679-3480-a818-ef5f52148a5a | -5.96331 | -41.35543 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5e6381a-2f8f-3402-9bd2-a06593f4b9f3 | -1.61635 | -55.11483 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4ad5976-b4ee-3fce-b635-7f92c5bbc2ab | -3.09179 | -54.17581 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| defd6144-d438-34e7-9b7b-f99b62080be1 | -2.77735 | -54.08778 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2b59ec0-d115-3b8b-8d99-5234ffc6bb23 | -4.11249 | -49.39864 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fef9c0e3-de4d-3d19-a9d8-ec90602d8e5a | -2.90133 | -54.07713 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f02666f-706c-3b60-9b2c-e96fe5a5c6bc | -4.50394 | -42.07298 | 2026-10-06 04:38:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32ca5e6b-2d66-3b6c-8a7c-93388bd8e58b | -5.4666 | -41.24118 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6a428e3-059f-36f9-848c-e863cf25a65b | -3.09977 | -53.73033 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e0752f8-cced-38d9-a5a0-14e253a6434d | -0.94202 | -47.55373 | 2026-10-06 04:38:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1661ce73-71c6-38ae-a5bc-455742bc47c4 | -3.08721 | -54.17509 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7df4315-7790-35ed-a7cd-99cb398690ce | -2.9948 | -54.10978 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52e7359a-e4bf-39ad-9c63-9f229c7e2960 | -3.28056 | -50.40261 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 934ec5a2-3a71-3f9f-b716-ee4df4062ab4 | -2.78794 | -54.10712 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7dca9ca-5a4e-3fd7-a1e1-6846074824e5 | -3.50294 | -51.67505 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9934daff-e34f-3947-949c-635372728f70 | -2.89836 | -54.12212 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 050d2891-bc3f-3e27-94e8-ea3a8be7c378 | -3.37952 | -58.20607 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 09cae9cd-6a44-3eff-be73-edbd85b90ecc | -5.96713 | -41.36049 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ead390f4-f55c-3864-ad03-da4017e2cada | -3.27631 | -50.40614 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 450b3cf8-c4aa-3b75-b493-a7c248891dc5 | -2.79019 | -54.09307 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f755a0d-6006-3d15-94bc-4ae96a5f930d | -3.47043 | -50.09466 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0245f503-534f-3995-8523-53b6a5c06c03 | -3.67888 | -55.95346 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a31f582b-c634-3013-bd1f-63096a658a30 | -3.66702 | -54.53807 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b17b9260-32cb-3e2a-81bc-ab5fe6f2fc4b | -3.28205 | -42.2632 | 2026-10-06 04:38:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a3a052a-3391-3773-8954-4659c5df6cb1 | -3.38103 | -58.19747 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d1bb7d1-8e6b-3bac-8e2d-742fdb30f5f5 | -3.0723 | -54.23784 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 852137a4-b25a-306c-a4b9-cfc3ee4eb0d7 | -5.64582 | -44.11971 | 2026-10-06 04:38:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58b072c6-e8fa-30ff-9bf8-f29ed54cfe2f | -3.51878 | -54.63605 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9facb9a-12f0-3df5-b517-e88fd0806356 | -2.22328 | -53.71195 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fadff86-ddf7-3757-8218-50a6aedbb644 | -3.07153 | -54.24265 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5addf76-2869-37b9-8b0a-dfb6f16b90e5 | -3.68804 | -55.96148 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58f6c95d-8e82-3907-b667-58f45d9665e3 | -1.05281 | -53.5941 | 2026-10-06 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16899c41-8cf4-3700-8a03-b942af88ca64 | -3.4946 | -49.90107 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc7be314-c932-31ec-bce5-47c900732a86 | -3.00389 | -54.13711 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a8a80389-03e0-39c4-ae4c-f29c324dbbe1 | -1.61043 | -55.11977 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22cbaa1-7892-36f3-a3b8-e24268aa791a | -4.7741 | -50.81071 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 519b7eee-a429-3514-8bc7-d3e5a85bc398 | -4.11464 | -49.07778 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8da29b7c-ecea-341e-87c4-1ffb5a517411 | 2.46012 | -50.8384 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 20336083-0d2e-32a0-8c14-2ea90b1c4f86 | -5.22844 | -48.39889 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dce7c85-bab9-371d-95fe-a091f37a3168 | -3.58576 | -54.31585 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96b90a1e-d84d-38d3-b990-f4e82b9c2aec | -3.09316 | -53.74274 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f613bb3d-aa47-3ee3-97fd-d17abfddac4d | -3.67482 | -55.94651 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 82508ba5-314d-3186-81ff-7245dc57c497 | -2.77955 | -54.10259 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 38d8cfed-530c-3b95-b802-f0c4026374d6 | -3.05242 | -54.21518 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dca76cc6-ed1c-3cba-b919-de83c1596717 | -2.9407 | -54.1506 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c91a521-7c10-3660-9918-e5a176e32fe2 | -3.67295 | -55.94245 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96ab1951-2e8c-3a6f-a781-21fbbcad96e0 | -0.69263 | -49.32271 | 2026-10-06 04:38:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c0ae8162-fbc3-3d7e-9f7a-73a42da9676c | -5.22568 | -48.39489 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc004d05-b343-3e33-ab2e-8927afdfe207 | -3.58843 | -53.47565 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c492d4-c56f-3d1d-8a63-94bc9078dc15 | -3.04861 | -54.20974 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db060bee-0f72-3625-84b5-e3fbfaff899c | -3.06151 | -54.24626 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2446ea6-f41e-3d47-9f24-15062376b8bc | -3.07152 | -54.18462 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72be4caf-576f-307a-8719-5068b2b7367e | -2.78405 | -51.66663 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1291d9a6-483c-3389-be68-9d6d7bdd273c | -3.3225 | -53.85828 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21c31a39-6062-3123-ad3b-189dbc756d7d | -3.84299 | -47.81672 | 2026-10-06 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab7b995-51fc-3cd4-bce6-54a47e42549a | -3.96417 | -48.1229 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d969c1f-9515-3a68-a1d5-32eb575d04aa | -3.07223 | -54.15137 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04c01a4d-800f-3c94-ba1e-7b308342acf7 | -3.93683 | -42.99543 | 2026-10-06 04:38:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2027d78a-0f71-3f0d-90fc-348d6685d4b8 | -3.06612 | -54.24687 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 79f6b5d1-f3cb-327e-b06b-14332f28e30d | -2.99323 | -54.11906 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2afffe85-b5fe-3281-b702-d58abfea3094 | -2.77419 | -54.10652 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f595ca17-b19e-3d9d-bdba-75fba0d284c9 | -3.09606 | -53.72524 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| acfe692b-0ef4-35a9-a80e-27eb7e81c7ab | -2.90155 | -54.02036 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab72cfa6-786c-30c9-ba3e-5ac4132018e9 | -3.94073 | -42.99602 | 2026-10-06 04:38:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d075556c-dc04-3712-b7dc-6b3899d7eb2c | -3.09354 | -54.16457 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9d0b962e-7480-3802-b8b4-8ffa18a0603c | -3.58118 | -54.3151 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a4abcae-d97b-356c-8ccc-0dcbcf54bf42 | -2.41114 | -48.2107 | 2026-10-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7560b1e-daf3-3843-9a43-98b2923a013f | -4.45456 | -40.05 | 2026-10-06 04:38:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8896f05-68d0-3b2d-a7e1-ae485547de24 | -3.49143 | -54.62681 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README38.md)
