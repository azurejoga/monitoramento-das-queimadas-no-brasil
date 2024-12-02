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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c7a1fa3-a131-3de2-81ed-b364a9cd5be7 | -3.4201 | -50.2375 | 2024-12-02 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 65b89d56-fe3c-3a14-9b62-c85e9b287ee3 | -6.0862 | -48.0339 | 2024-12-02 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| da1f1d39-aa91-3bc5-89b4-141c25be4953 | -3.3664 | -49.8602 | 2024-12-02 00:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 80252f7e-8158-3bc5-af5a-ed430feb5103 | -3.4769 | -46.0879 | 2024-12-02 00:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 806c7977-eec8-31ae-9cb9-5a3b881765d5 | -1.0735 | -53.4562 | 2024-12-02 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 233a8dc9-7e94-36c8-bf1b-82740ddc0fae | -3.2774 | -53.6383 | 2024-12-02 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| faa3fe24-acc1-3e6a-8653-e02d32ba4f44 | -4.267 | -50.8551 | 2024-12-02 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 21d24037-5a0b-35f9-8b28-9eeeed62551b | -2.9824 | -53.8879 | 2024-12-02 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 812c4289-4412-38d3-9b96-80d64cebceef | -3.4769 | -46.0879 | 2024-12-02 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f615448c-0ecb-378d-ab24-c584554ea6c2 | -12.4359 | -63.7264 | 2024-12-02 00:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 30b17068-caba-3c7d-bdfc-ec6f06c9cf84 | -3.6562 | -51.128 | 2024-12-02 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ff660a2e-978c-30ea-9618-f859d6ef1005 | -3.2775 | -53.6181 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 932566e2-7e2a-3482-bc9c-2eba64a46fb0 | -6.086 | -48.0557 | 2024-12-02 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 269.8 |
| cbafbf29-791d-3a01-9b58-c47aab7bae9b | -5.1367 | -43.2185 | 2024-12-02 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| be75afee-0b7f-37a2-ab05-779d557b1e11 | -5.118 | -43.2198 | 2024-12-02 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e7ce4ba3-a081-3a4e-a556-1ebfcb445f91 | -1.0735 | -53.4562 | 2024-12-02 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 132e1784-a640-3e6f-bd03-1ca622c932ae | -6.0862 | -48.0339 | 2024-12-02 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b477b354-cfa5-3c3e-ad3d-db0cae29f075 | -9.4184 | -35.8891 | 2024-12-02 00:40:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| eb4cf7b3-5dcb-34b1-9a05-d38eb1fa824a | -2.5428 | -53.3935 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 83c1393d-0bc5-3cd8-8fe5-3152f0714c60 | -2.5612 | -53.3931 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| e5431639-a405-3e23-a95b-dc5abc6d3aad | -12.4171 | -63.7274 | 2024-12-02 00:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4c86c473-fbfb-3e62-bc11-3abfec4dbeb2 | -2.0263 | -54.3289 | 2024-12-02 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 0572df58-e021-3503-aa72-baaaa1b4c15f | -2.8197 | -53.0425 | 2024-12-02 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c245ad65-bb18-3140-bd86-770a717fdd44 | -2.2667 | -53.6011 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 60b32bf2-161f-3c16-8285-8b9a258e81be | -3.6563 | -51.1072 | 2024-12-02 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| b592b39f-d462-3d33-8f61-2ea65f349e75 | -2.9208 | -45.8417 | 2024-12-02 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b73782b4-0122-3778-902e-6b8b878c5b2f | -2.5428 | -53.4137 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 0ba919ce-ad74-3740-b6a2-0e0ff9a58bc2 | -1.9171 | -46.4037 | 2024-12-02 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 72e12847-a05c-3ecf-a517-3245b5594a16 | -5.1369 | -43.1951 | 2024-12-02 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 79c154d1-232d-3643-8516-03aeffc34fef | -2.923 | -45.3487 | 2024-12-02 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c3fad380-196b-3b11-ac46-ac1f47975504 | -5.1181 | -43.1964 | 2024-12-02 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8fd4f734-9740-3c33-b206-dd4cb092a863 | -2.9044 | -45.3494 | 2024-12-02 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 9edd26dd-d3c5-3f70-a9a3-284c8b84b23d | -2.5612 | -53.4133 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| e21fc15a-62ae-3e55-9be0-d910bac17a74 | -12.2493 | -63.4688 | 2024-12-02 00:40:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9b71ce68-dbd1-3937-aff9-d3f94d80b11f | -3.4017 | -50.2381 | 2024-12-02 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d3d1bd99-e848-3005-a094-744b19bc70ab | -2.8012 | -53.0633 | 2024-12-02 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6b5a3f6c-a734-36b4-bfc2-660693d285cc | -3.4017 | -50.2171 | 2024-12-02 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 72ee14da-1ce9-3e18-98fe-be313a1af65f | -3.2591 | -53.6186 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| dfc4e520-0713-3bda-a17a-50eeddf05a9a | -2.8196 | -53.0629 | 2024-12-02 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b40b28c9-4008-3e0b-aebb-56ec123e4875 | -12.4358 | -63.7455 | 2024-12-02 00:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 36b36d48-f653-381b-a47e-cdda1638a0b4 | -2.0263 | -54.3088 | 2024-12-02 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| cbacf0bb-3d15-32ae-986e-5158b280669e | -3.4201 | -50.2375 | 2024-12-02 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c7811632-8885-309f-9ef8-c6a4e8265d47 | -4.5932 | -43.3471 | 2024-12-02 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e2407dd2-a3c8-3193-88d3-147f027ca878 | -2.008 | -54.3091 | 2024-12-02 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8462e6ab-bc15-378c-b751-f540e10fa204 | -2.5796 | -53.3927 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3525abd2-416b-353d-a148-0355318a1a86 | -2.9824 | -53.8879 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6bb6b6b6-1b36-34fa-82e9-9466d7c6db56 | -3.2407 | -53.6191 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f215440f-e67a-3164-b16c-0af03e65b83f | -3.3848 | -49.8596 | 2024-12-02 00:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8cf26598-1065-3b31-aaf1-86187b42e30f | -3.2774 | -53.6383 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fbc3f8f7-0522-31d8-94c6-ffaa84480932 | -12.4169 | -63.7465 | 2024-12-02 00:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c43be80b-9ee3-323e-a6d5-74ee2631e38e | -4.5745 | -43.3483 | 2024-12-02 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f70e4ca9-78a8-30c1-b903-5e02a134ab18 | -2.9871 | -52.5086 | 2024-12-02 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6401996d-b9cb-36a8-9072-ed8987073a9d | -10.6674 | -44.4835 | 2024-12-02 00:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4793cc43-bb9f-3110-8957-0dceb278ddda | -3.259 | -53.6388 | 2024-12-02 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 368ba1b6-e064-303a-9938-ecbe6625f681 | -2.8013 | -53.043 | 2024-12-02 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6ea28a7b-5c1e-35d4-847a-28a9d35c67db | -9.4377 | -35.8858 | 2024-12-02 00:40:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| a359ca4a-3b72-31d9-b308-564770aea538 | -2.2666 | -53.6212 | 2024-12-02 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9b831d6f-bcc4-3d03-90bc-ae1fe2ec99e9 | -6.0674 | -48.0569 | 2024-12-02 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 63d684e9-c0e9-37ad-be23-43f66d622903 | -2.2666 | -53.6212 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fcc707e3-170d-3b8a-b882-2ac1ff39e920 | -6.0674 | -48.0569 | 2024-12-02 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 60f9ec20-731a-3d54-868a-06398f29d22d | -2.008 | -54.3091 | 2024-12-02 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 81424059-61a0-3ee5-b65e-1ab043ed5b9e | -2.923 | -45.3487 | 2024-12-02 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f0fbd82a-2423-3c7b-b106-7b02c4c552c7 | -4.5745 | -43.3483 | 2024-12-02 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 815eaebc-ab6f-364d-adcd-22b47a858e31 | -4.5743 | -43.3716 | 2024-12-02 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9f28f45a-cb3e-337e-8421-5245895b0234 | -3.6562 | -51.128 | 2024-12-02 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2cb82c0e-2ffa-3460-a0ef-e4c3b1063b5e | -12.4169 | -63.7465 | 2024-12-02 00:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1a1a945e-031b-3f68-9d94-930e2508da33 | -4.9087 | -41.313 | 2024-12-02 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| ebe6a674-e6aa-362a-a122-fe832a081506 | -2.8197 | -53.0425 | 2024-12-02 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 62d258e2-a74c-3805-92a2-9695e21aab1d | -6.0676 | -48.0352 | 2024-12-02 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 977baaed-c1dd-3b6a-99a5-cf7286668607 | -2.5428 | -53.4137 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2317c82a-21d9-3e9b-b21b-d7d0ba4df6c5 | -4.9274 | -41.3116 | 2024-12-02 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 65195ae2-1af0-345c-ba85-49134059aabf | -1.0735 | -53.4562 | 2024-12-02 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8ecfbf47-552f-3112-9376-e0ff7c909290 | -2.5428 | -53.3935 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 05151544-83aa-36da-a5da-0cfdadf98227 | -2.8012 | -53.0633 | 2024-12-02 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3d58c1e7-8239-3640-9410-c03cff1acec2 | -6.086 | -48.0557 | 2024-12-02 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 64ac680b-92a1-3540-9fae-27d0dcc9a763 | -3.4017 | -50.2171 | 2024-12-02 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6082a48c-1ef8-3c39-8184-1722fd0078cc | -4.9083 | -41.3612 | 2024-12-02 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 3dc656fe-4113-3d83-9807-47830185f32c | -6.0862 | -48.0339 | 2024-12-02 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 134f06c4-ffc1-3307-abca-5d781afcaf89 | -12.4359 | -63.7264 | 2024-12-02 00:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 65cadcae-a04b-32d3-ab8d-05dd78622b8a | -12.2493 | -63.4688 | 2024-12-02 00:50:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 96b18a09-cc3b-3453-88b7-d92e0c074c57 | -3.3848 | -49.8596 | 2024-12-02 00:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 26099ede-f366-3aab-9bce-8c3b606e3566 | -2.5612 | -53.3931 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 570b10d8-c22e-3439-9e17-81d0cdac8cc9 | -3.3664 | -49.8602 | 2024-12-02 00:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 08877709-758e-30eb-b630-a6335bd32fb4 | -4.267 | -50.8551 | 2024-12-02 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4981d1c2-01ee-3192-b3d1-3544ba55351d | -12.4358 | -63.7455 | 2024-12-02 00:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 68d76e0a-6bb1-33bc-8ff3-8fba17746c48 | -2.8013 | -53.043 | 2024-12-02 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cadee8ea-5d4f-3e36-bab7-8449346ce10a | -12.4171 | -63.7274 | 2024-12-02 00:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 84831410-3883-3a87-8683-57eeb7d583a1 | -20.7217 | -54.4341 | 2024-12-02 00:50:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bd7abd7c-9fcf-342d-b265-8a84952fade5 | -5.5882 | -45.1412 | 2024-12-02 00:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5595797c-67e6-3cd9-acd2-4cf1a43932cc | -3.4017 | -50.2381 | 2024-12-02 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 449d498f-cc1b-370e-907d-ab7010433fec | -2.8196 | -53.0629 | 2024-12-02 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7734902e-2ea6-3ee4-904a-79af1661a3fb | -2.0263 | -54.3088 | 2024-12-02 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 84e7713c-c40f-3544-bae0-c4749f36644c | -4.9272 | -41.3358 | 2024-12-02 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| f4444a35-746d-3f0c-b421-0f2b0878557c | -3.2591 | -53.6186 | 2024-12-02 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ab9147b2-40af-33e4-a96c-46578aeab08a | -3.7248 | -52.2819 | 2024-12-02 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8a344056-22c9-38b3-b368-d22994c5ef94 | -2.2667 | -53.6011 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0aef3454-34b5-31a3-b88e-f0f9ce1ef09d | -3.3018 | -52.0694 | 2024-12-02 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 44d5e4f7-b59c-3ac7-bf29-2bb6ddec1198 | -3.259 | -53.6388 | 2024-12-02 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 75fe8fbf-504f-3d83-902a-f81b7e91db9d | -4.9085 | -41.3371 | 2024-12-02 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| deab0c1c-93e0-3c87-8f5a-1d8a54b1ac48 | -2.5612 | -53.4133 | 2024-12-02 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |


[Clique aqui para ver as próximas entradas](README7.md)
