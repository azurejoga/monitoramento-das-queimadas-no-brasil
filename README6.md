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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68fb46a1-1f8f-3fe8-9266-b63af4c91efb | -6.70174 | -44.35264 | 2025-05-24 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d1c2c2b-2285-30e6-8f94-9d79b12f8b18 | -9.489 | -40.34009 | 2025-05-24 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| bcfa69f4-1eeb-3e8c-846e-3e3f7575776c | -6.21948 | -43.34922 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4b10821-6bd1-3b60-b3db-b4d77d868786 | -7.48613 | -43.38272 | 2025-05-24 03:45:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d28f11a-dc90-3f03-89a5-a39a47395a23 | -7.66347 | -46.10629 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6329d67-5bee-366d-aefd-fbacd79e9048 | -7.2306 | -43.11778 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9ad50e3d-5e16-3b6a-b5dc-ab8f719e64e9 | -6.22033 | -43.34887 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b63a235-e608-3414-bcee-730c54379666 | -7.19488 | -43.13191 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f87687e-afe4-305a-90eb-75bdbc20d9e2 | -8.75233 | -48.04184 | 2025-05-24 03:45:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b968cd78-66f9-31e3-9859-5fcc47eab13b | -7.22185 | -43.12016 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 539403f4-71bc-38bb-bb5b-0a552c0032cf | -6.22651 | -43.37329 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 014a99a6-132e-3e32-9f8f-288489e2aa93 | -7.20932 | -43.12511 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 80174583-f8b0-3663-a6f6-7857917b825a | -6.95265 | -42.80449 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 235aff48-bed4-3e4c-83fb-25565c4e5b37 | -5.34665 | -43.75144 | 2025-05-24 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6b4c522-bf17-3412-b238-7bb629fcb066 | -10.03027 | -48.70137 | 2025-05-24 03:45:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6d5eafe-9dbf-3c47-8e77-98d34f1e1002 | -4.29265 | -48.28091 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f3b8cb3-5a29-389f-aa86-c414223368c1 | -7.53619 | -45.82939 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53182098-c58a-3049-8684-0c4607d70b34 | -7.6568 | -46.10962 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44386d2f-d7f2-3d29-b7c8-5ef28dfe9180 | -4.28688 | -48.27246 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fa80d835-4560-3cc2-82e6-afa283b1a3f0 | -6.61839 | -48.014 | 2025-05-24 03:45:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b267da4-c380-37d6-8635-27e8f07f0be5 | -7.21701 | -43.11933 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26bd9b2e-76a0-3b2a-bc21-cc8d87b1d930 | -8.07324 | -43.12229 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| e72e2094-2a56-3818-a772-4dcf7aa98966 | -6.94881 | -42.79849 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f47d774c-0bd3-30b8-8215-05ba0283b7c1 | -10.73032 | -45.16026 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5a37b55-89f7-3003-89c2-c82b7c7eb2ab | -8.37216 | -47.09195 | 2025-05-24 03:45:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4cb66a0-3420-3c28-aea7-de8272fafb4c | -10.46204 | -47.94896 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1486baa0-ee1b-3837-8b02-b1f3fc31d62d | -7.95085 | -46.82263 | 2025-05-24 03:45:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e7c2052-51ee-335b-a027-1cd60da30a0e | -7.65763 | -46.10518 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d3308dc-ba86-3cdc-aaae-0c108f748dc9 | -6.61161 | -48.0133 | 2025-05-24 03:45:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4fdc16f-5f6e-38cf-bf9a-edfbfdfa39b5 | -8.07925 | -43.11613 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 4e1f52cb-d94e-3b15-9dcb-c16c86304f06 | -10.876 | -45.07345 | 2025-05-24 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d96c7c6-2bd4-3c11-96f9-3f64f1b21419 | -10.73107 | -45.15677 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be69442c-4676-3b4a-8af5-0e1cdd4124b7 | -4.28989 | -48.27894 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 21f382c2-93bf-31b5-921a-66dea21ebd9d | -8.07193 | -34.97713 | 2025-05-24 03:45:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c60191ca-c896-36e6-aff8-f50fa5e06ada | -10.49316 | -42.41913 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b2c6e9c-0471-3b30-b24a-413c28ba7631 | -7.07138 | -44.93666 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e3af3c0-d317-3a0c-8b69-810726f3296a | -8.07356 | -43.12037 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 877f44d9-9f42-3d57-b6b2-80e1b1bc105d | -6.2235 | -43.35563 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0245b77-07c8-3190-95ca-64f6d5e0a707 | -7.21996 | -43.12148 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| af1de91d-727f-31b0-9292-0161d8f5d2b0 | -6.22449 | -43.35001 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d3cb70-34b0-3b33-a172-ffd6c93bca50 | -7.21417 | -43.12594 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 91a34de1-60fa-3b88-a6d6-d4db90a78ccb | -10.35958 | -47.98957 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64825e1d-90c1-398e-845c-42ad1ff1e0fb | -9.49205 | -40.34564 | 2025-05-24 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2df37101-64be-3de2-87fa-030dc59a9418 | -10.4924 | -42.42334 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bfc2daaf-3340-300d-935c-b1fe5eabaf74 | -6.2215 | -43.37237 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017885da-9b9b-30d1-9f37-f2ad87ec4cd4 | -7.20837 | -43.13042 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6ba332ef-52d3-3d61-9516-a6c05210f8f0 | -7.19973 | -43.13276 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7d0066b4-8b60-3b10-8789-21c9184a0b31 | -7.65987 | -46.10369 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83282b5f-9b42-3455-9381-cc51567026f9 | -8.07449 | -43.11525 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| fe3d7926-579a-3139-9cd2-b0675449b3ca | -6.22534 | -43.34969 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97316518-a3bb-32d4-8026-8efae1b7f04a | -4.28561 | -48.27974 | 2025-05-24 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| acbc0881-04b5-3a9b-aa7f-88cea80212bd | -6.22752 | -43.36206 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fbd4cc12-c7e6-37d2-80b9-e8d33a39855a | -6.94942 | -42.79729 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ee3825d9-f014-3f36-af32-5cb7bc8119a5 | -7.21125 | -43.12378 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0017c916-3870-3978-b560-ae56fe22a9cc | -9.49594 | -40.34631 | 2025-05-24 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f18c028-e96b-3f69-8e76-1493fd4c0905 | -9.73129 | -45.42609 | 2025-05-24 03:45:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68b9462-0738-38c6-a6f2-f5c85340935a | -10.46928 | -47.94516 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf3dba26-3b5f-3c3f-95d3-5ebfdd395ea2 | -7.2161 | -43.12461 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89ce37f0-2492-3a09-813b-da7d1b5cc098 | -8.07889 | -43.11803 | 2025-05-24 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 4c0017a6-1fa1-33d1-b5ca-4f245b252666 | -7.23245 | -43.11647 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c3cd8960-1293-38a3-b45d-6d55245d0762 | -9.73064 | -45.42954 | 2025-05-24 03:45:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 409d6b23-19fe-3345-b75c-7d0da82af3c9 | -7.06648 | -44.93242 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2681ee5e-a34b-3444-aee6-f8f978227bc7 | -10.72555 | -45.04095 | 2025-05-24 03:45:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da32286d-2ad6-3c10-bf58-6a0169754ae5 | -7.21034 | -43.12908 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1678735f-b70e-3d2a-81ab-2961b1ed650a | -6.22439 | -43.35532 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8bfa392-3c6d-3f47-8f60-fd003db95d89 | -10.463 | -47.94408 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad46461e-88dd-3504-b971-0b8ae70148d2 | -6.70233 | -44.34931 | 2025-05-24 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5fce489-cfcb-3139-9d1a-377f46b49e08 | -10.55351 | -42.43428 | 2025-05-24 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8b9cea4e-9dd6-3763-a1c8-d48cf22b784d | -7.0707 | -44.94044 | 2025-05-24 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72590c9e-f3cc-315b-9080-d70defe6c24b | -7.55204 | -45.84039 | 2025-05-24 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 826a1e6e-fb19-3c5f-a884-2ed38d7d91c0 | -6.22549 | -43.37353 | 2025-05-24 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1b81258-7122-38fa-840c-6928560ab3c3 | -6.95061 | -42.78839 | 2025-05-24 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3635ae53-c011-33fc-94cd-335d31529c58 | -10.36062 | -47.98426 | 2025-05-24 03:45:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 953f781c-2eb2-3e2d-94ed-6b25720e5d9c | -9.4941 | -47.48435 | 2025-05-24 03:45:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c132cbb7-ed66-337f-80ce-1ae342d86861 | -7.22276 | -43.11484 | 2025-05-24 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 683d4650-22af-3665-b132-14ec15c0204a | -6.70113 | -44.35601 | 2025-05-24 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c486ff3-4db6-3ac9-ab64-6769e017fd54 | -8.74857 | -44.92632 | 2025-05-24 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6acc5729-3edb-3887-bd07-a0fcbc0f908a | -17.56066 | -42.05336 | 2025-05-24 03:47:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 766ea6f6-6824-3325-8a9c-0ea82498d397 | -16.26997 | -39.55408 | 2025-05-24 03:47:00 | NPP-375D | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0119897e-1da2-31e5-ac52-05fa7d64d424 | -16.30532 | -42.77253 | 2025-05-24 03:47:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e211e44c-e42d-332d-ac11-f5b2752fe5c2 | -23.18011 | -52.10951 | 2025-05-24 03:47:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eda77b32-8752-3072-94fb-9cb8ba446b7b | -19.15366 | -41.56794 | 2025-05-24 03:47:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84784f37-b94a-342c-a2db-663faba353be | -17.5922 | -43.19783 | 2025-05-24 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dab04ad8-b6fe-3b31-b21c-bdd370fd0d0a | -22.5388 | -48.81485 | 2025-05-24 03:47:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b8883c5-306c-3e32-8fbd-3a5b69de842a | -13.6884 | -45.26721 | 2025-05-24 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af1d8a4d-2c94-3d19-9d22-8b19e2d390dd | -12.84003 | -47.39405 | 2025-05-24 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5b8eef-a298-32f4-bab5-9c774da0cb16 | -16.68126 | -43.88404 | 2025-05-24 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4074708c-5a84-379e-9c53-f28433a42116 | -12.35561 | -49.93468 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46a39ddc-0c42-3fb5-8c8a-05668db1ea0d | -12.84086 | -47.38993 | 2025-05-24 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e681c27d-40c0-3e24-b7ef-0740c847f552 | -12.35013 | -49.92718 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a16bdef4-c2b5-3f15-8409-dae845309a57 | -10.94409 | -48.15336 | 2025-05-24 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7256109-a1e4-3c51-b272-e19451410da1 | -12.40682 | -42.52646 | 2025-05-24 03:47:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a625453-16e5-3091-8353-c12de1754825 | -11.57473 | -47.62202 | 2025-05-24 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dba0add-4682-3fe7-9e55-aa1c6522e460 | -23.17827 | -52.10926 | 2025-05-24 03:47:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 470c5866-a9ee-36a8-82b4-c6e47c6685d8 | -11.56286 | -47.453 | 2025-05-24 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ce8958a-3e7f-3f11-81ca-1e7b1fc52590 | -12.37962 | -49.98568 | 2025-05-24 03:47:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23b75bf0-80c6-3cb4-8fa4-6846641ab12c | -12.40611 | -42.53051 | 2025-05-24 03:47:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8d6db508-6b5b-3b10-9a08-e1210c99e005 | -13.90221 | -43.81468 | 2025-05-24 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dba6330-3c01-3fe9-83da-5ae904f2927a | -11.56201 | -47.45738 | 2025-05-24 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a590859b-e182-3b07-bacd-5f8d486f91b6 | -16.59653 | -43.40403 | 2025-05-24 03:47:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
