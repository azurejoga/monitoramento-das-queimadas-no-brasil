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
| 5d79c5d3-93d5-3d3b-91d9-759d445293eb | 1.5041 | -59.92635 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 30d5ca80-a952-3d2e-b8a2-c5803c3912a8 | 1.48529 | -59.92944 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 405d735e-6002-3906-aa1a-14a3ccdd48b5 | 1.49941 | -59.93701 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46893ca8-8110-3ade-be6e-359455eff939 | 1.47902 | -59.93049 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0e428270-c630-3f07-a5bf-c1cf5768e4d2 | 1.48275 | -59.9141 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85193321-bb9d-3213-a14c-14973b6d98e4 | 1.48611 | -59.93443 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 4fe7a36f-06c6-300e-83b5-6af50aa716c6 | 1.47819 | -59.92548 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 17827a8f-86b8-3c96-b00b-8397d6b57e3e | 1.48062 | -59.94016 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75187910-1ffd-3e8e-9993-a41de5ccf495 | 1.48768 | -59.94392 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59a729ad-a99e-3daa-ad52-4343bb5dd810 | 1.47734 | -59.92036 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c391ddfa-e1fa-3838-b408-27aa04117e11 | 1.50323 | -59.92111 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81778301-cfe0-3855-befe-136019769d0f | 1.47352 | -59.93612 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2baf24db-68b3-3f47-a121-f65e4377a77d | 1.49693 | -59.92195 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f3f9f943-b83e-3990-9c22-5554102073d2 | 1.50723 | -59.9454 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec8b6399-cf92-39fe-bcb4-36725c7e6a1c | 1.42738 | -59.95223 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420677dc-360c-3f3d-8796-ad5bee5f5005 | 1.48143 | -59.94503 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8efb399c-621f-356b-8698-8e771f408c3f | 1.87955 | -60.91355 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7b80ebe-1604-3eff-868e-1c317d231715 | 1.88023 | -60.91768 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99d0ab42-74b0-35c5-893a-28a2b42c9bcd | 1.49394 | -59.94287 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36782e28-3fa6-3be3-9a76-1680ce1364ed | 1.48984 | -59.91804 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd8757e2-3be8-3e42-ba48-00ef0dc7b990 | 1.51111 | -59.92986 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6f967e87-d6ed-3570-9536-96e1afb12ccc | 1.49779 | -59.92719 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b2e30639-5e68-3661-bef9-edae7bd43bed | 1.4836 | -59.91922 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| a6a082b8-9f2e-3ece-af74-f05215510d88 | 1.49317 | -59.93817 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c461a2-d43a-3f31-b5ae-10f017f31ff6 | 1.49153 | -59.92826 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75055d47-e0d9-33a7-807b-51391c5ea15e | 1.87438 | -60.9187 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6667d76-e091-3b64-9a7b-ad1e260912dc | 1.49068 | -59.9231 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 09625888-645d-3787-8796-414c1ab0aa79 | 1.49862 | -59.9322 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| abfb609a-b4d6-345a-abf0-8423321e49a8 | 2.87762 | -60.60338 | 2026-02-28 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29bbb4a7-4c01-3a95-8922-32bdcbb52e98 | 1.8737 | -60.91458 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 419a0b44-ee1b-31d4-b0ad-6498a7fbf1c8 | 1.51268 | -59.93942 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cfdf68fe-517f-35e0-976a-ec7a8ef73ed3 | 1.47434 | -59.94109 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9c6a2a9-4dd1-3297-b3e4-ce4a306b71c9 | 1.50019 | -59.94174 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95efc744-124c-3f0c-9ed9-7909aa8f2cd9 | 1.50644 | -59.9406 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 20075697-f9da-3d43-be25-d3875c79706a | 1.51033 | -59.9251 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3e67b97b-65f8-3a51-8cb7-688e0ecc5fa4 | 1.47268 | -59.9311 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 4970f8b5-0588-357d-8297-34faf5fc3890 | 1.50566 | -59.93588 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cca94bd3-fe61-3b21-af9f-dde4e1095eeb | 2.87834 | -60.60764 | 2026-02-28 06:18:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3be41bc5-413b-3e70-bfd7-799984e48ab7 | 1.48691 | -59.93927 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d50dd3f8-6136-365b-a117-a3e34c0d959d | 1.43367 | -59.95135 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208f79d4-349f-3019-8c93-fbb7b0f40594 | -20.51981 | -50.8326 | 2026-02-28 06:22:00 | AQUA_M-M | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| fc4ca1d6-c4f7-3f83-bbe5-3bdc2e173961 | -20.51101 | -50.83111 | 2026-02-28 06:22:00 | AQUA_M-M | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7499f39b-48c1-3065-adc7-df48d0308655 | -21.68008 | -56.31436 | 2026-02-28 06:24:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c057b3b5-5011-35f0-ac80-2251d7574240 | -27.44314 | -48.44247 | 2026-02-28 06:24:00 | AQUA_M-M | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e17d0abe-1026-39ef-91ba-b51d4b8626a4 | 1.49722 | -59.9456 | 2026-02-28 07:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 10b90d4a-1adb-38b8-81be-b9cc92ed0de2 | 1.4864 | -59.9117 | 2026-02-28 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 6fa0eb0d-f80e-3158-bec8-8ddcd5be6df8 | 1.5046 | -59.9306 | 2026-02-28 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 080fafd9-a22e-3d78-b32d-77f466410074 | 1.4681 | -59.9309 | 2026-02-28 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 1fea35ce-3434-3d4c-a360-8e46542a6c3e | 1.4864 | -59.9308 | 2026-02-28 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 3965d12b-7808-327c-bb16-4a90e819708b | 1.4681 | -59.9309 | 2026-02-28 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.4 |
| db6d4c3b-3a60-3be0-88b0-b975805bccc6 | 1.5046 | -59.9306 | 2026-02-28 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 5d44b384-f736-322a-aa2d-0e96d5ec3ca9 | 1.4864 | -59.9117 | 2026-02-28 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 5e9c4c50-502e-371e-bda7-5307706d896c | 1.4864 | -59.9308 | 2026-02-28 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 3c96ef73-7e14-301d-9592-de23835e2765 | 1.4864 | -59.9308 | 2026-02-28 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 5a18870d-bc6b-3c3c-8ff5-eedd19531db3 | 1.4681 | -59.9309 | 2026-02-28 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 23a9105a-9620-3cc3-85d0-56256e013422 | 1.5046 | -59.9306 | 2026-02-28 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| eb30ffc5-7867-3800-8dee-30cd42ba7dbe | 1.4864 | -59.9117 | 2026-02-28 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 99ca7606-2029-347d-a0e7-60b413f1e91f | -21.7001 | -56.3109 | 2026-02-28 12:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 46a9db65-57b0-32ca-97ea-01819a991cb0 | 1.4864 | -59.9117 | 2026-02-28 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 1960d461-e56e-3521-bc33-0e6d7c3d9643 | 1.4864 | -59.9308 | 2026-02-28 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 15eb83f6-71de-36c9-8b5d-a82677524308 | 1.4681 | -59.9309 | 2026-02-28 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 410e1f11-141e-3450-8bf7-39d52afbbfec | 1.5046 | -59.9306 | 2026-02-28 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| d8b836da-1d92-3249-ad3c-7e8e3dcef6b2 | -21.6795 | -56.3142 | 2026-02-28 12:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 32e3f193-8a41-3304-84ad-9325bbebad3d | 1.5046 | -59.9306 | 2026-02-28 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 732c727d-477a-329b-9767-12553647f0ff | 1.4864 | -59.9117 | 2026-02-28 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 08234979-04ed-3b4d-b710-a973a6470e73 | 1.4864 | -59.9308 | 2026-02-28 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 200.2 |
| e5e6eb9b-17b5-3889-94dd-496144037bfa | 1.4681 | -59.9309 | 2026-02-28 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 6df0c241-f76a-36e6-8403-5c8c293e5277 | 1.5046 | -59.9306 | 2026-02-28 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 48cd6a32-4c37-3cac-a8f9-be036aec62ab | 1.4864 | -59.9117 | 2026-02-28 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 28ec7cd9-4557-319c-8388-662bcb02c253 | 1.4864 | -59.9308 | 2026-02-28 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 231.9 |
| f4805c07-f9a5-3fe0-8bdb-de77778f8a99 | 1.4681 | -59.9309 | 2026-02-28 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 0b1db75c-a294-3946-8d0f-4b241c59e933 | -21.6795 | -56.3142 | 2026-02-28 12:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0af2e626-e5a1-3931-8b3a-2cd211a0f205 | 1.4864 | -59.9308 | 2026-02-28 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 261.7 |
| 086628e8-34cb-3080-ac32-815b90956e5d | 1.5046 | -59.9306 | 2026-02-28 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 7554e663-ad80-3b21-9432-e4534613e22d | 1.4864 | -59.9117 | 2026-02-28 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 185.6 |
| cbe69d93-b5c5-3a7a-bc5a-da049aa0f277 | 1.4681 | -59.9309 | 2026-02-28 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 0fa1c62d-3f12-3cc0-85b7-f5f44e9d6901 | 1.5046 | -59.9306 | 2026-02-28 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.4 |
| a890af3e-dc1b-3a2e-9dfe-2b6488a1e17d | 1.4864 | -59.9117 | 2026-02-28 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 08ca908b-a595-354d-9581-1285a68a4230 | 1.4864 | -59.9308 | 2026-02-28 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 306.4 |
| 3bed5f81-7354-36a2-aa78-709bf51bde28 | -21.7001 | -56.3109 | 2026-02-28 12:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d2086e29-8d53-3941-aece-45e317ecfa2e | 1.4681 | -59.9309 | 2026-02-28 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.1 |
| d39e6ca5-d691-3834-b9c5-cd0ace67e4e3 | 1.5047 | -59.9116 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1a1aea86-a395-3db3-a70c-3e79e94c46a1 | 1.4681 | -59.9309 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.5 |
| bada26b5-3b9e-389b-a7a2-38f881f6807c | -21.7001 | -56.3109 | 2026-02-28 13:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d367f3ae-d016-30d5-97f5-5faf74fd5301 | 1.4864 | -59.9308 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 288.9 |
| b21ed195-03e9-374f-9114-a4ddf304ff6c | 1.4864 | -59.9117 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 200.9 |
| c6d904ad-6508-3263-93ce-214ba20da954 | -21.6795 | -56.3142 | 2026-02-28 13:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7e583b64-4d17-3d57-9804-3fec5eae8813 | 1.4682 | -59.9119 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cf8bd4a0-420c-3ca2-bd84-423714e47c7c | 1.5046 | -59.9306 | 2026-02-28 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| d0d596ae-1340-32fb-aaa5-8bef561c1607 | 1.4682 | -59.9119 | 2026-02-28 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 733f7781-7acf-382d-923d-ede2c284ff0e | -21.7001 | -56.3109 | 2026-02-28 13:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 5ae122fb-27da-3c83-acad-a216a91763a9 | 1.5046 | -59.9306 | 2026-02-28 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 498e091c-afb2-3676-8859-7a753c793908 | 1.4864 | -59.9308 | 2026-02-28 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 266.6 |
| d708bc0e-6e87-3c91-bb8f-e219a64c85b9 | 1.4864 | -59.9117 | 2026-02-28 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 10849afc-6ef8-3f63-863b-782274afde87 | -21.6795 | -56.3142 | 2026-02-28 13:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e2c75a82-cc00-31b3-b346-ab8d0a4636e3 | 1.4681 | -59.9309 | 2026-02-28 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 414ab83a-339b-3818-95d9-0900b7dabb67 | 1.5046 | -59.9306 | 2026-02-28 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c8f11059-383c-3588-bd8a-d7cd00f55f7a | 1.4864 | -59.9308 | 2026-02-28 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 295.0 |
| 7ed5529e-1255-317e-bcc4-fb970122b34f | 1.4864 | -59.9117 | 2026-02-28 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 3e946494-a07b-3018-9771-995de68f1d5d | -21.7001 | -56.3109 | 2026-02-28 13:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 91.3 |


[Clique aqui para ver as próximas entradas](README8.md)
