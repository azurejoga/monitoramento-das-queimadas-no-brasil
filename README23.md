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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 523e351f-fe97-3d1e-a265-fe3eba485534 | -15.5679 | -42.3794 | 2026-09-24 01:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5f594cf8-f082-3dae-90ed-8fdedad341b6 | -12.0605 | -50.2989 | 2026-09-24 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a7abdc76-9497-36ad-9b6e-c051ed0402e2 | -10.9115 | -53.9429 | 2026-09-24 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b14c4361-2916-3b76-91ce-27e05e8099dd | -3.4392 | -50.0896 | 2026-09-24 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7d137e04-a332-3c6c-b411-72b890ab70fb | -10.9115 | -53.9429 | 2026-09-24 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 44b6834a-2d3e-3341-bada-08ecbc16db5b | -12.4024 | -46.9579 | 2026-09-24 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 198bdf20-9b11-3745-80e4-a96d0335b7bd | -9.695 | -64.9081 | 2026-09-24 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1be306ad-5330-3a9d-9925-18b78b52ae1d | -11.9586 | -50.7393 | 2026-09-24 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f1bb5921-89c6-3be8-8070-eba75e84c36d | -3.4577 | -50.089 | 2026-09-24 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 37df9ee5-7d5f-3bf3-ab3d-179513e624db | -15.5686 | -42.3547 | 2026-09-24 01:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2a311982-f400-3078-aea7-0c3bb6220801 | -1.842 | -54.7313 | 2026-09-24 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 384e8a4f-2855-3e28-a344-5ca9faf5b8a9 | -6.3501 | -57.7717 | 2026-09-24 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a9a8454c-4d38-3720-ae74-f8c9c568e5a1 | -4.9876 | -45.5637 | 2026-09-24 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 018b83a5-9afe-3935-b5e4-18a2180e4f2d | -4.1181 | -51.0695 | 2026-09-24 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9c4d0e09-f9c3-3443-b8e8-2b86ecf3bebc | -10.2827 | -49.9606 | 2026-09-24 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 92c158f6-5980-3940-a521-ce1caab9e557 | -12.4216 | -46.9551 | 2026-09-24 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7c74c86e-b117-3496-b2fc-3299e6cd8e8c | -5.0064 | -45.5401 | 2026-09-24 01:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 58bc194b-3141-382a-b8f8-95d46543e0fe | -6.5962 | -59.9279 | 2026-09-24 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| a8a38dfe-4303-315c-acf7-fc2b5b89e342 | -9.6949 | -64.9269 | 2026-09-24 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 28a1ef92-f412-30ee-b9d3-b249068697d8 | -12.0605 | -50.2989 | 2026-09-24 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4d3d5e96-c73a-3808-a1d5-76a47b9a587d | -4.118 | -51.0903 | 2026-09-24 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 88a4b37f-5ac8-34a2-93e3-5e2d571e8d45 | -6.6331 | -59.9265 | 2026-09-24 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 87b80129-94d5-3101-8b8f-eae402c6806c | -11.9396 | -50.7415 | 2026-09-24 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 92c4104a-78f3-3624-82f5-cfd9218fb4b7 | -6.633 | -59.9457 | 2026-09-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 37de5bbb-90d3-37bd-b22e-77b1665a322b | -12.0414 | -50.3011 | 2026-09-24 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 062fb538-3396-31d6-a324-46312ef81a2c | -12.0418 | -50.2796 | 2026-09-24 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c2a5d5b8-304f-39ab-b9e1-00625ea64c7c | -10.2637 | -49.9626 | 2026-09-24 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 80f851c0-7120-34f6-b5e3-b1107adef9bd | -3.1637 | -54.6054 | 2026-09-24 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e1f396db-bf88-305e-98a7-d88c02cf3b6b | -9.0158 | -60.5138 | 2026-09-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| b6a86b26-8bb1-355b-8487-19dd5a1e4d72 | -6.6146 | -59.9272 | 2026-09-24 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 7ada3cc3-dc6a-3010-9f42-c96bebce436d | -5.7754 | -45.1053 | 2026-09-24 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 1f63608a-5c89-3c43-9c81-0b728b46b14a | -1.8421 | -54.7113 | 2026-09-24 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ae9b6229-ce8a-329f-8e93-5304ae1b8c96 | -11.9392 | -50.7629 | 2026-09-24 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 08191df1-47ec-3746-9b0a-00ed3b36ffd2 | -10.1281 | -50.233 | 2026-09-24 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| dfcf76f6-ea72-3307-9fe9-4bf4ba45bd94 | -11.9583 | -50.7607 | 2026-09-24 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b0136ada-2e05-393f-9fe9-c000767e864e | -4.9877 | -45.5412 | 2026-09-24 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 18c95639-fca4-3802-98b9-29c7a4da71f9 | -6.6145 | -59.9464 | 2026-09-24 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| cdf9310b-72fe-3484-9ba0-0559af84b487 | -10.0731 | -46.0254 | 2026-09-24 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 56757165-0b4f-38be-994d-5b70d73d76f0 | -4.9876 | -45.5637 | 2026-09-24 01:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 228.2 |
| d860716a-5973-3cbc-aa0a-4eba277faef2 | -6.3317 | -57.7725 | 2026-09-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 6a87461e-8091-3edf-aa0c-bafc322fd264 | -5.0062 | -45.5626 | 2026-09-24 01:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 65948ec1-5ab3-349b-a57f-ce361249cd60 | -11.9586 | -50.7393 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 13df076c-685a-3957-9548-e11299bbf2ed | -6.6331 | -59.9265 | 2026-09-24 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0e14edcd-643c-3aa2-bcf8-e3d10c1e2f9d | -10.0921 | -46.0232 | 2026-09-24 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 17929633-a7f8-31b3-9fea-d458a140fe48 | -5.0064 | -45.5401 | 2026-09-24 01:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 7133c295-eed8-347f-ab7b-56cede17577b | -13.7801 | -54.0639 | 2026-09-24 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9e35810b-2205-3a59-86c9-3a66b518ee10 | -4.9877 | -45.5412 | 2026-09-24 01:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 377.2 |
| 2cb13b53-3232-3a16-803e-59e13e4af525 | -11.9583 | -50.7607 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| de5a3811-9865-343c-9b81-b6f71a044e87 | -5.7754 | -45.1053 | 2026-09-24 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 96aad639-67bd-370b-9d35-45844dde1382 | -11.9396 | -50.7415 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 216.8 |
| f80116e1-7e9b-315c-be28-8ebbf2bc9845 | -10.0924 | -46.0005 | 2026-09-24 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 7ad27408-2538-37c8-8797-c29739fb8ff5 | -13.7993 | -54.0617 | 2026-09-24 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5711221e-df41-3175-b154-25be21809227 | -6.4487 | -59.9526 | 2026-09-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2afbc2c8-f20d-3f4f-a8ec-5c22f424f5d7 | -11.9392 | -50.7629 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 6d7c7f04-3d9e-3189-9d63-b43faa61d141 | -6.4303 | -59.9532 | 2026-09-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3ae192a9-b2a7-3fe5-9554-b338871a35ed | -6.6146 | -59.9272 | 2026-09-24 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| f259db4a-640e-3308-9cdf-395dd8deacf1 | -6.6145 | -59.9464 | 2026-09-24 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 32fcdc59-5a1f-3f54-b1d9-0f433db50930 | -4.1181 | -51.0695 | 2026-09-24 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 48bb35a7-b1d3-326f-b0c1-59017c730727 | -6.5962 | -59.9279 | 2026-09-24 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 74c00706-8c34-3ce8-b04f-8933854ee661 | -10.1092 | -50.2349 | 2026-09-24 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 707ee154-137f-3b38-8a85-5af9e1aa4efa | -3.4577 | -50.089 | 2026-09-24 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5ed4b329-e9f8-34bb-8a8b-f6831b8d333f | -12.4216 | -46.9551 | 2026-09-24 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 916d98a8-80b8-3372-891e-a62dc1160c3f | -1.842 | -54.7313 | 2026-09-24 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 4cf4a431-0a01-3264-b775-8ba85a1f5fc0 | -9.0158 | -60.5138 | 2026-09-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b573b09c-cedd-3654-9e8e-1f2ff6e8fda7 | -12.1494 | -50.717 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5df04e66-f540-3ce0-9873-29562b72bd76 | -10.0917 | -46.0458 | 2026-09-24 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 11b2927a-084b-3fbf-8830-4f1d4b855a57 | -9.695 | -64.9081 | 2026-09-24 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7c93738f-dbca-382e-ae19-91b59f4ed723 | -6.0928 | -57.6262 | 2026-09-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 90e8c37b-0726-39d2-b501-b55c37a9a6a8 | -10.1284 | -50.2116 | 2026-09-24 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 121d31b9-4b1c-3d3d-91b1-229393e986a5 | -1.8421 | -54.7113 | 2026-09-24 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4dd3db8a-47ea-3860-9fa7-0f6118afb1a6 | -6.3501 | -57.7717 | 2026-09-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 376a603e-0b03-3082-a294-cab7d50058d2 | -12.4212 | -46.9777 | 2026-09-24 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| edf3a6db-ea1d-38a0-9002-a0738b5784bb | -4.118 | -51.0903 | 2026-09-24 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1cd8245c-3801-30f0-b8cd-3d266094b47e | -13.7996 | -54.0409 | 2026-09-24 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 62edda6a-ef23-3fb4-8850-f9660cb595d5 | -11.9205 | -50.7437 | 2026-09-24 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| c1c00835-5f02-3509-9286-6d389e1d0719 | -7.8996 | -61.1772 | 2026-09-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 07106164-7730-3e43-a68a-ea703a06b2b5 | -10.1095 | -50.2135 | 2026-09-24 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ebc3f08d-eba6-33e5-a9cf-acb0616e8ef2 | -6.633 | -59.9457 | 2026-09-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b049e979-5490-3846-8e67-076d01fc22ce | -10.1281 | -50.233 | 2026-09-24 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| f6af1e4e-8923-3aa2-ae1f-7778b7f442b2 | -10.0921 | -46.0232 | 2026-09-24 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 67af2520-c6f3-3991-81cc-059aad493ddd | -6.6146 | -59.9272 | 2026-09-24 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0637e451-1ceb-37cf-bafd-b8bd95440e6b | -10.1281 | -50.233 | 2026-09-24 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9ac41ee6-ff60-3d59-99c3-1f2721da2599 | -3.6764 | -60.5649 | 2026-09-24 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e2c59a28-6cae-3547-94c1-9af3c2d5a2d7 | -7.8996 | -61.1772 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 020c5ed1-4bbe-3668-9238-7b26187c08eb | -11.9202 | -50.7651 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 649c2b4e-385a-30ad-b8f7-31836dbbee6f | -5.0064 | -45.5401 | 2026-09-24 02:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 239.8 |
| d48609a9-ed1d-3f89-bd15-537b6476360c | -13.7801 | -54.0639 | 2026-09-24 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a2b33f57-152f-3b5f-8fa8-2c5392387471 | -5.0062 | -45.5626 | 2026-09-24 02:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d246ffa9-fb51-37e6-8c12-461ea6b9bbb0 | -11.9583 | -50.7607 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 532e189c-71d8-3cf6-b8b5-b3125ce3f375 | -3.6763 | -60.5839 | 2026-09-24 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 451dc58c-e444-3536-ae9e-7cdf13643dec | -1.8421 | -54.7113 | 2026-09-24 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f5fc4ca7-5f2a-33b5-a99c-b8881240c60e | -11.9205 | -50.7437 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| dd677202-2797-319e-a685-0444959e5320 | -6.4487 | -59.9526 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b38f6481-55a0-36c0-8e9d-372073a7a21e | -13.7993 | -54.0617 | 2026-09-24 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 22dad3bf-eb82-3f63-9dd9-3e1d2644b7e4 | -11.9392 | -50.7629 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 77735082-70a4-36ee-aeca-7427b3278336 | -4.118 | -51.0903 | 2026-09-24 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6b487381-516f-3749-baa6-7d83961e7b3a | -10.1284 | -50.2116 | 2026-09-24 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 2bca42fe-0a81-3f01-ae66-d0e12c26cd95 | -3.1637 | -54.6054 | 2026-09-24 02:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a49b9bbb-40ad-393a-bb28-31fa88bdf8b9 | -4.9876 | -45.5637 | 2026-09-24 02:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 255.5 |
| ed379385-f8cd-315c-8304-f22a68f5f2b7 | -10.1092 | -50.2349 | 2026-09-24 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |


[Clique aqui para ver as próximas entradas](README24.md)
