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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be513615-a8f5-36f0-825d-a448103246d4 | -7.49552 | -54.98502 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c55228ba-d9e7-3f32-875d-674da75b5005 | -10.78989 | -50.52694 | 2026-10-01 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c803be-9235-3660-b06b-e975834873c9 | -7.49699 | -54.98666 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a8acbbe-25bf-36fd-8748-fcc4481c60b4 | -12.18758 | -48.4349 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d01dbb07-41cd-3b00-922e-95c2835a42e6 | -8.17739 | -54.79312 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6314752-52b8-3ce6-837e-e7bb2711bedf | -7.72433 | -54.79534 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596cd866-f06a-33b0-89c9-c992613c9e86 | -6.11264 | -55.69933 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e7523f5-86e3-3bf6-919f-6ae082f0e32e | -6.72626 | -52.96132 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44bf0a59-f9fa-3304-8c93-860f9f7d4cbd | -9.21207 | -50.68279 | 2026-10-01 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3464efa6-379e-3713-b4eb-44ffad500204 | -11.29217 | -50.96863 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 03d7e44a-40c2-3489-b309-eebf00ed4ff5 | -7.60598 | -49.53356 | 2026-10-01 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed2b010f-4e3a-3512-81a9-ba055304e072 | -6.4897 | -58.53527 | 2026-10-01 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd62531f-acad-32d9-9bc0-5f48232ce844 | -8.26313 | -54.75875 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a695a23e-75cc-3d9f-b684-ee9236cdcca6 | -7.63742 | -55.06456 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4292a25d-5c6d-36dc-8dfa-f4d8665e95f3 | -10.7759 | -54.75084 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d320a22c-00c9-3194-8a30-e05173740d58 | -9.70008 | -58.12594 | 2026-10-01 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 308c4530-4665-3a5a-b9ee-97bc7bf14dd3 | -6.19294 | -57.59221 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8086c1b2-007e-3795-a539-c5759861ce65 | -6.43392 | -55.80297 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d574bbc3-0d3f-3dc5-b9bb-e4a072061aa4 | -9.33865 | -57.17532 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32fb6455-3106-33f3-bb3f-34e52f0fcd6b | -6.35831 | -55.34726 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dcca11a-18fe-3a7e-9eeb-0125de26f64e | -9.35433 | -57.17225 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ff9fb49-c8a9-307b-bd6f-b2766a5a1af4 | -6.02992 | -53.36617 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f69bb2f8-7436-3305-9080-7dca6896a95a | -6.84885 | -59.35632 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de273b83-5f84-3ec5-9fd6-2b029774bda6 | -6.14062 | -53.28636 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5a27eaa-ef0d-3038-bb2a-2aebc9898051 | -9.02211 | -60.53016 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5537efbd-9363-3cd4-8f26-8c732419121f | -10.52619 | -57.78223 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69a76e56-e308-3f3c-9a8b-6dcd9a32c761 | -6.11565 | -55.70417 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b982086-24fc-39fe-9888-7d38f6d3bef4 | -10.25345 | -49.66957 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f7c85d-4f21-3247-b245-47ca555504d5 | -6.05841 | -59.92348 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858c5f30-3481-34c0-adad-e828a9d4b2ef | -5.86892 | -57.75612 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dbb8cf91-9fdd-378b-8031-848a9f956c34 | -6.70004 | -55.04713 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 234e69cc-df63-3a4a-857e-4c0e68cb5723 | -5.3256 | -56.00496 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e73fbccf-7432-3af7-a776-8e5bf83dde3f | -9.93152 | -63.75622 | 2026-10-01 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95dd8795-81c5-3faa-8a54-56e1aff60675 | -7.60548 | -49.53742 | 2026-10-01 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40d055c0-bdd9-3ab6-81e5-189d06a4394b | -6.03047 | -53.36238 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbbde57-a7d1-3365-a2ee-37f05fd852f6 | -10.51753 | -57.76904 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdd9fd53-8b36-3c26-a0b4-f0361a019c63 | -10.78441 | -50.52618 | 2026-10-01 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26122d54-784e-395d-8f41-b0b9d4343103 | -6.1433 | -53.06396 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a004412-82d9-38de-b48d-2e35ab184615 | -5.37574 | -56.05792 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16109b8d-3ac6-36ba-bb32-b2d782774792 | -6.084 | -56.47242 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2462d071-9ec9-38cc-a683-09e592738b90 | -9.06932 | -49.87288 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f7ed0b-7770-3707-bb2d-c5d11f8da607 | -9.06424 | -49.86831 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07828e50-5fef-3a99-b8c1-3905bb8e1379 | -8.51763 | -62.67755 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59a2957e-450c-3239-bc77-be5f045ddb56 | -9.06846 | -49.87044 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fb69720-60c3-3e13-b48f-3f26272548bf | -5.85777 | -57.76174 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45052fc4-7060-3ba2-a0f6-e0532ea50424 | -11.7418 | -50.40695 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee3a37f6-2680-3dd1-a6eb-608df8de706a | -6.05454 | -59.92645 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4dad34e-f6b9-358f-a1fb-5cce5011a77b | -9.78471 | -59.02127 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3a0c4e0-ddce-3fb7-b30d-ad818ec69157 | -9.35491 | -57.16829 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97123b76-23bd-3d48-b72c-914d06b3b785 | -8.17823 | -54.79202 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a3997f6-09a4-373e-aa8e-f7aa3e8a56b6 | -7.496 | -55.03476 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b29e984-8028-3921-95d2-927ecabc9ba5 | -6.531 | -60.03468 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78bee43b-8f8b-341d-84c8-e8e5c24af28c | -10.86812 | -54.10144 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e71c4d5-00c4-355d-b7d3-b0a9f63f059a | -10.66011 | -50.76387 | 2026-10-01 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e0521f6-dad8-36f9-9395-1912e6e92a29 | -9.91857 | -59.71707 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83441a85-1000-3023-8297-f1d3d5ba335d | -7.49794 | -54.9953 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 276dc13a-dd09-32f1-8c9f-4c4c926b86a4 | -5.86112 | -57.76227 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23c50333-07fa-3e69-b5bf-398d8d3b5096 | -7.17397 | -55.40306 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8012567-ea2c-3e54-9c00-9a9219327ddb | -7.49092 | -54.9894 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a59535a-88af-3e8d-8dd6-f3ef0382e851 | -7.69162 | -54.74409 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a275ce2-a035-3e50-8ed9-04a39697215c | -7.46631 | -54.99551 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf90b787-ef9f-36b7-8144-78e4c8ff7d75 | -6.01653 | -49.5578 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a4cdf95-ad37-3d5f-a1b5-e170f791d2d0 | -10.53889 | -57.76842 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 598c6587-9059-3860-9067-a8eb7024ad5c | -8.30839 | -54.71594 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe15606c-77df-3500-b0fc-82446469f5b7 | -9.95682 | -54.66855 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ee1fee7-a078-334e-9f00-28ea72b0c274 | -10.50888 | -57.77958 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a782a40-c185-3148-a2ff-fcee5bd857a4 | -7.98118 | -61.55251 | 2026-10-01 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcdda80a-9a0c-3242-935d-1244206cf5d4 | -8.17748 | -54.79713 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e19d4f-da9d-3fb5-8425-b106f770b1b8 | -6.84831 | -59.35978 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a8d07e6-43f2-33bc-aaab-f23c46b7b5e3 | -10.85561 | -48.68768 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c544ac4-2a04-38f6-9281-d40ee6d07e64 | -9.80044 | -54.29772 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbd71c36-4242-3769-a8c6-cc5d65ecb629 | -10.53543 | -57.76787 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3041240-da03-3d86-bdad-eaa6df38ebd6 | -10.25227 | -49.67019 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6e18194-f626-3c70-b3e4-8f6c9eb0e158 | -9.78193 | -59.01723 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a4b3f14-deff-3f3e-ac3e-fb6765c44d45 | -6.00962 | -49.56002 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7673e4ba-c6aa-310d-9fe8-46365076a080 | -12.19395 | -48.4357 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1b60808b-faec-3512-803d-47debd0da46f | -5.97424 | -55.37143 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef4d7f2e-61db-360f-899c-de0a065e1509 | -9.06894 | -49.86665 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca71468f-6405-365a-9fce-675ec7d47b9c | -5.85887 | -57.7546 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ccca52a-63de-3ea9-b69b-0a86c1e756f5 | -7.38748 | -46.42575 | 2026-10-01 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdd6dadb-734b-33ce-ad21-c915aec6bb3e | -8.83963 | -49.69207 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 989b433e-3f8a-3bbe-a32c-6470e1f2ec01 | -6.43693 | -55.80778 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 736d80f0-0f58-36aa-bf49-a08e47b70fb3 | -7.49172 | -54.99594 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7caa6c1c-5e3f-38b6-886f-0e2138f13f60 | -7.4948 | -54.98988 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4221de9-7b63-323a-a833-77a1a962dcb1 | -6.68192 | -58.87376 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 62429343-236e-3971-9d13-12603c7803e8 | -5.86809 | -53.4909 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 891e3e46-6b7f-31c7-adba-1066582fa610 | -11.37715 | -55.12696 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8a57b3b-2a25-337b-b1ce-4655a0138ee2 | -10.53485 | -57.77174 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71470214-a4ad-3f71-ab87-f8b26c42da92 | -8.38195 | -50.7264 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb42b4e9-38a1-38b6-b26b-3c692217ccf5 | -6.14509 | -53.31577 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43b4b7e2-133a-3df3-8774-e6de3fdc1270 | -7.34717 | -55.59615 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 965f410f-bd10-3e49-8174-1bc511b245f1 | -10.46788 | -59.13152 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3daca611-5003-35f2-ac1a-b84ec13c2540 | -7.73218 | -54.79651 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f377558-cde8-32b6-b851-a8b9a1221b25 | -5.86222 | -57.75512 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0be0244b-8f6a-34e9-8b19-1ca91f5ea720 | -9.08891 | -49.88864 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53f6674-6606-3e57-adb7-7b1bc71613aa | -10.89806 | -56.17306 | 2026-10-01 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a91d0a-b49f-3da8-bce1-4704f5d66ec1 | -6.13327 | -53.27713 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 017cdaf6-b2f4-361e-89e0-f61f158c5c65 | -5.90868 | -53.48691 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b0688f0-32b5-37d5-9ece-c14c74a6e34a | -6.67147 | -58.87567 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 083853e7-fa50-34c8-af97-b8b04bb57b42 | -6.34905 | -55.32088 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README83.md)
