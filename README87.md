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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abafd559-82ef-3637-ab45-85e4ea315aa4 | -2.86274 | -60.24682 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0cfcde8-3afa-3382-8220-e6af005eb70a | -3.3459 | -57.86576 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67ca2fa2-e65f-3da3-991f-19a44a5cf283 | -3.35866 | -59.86014 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96876daf-67ac-3367-ba64-5293cc456649 | -8.46824 | -57.62607 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d76b914-aff4-39ea-8c8b-c6036e97117d | -2.88163 | -57.80845 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 967786d3-8bcb-382e-aed2-1947653daee7 | -7.30182 | -59.91335 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b71966f1-d8f6-31fd-b0cc-d4c76c023599 | -3.45232 | -57.95059 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c06b52d-5948-3703-9329-dc9e00ef28ad | -8.24142 | -61.37637 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acbaba66-c2d1-3527-b5ec-5f2c9dbb982a | -8.60664 | -54.6099 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb1a9e3-9357-3b49-9c63-0c38270655bb | -6.29477 | -59.96175 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83752e08-1e01-3b1d-abba-e5952b33beac | -2.97512 | -54.7687 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44f7cef4-af97-3d42-9f1b-fc45fb0f4954 | -7.56094 | -61.33183 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e593c8-177c-317a-9826-d9520edefb73 | -7.77125 | -49.19405 | 2026-09-20 05:23:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df6b2004-e1cd-3b9b-8fd4-dd9ff0d01969 | -6.29072 | -59.92181 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4605a33-a015-346d-b33c-450f008afd5c | -1.71752 | -55.14801 | 2026-09-20 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f1f084d-1074-3460-964e-4482e80ff5e2 | -3.73995 | -51.8176 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d5d1badf-3874-39a1-8729-04b52365bf16 | -3.03093 | -59.1661 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250edb76-57be-3450-8687-10fb12725702 | -7.56808 | -57.66944 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8989b615-e675-3175-964f-fb0f5ced1afa | -3.34938 | -59.87629 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d1bd7c9-3fd8-3d35-a708-25315de44a1e | -3.40352 | -50.39911 | 2026-09-20 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd28a13a-3c29-349d-a30a-8639562c53e8 | -1.91294 | -58.26184 | 2026-09-20 05:23:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 368fd31e-941a-379f-8753-b49675c68694 | -7.59867 | -55.70839 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86019858-190c-392e-9cfe-9e30fe4ee678 | -2.88333 | -57.82024 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e20fc25a-9c3e-381f-975e-885aa6a76e3d | -3.04917 | -61.26781 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae61ab26-105b-3002-8527-022250946f20 | -1.37207 | -57.97305 | 2026-09-20 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c899ac-e771-3a24-9546-cd2124ea9300 | -8.17243 | -54.73124 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b099255a-8a4c-398c-9034-af8703240e60 | -3.33957 | -57.86093 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e3aff9-9fbd-35b2-8339-500b8c9eaf5b | -8.75889 | -48.65869 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 90ab5852-b665-3b9c-adfc-00f69e3a0605 | -3.44499 | -58.22671 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4417c119-037d-300b-986e-f5b5858e308f | -8.18201 | -54.75914 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7d34a9a-753e-3284-a11b-a5b1a35769ba | -2.1727 | -48.32052 | 2026-09-20 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a2b91d7-ec21-3835-9249-4e316826b426 | -7.3209 | -55.61733 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5b40c5-d39e-32c6-8bc2-dac1c6df1bff | -6.64913 | -62.8807 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9dd3bb0-9513-3a04-bcc9-ee7b0ea8dad7 | -8.61173 | -54.60604 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5656d990-49c4-3f1d-814f-d5894d6d5af7 | -3.48072 | -56.8758 | 2026-09-20 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53d2c245-7280-38bf-8d9a-3f82bca410e3 | -3.40901 | -50.40014 | 2026-09-20 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c31cff10-7370-37ca-874d-7d731695576b | -7.64453 | -57.60994 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a7a7192-05f3-376d-9335-085afba10a5f | -9.69432 | -48.31438 | 2026-09-20 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f080375-8438-3ebb-9a73-440f33be07ef | -7.49205 | -55.61007 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec17a35-8b2f-3511-9a3a-9c824662df43 | -8.42515 | -54.72406 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0278b10-1406-3a61-9a09-462ba95aca06 | -6.45477 | -59.98278 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c27782-25fd-3fab-81ef-6c2d7bc403ce | -3.39929 | -54.07324 | 2026-09-20 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef48dee-7dfc-34e0-aa52-8b61c25d9852 | -6.2935 | -59.92583 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e497b268-06ef-325b-8d44-56c0869ac8ee | -2.53473 | -57.55206 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4d54123-7131-31c5-8cfb-41a1c282f7af | -9.70497 | -58.14825 | 2026-09-20 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e5d401c-cf8d-3d6c-b910-e498bdeebb50 | -3.40299 | -50.40274 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 420c08f4-bca1-386b-be40-d94323c45db5 | -3.36081 | -50.45937 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a1a00ee-737c-34f8-bfa1-9be4c753091d | -2.8101 | -57.65931 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47babe26-5e04-35fb-ab37-cd844231a1e0 | -10.84349 | -50.93869 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cffa1945-27bf-3097-a3e1-e5524477e33b | -3.449 | -50.59495 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cce1b43b-f825-3bb3-a5b7-c0ac9029b2c7 | -2.79196 | -59.89062 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42484417-db15-36a4-8c52-dffdd83841a4 | -9.04242 | -48.71231 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ef63686-f2e3-3b35-aae2-64c0516d7998 | -3.15803 | -58.63115 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 655ca4a0-7207-3d0f-bea6-3da342fd5693 | -6.15283 | -62.62254 | 2026-09-20 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecb4f455-5205-3ef3-970c-43be04e033b9 | -2.91072 | -54.18765 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4013ba3d-31af-3201-a679-d736bae76653 | -2.9058 | -57.78909 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8013d96e-42dc-324a-8bb3-54360d11a6af | -8.17683 | -54.73191 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 333caa45-8c1a-3764-ad1c-5de349e1a51a | -2.75073 | -59.39177 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bfde0f6-78ec-336b-8236-ea0fa8b40188 | -3.45691 | -58.21725 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 603aba4c-07f0-3678-9979-0b84c7ebcb45 | -3.25253 | -60.885 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f5370ed-335a-32be-85fa-bffb0092ff1d | -2.81689 | -54.71281 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09de08b7-5041-3488-a22d-172435e2c407 | -6.13741 | -59.87982 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41c8bdd2-985a-3894-a1dc-a8085b4a3b13 | -10.60312 | -50.2477 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 465efd78-a579-3d2a-bf0a-9c3cc7ee79a2 | -9.58129 | -55.10226 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d4dda68-6b54-34c5-8b1c-eeedecb88757 | -8.23214 | -62.84595 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 065a0dbf-a9c3-3431-9d3c-a25a72b52b1a | -3.13361 | -52.71932 | 2026-09-20 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b82d13d4-45e9-3811-87c8-cafde29ce068 | -2.5529 | -56.02693 | 2026-09-20 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe227d0-7aa3-36f8-9f62-417d22bc85b5 | -8.16822 | -54.76148 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5b9c4b5-22d6-3d5a-8b35-0fae87e87dc0 | -3.34532 | -57.86952 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 689a70de-5bbb-34d3-88a1-7cff3cbfcf21 | -6.49373 | -58.38238 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f771d95-e10c-3bb9-9b5f-306fb6a1b81e | -2.45778 | -49.21562 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df3af5e2-7d99-3c5c-990e-d10697226b36 | -8.16382 | -54.76085 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68ecc59f-b9ef-3006-b868-db5432d678c9 | -9.0484 | -48.71861 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c652f142-6665-3214-a3f9-976645e68418 | -9.59171 | -60.51823 | 2026-09-20 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41a43830-0b89-320f-895c-be592d913220 | -8.76961 | -61.39331 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a53268c-e7c4-318c-a5eb-97653bc3519c | -3.44683 | -50.6001 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df927cae-7771-36ea-b458-69ad659ee482 | -8.73403 | -52.36561 | 2026-09-20 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffcc2b70-43bc-3620-add8-789f2fbbd984 | -3.14373 | -61.40261 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e715f4e4-85f4-3ff7-9afd-2d35cac993e7 | -2.58604 | -59.99231 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c55e3079-5aa2-34dd-a3af-1e8d5ae48d56 | -8.22976 | -50.656 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13f821ca-8a3a-3437-af64-6977dd355e66 | -4.07434 | -52.12014 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca094293-c173-3557-87bb-10d23a0dddad | -10.59438 | -51.90593 | 2026-09-20 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad1d3d3-3110-34bd-be8a-ee53ba5b312e | -3.36089 | -59.86752 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca19845-1dbd-333e-ac58-7fd545ea790f | -10.72149 | -50.2447 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 584f6f50-8c0f-3e8f-8060-71d8434f9040 | -3.35036 | -59.84831 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e020318b-88f8-373f-b513-0465bf2901b6 | -7.41059 | -49.83903 | 2026-09-20 05:23:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52e543b2-00d7-37cf-8c38-3c2910457188 | -6.91993 | -63.07446 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 213748e1-08ea-3312-819e-e90e04fd78cf | -3.75708 | -55.95454 | 2026-09-20 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed548321-6daf-3217-b508-4a56ca7c4c62 | -7.3138 | -55.60856 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddb9abe-77f6-390a-b5ca-8240250af5f5 | -3.1443 | -61.39905 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d90c39f3-c51a-3ae2-9553-8add21b8ad5b | -8.61298 | -54.59692 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2fd6081-2bb7-3a29-bc89-02a97141f431 | -10.40373 | -48.36516 | 2026-09-20 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d552025f-c604-3970-a79a-ed74fec4aec2 | -3.35152 | -59.86256 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 979de260-1dc7-35cb-9481-44adb1134597 | -8.63391 | -47.61775 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0394a35-c13d-3dd9-9cb7-a5f5a3775539 | -3.58883 | -47.35521 | 2026-09-20 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5727a624-b87d-33ef-b83e-26b7b070a68a | -5.22419 | -47.58601 | 2026-09-20 05:23:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3bf71806-9ddb-309b-88cf-fdbef9eff704 | -1.74628 | -60.53132 | 2026-09-20 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c5cee3-6ce3-39a7-93a7-b6262d0a312e | -3.34647 | -57.86199 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1554f9fa-e42c-383c-8331-f00819a777c9 | -8.17701 | -54.7628 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e178fa45-50b9-30f6-89bd-c2e9728437f7 | -3.35482 | -59.86306 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README88.md)
