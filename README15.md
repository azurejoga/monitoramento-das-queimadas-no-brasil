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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2b66bba-1981-34a9-a35a-c44652d074aa | -8.30698 | -55.09951 | 2025-07-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ef5b18-a0d2-31d4-8508-91892bc5dcca | -10.37774 | -62.76376 | 2025-07-20 04:40:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa3f6cbe-3bb5-3b64-bb1d-d6e38d0d2e01 | -11.48306 | -47.32062 | 2025-07-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48a64c84-630c-3035-b1d6-eecbcb851473 | -9.90873 | -55.53017 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b85370f8-db70-3224-81ab-2fd95475c7fa | -10.29617 | -60.54773 | 2025-07-20 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0fb998e-24ee-3969-9254-d75eb3d0b5aa | -12.98022 | -46.9247 | 2025-07-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa7f157-5fa6-3682-a50a-34cf09e0eb5a | -10.6748 | -46.79197 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77439f5d-d7c4-3019-9afe-d7026e72062a | -10.54916 | -49.49105 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db297f3c-0156-315a-8b8d-431435e6162c | -9.61414 | -49.01648 | 2025-07-20 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb19ba00-04b1-3aea-af89-eea49c5c3311 | -11.4954 | -48.07659 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f0141ba-4223-3659-829e-defa8b40ad12 | -12.02884 | -63.77374 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bc71c80-f902-389a-89d8-f5790a2ceada | -12.90493 | -48.92235 | 2025-07-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea94b98d-3dcf-302c-9ed9-d33330cfa8d7 | -12.70872 | -45.02958 | 2025-07-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45a82368-b61b-34e5-8d01-cbbbe00f533d | -10.37673 | -62.76886 | 2025-07-20 04:40:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67b0dd80-3e2f-3d16-8ab1-d2bf920bdd8f | -10.54582 | -49.49052 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d237bdd-0213-3ce2-8b2a-b46276dbd147 | -12.01674 | -63.75323 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae723b7-67fb-34db-a7d3-e8795f9b26c5 | -10.66036 | -46.80118 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c2b0d5db-8b19-3386-9a07-27549373d796 | -10.67993 | -49.67493 | 2025-07-20 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e8efda7-551b-34ba-9355-f3ad3f287fd0 | -11.83022 | -47.49923 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8076a2f-6684-3683-b9b3-71b7f211b75c | -11.82533 | -47.50726 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17f3f12a-0069-3c3e-a5d0-ba9db317a32c | -9.90934 | -55.52656 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac428b87-7cf8-37f1-b541-8f4b8db942f4 | -10.01654 | -48.07724 | 2025-07-20 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8707942e-b201-36ce-9187-313cfd19cdcf | -10.6516 | -46.80904 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8ee1c52-fc09-3182-9bf5-0e1156f30a30 | -9.62085 | -49.01752 | 2025-07-20 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da755508-548f-39a5-b90e-585b125f38e7 | -10.29496 | -60.5425 | 2025-07-20 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6aacb0c-ee2d-3f54-ac14-6324f234467b | -10.73164 | -52.5159 | 2025-07-20 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5451859d-c7bb-3ce2-b6e1-a65d139518bc | -9.01252 | -59.53638 | 2025-07-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d138b9-8b28-354e-9bb0-63533b787a7e | -9.80639 | -48.55954 | 2025-07-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af2f8ecb-f8d7-38c4-90ff-17241be710f4 | -10.87354 | -56.09065 | 2025-07-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65052f11-fe79-303f-8ad1-b5194817b43f | -8.9698 | -61.50964 | 2025-07-20 04:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d2bcf80-820a-3c33-8a83-8d144de40c6b | -10.70281 | -46.78231 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 388143ae-2b96-398b-b8cb-ac040bb26b67 | -9.91338 | -55.52728 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d6a041-a424-3da7-ad29-af6fec00da76 | -11.58304 | -47.22227 | 2025-07-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85610127-7fbb-3266-b417-7e2ec0c9a39d | -10.01115 | -48.22171 | 2025-07-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 277a1a1a-67da-337f-9285-b2a9ea2f3fc1 | -12.36589 | -50.31953 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6b35c46-33c4-3fac-ba64-807a3c75de85 | -12.03812 | -63.78233 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfd1f00c-88aa-376f-99a6-bd8f9036f267 | -10.72761 | -52.5191 | 2025-07-20 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dc297ad-2dcf-30a8-b5ed-6e55368200d1 | -10.00861 | -48.22201 | 2025-07-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a75a94e7-a442-3849-85c0-d2ae5b1bfd59 | -10.29688 | -60.54395 | 2025-07-20 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6724796-752f-3e0d-8a74-3af67e4d12cf | -12.34433 | -50.32695 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eff2f69-d05b-3b29-8ec4-e2123a763383 | -12.28969 | -48.78012 | 2025-07-20 04:40:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a61329-3e72-3f04-af20-6d46f105764f | -10.68289 | -46.7886 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca0e631b-7d70-313a-ad12-88572ce7a281 | -12.37253 | -50.32059 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1f98cc4-196c-344a-afdb-d78ac4626c78 | -10.26715 | -47.29079 | 2025-07-20 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1cc03c5-e4d6-36d4-b457-ef26255e5067 | -10.67917 | -46.78803 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b3b5de5-55f5-3926-8bee-143fb22daabe | -11.82107 | -47.511 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404bd31d-1027-325f-9d46-21349be03d8c | -11.83259 | -47.50834 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bed613ea-4059-3493-84af-22508bb1d675 | -13.45213 | -48.02732 | 2025-07-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90e0b062-5f54-31d7-87f1-4a1ca1e24de8 | -14.74403 | -48.27869 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53c6ebce-9c72-32e6-9755-7b4f271d73f7 | -12.03421 | -63.78115 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3db9fae-9cc6-3247-803f-dd2e87d7af97 | -10.663 | -46.79482 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9b570ba7-d87c-3870-9e85-77f65aa92259 | -15.99564 | -49.82049 | 2025-07-20 04:40:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a909a002-f742-3801-beed-f77217fc5b3a | -10.67208 | -56.54666 | 2025-07-20 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 765cf76e-a7c2-3f84-9da8-3f5bf51b706a | -9.93561 | -46.26458 | 2025-07-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5feb0de5-e239-3d09-966c-0b3890d5e750 | -12.57779 | -56.97784 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db516354-1fd8-383e-b8c4-b13095bce046 | -10.67852 | -46.79252 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1f75c2b-9a8d-3643-a0e1-d6ed5b265996 | -10.67108 | -46.7914 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dcf63b1e-4890-3f68-8847-3bbf2e00a32a | -11.15172 | -49.69852 | 2025-07-20 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e493652-69ae-3b69-a7ca-3cfcb04f25a1 | -11.49188 | -48.07605 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ba9954f-f80a-3841-8c65-5d71683a2ecd | -14.71821 | -48.25309 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0e5df74-1c96-3f2b-8861-c4d666ffcf41 | -10.37568 | -62.77415 | 2025-07-20 04:40:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f448490-459f-3efa-b25c-7225319eff2a | -14.75488 | -48.25465 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0f16a7d-b88c-3181-83b9-1fe400e9e054 | -10.68726 | -46.78464 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a4e8467-59c3-3758-b75a-04935d3fc79c | -10.68326 | -49.67546 | 2025-07-20 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa8603fb-036a-3c68-ac3a-374521ef2099 | -10.29423 | -60.54626 | 2025-07-20 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3966aafa-4310-3dc5-83af-c7cddd8494d7 | -12.51707 | -57.24384 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36f9445e-287f-307b-a7e3-d0f9003f4a62 | -10.97365 | -45.10799 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 28e489a8-5960-3f3d-b270-b44f0a340528 | -12.36921 | -50.32006 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd8a2237-90aa-357f-95db-25014056f794 | -10.64789 | -46.80844 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 98124d00-722f-38d5-a48e-36d66da2785e | -11.48671 | -47.32116 | 2025-07-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8a3d88a-a195-37f8-bf75-f517f8888426 | -12.01923 | -63.74149 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8562c323-c503-3341-8ad0-a7a32beee589 | -11.46136 | -48.16098 | 2025-07-20 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a59d3ed-1b00-32f5-9d02-241266da5637 | -16.70596 | -49.35812 | 2025-07-20 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b71daabc-68fb-36f9-96dd-42ab4cef9518 | -12.027 | -49.52147 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c30dcf2a-8a44-3711-8e58-b47f88786100 | -9.80185 | -48.56645 | 2025-07-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6ea34155-ba26-3fed-9453-6ba893ddcb18 | -10.65428 | -46.80268 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 93575379-3e39-3072-bac1-cd41aeb32c8d | -10.87426 | -47.16933 | 2025-07-20 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d5556e9-0148-3d56-b7c5-cefa1204193f | -16.05504 | -48.10863 | 2025-07-20 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4771334-89fc-365d-8cb3-4d0caf8d3369 | -10.65227 | -46.80451 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 95ecf9af-03ad-38ea-b8c3-1943bb992109 | -11.57205 | -47.09657 | 2025-07-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c73480a2-403f-3f59-a92c-c3919e23b73b | -14.78859 | -48.28482 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e9e33c9-5101-3d58-8764-017283fa0109 | -9.47149 | -57.83825 | 2025-07-20 04:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b3a5db8-bb77-37fa-a180-f97c0a8050fa | -11.55791 | -47.08987 | 2025-07-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9af384b-264b-3e54-9751-647c5718d94a | -15.25051 | -46.96254 | 2025-07-20 04:40:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc69b904-8725-3737-993e-a1a544818e90 | -12.01929 | -63.75325 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f653de24-c290-398b-bfe5-af0ed5be15f6 | -10.65364 | -46.80721 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6ee2eec2-74a1-3e5c-a712-62d8572bd6a0 | -10.67043 | -46.79596 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d262c6f0-396f-3a76-826f-c58113a69e25 | -10.62916 | -48.09411 | 2025-07-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8df22187-ed2a-354f-afa4-b32c1014de73 | -11.48608 | -47.32551 | 2025-07-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bf39225-7855-3fc8-a2a3-66f19d6e15c1 | -10.73103 | -52.51966 | 2025-07-20 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62c2254a-f6f1-3c11-876b-f1ad48a90530 | -12.3626 | -46.42926 | 2025-07-20 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31340235-b701-336f-a2e5-06672bfd3f43 | -10.88299 | -47.13522 | 2025-07-20 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f2bb85b-6a98-3c05-aa3f-e9fe2bb71c74 | -13.45632 | -48.0238 | 2025-07-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e95ea3dc-fde2-323b-8d27-13875fa29a90 | -13.45272 | -48.02325 | 2025-07-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92731a6-6798-32cf-91d6-1c92b56addf8 | -9.6203 | -49.02111 | 2025-07-20 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d19366ba-cf28-3aa7-934f-33b057299892 | -14.1533 | -58.20223 | 2025-07-20 04:40:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13f867f2-6aa2-3682-b919-1d7804d9544e | -8.3092 | -55.11084 | 2025-07-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54b0687c-88c5-325a-907a-b47e3baa2c9c | -10.72822 | -52.51533 | 2025-07-20 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17c9fc79-683f-3b81-a154-49b356d3aff9 | -12.37585 | -50.32113 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f28ca999-519d-3304-8c99-4682cb585799 | -10.00908 | -47.18683 | 2025-07-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
