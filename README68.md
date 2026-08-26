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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71c8f205-645b-3b4a-88af-af8b8258f466 | -6.4118 | -60.06343 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84a36fe2-7c97-3fdc-9d82-de323f16724a | -7.02359 | -59.23455 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac64f82f-a091-3317-b3d9-7692baedd616 | -6.61009 | -58.38709 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92aece0f-6f9c-35cb-97a9-2e1a47a88f1e | -6.63916 | -58.51487 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 272968a7-219b-34ef-8d81-22485e3cf33e | -8.17449 | -54.95986 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3fa9773-8be3-32d8-8f5e-5a7df40b465e | -9.12985 | -57.56328 | 2026-08-26 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f5fdf4b-4f02-3c64-a16a-c6371dd28cfb | -6.69975 | -56.15228 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 313543f9-bf06-3497-9964-bc8c36002fc9 | -6.85879 | -59.40987 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e8c02bc-11a7-3148-9dfe-11264952cebd | -6.93159 | -58.94828 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8084e6af-abbe-3c08-b2ad-e0a9827be902 | -9.10497 | -60.90262 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ba81537-320a-3e87-99de-0a9e0634a9f8 | -7.52167 | -61.37764 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 21c4d9fa-c65f-3db9-babf-0283db544b33 | -9.06871 | -60.43771 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 367457b8-cacc-3440-b61d-572d0b59562e | -8.63944 | -66.78639 | 2026-08-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6572523-e184-3620-84af-9791f1f5b722 | -7.02925 | -59.22655 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff080b44-5307-321d-87ae-68153a9b9f98 | -4.06217 | -56.33793 | 2026-08-26 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c5c115d-b2a8-355c-8ada-3829e00ccfef | -6.6313 | -58.50396 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a07de213-3792-3da0-ab1d-4ae0cb8027bc | -7.02042 | -59.22512 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 878f6b38-20a7-3462-8bc3-6acc56e2281b | -6.53831 | -56.26159 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8556d68c-fbe1-31ac-8231-741c0e06d013 | -7.79104 | -62.3926 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a04db282-0cb7-3efe-a04d-2285cd79aeac | -7.0274 | -59.23956 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5666393f-5c54-3eae-9c98-ccc9ec5000aa | -6.86814 | -59.40685 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba34954-8595-3149-990e-b31e04bd8b73 | -7.3974 | -55.16166 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41fafd14-4890-3c1e-b56d-dbb00d822966 | -6.95501 | -59.08643 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c8203f0-d46e-3504-a77f-844532196fd0 | -6.99536 | -59.27587 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c68f2fe8-c9e2-3996-97e9-08620ad7c432 | -7.39687 | -55.16556 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cbbf0df-d4f1-39d9-8683-ce43e617a401 | -6.84206 | -59.46283 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d4c416-8431-311a-8829-31887da23621 | -9.10904 | -60.90321 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d50110d-2a40-3a6c-b7e2-5c2a91419395 | -6.81215 | -58.61213 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01624eb9-5c51-39f3-ace7-724569570748 | -6.63661 | -58.49991 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d037f4dc-a57e-3203-9552-f5b73ee562fb | -7.56359 | -61.42595 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a273d74-fce0-340c-966a-c5e41b580193 | -8.82047 | -62.31799 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2531f38c-7ecc-3040-8d5a-fb584ec4d585 | -7.32246 | -64.69613 | 2026-08-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26f173c3-c4ee-35ee-9244-6a67a58eafab | -7.54005 | -61.36058 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91e24273-97f5-3b93-8fce-c664736ae119 | -6.14441 | -57.70643 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b34c53ee-1ee2-3c0f-b4aa-3e2d38be0596 | -8.56762 | -54.81712 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18b685f5-f48c-393d-a62a-6a132c1132af | -7.80729 | -63.26218 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bd50a92-a519-3d51-9b81-5ba2b292d83a | -6.41236 | -60.05968 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c736fc2c-9128-31ba-911c-633e60ea894f | -8.15278 | -54.9859 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 844c648d-57b5-32bf-8407-b0cf8a409f9c | -8.65038 | -62.89382 | 2026-08-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fba5ff69-aa56-3139-963f-38ea95036af0 | -8.81852 | -62.33144 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e0b5e51-8279-3aa1-9d17-845f6283540b | -6.64658 | -58.49634 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5a9928f7-25a1-3a8f-908f-6f9a84dfe8d5 | -6.50612 | -55.22625 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 272453d3-706c-3e9f-b45f-0c9cf605ba7e | -6.80687 | -58.6162 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cec73b4-88de-319d-adce-b7523229b3ab | -6.94099 | -59.08889 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47d8a1d2-96d7-33f9-80ee-ca15f5d9d6bf | -6.98968 | -59.28384 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d665162-7a30-35c5-b555-4b1d308307c5 | -6.99587 | -59.23915 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa4ec4c9-65ed-3bf1-bc92-d1cee9477f3a | -6.76017 | -59.44654 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dab9ad2d-e4b3-396b-9858-f8b42767de75 | -9.46946 | -56.91268 | 2026-08-26 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6c4881-375c-3eaa-91c0-4d5dd771eb6e | -7.52408 | -61.38794 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 6aded90c-8a56-3afd-a53f-2ca6f0a6ddbe | -6.933 | -58.95086 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79f18dc2-253e-3be0-a74e-a7a88997f901 | -7.62531 | -63.36732 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8e5d1d1-8426-3892-b61d-ea0f70811a70 | -7.10501 | -56.5647 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f50455bd-f01d-369f-98d8-ee415751dbc1 | -6.64124 | -58.50056 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1bab9171-0787-3ce8-ba6d-d77f5466289f | -6.94036 | -59.09337 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2ca4790-e93f-31a1-9c16-b7e3d6b2f11a | -7.06404 | -59.23602 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2559dc8a-ccad-35ab-bf6b-6535d9d9361f | -7.37532 | -55.19295 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b521561-05c0-329a-8aa5-952ea66810b1 | -7.47841 | -61.37615 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df4b96f0-6a51-3e1e-a388-25c8d54d7024 | -6.93641 | -62.882 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa6e15a1-be32-3a4d-9e38-bf2704fc31af | -6.63337 | -58.48966 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f5ba3e1-7955-3175-876d-38c321078e56 | -6.99219 | -59.2654 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 921fcccf-65dc-3e79-ad50-23e58218ace2 | -6.97965 | -59.26026 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90d6af7a-ef6e-30d0-ad87-afac1580b596 | -7.03367 | -59.22721 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b008b1f5-9cce-316c-93db-51ba6ec1894f | -6.14359 | -59.91758 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc2ec5be-8e5f-3371-8622-de0056d81208 | -6.12635 | -59.91892 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e70e226-58d5-356f-82a6-268d477581b6 | -7.52794 | -61.38853 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 13bbcdfe-e119-3419-b63d-3e701d78075c | -6.71825 | -59.44984 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29ec099c-93d9-38f4-898d-2c387ca48222 | -6.61881 | -58.49232 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b9957f8-9fd7-3ef5-b54f-6e61e4dd2841 | -6.91692 | -60.06969 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14354b08-4fa2-33e8-ae35-9cc9243f75ca | -9.46057 | -60.53429 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf94d85-f576-35eb-b6a4-6e66e3d8c22d | -6.99221 | -59.26669 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9ffb48e-943f-3edd-bb4a-f43942838f53 | -6.99526 | -59.24345 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c0c5a0e-e420-350e-a3cc-686646fce1a4 | -6.15739 | -53.68454 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc919c9d-7b63-3f55-beca-d441b416df15 | -6.99663 | -59.26731 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0ded52a-16bc-34d2-8f9b-1c05e1a7d2ab | -6.144 | -59.92464 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97c0a1e6-9908-3fef-bf16-30a89a88bace | -6.61147 | -58.37737 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4a5eba7-3548-3ca4-9ce1-2bf0ce02cafb | -6.62668 | -58.50325 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2449a929-6637-391c-8a3e-c83c71b6a491 | -8.15879 | -54.98655 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 501fc641-fe45-3e99-9e76-fe83be0c6e75 | -7.56114 | -61.41568 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95f11822-47c3-3c1f-b7a1-81dd2006ae6a | -6.30846 | -53.57489 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0f30f12-bc62-3d68-b59c-4a59ac0fb5f9 | -9.59609 | -61.00977 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac5993b3-3d93-3668-bc53-b5ecbe9ad844 | -8.21928 | -55.01147 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e97d737-c2bf-39e2-b18f-4cd8559fee30 | -6.13223 | -57.86448 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a315a5c3-dd18-3cec-a2ee-d40345a792e5 | -6.99158 | -59.27096 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8933c67-1973-34cb-ae00-f097ea1e0d0a | -8.63612 | -66.78586 | 2026-08-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd41640b-8898-3589-af0c-b150e3db091e | -7.45781 | -59.99899 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4d6b9b-2032-338d-8ec5-1424eba6f84e | -9.16982 | -58.33239 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 205ac665-e3ce-3694-8445-0a05622576a4 | -8.5686 | -54.81438 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9749e4f0-81e5-36bc-b46f-d40eda20e020 | -9.60324 | -55.11063 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| aed11f96-8ce1-39b0-b640-a209a67daf0e | -6.63524 | -58.5094 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f4f4acae-0772-3f7d-8b82-48b0d228ff8b | -5.77052 | -57.55846 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a08984-4283-37db-8a5d-03f15b2e59e6 | -6.78346 | -59.74122 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61c15f22-94d7-3612-98dd-4879862ce511 | -7.21055 | -60.61778 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f29aeb-f8f8-353b-86da-09bc8255a4f0 | -6.71563 | -59.12712 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59bff2a0-7c44-33e5-9fc0-221d60d490b9 | -9.17184 | -58.33133 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25e7a6c-1fb7-3e4d-b3c9-a37eec8ddb37 | -6.14454 | -59.92086 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91d5ae76-bbc8-36c2-88f4-b8bd61bb26f9 | -7.02483 | -59.22584 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06ff0ef1-16bc-3abd-a432-d2f1f39dd3bc | -6.33148 | -54.74377 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 427068a1-0212-38e9-9c4c-25f425fe9522 | -6.79413 | -59.8157 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84b90719-a613-3b6e-a4a0-c4c3506db3ae | -7.07098 | -59.21928 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 7448a94e-b52f-345d-b760-f88d2de418a6 | -7.11079 | -56.56218 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)
