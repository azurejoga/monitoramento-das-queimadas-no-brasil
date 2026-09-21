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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94c7a2f3-503f-3a27-b030-034e7072363a | -3.06805 | -61.27589 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a131cc08-b6c3-3273-b3da-aa5c2003f468 | -4.35155 | -55.64444 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be65dc1c-25b7-35cf-9ead-9f75971649c2 | -5.80517 | -57.73652 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d013401-a2d5-3c89-a487-94bacca65177 | -6.10246 | -57.63633 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4b05075-588f-3104-924e-abb2c9179d1b | -3.07106 | -61.28475 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27665d20-9698-35cb-bdad-ba1d1a7f1829 | -6.73305 | -55.07029 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af553e69-2c79-3d84-af05-fb3d083fe428 | -6.13608 | -59.94456 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f765be2f-550a-3e6c-b9e6-812ae8cdda2f | -3.69149 | -60.58382 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbecfe86-8ab7-30f0-9bcb-301df4f08720 | -5.86755 | -51.93809 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2111b74-5156-3717-a311-cd0d628acbaa | -2.45633 | -49.21486 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4b410b3-69a9-3fb8-9d67-25b98d5fbb88 | -6.25072 | -55.48444 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caff981d-f5cf-33f0-bee2-4f22bcd9122a | -3.46096 | -58.40234 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d334170-115c-37c6-bac5-ce5598c583b3 | -6.14081 | -55.66497 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a64c893-52b4-335f-94f1-6c3d92354571 | -2.17532 | -48.31965 | 2026-09-21 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b6862a0-609d-3218-b1b5-239178ac47be | -8.30749 | -46.87294 | 2026-09-21 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b655b71-c9e4-3e38-9de5-b48dd58baf39 | -3.40186 | -61.34681 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3676af-0ce0-3d3d-a8f4-84a700bd2350 | -3.48598 | -58.92159 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98f77d0f-94f4-3714-82d3-490e097da95a | -6.30035 | -59.96052 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3adc307-77d0-3282-b16e-5539c9238b58 | -4.45468 | -55.68155 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e93ad86-24a2-3dcf-99b5-5abe432038f0 | -3.07996 | -61.17348 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d979fd7c-ce89-30a8-bde6-847ff0c399ab | -3.39436 | -50.44351 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d44f11-d9d5-35da-88c4-041a458d5d48 | -3.68975 | -60.56872 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 060bcdb8-e014-3377-a367-c277d868edd6 | -3.54248 | -58.6877 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 105e373a-335e-3720-adbb-e71a6c2a8a9d | -6.12368 | -55.64465 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e662b7c5-0800-3060-add8-163d028b57b3 | -6.30872 | -60.00445 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aced587b-f9a3-3b74-bbdd-144e0063b9dd | -2.26144 | -48.75411 | 2026-09-21 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1281ab52-4542-3f38-a108-fdb787d8fe4f | -5.87467 | -52.0459 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 690e58e7-7360-3751-be20-5746ab55c177 | -5.42089 | -60.21457 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d346f88-4fed-3099-9a9c-231cc3e4ab4e | -3.39114 | -59.53027 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 469e86e3-5dcd-338f-87a5-da30ea6c1b18 | -3.53883 | -58.68715 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d19d08d5-de6a-3946-8c2e-b7344780dad6 | -4.86896 | -55.83878 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9290f61a-1b5a-3f0c-bcc7-e2b05b19b695 | -3.61939 | -56.83878 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1ad4d67-173d-30f7-8c73-44766186ae0d | -3.65335 | -58.8618 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8a328ff-716d-37d9-ab4c-57fc599e3acc | -5.87599 | -53.63167 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62992841-976a-3fa1-a99d-6391370d113c | -6.38941 | -55.20358 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5962dee-87d2-337a-bf1f-96c8df7426b1 | -6.04194 | -53.2769 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eefa0978-020a-3637-b479-e770374bbb97 | -3.18636 | -57.87206 | 2026-09-21 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e88a8294-e94d-3c84-ac06-34f2d5349d43 | -3.5261 | -59.88929 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dae1f03-2520-3d58-8956-4e4cb3f4b51f | -5.75597 | -51.93287 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b28b830-0d46-39e5-ab9e-ae387ccac697 | -6.35743 | -58.28201 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65f83942-a1f2-36bd-8fa9-fb0c72686da1 | -3.64762 | -58.87415 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92ac18d3-5f0d-35f9-91cf-580a1c813b20 | -3.68448 | -60.6013 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce3cb51e-2e4f-3477-b8e1-87f9c468da83 | -7.43566 | -44.77872 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 68bcf853-ff15-32a1-b251-d7818f5c3d96 | -7.43631 | -44.77366 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c279a21a-d165-3785-bca7-59acbb53180c | -3.52529 | -59.89115 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9c823c1-9a5a-3b37-9f08-ec9ec3c9d748 | -3.04425 | -51.10504 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6ff8144-c417-3647-81e2-e43d739dd92b | -5.72827 | -53.45383 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d297d46-44f2-3dce-b22a-6bf5fa1463b9 | -2.93763 | -50.492 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 569cb18b-9c9c-3b50-bba6-59cf7fc73235 | -6.02737 | -55.34647 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6824e2fd-c119-3724-8603-67598a693801 | -6.33447 | -60.01333 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6843f14d-2380-314d-8e49-12b93fc99d26 | -3.60746 | -54.03955 | 2026-09-21 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121ca6bc-716e-32ec-94f2-78f8a092fd36 | -3.19359 | -60.43408 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543e5e02-b151-3572-ac75-b5e82f7a82d7 | -7.25018 | -46.90802 | 2026-09-21 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83d9d74-98ba-395d-83b4-0b13db4abcbe | -5.21749 | -56.11279 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29150e37-97c1-3a77-bb78-37d93771723f | -5.88462 | -53.64463 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4a0d0b-871d-35fe-b56c-b89fbe10c65e | -6.11615 | -57.35589 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b53d2db2-9855-3d2d-b21d-92a7f7832124 | 0.78954 | -59.2048 | 2026-09-21 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d9237e1-9bc0-3941-bea1-53bc05f6331c | -2.82786 | -50.47736 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 695356bc-f9d3-366f-ab22-126b9266baa9 | -4.80471 | -54.74284 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c799bf79-46fc-3043-abb9-50046859fd7d | -8.00478 | -44.81581 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3220f5f2-2fab-32a1-87ef-29dee9ba8304 | -7.10713 | -48.42587 | 2026-09-21 05:04:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab356c6d-4a90-3293-95af-4723033303c0 | -5.82806 | -53.5114 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f867d118-9ff3-32a3-80ce-3aa07f5f164e | -5.83625 | -53.48125 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b53b412-40ae-3cb6-bc16-f196c5a830a5 | -6.03784 | -53.28032 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e050ab8-8cf5-358d-8fc5-7288fe03b9b1 | -7.44055 | -44.78951 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f2d79d2-e5b4-392a-8119-aa563e24019c | -3.82234 | -59.33558 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6af17a5e-3b8b-35b7-862c-9939136c5aec | -6.09711 | -57.69162 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f931e2-88df-3f19-8cc2-78e9d1b3c313 | -7.45368 | -44.73711 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 284d243b-5964-3741-aea4-295a2e9ae49d | -6.24993 | -55.42404 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c50f4cca-50d2-3b8c-b49c-ac704ec6dd5b | -7.08044 | -46.28699 | 2026-09-21 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 479d1794-3712-37ee-8ddb-21512079c6bb | -3.06674 | -61.28409 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62467883-8012-37b7-8480-208d76d052c4 | -6.35019 | -59.96631 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95136b5c-460f-3b16-8eaa-95e35a2d6b20 | -6.93388 | -55.61988 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6ff75fb-d1e0-39f6-9e37-637c63e0c3e4 | -6.76845 | -55.63265 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9594b793-06e2-3ac5-b7cc-48a43f2810ad | -6.15806 | -55.71056 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed45485e-a82f-3a2c-8feb-5944b045285d | -3.82556 | -58.88653 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7901585-8ce2-3e09-b601-5a0c5bb5a0b1 | -2.58415 | -59.41087 | 2026-09-21 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aa26788-3593-35cb-843c-c17e835949e6 | -3.05211 | -61.26493 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd5d07c8-d808-3aed-8f62-508161c88c6b | -5.47696 | -49.23352 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb2b7135-8090-32cb-baaa-28eae6ee1160 | -5.83786 | -53.48498 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a742392-9f2e-3410-a991-4d88d05d5b04 | -6.39567 | -55.25097 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a48c7741-dfec-3c83-aea6-6116d1d7f75e | -3.44101 | -58.23636 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9053333-ae45-39a6-a1fc-1d61a0d879e5 | -6.3547 | -57.77017 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53159cc8-e89d-3939-b1b8-57bba8e31224 | -6.12645 | -59.95475 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72d17e9e-2f97-3137-bd74-3b9cfd6f430f | -5.97886 | -57.77154 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edd6b21-fa43-3798-8c57-5ed602c5d129 | -2.91383 | -57.78699 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ea54965-412c-3730-9dbb-5d855de86162 | -6.35682 | -58.28584 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cf47fcd-d417-393d-b74d-0dce54c56231 | -3.74249 | -51.81904 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 751107c0-873d-367f-8b1d-e4d1d5233c64 | -6.25717 | -55.44291 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2961375-de4e-357e-86ea-7c1221fe1cbd | -3.14819 | -61.39746 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c9eab1d-9c88-3364-a8a4-1cceb019c058 | -3.14384 | -61.39678 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d05f718-0962-3d48-9091-2ec31efc7bb8 | -6.42246 | -55.01146 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81bd24df-d9c5-3f29-885a-6b81857ef56b | -3.47776 | -57.98022 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f618c17-99b8-37b2-ac77-6a310d3e96c7 | -3.12374 | -51.09078 | 2026-09-21 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aebe628-501f-3468-b03d-123762359952 | -4.83243 | -55.94243 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c4c8f1-f57d-36e1-980c-496c2b998bb0 | -2.90192 | -54.18383 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8ba15d1-c40e-3c5b-88e9-09f5a66c70cd | -2.9784 | -54.76353 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233ef2ca-9704-3b02-922e-72ae53b0739a | -2.26008 | -52.0263 | 2026-09-21 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84bb7d8f-2123-397f-863a-fa84da731290 | -4.2763 | -51.12576 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4f59684-3323-34f5-a6c7-07b560e6ab6a | -4.52602 | -55.66164 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
