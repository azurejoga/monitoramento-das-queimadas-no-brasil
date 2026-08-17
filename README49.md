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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c8b195c-198c-3fb9-8b22-eb5ab11c115e | -6.9809 | -59.01684 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f89c005-e0d0-3952-aad8-f15195145655 | -7.37549 | -55.4837 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff4c9de3-fbae-36af-9895-0a2dfc2042f4 | -7.58215 | -61.23114 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f08fa3-7ee1-31e1-8ba6-7cf13598ccc3 | -8.67085 | -54.77097 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f279edc-72bf-3c8c-b018-88a7a0aff66b | -8.63869 | -54.68762 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c8d610-160c-3850-8987-093a28e865c2 | -6.02147 | -57.81227 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c55ad9a8-9c1d-3408-a193-21bcd484ea26 | -6.12305 | -57.72958 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b3b591d-7f8a-3e42-9d38-8a9218953dc8 | -7.07334 | -56.65702 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1e34d8e-befa-3a1a-8400-81975533e488 | -8.95077 | -60.54111 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44aa5d3b-d0d7-3acd-9b19-247ed265edd2 | -8.97909 | -60.50848 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49dcfa77-037b-371f-82b0-52ce48a8cd60 | -3.99145 | -56.27719 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4385684-b268-38f0-b7bf-222ba3c28154 | -6.85873 | -58.97123 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f34128e1-b37d-3b68-8b6d-ea240f3215dd | -6.78829 | -59.47012 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78050045-4333-3117-ab8f-2bd6c440098b | -6.0314 | -57.81385 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac17c951-0a1c-3851-9d4e-6c5f96f3dffd | -6.11203 | -57.73492 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32782a88-f588-3ae2-a28a-c87537462d57 | -11.12818 | -46.50731 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e01b319-98f7-345f-bfe3-cc38b0ff779b | -7.45992 | -59.9989 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 606df848-e81d-3cc1-85ca-b6d49acb8440 | -8.52257 | -54.8882 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 773e6184-68a5-385a-8dba-b25112eb5ecd | -6.83307 | -56.45288 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc7a8078-165f-3567-a313-98cd2249a539 | -7.39149 | -60.01215 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96fba841-456d-37f2-8c7e-3f3e3f2f83a2 | -8.9691 | -60.51625 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1df70c4-cc12-348e-8561-799da94c32d8 | -8.94919 | -60.52886 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88847219-dc63-39dc-bd93-d812a2212856 | -8.97036 | -60.50852 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caa2278a-110e-3b3e-bb98-5567d4af677d | -6.98925 | -59.02922 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdbc803e-7cd8-37f4-96cf-ebe19e715ad0 | -7.38077 | -59.99084 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29e182ff-3035-3244-aabd-8e0c6c9f30b5 | -6.7713 | -59.76993 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c3e4ffb-249f-3beb-bece-363e065e7483 | -8.89525 | -60.59581 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b526b6c-a9b7-366a-a995-e5642067a919 | -6.86489 | -56.42494 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1654ba4-904b-368a-80b2-9474527a4d44 | -8.63358 | -54.72184 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b616b993-7fba-315a-8afd-32a154c33d37 | -8.97805 | -60.53614 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fceca911-d675-30c8-a9fd-c87bb5829d41 | -6.78268 | -59.46162 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ee53bb0-0583-3763-a6c5-2dd3d58be92a | -6.78047 | -59.4537 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8357b51-2f86-3458-b966-3177af7625ef | -8.95012 | -60.58897 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a4ae791-b7f3-328c-82ff-ba565bfce113 | -8.90232 | -60.55299 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f8a3e47c-1219-306e-a0ca-a2f244873a51 | -6.99263 | -48.05848 | 2026-08-17 05:16:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b879fd-9b03-31a9-aec2-cfec70899812 | -7.42853 | -60.01719 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8519091-cd08-35b1-941a-aeb9d3068b07 | -6.83919 | -56.43557 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29181c2b-6efa-34bc-8369-e61572e2ac24 | -8.96026 | -60.52672 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35fd738f-7879-3bc9-96b5-b1868b8543bf | -6.81864 | -59.88642 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b05e06cf-9922-3d3d-987f-10d9fa8a2fda | -6.61288 | -56.27234 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af53488d-6c17-333d-9c44-782a1981eb86 | -7.37599 | -55.50336 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5d24b0-a6e4-36c0-ad01-65aa3c6afe31 | -6.72128 | -58.92344 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 365899e4-ca63-3b70-b85c-c30067c6f065 | -8.52426 | -54.90141 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5078b15d-bd78-33a7-b984-c9b9eb38effd | -6.62185 | -59.06951 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa77c57-ccdd-326e-9df3-da0f52e1ca90 | -6.85596 | -58.96711 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 431ba462-b5d0-3246-be2f-9bf9baeab7d3 | -7.37857 | -55.4991 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86487460-0dce-39e8-ba11-fc79d6fcbd67 | -6.62077 | -58.96961 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ea4de66-6ee0-3493-b234-9fa80ca1f2c3 | -6.81911 | -56.45432 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b951c54-0d9c-3d50-aa00-d3640d0777f7 | -6.88205 | -59.01911 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0f30a0-78fb-3e0b-9df5-a89b8dd747a4 | -8.97214 | -60.50734 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d91aef0-ca54-3f43-9965-172c55039561 | -7.5314 | -60.68564 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dab3847-db16-3911-8ccb-e2c8353d81f9 | -8.61315 | -54.68364 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5626116-aba9-3722-8db6-63f2a693eb20 | -8.98707 | -60.58953 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa2f0c0-fd3c-3968-8368-d3a2c379759a | -7.39534 | -55.48209 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83c77f03-7a21-30a6-8b53-ddc2197ba374 | -8.60207 | -54.70817 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc0b1f80-12d8-3208-a10a-b3c44ae8f7d1 | -6.61462 | -58.96496 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b361a6d0-14cb-3250-ae0e-fb698cfe2f4b | -8.95203 | -60.53333 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6196673-9d33-37cd-8e93-d9c22b31ff19 | -8.59981 | -54.67286 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d46dc167-40f9-3873-afb4-2dd488e7810c | -8.59491 | -54.68082 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62245593-38fc-36e2-990d-21f24127f82b | -8.96891 | -60.52666 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a072cadd-6675-3639-9282-8c7a4559d4d5 | -6.11258 | -57.73146 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbad977b-7319-3f85-a4a8-3d52a50d319b | -6.61798 | -58.9655 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efd7c522-9d95-3543-9bf9-58d155ac91d0 | -7.37741 | -55.50676 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f3f5177-5e41-35ff-a88a-66e22c4a297d | -9.29968 | -56.92175 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60c7b8c4-391e-3a99-ab97-27a0542a908a | -4.35481 | -46.16226 | 2026-08-17 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c73a8d82-a2e9-35b6-8f8c-00ce4ed63afb | -7.40595 | -60.01056 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 116cb3f8-671a-37b1-a1c8-3848c52bfe87 | -8.56251 | -54.59854 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee014c07-315e-3ea4-a4c9-53d263b28253 | -8.95393 | -60.52169 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd5a4095-40e6-32c0-8e26-f124260e719c | -6.62923 | -58.95995 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 23dd8cac-bd3d-3ad2-a69e-745b57ff3642 | -6.1192 | -57.73252 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe74c1cb-c8f7-3c65-b8d9-a6a8b3088c00 | -4.12557 | -56.33056 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79bb5225-dbab-35a1-afd1-26eda81d3d96 | -3.79411 | -59.33379 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1cbab8c-3624-3b62-85d1-7b701f831e45 | -6.71621 | -58.93362 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6789fcaf-6298-3065-beaf-045da46634b9 | -6.63201 | -58.96409 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08abf1a2-55d6-3235-a219-7842dfcc1e26 | -8.97098 | -60.50466 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8952091a-503b-313e-868e-18341c221e8d | -7.87867 | -63.75311 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bde3cbaf-ff27-3076-a346-4325295fbba1 | -7.79679 | -62.39167 | 2026-08-17 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed3ae76a-0b47-3c80-8691-77e32f66f67c | -7.398 | -46.8233 | 2026-08-17 05:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f988095-6024-3421-b22b-f7b58ba40356 | -7.37568 | -55.49472 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17440536-3207-39cf-967c-74104cf8e63d | -2.96765 | -59.13202 | 2026-08-17 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbdff337-9479-3aa8-872a-21ef3439e059 | -7.8099 | -47.84015 | 2026-08-17 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9f23441-9392-3d03-980c-ae75ecaaca56 | -6.85144 | -58.97372 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42b32213-e60e-354f-a3c2-a599392c0520 | -6.84808 | -58.97319 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b36ba35e-9983-3cdd-9c90-f97c8703fb9d | -6.69934 | -58.95286 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82be2d5-7140-3856-b331-52ca2df3132d | -6.82637 | -56.45182 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58abef23-29b9-3c4a-9fc0-757a04c02c2c | -7.36737 | -55.49028 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2a66476-15cb-3370-ac4b-eef1a6a45fc7 | -7.55869 | -61.17014 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b22dd5e-1a09-3485-a583-4a1d59809700 | -8.95045 | -60.56496 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b921c10-6098-32d5-b60e-b90e19cee034 | -6.60167 | -58.39325 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeebdb88-a257-3b0f-9ff7-1aa0ed579b9e | -6.62976 | -59.06339 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5cbcee9-520b-395e-ae72-3652580c081a | -8.63422 | -54.71757 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c59325c-325f-385d-9b76-f7cf28da00f1 | -8.68435 | -54.7556 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8afce4f1-b951-3f0f-9130-bcd5cac75576 | -3.80107 | -59.33488 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e60048f-086a-32bb-8c89-10bda1dd816a | -8.95234 | -60.59735 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d31c526f-ed85-386c-b0e2-e37c9dc02bfd | -8.6702 | -54.77522 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94076662-d7ab-38d5-ad02-9863df9b4d85 | -7.42726 | -60.02485 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf85d65-3ad1-3547-8622-3cebf3464c93 | -6.96398 | -59.03618 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0886beea-bd3a-3bad-b4a6-72d411b5ff67 | -8.51283 | -54.9038 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b13349-a509-34ad-99c1-76c2ce232b6a | -8.94982 | -60.52499 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38e02b9f-fa15-3822-b442-17777ea7f0fe | -10.50142 | -50.02523 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README50.md)
