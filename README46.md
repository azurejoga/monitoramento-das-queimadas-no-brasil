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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cc662b0-c818-3654-a615-0f5b1c55db49 | -6.59866 | -56.35777 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 024e46f0-608c-36f6-8174-fce86bb7fb06 | -6.58911 | -56.3567 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1396789-aee8-36f1-a55e-746a865b49c2 | -6.79222 | -55.83862 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99fba25d-d6c2-3d93-9f65-30d82c44e638 | -3.59885 | -58.61712 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27bd0b3c-5e56-371e-8f33-f3524b64e817 | -6.96297 | -59.28779 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f004903-8911-31bb-8bdb-0beb2ecd1255 | -6.78495 | -55.85007 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c45ec077-c7ef-3693-a639-45bd5f8ed504 | -8.61096 | -54.67225 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2712833d-c455-3bad-a63b-62d328b623ef | -6.95645 | -59.29807 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aee89a89-3b12-3de7-99bd-b47a369ab247 | 0.49822 | -60.59252 | 2026-08-15 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff96e1cf-bb18-3542-be68-2d0a3a5ac65b | -8.78167 | -63.97635 | 2026-08-15 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb77dd6-2eda-3e10-a089-a7db7f8f4861 | -6.7856 | -55.84535 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf7ce43-ca84-38f2-9a55-79948d3fd4d9 | -6.96969 | -59.29024 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5791ef66-02fb-330a-896a-c8940ab41af8 | -6.8521 | -58.96054 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1fad778-4f96-38f2-972a-f10ed38def74 | -6.83205 | -56.42973 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9822c3f9-eaa3-3cd2-b4f3-d5288e351de0 | -7.58777 | -61.2352 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36a38ccc-65bf-36a7-8b8b-85a32426a71d | -8.9593 | -60.53851 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aead75a7-9ec6-3484-a624-e0a40189c750 | 0.49022 | -60.59376 | 2026-08-15 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ead5314-7b8e-3032-946d-5ec73a42288e | -6.65371 | -59.10366 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d79fe21-edbe-39dd-97d2-6a723e19370a | -6.84448 | -56.42725 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 269b5548-9dc1-3c4a-91af-e51897dabf35 | -6.71715 | -58.94014 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acad01a8-682b-3652-aa5d-27ac72862f8a | -6.82877 | -56.4257 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ffb367a-8d4e-3584-8eef-14fdd254fa2b | -6.42992 | -60.0718 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bde67c0-d0d8-39ef-92b6-81122e28d1f2 | -6.96064 | -59.28327 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80e17f23-c489-3041-b560-51d3164d873d | -8.96264 | -60.51422 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dda7715c-83ec-3f46-a58c-200f715eeb6a | -6.78544 | -55.84244 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2782e334-b417-3ee6-b652-86bda86893e9 | -6.63568 | -56.26264 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc7f78f-edca-39f2-ba05-805b721d2693 | -7.58344 | -61.23457 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e0e83ad-bdbd-381e-a8fc-c29ddf2e57ce | -6.78066 | -58.74621 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f89ebd6c-254f-331e-a55d-f20588a0e862 | -3.2428 | -60.12575 | 2026-08-15 05:53:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7fa1a8b-81d1-32b3-a2b1-f9991bf64ccf | -7.51245 | -72.82624 | 2026-08-15 05:53:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24826b4c-3869-37cc-be67-a049aa8fb0a5 | -8.6122 | -54.67868 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f4b778-edd5-35a7-8348-a9813abd12b2 | -7.54832 | -61.16998 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a22cb66a-40b4-3982-bcf4-493cde551344 | -6.60577 | -56.34984 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bbe0d18-f327-3d9d-a79f-27c905c7d763 | -6.81787 | -56.44537 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d93ca755-677d-3494-a6f7-1dbcdfc426ed | -7.59211 | -61.2358 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ca87250-b072-388c-a307-ee7b6636a562 | -1.48186 | -60.29763 | 2026-08-15 05:53:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82dee8e3-5e13-3a3d-9efe-2f1bf29ac1d8 | -6.95235 | -59.29187 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71a36b49-e0af-39bd-bfef-5ac8c9acb400 | -7.69529 | -55.16038 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5df019c-599d-3282-a053-d087b68b3672 | -8.60615 | -54.67184 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81e9a515-6164-3fb2-b461-3b9080610d32 | -8.95334 | -60.51292 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6720234d-2a4c-32bc-8119-86d368474f49 | -6.8498 | -56.43263 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf2839ee-1484-35b1-8cdd-b7454b7c544d | -6.88487 | -59.01955 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3953da1c-b4ef-3afe-b25b-1ffaa131f143 | -6.62421 | -59.05292 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66e8d7d5-1162-3557-8b44-eb1325152fce | -8.98383 | -60.5322 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbc0cf8c-d012-31a3-9149-7d43c403f875 | -6.96326 | -59.30047 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 352062fb-e4c0-3140-baf9-8a6b981b396c | -6.60274 | -56.3459 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a4ba72c-b72d-3a4b-a7f3-0113321900a8 | -6.59155 | -56.36568 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eabaf692-d4b2-396d-b2f0-f0bf1b20f5d3 | -6.96402 | -59.29503 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5c486a3-0005-3729-85f1-e8fa9ad859cd | -6.95572 | -59.28259 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14ff5710-1749-3a71-b24b-044e2a648cf9 | -6.61685 | -59.06894 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c4a99ffc-de7b-31ce-9594-b53929347b7a | -7.98676 | -70.9343 | 2026-08-15 05:53:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 592d73c0-b1d5-3305-ae3a-ee800b3e3258 | -9.34679 | -62.35973 | 2026-08-15 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07a74e94-578b-3257-a2f4-db49c9252e3b | -6.59985 | -56.3488 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f13a7c46-ef66-3325-8868-cc9c464ccb85 | -8.60469 | -54.68388 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84ce97a7-6c0a-30bb-baf2-8c341c0dad17 | -7.58837 | -61.23105 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a9088ad-cdc3-3190-a77f-a5e31b39b114 | -6.72256 | -58.93798 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267e4b86-ce68-32e2-ae37-8934531bdbef | -6.61233 | -58.99385 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e6605d6b-702e-3e46-9fa7-e708ef05560a | -6.96377 | -59.28229 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9dd16de2-a658-36c8-aa36-d13bcc1eb6fa | -9.34731 | -62.35604 | 2026-08-15 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d5d993d-46fc-3604-972e-afa4f97738fa | -6.62083 | -59.04111 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25d19c14-2224-31ac-b68d-52edbc43e1f1 | -6.65733 | -59.10366 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 792e17f3-3d9a-3b08-a516-e3301438b6dd | -6.70427 | -58.95911 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38bf6dec-3548-357a-899d-a9856f07c03e | -8.64443 | -54.69613 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e17814ef-9475-3377-ab2c-5634eb7a6177 | -6.96478 | -59.28951 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7425b49-05fc-3a31-9138-347dec6c22b5 | -6.94217 | -62.87912 | 2026-08-15 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12b894a3-5cb7-36c8-95b4-2265d53dea8c | -6.95886 | -59.28161 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb76866c-8980-3dd6-918d-a4537f53d840 | -6.70547 | -58.95052 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c08897d4-0b9b-324e-b3b1-3781adb8ceb4 | -11.50561 | -54.62391 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6157e0-ac92-36f1-8436-98b7426f6294 | -11.58365 | -54.68743 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04e8aaa4-5848-3156-a421-feedb126121d | -3.74817 | -59.33146 | 2026-08-15 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84d84fef-990d-31ff-9bcb-22c0bd236cb5 | -6.01997 | -57.84187 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2295f49-86d3-3037-98ae-ab45373f2661 | -11.58128 | -54.69349 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc87a9e3-a8f8-341b-9e6c-a686b2cd8cd8 | -11.505 | -54.64269 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc838c05-e0f3-37f8-842b-00f751d80b61 | -6.01646 | -57.82806 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 682c8c83-a56f-387a-b176-4dc0044bdaaa | -11.58289 | -54.69389 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c22e424e-628c-3070-bc91-f3546ce85d40 | -6.02091 | -57.83519 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 799b2d6a-a2bd-3292-92b9-e638cb54c581 | -13.42142 | -57.0491 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc3d9bd5-0d9d-32ab-82c3-2b97b36323db | -9.71111 | -69.07141 | 2026-08-15 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9390119-3a27-368d-a067-09ccf49ac45a | -14.75427 | -56.3489 | 2026-08-15 05:55:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adcd77fc-efb0-3271-b299-7b92b09777a4 | -9.7117 | -69.06782 | 2026-08-15 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a482df82-8fa9-31e7-a033-8f8ef2ba43f4 | -9.70776 | -69.07086 | 2026-08-15 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 849843ee-4504-35a5-a940-cca355b9e01e | -11.49781 | -54.63006 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3284592c-896a-358b-b808-410758e6db7a | -11.51041 | -54.64459 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08567feb-9090-3e2e-89a3-5c431f2e31b3 | -10.05101 | -67.5405 | 2026-08-15 05:55:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b67d2a6d-e6cd-3f1d-a47e-7ce54c7d2e29 | -6.54026 | -55.17888 | 2026-08-15 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 437b06ae-1a10-3639-92a2-a854b1fac869 | -3.06503 | -67.94533 | 2026-08-15 05:55:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 419831f8-cd79-3994-81c8-d88f21ba4c89 | -13.42089 | -57.05395 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b957f9a-ac50-3b42-9588-0ac0ecc67207 | -6.01556 | -57.83448 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ca5930-9bda-38bd-a773-3aae7adcb087 | -3.74351 | -59.33076 | 2026-08-15 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4867cdb7-699e-3a1d-a466-6f19f4e4eee9 | -11.50032 | -54.62203 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 461e411c-e6b0-391b-911b-2da2b3762c80 | -6.02137 | -57.83198 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3b3fd51-3d53-342e-9088-6d140ecba5e0 | -6.20324 | -57.76737 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73bced33-c3c4-38b8-b876-7c411f775194 | -13.42708 | -57.0549 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62720744-c36a-3ef9-abd7-26bb7d30827b | -11.49952 | -54.62883 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09a387dc-7625-330e-8cf0-b821130f4600 | -6.54664 | -55.17984 | 2026-08-15 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deef92f2-559c-3ee8-a357-5b0d61437632 | -11.59296 | -54.6685 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97230cf2-be16-3015-8cbb-ebd6e62f367f | -3.73885 | -59.33008 | 2026-08-15 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57188f50-d9c2-3a46-abc3-5bc9e2e0181c | -6.02183 | -57.82872 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c40d97-723f-3704-94c3-366182d4bfc2 | -6.0223 | -57.82539 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cdadaf0-afbb-39cc-a1d3-c588e4a3619e | -6.01694 | -57.82466 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
