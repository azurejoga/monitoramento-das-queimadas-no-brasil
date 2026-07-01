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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afc0dc6d-278a-32f1-bd2d-acc5cc9a4fa6 | -10.76937 | -53.53975 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51ef2bf3-0f46-3c14-a8ae-ee8b7030ebd3 | -8.50889 | -50.15166 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e7ee61f-6811-3e8b-80cd-4ab4ba626505 | -8.85056 | -50.18362 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6199c637-1720-35f1-8d3a-6884bf0d14b4 | -12.21962 | -56.56301 | 2026-07-01 04:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7abe38ab-5773-3a8c-8534-a671f11c79cf | -10.65709 | -54.5417 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c630b2d6-5637-309b-a829-de2004bea15f | -7.47615 | -44.74681 | 2026-07-01 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8dbbc9-7bfc-374c-bdc9-f091a69deca2 | -12.4545 | -46.91962 | 2026-07-01 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb7abeb7-bf36-3b7f-be79-54255cf3a561 | -7.71011 | -45.93716 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3b41673-a3f5-3fdb-990c-6531dcadb05e | -8.135 | -47.88221 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba15cf3e-20f0-39d7-a987-145674060754 | -12.76534 | -44.48094 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4e2659a-4cb5-38de-b3ff-45f9bf4209b1 | -7.71067 | -45.93363 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a00eff2c-c739-31f4-a657-08a2e4a0259e | -9.60714 | -56.93588 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf4a8f05-79e7-3420-848f-51788e88618c | -11.43692 | -55.92077 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c16cd290-bd06-38db-bb77-840a26a74937 | -11.94357 | -57.04785 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e83fa9e9-5497-3143-b207-1c12f908029c | -10.76333 | -48.35595 | 2026-07-01 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e69debe-6d5a-3cfe-b802-8609fc0a2021 | -11.90652 | -57.38843 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2b8eec7-17c6-3d69-8340-23182f488af1 | -9.20444 | -45.32741 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54c58fb5-7556-33c3-ae51-8238f0c6af4c | -10.12929 | -52.09576 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c076e1c2-dbc0-3ecf-abcd-e34420206ddd | -8.80427 | -47.48359 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16ef8321-122a-3960-a69e-c46f322c4029 | -11.2165 | -54.33704 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cc1cebb-e60a-3876-a808-00a0526557c6 | -10.9196 | -43.04883 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 80420eea-9335-3724-aeae-8e0380239c49 | -10.38677 | -49.58648 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d03f28c-1659-3a86-9274-5de733d83f8e | -11.4299 | -56.06337 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 2066ea8f-847d-39f1-89fb-5a75cffcfd50 | -10.77367 | -53.54051 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 307ca821-a9dc-3c17-b04d-cea07e554a12 | -10.38129 | -49.59053 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f883c816-b439-39f3-bdbb-152f66629144 | -10.91888 | -43.05377 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 4ab884c8-1d5e-38ee-b73a-dbb28153c3e7 | -9.20387 | -45.33114 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f169a118-c7cb-3dc8-b49d-6bc13a55f4b0 | -7.4727 | -44.7463 | 2026-07-01 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d082d4e-069c-3897-bb0c-a7731c01f2c7 | -9.21071 | -45.3322 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef309fd1-ae44-3c0a-9fb1-c2c51daeaf21 | -11.49709 | -47.42233 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5545c92a-ade6-3df0-8afd-a94e52b50a7d | -13.88458 | -45.08962 | 2026-07-01 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ef00018-3cc5-3c6e-b6f8-865577a0552f | -10.6617 | -54.5425 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f187acdd-ef5a-35fb-9c46-3a8a6317d74c | -9.20102 | -45.32689 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3f97a16-91d6-39ec-b296-1c0e7d3e1fcc | -7.71401 | -45.93415 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a35007e6-d44d-3687-bec7-83c2916d06ae | -9.5989 | -56.91898 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1b9d4ab-e63f-3225-9945-47fbb12951d8 | -10.5965 | -53.45417 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e156a17-fae2-3d81-9675-7aa73a802ded | -12.83132 | -44.35394 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| a4acce2e-384a-3b32-9c8a-cdb88b6b4caf | -12.83936 | -44.35063 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 64e044e6-6519-3875-9633-06e05054f0f9 | -10.66804 | -54.53376 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a9b0f3f-6f69-3852-b286-345fe75216d9 | -12.82761 | -44.35337 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 87ff92cc-6624-3f3c-ad48-525314b03cbe | -9.69625 | -56.10111 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bed260a2-3d3e-3840-91b0-f882ad05af8f | -11.53928 | -46.65422 | 2026-07-01 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcfead3d-1f03-3f3d-93d1-5934aef0bc15 | -11.43321 | -56.07341 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 594b6858-148d-3c28-a83d-654ed874d021 | -8.34858 | -46.8166 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f39fec74-8d57-3d0b-ba3a-e2ef6cd13812 | -9.17594 | -58.06357 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 181a15a9-021e-3e52-ba95-2cc82bc3e6eb | -11.42042 | -56.0585 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a23235ab-3a3f-37dc-a3c0-85f07ed5ec4c | -11.314 | -54.47084 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 431d8329-a4c2-322b-94ea-9b5caecac86a | -11.90807 | -57.38464 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb8b1614-2bf6-3d42-9117-2f7c884725fd | -12.4443 | -49.57945 | 2026-07-01 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4e5d9b9-da62-3b7d-8c34-83c6134f6918 | -10.78615 | -53.55363 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc9c7fa-cf74-303e-8a1a-37c280530efb | -12.76278 | -44.49845 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| bece3790-7c61-3ddb-9514-6be8079ccf9c | -12.83629 | -44.3456 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| bee2706b-6b81-34c0-abd2-492619fcc948 | -8.60023 | -48.01551 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726a5f4a-fe64-3f9e-bbc7-55c091a65ffa | -10.92278 | -43.05434 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| fd31b37a-4843-39f8-9dcf-7ee8365b155a | -9.67955 | -47.02583 | 2026-07-01 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7891def6-8dec-378b-97a3-71709ad56a23 | -11.30445 | -51.40221 | 2026-07-01 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 068e51c0-2834-3ba5-95d3-295e1e8e9450 | -9.75069 | -49.04116 | 2026-07-01 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe790e41-ec3a-3bf8-9d6c-65e08de43347 | -10.90793 | -56.85493 | 2026-07-01 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b50ebd92-1cc7-34a7-967e-65c1926b445a | -12.39135 | -49.8179 | 2026-07-01 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba6a499b-1c6a-3e7f-92e5-7a276e2fb646 | -9.67623 | -47.0253 | 2026-07-01 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f619c75-5e93-3a4e-b0b6-9ef1430ff457 | -11.54585 | -47.45909 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ea7d5207-0256-3028-a30e-c37cda5b1846 | -12.45785 | -46.92016 | 2026-07-01 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e09d0ba-6070-39c1-bd20-4b3279b2a11e | -11.84516 | -45.52013 | 2026-07-01 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68dddc41-bb92-3f2e-9fc0-c58c5f621855 | -12.76902 | -44.48149 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf27749c-444a-3de2-a921-c1af154f1903 | -10.12534 | -52.09508 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b835e1f9-487b-34e7-a3d5-2872296c75f4 | -8.05656 | -46.71641 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13069ebc-3682-307d-bed1-cca33da4adda | -12.46072 | -49.58611 | 2026-07-01 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff955000-1a47-35da-9ed0-ec070182d812 | -7.00966 | -50.07497 | 2026-07-01 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e58aae5-8bee-3474-bcd5-cb8b27f276d5 | -12.52733 | -48.28883 | 2026-07-01 04:38:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0d3f904-33a2-35fb-83b3-b63a24be68f1 | -12.82888 | -44.34445 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| eed50762-bddd-39cf-9727-09b07635a6cb | -12.66805 | -54.58373 | 2026-07-01 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f9296bd-c3b2-3512-9f87-bf78c9d99071 | -11.54264 | -46.65474 | 2026-07-01 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 656dc94b-f634-3267-ba3c-ad95a95c3ab1 | -9.17723 | -58.07083 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c397fdf-3416-3f10-ab3f-e054668b1a3b | -9.69044 | -56.10337 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0d4e50-dbbc-3658-bf59-5d1fde68a46b | -10.3833 | -49.5859 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f74685ff-7cc6-3044-974c-fe1b2bcff6bd | -8.50328 | -50.42591 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f01399b7-5b25-3896-bbda-6f97da4e4f3a | -9.16916 | -58.06682 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15be86c4-8c76-3127-b944-d30c4549d12a | -8.05989 | -46.71694 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a3ecfc-1c88-3f44-bc97-fdc794b0eeea | -12.05087 | -55.45721 | 2026-07-01 04:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d0a4a8-9c6d-3f30-8618-093cec993a5e | -10.4413 | -49.57989 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e020045e-4d09-390d-9b45-c00993f4076d | -10.38266 | -49.58974 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84a204bf-3a29-3555-b8e1-3d0b6bfb9a5a | -10.9235 | -43.0494 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 49d2d2ea-fc4b-3eac-9d7e-3da7024bda26 | -11.90333 | -57.38008 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f28f41b-fa21-3d25-8b83-0c81f8bb426f | -10.80675 | -49.33617 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a6aefdb-428b-3e14-b167-ccb22d2e10ea | -11.91965 | -57.38315 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 274300f5-4b2d-320c-a447-45fa01fd6886 | -11.04422 | -56.9212 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd67fe29-39c3-3993-b119-8b75a0a62b5e | -9.97871 | -48.24212 | 2026-07-01 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 059b3ce0-6dda-3581-9750-b854ada958a0 | -13.72568 | -47.87447 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fda7fc7-ea96-3546-a81f-eccc219a0f92 | -13.47809 | -47.87735 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d432946-39ea-3d85-97e6-93886a6ab5d3 | -8.59746 | -48.0114 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b7eaaa86-3a03-3827-9ff3-86948ae5a08d | -10.85386 | -56.65783 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15b695a3-0ba4-3005-ac85-dd549c457d6c | -9.17808 | -58.06647 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3444e325-c259-32a9-b8d8-11bb52114f7b | -10.38192 | -49.58668 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 968e4d3f-b78d-3fe0-af15-b97218f9ec08 | -10.43939 | -49.59141 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23add1e-5fd2-3af3-884f-a24f79c248be | -11.43435 | -56.06739 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e0c6f957-af17-3918-9ca3-286bc8bc775e | -10.59723 | -53.45012 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 718c46b9-eddc-371d-a3eb-222546d96418 | -11.41985 | -56.06148 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 8459635a-bb75-3395-9e99-f57b45dfc219 | -10.77295 | -53.54461 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bbce9ef-763a-3a90-809c-a887e0702883 | -10.77798 | -53.54125 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f014ed62-2c00-3911-a762-6ce85d72a40e | -10.68184 | -54.53628 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
