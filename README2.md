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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8146cf44-ffa4-3d78-9362-867437649a79 | -14.1286 | -45.3161 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1a661d9-65d6-31ac-8fd6-36f1bb1981e5 | -14.12353 | -45.30997 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01263d63-0ec8-324a-9957-2742927cc355 | -11.96946 | -46.78368 | 2026-05-13 03:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe15379-aca0-35c6-8bf4-bf68f19f98a8 | -14.13709 | -45.42865 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acdf46b6-f134-3ef0-abae-d99e0ac759cb | -14.13809 | -45.42381 | 2026-05-13 03:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab783f4-a5d9-3cc7-84d0-62427a87040e | -11.79928 | -43.63099 | 2026-05-13 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe1b0a27-eca3-3340-9d03-46d957f5a02e | -12.8548 | -43.76305 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c65d4fe2-fac9-3797-aa58-78961b3d6c39 | -11.93713 | -43.38065 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 680b773d-f627-36d2-aed7-8449a3705035 | -12.61815 | -44.5275 | 2026-05-13 03:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46ab4622-407f-3b7b-8626-59b61ff3878d | -12.11551 | -43.64239 | 2026-05-13 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a338618-c006-3556-96c7-c82f9b6dabea | -12.85336 | -43.75865 | 2026-05-13 03:34:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff3e2ae2-18a2-3a27-9339-bc59ecd456cb | -21.3292 | -47.03112 | 2026-05-13 03:36:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bbb0656-e04f-3977-abd9-980235818c70 | -21.33704 | -47.024 | 2026-05-13 03:36:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d960d39-b8ee-35b7-bcdd-d2fd802e346a | -21.33603 | -47.02839 | 2026-05-13 03:36:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 518b7eee-cddb-3c39-8c49-e51d30495124 | -22.87421 | -48.6279 | 2026-05-13 03:36:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce0dd633-e1c8-3f6b-92f0-a9788357a0c6 | -21.33022 | -47.02674 | 2026-05-13 03:36:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef8da448-0865-379b-9881-67ea3664bcc7 | -21.86652 | -41.20963 | 2026-05-13 03:36:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| de5fa667-0f39-39a3-ab86-dc3a7284b282 | -21.33124 | -47.02233 | 2026-05-13 03:36:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1eb0230a-b4e2-3ba0-8484-5e1f93f0c599 | -7.28035 | -46.80233 | 2026-05-13 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d6ae56-6313-3f43-aac4-dd17aa266e04 | -7.27752 | -46.79806 | 2026-05-13 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70aecd40-d5cd-3fe0-afb4-394f352b7c12 | -6.21753 | -46.88583 | 2026-05-13 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fbb82e6-e0e6-35b8-b8cf-706141f577ee | -7.01298 | -44.98885 | 2026-05-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cbcc041-6379-339d-aabc-8f015715ee6e | -7.24889 | -45.39284 | 2026-05-13 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b4f76b3-6d83-38dd-b926-d4a5957c2028 | -14.12158 | -45.31975 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf9139c2-5187-3146-a427-1c4ab12186e0 | -14.11934 | -45.31199 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79d94b63-6dbe-3331-a23c-3e2380141a6d | -10.86318 | -46.71969 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78b05a2f-e204-360e-8b3e-28ccae01419a | -10.67596 | -42.15448 | 2026-05-13 04:21:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59ab21dd-d2a5-3c97-aa87-a5ef628602d3 | -14.14015 | -45.4224 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36222a12-27d2-345a-92c8-f94a027f8899 | -14.13214 | -45.31773 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d4ef833-71f9-3d36-a9f9-194b40af2c27 | -14.12547 | -45.31667 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc103a6d-b6dc-39a3-b6fe-5b6bcca38ba0 | -10.4308 | -46.65676 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 301a2fd3-0928-3687-9bf0-1b1403a7b559 | -14.12826 | -45.32082 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87a94f33-eaea-3554-95fc-765605f6646c | -14.13627 | -45.42546 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c325b4-5e40-3e6b-b090-ea4dc542d780 | -11.98543 | -46.78974 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46eda57-84e1-3bb7-ba90-22cba153d9f0 | -11.45154 | -39.28958 | 2026-05-13 04:21:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c5b08e3-400e-3ab4-bab7-fcf93f22d246 | -12.48921 | -45.4404 | 2026-05-13 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4612a1f0-832e-368f-9686-20de0f9dac09 | -14.30873 | -49.24918 | 2026-05-13 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17d98b03-243d-3022-a470-aca8ae04cc64 | -8.0949 | -44.17532 | 2026-05-13 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c28b57ca-72cd-3506-a869-d9482330da0d | -12.05052 | -45.28751 | 2026-05-13 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2bb7c0-f7cf-313f-b6e4-ccff7ea41477 | -14.13682 | -45.42186 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4886e713-5f23-3c27-89db-7f0c9fbf0ce4 | -14.1299 | -45.30997 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2282bebf-fd2a-39ab-abd7-f11e8283c0a4 | -10.15042 | -39.99815 | 2026-05-13 04:21:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6fa77f0-caf8-34cd-a993-3f5c14ca93cf | -13.54478 | -49.90639 | 2026-05-13 04:21:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5503cd02-e5f8-321b-b562-e7c401c8179d | -14.1479 | -45.41625 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c328ea1-918d-3f24-b3c5-7a51691850bf | -14.12268 | -45.31252 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea3a20ed-1211-37f9-bb26-151d08bfafc6 | -11.9821 | -46.78919 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75cec7f7-709c-3295-b48b-5225df577481 | -11.18329 | -55.92884 | 2026-05-13 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e7461402-49cc-3183-9341-6077b8384a9b | -10.71295 | -47.73572 | 2026-05-13 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4419e52-da7b-3a3f-884a-a857956ae2f1 | -11.41035 | -48.44367 | 2026-05-13 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f5f3b05-de72-3697-a2b7-a9b39853dcde | -12.11482 | -43.64525 | 2026-05-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61fc869f-b739-32af-86f7-6baeb011c9fc | -11.84328 | -49.43642 | 2026-05-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca240738-de10-31ee-ba1d-3ffb11e81661 | -11.986 | -46.78617 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c56c7013-3427-35e2-84bd-ee2a1f5d49f4 | -8.54056 | -45.98338 | 2026-05-13 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd1c5f00-491b-3920-a4ac-052ec54b6ee6 | -11.40702 | -48.43925 | 2026-05-13 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bd12c09-f61c-389f-9afd-2c7d66072f62 | -10.66229 | -49.70386 | 2026-05-13 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a66b5011-52f7-3378-bc26-8351dc43b1bf | -14.13493 | -45.32187 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b8ccac-fff3-3f2a-89b2-b52d5cfe21c4 | -10.18724 | -49.59138 | 2026-05-13 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05028667-0241-3b01-9380-bbbcee3d333f | -14.14845 | -45.41265 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7eb9da9-c031-3477-a5ea-47e5af76c75d | -10.5625 | -45.06139 | 2026-05-13 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 413c7682-e014-3709-8735-3f2e3a0eeaf2 | -11.94015 | -43.38164 | 2026-05-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dccd28d4-06e5-37f3-bba3-487d1cf7d05a | -14.13602 | -45.31465 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f017bd58-398b-3667-9bf0-fc720d7124b4 | -13.96073 | -46.03642 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6669a0d2-34c7-358b-99e8-41f195000d6e | -14.11546 | -45.31507 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d7cad54-992d-3cc1-b558-74f19d39b651 | -14.38493 | -45.57549 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8772c59-e68f-32b9-9445-2f453323a4d7 | -12.08269 | -51.25587 | 2026-05-13 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58cd2542-24ca-3d39-b897-2291e46877ff | -12.62892 | -44.52171 | 2026-05-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbed5a0a-daa6-33d0-9433-605f39fee964 | -11.84253 | -49.44086 | 2026-05-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aa31474-11ba-3f9f-b4c1-7074502d479d | -11.12532 | -45.11501 | 2026-05-13 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adbe7b97-16a5-3e8c-96e3-470d2f3263f6 | -14.13269 | -45.31412 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57c38796-3d5a-3b51-a059-064abe5395ba | -8.70524 | -47.97999 | 2026-05-13 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b80b6760-8e66-350b-a70a-7cc7b028143c | -13.68665 | -44.28888 | 2026-05-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d139733f-ba86-3fe7-9b13-c05923824bb4 | -14.12935 | -45.31359 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2e221ff-f7bf-37fa-8fbf-be7970a03e89 | -12.0472 | -45.28698 | 2026-05-13 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eca3fe51-35f3-3edf-ac3c-e297c26d2131 | -11.74234 | -44.74765 | 2026-05-13 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5820adcb-658f-3809-8a23-233361f6ea39 | -11.63665 | -54.15583 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24833bfb-6c9f-3afe-b6b8-861680313a53 | -14.11964 | -47.42296 | 2026-05-13 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 599b59bb-4545-3296-bf7e-7b9762d48c52 | -11.97212 | -46.78754 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fdc6a7f-5f2f-3e43-aa43-beacda7ddc6c | -11.6306 | -54.16055 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d88e80b-78e5-3631-b725-4d634c421c49 | -10.55268 | -42.43578 | 2026-05-13 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b17a63c-4bc6-3581-81eb-87b3cf4de980 | -12.85454 | -43.7578 | 2026-05-13 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb4a6559-f10d-3e92-9ebf-6c25be62b2e2 | -11.26827 | -55.78953 | 2026-05-13 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dff83ca6-57da-349e-8121-76765c6feb91 | -7.62761 | -48.0243 | 2026-05-13 04:21:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c24baa8-4a9d-3350-9116-cd8c62094631 | -14.40559 | -44.58761 | 2026-05-13 04:21:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c7943e2-ecb8-3a7b-afb6-18a1370f14d9 | -14.70861 | -43.21241 | 2026-05-13 04:21:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed83e51f-573b-3c1d-ae00-1823c207ff99 | -12.3881 | -49.2823 | 2026-05-13 04:21:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3db64640-41bb-397b-8ac3-8f7be1853d4e | -14.14567 | -45.40852 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72048b8a-a5e8-3127-8bfc-f6774d914b09 | -14.1341 | -47.41821 | 2026-05-13 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a73dec9c-5959-3dd7-847a-226573060493 | -14.12601 | -45.31306 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15dcd488-fe4b-345f-b342-6d34f092e363 | -14.11491 | -45.31868 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a610c578-aaeb-3efc-9509-1a3274acbce7 | -13.96349 | -46.0405 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d90a7e50-e249-3078-b6c0-7e5ebfbc6db8 | -10.55919 | -45.06087 | 2026-05-13 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bf3e688-e1ce-3a64-8710-ce4fbce21cf3 | -14.3816 | -45.57495 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13d77af6-c97e-36cc-97f9-239841e1344e | -14.149 | -45.40904 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8d13fdf-3ec0-378f-afc3-2b5f10f97f2e | -11.26755 | -55.79333 | 2026-05-13 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a2565a0-58e1-3975-bb92-9b498a4eddec | -8.8514 | -50.21414 | 2026-05-13 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d911db1-67dc-3944-b12e-f6f31f898f3e | -12.07861 | -51.25515 | 2026-05-13 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b308dc3f-67ee-31de-bd08-cd4ebc7f8f42 | -9.45878 | -47.79273 | 2026-05-13 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1252940c-3614-3af9-a3c2-d27737acd025 | -13.96404 | -46.03696 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc7c602-489e-3236-a1ab-c0b08dcbe920 | -11.54868 | -46.56117 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcc6c8c2-709c-376a-bac8-607918182f6e | -12.85397 | -43.7617 | 2026-05-13 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README3.md)
