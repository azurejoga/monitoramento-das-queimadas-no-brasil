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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bc780c5-79a1-3959-8609-039437ff1db4 | -11.87649 | -46.39737 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60dabda0-a66d-3000-a805-f07c556909da | -12.70614 | -48.1986 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40209928-b53d-3e27-bab4-2439b97385c1 | -12.70837 | -48.15896 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d0e3247-a2be-3285-b04e-6a5369af1340 | -13.66499 | -46.87894 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbd28d03-5a64-36d3-818e-3f93e00e6bd4 | -15.12939 | -48.12611 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c9a23b5-d30a-3e06-849f-635fce1dda2b | -10.94288 | -46.85895 | 2025-08-29 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c2b6c8d-b571-300f-b1ce-60c24588acf1 | -11.02585 | -45.0691 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c785b029-872d-3b69-ab40-9321d22afecb | -11.29902 | -43.54943 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd91c097-3ad3-3fed-a977-4b455815108d | -11.83744 | -46.79515 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c982d41-5b5e-349d-85af-e2611b6aecbd | -6.26248 | -43.81458 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6eb73ea-4234-3cef-816b-de2a4fd5d851 | -12.82753 | -48.10454 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c0b1fff-a60e-3aeb-9ee2-39fc44c666b2 | -11.35022 | -43.55082 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94097293-ef5b-32dc-9cf0-c7f4bc09d24f | -11.08624 | -45.13113 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3ce1bd6-f4de-3851-8dab-0a75c3bfabdf | -11.24535 | -45.00834 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9d806f9-2afd-3727-a028-4f14c5aa9a96 | -12.83089 | -48.17402 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5adbedae-bb7a-369d-ad3b-0bf2364518b6 | -10.98102 | -46.85696 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49153898-4ff6-3a07-a4ff-3ce1b7420670 | -11.08735 | -44.76158 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74ec6d9e-edac-35da-aa5a-093a0b841a6e | -11.56179 | -46.34172 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcf360a9-d93b-3ab0-86a5-a9b58981dc66 | -11.32056 | -43.57294 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be870ccb-974a-362e-814d-72069d9a0c40 | -11.58197 | -46.26241 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe0de87e-b0a9-3e57-8305-1685ed49ce18 | -12.3252 | -47.05114 | 2025-08-29 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 931871ee-6a8d-3390-82b9-478b2e9c9165 | -5.62224 | -45.00319 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37a8c73b-f60a-337c-982a-9a04d1ec0cba | -13.55863 | -46.92108 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f844faf1-b823-3576-833d-eb299bfe2827 | -12.90033 | -48.13842 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8b7d791-0d95-3280-8d20-472fb3c5ff1b | -11.32336 | -43.58132 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae83838f-dca9-3a41-9446-0b0c8ac09550 | -6.08513 | -44.00319 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2ebde1b-e3a6-3afc-aa84-1d98fd5b09e5 | -12.69618 | -48.19121 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c72cedcd-e6b6-3698-9e8d-6e286d246698 | -11.89922 | -46.71901 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e42028c2-0a44-37e5-afa4-6c99aa4a89d6 | -13.54401 | -46.94312 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6bd4dba-c056-3e1d-bad4-8b09b6c7aba7 | -9.6806 | -48.31516 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b167f6-6583-3985-a2e2-8869fd292b78 | -13.50102 | -46.84448 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e0725c0b-389e-332a-9591-95337e6890b0 | -11.07973 | -44.77251 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73c00d56-a050-3858-9141-f543b0f71981 | -14.84489 | -46.74768 | 2025-08-29 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0823455-dc3c-3f7f-9cb3-7064512611a5 | -12.68502 | -48.19154 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dacfd612-57e4-3136-86af-cdd62c29d935 | -5.86673 | -38.28527 | 2025-08-29 03:49:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c8f0752-31b7-39cc-a6a3-3471d96f4a72 | -10.94901 | -46.88363 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea25c372-ce50-3f7b-aa68-0531484169fd | -11.87534 | -46.40342 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e147ffc-1a27-3a26-8499-658db518bdce | -5.61423 | -45.01196 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a057a58-b0f1-355a-977f-2ecf31468bd1 | -13.55356 | -46.89357 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c540154-f128-38e4-816b-49ebdc29701c | -12.30011 | -41.99635 | 2025-08-29 03:49:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a785a8f-c455-302b-b0cb-0d7894da577f | -13.53451 | -46.9386 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4b6d6b4-078d-3e78-9af9-724aa7ec2ed4 | -12.81351 | -48.17557 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4512b0eb-f290-3ba0-9823-db450951e3a5 | -11.55168 | -46.36774 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfdf7a3f-481c-368c-8a75-0501ae138309 | -6.32716 | -42.51407 | 2025-08-29 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b4eb545-0ea5-3721-948c-38b698a65d5d | -13.40218 | -46.84793 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e38584d-81a9-310a-a572-6871526c0990 | -13.42278 | -46.95564 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cacbbccd-9053-3b77-b5c4-699e818671ff | -12.8216 | -48.10418 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80ddec0c-1f68-3f09-9579-faa06f876ba6 | -11.23624 | -45.00631 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd86d57e-9ca0-3b5b-a1ec-aab35a3d41a8 | -11.26195 | -45.49337 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d146912a-5cb5-3cf9-bfb9-73de1575d32d | -17.34575 | -42.64369 | 2025-08-29 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f2ea011-b71e-3f94-8e2c-79d801def775 | -12.92115 | -48.1482 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34927fe3-6b1c-3489-a142-bb6b76f989bf | -13.61942 | -48.24976 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0578e74-c009-344a-b1aa-529b5b451907 | -12.83647 | -48.11533 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26c6fc93-303b-3796-9555-3de51f0bad3a | -14.25241 | -48.06833 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3243fe70-4155-389b-abbc-4ac7eb9db3dc | -6.26328 | -43.80998 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca1bf6d2-00ef-3f4b-b9b0-bc0da2b3530b | -13.43824 | -46.95647 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acc29a75-3bb1-322f-81a9-20d5183971bf | -12.0907 | -44.724 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 43ea2386-f058-35aa-9a79-a88551a94038 | -14.27452 | -42.38146 | 2025-08-29 03:49:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 866c1f02-5ef1-35e1-b827-69631b339ad2 | -6.04121 | -44.46661 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c0e326-4e3b-3402-9ffb-e65e8dd43e69 | -11.32608 | -43.56604 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54ddbfb2-8aa7-327d-bfc1-d0eb3c3ecadf | -11.57476 | -49.51589 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24844cab-ea2c-3c50-9273-95182cb84a9d | -14.90302 | -46.45042 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55199e38-31d3-310b-9493-2503d90f6f2a | -12.83229 | -48.10912 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a860ddc0-0d35-3d15-83d2-badc9e0535d9 | -6.54424 | -43.93214 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 72bb462c-6c59-3044-aeb8-acd3d32821a0 | -10.67794 | -47.08561 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7de30a8-d6ae-322d-80e9-91066ce037f1 | -12.86277 | -48.09859 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d06b6ae4-f536-38de-b63d-fa2fdccc9259 | -13.51229 | -46.94604 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85720424-c720-3abc-b785-a113ad2dae55 | -15.32133 | -48.22383 | 2025-08-29 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56492912-a370-3d84-8ea3-1d733dcef036 | -15.12348 | -48.12834 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d112525-7f6c-39c3-96b7-f08fe8ad6cbd | -15.13009 | -48.12267 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8f40f1b-c0c2-3b5b-bef3-6873227a7136 | -13.37057 | -46.87828 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f7a4824-3980-3649-8238-fd3365de2ebf | -13.56903 | -46.86681 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 415b3b17-40ad-3b32-abcc-9917c9029161 | -5.47802 | -41.40674 | 2025-08-29 03:49:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7e3a3793-e33e-3104-b668-2d6bb4fc7248 | -6.48915 | -44.40202 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1558f17-2980-32cd-919f-4df0e2e5ced6 | -6.19133 | -43.32062 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d4eefc-fde9-31cc-af60-1b5572a3f31d | -13.55925 | -46.91786 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e03037a-3c45-3378-b5d4-97cb6c5134af | -13.40716 | -46.84897 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e4f5410-0f47-31f9-a8a4-251f1363395c | -12.82606 | -48.16955 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7345b69a-f95c-3d0d-a122-123ac7957ffa | -6.53405 | -44.10601 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfeae789-959e-3fb7-a67b-56428cc7d2a7 | -5.85645 | -42.94997 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 96178b72-bc34-3865-8e19-db26760c4738 | -13.47411 | -46.85034 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| da79d072-4a58-32b8-a003-32d77b079474 | -5.53527 | -42.6599 | 2025-08-29 03:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 620a65b3-5da3-331e-93e6-f800296e3c2e | -6.44564 | -44.57181 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d65986-cfc5-3523-94be-500961167c09 | -12.06499 | -46.62801 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41a7bd15-6454-3b74-a4a3-fdd065fa4227 | -13.40605 | -46.98824 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc8708ea-07fb-3b42-a637-00c30c0e0bf3 | -12.83919 | -48.103 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5204866d-4df6-38b0-8475-e01bb49074cc | -9.67189 | -48.3289 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30534330-e066-3dc0-ab59-5f2c038529b1 | -12.83159 | -48.16953 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cd8d565-9d5b-3238-ab66-552b2069f74b | -13.42823 | -46.9544 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e834738c-a188-31da-8e97-888ce03fbc14 | -13.41232 | -46.9828 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cab8e6c6-a118-3d03-902b-5b49b354c4f5 | -6.13621 | -44.05586 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 621a6cb3-176a-39a0-988e-7ddeb6f2c8dc | -12.69994 | -48.201 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ebd23056-4d64-36cf-b76c-dc3396b5d796 | -15.03291 | -45.65714 | 2025-08-29 03:49:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9eacf60a-98b0-3f18-90d7-87f57438f730 | -5.87257 | -42.96433 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a04b9d8e-2323-36d5-a6ce-599a84610c4a | -14.24508 | -48.06782 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba5b0f38-6572-3722-9470-fcdf229cb464 | -13.5889 | -46.87089 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bce7aa8-78d9-33e8-b1b1-7a0566772d13 | -13.50004 | -46.8499 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca3cb672-3aaa-3b08-b4e7-4dcbfd243ff8 | -5.83178 | -44.10715 | 2025-08-29 03:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67454587-bd1d-32bb-a191-527c4d46a609 | -13.53313 | -46.94568 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c3a0244-0bc9-39f8-b84f-ee3f1c12e98a | -10.02139 | -48.07171 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
