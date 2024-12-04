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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 537609e4-259c-3ace-9c5f-8771827c505a | -3.2591 | -53.6186 | 2024-12-04 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1bdefb0e-520f-30ff-928f-9db744f73a5c | -2.8012 | -53.0633 | 2024-12-04 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5e5afa35-dcfc-3264-94f1-cd71fdca4679 | -2.8197 | -53.0425 | 2024-12-04 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2f7d57f6-c6d2-3dfe-a7aa-c8caac25de0b | -3.259 | -53.659 | 2024-12-04 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 093b2337-1a7d-3623-887c-d037c158f279 | -2.8196 | -53.0629 | 2024-12-04 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e29417d7-48fe-3468-a990-173b5bc4dbb5 | -3.1269 | -54.6463 | 2024-12-04 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d6b751d6-7318-3cb9-bada-488cdb7c091e | -1.7361 | -52.6162 | 2024-12-04 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6985da75-064d-30a8-b21c-44790de957a7 | -3.1086 | -54.6268 | 2024-12-04 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 140c30fb-850d-3a62-9d14-cfda4f9fd686 | -2.6242 | -45.7399 | 2024-12-04 04:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e3cb5aee-db9b-3429-baaf-87a6cdf3b050 | -3.259 | -53.6388 | 2024-12-04 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| de3fdce8-390c-3d3d-b2ba-976657a1fe19 | -1.7728 | -52.636 | 2024-12-04 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d2138def-9576-3146-aea4-aabf03a6be21 | -1.7545 | -52.6159 | 2024-12-04 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| bcf7877b-0dba-31c1-93d3-afe9c94586d1 | -4.1223 | -43.9299 | 2024-12-04 04:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 960fdf78-5909-394e-9869-bfb6ecd9e6b5 | -1.7729 | -52.6156 | 2024-12-04 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 16ee10ca-0845-3e92-b884-a3e6550695d1 | -1.7544 | -52.6363 | 2024-12-04 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 76ba0f82-170d-3358-b0ec-ecf34f6156dc | -3.1086 | -54.6068 | 2024-12-04 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1de3ae9b-5e9b-30d5-b582-24ddfc3126f0 | -2.6428 | -45.7394 | 2024-12-04 04:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d49614cf-9f8b-3ce7-a252-ec768d106745 | -3.1269 | -54.6263 | 2024-12-04 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 319.8 |
| 6748232d-211f-30b9-9e59-8beb4417a711 | -3.2591 | -53.6186 | 2024-12-04 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d23ca5b6-cf6b-31df-91a0-db2a4b788437 | -3.127 | -54.6063 | 2024-12-04 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 229.3 |
| 5df5e7d6-9fae-3bf5-afd1-621442b405aa | -3.259 | -53.6388 | 2024-12-04 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5033e927-5992-34d2-a489-475da301f1ab | -1.7545 | -52.6159 | 2024-12-04 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| f0aaff6a-26bd-3d12-8389-9588d740778c | -6.0858 | -48.0774 | 2024-12-04 04:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| dccb7607-e52d-3315-944c-c4e7f1a01ecf | -6.0674 | -48.0569 | 2024-12-04 04:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a8f8b5c7-3dec-3a70-b0c2-93d63de7120b | -3.2591 | -53.6186 | 2024-12-04 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6034e269-a4ab-3784-bfe9-a6bdb8afe12b | -3.259 | -53.659 | 2024-12-04 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e40ae1c1-f3e4-3bfa-86e0-b7a3d20ad290 | -1.7728 | -52.636 | 2024-12-04 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 163eb659-014f-325f-bccc-81a932a53cdc | -3.1453 | -54.6259 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 645deca0-7b6b-39aa-b7be-32207f46c389 | -2.6242 | -45.7399 | 2024-12-04 04:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f725a12d-e4f6-3285-9e9d-eadbb5613205 | -4.1223 | -43.9299 | 2024-12-04 04:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 05be03d9-5502-30e3-8d85-dc1d29007b4d | -3.1086 | -54.6068 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 89d48332-01bb-30df-8350-e8f2f9ab6dbf | -1.7361 | -52.6162 | 2024-12-04 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 442198af-e8db-327a-99cf-db6c11a516c8 | -5.5882 | -45.1412 | 2024-12-04 04:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 63c909ad-0be0-33b7-bee7-93104acf1330 | -3.127 | -54.6063 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 9722829e-3e19-3607-bba5-f1a6a69f1e47 | -2.8197 | -53.0425 | 2024-12-04 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 332c2998-01bd-397c-ba74-8e1e3f873513 | -6.086 | -48.0557 | 2024-12-04 04:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b2246c8e-330c-3646-b87d-1d90b98a8860 | -5.5695 | -45.1425 | 2024-12-04 04:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| cfdff85b-b9b4-323c-96e5-95ab0d22e960 | -1.7729 | -52.6156 | 2024-12-04 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fd148a37-46ed-3e90-8170-da144b3f4188 | -5.5693 | -45.1651 | 2024-12-04 04:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e33eaf48-a64b-3931-9135-45a10c016e7a | -1.6241 | -53.5308 | 2024-12-04 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 017904c9-2c2b-3577-9d18-03c3bfa17cda | -3.1454 | -54.6059 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 64e59017-7a91-3dd3-ad39-af9b1c8e776c | -5.588 | -45.1638 | 2024-12-04 04:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8ddce69b-6045-3a65-bb2b-45ff4c09e9cb | -1.7544 | -52.6363 | 2024-12-04 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| da2bea0e-be44-3c43-9c36-0aeea2aeec53 | -3.1269 | -54.6263 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 277.9 |
| 2b693608-2919-314f-ae76-b0737902e3dc | -2.8196 | -53.0629 | 2024-12-04 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| dc5cfc7e-a255-3eac-b6f3-cb757642aefd | -3.1086 | -54.6268 | 2024-12-04 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 9a49e668-557c-3ee7-97d0-bb116198929e | -3.2591 | -53.6186 | 2024-12-04 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 78625c3b-6f66-33d4-bec1-35642ea9476d | -3.1453 | -54.6259 | 2024-12-04 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 49626d98-e411-31e5-8f5c-d106160bcf00 | -3.259 | -53.6388 | 2024-12-04 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 08f15449-6af7-390e-811a-382f372f7096 | -1.6241 | -53.5308 | 2024-12-04 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3919cd19-201a-386e-a619-a53c369fab7f | -5.588 | -45.1638 | 2024-12-04 04:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| df58d5ca-315a-3973-b77e-63f0a17e1aee | -1.7544 | -52.6363 | 2024-12-04 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| fb655e77-2e1b-3876-9090-bfb20179e010 | -2.6242 | -45.7399 | 2024-12-04 04:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c01865c3-40cb-38f4-89b2-00a10bed30b3 | -1.7729 | -52.6156 | 2024-12-04 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5fd8c27b-de54-3084-a2cf-d5120e49f9b5 | -3.1086 | -54.6268 | 2024-12-04 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7316923d-c1a2-34cd-9c5a-42d602908fe6 | -3.259 | -53.659 | 2024-12-04 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c500dbae-b835-3925-9159-9a7ce6775426 | -3.1269 | -54.6263 | 2024-12-04 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 320.9 |
| 1940dc3f-7d26-3f8e-86f4-3bb808e5dbcb | -3.1086 | -54.6068 | 2024-12-04 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2ee56a56-002e-3229-affd-9718d3626938 | -1.7545 | -52.6159 | 2024-12-04 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 11112b53-2f25-3c77-bebc-421f5aad1c60 | -1.7728 | -52.636 | 2024-12-04 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fb2025cd-806f-3b44-8157-65e9d4a70837 | -4.1223 | -43.9299 | 2024-12-04 04:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bb026912-27c5-3848-9e32-ecece4864954 | -2.8196 | -53.0629 | 2024-12-04 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1e2b973c-b5f7-30dc-8141-a6dea21687eb | -1.7361 | -52.6162 | 2024-12-04 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| dd0fe050-a7d3-36ac-9bb8-22121a2c2439 | -3.127 | -54.6063 | 2024-12-04 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 211.0 |
| cdd80819-f98e-302c-adbf-87542bf9508f | -5.5695 | -45.1425 | 2024-12-04 05:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2487b0ed-fbf7-3db3-8c50-f98210893206 | -3.1269 | -54.6263 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 3b0e2448-cb64-3c37-8538-706125bd3763 | -5.5693 | -45.1651 | 2024-12-04 05:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f10d0106-1841-32a9-8bac-b3a02010b014 | -3.1453 | -54.6259 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2a5bd3b3-e6c9-3576-8520-6da53260a48b | -3.259 | -53.6388 | 2024-12-04 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c1c5abeb-4a5b-3f81-b897-9f107f08a9f7 | -1.7361 | -52.6162 | 2024-12-04 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b4108a73-efd1-3762-b71e-6a30af4192b9 | -3.259 | -53.659 | 2024-12-04 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d5e6fced-3971-3762-a983-458864548b77 | -1.7728 | -52.636 | 2024-12-04 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5793e7a7-6ceb-372a-aa5f-aca90a6fb764 | -2.8196 | -53.0629 | 2024-12-04 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a7d04058-a090-3099-bea7-74f1c0785f0d | -2.8197 | -53.0425 | 2024-12-04 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 93470412-2480-3723-b579-175cfe6bff64 | -3.1086 | -54.6268 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 42e25a79-58dd-32e3-8efd-537a84122c2c | -1.7544 | -52.6363 | 2024-12-04 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 4c847f41-6e79-39e9-8ef9-8995692110bd | -3.2591 | -53.6186 | 2024-12-04 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e3c9e873-7457-37aa-aadb-bb7e66838d24 | -3.1086 | -54.6068 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0aa30c49-b1ed-3ebc-bfc8-f5b2a4b3ed01 | -3.1454 | -54.6059 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 773c9572-ab58-3776-828c-35a10c875f6f | -1.7545 | -52.6159 | 2024-12-04 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 0906070d-51c5-3278-bedd-0f916f9e2497 | -3.127 | -54.6063 | 2024-12-04 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 9c50d4a6-81f2-3bee-8351-459a35ddd0ed | -2.44712 | -53.62959 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b225ef-1823-3e4f-93da-4c60ada4fae2 | -3.31 | -53.35285 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e98b0a5-87ee-3cbb-91f1-1c0c0c4749cc | -4.11971 | -46.90959 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a76e918-35c3-3e5c-a212-5f61aeb8156b | -3.12313 | -54.62386 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d06ad69f-a044-33ec-b386-9cc27e351405 | -2.81559 | -53.05726 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62acab67-1ee5-3890-9002-e69fd574309d | -2.5574 | -53.40945 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c85ce1c1-c362-378e-bef2-e915aa39b4fe | -3.55665 | -50.40092 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 714879df-8026-3825-9ec2-561ba2b050cc | -3.0725 | -53.76109 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25aa4b85-8d4f-37ad-871c-6be5d7dca758 | -2.99229 | -54.91761 | 2024-12-04 05:03:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554816a3-5a8f-3ff6-a6a0-00d0f6987b94 | -2.67297 | -53.04758 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bcdbb43-da28-35a3-b575-99caa1feae75 | -2.86462 | -53.98923 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 437a8a30-15c7-3dbf-981a-0101812482d5 | -1.51964 | -60.32458 | 2024-12-04 05:03:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 323f7964-3822-3196-a01b-b26efb531e3c | -3.11021 | -54.05198 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b0fe0a0-39a1-3f51-9d37-4e4d0ec0e6e2 | -2.79777 | -53.05836 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7f01f5d-ac75-3448-9c6a-76880d9e85f5 | -3.1165 | -54.62283 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 024f9bb3-9159-3fc2-91e4-4f0e1c95ffd6 | -2.7784 | -55.37347 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affbc631-e7ae-32cd-ad3f-fc8ab60c3b8c | -3.1303 | -54.62142 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| d87b91aa-fab8-359a-9f8f-c4a7c113504e | 1.32912 | -60.7246 | 2024-12-04 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2beedb00-c924-3d29-a3eb-89d73f6f97f5 | -1.22003 | -52.10413 | 2024-12-04 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
