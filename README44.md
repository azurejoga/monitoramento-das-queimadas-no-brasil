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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a5d8ee2-5609-37bc-892e-0b0e8ef470f7 | -7.43211 | -60.03447 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 866905b9-c0b0-3cfe-b9ce-4c80d822106a | -12.58728 | -46.9436 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 08351839-684a-3693-a19e-68a6cc27f36f | -6.88933 | -59.13266 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a309ed2a-777a-3bfd-942b-6c3a58f5449e | -10.35119 | -64.445 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 994d4a07-e561-32a9-915c-76912344d691 | -9.53629 | -56.28956 | 2025-08-15 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f7e9a733-652f-3f88-ab8a-9c511495f0d9 | -9.16196 | -59.68353 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a49877-85fb-3b75-9953-73b7ab407657 | -6.65864 | -58.82339 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7d850138-0d29-337c-9287-0905d4b19ca2 | -6.88498 | -59.15817 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9871ec39-97f8-325f-803b-2311c8e1f10b | -7.53238 | -61.34261 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2071917a-8967-30dc-83e0-62d0e1bc5800 | -7.95242 | -61.75787 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 922dd380-6243-3493-bd41-079b4b72ca70 | -9.83256 | -60.76455 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb2c534-a79f-3d1a-8013-e63fc6ce3fd8 | -12.67259 | -44.95143 | 2025-08-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eb9febc-47af-3d3c-9467-77ef7c75d49b | -9.49745 | -60.53314 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bf21ce63-41ab-3cf2-84de-46062028fc43 | -6.66436 | -58.81597 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e44bbb7-93ec-3140-ab5a-35f72862d1a3 | -6.08295 | -59.93809 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee218a8d-1ff9-3be1-b18a-7ff441d83a60 | -13.03569 | -56.87622 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90991c3d-3ea1-347b-9be5-235999be8d3a | -7.87709 | -61.81315 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ada9a4d-5a76-3614-abf1-bf604522ab4b | -11.36097 | -55.43148 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ab9d192-f397-3b96-ad34-386d18a92895 | -5.88866 | -57.74146 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 397348ab-a36f-36a3-8e36-555d7c197794 | -6.91416 | -59.14574 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c79d8a9-2573-31d5-a42c-714146d33fec | -11.35361 | -55.43403 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eb76c7b-fcc9-340d-ab3b-c83dff30d397 | -6.48463 | -62.93372 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dec927cf-696c-3d62-a6f4-ec768651accf | -7.87492 | -61.82558 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 488756b1-b4a5-3685-811c-0563d818d6bf | -6.87347 | -59.83064 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12dac720-debf-34ec-a7c5-5022edf8b9b8 | -6.06814 | -57.93884 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ef29fc8-db94-3ca3-886d-cd446aa1f56c | -7.52327 | -61.33081 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 15ad0a59-57d6-3eba-bee1-67d1decc9425 | -9.19021 | -45.32353 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33357519-4fc2-312d-bd0f-0fb7c6a49146 | -9.20285 | -59.6557 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00ab9a8b-f35f-38c2-8430-4964c0b396e5 | -9.15168 | -59.69064 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d847e0f-8464-3e94-8d1f-77370eef1e4b | -9.21414 | -45.33251 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f247a38d-4066-3b7e-87b2-9d54bbc9edea | -9.49826 | -60.54919 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51d0cc6c-d5b4-3a03-877a-d1acb900af99 | -7.53333 | -61.3326 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bf5d68d-93f4-3aea-8c20-2f4d9a00a929 | -7.0831 | -59.21465 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c7ebc7ba-0829-33e2-a134-58b2c0cd7b5f | -13.31511 | -45.23745 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5c86920-9ace-309d-b873-4b6d43b373fe | -9.17657 | -59.67734 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56278837-e46a-3480-8def-4487287f08c2 | -10.01347 | -62.75303 | 2025-08-15 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35d96885-1920-3561-9538-737388d500e7 | -9.16134 | -59.66141 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4ca8484-e2c1-3376-8f57-ff116b869a59 | -5.8927 | -57.7422 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d61ceb-f53c-3143-a56e-652664669740 | -9.91493 | -60.43745 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcbff0e1-68cf-3655-9132-2fcd30a7ebe5 | -9.51405 | -58.3557 | 2025-08-15 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9fbd7c6-7d6a-3eb3-b469-321889377470 | -9.90047 | -60.43959 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76409f1c-fef7-3b04-9261-cc22ee310fd0 | -9.50835 | -60.54609 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df6b2902-db82-32d9-baae-2d7b98e0ef7a | -14.01938 | -52.0444 | 2025-08-15 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b9e98a6-0e50-3344-881d-5239c87fff9d | -6.94039 | -59.82477 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2fba45d-a4a7-369d-aa97-d4a578ffcaf8 | -6.9222 | -59.15154 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e24524fe-c847-3b8f-b490-93a46e7a3130 | -9.50923 | -60.54128 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be157f59-9133-3b39-9ac8-ef9d012fdf66 | -7.08822 | -59.21114 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd450788-fa70-3b41-b8cb-9044dc80bc16 | -7.87144 | -61.8232 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0129553-9440-3990-b035-8b0ced8c530b | -7.03959 | -59.85216 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2443e2b7-dbea-3384-9d2d-9d7cfe2595d1 | -9.39239 | -60.54096 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 757ee0b9-726b-3dff-b1b8-227486fb362d | -6.69954 | -58.84312 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b86f6b9d-721c-311f-beb0-113ddbc5f6be | -9.50204 | -60.53406 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2cba3966-8cda-3c46-82f9-75b29914dd49 | -9.20795 | -59.65228 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bc11ad9-f25e-39d2-bb0a-704dea947049 | -6.89447 | -59.15545 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03231ae0-5d63-34fe-9079-4a27b8e38231 | -8.31715 | -45.01831 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9ec95d1-2923-3e96-9af6-af728ceb3234 | -10.11475 | -57.76871 | 2025-08-15 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8a1d57c-0b07-3276-8c00-84f0db0d23a3 | -6.72315 | -58.83455 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5cd70d4-66f5-3fae-b45d-1948543d796f | -7.96102 | -63.46937 | 2025-08-15 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c86b440-570d-3ea1-9ccb-037e4f1379f1 | -7.87945 | -61.80862 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84310e6b-6429-3aa6-b28c-fbb2c5e55fd5 | -9.16783 | -59.67579 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58453e66-b051-313f-a4e4-412543ee17bf | -6.8764 | -59.84113 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671d1e30-979a-3884-9a87-d3cfe42bd2e7 | -9.21156 | -59.65738 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd78a0ec-53d6-38e8-a88c-2bf9b2505999 | -8.55428 | -63.91845 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53d12f7-0a57-3d12-8b17-8c29fa696bd2 | -10.96036 | -49.56684 | 2025-08-15 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37609e6a-beeb-390b-9c57-e3b37cde1886 | -7.81255 | -61.32805 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 546dec83-8f41-35bf-b57c-9b49e5638b90 | -7.28622 | -60.62928 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99f5edbd-dcda-37ca-9f94-c38562e60949 | -12.58998 | -46.95876 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0f9a2ba-61c3-3627-9def-aa7e6ca638d5 | -10.47421 | -61.328 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b60edba-72a3-37e9-ba83-608a7d3e1a28 | -7.58495 | -63.46634 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc3ad5c1-4c00-3f51-9ee7-eb2308a6a33e | -7.94948 | -61.74458 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6107021-88fa-3105-aa63-d70467bf02a6 | -9.93553 | -60.48023 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66861bff-7940-3729-8f72-801b118f06b5 | -7.95527 | -63.4683 | 2025-08-15 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc55d689-924c-3966-96f8-d1a13aae2c65 | -6.99843 | -59.98363 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f7ac9d8-695a-3058-9b6a-057b2871e164 | -7.87259 | -61.81695 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b22cc14-1350-39e9-80f7-20618e371f16 | -12.34602 | -49.91323 | 2025-08-15 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0af2755d-2808-3ed1-924b-a045df0825b3 | -7.32083 | -60.63005 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 513486c2-5975-38fe-9054-341c8bffd313 | -10.32528 | -64.45301 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b6987fc-bda8-39e9-bc60-1a3b70f944a6 | -7.80447 | -61.34452 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78255c32-8b65-3f1a-b15a-e3ef220223b3 | -7.94214 | -61.75602 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cf98c4c-cc0b-3286-8e44-048c74e1f81b | -10.01938 | -62.75076 | 2025-08-15 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23297ee-c6da-3e18-bebc-1c6ce851bf6d | -7.80497 | -61.34167 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43eba5c4-7116-3ee2-a4ad-e5b84990ca46 | -9.34237 | -62.58792 | 2025-08-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 55d5e415-f879-39f8-aad5-a3ca718ac74d | -7.4581 | -60.40262 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96800492-eff2-39f3-b271-07701a6570bd | -13.10999 | -57.14763 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06281f4-215f-37d6-89bb-c72453588378 | -12.50801 | -47.01023 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcbce712-9f53-3d1d-925b-c262a97b8b84 | -11.35877 | -55.42353 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2c139e6-0659-3e0f-b638-0326a2b4a9b7 | -7.53187 | -61.34554 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bf0532c-1472-3ecc-abea-79351da22622 | -6.67225 | -58.82153 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9bab5dd-0ce1-3b1f-a92a-140dd29f5acb | -7.80345 | -61.35028 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97e70ea5-95b2-3be3-9745-4790578f1d95 | -9.00583 | -48.7248 | 2025-08-15 04:51:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32529cdb-9005-3297-b268-ce5517069bba | -7.29773 | -60.62016 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed863267-b843-38f9-8cd9-03c835b48c51 | -12.59681 | -46.9712 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1425dda5-58bd-3cac-b342-20bf8eeec0a3 | -9.89847 | -58.57551 | 2025-08-15 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5946a1dd-96a6-3f8a-9bd6-b2a2d358542f | -7.25549 | -60.63464 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ee2dd57-e279-333e-8d81-87a408d4c7ec | -8.10718 | -61.20767 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4177dd2b-592d-36a2-b68b-3fa0efdebc92 | -9.20074 | -59.64194 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9aa0a5b6-eb17-389b-8e84-84da47daed19 | -7.01157 | -59.82253 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e83e5d-8414-3cae-8aca-552d1b5abaf4 | -6.94421 | -59.99358 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c63a0fd6-aded-3980-aa85-2d46b60e1ad9 | -9.18469 | -59.65663 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f1cdbc0-3c2c-3f50-aa7b-59ae2b362549 | -9.50832 | -60.5253 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
