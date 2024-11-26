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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 439175f1-6a63-3d59-88d7-a47efd1d1c01 | 0.97407 | -50.12642 | 2024-11-26 04:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6900a0f-ef01-3090-b490-298407f44ab3 | -3.58976 | -50.3822 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5a092f7-cbc8-3673-a8a1-72cf25ef0b22 | -3.98532 | -48.05647 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00d7cfd1-530c-3adc-ac5e-958cfc2d7abc | -3.19078 | -48.43304 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d7f7d0a-6428-3919-80ce-55747f3136d7 | -3.49404 | -50.45758 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4968b2c1-e1c9-3e30-bd99-10365cbff53f | -1.1885 | -47.66639 | 2024-11-26 04:14:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de11c865-35f4-3703-a1ff-b3f229a97e02 | -4.54509 | -43.29173 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7a5e0d01-5ef5-3ddd-a75c-ff9b45ee0861 | -4.5374 | -43.2976 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fb079a0-68a9-3bab-be11-0f08cb0dfb24 | -3.47317 | -47.68808 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a844b8-45cc-3a13-8d30-4db77c0204b9 | -1.63214 | -52.77325 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 874d1136-69a8-3c0b-a8cd-367283173d4b | -3.96004 | -48.10846 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e01d99-917e-31e4-9e62-951600d63b6f | -5.9339 | -42.0804 | 2024-11-26 04:14:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64b70911-d3f0-36d7-b55f-101e04633486 | -5.06631 | -46.77399 | 2024-11-26 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9df556a2-c15a-397c-9127-69b739cf1f8a | -3.462 | -50.83968 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94590e09-fd37-3d21-9c82-49ca57827d7b | -1.82931 | -45.58626 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59a50a84-4a43-3cbf-b961-aef57d7769d5 | -4.24098 | -48.67254 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9f71056-6d21-3dd6-9772-7c69f808c621 | -1.82509 | -46.2851 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 458fe5b9-e937-3929-b215-e22f85b1d313 | -3.97253 | -48.05775 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6dd5c874-2b29-3b2a-a316-88a6ced5ab6e | -1.485 | -53.81044 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56a597bc-cb49-36fe-abb6-7cabd5939753 | -3.96435 | -48.05647 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d493eaca-333d-379a-8c98-c03074baf6cc | -3.91027 | -42.41241 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09b758b9-91a2-30f9-b1df-d9a6bd0f809a | -4.01305 | -43.25715 | 2024-11-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 438dc0c6-520a-3f69-af35-5fceff430463 | -2.33027 | -53.86554 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f157d80f-fbb7-348a-a368-38f48d89d064 | -3.18716 | -48.42845 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 758408b3-d91b-3298-ab69-121f771eb3d7 | -1.92974 | -50.58812 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b8ee0f-4320-3ba2-a15a-67e4139c4966 | -3.38564 | -50.1019 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b581070-7d42-3be8-a0fe-c0708c963344 | -4.31433 | -47.51619 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3c80a406-79c2-3712-b00d-531f649adff8 | -3.96835 | -48.08332 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad8e01fe-e2e2-309b-a87d-ec476ba172e4 | -4.42576 | -48.70948 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79665cfc-4496-3a33-80fc-39a0ca8a38c2 | -3.08689 | -49.21185 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4010fd57-1d4b-349b-b161-41772ca77cb1 | -3.76157 | -43.25636 | 2024-11-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0956131-967b-3027-ad48-6ff0f4060990 | -4.25797 | -48.72449 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bd6915f-baf5-30a5-bf29-c853281cdeee | -3.457 | -50.83894 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0bd63e4-dc37-3f65-ad53-774247bdb75f | -2.61144 | -48.36526 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c32cbaf6-353c-3ee6-86f0-40fd43a02130 | -3.96476 | -48.1053 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e380d6df-4e8b-358d-8329-88d995f20a00 | -2.7758 | -48.57976 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9da0eaa7-051a-3af1-a13a-4a0224bd507f | -4.9521 | -45.79301 | 2024-11-26 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39fc6073-5031-3ac4-86cf-f4473d336931 | -2.09752 | -45.97037 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29fea060-783a-3d86-8110-d08d3a80cb0b | -3.49798 | -50.46397 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6171a1e3-e959-3724-a15b-702cd18fc3c5 | -3.97776 | -48.05137 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0c31240-a63a-3ceb-b374-f99c3097c1ec | -3.47263 | -50.25787 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8d1821-3ee2-3f5d-9e96-ccc62d019ed8 | -3.8351 | -44.04207 | 2024-11-26 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e50797d7-7e46-3f8a-8814-4f5523fe5dae | -6.06734 | -39.18567 | 2024-11-26 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ef4839a-2574-329f-8b95-581817ac4213 | -4.36733 | -48.56107 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a6dcf33-9067-3de4-ab32-9420cb79086d | -3.46152 | -50.8426 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbd8945d-7e06-3b63-a8ea-b90de0197177 | -3.4405 | -50.27414 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c8474d-216e-381e-8d03-48c1c92a4310 | -3.98473 | -48.0601 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 774bf732-8969-37b2-8cce-fb22f0f49a0a | -3.96484 | -48.07909 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bafef54e-8c96-3ce5-aea6-21d5dd557c25 | -3.97306 | -48.08022 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b55ecafd-4c58-3707-bdda-745bb22e3055 | -3.39022 | -44.16684 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1e9a7e18-de88-3875-8c3e-4677b3741745 | -3.95721 | -48.0744 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a6773c0-2a29-3069-8813-c023e1cc22a0 | -1.5894 | -45.46257 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2f7a26c3-057c-383b-8716-40f4815bbea7 | -2.93577 | -48.01861 | 2024-11-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d988f87-6dd0-3b85-800c-5042eb5ac270 | -1.43142 | -47.32124 | 2024-11-26 04:14:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e3035711-836b-316a-b2e8-88199d1c567b | -3.96896 | -48.07963 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 820deb39-b332-3e51-a65e-25473e58d694 | -3.18292 | -48.42777 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 653afcbc-c710-3a16-ab3c-0509fe3c4c0e | -2.22325 | -47.72435 | 2024-11-26 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e213ab3-4a62-30e7-b111-bb8cff975b17 | -1.63545 | -53.30459 | 2024-11-26 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f40a053b-f109-3506-9f88-a667515ea8b1 | -2.93163 | -48.01794 | 2024-11-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dcd5221f-0a54-3a08-91c4-67563bcce3b1 | -2.5873 | -46.19758 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eaf5719-c755-3742-bf6e-d7912a1b8cc8 | -1.63055 | -53.87601 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d716213-28d9-3cf9-914d-f85f8aba566b | -3.97537 | -48.09185 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2101ed5c-d102-3c64-963b-8f0443c723e1 | -4.24455 | -48.59678 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e77f145-42ac-3509-8439-8c1521823abb | -2.31775 | -48.55452 | 2024-11-26 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262553d1-71d0-30ad-b6ba-1ceefc5cb408 | -2.7142 | -47.70545 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1efc3a7-f0d1-3ff9-9f80-f27779b55212 | -3.46092 | -49.96924 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a1c4b39-ec95-3f3f-bc25-b3d0560cfb9c | -1.82999 | -45.58206 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b095202-75fe-329b-b074-c96b90be70eb | -3.23136 | -50.31789 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2fbec924-1b30-3168-b155-ffdb18d6b067 | -4.38093 | -48.50342 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1b2c15-27d9-359b-a82d-a6f1c8d99bbb | -1.19433 | -46.20124 | 2024-11-26 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d544b6a4-5356-3e07-9f63-9b8e77df8325 | -1.70782 | -46.24094 | 2024-11-26 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a670084e-3c59-35be-a788-9f275f13bde2 | -2.40601 | -53.67807 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3dc7472-7c5e-38d0-982c-733553766e3e | -4.66232 | -47.95014 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6712b5e4-a2ca-31bb-a013-1c4742f083fd | -2.33103 | -53.868 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d154e12-51df-3a1d-a3cb-4055577cba56 | -4.37193 | -48.50597 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5342572c-3492-38ac-8f93-d11d219f924c | -4.46381 | -45.87703 | 2024-11-26 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b9eba6-9f83-38bf-9289-e152b5700ad2 | -3.46763 | -50.25896 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcecbe57-c7f6-389a-8adf-b7abc65988e9 | -4.50655 | -42.07619 | 2024-11-26 04:14:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4be11522-1453-36bb-b6b5-20a7f7c9100e | -4.31746 | -47.52178 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6de9c699-6a25-3719-a9ee-d60114f7ba5f | -2.18819 | -45.97094 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe58117-ea2b-371d-ac99-e70cbe17e1df | -3.91304 | -42.41637 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c66b88ae-4f9b-3605-a940-5a19c790066c | -2.69098 | -46.87221 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eb48865-c828-32c8-b984-50a2e862d22c | -3.97418 | -48.09915 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8cba6f8-f7fa-3ad9-a8df-8d98518a0a8f | -3.32163 | -50.31091 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f0436f6-24fb-373e-84ed-c42de046fc96 | -3.38089 | -50.10117 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80086919-ae30-3c7c-a783-04e87b53f6c2 | -1.79159 | -52.74537 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cbd0924-097d-3bcb-b8dd-db6e0df1502d | -3.18228 | -48.43172 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 619239c7-a72b-3e93-bab3-0638517b2617 | -3.27894 | -48.75312 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62690bae-8698-330e-b752-dc87774a7c85 | -3.70102 | -45.28939 | 2024-11-26 04:14:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4704c44a-c469-358c-b99a-2240f2c961f7 | -1.47083 | -52.29524 | 2024-11-26 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ff6a07-ce4d-37a6-8efb-1a42b03c2574 | -3.80903 | -46.59819 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49505af8-051a-347e-be39-2a2ce9da4429 | -3.96784 | -48.06078 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 804ef06d-e700-336c-90af-bc58162e98bd | -3.38514 | -44.17712 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a77f43c-0477-3b10-8be8-f6cc15d0deab | -1.63281 | -52.76909 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac7cdff-2e61-315e-a44b-1d930240960c | -2.93431 | -48.8255 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f226e6d0-66f7-341a-8d3e-6cb292592c9b | -4.53848 | -43.2907 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 247998b5-d1d2-3f31-abc0-4dff86f3db66 | 0.67937 | -50.80051 | 2024-11-26 04:14:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c172ca96-a080-3fb9-acf8-3698ca9fc186 | -1.56732 | -45.67521 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fb58454-82a7-3d30-83be-b1d7fc23e872 | -3.96373 | -48.06023 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05c4bb9b-7c71-374e-9d20-ad3ccc1666ce | -2.32744 | -46.12937 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README15.md)
