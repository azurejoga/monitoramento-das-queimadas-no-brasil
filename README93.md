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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af290842-f218-3a8c-a856-62ab64df6c44 | 0.3221 | -51.0038 | 2026-10-06 15:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4f27d1ce-fd28-3334-bfe9-ba3e3ae34215 | -9.1076 | -67.7215 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| faa0486d-9d1a-3806-8a9e-1c6cc0801305 | 1.8038 | -55.5656 | 2026-10-06 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bcba1c19-5d0b-3d57-95fd-35d90c5118da | -8.5367 | -67.032 | 2026-10-06 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 021c8f54-85fa-3abc-9a44-bab635a1a8b5 | -9.1426 | -68.2941 | 2026-10-06 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 386ef241-179a-3977-80ce-8fdd826bd08a | -9.8059 | -65.0354 | 2026-10-06 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a613e7a6-7068-37a7-87f9-f581a5b213cf | -9.1077 | -67.6845 | 2026-10-06 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e9f9dee9-7ed5-325b-ba2c-e8343c04b265 | -11.8814 | -64.9323 | 2026-10-06 16:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7afa6a99-febd-36fa-9508-3fb31f0e63fc | -9.1333 | -65.9186 | 2026-10-06 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 39cb59cc-e7fe-3485-aeae-099eb113a729 | 1.7671 | -55.5859 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| da0019eb-1b43-3bd8-b0a5-a066e1214a96 | 1.7487 | -55.6059 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 573e323c-eae9-35c0-81f7-e4009552f8a9 | 1.8767 | -55.7621 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8c1b838e-30b7-38da-9459-202466f33372 | -8.5183 | -67.0139 | 2026-10-06 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b5923cfe-0427-33a3-aac4-f65473123845 | 1.7304 | -55.6259 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e7470060-fdde-3ed1-95f4-451a3c0a40bc | -9.0983 | -65.4717 | 2026-10-06 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b4ca0bdb-0cbb-30bb-b7fc-c9cb278aea28 | -9.1221 | -64.4031 | 2026-10-06 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4a5a6ecc-88e3-35ba-98bc-593900e36b98 | -11.657 | -43.6373 | 2026-10-06 16:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.0 |
| ec9520c1-33bf-3f04-8e39-d5330f5d5ca2 | -8.7782 | -62.8703 | 2026-10-06 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7de93ec3-b692-3896-8a3e-77f81f70ca33 | -9.1072 | -67.8326 | 2026-10-06 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ccbfc491-c793-360c-a3d3-865da4fe8754 | -10.9758 | -45.4324 | 2026-10-06 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 310.1 |
| 0bf40d08-b4e5-3bea-96d0-4b2570363abd | 0.3221 | -51.0038 | 2026-10-06 16:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 126.7 |
| fb61ca3b-d679-371f-a142-eab95e982c89 | -9.1511 | -66.0859 | 2026-10-06 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c77a080d-9c58-3632-96fb-8df07315a39d | 1.8767 | -55.7424 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 7bff65db-6570-352c-a2e5-859684e69818 | -9.1442 | -67.8317 | 2026-10-06 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ca9a9240-6676-3b30-af6c-df3c1a0d7334 | 1.7855 | -55.5461 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c50dbc50-61d9-36a0-8f37-fbfa0fe41114 | 1.7304 | -55.6061 | 2026-10-06 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 60085fd9-644f-394e-a62a-d47cb525d35c | -7.3641 | -72.4622 | 2026-10-06 16:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| bf9a9433-feac-32ca-8c6c-a8a6edbc3ea2 | -9.1241 | -68.2946 | 2026-10-06 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f8c1d89d-702e-315f-9efb-8e51721cf248 | -9.1241 | -68.2946 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c620f8bf-f6c8-3a12-a585-9a8f26b5bf57 | -9.0705 | -67.741 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| c9b1ed46-4e93-325a-8ab2-4bf2d7bf22cb | -9.236 | -68.0516 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1e31713b-f019-32b9-968d-75ff1aebcb00 | 1.7304 | -55.6061 | 2026-10-06 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| be8e1b7b-7177-3206-b1fc-223e333dd2a0 | -9.1055 | -68.3135 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 117a8caf-c656-3f81-9727-2118e421a269 | 1.7854 | -55.5658 | 2026-10-06 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ba72d70c-c566-3eab-805f-c5c78430f84a | -8.6937 | -70.126 | 2026-10-06 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f6cfee0d-c844-3f6b-8c4e-a7384818c2a6 | -9.0585 | -66.0887 | 2026-10-06 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b67c6cc0-0f06-3bda-9367-41b5d8e37f71 | -11.8814 | -64.9323 | 2026-10-06 16:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 7a227295-56d2-3480-be98-5bc9fc9cf4f1 | 1.7303 | -55.6456 | 2026-10-06 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 48d63b8b-4da8-3d50-9119-7f3b28bc5755 | -9.1511 | -66.0859 | 2026-10-06 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| de22f916-00f7-3d1a-93dc-f47f3fdea29f | -9.1072 | -67.8326 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 461a4914-60dc-3c1b-98f2-efcfaa745431 | 0.3221 | -51.0038 | 2026-10-06 16:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 94.8 |
| c77f8f2d-ec8f-357d-9874-b3234ccbed91 | -9.1076 | -67.703 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 9574ef85-ccc2-3b7d-9512-8f62f24a6f5d | 1.8767 | -55.7424 | 2026-10-06 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 780d603c-02d8-3454-9166-917d1d461fd9 | -8.6753 | -70.1263 | 2026-10-06 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 43dd0f57-78e6-39b5-a18c-688f232a3179 | -9.0892 | -67.685 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a0767ca6-32a9-3449-8877-95ec87537dd2 | -8.852 | -66.7827 | 2026-10-06 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| bd42c0fa-2fef-3f09-af6b-f41cb344326e | 1.7854 | -55.5856 | 2026-10-06 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 88a48476-5fa7-34f7-8af0-19e97b10c55f | -7.3641 | -72.4622 | 2026-10-06 16:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 63ee2515-b1c6-3e34-9cc5-7aaa80b49325 | -9.1261 | -67.7026 | 2026-10-06 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5fda2ffa-624f-306b-9696-2e945328b581 | -3.39 | -44.44 | 2026-10-06 16:15:00 | MSG-03 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89ec60f3-89fd-353f-bad3-1ecfe2d2b5ae | -2.31 | -57.05 | 2026-10-06 16:15:00 | MSG-03 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de958c96-655c-3fd4-b690-81a34d14fc36 | -12.19 | -44.69 | 2026-10-06 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30322d07-2f3b-3773-9aed-2daceab388a6 | -3.5 | -51.67 | 2026-10-06 16:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3402d7c1-d511-3817-835a-041b776bf56b | -3.39 | -44.49 | 2026-10-06 16:15:00 | MSG-03 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1ea6682-666a-3b5e-9d6c-d25848965fb6 | -7.43 | -44.5 | 2026-10-06 16:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 21ef7b31-22eb-3d32-b683-e8414855d5d0 | -10.99 | -45.42 | 2026-10-06 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 731a7f24-3080-3410-819a-06da9578b508 | -12.22 | -44.7 | 2026-10-06 16:15:00 | MSG-03 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bde7755-17ed-3f6f-a520-ee16afa259ff | -9.42 | -45.91 | 2026-10-06 16:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c600b55-7222-3173-8c2e-ac7413ace0bf | -7.43 | -44.46 | 2026-10-06 16:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee757856-6c5a-3997-81aa-838d8ead34e0 | -3.29 | -54.01 | 2026-10-06 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22aacad7-e4d8-30f1-bf55-72d556e16bc3 | -8.5733 | -67.1422 | 2026-10-06 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5d2d5d7c-8f18-3c40-8f29-0f98d0c854f0 | 1.712 | -55.6459 | 2026-10-06 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e5473cb7-4c4e-3b5f-b83a-b75f973fa789 | 1.8767 | -55.7424 | 2026-10-06 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 888f18c7-093e-32c3-b7b7-4622ca24b66a | -9.1055 | -68.3135 | 2026-10-06 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9ab1ceb4-ad83-31c1-9374-ad2b73ce460d | -9.1261 | -67.7211 | 2026-10-06 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ca8f3b91-1bcd-3e80-a351-8ff73bca71fa | -9.1077 | -67.6845 | 2026-10-06 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3a3544a3-c338-348e-8de2-49b62a39bfbb | -8.9257 | -66.8549 | 2026-10-06 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ba4ceaa1-a854-3bd9-9f6d-353e16289a6a | 1.7854 | -55.5658 | 2026-10-06 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 62c1069a-c542-32c2-bbbe-a833b3e3c013 | -9.1221 | -64.4031 | 2026-10-06 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ea6d264c-bae0-3ca8-8e52-6ec2c5105d34 | 1.7854 | -55.5856 | 2026-10-06 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 99fbeb38-67ae-37ab-a5bc-9994a2593a83 | 1.8038 | -55.5458 | 2026-10-06 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| dd181834-dbb0-3905-9fd6-32bf7ef001ab | -8.6753 | -70.1263 | 2026-10-06 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9cd09793-a20c-3f1e-8234-15b6cfb0781a | -9.236 | -68.0701 | 2026-10-06 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5430165f-c949-3afc-ba90-e942c8ecd3e1 | -9.1055 | -68.3135 | 2026-10-06 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9bd5afd8-49f6-3ae4-aeaa-677542da1982 | -7.5657 | -73.0437 | 2026-10-06 16:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6ac7f774-fbb8-31e8-9e45-4934972a8e23 | -9.5593 | -66.0545 | 2026-10-06 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6b00b9e5-6f5b-34a6-b61c-73acc063d212 | -7.364 | -72.6079 | 2026-10-06 16:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e45c8d97-86e6-31bb-b62a-c64a8e8ee007 | -9.1221 | -64.4031 | 2026-10-06 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| deb2e4ab-e83d-3ef5-9b25-c633612e1008 | 1.8038 | -55.5656 | 2026-10-06 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5b386a56-7ca6-331e-95c6-d8f381227a66 | -9.8257 | -44.8011 | 2026-10-06 16:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 33efa881-32ba-3030-b05c-777d8f11f982 | -8.5733 | -67.1422 | 2026-10-06 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4d461d6f-b532-35aa-9bca-3b1e6a7d5e15 | 1.8767 | -55.7621 | 2026-10-06 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c5c51f18-53d5-3be2-b643-7faf0f67a55a | -9.1221 | -64.4031 | 2026-10-06 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a2264457-3464-3972-a429-ff78adc92a81 | 1.6202 | -55.7852 | 2026-10-06 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9d23262f-3170-3dd2-9ae0-d3fec1fab909 | -9.1438 | -67.9428 | 2026-10-06 16:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 515f9d10-b9e5-350c-b50d-84854b7f20d5 | -8.5918 | -67.1418 | 2026-10-06 16:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 54e1d5d0-0d48-3d5c-b1aa-cd69d12a950f | -9.1221 | -64.4031 | 2026-10-06 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 1f952715-0724-39c4-b41d-51f3e02d4564 | 1.8038 | -55.5458 | 2026-10-06 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c49bb1a8-811d-37c0-aa77-e4ae85645b83 | -9.1253 | -67.9432 | 2026-10-06 16:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6758d882-678a-3ca1-aded-5d68bf0b67e6 | 1.6202 | -55.7852 | 2026-10-06 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 0d6b21b5-acdd-34da-aa26-384cbba4ba24 | 1.8221 | -55.5456 | 2026-10-06 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1e42ccc3-b572-39ec-a51e-02e1ae6b3aba | -9.1438 | -67.9428 | 2026-10-06 16:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0a83ce12-6f45-3354-bd80-2385ff917cb1 | 1.6202 | -55.7852 | 2026-10-06 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 978a5a1f-35f5-382a-a76c-21f0a312ad83 | -8.5918 | -67.1418 | 2026-10-06 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4e26b072-604c-3d76-a950-1cd3efb30256 | -8.5733 | -67.1422 | 2026-10-06 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0727684f-75a6-3d16-b8a2-d3995b0ad242 | -10.7493 | -45.3024 | 2026-10-06 17:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f683aa27-af9f-3940-bf07-5726c0a22fd8 | -9.1072 | -67.8326 | 2026-10-06 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 41522eac-c072-33d0-888a-8b07e44a6644 | -9.1055 | -68.3135 | 2026-10-06 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| cbd963bc-1a5e-360c-a0a6-ce71636d45ed | -7.364 | -72.6079 | 2026-10-06 17:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 86fd99bb-a7cb-3e33-a781-7fd11d4f00d3 | 1.8038 | -55.5458 | 2026-10-06 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |


[Clique aqui para ver as próximas entradas](README94.md)
