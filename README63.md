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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e0ae2f5-6902-3185-994e-bb892374ca36 | -6.0371 | -57.7065 | 2026-08-16 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| b65a9e42-7d35-3ef9-87b4-8d61cc9d0ea9 | -14.4678 | -51.9832 | 2026-08-16 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 810845a3-4e14-354c-a019-279e3d8deb7a | -15.0682 | -47.0098 | 2026-08-16 14:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 45c2d9d4-9588-3a62-b517-1d78a9e0f76a | -12.7017 | -48.4753 | 2026-08-16 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 03e5b603-0a31-350f-b13e-7d1616e9c390 | -6.6854 | -43.9802 | 2026-08-16 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 548.7 |
| 688e3b83-16f8-36a9-8dd4-0aee0c3b67c8 | -14.5382 | -53.5366 | 2026-08-16 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 47fc0ae6-c460-3432-9848-2d7b253e9fb1 | -9.2079 | -59.6742 | 2026-08-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b661b869-c14b-340f-9792-3ca9a8bde7a2 | -6.704 | -44.0017 | 2026-08-16 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0d0d859a-e51f-3da5-89f0-fe4248ff11dc | -6.8387 | -56.4344 | 2026-08-16 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a4daad73-3dec-3297-9bc7-c4f745492329 | -6.6664 | -44.005 | 2026-08-16 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 72ea84c1-1a92-348e-9387-84ce2f3c0412 | -11.8291 | -51.7937 | 2026-08-16 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 308de5dd-8d2a-333d-b5ab-d6522b445fbe | -11.8101 | -51.7957 | 2026-08-16 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| b3df1bad-c750-3c36-a30a-dd25d1317285 | -12.1768 | -50.1773 | 2026-08-16 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 897c5e14-90a0-3878-a9b2-4e06c2e0f0d9 | -8.446 | -62.6752 | 2026-08-16 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 373303a5-00f6-3375-b90e-f826290e57e1 | -8.4276 | -62.657 | 2026-08-16 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3b8f2cbe-e257-3a6c-9c71-f7acf6e89bac | -6.1107 | -57.723 | 2026-08-16 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 2a54fa33-3a26-3564-834c-7dc200ea0bda | -12.6825 | -48.4779 | 2026-08-16 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| a696441c-a460-363d-b0ed-7afd6536b993 | -8.9601 | -60.5165 | 2026-08-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 996ac5c9-dd32-3d6e-a2eb-ea0ac0d63f18 | -6.8572 | -56.4335 | 2026-08-16 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7a4fef78-ea61-31b4-9071-52fa1c64ae06 | -12.0474 | -46.4444 | 2026-08-16 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 1abb13a4-5012-34e0-8774-21c17847920e | -14.2949 | -51.9422 | 2026-08-16 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6a75e9b1-7cf0-3238-ae66-c8b4f7c2d53c | -6.6198 | -58.9836 | 2026-08-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a03de568-b29e-3c11-939a-19ee08a9346e | -11.0613 | -47.2279 | 2026-08-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 73b86596-b9a4-35b7-a97c-f5a7b6564985 | -8.9787 | -60.5156 | 2026-08-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| f914722d-6a28-31b3-8d9b-ed47cc914f65 | -6.6666 | -43.9818 | 2026-08-16 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| adaf3098-4e5f-342a-9e66-b549bff59fca | -6.11 | -45.3298 | 2026-08-16 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 90a00d6e-0159-32cc-bcdc-53694d4512aa | -8.4275 | -62.676 | 2026-08-16 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c27eff6b-3c83-3bec-a1bc-462351517f64 | -15.0677 | -47.0326 | 2026-08-16 14:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 742b64c1-025e-39f2-ae2f-b660102f2031 | -6.6852 | -44.0033 | 2026-08-16 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 551.7 |
| 7fe58325-8b82-3eb1-931b-2b07db32b4db | -8.9785 | -60.5349 | 2026-08-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a3103683-370c-3e0a-ace6-3f312593075e | -6.1108 | -57.7035 | 2026-08-16 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f2e681a9-e3ac-37f8-bb55-a3ea9a2ffbe5 | -6.1107 | -57.723 | 2026-08-16 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 64154eab-565a-3699-b76b-2772a49d38b0 | -12.0091 | -46.4498 | 2026-08-16 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b8616735-2a8e-3dc4-939a-8bf6e6395570 | -10.2576 | -50.4332 | 2026-08-16 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 5968f634-8a28-3983-8def-14f5e478e713 | -14.2755 | -51.9447 | 2026-08-16 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| af012a74-66cd-337c-8a8c-d0ddd5484cce | -6.11 | -45.3298 | 2026-08-16 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| a6e35fe9-1fb1-3430-b2c3-a54accf203ae | -15.1106 | -48.7128 | 2026-08-16 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ff3eebe1-2e6f-30db-9e3c-21843783faab | -8.9785 | -60.5349 | 2026-08-16 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 19fb1445-061a-31c5-a5e6-ebed3aa4c2f1 | -6.3137 | -43.6178 | 2026-08-16 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 290c62d3-2c8c-3070-8e86-902a4bc690aa | -6.8597 | -58.9738 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 96bab35b-5879-3f0a-9b0d-d01fb6892fbf | -6.8387 | -56.4344 | 2026-08-16 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c28634d7-4215-3bff-9777-46aeb9f92cd8 | -15.1515 | -48.6171 | 2026-08-16 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 50b9d9c2-c38f-3ebf-8c90-2fc8b0a8439b | -12.0282 | -46.4471 | 2026-08-16 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 303729fc-231c-3756-afe1-31c4b07384af | -7.5871 | -60.8845 | 2026-08-16 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0d379b73-3a3f-3aca-87cd-faaf20c6ce45 | -6.704 | -44.0017 | 2026-08-16 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 7ef13a94-3df1-3ed5-8298-1856fb6c12aa | -8.9601 | -60.5165 | 2026-08-16 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 1ce0380c-2f83-3e11-b6d3-b3997a7c990a | -14.4868 | -52.002 | 2026-08-16 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d43436e2-66fa-324c-b003-aa94ad5a3e46 | -6.6854 | -43.9802 | 2026-08-16 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 372.6 |
| cc738493-bcb1-3085-913d-aa27ba8f3b4c | -6.6013 | -59.0037 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| bcfa33c8-c938-3279-88f0-c5ce6e70036b | -14.4678 | -51.9832 | 2026-08-16 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 32f03dce-26ef-3cb9-b174-ce2db54dd69f | -6.2938 | -47.7367 | 2026-08-16 14:10:00 | GOES-19 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d7a05bd6-e1a5-3246-9901-dcd1d9510d06 | -8.4461 | -62.6563 | 2026-08-16 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e4d833ca-5116-3985-a809-228104cf995b | -6.7123 | -58.9412 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 2f983e79-7def-3932-834c-5bc2903f61b5 | -11.08 | -47.2479 | 2026-08-16 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c072b91e-6917-3707-83b9-1c95c60594da | -6.6198 | -58.9836 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 227cebbe-63d9-323a-a8c1-da5022d68e63 | -11.8291 | -51.7937 | 2026-08-16 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| bc6038b9-2741-3451-aeaa-21b4daf72cbd | -14.5382 | -53.5366 | 2026-08-16 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b8b6cc3d-70c9-368e-9cfb-c99ef0805ed7 | -8.96 | -60.5358 | 2026-08-16 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5a39b25c-c58b-33e9-8f08-40c4d910690c | -14.4317 | -51.8388 | 2026-08-16 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 79068a17-fcd8-3f0e-ba67-a9d757b811f9 | -15.0677 | -47.0326 | 2026-08-16 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 81cf8fe0-4f5d-368d-9cff-a6fb39efb1c5 | -8.446 | -62.6752 | 2026-08-16 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e4dbff57-cb8e-3f93-acec-6ba95d70b13d | -6.6014 | -58.9844 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.5 |
| b120ce11-b6d7-3cb4-9132-a8750b75032c | -6.0371 | -57.7065 | 2026-08-16 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 997ce401-9f28-3965-9d2c-609b9d42195d | -6.6664 | -44.005 | 2026-08-16 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 13213bda-3855-3235-840a-69c1d4b26c89 | -7.4444 | -60.0092 | 2026-08-16 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 86abdbad-c502-3626-9468-ee11ad76139f | -6.8573 | -56.4137 | 2026-08-16 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e2d7578d-1822-3bdb-a76f-a0f3d5b2a3fd | -11.0796 | -47.2702 | 2026-08-16 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 8a13168e-b698-374a-acc9-ddd593fff083 | -6.8572 | -56.4335 | 2026-08-16 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6d6fa957-dd4b-3568-9316-620dda54be68 | -8.9787 | -60.5156 | 2026-08-16 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9af3e1ae-2327-3faf-9667-fe20fd2c0c1e | -6.6714 | -45.3535 | 2026-08-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 33311421-8dbe-36cd-8e98-f733370fc271 | -6.1106 | -57.7425 | 2026-08-16 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 30748aec-adb3-39e1-b70a-6b97567ac1c1 | -6.6666 | -43.9818 | 2026-08-16 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 49805757-8a23-3e6c-a81e-ddaa04b85fef | -8.4275 | -62.676 | 2026-08-16 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0e17ec73-f48b-325c-bdac-eb99c31e8917 | -11.9365 | -47.3367 | 2026-08-16 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ea8b5ddd-35d0-375f-ab39-0dff0145deb1 | -12.1577 | -50.1796 | 2026-08-16 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bbeda277-f082-3a72-a495-1f346638ec54 | -14.4484 | -51.9858 | 2026-08-16 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 23c4e055-aa4e-3246-aa79-cd9575164b66 | -6.67 | -44.02 | 2026-08-16 14:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4097b8a-3cc5-3438-97df-2180c5d8eeec | -6.67 | -43.98 | 2026-08-16 14:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b440bce-9d3f-3232-bda9-20a74dfc1a64 | -12.1577 | -50.1796 | 2026-08-16 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 62fa28d2-c2bb-3b6a-9754-008b2a19a3cb | -6.8387 | -56.4344 | 2026-08-16 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9e996185-7d13-3184-84a9-ac956f0f63fb | -14.4317 | -51.8388 | 2026-08-16 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 187.5 |
| bf84e939-9e65-34fb-b1be-aab3826e0a9e | -11.8291 | -51.7937 | 2026-08-16 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 468747a5-94a3-3115-b616-218bb03369ef | -6.9702 | -59.0078 | 2026-08-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b7b3700c-42e7-3b4a-9351-a70e6b98e019 | -6.7123 | -58.9412 | 2026-08-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c35d1477-d85f-3435-bba1-60e8236a4382 | -6.8573 | -56.4137 | 2026-08-16 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| bf282bda-b564-37e4-813e-1251b3ff437d | -6.3137 | -43.6178 | 2026-08-16 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d22c7b2e-565a-3920-8ed4-48dc65dd23c6 | -6.6666 | -43.9818 | 2026-08-16 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| b81711ae-d441-3ccc-8769-5ae92715beda | -6.1108 | -57.7035 | 2026-08-16 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 09b638c3-3071-3059-8bac-d175000ab93e | -8.446 | -62.6752 | 2026-08-16 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c6ca73be-c653-3240-a7a0-67b4e06caa7e | -6.7236 | -45.7552 | 2026-08-16 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 74cb5204-2aba-36c8-98ae-a06e9a864105 | -15.1515 | -48.6171 | 2026-08-16 14:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0e7b727b-32e2-3f3f-98f0-8079d37e60d5 | -8.4275 | -62.676 | 2026-08-16 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 69fe6d52-e3ca-32e2-a145-7997bafdac8d | -14.4678 | -51.9832 | 2026-08-16 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 15c1ef16-0786-3960-b202-301395f59b3b | -6.1106 | -57.7425 | 2026-08-16 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 751801de-8eab-3b05-862b-20140bb3baea | -8.9601 | -60.5165 | 2026-08-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 194ab85c-f2ab-3b1c-b5c9-e26c1667cd91 | -7.5871 | -60.8845 | 2026-08-16 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 58f61e39-614d-3377-9981-fe711365d27e | -14.4321 | -51.8175 | 2026-08-16 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 87c97177-a9b5-3204-83b2-3656b671bd72 | -11.4094 | -50.6096 | 2026-08-16 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1e1cad5e-8388-396c-b714-a6e4b191c060 | -7.0257 | -43.7875 | 2026-08-16 14:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d5f9090c-f24c-3fb6-bf7e-b7125a00b401 | -8.4276 | -62.657 | 2026-08-16 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |


[Clique aqui para ver as próximas entradas](README64.md)
