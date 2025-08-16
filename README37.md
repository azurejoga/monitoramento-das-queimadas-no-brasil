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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9d1e697-77db-3bab-8207-ef00fb84f03e | -8.80081 | -52.07499 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ba506b9-4124-3af2-988c-5b2929ba4108 | -2.91469 | -48.30283 | 2025-08-16 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5362d6-f52a-39b0-8f04-d7b625bbfdb2 | -5.64457 | -46.47158 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d40c6cf7-e89a-36ad-9937-d43a7c7902e8 | -7.59925 | -45.20752 | 2025-08-16 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fe9452c-72f6-3686-8d5a-19814e5a23e5 | -3.56971 | -49.50498 | 2025-08-16 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae6a985f-1939-3461-b725-2cfa4cbafe0b | -3.98487 | -43.24159 | 2025-08-16 04:32:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 855bab36-add1-39d2-b98d-36d0f3158928 | -8.16475 | -45.02522 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d5ba5f1-f032-3bdc-8613-eef6e927ab35 | -8.09147 | -54.98829 | 2025-08-16 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f29c2d6-80f5-3588-bdec-e7fde26c89ad | -6.55811 | -43.03453 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 7838482e-df6d-3bcc-9715-fba43c7aa0a4 | -8.38392 | -47.01654 | 2025-08-16 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c64df6e-fee7-3966-822b-cfd16f4d7d65 | -9.81853 | -48.53166 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f33e435d-da66-36d0-bac9-1f528be3c9f7 | -6.78286 | -44.35453 | 2025-08-16 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 156fe011-45f0-36cc-861e-0a22b5241325 | -6.86312 | -42.80307 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad1c1e1f-4309-3d15-b115-4f4512466bde | -3.82898 | -47.74003 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fc4fce36-beba-3789-bc0c-33fd447eda66 | -5.61171 | -44.80035 | 2025-08-16 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34b0df81-5d28-3e53-b687-2e9363fc6b69 | -6.66976 | -43.76705 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 187812dc-6bfb-389c-bc17-a0e8c3ae4ecb | -7.94984 | -61.75656 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1b880e1-3266-3b34-a51b-b18f2a0420f0 | -5.59966 | -45.37603 | 2025-08-16 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fcbd9c5-b376-366a-9615-097d1100e448 | -6.14578 | -57.93747 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70aade36-7165-3c74-a5aa-18ac0bb1cf35 | -7.8189 | -61.33115 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66f3b314-5853-3914-8fb4-bae61a7ee1e8 | -9.80972 | -48.54456 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab654eea-cada-34e1-9886-5347348e5c5a | -7.52771 | -61.32166 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad854d3c-8053-34bb-803f-c17182eff751 | -5.75367 | -46.66663 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 128ca192-bf31-3634-8d5d-0bfcdb27b154 | -6.67046 | -43.76224 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaa5948b-98ad-3d1e-b51e-b25686f97b6a | -4.91764 | -43.25618 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d7588fd7-7ac1-3b7d-b0f9-bdf0135004a9 | -7.52537 | -61.33381 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ca33b1e-c23a-368f-aabb-b51c60da14f1 | -8.16539 | -45.02098 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47bc3ddd-c528-3122-bdc6-bf63d39159f8 | -7.52529 | -61.32715 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3688ff36-2b59-33bd-8fa2-212c369c3439 | -7.07601 | -44.9363 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ff7d23b-6fa7-3686-a17e-a3d62c902fd6 | -3.44501 | -48.96495 | 2025-08-16 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a99203ce-f27b-3709-8c00-c49eefb59b84 | -7.15042 | -44.38738 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ad3e30-9290-3ceb-b377-694a47c9215f | -7.36443 | -43.83081 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3174b438-7c01-3fbe-962d-c1352fb57e06 | -10.24057 | -48.30844 | 2025-08-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 924815fa-0558-37c2-910c-7b7cf9fd1333 | -7.40496 | -44.88622 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c901a889-c490-31ea-a0b1-2f2e03d93fa6 | -7.53092 | -61.33463 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45461b3b-fcb9-3bd5-ab89-b7cdd74cc3d0 | -9.81522 | -48.53114 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5318512-3b6e-3567-ab6b-01c45fcaf9cd | -4.91306 | -43.26043 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| b88629e8-f7d6-3079-a916-74450b94adfb | -7.29454 | -46.03854 | 2025-08-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5236c2e-c959-3ee4-8dd3-1dee12ea8f9a | -5.75981 | -46.6712 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9fd3ac3d-c843-3389-91fe-4f8d5adaafdc | -9.85152 | -47.81756 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f57fa0-abef-325a-bd4b-3e0452505bd4 | -7.6661 | -42.23238 | 2025-08-16 04:32:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f6dc6f22-65f7-3aa9-8dd5-cefb05dba098 | -7.42255 | -44.61626 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c45bc584-a868-3009-a6bb-ca138470189f | -6.94245 | -59.55108 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbb846a5-23da-379f-9ccd-c2e47e1936b8 | -9.6985 | -46.26491 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c92ee33-a6ad-3bc3-a49a-e7df9134cc58 | -7.94189 | -46.81963 | 2025-08-16 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09ac2751-f87a-3e53-9bb4-d831f57ed8db | -8.16112 | -45.02463 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02f5ec75-55e2-364d-9749-344d9e8f2f8e | -3.82291 | -47.73555 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e54a3651-b117-371f-9fcb-f9f969930fbe | -7.39028 | -44.90998 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 706afdb1-a904-3590-95d3-aa250e380568 | -6.93977 | -59.53091 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5abb7522-a906-3402-b7e8-8866603933c7 | -7.3939 | -44.91059 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d54b9496-0bb9-3f2e-89f2-abe7ac58c1cf | -7.38176 | -44.91733 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d166573-2ecf-3cde-b1ed-3084a26efbfb | -4.19085 | -48.22293 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0229c7-a756-31df-9b4f-92b94126f7ae | -6.94682 | -59.52715 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3076e3a8-cfa5-358b-aa2a-10e1a2607081 | -6.5145 | -44.21808 | 2025-08-16 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f48fc7a-ec75-3cce-9a92-9033748ed48d | -6.70318 | -58.82406 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b177bb8-6a1e-32dc-9f8a-acc3396343db | -8.80526 | -52.07095 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14d20fff-0eb3-3a57-a63d-a5d077eb3c40 | -7.51978 | -61.32635 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2a8564a-b326-389f-9591-65f3fe0f23b1 | -3.81752 | -41.57742 | 2025-08-16 04:32:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bfa9bece-24b5-3d6d-99ed-f87bfec5e999 | -8.17266 | -45.02213 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a8117de-9595-36a7-90f8-f81bfff36d63 | -10.32703 | -47.72753 | 2025-08-16 04:32:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8695b935-5343-3187-a988-1ab20c6c7f5d | -9.70081 | -46.27328 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3ad261b-694c-3337-a213-afe6007ec414 | -9.18129 | -45.32329 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 201c7688-b352-3a52-9de8-afc4ee670d1c | -7.25024 | -57.62787 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4201afb-a602-3431-9c96-a911ba7b1b24 | -7.42081 | -44.87962 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1dee21-41f1-331f-82eb-85b4bdb50741 | -9.96462 | -48.33686 | 2025-08-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf75ffcb-c8fc-3db7-aa78-f15add3c7fc0 | -7.24483 | -57.62687 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff463180-0a96-35df-90d0-8f010fd76ca5 | -5.62336 | -51.29756 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5199262f-9343-3bab-bf51-c9bac193b863 | -7.07471 | -59.24275 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2355a3af-aa63-3f72-813b-abce1b64a7c0 | -8.38221 | -47.00523 | 2025-08-16 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b48cfdf1-25b7-3478-b970-8f8f79ca7be4 | -2.60129 | -51.94739 | 2025-08-16 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c542909d-f648-3125-8a0e-1671248708d9 | -3.98557 | -47.88882 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e22e61ab-5788-39e4-b9a7-2a5cefc182b6 | -8.18057 | -45.019 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d371d1da-9768-3aeb-a8fb-bf118cc8ca23 | -6.66393 | -58.81866 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e46ed20-74da-3c99-baf9-27eb0425e807 | -6.69025 | -41.7366 | 2025-08-16 04:32:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad54d950-a4d3-3e8f-bf48-ff0f3d975486 | -9.37181 | -47.98079 | 2025-08-16 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 66af4e42-52a6-3599-be78-ecf3ce6ec0ef | -9.39988 | -40.55212 | 2025-08-16 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0c68232-fd97-37c6-bc5e-543df1278591 | -6.86258 | -42.80676 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bc67473-9a23-374e-ba53-c6b9cb156bbd | -7.61832 | -44.93326 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552f5204-3da5-34a9-95e7-58f12f72438e | -7.42624 | -44.61679 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ff3da5c-b281-34f9-a9c1-d371b9cffc36 | -6.66704 | -43.76875 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e663fb71-3a34-37f5-aec0-4dfc31687772 | -6.94334 | -59.54622 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a113877d-879c-3418-a110-ec6987913edc | -4.92008 | -43.26635 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09b69a54-45c5-35c4-8956-0e440418b9eb | -8.7501 | -55.01943 | 2025-08-16 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7242db9-9ac6-3ad1-9eec-65d3d3a035e0 | -6.94423 | -59.54134 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 507f50c9-b672-3d29-8c96-84db0afd657b | -7.36686 | -43.84101 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f6f65fd-4fba-39b7-b268-1455233b7678 | -2.50867 | -51.82387 | 2025-08-16 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf6bfc93-b213-3de6-bc50-487f5b7ce5aa | -6.56414 | -43.03247 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 48faffba-08a3-345c-ab12-089ab04f6914 | -6.14017 | -57.93634 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5591c867-8f05-3f36-a352-1371af3115e0 | -9.36849 | -47.98027 | 2025-08-16 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cf84781d-f46e-363b-904f-249bceeab494 | -9.80365 | -48.54002 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13861954-361f-3565-a956-eb47d424ef7f | -6.61759 | -42.74806 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a486f3b9-3d11-3251-9127-b2605bdeee5e | -7.95551 | -61.76438 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 147ae36b-d924-363e-847b-0f8ab34fbcb9 | -7.39707 | -44.88924 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b3a6db2-1565-3c49-8993-9a29908ec681 | -6.6736 | -43.7676 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d214ee08-b75a-3f91-b92a-61f56ed6aa5d | -5.93399 | -53.64705 | 2025-08-16 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde175a1-b749-3c04-8afb-11a55e2f2fbb | -8.73615 | -44.03609 | 2025-08-16 04:32:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6130d5f4-c480-345c-8282-e4926666c602 | -6.14084 | -57.93252 | 2025-08-16 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecf5715-f8cc-3a8b-b15e-a9106e5a9b6a | -6.55757 | -43.03805 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| bfd7663a-a813-3393-a81c-f5e7092dcfdb | -6.09402 | -44.62988 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d023e051-bc26-3285-9bfc-28f107717adf | -6.93095 | -59.54437 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README38.md)
