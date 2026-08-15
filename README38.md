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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e08cffc0-cd23-3e6d-bba0-fb4dac5e8809 | -6.85844 | -56.42255 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 774f9999-76c6-3274-a1a0-e6afa86dc5b4 | -6.61189 | -56.33696 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c87600f1-c290-3d51-9694-19ee71b743f4 | -7.55556 | -61.16927 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65b917ae-0cfe-370e-a233-bf99283f691b | -3.75913 | -59.42852 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b68822b-1b90-3b6b-92a7-7c1ffc9bb2fe | -6.83244 | -56.46331 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ae6cd65-883c-35c8-962c-cab9f0e9c30d | -4.10488 | -50.99472 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfb2fa81-167a-3422-bec6-3d87e7fb3e9f | -6.96299 | -59.28526 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26135fdd-0244-3c32-b38f-9a214f79b790 | -6.02114 | -57.82854 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b59dbed2-0815-33cf-baf3-27f150d99d3a | -6.97001 | -59.28967 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0957866-8ad8-3614-a48b-60ae88dd8e9c | -8.01995 | -55.13283 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92b5811c-a224-3a93-8696-852c05b286a8 | -7.55169 | -61.17221 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4addc4c-b51c-35ce-9f37-0918076162cb | -6.61209 | -59.05238 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd7e11d-cf0a-3d7c-98f9-a4a6f5545097 | -6.01819 | -57.82399 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1228711-c5b3-3722-b383-4545f89c222e | -6.85938 | -56.41943 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef5929bb-e815-31a8-a2ee-504923095897 | -7.41742 | -60.00355 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdf7135c-07c6-3434-a6d6-7e6378764432 | -6.79409 | -55.83748 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67803740-a55a-3109-9d49-82d11964d03a | -6.84878 | -56.43784 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3043fd2d-202a-38da-8de0-5a9c0963424b | -6.9655 | -59.2964 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb80f487-fdac-34c5-8308-a09adba7ffdf | -6.8555 | -56.41885 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcf98ae3-018b-37d2-91cd-d3945e4994cf | -3.24272 | -60.12603 | 2026-08-15 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5135c995-0cf5-3a34-a760-f9297b8b6767 | -5.49978 | -60.15003 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f61c3e37-805e-3ab3-8ae4-cc30c4db2aac | -6.72055 | -58.93638 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f51ad9-c3ae-3560-8522-4bd006d5421b | -2.64735 | -47.97564 | 2026-08-15 05:33:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2d097e1-961f-3ca9-a01b-4e0d9d0812fb | -3.59296 | -58.61834 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f3ec53b-370b-3021-89c5-80cd040049f7 | -6.60752 | -58.99155 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f114486a-4e80-3ff7-874e-ceb7140cced4 | -6.2078 | -57.76965 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 3924bab2-5de4-3614-a5d2-7ae5d2119bbb | -6.80192 | -58.7737 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a131a1df-35cf-3049-8d94-b31a4626f7d6 | -7.06417 | -56.65495 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04335002-3f4a-3da3-bea5-00b3ae185639 | -6.54336 | -55.17938 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db0368dc-116d-37a3-9736-2931ac0dc005 | -2.88127 | -48.85469 | 2026-08-15 05:33:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bda0356-d02d-3a24-a620-ee7e71ec1f7e | -6.8553 | -56.4171 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1493c58-1de8-3747-8e12-ab2484dffd49 | -6.60582 | -59.00257 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0f9676b6-572c-3b89-b801-885511bee32a | -6.61037 | -58.99578 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab0219f0-24ae-38b0-bd54-945ba011cf97 | -6.59105 | -59.00779 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6d4bec-2c30-3267-a24f-d33f2e6e2266 | -7.41797 | -60.00001 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f81d11-dcca-3cec-9b2e-e7c7feabc4cb | -6.60185 | -59.00572 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6dd03783-f316-3097-be9d-4a954d0ce6a8 | -6.78535 | -58.74409 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14062059-c394-3bde-be53-653298e8c054 | -6.6058 | -56.35107 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82d8e4ad-60de-3e40-bb29-8a720d874b07 | -7.69138 | -55.15788 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ba253cf-d632-314b-9da0-c0323c40873b | -6.79253 | -55.84796 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc1a3b8b-8520-35a0-8699-15092f63f9db | -7.39269 | -59.9964 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce57ff8-23fe-3cf9-940e-65a836dfbbab | -7.4029 | -59.98677 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce943c45-9d98-3f8a-b693-d137ac02dc56 | -7.5528 | -61.16527 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 688268b7-dad6-333f-a176-0653c8c81377 | -1.59081 | -50.44322 | 2026-08-15 05:33:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e83333e4-8785-31af-9773-de4cec896c4c | -6.6386 | -56.26537 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df55f0b-a658-30d6-9259-8cbe4f39f507 | -6.70116 | -58.94863 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2818b70d-9bb2-3909-bac5-3f97d3e24939 | -6.61493 | -59.05655 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85b021bb-6bf3-3733-90c0-c7e4549d84eb | -6.78903 | -55.84386 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b048f2e-ade5-3dd9-b075-21bcf24ea3b4 | -6.83056 | -56.42332 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfd74cee-08b7-373f-8556-261323914b25 | -6.83444 | -56.42393 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05205f22-cc0b-3531-8f66-fbcc048e7f64 | -6.96435 | -59.28134 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33c70b0c-ddcc-3cff-aabc-82fea023bf92 | -6.95732 | -59.29926 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f10e128-9ffe-3a5d-85bd-e8e6a8c0863d | -6.78851 | -55.84734 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1873e3d9-e8db-3fcd-bb48-17d332808ca4 | -3.97315 | -49.45944 | 2026-08-15 05:33:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a91a1134-7dcf-36d8-860e-b5a1b89b950f | -6.6098 | -58.99945 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e46ecd4e-31fb-3e87-acfb-0ca6e31d443d | -6.88626 | -59.01838 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8150a98-f69e-3937-8356-2fa3dd75caca | -8.02333 | -55.12197 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb4f1383-9b49-3a29-a4e2-f80c8522fbf6 | -6.53501 | -55.17805 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26109046-d8ea-3062-a370-5765c5f2499e | -6.85327 | -58.96031 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 046f6452-057b-3e1e-a7a2-806743f43d80 | -4.11022 | -50.99576 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6ba18a0-1dca-3f96-9ddd-e522f5d5b963 | -6.61378 | -58.9963 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b249f566-a698-3f3f-8bdb-4b7c00543b3b | -3.62409 | -60.32429 | 2026-08-15 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff60fb0d-9a05-3e10-ac71-031d861c6f36 | -6.59805 | -56.34983 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b404da-fe1e-3659-80f1-fde3fc1faac1 | -6.70458 | -58.94913 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42cfb643-7acd-3455-a2ee-50f91fde3361 | -6.62175 | -59.0576 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f914f2e1-92cb-3e6d-a393-8df8bb4d5bdc | -6.8608 | -56.40966 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20abc739-f84d-3b5e-8d87-7870a60c2432 | -6.85621 | -56.41397 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ab32ca-eb75-31ba-993c-87d6bb031b96 | -6.78501 | -55.84324 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0f1e1f9-884d-3d93-a91d-4978146dfc31 | -8.01626 | -55.12787 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eaf288e-55fa-3ca4-803b-4a7744a7bdb3 | -6.61777 | -59.06072 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fbdd359-042b-3c0a-83c2-8dd144b72807 | -3.9308 | -59.32351 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d22d3d6c-75ae-3f99-a788-54391c3cb392 | -6.65632 | -59.10425 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a78b522b-698c-366d-88f8-1674457bf26a | -3.59691 | -58.61526 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6fb483-f739-3554-b934-55af0ed37d68 | -6.62118 | -59.08374 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da3d56f5-8f0d-3ce2-a035-ed96e0c9a9f8 | -6.61834 | -59.05707 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d96e392b-8a0c-32ca-96c7-5b6a159366fb | -6.61607 | -59.04925 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddb28913-1b9e-350c-8f7b-173fcf2c1a83 | -6.96379 | -59.28497 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92c37f6b-0a29-3f7a-b3f7-efe08ff60ec3 | -6.85162 | -56.41827 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7d9af3a-1c8f-37f2-aa5e-86240eb02149 | -6.84219 | -56.42512 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 561545cd-9408-3534-9689-ef8a59bdaa14 | -6.96323 | -59.2886 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b09f7990-c9fc-3b49-91a9-86d572d55826 | -6.96606 | -59.29277 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcf21cf3-36e9-38f5-b150-ab791c2a4406 | -6.60876 | -56.33136 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 874e6361-29da-3faf-928a-349c72483382 | -8.02484 | -55.12916 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5bb35bc-6695-373f-9ffc-ebe3d4c188c7 | -6.64868 | -56.41348 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76540ac5-fb33-3f08-8219-404c54d9c6f4 | -6.85269 | -58.96402 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31a94b1f-9175-3617-9c26-0f3d7da61792 | -3.24604 | -60.12655 | 2026-08-15 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfc12c82-647f-314f-9737-7cd12e2ef8b0 | -7.42131 | -60.00053 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2181f35e-39b5-3db8-9878-ffdee8adeaa3 | -6.95111 | -59.29457 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b205e9-d236-31da-8467-bed534326a72 | -8.02856 | -55.13384 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 214addc0-4b44-3906-8b84-74adfaea023a | -6.58764 | -59.00725 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68c3cfb-f3ea-340a-8e8b-a22b0a718845 | -6.85604 | -56.41224 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f325180-f8d0-3501-8ff7-ade03cff4531 | -6.96495 | -59.30003 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dae2f026-51af-32e6-9f14-7e0dae210816 | -6.79531 | -55.68959 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56cba227-4124-3d97-ae2a-7e1332f800a2 | -6.54393 | -55.17549 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7d1b8b6-26cd-3a88-bc5e-0d7fc1d18d65 | -6.59198 | -56.36394 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0aa02e-2d9c-368e-ab03-87801158d5bf | -2.41158 | -51.83677 | 2026-08-15 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 460b31c9-dc01-3682-8b10-46207630e843 | -6.70914 | -58.94222 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aaba376-5a90-3346-9d78-865a000b09d1 | -6.85381 | -56.42691 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8556b0d-fc2a-3bf8-974c-532ebbd32f7a | -6.96889 | -59.29693 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dea6c55e-bffc-34b1-9e12-f5274cd7950f | -6.95564 | -59.28784 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README39.md)
