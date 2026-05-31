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
| 71cc5d53-828b-3175-8dd0-2910e456521e | -9.15765 | -46.8397 | 2026-05-31 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7469de23-54d6-315c-8aa9-5b2bf3d3904c | -10.0682 | -51.65431 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ebf374a8-daa3-3958-bb08-72b3a2121a82 | -8.25889 | -48.22723 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2871f76-7d48-33b2-8efc-c1972426b02c | -10.63153 | -48.32077 | 2026-05-31 04:36:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8af98235-47d1-32d4-a9ff-6041e8326157 | -9.21243 | -48.55539 | 2026-05-31 04:36:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56ae62f7-c891-3b90-8ef8-ab03c53ff3a3 | -10.06905 | -51.67146 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1a9bcaa-712d-3e98-91df-375b4dc65f0b | -9.02094 | -46.66048 | 2026-05-31 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6f6516c-bd9e-3de3-a06d-48cf68fb9cd2 | -10.14283 | -48.08128 | 2026-05-31 04:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32f7d92b-89e2-3ea5-a8c5-291d371f9fb0 | -10.07562 | -51.66697 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a2f24c1-ac64-378f-92c4-389e1b82d3f8 | -7.65395 | -51.65944 | 2026-05-31 04:36:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 880975b5-0efd-3435-83cc-dc5cc0b91bc5 | -10.03842 | -51.6789 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ede6a58-c329-330f-8a67-489c694b9899 | -10.75654 | -46.91476 | 2026-05-31 04:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dad4854d-b41d-392b-9ee9-dd350f899371 | -10.06837 | -51.6756 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bac2af5d-b560-3df9-9e4f-4cf8acc04047 | -10.05436 | -49.11361 | 2026-05-31 04:36:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04cf2320-4b4c-384e-8de0-088c94c0af13 | -10.07135 | -51.67047 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 20396f78-58c6-34b5-ac97-d1a7f141bdd0 | -6.80186 | -59.04509 | 2026-05-31 04:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a7cfcaf-ddf9-34c7-8acb-34a3d7367afb | -10.81422 | -46.88123 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 327be386-6177-39ee-afc9-79c0382a644a | -10.04898 | -51.65954 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 740a1790-dc2b-30c8-92cb-c67949cc89e8 | -7.07906 | -46.2841 | 2026-05-31 04:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 754c7d65-91a6-3946-bb20-2c8a3e3924a7 | -10.06769 | -51.67973 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12490ed2-f881-3ae8-9ceb-ab5dfb0af562 | -10.07128 | -51.64925 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 830b340f-7944-3fb5-bf83-4623e0b734d6 | -10.06702 | -51.65273 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b1f5262d-7d58-3219-bbbc-25880a003f57 | -8.03844 | -46.57946 | 2026-05-31 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7332f7ba-a2c4-3660-bae8-837d6128f906 | -10.07198 | -51.64515 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5653e7f9-db7a-3be0-a72d-0130633b0a74 | -9.45449 | -51.83115 | 2026-05-31 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 396940cf-4aef-3878-ac84-1645965a46c2 | -10.06616 | -51.66671 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e47fb75-0b75-35a8-a58f-b47a1625860e | -8.26496 | -48.23175 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8333c9b2-9ce2-3eb9-b4f0-2f2365902c3b | -10.13952 | -48.08074 | 2026-05-31 04:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de310de-29fe-39cb-8909-05f184f8566f | -10.38933 | -49.44218 | 2026-05-31 04:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fc3b129-2740-3178-a278-7b560f0ec5f2 | -10.06841 | -51.64454 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 938bd009-181e-3d3c-a0dc-4fc81a64361a | -7.50743 | -55.00817 | 2026-05-31 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08d6e83-0be1-3472-8c04-c05d92997c1e | -6.83786 | -47.93303 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d226a1bd-519b-3d40-81bf-84258caf6103 | -8.26055 | -48.23817 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c6885ff-7dfc-3e6b-adad-96829cd5f050 | -9.79482 | -49.67233 | 2026-05-31 04:36:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8799e5d3-521b-3024-b65a-53b67d3c9e6e | -9.02086 | -46.65743 | 2026-05-31 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 313fcecd-097a-3684-ae55-e040d2c25907 | -10.07415 | -51.65398 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b29e51ee-193c-3ace-b704-a7a310f49b00 | -10.07244 | -51.65082 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d14cf356-7e11-392e-b1f3-7cc56b5a19cf | -6.84117 | -47.93356 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8577a84c-4faa-3607-b2f3-6e4303ce59c5 | -10.0628 | -51.6775 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78385504-5151-334e-b9f1-baec7fb661ac | -10.54892 | -48.69532 | 2026-05-31 04:36:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42ca74cd-8e7c-393a-9c68-16348b137596 | -10.06919 | -51.66159 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bc84cef1-dd4e-30bb-a174-0e0c7512e22a | -7.49911 | -55.002 | 2026-05-31 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b1a7928-47e7-3071-98ed-5c0acf9a4220 | -10.77935 | -46.90292 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b213210-ff0d-3b01-91e8-75777b916376 | -10.79079 | -46.89684 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25451cc8-b9ad-3e72-b4c9-16318a93e19c | -7.07849 | -46.28777 | 2026-05-31 04:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cffcde7-f114-3a9c-9696-a1c2e95af25f | -10.05901 | -51.66549 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7f4ce47b-c88d-3e48-ab4b-2e666c9d115d | -10.47114 | -48.67202 | 2026-05-31 04:36:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfdc6a63-364e-33be-9ed0-00da6cbc16e1 | -10.06561 | -51.66098 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3ca864ff-c75a-38b0-acf4-41a446a52c77 | -8.2622 | -48.22775 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de67ec88-08a0-3fc2-9134-506edcbfc2c0 | -8.72973 | -48.32083 | 2026-05-31 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfdab34a-9fbb-33e5-92d7-7e33ab61e13b | -6.84448 | -47.93408 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0348260d-8fc3-3957-a8bd-701e727345d2 | -9.45157 | -51.82629 | 2026-05-31 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29d64a4a-27f6-3d8c-9a2b-962b6bdacbf1 | -10.05476 | -51.66902 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a1bcae-5323-3252-9506-8be930efa1f7 | -10.06684 | -51.66257 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c275b409-046d-3ff1-9e35-dceb1876c7c3 | -10.06771 | -51.64863 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d4f3d97f-b23b-342e-9e89-4c2073b299ae | -8.26165 | -48.23122 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7390ae3f-b700-39ae-9478-361d72b88f6d | -10.06632 | -51.65685 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a2fd70b5-6ef9-31b1-aa7f-af34f6e2a825 | -8.04183 | -46.57999 | 2026-05-31 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15fd783d-fbff-32c9-acc8-2d22e9725e16 | -10.07177 | -51.65493 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e013c5f-4465-3881-98bb-c0377ef1fe95 | -10.05969 | -51.66136 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 25cbaf5e-2f04-3d51-97a1-e296efc21fbe | -8.25504 | -48.23017 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 723673b5-07b9-391e-8868-5fbf84091e68 | -8.20684 | -49.84023 | 2026-05-31 04:36:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| daee3e88-d0b3-3fff-924c-70a9d0e61290 | -10.46782 | -48.67149 | 2026-05-31 04:36:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da3e85c-5358-3f2d-8eb8-02b264bc3d1e | -10.05105 | -49.11307 | 2026-05-31 04:36:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87d2f5fb-81fc-3aab-8824-819363d39f0b | -10.74409 | -49.02832 | 2026-05-31 04:36:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e76185ad-2bce-3f32-aa1d-f50947e5cbbe | -10.06752 | -51.65844 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f24d7eff-e684-374a-9c0e-02a7bc6b550c | -10.0648 | -51.67498 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 190bcd45-446a-3cf4-aad4-ade6871befac | -10.06598 | -51.64548 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b097742-c2e2-3376-9f81-6f51556aa63e | -10.06778 | -51.66985 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c13ab96d-a52b-3de6-b17d-26e2ae81f6c1 | -10.78221 | -46.90715 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d76eb94-11b8-3ea2-9cd8-b286fef8ad56 | -10.0653 | -51.64959 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ebafe162-23f8-376c-afc4-29e1143d0824 | -7.8942 | -47.99832 | 2026-05-31 04:36:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c06a191b-80e2-3935-adc0-d97e9b11eda1 | -7.35322 | -45.37149 | 2026-05-31 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d9d927d-ba83-3d96-ae35-cb5d16c9ecc1 | -10.06327 | -51.66196 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 139191c7-888d-3e35-bc9e-91c696a472d2 | -9.49179 | -48.65711 | 2026-05-31 04:36:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8604d873-7776-39c1-a3ce-63e49a830acb | -10.07275 | -51.66221 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11dc37fa-0ab3-3918-beb1-b4e7633add51 | -8.25779 | -48.23417 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e3e3ace-9aa9-38b2-88fb-33aa620c164e | -7.08654 | -50.4082 | 2026-05-31 04:36:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fe3c6fe-9bf8-3d8f-ae6d-80ad90a25da8 | -10.75996 | -46.91531 | 2026-05-31 04:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 505f2bb2-f646-3b3c-b081-85e6d1b2ae1e | -8.72918 | -48.32431 | 2026-05-31 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef62a1c1-0df9-31bf-b6b2-d8c5836c7d86 | -10.68506 | -49.61039 | 2026-05-31 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0923396c-4eb6-3f7c-ab65-77eb0c03b82c | -10.81095 | -49.33389 | 2026-05-31 04:36:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 600eccdb-fc79-390d-8f69-dcaf6855410a | -10.21144 | -48.33638 | 2026-05-31 04:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd57db51-0f9a-3122-8318-b579de68ce94 | -10.06548 | -51.67085 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 58316ef7-5cc0-3a75-930f-2c0c99e6fa0a | -6.83841 | -47.92957 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33210c80-deb9-3a08-a9d7-2a7ba46834e2 | -8.25834 | -48.2307 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e2dd0cc-dcc0-36d1-9cf5-452cdd28acf5 | -10.07205 | -51.66634 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 779f8fed-0b38-3098-a966-f91a12de3daa | -10.07345 | -51.65809 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57d26343-d8f8-376f-8060-a288020926b9 | -9.49124 | -48.66059 | 2026-05-31 04:36:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652f098b-a77d-387b-9f7d-f44ea550b31e | -8.11842 | -46.4712 | 2026-05-31 04:36:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9fccd05-e9a3-3f2a-9e68-0ebb4b5d1a16 | -7.65324 | -51.66374 | 2026-05-31 04:36:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65946e42-9650-3fbb-b27f-0da8dd4d605f | -10.06955 | -51.6461 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7417ad5-6cc5-3efe-bf46-62d3bd365b87 | -10.05161 | -49.10957 | 2026-05-31 04:36:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7364d626-d2a7-3420-8efe-94857ef73d69 | -10.07312 | -51.64672 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 975d3a93-0519-3498-8b67-fa12c2c0ed94 | -10.06421 | -51.66924 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 69623ed7-38de-3cd1-b250-3337e6ef42df | -9.23035 | -46.6165 | 2026-05-31 04:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f499544-1008-342d-8907-029a869dccc5 | -10.74078 | -49.02779 | 2026-05-31 04:36:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10c07b51-84c5-3ba3-8133-df78aa40afc9 | -9.16104 | -46.84023 | 2026-05-31 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8730306-654b-3e71-bd6f-83cd960df568 | -8.20346 | -49.83968 | 2026-05-31 04:36:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b25a3991-5227-3a49-8fdc-7202ba19e2d5 | -7.4983 | -55.00666 | 2026-05-31 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README7.md)
