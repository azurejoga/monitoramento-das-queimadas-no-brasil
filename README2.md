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
| 41e1659f-83bd-39ea-996b-fbd94c2dbf19 | -10.06341 | -36.34369 | 2025-01-24 02:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dad70d28-a7e6-3161-bdd0-5a7df2ca8574 | -5.8722 | -35.4045 | 2025-01-24 03:10:00 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 11f49405-4628-34b6-a41b-4220a7f53368 | -5.86618 | -35.42162 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 79c34fa3-d766-33e7-9187-cd58ca3f69bc | -5.86692 | -35.41715 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 67772d19-4aa4-39a8-88a3-999e58fb9ca9 | -5.87139 | -35.41802 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 33.6 |
| c19381aa-7a0d-3057-b123-bd58aa094029 | -5.86914 | -35.4153 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 4e7b0917-1bb7-3dc4-a29d-9d1c6e0192bc | -5.87363 | -35.41607 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 03fa2750-4e2a-3837-8200-a3a064634ad6 | -5.87213 | -35.41357 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 6f2fc265-a0d7-3d95-97f7-8637df72adad | -5.87285 | -35.42054 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 18dd9041-c74d-380a-8a1f-12e613997f58 | -5.86837 | -35.41975 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 62.5 |
| bde3abfa-e50d-3ffb-a3ca-dc168cc124cb | -5.87066 | -35.42246 | 2025-01-24 03:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 1aa7ef01-fd0d-3243-b629-2586df20152a | -9.42133 | -35.9337 | 2025-01-24 03:17:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 68bd6ec5-ab53-3e4c-8818-52ae42d1cc34 | -7.96655 | -35.20854 | 2025-01-24 03:17:00 | NOAA-20 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 614e0b99-1167-325d-90ca-afe0a23e73a9 | -16.34666 | -43.69648 | 2025-01-24 03:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a98a963b-16b3-3cfe-bcad-f039500de7c0 | -6.78461 | -35.16513 | 2025-01-24 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 6f126334-cd3c-352b-b571-2ae5885e7738 | -9.4177 | -35.92861 | 2025-01-24 03:17:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ac93bd8d-f892-399f-a26f-5f591e604484 | -6.78419 | -35.16233 | 2025-01-24 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b3970422-8c3e-3bec-8101-33fa1a1c13af | -17.79676 | -40.01248 | 2025-01-24 03:17:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 51f26bb4-0f78-3ee9-be57-6e44a457de6e | -7.37604 | -34.8861 | 2025-01-24 03:17:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 825cde87-8eca-3843-b3b2-6ec51d5a561d | -6.78783 | -35.16737 | 2025-01-24 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 741c51a1-970d-3d90-a3e4-f08d42e756f7 | -17.67698 | -42.31288 | 2025-01-24 03:17:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b6e0d53-2676-3fdc-9d97-4eb942e5aca6 | -18.63233 | -40.31515 | 2025-01-24 03:17:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1f8622de-f33b-3b17-b1d9-25bcd582db63 | -18.42976 | -40.0363 | 2025-01-24 03:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dc9fabcf-47bc-301d-8305-bdd550e2ff3e | -6.7835 | -35.16653 | 2025-01-24 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1363412a-7569-303a-8f99-6796bfb05aa4 | -12.07817 | -38.0181 | 2025-01-24 03:17:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9a1f97d9-7acc-3115-baa0-073bcea01ef4 | -17.67787 | -42.30867 | 2025-01-24 03:17:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0f71568-c65a-372c-8ed0-88390299b9bc | -6.78854 | -35.16312 | 2025-01-24 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0c08e78e-4a77-38c0-ad46-062757706058 | -8.20312 | -35.14795 | 2025-01-24 03:17:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ef6c6a4-0bd1-3338-b51f-aca83110a3f2 | -9.259 | -60.309 | 2025-01-24 04:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1efa4058-a189-3a70-a776-7357025d54db | -5.27496 | -40.36201 | 2025-01-24 04:06:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4eecbde9-582c-3e56-b92b-5b8c6c8129a1 | -10.3483 | -47.90745 | 2025-01-24 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a64f064e-70ed-3d05-86a2-2695796c416c | -11.26325 | -41.06433 | 2025-01-24 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e287c62f-a4dc-36f8-abfd-2bf926b52cc6 | -8.94175 | -44.24508 | 2025-01-24 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3147c1fd-0d5d-3915-9557-41ba6fb24797 | -7.8633 | -43.08349 | 2025-01-24 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d736dcf-4951-3bbb-85dd-026e95b8a382 | -10.18608 | -36.39677 | 2025-01-24 04:08:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c4eae0b-3944-38e7-b6a9-94db8dd42c34 | -8.41616 | -40.56879 | 2025-01-24 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe2c351a-5897-3353-8748-d7326f9a4828 | -11.2337 | -40.37568 | 2025-01-24 04:08:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6f8f390-d421-39a7-bdae-10019e2fc5ba | -11.03271 | -45.06172 | 2025-01-24 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c64853e3-c23b-37f6-bb97-0acaae382057 | -8.81074 | -44.70189 | 2025-01-24 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9f04a94-ed9b-3f31-a969-97f40cee7381 | -6.64179 | -47.3522 | 2025-01-24 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dab3cea-dbc2-305b-8713-25c4eb50f0ef | -11.02639 | -45.05659 | 2025-01-24 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0b6d8e3-3bc9-36ee-9b71-9f5062887162 | -11.03336 | -45.0578 | 2025-01-24 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49fe02f1-c637-3464-9724-7191c6734135 | -12.18407 | -41.35485 | 2025-01-24 04:08:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c907f10d-9e42-3dcc-881a-729acbedc2b6 | -10.34452 | -36.30423 | 2025-01-24 04:08:00 | NOAA-21 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7cdd7513-a596-33ca-acc1-9cffadd42a60 | -12.04098 | -40.55341 | 2025-01-24 04:08:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22f7d4ae-62af-347d-ba6e-d5501ed6e190 | -10.34897 | -47.90358 | 2025-01-24 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 808d4eb6-7cb6-3fab-b2ac-0660da46dfd5 | -8.94111 | -44.24451 | 2025-01-24 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c7e8478-d4d3-3389-8209-92c4fc31410c | -12.26418 | -43.43047 | 2025-01-24 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f3ec49-4a27-3846-a6b9-dbcbb4495586 | -10.6424 | -47.46537 | 2025-01-24 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6be4176f-055c-31a4-a7db-4263be964055 | -8.9383 | -44.24453 | 2025-01-24 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7678e261-f2a9-3454-b3f0-f66e80926667 | -8.9396 | -40.85397 | 2025-01-24 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 918d803a-e242-390f-83b4-96d1cd90d8bf | -11.97104 | -41.3257 | 2025-01-24 04:08:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2be35528-a32c-3bde-8af2-66e7947e408b | -12.078 | -38.01833 | 2025-01-24 04:08:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75fbb4f4-e7f6-3822-afd7-a98e89b75ac0 | -11.02704 | -45.05265 | 2025-01-24 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2a4c93c-01c0-33e4-bd34-beb7deb49a03 | -10.69761 | -37.04898 | 2025-01-24 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dd23fb6-afb6-35d2-a606-1d808b5a0e78 | -10.55585 | -37.50412 | 2025-01-24 04:08:00 | NOAA-21 | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e73858ac-7dc8-3d51-a9ad-e2fbb0409568 | -8.95843 | -37.62906 | 2025-01-24 04:08:00 | NOAA-21 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0cb4ef34-79a5-3261-ba01-eaae1cd43c92 | -11.27736 | -44.44826 | 2025-01-24 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c71d84ad-b0ff-31ab-a520-08792fdbea9d | -8.91189 | -40.36237 | 2025-01-24 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 65fc21d9-cddc-3643-9504-eb2af92f9561 | -9.44823 | -43.19919 | 2025-01-24 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e573c931-00c6-3db6-8080-4f597a1bc1cf | -10.07233 | -36.34521 | 2025-01-24 04:08:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e08b6d5a-a6bd-351b-90e8-e0f31a264ba3 | -12.13619 | -41.42181 | 2025-01-24 04:08:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45a0d73f-2c5d-3232-a9f5-a68fc56ef7d4 | -10.35312 | -47.9042 | 2025-01-24 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62fc85cc-7294-384f-99d1-6f93ba3439c1 | -9.60896 | -42.13925 | 2025-01-24 04:08:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2d477f7-aec2-36a3-b5c7-5d7d9240f536 | -12.5054 | -44.3503 | 2025-01-24 04:08:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e948ad7a-bfb4-3c1a-9fee-b816eddb729e | -12.08193 | -38.01888 | 2025-01-24 04:08:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7688ca2a-0a28-3736-91e2-deeda1a7d284 | -15.26967 | -51.47042 | 2025-01-24 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64f2a927-7a65-303b-943c-777f7281c729 | -17.7184 | -40.14928 | 2025-01-24 04:10:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c677d23d-1167-379c-b83d-ae956fb8a0f2 | -16.80374 | -42.57397 | 2025-01-24 04:10:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6195c1-796f-3733-838b-7048b78bd3fa | -17.09516 | -43.80292 | 2025-01-24 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ba2e0fa-7731-3e53-bec5-230ab20f6484 | -12.76446 | -44.83564 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c8dc213-1026-3ecd-a6ba-8b9723fa58c8 | -17.67784 | -42.30865 | 2025-01-24 04:10:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59abed10-acc1-3f3a-b5c0-4b2fd9dba323 | -12.74621 | -44.84034 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c6225a-e489-3316-b66d-b60b293e5e47 | -17.59615 | -43.19751 | 2025-01-24 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a73f0ec-0410-352a-9c26-b06a077b34bb | -16.04079 | -43.38515 | 2025-01-24 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c142fb52-8d2c-36a0-abda-c19d9d00529a | -19.45393 | -45.30555 | 2025-01-24 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e998d0a5-4998-3a53-844a-6241dc1eed86 | -12.74402 | -44.83222 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3f53204-bfb5-34a7-8170-ad05e7a3fad6 | -12.76167 | -44.8313 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f342234-33c9-3e03-a367-2505f0a416f6 | -15.27343 | -51.47681 | 2025-01-24 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a975b4c3-065e-3a74-b2d4-79f2ee6a77f9 | -12.7718 | -44.83645 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b734f2a-6cc2-3e07-b86a-413537d3c064 | -17.71532 | -40.14401 | 2025-01-24 04:10:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ae3be3fb-fb25-3426-93df-4a09ff07dbb8 | -16.80709 | -42.5745 | 2025-01-24 04:10:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dd99302-ef5b-3a9a-aa7f-611c7ecae134 | -13.0109 | -44.48734 | 2025-01-24 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7455e0a-7c87-30ca-ba40-b5a309049378 | -15.27071 | -51.46499 | 2025-01-24 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7749e25a-c97e-3a9a-b90f-c1f06b0c3a1c | -17.96485 | -44.93237 | 2025-01-24 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8fbc1c3-8407-3dba-9d08-a45b77870738 | -18.63119 | -40.31477 | 2025-01-24 04:10:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c9f127d9-2386-3e18-84dc-1df37387de7a | -12.74682 | -44.83656 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba37e7e1-8e83-38cd-983b-3dfad7fa613b | -15.26863 | -51.47584 | 2025-01-24 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efb13ec7-0f76-33bf-9014-eae27a1376ab | -15.07958 | -48.94471 | 2025-01-24 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af7020d3-06cd-319b-90f0-cc2f9c16483b | -16.68103 | -43.88376 | 2025-01-24 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3c206f8-cc52-34bd-a97a-caaa8ec1c197 | -12.75643 | -44.84204 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ccc71c3-2e5a-3c19-9a67-2bccf154d968 | -12.74341 | -44.83599 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9875c68f-6bc9-365b-ac6e-702ca231edbc | -18.63493 | -40.31533 | 2025-01-24 04:10:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e5a6ff2b-89f7-3d46-b35a-a0dd6a3afcb7 | -20.27761 | -41.37572 | 2025-01-24 04:10:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51e6d6e5-0677-321b-9ae1-980ba8d95bb6 | -12.76777 | -44.83964 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3530bb29-2d9c-34ff-aeb8-249633ba440c | -12.76507 | -44.83187 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 197d5b7a-f062-3ba2-a827-94a7e5b558c5 | -12.77458 | -44.84079 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7500d5-dbbb-3fcd-97bc-5ea988373041 | -19.83881 | -40.08309 | 2025-01-24 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6e159872-1785-3453-b24e-022aefe77464 | -16.92456 | -43.60869 | 2025-01-24 04:10:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d8058ad-95c1-3d93-985d-5d9eb960133b | -13.01367 | -44.49157 | 2025-01-24 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
