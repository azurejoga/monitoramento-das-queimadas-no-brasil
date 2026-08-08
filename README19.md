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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b41dd0f-51f3-3cb5-ac39-c9e84faf300b | -15.09894 | -52.73155 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107e70ca-85b2-3492-a1ec-c9c772a6f4ce | -12.35347 | -48.20508 | 2026-08-08 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a73ee625-2c68-32f8-b518-31547dfea0d4 | -11.15983 | -54.85486 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a078bd43-8112-334b-9f9c-e76a15812aae | -13.82494 | -53.69082 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d2ccd19-8118-3750-8379-415de74538b1 | -14.35812 | -54.88636 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e26fc94-3391-3b36-a17b-6279cb604b8e | -12.54101 | -46.94894 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab36075f-5b69-3a54-9084-3c10c8851bc8 | -11.19719 | -54.84216 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 312df266-1d54-358b-a15f-7591aeaa05c1 | -14.9312 | -48.26168 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5e11d59b-a0b9-39da-90a5-5fac8d776499 | -14.32183 | -54.96531 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e9d800-40b5-307f-a7aa-3df5f6f0f365 | -15.69618 | -54.83424 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87993454-dcf2-3608-a41a-e51f1ef947f4 | -11.66955 | -50.11302 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 043e29e4-7577-3b4e-bbc5-f4a9a2f6428d | -12.33332 | -53.15822 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eecc8a0b-b52d-37cc-b6fe-12af52a40ef2 | -11.11527 | -50.76634 | 2026-08-08 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c65ec7a4-2a39-37d6-9089-ffcc0c6e30e0 | -21.36782 | -45.13207 | 2026-08-08 04:46:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f20d6d77-8f0b-3d00-afcd-8e9bad011142 | -13.83856 | -53.7377 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67bcf36b-3700-3298-a03d-2e8fb309c993 | -14.20217 | -53.32308 | 2026-08-08 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eaa8771-8040-3ad9-bcfe-9e664fdf007d | -7.55072 | -61.1565 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21c67ede-86ce-30ca-b62e-000a44d233be | -14.37078 | -54.96539 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f4c77ddb-144f-3b2c-94f8-d9ab56d2b27e | -14.92725 | -48.25815 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9911a063-fa4c-34fb-95d6-4dd176e42464 | -12.34993 | -48.20452 | 2026-08-08 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 653fa0e4-e343-3dd9-afa6-a427e9bc2c20 | -14.92916 | -48.24511 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bacd1d55-c30f-3cbd-a427-145c61099d4b | -11.26944 | -55.86173 | 2026-08-08 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8121495f-af48-3d79-a836-b64f36bad619 | -15.6997 | -54.85665 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8988a69-728d-3c1b-a816-a621e1904b4a | -11.72505 | -50.12539 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ace1640-5239-309d-838d-fac49eb33238 | -10.50007 | -46.71653 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74222392-b33c-311b-8c80-7429f415c3d9 | -11.01323 | -50.5305 | 2026-08-08 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9d57b5d-54fc-311c-8ce4-d71b105bda4a | -8.15203 | -55.42443 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb7691d2-a636-3881-a261-5965acc0f5e3 | -14.31355 | -54.99105 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67b0eaed-190e-36ba-9e5b-8fb93e18df42 | -15.6969 | -54.83001 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f7a9225-1a39-3be3-ada5-c73196b0050a | -11.83885 | -56.94472 | 2026-08-08 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a5e638-028f-30db-98dd-035231b7cdb8 | -12.5399 | -46.92927 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7497d5c-d134-3aab-8b6d-5df70417bad6 | -10.26457 | -45.81641 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5de13458-599e-389e-b989-284d0b14cd9c | -11.15027 | -54.84617 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a90e694f-3b6c-376a-b184-bb967c76581c | -15.11245 | -52.72638 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0353833b-502d-3f07-95f0-dee68d814808 | -14.42012 | -45.65415 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe09c30d-5f35-34b5-a097-3770ef119169 | -16.18195 | -46.2212 | 2026-08-08 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74bdca41-f36d-30cb-a874-f632dcf2bbdd | -12.54167 | -46.94419 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 32b5785f-f0a6-3ec5-9e6e-475100907002 | -15.38434 | -53.79124 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27812603-1d03-3eb0-99eb-1eeb7e2309bb | -12.3443 | -53.15616 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54809669-1998-3f9d-aace-bd7f6c908e86 | -12.5244 | -46.98463 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 065a7aa0-799a-389a-ad4b-44057db77de2 | -11.70612 | -50.14066 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12bc5d8c-872f-301a-8778-ed3feca03e32 | -12.52687 | -46.99453 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd3e681f-a981-3377-84dd-3adf3369f302 | -14.41491 | -45.65808 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 290436be-8490-3fc1-a70a-ec3f2b731eef | -11.3102 | -44.8356 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0a81245-3ffe-39c5-8a83-4d316a78e20a | -12.54477 | -46.94967 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c57e799-8493-3ba6-8f99-665b2550caf5 | -14.31798 | -54.98729 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a268b2c9-7ed5-37dc-b8b1-c094008c8cdf | -15.70042 | -54.85243 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24c6d489-364a-3f0e-9ff1-27a5ef7a4d61 | -14.30989 | -54.99039 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae6b123-eb03-3ddc-81c6-1c5d7d73c15c | -14.00423 | -53.8344 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420f3af3-fd70-36dd-a84a-0db652e984b3 | -14.27489 | -45.28254 | 2026-08-08 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65440034-c223-3331-b0b4-6b848ea66eed | -12.54972 | -46.96933 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23c3ea2f-a1f9-302f-8481-037827fba1f8 | -12.32643 | -53.15703 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e8a4ab5-e8c6-39b1-9b0c-1b6f2f6e6ac7 | -12.52818 | -46.98518 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6d0741f-a7fc-3a84-b5a8-05f409dbd062 | -15.70552 | -42.18521 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a60749b-2f90-359c-940e-20bbc5f51b22 | -20.85869 | -57.50161 | 2026-08-08 04:46:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b27725de-01eb-35b9-9b09-67e6b96c65cb | -12.14227 | -48.26645 | 2026-08-08 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb34612e-374e-38c1-95c4-81d07b110426 | -14.27865 | -45.28735 | 2026-08-08 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32e2e99-59f0-3615-b264-867f4a602e98 | -12.54123 | -46.91981 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 999deef2-9992-3131-bb85-c02e1e0ad1c4 | -11.61529 | -54.57809 | 2026-08-08 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b656a66-739c-3294-a6b7-bccc689d5a9d | -11.01599 | -50.53454 | 2026-08-08 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847fdd4c-6ef8-3fcd-bead-d07bd7f0faea | -14.41967 | -45.65467 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df0aa648-420b-355b-8751-5cd685f333a3 | -10.9198 | -50.2823 | 2026-08-08 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36f4de01-d34d-38da-b388-b7c18fceba4d | -10.27023 | -48.25956 | 2026-08-08 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add4876a-a3ac-3255-8be4-42672cfc183f | -12.54906 | -46.974 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00c5b9ba-0151-3f5e-88b7-9a867889504c | -14.9285 | -48.24955 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d3097ff-0f87-34d7-96d4-9336e816a7ab | -12.53809 | -46.91454 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c19ec14-f671-3f71-8590-5039b3bab390 | -15.70888 | -42.18536 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e9b2b2-0937-38ac-b594-5dd0bba1beaa | -10.50543 | -46.629 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4671594e-8888-31d6-b521-f043449df43c | -10.27237 | -48.25915 | 2026-08-08 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a79e89-5612-3155-9c1b-82b3f1e39f66 | -12.85694 | -52.81809 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0831bb1-8a28-3713-96b2-eb2bfbc83fc5 | -17.54518 | -49.63424 | 2026-08-08 04:49:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e431d301-04bd-3367-8fdb-80ac7aa67898 | -19.78667 | -43.73269 | 2026-08-08 04:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ac3c604-7663-3f56-9103-e86a4170b41a | -18.51031 | -48.34093 | 2026-08-08 04:49:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce96bca6-390c-3ea3-a027-c414907aff77 | -18.95237 | -50.62893 | 2026-08-08 04:49:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5fd721bb-5117-3f2f-a1dd-4f9f15978835 | -18.21877 | -44.35426 | 2026-08-08 04:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e5fb7eb-291c-36a6-a801-da0d9cf1b2b2 | -18.35092 | -50.72152 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9c42be-fb1d-3386-845a-49c77642e8f8 | -17.5441 | -45.2824 | 2026-08-08 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f253b73-82eb-3f2b-af2b-22ce02da2fce | -18.36001 | -50.70735 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9d8413b-cb24-3e94-a683-ec2252867f34 | -19.74276 | -45.96577 | 2026-08-08 04:49:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b651df-0be0-3e49-b06b-970fff8bb236 | -17.77316 | -50.44654 | 2026-08-08 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a65af379-830a-3286-a6b0-32c350fa189f | -16.6882 | -51.34526 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad1c2f5c-2e8d-3a09-bc50-a457ee0fbfbf | -18.36127 | -50.70221 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2d085b89-f104-3c1e-a82d-3b30590a392a | -18.95295 | -50.62502 | 2026-08-08 04:49:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bdeb46a-4a47-39d0-a989-c8c97fd79182 | -18.21965 | -44.35817 | 2026-08-08 04:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 36f12ef8-426d-3336-b28d-c9c539186377 | -18.3658 | -50.69507 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 11a05613-9eb3-34a3-9abf-35496c82c02d | -17.77259 | -50.45039 | 2026-08-08 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c867dc16-7005-3888-8573-07a954fb193c | -16.68208 | -51.3628 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e275a6a-dadf-3e14-8980-76e35177beb5 | -17.87867 | -50.53712 | 2026-08-08 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e82877fe-f647-3a54-a21c-e5cb3658c6db | -18.36014 | -50.70989 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b91a720c-a4b6-34bb-bdcf-d667a8a73f2c | -17.57612 | -49.66811 | 2026-08-08 04:49:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85aa4dfa-9ce8-36cc-92d5-909524ed891a | -18.00214 | -50.01046 | 2026-08-08 04:49:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a73483ab-92cb-3190-ad8d-c93ae0385ec6 | -18.95579 | -50.62948 | 2026-08-08 04:49:00 | NOAA-20 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce6fb291-294f-3dba-8ccd-b54610fc391a | -18.21815 | -44.35983 | 2026-08-08 04:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f329c88b-02c5-396a-8c6e-9045595acaa9 | -19.85628 | -43.46822 | 2026-08-08 04:49:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0edefb2f-2542-3a69-9e8c-10081fdfeba7 | -17.54352 | -45.28713 | 2026-08-08 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c768ffea-8494-34fa-a8b9-c67f485139b2 | -18.36524 | -50.69892 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 56a373bb-897b-3060-b4a0-d70ad487eb11 | -18.35035 | -50.72531 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc353fef-871e-3a89-ab29-b4d5e8a18ccb | -17.88492 | -50.51851 | 2026-08-08 04:49:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5b24a64-8756-3de6-ad09-2dc4b2beb2de | -16.67987 | -51.35501 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e13f8363-b028-3bc5-9263-147283d6f330 | -17.88156 | -43.7762 | 2026-08-08 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
