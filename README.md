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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b089dc0-b306-3c36-8255-7c0de57d1ec0 | 2.5617 | -60.7544 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 661d8a18-1fdb-30b0-9be1-1c24aec5769b | 2.5434 | -60.7357 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 432.7 |
| 11f350db-e7b7-3285-b970-88de8bbd9d3c | 2.5617 | -60.7354 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 394.5 |
| 34f58e68-2a3e-3a1a-99de-c4eb1f089a4d | 2.562 | -60.5648 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d78f8540-7248-3729-ba2d-88deefbd274a | 1.3765 | -60.3119 | 2026-02-21 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 505082a6-52a9-3f51-84c8-c2b169fa5a08 | 2.5435 | -60.7167 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 147.5 |
| b6a1cef9-cf7e-37a5-a458-7533694061ee | 2.5617 | -60.7165 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 529298a2-e8d3-34a2-b64b-7aef520424fb | 1.9419 | -60.3637 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c5e29983-ace7-34b1-88e3-72347b036680 | 2.7088 | -60.2208 | 2026-02-21 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 389355b9-f923-3549-a194-abce0c12b752 | 2.6905 | -60.2401 | 2026-02-21 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 114.0 |
| feee3df9-ec50-3587-a7ca-9d0806591582 | 2.5434 | -60.7546 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2ee2ab24-7663-3f58-897e-2f0b9dc16a3f | 2.7088 | -60.2398 | 2026-02-21 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 90941a07-c415-3ca2-8467-fbc6db3da1a1 | 1.9419 | -60.3827 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7328a0c7-457d-3df9-8681-4d8d29078075 | 2.5438 | -60.5651 | 2026-02-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a948c158-cacb-3c89-a72c-33e2040ebddb | 2.6905 | -60.2211 | 2026-02-21 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 89e57b44-49eb-312a-91bb-8019d2986e0b | 2.5617 | -60.7544 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 01ba9d2c-243d-3b0c-a3d4-213df1762bae | 2.6905 | -60.2401 | 2026-02-21 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a492a087-f32e-3a86-bf0d-3901c1549dc1 | 2.5435 | -60.7167 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 9217b008-ddcc-370a-917d-1640ad6af8e6 | 1.9419 | -60.3637 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 137df6ff-d0fc-3e1f-8f39-37286d895a87 | 2.562 | -60.5648 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2b4671e0-12e6-3e9a-86ed-4ca3fc21aa5c | 2.7088 | -60.2398 | 2026-02-21 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 2755c838-5782-3319-a68e-f57ebe3e2423 | 2.5617 | -60.7165 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 5749d966-9801-3641-9ad5-af0d39d3ae03 | 2.5434 | -60.7546 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 668c1063-09c0-35a2-9de0-c4e1b77e377a | 2.7088 | -60.2208 | 2026-02-21 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f54524cf-d3cd-34a1-ae88-d1f6ee8d6028 | 2.6905 | -60.2211 | 2026-02-21 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5dd7713b-115c-38bb-87dd-b762401f1da9 | 2.5617 | -60.7354 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 491.0 |
| 9735189e-b9b0-37e3-90e3-ca77c14ad1b5 | 2.5434 | -60.7357 | 2026-02-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 420.7 |
| 4c77075e-f290-3012-a48f-6bcbb80afb7a | 2.6905 | -60.2591 | 2026-02-21 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.6 |
| cea56c13-8e2f-3296-818d-831c6fcbe1f9 | 1.9419 | -60.3637 | 2026-02-21 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 997e9eb9-e7f4-3808-9878-3433de316de7 | 2.6905 | -60.2211 | 2026-02-21 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ec11f211-ba5c-3214-b16f-e8824d0416b9 | 2.7088 | -60.2208 | 2026-02-21 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 47ccb8b6-36e0-3c72-8cf4-85ec3fcc26e1 | 2.7088 | -60.2398 | 2026-02-21 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 0f0cd7d5-b36c-3007-81e6-c659f0d8ca6f | 2.6905 | -60.2401 | 2026-02-21 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 931584c3-1529-3aba-957d-b54c220b6d38 | 2.5438 | -60.5651 | 2026-02-21 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2e2f11c7-609c-3b3e-9493-a82b64ed4d16 | 2.562 | -60.5648 | 2026-02-21 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 23cc430b-b67b-3701-904b-9c4a172e8f1d | 2.5617 | -60.7354 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 304.7 |
| 06cf4377-1b95-39f7-b79a-edc761b2bb57 | 2.6905 | -60.2401 | 2026-02-21 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b8f279c4-df47-3a26-bda1-4962a05d6a27 | 2.5435 | -60.7167 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 122.9 |
| b2f6d0a1-4265-3feb-aee2-bd479756b44a | -6.5631 | -51.1126 | 2026-02-21 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c4175c4b-6fa9-3219-9e44-516d614c2134 | 2.5434 | -60.7546 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2dea721b-c514-3002-8ded-8e2287623274 | 2.7088 | -60.2398 | 2026-02-21 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 721aedd1-bbe0-301c-991c-9c0cbd86d723 | 2.5617 | -60.7165 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 133.8 |
| f9ab1b46-adba-391a-a81c-6313c8549c63 | 2.5617 | -60.7544 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f9ef9b07-5590-3720-8174-6a676f0a82a8 | 2.562 | -60.5648 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9cb9bca7-b335-318d-92f1-62d930433d1e | 2.5434 | -60.7357 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 282.6 |
| 64f7867e-d185-39ba-930f-8cd4d41c5186 | 2.6905 | -60.2211 | 2026-02-21 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 99283fe6-99ee-3449-a4d3-666da868bd93 | 2.7088 | -60.2208 | 2026-02-21 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c4c98284-b631-3188-b12f-2e11e244d7f3 | 1.9419 | -60.3637 | 2026-02-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 64f2478a-036e-39e6-b7e8-854a766b3377 | 2.6905 | -60.2401 | 2026-02-21 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 112ff9d1-80e4-3d8c-8f72-1a8b15a79749 | 2.5617 | -60.7544 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 05be5def-4945-3bdc-8a83-6dad13dd6e08 | 2.5438 | -60.5651 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 937a45c4-22de-36cf-af6f-c630392d3e93 | 2.7088 | -60.2398 | 2026-02-21 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 0bcc7845-430b-3eda-8721-914a6ff0d911 | 2.562 | -60.5648 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e0d93211-e835-3fa4-9a46-06f1c0a206ff | 2.6905 | -60.2211 | 2026-02-21 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cd527eb8-7f38-3541-a63c-d8021c372216 | 2.5617 | -60.7354 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 339.0 |
| e246ddef-207b-30d4-b202-28eb648258e5 | 2.5435 | -60.7167 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 120.2 |
| a8e82f70-9bf0-308f-85df-539eeb9b4553 | 1.9419 | -60.3637 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dfd877da-b03e-33ce-aa65-699e713c8f63 | 2.5434 | -60.7546 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 622732bd-5bcc-3134-902b-f51a1f68abe8 | 2.7088 | -60.2208 | 2026-02-21 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 5b08cff1-6d13-3437-a4e7-7a4fe70f907b | 2.5434 | -60.7357 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 409.2 |
| 29416212-ab34-3193-8c5b-14fa7de11f79 | 2.5617 | -60.7165 | 2026-02-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 57b91525-79f1-3435-8cf5-8fcc2c818013 | 2.5438 | -60.5651 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d3dd245c-7319-34ac-9ff4-8af83c453946 | 2.5617 | -60.7354 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 252.5 |
| 3cc73ba9-da2c-3cb2-b337-5a50c5a8a37d | 2.7088 | -60.2208 | 2026-02-21 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 8610f277-1640-35dc-b543-e405e7e40b3e | 2.562 | -60.5648 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 38e7c7da-9683-3683-8537-3f7b509cacc4 | 2.5617 | -60.7165 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 60dcee7f-a957-3c5e-9b6e-79ac5d2a8fc5 | 2.6905 | -60.2211 | 2026-02-21 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a489160d-82e9-31d1-844a-e4f715b0bad8 | 2.5617 | -60.7544 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 05868887-2359-39ba-bb18-4099cd199c8d | 2.6905 | -60.2401 | 2026-02-21 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 125.7 |
| be731b53-8d14-3023-8a4c-c73b51b9301e | 2.5435 | -60.7167 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 7a5a9a17-cc7f-3e81-af1a-82c2e3e7fa26 | 2.5434 | -60.7357 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 413.5 |
| 53805a52-9c8b-384e-91b6-43784ab92bb2 | 2.5434 | -60.7546 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f739b74c-3d4f-3d98-9a50-cb345d8b59ad | 2.7088 | -60.2398 | 2026-02-21 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 2683e63b-4d2e-3a18-a37d-a70c0296b4e7 | 1.9419 | -60.3637 | 2026-02-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| eb621c25-9fa4-36ba-9451-6adba67cf41d | -11.8431 | -58.046902 | 2026-02-21 00:50:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee816f9f-5780-3bec-8583-cd57cb3a0617 | -20.5317 | -49.882099 | 2026-02-21 00:50:00 | METOP-B | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca4012c-02ad-39c4-923f-a2f3022d7268 | -20.5284 | -49.869301 | 2026-02-21 00:50:00 | METOP-B | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4064f34b-7e71-3355-bb7c-6dc77945cd81 | -11.9579 | -58.7453 | 2026-02-21 00:50:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfb019e-f5fd-30a4-84a9-9d8be6ac09a0 | -11.9564 | -58.7383 | 2026-02-21 00:50:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9ec9cb0-9b3e-32e6-bf7b-22e41fec73b8 | 2.5435 | -60.7167 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 87943f8f-119e-3687-95e2-2ee618436776 | 2.6905 | -60.2211 | 2026-02-21 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a00850fa-e950-3949-b71d-184dcc50f62e | 2.5617 | -60.7354 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 13141008-21be-3256-8d24-9997a0c6f2b6 | 2.6905 | -60.2401 | 2026-02-21 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 446efdea-3fa4-3d38-905c-ec35837a98f6 | 2.7088 | -60.2398 | 2026-02-21 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 971b6642-298b-3ebb-b857-68dca886afa5 | 2.5434 | -60.7357 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 150.2 |
| f5c4b830-3a9a-3e4d-8116-ab0687c05d79 | 2.5438 | -60.5651 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d2ae65c0-4cb5-3b21-81d7-4f7ab8cfdacb | 2.5434 | -60.7546 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d4024713-897b-321d-821f-0880cc682de0 | 2.562 | -60.5648 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| af3129af-7926-3dc2-9bcc-58f9d1231b75 | 2.5617 | -60.7165 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3c95fbb8-115c-3ec4-8225-e9c893445027 | 2.7088 | -60.2208 | 2026-02-21 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 38d6d9b1-7f8e-376e-9310-98eed95c340f | 2.5617 | -60.7544 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| afb96fb9-e0e3-3515-9b77-ce934b003cda | 1.9419 | -60.3637 | 2026-02-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2ff742d0-bb4c-3f86-8ea6-7c3f6a13a04a | 2.6905 | -60.2591 | 2026-02-21 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 239666c9-4603-3a82-8a01-27960cb9cfbb | 2.5617 | -60.7354 | 2026-02-21 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 06ca1408-3e61-3981-bedb-106eb47bac1f | 2.6905 | -60.2401 | 2026-02-21 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| d7e22c33-206c-3019-99e4-65e8ff49be5e | 2.7088 | -60.2398 | 2026-02-21 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 256.3 |
| 3fd49b50-37a8-3935-868b-278ab66eb782 | 2.5434 | -60.7546 | 2026-02-21 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9d2d2b41-f0cf-3add-897b-711a75220d0b | 2.7088 | -60.2208 | 2026-02-21 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 131.5 |
| d2e3e3bf-0928-3dab-a404-ebd85122d186 | 2.7087 | -60.2588 | 2026-02-21 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 16432a3d-ff0e-3d86-a41d-b54b1b925bf0 | 2.562 | -60.5648 | 2026-02-21 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |


[Clique aqui para ver as próximas entradas](README2.md)
