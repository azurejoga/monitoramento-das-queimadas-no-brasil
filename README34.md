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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b9be5cc-360e-32c8-a1e3-d107a610918e | -6.66905 | -52.88792 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8726f5-1e94-3078-8b7b-4b92c278f366 | -6.75412 | -59.46656 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d1e1dbb-8c93-31af-b3df-9f43ef026f4e | -9.4216 | -60.40738 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3d9b5f2b-128c-3da3-87b1-8ff5ea713e38 | -9.40974 | -60.41469 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4e5d452c-6b67-31c2-af96-509fde069ec3 | -9.80282 | -46.64536 | 2026-08-21 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f69fa37-ef2c-3016-8bf9-05f948376568 | -8.52427 | -55.33761 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91f6c28d-6fe5-3664-a0a6-17857180e17d | -9.39228 | -60.56634 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec84b0fc-c1c2-3d30-a15e-ca27a0890da9 | -5.32217 | -50.95055 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96df75b1-9a84-38c2-bf03-232ed4eabd12 | -9.40027 | -60.55184 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 536d58f5-1ff4-3152-a54c-3acb5035156b | -8.58248 | -54.77657 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79ce59e9-1ce6-370b-b561-0653f7e20998 | -5.60781 | -44.01327 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| d718df5f-6041-3097-af22-e905b45e833f | -8.09109 | -51.66538 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f6cfbbca-8bb3-3e7a-977f-2cc3e0576065 | -6.86155 | -59.44039 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79abaea4-0680-3e2c-9f84-0d4c70fe514c | -7.60123 | -60.95222 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b0e67de-1832-330e-b7fe-134da86ac937 | -11.32662 | -45.02438 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7b13b59-686b-327e-bfc7-f4e6ecef82d0 | -6.8841 | -59.42826 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e07d6be4-6b9a-3ff4-b3b7-eae74b87c021 | -8.89185 | -60.54621 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a382e9ee-9d10-3c53-8283-3f55cb881c39 | -3.76127 | -59.42229 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6736797d-222b-342c-8f2e-6a6056a26217 | -9.40581 | -60.43595 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef19cf0d-0fc0-3462-84f5-53405b90053f | -6.4351 | -52.74265 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da29548d-176c-3aa6-954b-ebf6f930277b | -6.01375 | -57.82381 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8a39a36f-8953-38b5-9741-9f987291886f | -7.36094 | -45.81737 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8f938eca-9ee7-3ccf-b289-4b34b6516832 | -6.89589 | -55.71906 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d2d3d0e-8330-3a83-8b97-2f896d03eb50 | -10.25446 | -54.36549 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cff8a72-dbbb-3ac6-ba6b-909fdbf753c2 | -9.40352 | -60.41989 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 281037c4-3314-3200-b9e0-89fa00e1f561 | -6.89346 | -59.43724 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f788f784-8732-3a52-bef1-abf2a89670d9 | -4.35073 | -59.54078 | 2026-08-21 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f0a42c4-e7c0-3122-ac8e-ce21851f8bbe | -6.11675 | -59.91309 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aefb69ea-4008-37d4-bb2f-c3f03cb36293 | -7.25625 | -49.89381 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1a937a7-8b68-3547-a172-83deef4e25d8 | -7.35261 | -45.81614 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 209b6a37-b913-3da4-b8b1-66d0dd208b97 | -6.42149 | -52.76284 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f12bbb11-25f4-3b02-8791-3eb161ab4f13 | -3.97921 | -47.20805 | 2026-08-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002327bf-bf23-3756-a511-a3614007b431 | -9.06896 | -60.42849 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 236f7c94-891b-32e8-8c40-c3e1b802005a | -2.85934 | -60.86165 | 2026-08-21 04:46:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62151e69-9921-3ec5-8b5f-a695253e0541 | -6.83136 | -59.40747 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dbf9cae9-c676-314f-95f0-c881d94fd16c | -7.2579 | -49.8829 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d92993d9-02f1-3be4-bec7-01e06544f13b | -6.90329 | -58.99073 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 564aa43a-a352-3861-83c1-57835f27f094 | -10.76171 | -50.30614 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa2b566-6c96-369b-8084-6b07695fac0b | -7.60252 | -60.94515 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5954beaf-7cdc-3d54-a01e-1633cc9c544b | -4.93737 | -55.78234 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bbcd848f-cf20-363e-827e-a75443ead785 | -9.39458 | -60.55392 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 960a34b2-4dfd-3d0c-a0eb-dbaa9f574ca1 | -11.1066 | -49.89573 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 652bd7eb-9a99-3645-b2c4-bb49cb4232f7 | -6.70733 | -59.09219 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b50541e-6b98-3a03-84e5-b19b86584175 | -9.21787 | -59.77074 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e89fcbb1-bb11-3d9d-811b-040685d3ff8f | -8.03022 | -51.79439 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 991925c3-d574-3dc8-b0af-47905ab23fde | -6.12959 | -59.9064 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1492e671-7a48-370a-9482-1b13687d08c6 | -5.90773 | -49.25848 | 2026-08-21 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55febbf9-794a-391b-8a51-924da62b36c4 | -6.11297 | -53.06913 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42a59ec1-0e5d-3aa9-a1b9-b1b35a25edfb | -9.40653 | -60.54662 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c170e3a-1797-391b-839f-1bb0e7283a45 | -6.44009 | -54.95302 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94181a35-657d-33c1-a3ab-1ac7a5fbf6f8 | -6.37871 | -54.94482 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e050cda0-e7bc-3124-94f2-a43271f3dab0 | -6.66073 | -56.353 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2136266-7a95-3fd5-aff2-d88c77f83b2e | -6.37124 | -54.94357 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9788793c-8c60-36c7-949d-1964d197abd1 | -6.10491 | -57.87121 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0968a0e0-c390-3146-a2f5-fa8509741bec | -8.71801 | -49.61193 | 2026-08-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a425c8db-9bb4-353b-b139-967e4ce5d374 | -8.10816 | -51.66451 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 193769b3-9fb1-3428-9feb-37b7be9667b9 | -8.61177 | -54.68777 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e79530f-2b6e-3b65-9256-315ee5fd17fd | -9.25106 | -59.81087 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3e6a482-5012-3adf-8b2f-987c0bda116a | -7.87252 | -63.76507 | 2026-08-21 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d3bb6c-807d-33c6-85d0-09b09f54dc2d | -6.66625 | -52.88373 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445ffbd3-3510-35f4-9eac-2d4de2763884 | -6.43337 | -54.94734 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f9dedd-1ced-3dee-8bd0-29468435bcb8 | -6.57893 | -58.98867 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57739622-81be-3106-ab4c-bbb5951153ad | -6.86531 | -59.45142 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f5fbd90-79e4-312b-ac74-e949157e0991 | -5.61415 | -45.70267 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5753e4b9-5aa9-3c73-ae38-dda6e297a273 | -10.3048 | -48.23087 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66ffe953-ec02-3dd5-a9d7-96061ccda126 | -6.60983 | -58.38797 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 248c9e26-f1d9-3745-8cbc-66dc03983af2 | -10.75047 | -50.3349 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5422fbe6-4f3a-3d3f-9e47-61fc3f461552 | -7.20275 | -59.40993 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78da6a9d-cc97-351d-95f7-ee7a8a7dfd5e | -10.66009 | -49.02205 | 2026-08-21 04:46:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb94b40-9c7f-3cff-aef0-fa8ba9d7395f | -9.06786 | -60.43467 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 671ef060-6410-34ea-b277-177c50d4c39b | -9.4498 | -51.60752 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bab9522-f737-3b51-be1f-d3a558775f66 | -7.50873 | -55.58662 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea209f0-8d4f-34a5-8d9a-b05401eac670 | -6.86958 | -59.4535 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23689607-c962-34e9-9567-b2a9a31ab54d | -6.37497 | -54.94419 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e2bf511-ac6c-3b0c-86e0-9826a7811f9b | -10.24341 | -54.3676 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14f3a85b-6801-3bdb-912b-1751758fac9e | -6.54891 | -56.54723 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd26045b-c55b-3b9c-b55b-47ada0d8e1f0 | -9.99861 | -48.55769 | 2026-08-21 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb6b2c25-1c00-3371-a9dc-e590482f87e3 | -9.21819 | -59.65844 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 031582fd-5bd4-3e03-96cc-b2f06f4e8331 | -8.52726 | -55.34266 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc6e0b2f-9ccd-320d-934b-01613f3a9b41 | -8.57888 | -54.77597 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f7e38f2-e7a5-30a1-8938-019c9984c9b6 | -10.28722 | -48.22081 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b8886aa-a413-368b-9fcc-cbbd8f0b4263 | -11.48559 | -45.09002 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa4964f0-a850-3f56-8ecc-b4ad5d26d19a | -6.72193 | -59.09483 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77d3400a-968f-3e7f-bbc7-3993b35eb80a | -8.09548 | -51.65897 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28a801e8-962f-3db9-b2d6-c87d83fe0881 | -6.86632 | -59.44572 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8707e7e-79f7-3989-890c-bd219efe912e | -10.90234 | -50.27808 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f43a326e-ae28-31a3-8e08-d077f0ebcaa1 | -6.64637 | -56.41338 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dec0485-5c5f-3c36-820b-cf3daa6086ba | -6.71219 | -59.0931 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1881882a-297d-35ef-b2f7-e20003c5bbc3 | -6.85501 | -57.68377 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b03825bc-c969-3d73-8994-0b0e5dc1966a | -5.80843 | -55.72134 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a7f1e12-52bf-31c7-afe0-efe714192d4d | -9.12029 | -61.60012 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e588c164-0881-335b-85a3-c21b9288b277 | -7.00212 | -48.0359 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31b99409-f98e-37f0-8c7b-59ad39e30569 | -10.29917 | -48.22813 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ae8929b-9dac-37fb-991d-f0afa8e1a7ed | -5.60914 | -44.00375 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4df1ff4c-bfe8-308a-b62a-c515aa442d60 | -8.09054 | -51.66885 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b6246d6a-5758-3108-b856-2e2e83a224fb | -6.36577 | -58.33329 | 2026-08-21 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aba17dec-66d2-3e51-9a7c-c9e7e6110f45 | -4.39024 | -49.99124 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ca74da6-4632-379f-b395-5f758af873df | -9.05991 | -50.87513 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7dbba4c-8fa7-3d15-bedf-045cf6cf2d13 | -7.78205 | -46.04157 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d0888d0-f1b7-3da2-aab1-a2af71a5bceb | -6.10118 | -57.86569 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README35.md)
