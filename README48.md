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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e72b51-a658-3162-a415-2d26a86e95b9 | -10.8403 | -46.19656 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06f4a0ea-e2be-321c-9b7f-af7304850fb6 | -9.0201 | -61.01089 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9985618c-f5ed-3da9-9df9-1bf413ca42d2 | -10.88452 | -54.02122 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23850c8b-ed53-3222-9552-6e72d73861f0 | -11.54802 | -46.86253 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bc9ae705-2d8b-364a-ac73-7e7494de880c | -8.60068 | -64.10361 | 2026-09-16 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85e0298c-db7f-3031-9fa7-504fee313f2b | -11.36598 | -43.9436 | 2026-09-16 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de481be0-8432-3922-83bd-95e82feadd27 | -10.89571 | -54.01556 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78602bde-5a05-359f-9d1e-79a4d0fc06b3 | -15.2464 | -49.10795 | 2026-09-16 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1db44e47-b517-3a41-b06c-3669c8d3ed8f | -10.90349 | -46.2943 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46601830-1792-394c-9055-e6854c523ff6 | -10.9322 | -54.08382 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23afbccb-9ada-3c1d-bb50-d9bcc8a91cea | -9.76375 | -46.58099 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c860808-d54b-3e16-8269-3c5eed2bd014 | -10.69453 | -54.17293 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85b0edc7-42f5-3cb1-addf-fd70c5825580 | -15.03554 | -48.56611 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afd78d18-c2ec-3022-b517-3fbfc586b2b1 | -9.17515 | -50.00012 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa9ab507-6dff-35f1-ab78-f1bebac462a5 | -7.65529 | -67.17258 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4158bfb2-4b2b-3cf9-b7ad-16de20edcaff | -12.32314 | -47.96329 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67a99f99-ec10-3c79-a4c9-e746a98c08c4 | -10.82072 | -46.17968 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef08c942-d6e9-3483-b46e-b327643b336c | -11.32814 | -46.78434 | 2026-09-16 04:59:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 123854dc-de33-3f6d-8332-b724a82138aa | -9.12659 | -51.58261 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1373c25-ff7f-362b-8307-7220337244be | -11.05224 | -47.94735 | 2026-09-16 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb4074ea-e30b-3a1f-a5aa-232022a2d117 | -8.41133 | -54.71711 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7e50c1-878f-39af-a6c7-cf25ce0bef3c | -10.41657 | -48.66065 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fed5105-c430-37fb-8b66-e2cbdd20f9c1 | -10.84804 | -46.17783 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d973821-7029-3820-9a65-ff07b23522fd | -9.7268 | -64.90675 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a75a175c-d0ff-3361-9315-14aab14c464b | -11.02249 | -57.13301 | 2026-09-16 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 674f5bc0-0356-3396-880d-a4c34a9d3858 | -11.2676 | -54.13541 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90d42795-8aa4-30f7-80a9-66bd5b75c75e | -10.47065 | -57.90973 | 2026-09-16 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7430f6b-394e-3b7a-9df4-b872a7fca904 | -8.64919 | -66.5797 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6293cfb-239d-3981-bfbb-87c0af6a135c | -9.56482 | -59.3114 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c9a6cd-6966-34ff-a058-1810aa13c199 | -8.54767 | -54.71787 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68c8e9c5-7149-3419-8bdb-35141a8433fc | -12.15881 | -47.99189 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c529eef8-0f9e-3d68-a7b8-5e58f4ec249a | -13.63815 | -45.97447 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f2287fa-3e27-37e4-972c-bbd05a48fdd1 | -12.71802 | -43.20745 | 2026-09-16 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 548e884a-407d-3497-88b4-ac7ed7ab8fca | -6.91909 | -63.11046 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d247e01-88c8-306f-b920-8bf88d9d0809 | -8.63772 | -66.57255 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dae0ad8-3775-3ed4-92ba-d2a1894ff39a | -9.85701 | -48.36041 | 2026-09-16 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54eb75d2-3bd3-353d-9387-fc30d661e7ae | -9.62036 | -61.82156 | 2026-09-16 04:59:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dcafd38-af98-3041-a633-cdd5f2f0e3c7 | -10.99595 | -48.34417 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6867f38-6146-3a6e-b087-f01996942851 | -10.76742 | -46.2282 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c22f3831-65ef-396c-9969-23d887d3518b | -10.77527 | -46.20893 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c6afbe2-8c37-3295-9075-aa82ab9c3527 | -11.20328 | -42.82892 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 92af44e1-fa6c-3bbf-bc0f-3f2d33b5dfb3 | -10.41154 | -48.66427 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e96fb16-6569-33dd-abd8-284fd1a23cf7 | -10.90017 | -54.00886 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e093554-330f-3b42-870b-8489af060654 | -15.04161 | -48.55614 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1752e41d-3ba0-3cb4-9b8e-1646d7674e71 | -10.83543 | -46.19221 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3539c40-b156-3133-a0ae-e0f6452d8a31 | -9.78535 | -46.49627 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bb85e26-5b3c-3d83-8dcc-0911fd9e71b7 | -7.55156 | -62.32798 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b2d136a-aea5-300b-8234-ca9997bb7bf0 | -8.5443 | -54.69602 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2079f448-7e3b-3a2e-acec-8aa08cd9ee0a | -12.85364 | -44.39232 | 2026-09-16 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0eb855c5-dfea-36a7-89d4-a6be7e8cac48 | -9.86791 | -49.83342 | 2026-09-16 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46121ede-4e44-3787-b36d-af4b579a301f | -10.93555 | -54.08434 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe022f90-1b3b-3ae1-bd6e-80bd86fab31e | -10.84885 | -46.17134 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfaf749b-e3f2-31e4-a4c0-a7200dcc4f3d | -12.76788 | -51.2508 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 49bb3407-6eba-354c-a957-a61f0a33b061 | -6.93064 | -63.13442 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 898dd4af-9f40-3402-b7aa-a6bc936fbce4 | -10.88397 | -54.02484 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c38adcd-8092-327c-8aa3-0afe8c87f0f4 | -9.12581 | -65.85069 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f16918c5-9a67-3086-9e0a-ed1026cc8f0a | -14.85671 | -48.12613 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77879325-d721-3b91-8631-5fe013d4b19f | -9.80219 | -46.50757 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 171885f0-14be-3fb6-a3ec-ea82061b0d64 | -9.02155 | -61.01197 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e8216e-7d83-31f0-be32-c7276e44aa59 | -10.47686 | -50.95771 | 2026-09-16 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e75796e-e559-3e1e-9cc3-2cf007d0332a | -10.70177 | -54.17037 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9dc0d895-504f-3eed-95d7-e1a80e8d7f35 | -9.79089 | -46.49398 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5113a4fe-114a-3d51-86ca-ccaaad25109c | -10.40376 | -48.65419 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5a7cd7a-253c-36a6-96c8-76f78a42b13d | -11.20728 | -54.11159 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4574f626-d006-3f83-a784-6fa7df59ff17 | -9.1034 | -65.93562 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4051e9b9-07f2-300b-b751-4651efe97ede | -13.34861 | -46.3061 | 2026-09-16 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f9db305-2be8-3877-8295-65d37f954dbd | -10.69843 | -54.16985 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b3d488e-6b1b-3d64-ba43-b6720dc3e1b0 | -10.40931 | -48.64674 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e971a263-3270-33da-a673-1c51648a52f4 | -9.71302 | -64.91941 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8889195-ef38-3c0f-a81b-0aab4301af92 | -9.10423 | -65.93127 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 221d5bbb-59f3-3801-8e20-25e410401302 | -11.24558 | -43.44088 | 2026-09-16 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27638d87-fcf1-3887-ad90-6b57fbd8b085 | -8.37228 | -54.72875 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2e96bfc-109f-3653-87b6-bbde88e6a901 | -10.90309 | -46.29734 | 2026-09-16 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95c9cad-3835-3f4a-a82d-f521187a62d2 | -10.93836 | -54.08848 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ed911b5-2943-3538-b761-0c685e897532 | -9.87201 | -49.83402 | 2026-09-16 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f19f4d5-9986-3ed7-b675-139b7d858c66 | -12.38185 | -51.4149 | 2026-09-16 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c99675c-4ee2-3710-b098-dc1b8adfdcb1 | -10.59868 | -47.75879 | 2026-09-16 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 029aa2c1-21f1-3c97-bd8d-606e16caeac6 | -8.53553 | -54.70886 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50f5fce-6235-3d29-a072-d525b91ac1d1 | -11.20533 | -42.82985 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f56dbe65-8a3c-3d5e-a30d-babae1e53021 | -11.91502 | -49.73581 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfddd3d8-4ba7-3180-a092-60a95e377c5d | -10.03623 | -52.08949 | 2026-09-16 04:59:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83c26789-248b-3464-ab04-81391d3d76fe | -12.13488 | -57.18326 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ddff9c74-e6b3-30a4-a141-22a2a181ee0f | -9.813 | -48.9133 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c72f12f-e91d-36de-8353-0b6c23973832 | -9.38669 | -60.30539 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8081df97-779f-3c7c-b800-ec095c47a77b | -9.09854 | -65.94138 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1634f9b9-deaf-382e-99cb-afaf3037ad58 | -11.54844 | -46.85919 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 849e7094-8fcf-3173-a0a3-128212f10379 | -9.38889 | -60.31695 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e1a6579-21f6-3efc-b66a-79e9757a1684 | -9.80696 | -48.92537 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35885f65-5e58-36d1-9bf8-6df8718866c1 | -10.46557 | -44.95248 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56dba754-34d5-37ae-aff1-72f734b53add | -9.04172 | -65.91747 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1394b982-8ee6-3e26-8507-2780aa21fe7b | -9.11987 | -59.50911 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d030ae8-d97c-33cd-83ae-37ecf5702d04 | -10.83937 | -46.20409 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a57c4476-a776-3e4c-9d8d-f77cd1591f66 | -13.40216 | -57.02448 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3584df54-443f-3027-900c-2193f8f8e78c | -12.80752 | -60.48838 | 2026-09-16 04:59:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e445a8d1-ebaa-31ac-9093-9833f06fd054 | -9.72611 | -64.91039 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f5b5153c-4577-3498-91b6-84f3ad4874b3 | -7.64981 | -67.16576 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 05037e0d-cc5b-374e-bacf-8f2a341dbd2a | -11.55316 | -46.86324 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d21b756-6d7b-3d74-9862-6192152a4010 | -10.82114 | -46.17627 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25a8e7c3-c08b-35cc-a2e7-5f89fcca7062 | -10.90354 | -54.00938 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c956216-bc48-35b0-af01-d211036d75d7 | -12.66967 | -50.83484 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README49.md)
