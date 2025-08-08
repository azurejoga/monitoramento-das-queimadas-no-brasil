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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b20e8db-a9a9-38f6-b773-fcc972494bee | -19.23002 | -46.5854 | 2025-08-08 05:01:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cfdd528-db61-3e10-883f-5cc655533f27 | -9.93529 | -60.50217 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22a96d60-165f-3d5a-94a4-5bb1e2d2ead5 | -12.61908 | -48.11254 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4077c5c1-9fe5-3d1f-8171-738d14a75d5d | -13.03674 | -56.86112 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fcf3ac4-6014-320a-b78c-d94e1987e335 | -11.19641 | -51.43481 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2b04f86-a447-305e-a830-cf0fd1351834 | -9.94057 | -60.47152 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 618ba8f3-c693-3a40-ac58-e9dc812753a2 | -13.03733 | -56.85749 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ff559e-42fa-3bfe-9d0e-c6d1d3d7a038 | -9.92544 | -60.48449 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea4a90ef-9a3b-3b5b-822c-f12db8102c9f | -13.03952 | -56.86532 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1803e6c-71d8-3270-89f8-b2867e2c09f8 | -9.70737 | -61.2977 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b6818ef-2c04-3bfc-bc98-9ec374f44722 | -12.71261 | -46.37619 | 2025-08-08 05:01:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a03b251e-6a97-3e5b-85fc-332546459a3d | -12.52048 | -47.12729 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65365027-d7d7-3111-bc6c-ae1c0c747f4a | -9.70295 | -61.29689 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79aa5ffb-86a1-3700-8f93-aacf2390c781 | -9.94297 | -60.50755 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14a2ffc2-ff6b-3eb8-a674-743a97c200fa | -12.71795 | -46.37686 | 2025-08-08 05:01:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06f6baf9-8311-3291-9b61-99a99f94a231 | -9.7037 | -61.29255 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67b0b846-cf69-3de8-849b-3bf35518a553 | -13.0407 | -56.85805 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee71812d-282f-36d2-83f3-30d0b09cbee3 | -9.70445 | -61.28822 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b94a215-d765-3f83-a992-a9c566c32dd6 | -12.55849 | -47.1438 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07baae92-4e7e-3a97-9031-6d9cc7a75b19 | -12.56863 | -47.14484 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 096d477c-a903-374f-88c8-49cdc45e5e64 | -9.71467 | -61.30177 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44b72ce3-cfa3-3604-b1a5-3bab904b9cc5 | -11.75238 | -47.49859 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7cbf631-49ec-31bd-8adc-2dbbd6e50f61 | -9.70664 | -61.29577 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4550fc2d-797d-3d73-bd85-18bc14cef6e0 | -12.33986 | -46.05825 | 2025-08-08 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a786af0-44f3-38b9-a3a2-5b70651b54d6 | -14.81356 | -48.4098 | 2025-08-08 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51924fce-4d60-355b-b14e-bdb2c33d91bd | -9.70887 | -61.28903 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8615f6b9-2ef8-31c6-a0ac-8a7706544341 | -12.61437 | -48.11176 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e06f3e99-dab8-36e6-82e8-2214db13bd94 | -9.93443 | -60.48224 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfb1d141-8dc4-36bf-8a35-1c9977293f13 | -13.04406 | -56.85861 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c952e8-6273-3ea0-ba17-689678f02ec1 | -12.52922 | -47.13906 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 45e1b1b4-53d1-326d-9780-a0a042e21a18 | -12.52238 | -47.11264 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70aa4ab2-0e33-3770-920c-0c1122227d98 | -12.55938 | -47.13662 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 464681e9-dc78-3fc5-898e-1e1fbe373e1a | -12.33829 | -46.06065 | 2025-08-08 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3d364a4-a382-3b9b-9928-611d976242f1 | -11.74838 | -47.51178 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 51a6f545-3e1c-3ac3-a000-05e6cdc49af2 | -9.70812 | -61.29336 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d0eece-2c32-3a8f-a918-bd9bf7261153 | -12.52276 | -47.10967 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78bff7ae-fe6f-376e-8056-3da29a189f34 | -13.04011 | -56.86169 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 733f2932-1384-329a-9329-03193522db97 | -9.71178 | -61.29854 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 765221eb-343e-3404-8e93-2a424e9d6b62 | -12.53889 | -47.13619 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a188ca21-15a2-3d6b-ace9-2569e6ef7d73 | -12.55436 | -47.1357 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80db4322-48a8-35f7-89ab-bdd07c5700c5 | -9.71544 | -61.30373 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 917b4e73-2a63-3f7c-8aba-f97880fc60db | -9.93008 | -60.45769 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0545b020-3983-3fd5-8e14-ba82a9e9ede5 | -9.92961 | -60.48527 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f778961-cf83-3762-a8e3-f81ee572f24a | -16.72586 | -49.13214 | 2025-08-08 05:01:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c150426-038e-35cc-9684-7dde546241d7 | -13.04802 | -56.85553 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdea0b19-c036-3b0e-977b-dba789bbf6b2 | -11.31944 | -55.21638 | 2025-08-08 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| badf96ce-83db-39ce-ac23-ae71a28d8ae6 | -11.74816 | -58.34016 | 2025-08-08 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6bb3f59-7a2f-34c5-a51a-c418b95612d4 | -12.57725 | -47.1579 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ff889a-fe40-3a55-87f4-6a8c7ec0052e | -18.22204 | -45.6277 | 2025-08-08 05:01:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a4d9c93-bbe9-394c-b1fc-db7fd163d083 | -12.54842 | -47.1422 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee3fc6dd-f869-3844-a56a-bf2aeed64669 | -15.17358 | -59.32041 | 2025-08-08 05:01:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 470028a1-7cad-3ea7-b732-53cdd6ecad1e | -13.04743 | -56.85917 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595b9900-0a99-377f-9bbd-04355caec2e5 | -9.71596 | -62.40093 | 2025-08-08 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f601268-8fe2-3377-bf36-ff5fc8b140fa | -12.52418 | -47.13836 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 07d20e0d-8557-33de-a631-b6a4c3a8dd63 | -9.93424 | -60.45847 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37f34251-a64b-3ba4-af10-d8a4d4c98821 | -12.54436 | -47.14113 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5864e855-25e0-3560-96f8-fb03527b7af3 | -13.04347 | -56.86225 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097a665f-6dcd-369e-8f1c-e7888ec6328f | -20.05552 | -47.5853 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 84b1740a-c8e6-32d8-afeb-f0df16ee0229 | -23.3645 | -47.33969 | 2025-08-08 05:04:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56249087-de87-3bd8-9ce1-47cadac960e3 | -20.0548 | -47.59234 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f63e4ce2-8d9e-37a9-8e05-cf4143ab3e1f | -21.35922 | -56.12135 | 2025-08-08 05:04:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8efb5b3b-33cd-355e-becc-b0d4889a6aab | -23.37022 | -47.34016 | 2025-08-08 05:04:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| caceedbf-6083-31eb-9eff-616267501756 | -24.07532 | -48.54794 | 2025-08-08 05:04:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4b5a5a6a-ec44-34b3-8716-0adaadae7e1c | -23.03134 | -47.52869 | 2025-08-08 05:04:00 | NPP-375D | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24b0de9f-61f2-35de-9028-0ba43776ecea | -20.05516 | -47.5888 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6c3f0236-83ef-3bfe-9649-f3f2d11d5aee | -21.38866 | -48.67397 | 2025-08-08 05:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89c746dd-2976-3c5a-8d37-433574e87a33 | -21.68387 | -47.47453 | 2025-08-08 05:04:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3584d84b-1e73-39d4-aea8-0625292baf48 | -20.05588 | -47.58178 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 746a8fdc-8cb2-3b85-a171-46ddac1374be | -20.0609 | -47.58621 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5eeb6059-268b-338f-a316-4b0dcf01d6eb | -21.35979 | -56.11749 | 2025-08-08 05:04:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e3ac7b5-d69f-3937-a81d-6877d295eb6d | -21.38834 | -48.6771 | 2025-08-08 05:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d680020-faac-31ab-ae48-2390a04d185d | -20.06129 | -47.58242 | 2025-08-08 05:04:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73007b53-4c32-31af-ac18-1717577fcced | -21.68351 | -47.47821 | 2025-08-08 05:04:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b9254cc-76d2-3bfb-9843-afeb7e8237a0 | -23.34433 | -52.31562 | 2025-08-08 05:04:00 | NPP-375D | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ee8f207-e03c-3d6e-85cf-71dc940fe756 | -7.0429 | -59.198 | 2025-08-08 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 993461f3-1504-34e9-ad40-25dfbc03c809 | -20.0613 | -47.5897 | 2025-08-08 05:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f809f195-28b3-3f04-8491-60bdbc58e47e | -8.9213 | -60.7489 | 2025-08-08 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 546bc123-e1a0-3e29-853e-6cf99c601db3 | -7.043 | -59.1787 | 2025-08-08 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f730f072-f840-3d44-8c64-931c0be6fa04 | -7.0801 | -59.1578 | 2025-08-08 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a6052d71-fe94-32c9-aae0-a9fbb2f985e1 | -7.0615 | -59.1779 | 2025-08-08 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 231d208e-abf6-371b-b86c-afe1168a994f | -7.0616 | -59.1586 | 2025-08-08 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 72a2a0f2-5a45-3a7c-8602-278ae9e72124 | -5.81301 | -59.23012 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e8aa6574-8c10-3d91-a13a-6265b84d4382 | -7.03937 | -59.18056 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9720c5c4-eed4-34e8-b43a-86e07f1be856 | -7.05517 | -59.19054 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd9f974b-c707-3fa6-8bbf-42e9c467f13d | -7.06139 | -59.17275 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 642878b9-a8a6-3f14-8697-db751d3563b9 | -7.03994 | -59.1769 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2555a7d3-891b-360d-886c-6438144bcea4 | -7.05461 | -59.19418 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| aa2576a8-3137-30de-b42d-045a3db7fb8d | -7.40604 | -60.01216 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fc04f29-4862-38d4-900f-be731d0ef96f | -7.40325 | -60.00814 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe0c066c-b5f5-32bc-93bc-9f1f7b6ea461 | -7.05235 | -59.18636 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb319ed0-a516-33dd-8aec-d44a3302d780 | -5.87256 | -57.75423 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a54943e-0820-3d4f-adf6-25bb7b4c7374 | -7.06252 | -59.16544 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 39c5d957-d5fe-31fa-9f57-79fe4c44b94a | -7.40882 | -60.01619 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12289c59-54f3-375b-bfd0-42db6b5d8f54 | -7.05178 | -59.19001 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a681553-e3f4-3efa-8a34-8b95c44b57fd | -7.40991 | -60.00918 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26d81a0b-6282-3ebd-a4b3-fa5e5e2f54dc | -5.87734 | -57.74676 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf9712d6-17c9-35ab-8097-45ad2f4887ce | -12.61733 | -48.11057 | 2025-08-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80c407df-196d-31f4-ad71-bdc0af0f261e | -7.06648 | -59.16233 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be796974-76ed-3ff0-98fc-33f76bb88a21 | -7.05349 | -59.20143 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a224f3e7-a65c-3e8e-b98d-f0f0437dc29b | -7.04389 | -59.19623 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |


[Clique aqui para ver as próximas entradas](README23.md)
