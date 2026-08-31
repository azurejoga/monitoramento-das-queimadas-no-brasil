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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e8ae284-6ffd-3b49-9aeb-b6da15b4c320 | -19.11072 | -39.75737 | 2026-08-31 16:28:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b2f532c3-6f74-3473-b9ae-de46ce823f38 | -14.31798 | -42.21896 | 2026-08-31 16:28:00 | NPP-375 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 22c14cb8-18eb-3521-bf8b-133e0428a639 | -17.86592 | -52.09667 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.0 |
| fa7cbf4d-8c41-33f6-ad7b-7dfe677c407f | -16.28527 | -42.58302 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 86bee4e8-71c1-3aa8-aadd-7d7136a1e57b | -15.11783 | -40.04494 | 2026-08-31 16:28:00 | NPP-375 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f809b8df-fe07-3187-9c2a-8bdc8a8fe98a | -18.264 | -52.71803 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 5811d468-4d16-3105-a58c-3295e6c300e8 | -17.86009 | -52.10242 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| cfced517-e1f2-353f-bd5d-45c23b361f34 | -14.99193 | -48.15585 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d03e013-b04d-3a15-9bc4-43147108d951 | -16.5583 | -52.52309 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2506f533-eebe-3819-b341-712aeddf12f4 | -15.19534 | -46.25252 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 02ad3e62-2b05-3ab1-8390-bd0e66fa8ef4 | -19.20279 | -45.47348 | 2026-08-31 16:28:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 52dd5610-ba96-303f-b6e9-d4a3ece2645d | -15.18725 | -46.24632 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b780f28-030e-3507-8a72-34beb50f15c6 | -15.42882 | -41.21262 | 2026-08-31 16:28:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 18ed2367-c5d1-3084-814f-c4dcedb5ab8f | -15.01949 | -48.18563 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2954b34a-5426-3deb-882c-85b06d785465 | -17.88767 | -52.10314 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 924f22f7-c81e-3b73-9e7a-bb4c1a2dc701 | -17.84987 | -50.49674 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0870cb9c-baf9-3ca4-8869-efbf3970cca1 | -17.50284 | -44.22849 | 2026-08-31 16:28:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 07b0667a-b5f7-3df7-8276-ea18891cdf32 | -15.67195 | -45.92947 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfdbbc6b-7993-322c-9c09-b43048646cbb | -15.66629 | -45.91836 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2d522003-c289-310c-a13f-569bf15e7603 | -17.86668 | -52.08345 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9fc6f40e-3db9-3835-acda-0b32c30aea00 | -17.88167 | -52.17739 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bc898dab-fe1a-338e-9f3d-b6c3091af3cd | -17.35764 | -45.81079 | 2026-08-31 16:28:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| daed8eec-5d7f-3a58-95d2-d033c35dc14c | -19.1538 | -45.49599 | 2026-08-31 16:28:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e049d00-7d70-38c1-81d9-cb8992ae21f6 | -16.2876 | -42.57454 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fbfa6987-4ebe-3140-a94d-bc3b873c04f4 | -19.84306 | -47.92679 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 9ee682c8-c530-3c5a-a09e-44ed5ef4c5d1 | -17.85001 | -52.11115 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| da011a2c-fb1a-3c04-8502-a594006fd05a | -17.87987 | -52.08783 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 585.0 |
| a23d20ef-11f1-35dd-8a28-51300e7f6818 | -17.88072 | -52.11702 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| deea2add-37f9-31a6-b20c-b5216d269760 | -14.86547 | -40.73113 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e2314807-ac35-38cb-b9a4-d49c258e5f80 | -15.02425 | -48.1851 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c9d72524-a4d5-38f0-92a9-2328bc24b178 | -17.86081 | -52.08908 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 4c9ab461-7d50-38e3-b2fd-a614b0f22859 | -17.85764 | -50.51613 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| ab227465-aea1-3799-8631-acd7f4b8f300 | -20.82449 | -42.27152 | 2026-08-31 16:28:00 | NPP-375 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a39a9fee-f049-3554-90d4-20d9bfa2fc33 | -18.26193 | -52.74979 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d7ca555d-d206-3887-af83-bd086897060e | -17.95145 | -44.57655 | 2026-08-31 16:28:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 01c82200-50e3-3e57-805c-293f793a0fee | -16.55139 | -52.51878 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d35f10e7-714f-375a-b0a1-359181136930 | -17.84495 | -50.50554 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 5183f050-fa07-3407-884f-524f39a597d2 | -19.9127 | -47.96095 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2400f26a-b09c-37a9-9407-fe2a96a51a26 | -17.87761 | -52.08552 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 636.0 |
| f39412d9-48e2-358f-809d-e9659bd5cb9b | -18.74825 | -40.55253 | 2026-08-31 16:28:00 | NPP-375 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 1d026f78-293e-38e5-877f-c65bd253e16a | -17.86339 | -50.51553 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 9a002906-18e9-33e5-b648-c06dea8bff16 | -18.93065 | -40.23903 | 2026-08-31 16:28:00 | NPP-375 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ac7e1d4e-6ff6-3f6b-8612-89ae7e61f883 | -17.59457 | -46.49063 | 2026-08-31 16:28:00 | NPP-375 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1908ac6e-4472-309d-bddc-2422b45549f1 | -17.86747 | -52.11252 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d596876f-2c88-3233-b3d0-81dcf62b6c7b | -16.55335 | -52.52145 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ecb616d4-ccab-3387-b6b6-196a5969f621 | -16.57199 | -52.51342 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 282a22e9-c945-3b9a-8afb-537fe05fa013 | -20.15898 | -42.17685 | 2026-08-31 16:28:00 | NPP-375 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 1beccde5-f6a1-35da-83f6-bb36ee6b0582 | -16.20044 | -49.31551 | 2026-08-31 16:28:00 | NPP-375 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9821081-6b74-33cc-8a88-34eee03054cf | -16.86353 | -48.27693 | 2026-08-31 16:28:00 | NPP-375 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e8a1b24f-83c6-3213-8101-a3e652ae1bc0 | -15.61262 | -41.52514 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 530c8cf7-b305-3f33-a49b-03b5591aae58 | -18.94908 | -40.15688 | 2026-08-31 16:28:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 9d024a95-c4d8-3e6f-b6cd-0f86b2992adb | -18.26322 | -40.55296 | 2026-08-31 16:28:00 | NPP-375 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 4767b590-a78e-3514-b37c-ef0d120f879d | -17.70691 | -49.23027 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d95bf42-bebc-3348-be29-c2ff3b322328 | -16.57253 | -52.51905 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| aa30a7fb-e16b-3937-98d5-35df332fd624 | -14.51143 | -41.17858 | 2026-08-31 16:28:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5614988-3547-30af-adb9-5755443e6be6 | -20.25005 | -40.7502 | 2026-08-31 16:28:00 | NPP-375 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| f19c58e2-413b-3598-912d-1e89c8ca5738 | -19.06873 | -46.21009 | 2026-08-31 16:28:00 | NPP-375 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0a5f52db-967b-39e8-848b-74f22a88a432 | -16.01499 | -54.40853 | 2026-08-31 16:28:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7e0666e4-5712-3aea-aa33-af0a42660e64 | -16.00068 | -43.55886 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e26fad2c-8540-32e8-a174-0722444eeb8b | -16.55282 | -52.51589 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ff71bd91-bd89-3a7b-b391-50bddeb43071 | -15.68414 | -47.31527 | 2026-08-31 16:28:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d03e49e7-f1e4-38a3-834d-fde148679f9a | -16.86912 | -48.28233 | 2026-08-31 16:28:00 | NPP-375 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f33a49a0-61c7-31f0-a2df-31a2e6b18449 | -17.87864 | -52.09595 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 279.8 |
| dedaf935-b700-361b-ac0e-3a88f8cffc83 | -14.54367 | -39.74375 | 2026-08-31 16:28:00 | NPP-375 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 65b27225-caf3-3041-b907-d6ed77c3d0fc | -17.87331 | -52.10674 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6147c407-1540-3d12-b785-cdd90ac2e444 | -18.26707 | -52.75287 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 1029a09d-9594-35c1-8f0a-12c3da6fd7d7 | -14.80217 | -40.66864 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c701ae96-8c13-3034-ad23-8df4a2893c3c | -17.85068 | -50.50472 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 238.7 |
| fba2af6b-d869-36a7-b759-be3ccd49107d | -15.10557 | -39.58435 | 2026-08-31 16:28:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dcdd7259-1f02-3c43-b0ff-0a5c7eb6ab88 | -17.76554 | -42.28437 | 2026-08-31 16:28:00 | NPP-375 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 50189c76-d358-358d-8af1-ade6909b17dc | -19.82942 | -47.94043 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 95fb32c1-0bcb-3075-ae2d-17969cc386b8 | -16.56355 | -52.51123 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e4918edf-2eaf-3afb-a1ae-101fc1549b5f | -18.9641 | -39.97339 | 2026-08-31 16:28:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f515a953-4a59-36af-8f52-44302be4d582 | -15.17815 | -48.71719 | 2026-08-31 16:28:00 | NPP-375 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c021e7c5-c565-354e-99d7-9ab386084d75 | -17.85589 | -52.10535 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 03cac74c-3433-320c-99e1-0b447dc9ddfa | -16.89524 | -40.21912 | 2026-08-31 16:28:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b89d26ee-8bc4-3795-ae40-e5ca8d8a228e | -19.74847 | -47.89088 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5561de75-ea2d-34c4-9adc-4a17339b1469 | -15.64405 | -50.09889 | 2026-08-31 16:28:00 | NPP-375 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9407f4b2-45ef-39ff-a1d3-4ab17e487655 | -18.2157 | -43.97293 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ef8eb639-d12f-313b-90ce-d14fe1817057 | -18.47217 | -43.9679 | 2026-08-31 16:28:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5645bcd5-9660-3f6d-84aa-fa221ebe0d97 | -18.9101 | -50.88283 | 2026-08-31 16:28:00 | NPP-375 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| ac486657-16b6-3534-896b-24f0c74f8e95 | -15.6847 | -41.07828 | 2026-08-31 16:28:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 86e3618d-4c58-3a2b-8a7f-0ba3f4af70a6 | -16.70584 | -43.89248 | 2026-08-31 16:28:00 | NPP-375 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64b8ed9-a5a1-324b-95a8-3189aba1ed28 | -17.87494 | -52.10381 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 0d98e6a8-1c85-3632-b5e8-a38f187737ae | -17.8681 | -52.099 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 4144e324-1fa3-31cf-8923-00f2c9ff506a | -14.5431 | -39.74009 | 2026-08-31 16:28:00 | NPP-375 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9e6c9c41-fe0e-3c98-8f96-4eed82141171 | -17.45236 | -52.41273 | 2026-08-31 16:28:00 | NPP-375 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3d3c5eab-5644-3f3d-b339-38f7dce099e4 | -16.24105 | -48.32544 | 2026-08-31 16:28:00 | NPP-375 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| fd3ec772-f443-3b14-9c8f-3cabd41df777 | -17.7118 | -49.2261 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 40af6c8a-0cfd-342e-adb3-398ae507deac | -16.7123 | -47.64346 | 2026-08-31 16:28:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 327731c5-fd23-3c5b-a15a-85c9a0ceb39f | -20.75201 | -49.72004 | 2026-08-31 16:28:00 | NPP-375 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2c3de17f-16f0-362c-9d8c-ed0428dea441 | -16.28816 | -42.57846 | 2026-08-31 16:28:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bb8945ac-e5a3-34bd-b4dc-79d19b8ff8f3 | -19.42319 | -41.07613 | 2026-08-31 16:28:00 | NPP-375 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d0cb5f3d-8246-3bdb-9441-ce1eeff1c638 | -17.88051 | -52.18022 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 99a9a61f-8899-399d-87ba-963b9781c801 | -15.53753 | -45.9158 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0830c23a-e91b-39a9-8b26-1e4e45402d82 | -15.0245 | -40.9547 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| f661bc8f-8ae3-33a9-9e53-d93ed6dac0e2 | -17.85559 | -50.49593 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 748e9362-07e4-30c2-be6b-20535f4aea98 | -16.55232 | -52.5107 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| dc02b7e3-0d87-342e-9f63-d77386a524aa | -19.11405 | -39.7568 | 2026-08-31 16:28:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 452cd4ab-9c3d-3c26-b089-3399c286f4b8 | -20.17628 | -41.86182 | 2026-08-31 16:28:00 | NPP-375 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README113.md)
