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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a71a73-1141-3fee-bf10-69a94ee568b9 | -10.4794 | -64.5012 | 2026-08-29 07:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 405ef5f2-0131-32c9-8b9b-c5bee2c05f71 | -6.7884 | -55.6635 | 2026-08-29 07:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 8e26a90c-434e-3b24-b4f0-dda479e4d5a4 | -6.7884 | -55.6635 | 2026-08-29 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 0c8213e5-2a1f-3cc3-8855-0d53b395d2c3 | -6.6315 | -43.7533 | 2026-08-29 07:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 789469dc-6eb2-34cb-bcc9-ea67c42e39a2 | -10.4795 | -64.4824 | 2026-08-29 07:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 213f9f08-e9b2-3fad-8b88-dca6a7b06949 | -5.8895 | -57.7513 | 2026-08-29 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b02953cc-4e80-34cc-9ba4-cc18d297ab34 | -6.6317 | -43.73 | 2026-08-29 07:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 6efc64d1-8633-37d4-af61-3145ed1ba197 | -10.4794 | -64.5012 | 2026-08-29 07:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d5bb5bc9-1f96-3ed3-a40b-ed728c34e11a | -6.7885 | -55.6436 | 2026-08-29 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 766f5450-f0aa-3e03-927e-aec8fe71df9b | -6.7699 | -55.6644 | 2026-08-29 07:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e72af560-d37b-30b9-9780-59e7ea4b651e | -10.4794 | -64.5012 | 2026-08-29 07:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 744f0452-fb27-34c6-96e2-7c7594501773 | -6.7699 | -55.6644 | 2026-08-29 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 62d7e0e9-6082-30b0-b8a0-69f7961a2fd9 | -6.7884 | -55.6635 | 2026-08-29 07:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 3d4a9ad2-9ebe-30a3-bda9-af6d4b3deb33 | -5.8895 | -57.7513 | 2026-08-29 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d7e90372-4da6-30ba-9b94-c4fbea69824e | -6.6315 | -43.7533 | 2026-08-29 07:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b24eaf4a-ebb6-373a-8ac7-276eb3c00af6 | -6.6317 | -43.73 | 2026-08-29 07:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| eaf713a6-376d-3a2a-9cb1-51b8bd91810a | -5.8894 | -57.7708 | 2026-08-29 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5cdc5724-198c-3378-8249-2c77318f7f87 | -10.4794 | -64.5012 | 2026-08-29 08:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 655f9b00-9d33-32ee-bfd7-20b82b899b4c | -5.8895 | -57.7513 | 2026-08-29 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| eb904ce1-9e3a-3720-8679-57b7b2a4d438 | -6.7884 | -55.6635 | 2026-08-29 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| d768b160-fe01-3b28-b26a-6fa13068d906 | -6.6317 | -43.73 | 2026-08-29 08:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| f6f9c7fe-d41b-37eb-b164-f55ecde695ea | -6.6315 | -43.7533 | 2026-08-29 08:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 58422e62-715e-3f00-80f2-9812396b6191 | -6.7699 | -55.6644 | 2026-08-29 08:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a9922c10-0aa9-3b4b-a4e9-620bff66043d | -6.7699 | -55.6644 | 2026-08-29 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4858f2a7-4684-3ac9-a087-2d42e188e6f6 | -5.8895 | -57.7513 | 2026-08-29 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e1e3c1d8-3ef3-35a2-abe3-152fa97b1cb2 | -6.6317 | -43.73 | 2026-08-29 08:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 147abbbb-c03c-3bd8-a130-91663bd81395 | -6.6315 | -43.7533 | 2026-08-29 08:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b7d70fa3-f875-3b24-88ff-b6ebc898b46a | -10.4794 | -64.5012 | 2026-08-29 08:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5a59ab74-d030-33dc-8788-f904b9dd5084 | -6.7884 | -55.6635 | 2026-08-29 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 270201b5-24d9-355e-a2b4-5e4fe1931eae | -12.2666 | -50.5317 | 2026-08-29 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a14cdb29-5889-393f-9e66-7272f8a8c997 | -6.7884 | -55.6635 | 2026-08-29 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| af49b565-3eae-384a-81b9-b6d10cbcb1dc | -10.4794 | -64.5012 | 2026-08-29 08:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 965badaf-5f3b-3392-a29b-19c57159f534 | -6.6315 | -43.7533 | 2026-08-29 08:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ff80760d-0e1c-370b-8a09-c00583c0823c | -6.6317 | -43.73 | 2026-08-29 08:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 655123f0-bf87-3ca9-b0d4-4da8056901a7 | -12.1902 | -50.5409 | 2026-08-29 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8b429ac5-2896-3bbc-b708-b4d2aadada68 | -5.8895 | -57.7513 | 2026-08-29 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 95adbc39-8081-3e82-a3b3-52ab13e2157e | -12.2284 | -50.5363 | 2026-08-29 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 75783771-d4b2-3848-888e-32e5caf98011 | -6.7699 | -55.6644 | 2026-08-29 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ca7357fe-a25d-3c8a-8cfe-69e784df3877 | -6.7884 | -55.6635 | 2026-08-29 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 953269b8-98a5-3196-a3a6-0e7aef83dfd9 | -12.2093 | -50.5386 | 2026-08-29 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 60055dd1-8de7-351c-a022-35238c138acc | -10.4794 | -64.5012 | 2026-08-29 08:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0c63cbda-f3bf-3f37-a96e-ad7f214414fa | -5.8895 | -57.7513 | 2026-08-29 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f433b276-a00f-3457-bfca-2e00c2df2406 | -6.7699 | -55.6644 | 2026-08-29 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ef442c92-ad7f-3950-9694-ef865ad084d6 | -10.4795 | -64.4824 | 2026-08-29 08:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4dc7f5f2-17f3-3a55-815f-25f54c92aee5 | -10.4794 | -64.5012 | 2026-08-29 08:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 110.3 |
| f867a3bf-be49-317b-88af-60bd89e79296 | -12.2093 | -50.5386 | 2026-08-29 08:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f760442b-3ba0-37f8-baa5-7e12dfa47ce5 | -6.7699 | -55.6644 | 2026-08-29 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5fc35eea-5bfe-34c6-8257-283270fd6dae | -6.7884 | -55.6635 | 2026-08-29 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 351c2c61-5a33-38b4-a3c0-52433a6b5405 | -12.1902 | -50.5409 | 2026-08-29 08:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 6b5ae97c-d063-3832-8841-77648e3c122c | -10.4794 | -64.5012 | 2026-08-29 08:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 28b06051-0a02-3fe7-8f0d-924c8757195f | -10.4795 | -64.4824 | 2026-08-29 08:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ba4cad40-ce01-3ba6-a10b-8019112bc48c | -5.8895 | -57.7513 | 2026-08-29 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 37abc498-3513-355b-9064-dd077ce82526 | -6.7884 | -55.6635 | 2026-08-29 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6628c4c8-e53f-3784-96a1-3e80280480b7 | -6.7699 | -55.6644 | 2026-08-29 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 78fbfc37-8b0b-3110-987b-e56caee54ffc | -5.8895 | -57.7513 | 2026-08-29 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ae3beb47-e0b5-3210-b970-17166cc26686 | -6.7884 | -55.6635 | 2026-08-29 09:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 44f98d4f-9d4a-3470-8fa2-aa2b83f5ddd5 | -6.7699 | -55.6644 | 2026-08-29 09:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e8a3ffea-a40f-396a-8aca-0880f6ca5b19 | -10.4794 | -64.5012 | 2026-08-29 09:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 41855353-58c7-3fae-b052-1b2468a08abf | -10.4795 | -64.4824 | 2026-08-29 09:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fbd40fe1-904c-3f15-805f-de31f98ddf77 | -5.8895 | -57.7513 | 2026-08-29 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| d4beb786-8a9d-307f-bde7-ebc6f5fcba1f | -10.4794 | -64.5012 | 2026-08-29 09:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b18e39f1-6801-34ae-8985-e35ede8040bb | -10.4795 | -64.4824 | 2026-08-29 09:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 69046bf2-9e57-3a2d-aac4-db5b5ad06be9 | -10.4981 | -64.5005 | 2026-08-29 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f0ca78d0-d02d-33f2-9512-b2cfd121437e | -10.4795 | -64.4824 | 2026-08-29 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e2354802-b664-3b6f-ba8b-994a34636cd3 | -10.4794 | -64.5012 | 2026-08-29 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 937dd640-ef62-322b-b8ac-0ce390167596 | -10.4981 | -64.5005 | 2026-08-29 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6007e006-219a-31b7-9d85-443303d3aa28 | -10.4794 | -64.5012 | 2026-08-29 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 111.3 |
| d5085c2c-e0ef-3433-9401-6520d181c295 | -10.4795 | -64.4824 | 2026-08-29 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c9c39f10-8835-3937-815c-fda8e0a4b653 | -10.4794 | -64.5012 | 2026-08-29 09:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b2237135-793d-3a85-aaba-924830400ea9 | -12.2093 | -50.5386 | 2026-08-29 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 7444bd0f-c32d-3c92-8507-27283f7a0ba8 | -12.1902 | -50.5409 | 2026-08-29 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 59e48523-d017-342f-80a1-585575971277 | -2.5035 | -48.3521 | 2026-08-29 10:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 257.8 |
| de5e0f60-078a-3b52-a482-b21ce18e6575 | -12.1902 | -50.5409 | 2026-08-29 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3cddf6aa-7942-3b58-8480-9c1f3b82c170 | -6.7884 | -55.6635 | 2026-08-29 10:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ad58b9c8-f4bb-3a39-9bc3-d60933c928e8 | -12.2093 | -50.5386 | 2026-08-29 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| fe7972a2-6a4a-30e7-8d79-0dd4dfbe90c7 | -2.5035 | -48.3306 | 2026-08-29 10:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 60e75456-43cc-3fef-8315-f93d539aed00 | -18.62252 | -40.26067 | 2026-08-29 10:58:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| b8bfb3e0-caa2-3f2b-91fa-b3dbfa3f3496 | -6.7884 | -55.6635 | 2026-08-29 11:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 30ad0990-2584-3507-b177-7dd0b40c63e3 | -6.7884 | -55.6635 | 2026-08-29 11:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3f884283-9aaa-3176-a10f-25ac7557b065 | -6.7884 | -55.6635 | 2026-08-29 11:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a446e097-96ef-336b-8014-83c3bf6a9eae | -6.6317 | -43.73 | 2026-08-29 11:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c2fb305f-a2d6-3855-b96b-5d10b3e8e74d | -6.7884 | -55.6635 | 2026-08-29 11:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4cbefdff-c289-3dab-9a63-17e2abfa3b1b | -13.5991 | -45.772 | 2026-08-29 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b728585e-28ef-3654-85c6-7e69892d2862 | -6.6317 | -43.73 | 2026-08-29 11:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ecab0843-b466-30c4-87dd-d8dd1c0eec67 | -6.7884 | -55.6635 | 2026-08-29 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 785ac238-b40e-37b1-b61f-59efb49e01c8 | -6.6315 | -43.7533 | 2026-08-29 11:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| daeec7fe-1905-36d8-8e6e-43e2c6b8a10d | -13.5991 | -45.772 | 2026-08-29 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| adb461a6-0505-362d-9a43-2094e9ec9745 | -6.7884 | -55.6635 | 2026-08-29 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 941ca0ed-4b45-3d97-8f1c-1f9987de10cd | -6.7699 | -55.6644 | 2026-08-29 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 14aa25b0-a296-3dee-a7fc-3378ef77a33d | -5.9819 | -57.6892 | 2026-08-29 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| dbb74aeb-068a-3311-8216-67c05bf852aa | -6.6129 | -43.7317 | 2026-08-29 11:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5157c432-27a0-3454-9e07-861a0efcf952 | -6.6317 | -43.73 | 2026-08-29 11:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 840f8423-4001-3c48-a32c-721b6933221b | -8.6691 | -49.5584 | 2026-08-29 12:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7605050c-b050-349b-9f3c-d1f21e48a364 | -8.6694 | -49.5369 | 2026-08-29 12:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e245cf00-9bab-30e1-9aea-564768e6e4f9 | -6.7699 | -55.6644 | 2026-08-29 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 006a54ee-70a9-3fb9-9ec9-8492a773de53 | -6.7885 | -55.6436 | 2026-08-29 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5167c9c7-5d92-37ab-94ad-a426f6a2914a | -13.5991 | -45.772 | 2026-08-29 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 354ca10b-ba61-321e-97d7-59f407a18b31 | -5.9819 | -57.6892 | 2026-08-29 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| cdda4ead-ba8a-3331-862d-2c39e72a2f35 | -6.6129 | -43.7317 | 2026-08-29 12:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 82af5eb3-a9a1-3cc3-a446-f9b064309522 | -6.6315 | -43.7533 | 2026-08-29 12:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |


[Clique aqui para ver as próximas entradas](README75.md)
