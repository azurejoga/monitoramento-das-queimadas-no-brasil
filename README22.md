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
| bea1879c-e643-3449-bfe3-c2a2b5bc6491 | -7.86366 | -47.87719 | 2025-07-29 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5f71dfa-32fd-3aaa-9874-3802407b6052 | -8.94233 | -46.74776 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e78134c3-ca05-3c1a-a6f0-10827f0ebc74 | -7.8114 | -50.22818 | 2025-07-29 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48590db7-48b9-31b6-afc2-4e5504648c7e | -9.45807 | -57.84575 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b40086ba-9b37-3346-a721-3f684b0d0e42 | -6.3968 | -53.3549 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b70670ea-ee58-3e77-828e-ac216eeefca8 | -6.38917 | -53.35384 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d194d91d-a6f2-33ff-8aaa-c14e9ea772fb | -11.34664 | -51.2494 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 349b6b18-b5a8-3318-aaca-ddfe157b8478 | -6.499 | -56.1979 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d79553-580e-371f-8d2b-f662f616592b | -11.74575 | -48.18811 | 2025-07-29 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 099b066d-2d97-361d-8895-1a00734a263f | -6.40552 | -53.32271 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa87b69-1715-3537-9573-906d14b300b7 | -7.46157 | -49.39694 | 2025-07-29 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 008a4fd8-6d5e-3c67-adbd-656bc71eff2a | -6.39991 | -53.36017 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b3be616-b81c-382a-b32d-9f66cbbf0106 | -5.35394 | -45.27599 | 2025-07-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d42e696b-913f-33ab-9ed3-bd45a7e41237 | -6.49955 | -56.19432 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2950abcf-8a37-3577-b5cd-8c0af16b5703 | -8.96021 | -46.75441 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3be4abed-b133-375b-9244-f5580b75ff3e | -6.40302 | -53.36543 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14cdc952-714f-36d9-8efd-1b4c3d1940d7 | -6.63839 | -58.85082 | 2025-07-29 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7411e03b-6338-3802-a42e-f05e8148c5eb | -9.62579 | -48.55292 | 2025-07-29 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30355850-d8d3-3df8-a44e-ea59433080f7 | -4.05393 | -56.24176 | 2025-07-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc22c57b-56db-36ee-a13c-735ce24c22d8 | -7.73893 | -51.10386 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcb8d5ef-6ba1-38ca-bbc9-fd45e508b2ae | -7.79223 | -44.95581 | 2025-07-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14c80957-db18-3ff5-9535-64a07c8ea70a | -11.4269 | -45.12764 | 2025-07-29 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c818c7e4-a95e-3289-bc70-d78fc474ef95 | -8.96046 | -46.75274 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5552460c-cacd-30e0-a963-75c8a407bb94 | -6.49959 | -56.21629 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4476cff7-41be-3d0f-b81f-7cb67e1da19d | -6.49063 | -56.20757 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 694ee33e-8289-3e02-8033-9b16ff8ca22b | -11.74046 | -48.18311 | 2025-07-29 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dbc8bbf1-61ad-3c09-a7e5-5c7bda3b4f7d | -6.45409 | -53.35611 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbed1183-5da8-3b51-91f4-922feaad6b66 | -6.90251 | -52.86483 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7058263a-939a-30fa-be77-86e0267c5cff | -6.39719 | -53.32626 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c5b0c40-e241-3b3d-ab58-56a1e76266aa | -8.9543 | -46.75209 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13835357-70b6-33e1-b52c-1ce9e7593c63 | -7.72922 | -51.10739 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273b6933-3be6-37fd-98e5-befdef284924 | -6.40061 | -53.35549 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 965864cd-31d1-3e51-9905-80a4d6c6d564 | -7.94069 | -44.08422 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e116d309-bb20-36c9-bfd8-46b11d49618d | -6.5449 | -56.19033 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dbdc85f-3eb4-313b-bf7b-1d53e862deec | -5.35468 | -45.27083 | 2025-07-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a81694f7-5d7b-3d90-892b-6436349a7977 | -6.49023 | -56.00883 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d25e333-467b-3814-bcd1-24a68d0525fd | -6.49734 | -56.20862 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6874aabd-353b-3429-9efa-de4e67f5145f | -8.8888 | -47.34375 | 2025-07-29 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf1db66d-9630-3a73-b1a9-aafa9edbe959 | -11.74627 | -48.18388 | 2025-07-29 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f615bb6-9076-31c9-8f6c-6b03e3d244a7 | -6.64117 | -58.85495 | 2025-07-29 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 680db74f-3759-333b-ad9c-449e1dc78725 | -6.3975 | -53.35024 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5addca01-7faf-3ffe-a193-b8602fb97fd4 | -11.6888 | -47.4325 | 2025-07-29 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f5ea610-8f3d-3e8b-89a9-9a802888cdd5 | -7.93718 | -44.08309 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e54eba52-cf57-3595-9bdc-98f7d73b6a2d | -6.41005 | -53.31858 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 585bc485-2dae-3e6d-96b5-bbb6970ccffe | -14.48571 | -50.29395 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14f6e387-7f5b-35a0-a46a-747f9bafb621 | -12.37314 | -56.80285 | 2025-07-29 05:12:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b67439cd-cabf-349a-8b49-aa9d499aae9a | -13.51999 | -45.62614 | 2025-07-29 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f31a3143-8a66-3d46-8342-7ddc6e0f49c2 | -11.99931 | -46.96912 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aad86cb-f09e-3774-90b2-907253dfdf44 | -12.27896 | -63.80136 | 2025-07-29 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 744c0f13-6678-3fd5-ae8f-f3b219529eb7 | -14.72054 | -59.60806 | 2025-07-29 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8377e0c2-a905-3200-b555-943d608677cb | -12.12565 | -56.91344 | 2025-07-29 05:12:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c52b2f0f-02eb-3975-85df-b6ff557e61af | -11.29248 | -55.13644 | 2025-07-29 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb5c5f9a-ecca-3a20-a05d-e033fc3012dd | -14.36025 | -59.33007 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bb10cf9-1993-3632-ba1f-1f9de4b46e00 | -14.49656 | -46.54537 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af7abe2a-4c56-396a-a8f6-5b16b01449d7 | -12.99161 | -44.89598 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2b605e5-5a89-3709-973d-99b3311871ca | -14.87876 | -48.39927 | 2025-07-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59f66610-9776-3a2e-b880-33e915720698 | -14.37513 | -50.32968 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 583adce6-5374-392f-9c33-c454f5a05909 | -13.12056 | -47.37969 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79cecf6e-06e2-3bf5-b436-98d99fa65269 | -11.9933 | -57.20905 | 2025-07-29 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ff6aa28-c6b1-3be1-9e03-35763b7cf886 | -11.99833 | -46.95009 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 639c6550-f716-39a7-8ba7-41f0cc00d075 | -14.48618 | -50.29164 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a19e87c-74a9-31c3-9377-18766b52434b | -11.99991 | -46.96409 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 095c21d6-5def-37da-9b93-c95954ac5e32 | -13.11367 | -47.38477 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b52c6540-dcdf-3f76-bee1-33233cb08958 | -14.37483 | -50.32943 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5d28d3c-ca3a-3c57-8547-d8da25a7914c | -14.49716 | -46.53947 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e384c9e-1220-348b-94db-1aacba30388e | -11.51874 | -54.68563 | 2025-07-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23eca39d-3154-3813-b64e-8f60fa12bd7e | -14.35914 | -59.33716 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d927fe16-4212-3824-8068-6777256c021d | -14.37899 | -59.34046 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f92b49-b634-3f28-b732-2bb337144a61 | -12.99439 | -44.89709 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2d1b205-90e4-3bd1-b896-7c000b6ae2bc | -12.12508 | -56.91722 | 2025-07-29 05:12:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c664e58e-fdfc-3d66-86d4-7f968bbe5e84 | -13.11849 | -47.38599 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae19419e-39e0-3a1d-861f-aa2d0ce9f918 | -14.37568 | -59.3399 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e498bf65-fe0d-3431-bb0a-dc664da70855 | -13.00087 | -44.9049 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d1e2dd2-8eae-30e9-bd01-b08a339f9fd7 | -12.99885 | -44.89637 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2742395e-8f72-3dca-9157-9e32d97d3c42 | -13.09153 | -47.30183 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77668eef-ec5b-3e21-bdc5-d37bae13a8e6 | -12.00295 | -46.96596 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f767615-31c0-38e6-ad6a-2b2c7d601d43 | -14.3823 | -59.341 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc1b09bf-6e26-3d08-93d3-a60b05c98824 | -14.48581 | -50.29487 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d26a0ad-30b3-3bbe-89b7-bb1f30502638 | -12.37715 | -56.79959 | 2025-07-29 05:12:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7793e75f-74fd-3c4e-88be-9df4ee00a8c6 | -14.36356 | -59.33062 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b426bcf2-1a84-39a4-b60e-790c85e14df2 | -14.50318 | -46.54646 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5b8539d-e2d7-3b9c-b608-5f578095998d | -14.48611 | -50.29073 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0712873c-624b-3ab4-98f1-11b48d5fbf5c | -14.37237 | -59.33936 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f84c9b97-8bc6-37fe-9c81-35f2c45110ad | -11.63877 | -55.68529 | 2025-07-29 05:12:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e4c6cda-397c-3d2a-8154-8fdf0a566635 | -12.00051 | -46.95905 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab3f927e-f5b4-3df9-9cdf-e50d986dd827 | -14.35969 | -59.33361 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03c566d1-492d-322a-a237-14446a717bf4 | -15.508 | -57.42567 | 2025-07-29 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23b891ee-5872-3edc-a8e3-06bedf9204a9 | -11.52317 | -54.68159 | 2025-07-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9f11314-0e3c-34f3-9b02-f9a9d0c9a0a1 | -14.49873 | -46.54689 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03c7cad7-12db-31d7-8ec3-13ea926ea688 | -14.37624 | -59.33636 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11fe4375-2ccc-3526-87c2-68a1a6a64840 | -13.0077 | -44.88203 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b950634e-5358-3c10-88dc-98e9733adf34 | -9.96573 | -64.97583 | 2025-07-29 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b7e53215-8684-3653-bdd0-e0083cc36b58 | -13.00609 | -44.89677 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da4c757f-dfc9-3e5e-ac58-70b166e742a3 | -13.06405 | -47.3776 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d73986ef-4f11-3065-9b36-8e93a592146d | -13.00688 | -44.88948 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a905b44b-07a5-3591-bb97-0c0badd07d3b | -16.01605 | -58.00812 | 2025-07-29 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1eb5d98b-c51e-3dc3-829d-bec05f683473 | -13.10735 | -47.38488 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 191731b8-2d65-3641-94d0-5a797ce98eb1 | -14.48125 | -50.28689 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91081f20-bd94-37bc-93d9-e0786b7d81ae | -12.00352 | -46.96091 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aaf4bb9-4276-365f-86f8-c817a6d7725b | -13.48795 | -45.59692 | 2025-07-29 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
