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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56cc2bb8-543c-3dd1-ad8a-d35f13ccec0a | -10.4608 | -64.502 | 2026-08-29 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| bd233147-bd8c-3d45-b800-9d02405fd0cf | -6.7884 | -55.6635 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 63ad5b95-7e55-34a6-8c5c-b5cf9ef668e3 | -6.6317 | -43.73 | 2026-08-29 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1de25201-c356-38f2-bbee-49558d1f3fe3 | -5.9819 | -57.6892 | 2026-08-29 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 227c4bc8-1883-39f5-b352-5bab4584e5c2 | -6.77 | -55.6445 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9b308162-7957-3ecd-8991-eda1c2b1f618 | -10.4794 | -64.5012 | 2026-08-29 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 5e0d24f5-bb0b-33fa-90d4-b7bc61579110 | -11.0443 | -57.2222 | 2026-08-29 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ee870222-881d-3e8e-944b-57b591ad2d61 | -10.4981 | -64.5005 | 2026-08-29 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 133e6b30-eb67-341e-ab63-2d66593cc285 | -5.9079 | -57.7506 | 2026-08-29 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b10e1fbc-f0a1-317b-9243-83af2ce59507 | -6.7883 | -55.6834 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3a788933-8df9-3feb-b264-df2b8f4332dd | -5.8895 | -57.7513 | 2026-08-29 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 9e44f537-b30e-3216-a095-cecd654a7eb8 | -6.7698 | -55.6844 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 60fcb431-f293-3cdc-bcf4-905553f8b355 | -8.9613 | -63.279 | 2026-08-29 03:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 97a404b2-1dc4-3a28-bd40-a9006f443cf1 | -7.5137 | -55.3051 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 6fe888d7-110a-30e5-9355-782b325f56c8 | -6.7884 | -55.6635 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 9ae326a7-6a58-3db4-a9ca-ea010e81b09b | -7.4952 | -55.3062 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0c02b4ad-f513-3471-84f5-28b1837c152a | -6.7699 | -55.6644 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.2 |
| d14ce1e7-6f4e-37e1-9c04-b808d025b1b2 | -7.5139 | -55.2851 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5dddc6ca-093e-32d0-a340-34c4be12ae3e | -6.7698 | -55.6844 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5574858d-7726-3b58-81e8-f233854d190b | -10.4609 | -64.4831 | 2026-08-29 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 95f95f16-31f1-3916-a0c0-adf5e9675434 | -5.8895 | -57.7513 | 2026-08-29 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 46c9d689-f29c-3333-badd-523ea7ed44ea | -5.4179 | -43.1752 | 2026-08-29 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 75643ad4-04ff-3497-9ad4-6c96d741060a | -10.4608 | -64.502 | 2026-08-29 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8f8aef18-5c0b-3537-86e0-edd1e9fdc345 | -10.4794 | -64.5012 | 2026-08-29 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 12beedfc-61c8-35a5-8e28-bbacd489f7f5 | -5.8894 | -57.7708 | 2026-08-29 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ed26bd61-74aa-3234-b4bb-54e80f97c913 | -10.4795 | -64.4824 | 2026-08-29 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b641dd33-68a5-33f3-8348-d47a36991a90 | -8.9428 | -63.2797 | 2026-08-29 03:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b6e7584a-82f6-3fc8-8bb9-5b78a265bbd2 | -5.9079 | -57.7506 | 2026-08-29 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 4af49239-2ffd-3707-a5b5-a6a7738b06fb | -5.4177 | -43.1986 | 2026-08-29 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7ce85b9e-e8c5-309b-ad03-ef8715a31eec | -5.9819 | -57.6892 | 2026-08-29 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a9048714-3a10-39a2-8ab8-c526d4889449 | -6.77 | -55.6445 | 2026-08-29 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f65ca222-dda9-379d-8e32-bd3cfc0ab52b | -14.9216 | -41.30969 | 2026-08-29 03:10:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2d388b25-d9a4-30a8-83f0-6bc763d487e9 | -13.24492 | -41.32729 | 2026-08-29 03:10:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7c342c6-2a0e-3596-a5a6-357f64a1a4cf | -6.33192 | -35.20308 | 2026-08-29 03:10:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68b41987-7890-35e6-8a51-3468bd4d3cdc | -6.3373 | -35.20404 | 2026-08-29 03:10:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bb592430-3db2-393f-8044-d7227eb07d33 | -17.82485 | -39.6866 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e677c36-436a-3e98-9174-01ab46ec1f87 | -17.82391 | -39.69099 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 30ee1175-a17e-30b3-81a5-9f6eb5b26288 | -17.81811 | -39.68956 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bf35db40-39ee-39a0-acf9-63402de19a58 | -17.82304 | -39.68859 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c93f3fd5-fb99-3ad7-bc5f-3211e01e7360 | -17.05417 | -39.86648 | 2026-08-29 03:13:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74e4dce4-e50e-3dc6-b21e-35962f41e8c0 | -17.82208 | -39.69293 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 201f692e-7d51-33f9-b248-fc9a504d10fb | -17.82297 | -39.69533 | 2026-08-29 03:13:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d2726b09-717c-3533-bd45-440f798f7cef | -7.5137 | -55.3051 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| b2c4a009-6b07-31e5-81f0-898f41088a45 | -5.8894 | -57.7708 | 2026-08-29 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9c140a03-b6e7-32a8-8541-a991ba83fca5 | -5.9079 | -57.7506 | 2026-08-29 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a6eb3c86-9821-34d3-87a0-c749be7691b4 | -7.4952 | -55.3062 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6dde5277-7f81-388b-b158-a34196de1550 | -11.0443 | -57.2222 | 2026-08-29 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0f044adf-575e-3437-a5ca-478d73ae22b6 | -5.4179 | -43.1752 | 2026-08-29 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 1851d99f-f115-396c-ad81-43e5e205e43b | -6.7884 | -55.6635 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 4313dab7-7e4a-3a8e-8670-e2d5cf065c06 | -6.7699 | -55.6644 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 0adc7f51-6089-3ce1-9e28-745b319c156e | -6.7883 | -55.6834 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cdefa6bf-e658-3d82-b45a-d61c8373f7bc | -6.7698 | -55.6844 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 63797e0e-0e75-3452-b7e2-9bc70db18989 | -5.4177 | -43.1986 | 2026-08-29 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 5575373e-54d8-3a08-a5dd-3f5a98a81e38 | -7.5139 | -55.2851 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0ae3df08-d3e8-3c4f-a0f3-b6265cfe88a8 | 3.1095 | -60.7081 | 2026-08-29 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 412af4ef-5a7d-3c90-a2d2-10859b906fac | -5.9819 | -57.6892 | 2026-08-29 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 55cefa1b-4f41-35d3-9547-40634b7cfb7b | -5.982 | -57.6697 | 2026-08-29 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6c66fa54-234a-300c-90ac-77d6c63eccba | -10.4795 | -64.4824 | 2026-08-29 03:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| e8b2dabc-665d-322c-8a18-87287e47224e | -6.77 | -55.6445 | 2026-08-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e98bc65b-94f4-38af-9391-dcf72c3eb153 | -10.4794 | -64.5012 | 2026-08-29 03:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 983ff158-3446-3611-86f2-685b1722c41e | -5.8895 | -57.7513 | 2026-08-29 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| e205086b-e027-3f50-b6eb-b54514534112 | -6.7699 | -55.6644 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 8433b694-0453-3805-8f48-704727f104f3 | -7.5137 | -55.3051 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 294e5f7d-2eb3-3cdb-a87d-c418115a133c | -10.4794 | -64.5012 | 2026-08-29 03:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 53022c3f-024d-3bbf-83dd-c364973fd12b | -6.7885 | -55.6436 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 174e963c-c62e-3553-a263-08ebee672f5d | -7.5139 | -55.2851 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 45a02c52-5dbb-349e-9eb5-d95b2bd1afe1 | -5.8895 | -57.7513 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| f8515587-bf1a-3a56-a81c-ed74f5ca92bc | -6.7698 | -55.6844 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 50bfe1df-1252-3cbc-8db3-389de9cc722c | -10.4795 | -64.4824 | 2026-08-29 03:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 61e57f6c-63c2-3d84-9bc3-5e406c505e72 | -5.9079 | -57.7506 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a0fa7daa-084f-3456-a23d-77f77346551a | -6.0004 | -57.6884 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7050ce16-1939-3d31-bf48-79eb65d76401 | -5.982 | -57.6697 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fff679aa-fa10-3cf2-be44-18a03754e77f | -5.9819 | -57.6892 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0ad60c70-97ef-31f9-9e4a-be742542c1e9 | -6.7884 | -55.6635 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 257.2 |
| a41b7445-7f59-362e-a526-cb9e64880a8d | -5.8894 | -57.7708 | 2026-08-29 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0cee7dae-f263-379d-9cd3-ed25008f021f | -6.7883 | -55.6834 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d96d8625-9a55-3f4e-9ce8-035cc38ca0ce | 3.1095 | -60.7081 | 2026-08-29 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 1dd30591-2c0d-3c08-ad4b-c209b680ff44 | -6.77 | -55.6445 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9d1c0ac1-c20c-3819-9bb8-37e045e7ba58 | -7.4952 | -55.3062 | 2026-08-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c67566db-cbe0-320c-9aab-d180feea132a | -5.8895 | -57.7513 | 2026-08-29 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 07ef538a-19ec-350b-a2be-c28e7e1cfd0e | 3.1095 | -60.7081 | 2026-08-29 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| de8f022a-4cf9-3d3a-97a2-dd85f0f25aec | -5.8894 | -57.7708 | 2026-08-29 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1699cbe9-1474-3059-a27a-2e1dddcc322b | -7.4952 | -55.3062 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5708e1e4-1da2-34a8-890b-ce0a7827d5d9 | -10.4794 | -64.5012 | 2026-08-29 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 055f1c20-0a49-322d-9e3c-d3850423cf5c | -6.7884 | -55.6635 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 6e668d49-1b5e-3014-8182-8ba3b58b8af6 | -6.7885 | -55.6436 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 484fde01-9e8b-3bc5-a679-dd0f9b7cc75d | -6.7699 | -55.6644 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 33c20db9-6900-380a-8f4b-48f04b8338d7 | -5.9819 | -57.6892 | 2026-08-29 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9dc522e8-655c-320b-8cee-698259ed5408 | -6.7883 | -55.6834 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 15e435d5-26fa-3ff3-9ba4-700d5929da85 | -11.0443 | -57.2222 | 2026-08-29 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0bfb55ed-7c13-33eb-b69c-c579678c034c | -6.77 | -55.6445 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2a1b4679-3878-3a3f-b102-ff99572d51f6 | -6.7698 | -55.6844 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 456c1c95-409b-3088-8eea-95c29bcf4161 | -7.5137 | -55.3051 | 2026-08-29 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| ed99a246-9859-315f-871c-8353188fffa8 | -5.4177 | -43.1986 | 2026-08-29 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 37d884e0-0d90-3dd5-b69e-7b59b25543eb | -5.4179 | -43.1752 | 2026-08-29 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a9758f38-6862-3a44-8790-bdd461e51cbd | -10.4795 | -64.4824 | 2026-08-29 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 42804f22-0611-37e1-ba40-50aa4e1289a8 | -6.7698 | -55.6844 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a24cfbe3-bbf0-3bb2-b529-57a0837bf90e | -6.77 | -55.6445 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6b54a27d-5739-3953-b228-72bf93e5fbb8 | -6.7699 | -55.6644 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 09a432b5-c0c1-3085-9a63-c56b520ad8fd | -5.9819 | -57.6892 | 2026-08-29 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README21.md)
