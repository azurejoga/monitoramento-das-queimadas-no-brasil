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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3c6bab9-f8d2-3df5-8d80-83b8280d7bc9 | -5.12984 | -56.20348 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 008353ca-5058-3e27-8e03-96dabff3ea34 | -2.29695 | -57.08459 | 2026-09-18 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1813a82f-7521-3ab5-bb8d-80bc3b68b79d | -4.5496 | -54.93297 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa948fca-a9d7-37fc-a472-df75fde7aaf0 | -2.70427 | -57.60041 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f1267c1-b7f8-3d02-a05c-0b512e088cdc | -3.36203 | -50.45064 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82213511-a962-3ec5-9ec1-03d58a5c256d | -2.82281 | -50.47433 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 83d7717f-1a7b-3a51-b68b-256282db6349 | -3.04239 | -51.37217 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5e4c128f-e80c-34ca-9c88-5bb52ec6dd5d | -3.37087 | -50.44621 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fee9ed10-4c40-356c-be51-ceebfeef4283 | -4.51841 | -56.07618 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9a6cacd-2542-307b-b539-514023ca05fb | -3.44616 | -58.2153 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3245b66-239c-3489-acea-5264aac7beba | -4.43445 | -55.78664 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a94d154-41ab-3878-b8db-1758891c8274 | -4.57335 | -54.9169 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c108547f-bd49-3b3d-a928-bb7c528f8940 | -4.53864 | -54.93513 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c38685d-ea1d-3d61-b279-48370b5e4b5b | -3.92421 | -55.92615 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46d049f5-a931-39cd-a03f-88995ed4fb1f | -3.9214 | -55.74809 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afcf185c-3a61-35ba-a791-31767a551e9e | -1.4957 | -54.97236 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0123fc90-f236-3897-a4b7-460c684d9d9a | -3.2626 | -54.27082 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e663f778-4347-345e-a6ce-c205a327a834 | -6.33413 | -45.67546 | 2026-09-18 05:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16f055ba-e7a7-3b57-91dc-70b3b8deb95e | -5.73831 | -52.24495 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82f3f5d1-5914-3dff-aef1-76560c12ab0b | -4.36999 | -55.41516 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b0ee4b-3b8c-3b94-955d-6b8b2bf8c748 | -7.34425 | -44.64335 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16ccec08-9289-3946-805f-62de3ec1f1e1 | -6.29993 | -57.78662 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b40026c-bac5-3532-9fa6-b51747e316ee | -4.07153 | -56.24004 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06f88d27-c67b-3df9-8f12-fdaddfc9c2d1 | -6.36902 | -58.29294 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25fadf9b-6a3c-3531-bf27-546bb1b453fc | -3.36579 | -50.44992 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef0445be-0db9-317f-a086-e7669a22a312 | -1.49176 | -54.97543 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3127f874-db20-3616-a995-5642023d55e5 | -6.11889 | -44.02522 | 2026-09-18 05:16:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dbb16a2-79b1-3431-80b1-fce7af8a29fb | -3.44563 | -58.19696 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e517085-2306-3625-9279-664ed33b2597 | -2.6401 | -54.68972 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd5b26ef-e952-34ee-b715-48f698930871 | -2.82413 | -50.46588 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d05e10b-da15-3f2b-922d-35d432ee0edc | -4.53461 | -54.93836 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a988ff9-86b9-343c-b02b-38c57332d064 | -4.88403 | -56.06361 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a01598-bbd9-3afe-9f46-8c4556dc2466 | -6.4525 | -52.84946 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62edd8ec-e974-3946-80c3-9529a3552252 | -2.19703 | -56.08479 | 2026-09-18 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4aa8799-049c-3614-b3a4-7f0490eda1b6 | -2.8962 | -54.18176 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da558d37-47ab-390e-934f-a69196fe4277 | -3.26733 | -54.26355 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eee022a-0512-3c83-b2a2-675bd02dab26 | -7.78938 | -44.90254 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cee783e0-cdff-3007-b9db-d8b05aa78d8a | -2.9127 | -50.41632 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8614eb90-b41d-3900-aab4-933ef23232f1 | -3.70755 | -54.17768 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0218ea-8ef8-3c91-b4a7-e238f61f2276 | -5.75037 | -45.09755 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4c97c307-2552-3c0f-8441-beb347affc29 | -5.97502 | -55.3605 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b61163d-59b6-3437-8874-4a1f2f1b69a5 | -3.49331 | -54.72114 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28694c9f-e693-315d-8d46-86571da3f820 | -1.20057 | -54.21733 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26fb8c96-190c-3e20-999e-d08ffe22b0e4 | -7.66294 | -46.09226 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0b5f0be-dfe2-3bd5-976b-b2307835f396 | -1.17883 | -54.17536 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a73e4bf3-a2c6-3e52-9dcb-dbf7ca29cab2 | -2.0564 | -56.84527 | 2026-09-18 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caa555c1-c5ce-3e42-9303-17a548e920db | -5.73474 | -52.24097 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9726547-f8bf-3e27-9b5d-3f8848d8f698 | -3.25909 | -54.27026 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1fc5bb58-ce11-3bf6-8c6a-d7f94ebf463a | -3.69756 | -60.6151 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4185483-77f1-355b-a207-b7fc67b16acd | -4.36942 | -55.4188 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8894f4bf-5186-3a4a-842d-78f7dd21f470 | -3.79633 | -55.87349 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ac90d74-df57-3588-8fca-61757d6b49ea | -4.30039 | -56.2539 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 148a7d81-986c-3326-ad69-123571ced0a7 | -3.27888 | -57.92075 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5960c0d5-4b89-3cbc-970f-adc400c65f66 | -2.82364 | -50.46848 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9cdaa031-23cf-3bb8-95c9-8cef3b447ee6 | -6.01602 | -51.77055 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edf50e47-7807-32cc-b574-860bd7769691 | -4.48087 | -54.97332 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be44fa8d-7915-3abe-bbad-aa897be574e4 | -2.69037 | -57.62327 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e9cdd16-c8d6-38c2-b8b6-8a8076fa2e3d | -5.19161 | -49.33358 | 2026-09-18 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be898ab6-36e9-3691-892d-ab0564d454fe | -2.8974 | -54.17701 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b005ef2e-bf3e-36fa-94fc-0e0890b14a2d | -2.96049 | -52.14804 | 2026-09-18 05:16:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb9e4cb2-08f1-3062-953b-211c83981cd4 | -6.45303 | -52.8524 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 634c3a0f-6463-304d-b533-59e8ace3edf9 | -3.47894 | -54.69957 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 838fc593-a982-3791-8c86-5ada67330537 | -3.43721 | -58.20658 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b669e53a-9ccf-3280-822d-f7d67ea2602c | -4.42686 | -55.52411 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a09bb1cd-1c15-3092-bcc8-c6f4449feafc | -4.5173 | -56.08325 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ed04f35-609e-305f-96d0-0c02f58648c7 | -4.38413 | -55.03215 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d12fdc8-6180-310e-8371-03309859ebda | -6.3349 | -45.66973 | 2026-09-18 05:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09a55d9f-8c53-3896-80a8-e31ad8e36b49 | -4.88347 | -56.06714 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70ea2ebd-7c81-3aec-be04-648f591bd681 | -5.17721 | -56.18555 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c35eaff9-9d56-3f03-bd73-efb4abd92556 | -3.37153 | -50.44177 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e75d93b6-c56a-3bfe-9372-72c8f9c40d0c | -2.81908 | -50.46944 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 846fb584-f446-32c3-97f5-91885c041ce3 | -4.53577 | -54.93078 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7b577fca-12de-3d7c-8664-9d3f6cf16ce3 | -3.32991 | -57.85345 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0dcdb06-b754-3f1e-a39a-5bd46437120a | -3.36644 | -50.44551 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 606246b6-87e0-353a-a5fc-a4b7436c5d80 | -6.11784 | -44.03315 | 2026-09-18 05:16:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99aa6129-5013-373c-af49-14dcf254c5fb | -4.43362 | -55.52528 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd9a733f-5984-3751-95fa-7d9e93abc920 | -4.36159 | -47.78113 | 2026-09-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fbc32d7-f69f-3866-bff4-7f69479bed3b | -3.81534 | -58.89396 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3e576d-89c2-3cfa-9f81-66fdbced025f | -7.66154 | -45.84175 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd4b11ce-d698-35a4-aba6-9502f9a45471 | -4.33437 | -55.44301 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aafc090-edcb-3c2f-9cf6-5aee137f89d8 | -4.56759 | -54.90827 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4419e61-1094-3acf-881b-0957f4c52fdd | -5.17386 | -56.18503 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c55e7f-1198-3eb0-823c-42430d5daf2a | -2.74756 | -57.6287 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713cb3ad-b1de-3cdc-9b41-1f6bfdf33a10 | -3.20545 | -57.84431 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dad8a970-e535-3805-84e1-2c3e25e840ff | -6.27009 | -51.74635 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8f09a92-60ba-3ea6-9e2a-a34703ccbd03 | -3.36134 | -50.45504 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82e4bc83-a3a8-3a9a-ac2a-bc58f2b6266e | -3.30262 | -57.87432 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b3c8aa7-7cd6-3c6a-8a5a-a743e56bc75b | -4.30092 | -55.72587 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 262657e1-74c5-34a3-a3f4-65e31c2013c5 | -2.70482 | -57.59692 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a40e070a-d20c-3f05-915d-bfcfb3e209f2 | -5.33312 | -45.14911 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45415dae-24f0-364f-b2c6-499cfff81bf2 | -3.36006 | -50.458 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae9016ca-ba5a-3a45-a372-f87f3de1b044 | -3.4428 | -58.21477 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a17d847b-851d-3354-948b-7dd908dd8f5c | -4.3509 | -54.79071 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bc3587b-b6fe-3f20-ae25-968053c6e10f | -2.25684 | -52.02803 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3daa91da-90c7-3834-89ae-28c685d64018 | -6.36293 | -58.28838 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c33df05-360e-3117-87ac-de348ac5f72c | -2.81468 | -50.46877 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 735419b8-d6c1-3a3c-94ee-474dc0639a57 | -4.53519 | -54.93457 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36b257a4-af77-3303-9e26-97738034e25c | -5.86659 | -52.05126 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6014bc8d-3729-3cfc-943c-b80aa46e7b89 | -7.45732 | -46.84363 | 2026-09-18 05:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 961d018e-f04e-3953-93b1-64684c948145 | -3.18126 | -57.82977 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README79.md)
