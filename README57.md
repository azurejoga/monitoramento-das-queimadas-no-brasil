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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5b341ae-ae89-3516-9bbf-4ea4d43e312c | -11.4713 | -47.38771 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26864dbe-6b48-3cea-aeea-b6b4a5a584d9 | -12.15559 | -50.75338 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de5093c2-f231-38b7-85f1-69823267167c | -10.41895 | -49.37371 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d383cfe-2de1-388e-8d66-8ec9c5d4bf1b | -12.16179 | -50.75825 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b3d7208-08e6-384b-bad4-e4681c5bd237 | -8.39075 | -46.29216 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ed8272f-b724-3dd9-be69-1d09da20a327 | -9.57604 | -46.51096 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c3436f8-37ad-3012-8ef4-46eee0dc794c | -11.96521 | -50.76361 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b8343f1-54a7-3b07-9410-7c9de59995c8 | -10.09184 | -46.04596 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ee9fb6a-a76d-3095-8086-58ed95d632c5 | -10.08951 | -46.06161 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4bb8616-4366-34b3-b191-a5357a00da23 | -12.67875 | -45.0335 | 2026-09-24 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bced328-fe4d-3154-bf8c-9329d8ac3c08 | -11.64956 | -43.48429 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f8546920-ee34-3278-891b-a2a70a9cdef0 | -10.25846 | -49.96332 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f86cce6e-a1d1-332d-a082-52d7463d9634 | -10.2815 | -49.97084 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b090dd11-63f6-3087-a167-c9e457211169 | -6.89731 | -55.57456 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 366f67f1-a112-3eb0-a9f5-a26df6a4892e | -9.4652 | -40.33202 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 140da79c-9c3d-3198-9cfa-aa6e042f7ec8 | -12.15994 | -50.76938 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 108c8edc-5be3-3464-8a6a-682e0b6eaaf3 | -6.44905 | -59.9613 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19c90f83-92c4-30dd-86eb-10b2c5f14457 | -8.38672 | -46.29538 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5baef650-d09b-3e8f-b819-b22d507b19a3 | -9.32761 | -56.81433 | 2026-09-24 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbb494ff-77d7-3120-8c2f-3ff423b3e1f4 | -8.72018 | -47.60669 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5634a6e-2df5-3ad0-b9be-d7be5988f88f | -12.28918 | -46.39132 | 2026-09-24 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea461e4f-23cb-3be7-8a2e-d48cf067fde2 | -12.17429 | -47.37199 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9df95a5f-d749-3e0b-93df-c2c0a85e3e4c | -9.85946 | -48.5084 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 965791dc-739d-3e21-bc88-3d223d26ef56 | -10.90882 | -53.9472 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d920a22d-d45b-3aa0-9e19-d08d33065a46 | -12.14361 | -50.72157 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d6adf30-7258-3e6e-90cc-020e2ce5dd6a | -10.41454 | -49.35847 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ed07c43a-beb9-398c-a451-32fc4f78df0b | -11.62744 | -50.60886 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7009b930-9e48-3174-8c06-5044092bf30c | -12.05849 | -50.30057 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfac6a67-e2f5-3228-9b2c-54c99fd6f6af | -6.87898 | -55.56611 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a19a90-4e45-3a72-99db-0aeec973665f | -6.62056 | -59.93525 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ddca74b-526d-3f30-908b-6b10a0ea80a5 | -10.45889 | -51.31002 | 2026-09-24 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77be083d-55b2-3db2-88bf-91343e2b1d8a | -10.91069 | -53.93654 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a45b804-2e04-356c-a703-167186ab26ab | -6.63978 | -59.93881 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf7a27a5-915a-3f30-9a84-c935ce402ff5 | -8.77232 | -45.66014 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92846b4-406f-3688-92d5-64b4e450f524 | -11.79679 | -50.97848 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae748122-0655-31f1-97a1-9b82b671a4c3 | -11.65269 | -43.49261 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1ad8e184-a924-3d1d-803e-008af438568b | -10.61757 | -53.99164 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 001212c3-05ef-3e1f-b243-3afe67e68f2a | -9.23502 | -47.35229 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83427999-c7f2-3261-b8a5-649abea3b52e | -11.49625 | -42.33795 | 2026-09-24 04:46:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ac2d3970-14e7-3b65-b0af-b2d9834e593a | -10.09066 | -46.05391 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a0cae6b-e687-3464-b085-b2f6ce08bd89 | -6.03926 | -57.77588 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 473b741a-3025-3867-9732-fb88025eb6c3 | -11.72018 | -50.76524 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75393b25-aa45-310a-8598-8d3023492630 | -11.63151 | -50.60601 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 63f26918-04a7-3085-93ae-945b4a88a3cf | -12.14618 | -50.74867 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 252f73b9-f616-36b3-804c-1dea29636fcb | -10.31762 | -50.41293 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a7c70f-64f9-3060-9752-c308357c8053 | -9.22516 | -47.34311 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e64ae687-c06c-3dbc-ba2b-5d9b58977697 | -10.87353 | -48.51242 | 2026-09-24 04:46:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 483031fe-1849-3c5c-b6e0-7190618d031f | -11.93142 | -50.73496 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dd9ae8c-13ca-3fba-8101-d9a4eb1546bb | -7.90448 | -61.16704 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7e48ab1-10a3-3378-a88c-da91c06a3cd8 | -11.48908 | -47.34044 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 693a2d26-6d3b-32e8-9032-9a75bd7797f8 | -8.3873 | -46.29161 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 81bc8c3b-b5aa-3faa-8adf-18f13d08fa39 | -12.67945 | -45.02868 | 2026-09-24 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3966ec70-6b80-305e-af5e-730054d6d2a6 | -12.92045 | -50.90724 | 2026-09-24 04:46:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea3afdb1-1f99-39aa-83f0-181e46ce3649 | -11.28789 | -51.31729 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b9a0f5f-aa48-3fc2-8e16-b8356593dc44 | -6.31191 | -59.9474 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 314cd881-075e-37ed-a05d-001267402302 | -9.33261 | -56.81532 | 2026-09-24 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c58d3cdf-f25c-34a2-910a-d94964c7d0aa | -12.10104 | -52.55385 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7690f9a9-28a7-3c9d-ae96-ec72e602022b | -9.86279 | -48.50893 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76336c71-2a1b-300e-ad62-3269c316367c | -10.71982 | -48.7368 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fb6fc20-6bcb-357b-be4a-55e8484cd882 | -11.43717 | -47.40545 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8946c5e-2892-364e-b57a-f0393b454b61 | -11.6343 | -50.61028 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de3b7bac-3630-36ad-83ff-4a1a3b330053 | -11.79641 | -50.04286 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b532aa47-1072-31c9-8512-9c2a607fa7e2 | -11.95403 | -50.74643 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a703b865-b9fb-3792-afb7-051f971420d1 | -10.0789 | -46.01114 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 710e06ba-7072-3094-bb63-1844238f1101 | -11.93779 | -38.29132 | 2026-09-24 04:46:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 194f4d75-1a01-3cf3-bfb1-d18942801152 | -13.99338 | -44.06747 | 2026-09-24 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05deca65-a904-3e15-81e7-841d652ae31d | -12.13378 | -50.73893 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 06a3d2cd-98e9-3673-a318-7c849f6c5dce | -8.82188 | -45.92617 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a6dbb23-cc2d-3680-bb3d-64fe97d5b76a | -11.42982 | -47.40791 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5ad0f0b-1f89-3e4f-b6a2-e7e566f2e62b | -11.65321 | -43.48876 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| be57ce40-25d6-3ea3-9c2c-c29ab6820c12 | -12.13718 | -50.73951 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 493df1ae-15bf-3fe0-a79e-f1cf13bdc14f | -6.46512 | -54.99459 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dca9ad5-0278-3d2f-8a76-0658d7e06470 | -8.89939 | -46.81409 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13d61be3-3fba-333b-ae5a-dc26c548605d | -10.91224 | -53.9515 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8454711a-756b-33f5-9e8e-ea0fd5471be9 | -13.78309 | -54.07079 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d166b9b-ded9-30cd-9d0f-2219c73b3ffa | -11.12357 | -48.29926 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d5151f7-a340-3fab-a2b9-2038fe87274a | -8.27399 | -54.76848 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be7e4291-55e5-3ca2-8b1e-cb729407c778 | -12.15041 | -50.72272 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86bc7890-116e-342c-9a58-0aebabfb7d8f | -13.78788 | -54.06643 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cfa38a0e-79fc-3411-8aaf-ac7cb5077778 | -11.79699 | -50.03927 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea62bae1-3a14-3c18-bfc0-e9d88dcb807d | -10.70485 | -48.72356 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57005842-b750-34f8-af7f-9cbad7aff872 | -6.24252 | -60.03257 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51662263-1ad9-38f5-a66f-97b150d36154 | -6.68129 | -55.0471 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bc8a253-4783-3896-b572-5473d575ed85 | -10.33211 | -50.19598 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e73e68a-24c3-3a04-b71d-6e8922350063 | -11.23073 | -51.3801 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ce9599f-4480-3914-8f08-24db3103907c | -10.91007 | -53.94009 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b3cbba1-921e-3154-93f5-330f696ff3a6 | -10.09597 | -46.06674 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d299f06-8bc1-311e-ab44-22092930c66b | -6.44367 | -59.95491 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a82fb575-1e61-3977-ad82-95ebda0fbd87 | -8.59693 | -54.59501 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409be299-9855-3cb8-ac24-71d86a73b75b | -8.73021 | -47.60828 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d26b25f2-646b-3f2e-a771-1c502b93d4e8 | -9.59334 | -46.51351 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5c82070-0f58-3e14-9ce8-d383e0778cc1 | -12.14817 | -50.75594 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65f99736-8fa6-3da2-bfb5-5d1f951fa2c5 | -8.24095 | -48.21704 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ebe3579-c7b7-3696-97ec-4b06f203ba15 | -12.34809 | -48.19587 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3225f89f-63f4-3dee-8813-9c5786a595b4 | -8.59246 | -54.62027 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d48d838-21fe-39e3-9916-6ffa95456fd2 | -7.58986 | -57.66161 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a8bfb8a-7297-3a7b-9091-aa371705ae6f | -8.3577 | -45.59351 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67b3586c-7469-3034-b2f0-5889a7c343e7 | -6.34359 | -57.77608 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 900de557-001c-3fac-8b38-cedc687cb8c2 | -11.62804 | -50.60517 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 043c607f-6489-3f8a-bc8c-2313334e9e50 | -9.26083 | -47.3416 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README58.md)
