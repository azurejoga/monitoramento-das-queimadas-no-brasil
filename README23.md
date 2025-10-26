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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a62b0dd-3d05-3b04-a7a9-fc146d5c0c07 | -8.73133 | -48.56712 | 2025-10-26 04:02:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43078a9-0809-3354-a2f3-6a06de512a9f | -13.5359 | -47.15126 | 2025-10-26 04:02:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aa5e2c4-7835-3538-afd3-62d08b364265 | -14.76848 | -46.62178 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9016e630-a382-3dc7-9a2c-8ee84168c535 | -10.9407 | -49.48166 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b58be34-997a-378a-b4d8-d9292e7fa043 | -9.26226 | -46.41954 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c9892d5-c5c5-33e3-ba7e-ed681ee3b2d7 | -11.52809 | -44.97903 | 2025-10-26 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c760f44a-e799-3ff8-87ba-4eeda90de282 | -10.55784 | -43.8577 | 2025-10-26 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94910878-af2b-3534-aec6-c2ff421a3941 | -15.82648 | -49.0836 | 2025-10-26 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b86d640-8111-333f-b475-5cc647d09870 | -11.21175 | -54.84795 | 2025-10-26 04:02:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ced4e35f-14c2-3fcd-b6be-441334e169cf | -13.43417 | -44.58568 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b87ea54f-564e-3ab2-9d13-9eac03451050 | -15.96832 | -44.45374 | 2025-10-26 04:02:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c286bf7f-9ddf-3700-b58c-77792b1edd65 | -11.47893 | -43.24609 | 2025-10-26 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80dd7a9e-21e6-3659-8f51-04439d7d9672 | -14.50865 | -43.00675 | 2025-10-26 04:02:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cd5ad1f0-0d91-3251-8ba0-936ad1931f2f | -10.55853 | -43.85352 | 2025-10-26 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b51ab6d1-7ddb-3d96-8cfd-4da2d7d8fb25 | -9.43688 | -46.33607 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e535a0c2-e39b-3739-84b8-6752e71c064e | -11.67336 | -43.90574 | 2025-10-26 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de456db8-e0f2-3689-a8ce-d945947243d2 | -10.76681 | -44.22615 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303d3f7f-1c44-3ec7-a931-bb6cd15dcb00 | -10.8761 | -48.03579 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d46a79b1-b6f0-3a62-99a5-0473d06d5402 | -10.85843 | -47.94996 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a9c860b-7869-3adf-92cc-f43bd1a07e1f | -12.06232 | -43.98992 | 2025-10-26 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8cb4efa-82db-3bc3-8b27-27cad7bce27a | -12.33479 | -43.44212 | 2025-10-26 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd1d312-3219-3cf2-b59e-026f1a4b51be | -15.46001 | -50.48434 | 2025-10-26 04:02:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fc9be1e-62be-3dc0-bd2c-2643050cb11f | -13.53396 | -49.55819 | 2025-10-26 04:02:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc092dee-3977-35fa-831c-ccb00ee69f00 | -13.87783 | -48.48001 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e122b12-4a4f-3271-b292-ada39dc76276 | -11.02931 | -47.86772 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0fe9b8c-1304-313d-9bc8-efa82ca78b30 | -14.50589 | -43.00248 | 2025-10-26 04:02:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b270aee-2275-3b81-87ae-07f23f3fab99 | -10.1242 | -44.85029 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 678b8a53-fee8-33dd-98e8-b2b314665d49 | -13.40167 | -43.01725 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 71484305-e7a4-3d4e-ad37-d4460727fe95 | -11.67986 | -43.93216 | 2025-10-26 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42029fd5-fd17-39cd-9e69-5ef45a2a6a9c | -10.40906 | -45.32605 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b96fbab0-9558-39ee-8828-ca1727340a11 | -14.83309 | -52.43502 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ed7a10-1017-36e1-95ff-5b6c9b5a676a | -13.75364 | -48.41295 | 2025-10-26 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5062db41-73cd-36a1-a202-b5f9b7720806 | -10.53349 | -46.37585 | 2025-10-26 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51eb7004-2ed8-340f-b05c-1216d68cd813 | -14.50529 | -43.00617 | 2025-10-26 04:02:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87fdbce5-10f1-3721-9ad8-ae325b0fed67 | -12.85134 | -48.64383 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62a0c8e8-61ef-3be5-bf5f-09a10a7a9b57 | -10.41388 | -45.32133 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3b565b26-af31-39e0-951f-ca598190faf4 | -11.84415 | -49.86195 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 676e1e0b-a3e6-33d3-a4c4-33f53260dc8a | -16.13079 | -40.26134 | 2025-10-26 04:02:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e714ed30-90d8-3fda-855f-a0f6b572871c | -14.76563 | -46.61473 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9938d7fe-d90a-3249-b0fa-b70d9357aee1 | -11.2072 | -54.84763 | 2025-10-26 04:02:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de1d0e19-0042-3f2d-a3e5-fcae222be4a5 | -13.84667 | -44.35983 | 2025-10-26 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59f299b5-ad60-3b56-8bb4-4e1a2f994d0e | -13.30713 | -47.09403 | 2025-10-26 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d56637-444a-35ff-87fe-21cef3524fe5 | -13.73708 | -43.13815 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 35761916-7552-33c3-851d-dee0ca622c2b | -10.98788 | -47.88827 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22cbb5e9-2c9d-3e14-9650-4cc4b2288f4e | -13.89994 | -48.44464 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d01c9ce-9489-32fd-9e14-76da9b2eca1e | -9.6905 | -47.43977 | 2025-10-26 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e701bf0d-6642-3598-8298-603025b8e634 | -13.89544 | -48.44378 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8fc41ea-0ab1-309a-9b32-ee0afdaa259c | -13.32086 | -47.93399 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36490fd0-7b68-31e6-96a2-beeec99d789c | -11.53774 | -49.43217 | 2025-10-26 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62d9a07-22e9-30a7-aa89-5235efb0f3f1 | -10.91053 | -48.03 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6130539f-8d1f-314c-a30b-88b2d3c4c1e2 | -11.99727 | -48.93933 | 2025-10-26 04:02:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5811e5e-1bd3-376a-a03d-d15f77d827c8 | -10.25202 | -43.9863 | 2025-10-26 04:02:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 432a027d-3027-32f0-a977-e90b76049d3b | -10.94826 | -48.07861 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2e7386f-85db-3c7c-ae6b-e039beddd4c4 | -12.84673 | -48.64276 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880c2a79-7e48-3a52-b0ee-1c0a6e9ffa5a | -10.97956 | -47.88219 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca344c7c-acdb-3a85-ad24-d6357b44f8c3 | -13.73646 | -43.14187 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 587fbc8a-afd3-3e99-a853-b16c0385474f | -10.8731 | -50.13639 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58dceff-24b2-31e0-8f79-96d6d61eb529 | -14.58425 | -44.13977 | 2025-10-26 04:02:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2c1d3898-6368-3520-acac-6fb6f7e2432d | -15.45499 | -50.48135 | 2025-10-26 04:02:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea6f1df5-05ab-3646-a849-5b8e03da2eb0 | -13.65963 | -42.70575 | 2025-10-26 04:02:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb13b3b2-c42d-3452-9499-73b9442c790e | -13.00881 | -44.01254 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 914f57ef-8a77-3e89-b691-6a8a438429fa | -10.90591 | -48.02922 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d24124b-00df-3531-9d18-a85c2d005a10 | -10.17503 | -41.99188 | 2025-10-26 04:02:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d723681-ff7c-31cf-b27f-e9a4b6f4ff36 | -11.53831 | -49.43201 | 2025-10-26 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00f181a4-97fa-3265-b670-e285b882d5f7 | -10.82727 | -47.62873 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27564468-ff0a-3ccd-85b8-f078a16fc80e | -15.29482 | -50.76077 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a45d499b-eff8-337b-b055-5a4e3eb3858f | -15.21726 | -47.9295 | 2025-10-26 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c55ebd1d-e326-3c8c-95c3-ad7587c7b423 | -8.77512 | -48.37889 | 2025-10-26 04:02:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87b95029-ba8c-384c-8069-23cb7de76c77 | -13.53479 | -47.56154 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5f5ef8c-e2ba-3811-899e-74ade55bc501 | -14.76414 | -46.61637 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea9a213a-b919-3a07-82b4-002be30dcfdc | -14.44002 | -49.95623 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d1cde6b9-4a81-36bc-9cb7-db24ee897c7c | -13.2171 | -47.78272 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f8fbdd9-2f96-3fe7-bfc1-1845e87beb24 | -14.76695 | -46.62328 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed59aa7d-f704-3751-bc5a-c764b0595f13 | -12.2124 | -44.86212 | 2025-10-26 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2351d35c-fee4-380f-99de-bd49dfdd7757 | -13.40062 | -43.55613 | 2025-10-26 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca19e565-0a44-3a38-93de-1f6db6f9df8d | -15.68727 | -49.41237 | 2025-10-26 04:02:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 180391be-569b-3494-955e-3fbdf6648fc8 | -11.06051 | -48.32164 | 2025-10-26 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efc75b76-1e57-3093-8759-15ad1736e53d | -13.53232 | -49.54021 | 2025-10-26 04:02:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5d4e9dd-0c9e-3179-a6ac-96502523ed96 | -9.2197 | -50.76095 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d40b01f-9ced-3334-b009-e91fc692146e | -9.57882 | -46.91933 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b79d367e-093d-36d3-a961-059ae9ff1cea | -12.62686 | -44.23319 | 2025-10-26 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb06a1a7-90ef-3bb4-877d-1dd37ffb7db6 | -10.94454 | -48.07283 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3765cf6-8673-32e0-a486-fa9adbebf599 | -12.50197 | -44.32844 | 2025-10-26 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93022869-31c9-34e4-a127-ad295e2fc759 | -11.05574 | -48.32118 | 2025-10-26 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e211e58-e032-364a-8bbe-f56d7ff94d2e | -9.43334 | -46.33138 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bcb207e-0554-3c69-a04b-0fcdc33fe7ef | -12.83524 | -48.65287 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ecc5fc5-abad-3836-baef-273502864ce8 | -13.89909 | -48.44912 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fccd2628-7abf-3fba-b9a6-652d9f5329d0 | -10.4071 | -44.74013 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8015dd9f-7d8a-36cf-b435-94bb6c1aed4a | -14.65304 | -50.19203 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f233443b-e6ab-373e-8401-6a290f05afcc | -12.09417 | -47.25676 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a68040-27bf-3008-b4f6-81855095fffd | -16.21947 | -45.65951 | 2025-10-26 04:02:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2959e96-3d27-35d3-89ec-785166683934 | -9.26199 | -46.41457 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 487ee530-b236-351a-ae87-0ee605210dcf | -9.26126 | -46.41867 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbc16225-c81f-39fa-b986-eae33c463b68 | -14.56296 | -43.78792 | 2025-10-26 04:02:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 235bd14b-b520-3e44-bbc6-ca9bf108b8bc | -13.28487 | -47.50677 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee654fa-3f3e-3f2b-a5b0-bb8c8b09f98e | -12.2246 | -47.03999 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 885e43a0-60bc-3e0c-a527-f7f250b134a7 | -15.2801 | -43.04316 | 2025-10-26 04:02:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8244dca6-f18b-31a7-89cf-fb182e9b8562 | -13.25142 | -47.98949 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7a4f149-efc0-3de5-a7dc-986a7b5a9d21 | -10.61277 | -48.00104 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41606f96-523d-3044-9161-a3e22c013647 | -11.46792 | -46.12264 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README24.md)
