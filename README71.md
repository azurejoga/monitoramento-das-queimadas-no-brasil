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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e6ebfdb-f430-3164-bf17-14093472af0d | -2.94905 | -52.14922 | 2026-09-24 05:04:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaae9e16-0d02-31da-8bd3-aac925fd4b35 | -3.41739 | -54.00576 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ac69e68-9e16-3973-8bd2-2ea5c3b2a375 | -3.17999 | -48.02759 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d510704-1f0f-32eb-b9d0-4bb7a750d39a | -5.19587 | -44.69509 | 2026-09-24 05:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 578afe5e-25ce-3834-a634-0f1089aa77c0 | -6.30763 | -59.94902 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11e21067-0347-38e9-9295-66f7fb9c7f8b | -7.55742 | -55.01911 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b53a897-f08b-3bac-b3b3-cb8d40dbfba0 | -4.51559 | -54.9843 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec4213d6-933e-35c6-a1b3-f1734f0c644e | -6.00258 | -57.72638 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa289fe5-e2ae-3f28-a4ce-1af683ada726 | -6.441 | -59.96168 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ff57bc4-b127-3c7d-9582-233d7c202b6e | -8.07915 | -54.75072 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4758057d-2a25-3dc3-b959-709a32124cf9 | -3.4604 | -50.07866 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b262fc94-80d2-3feb-b223-251b6be59484 | -4.50226 | -54.96056 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5e20f9-6efc-370c-9a7d-5e8e90803f29 | -10.09 | -46.05711 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 659cb8df-2f34-3b38-8a44-e8aaff3ee253 | -5.49829 | -49.02641 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78bfb2b0-ab7f-331a-9979-50d68060ba2e | -3.2684 | -49.14515 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66214a17-7f2e-3292-84f2-eb3b157926a8 | -9.25832 | -46.24616 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a6fe8d44-e7d9-3d41-90f5-4ce7ff94f7e3 | -3.42015 | -54.00972 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fa557af-382a-344a-8fe0-abc8cd077362 | -8.15179 | -49.54423 | 2026-09-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2304f9d1-4b2b-3623-98f2-d48ab96bacf4 | -8.27015 | -54.76729 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf614c78-dcc8-3d19-9dd3-f6a00d6309f2 | -5.10551 | -60.26254 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 716e3553-de8e-32a6-aee7-8c2afded66c8 | -6.60669 | -59.92759 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d27d1fb-ea30-37b1-aae6-1c3ddc8c6301 | -6.43145 | -48.46786 | 2026-09-24 05:04:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7beaacc4-0d94-3bb5-9357-06b63a5a3461 | -3.44699 | -50.07856 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 112a7bc5-5d21-37ce-aa2a-8f06fc120c04 | -8.2663 | -54.77023 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd3c309d-56cc-3920-9024-eaa1c8ded430 | -8.2038 | -54.73503 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7fc5b17-2399-30df-b7e9-af636e3e879e | -2.9497 | -54.08383 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f93416-09e0-39ae-99fc-71dd14d8777e | -3.75224 | -59.30809 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19a15eb2-7d2f-31ec-aedb-6d0c8436e440 | -3.63667 | -58.92277 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb30ee5a-fcf0-35a2-8841-bf4e82800a43 | -3.22762 | -54.3224 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd07c35a-f80d-325e-9d40-4661debd29a6 | -3.41684 | -54.00921 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eecee115-880e-3b13-afc3-c064e4cae249 | -3.4419 | -50.0868 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cabfe5d-1dc5-3da9-b961-cdfd7785e6e4 | -5.95681 | -49.9715 | 2026-09-24 05:04:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 824959d9-96ca-366a-84b8-88e2d3379500 | -6.42369 | -43.48611 | 2026-09-24 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f82b51d-502c-3373-835c-a4200118bf92 | -3.7269 | -49.05615 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9953c7ea-d6f6-3e60-849a-e708fecb341f | -4.8372 | -55.76615 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 263164c1-0dc0-3c38-8fd4-aed0eaeefe2d | -7.50943 | -61.48808 | 2026-09-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c6fbe46-43c2-3e21-ba42-78013623d8d5 | -9.02208 | -49.81379 | 2026-09-24 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e761e3d6-8fb4-365c-a42a-fcabea69e32a | -3.01361 | -51.53244 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe7d481-ef93-3808-8c06-4b5bcfefdabf | -4.33947 | -55.21427 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8b1e205-04d5-3263-84de-1ed102e52b38 | -3.44861 | -50.09238 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a520ec4d-64ff-391f-b2ba-abfd3c551ce7 | -3.71003 | -58.85825 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6edcf5-4f67-3915-9b89-5fdb8d42de4b | -6.1101 | -59.88459 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1869fd6-10d1-3c83-b7c1-6f4f62639abe | -6.61784 | -59.93735 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| af41d11d-5090-3727-9503-fd7bc8e4310a | -1.27444 | -57.04028 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3695cb8-d682-36a0-866a-b99c87b7b0ab | -3.00668 | -54.17424 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d143b0-7f4f-3084-adaa-c84b3272cfc2 | -3.70648 | -54.19594 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5afe7db-5bf7-36fc-b5dd-4a4d32bf303d | -5.29195 | -49.28769 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 204b9554-bb9b-3dd0-99cd-a34ff97b78ca | -5.77021 | -56.52504 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0857b1f9-cc3f-3632-b9b1-cbbde7f9da9c | -5.17364 | -56.17952 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34afaa6a-17b3-3c62-b464-d471ed164266 | -6.43684 | -59.96097 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e5b92c6c-c8f1-3aca-bfff-48623c54e95a | -4.28721 | -55.26076 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce3ada96-17db-3585-8529-fba60e8a4d61 | -10.08926 | -46.06289 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd75c4b0-5ece-3180-8fee-7de4e80ca3f8 | -3.70815 | -54.20682 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e9a5b1a-77a4-3a55-ab5c-5d1dc48ff1e2 | -2.92213 | -54.15031 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d2aae8-b3cb-30bc-ba3a-f8a171bbaa37 | -6.10385 | -57.68045 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04a6351-34ad-32e7-a59a-2551a63f0005 | -3.45736 | -50.07367 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a043aacc-a8b0-3e00-90ac-44e58f2e2390 | -6.30529 | -57.75433 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 570d5c93-f8b2-3aaa-a0f6-60125902e4d4 | -6.23843 | -60.02799 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c0f2961-be97-315c-ac81-6cccb99bf7cc | -1.21728 | -54.55643 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| adc1de84-c96d-3b2b-bd2a-4ec0ccdf87b0 | -4.42517 | -55.07848 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cce78d6-7036-3b1a-87af-8b7874732ef4 | -3.8092 | -58.88882 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2387cf09-69fe-3ed8-8674-a1be46591a2a | -2.89441 | -54.08891 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9102fd9b-042d-342d-a366-bb3c3918db1c | -7.57209 | -57.65718 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5bbdc70-576a-3849-8542-a57f7c54bf5a | -6.43748 | -59.95725 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9ad1d835-0384-3cea-a85d-848727ed931f | -3.44629 | -50.08298 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59324b2f-f08f-3890-980c-3f0cecb94b22 | -5.91439 | -59.91898 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7a3aa61-b65b-3a09-af40-bb1ffcf5c0ac | -6.77568 | -42.374 | 2026-09-24 05:04:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8acdbd67-6436-3603-903c-6a708287dfe0 | -6.15892 | -57.70978 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7185aa3-3c55-35ce-bc81-5e048d4365bb | -3.26849 | -49.14682 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eb46f04-0656-3594-a647-30a4ab8f1d8d | -4.43748 | -55.0659 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9537b74c-ebf4-3bcf-8de4-bf9d7f23679b | -6.48219 | -55.98155 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3ba878d-b40e-35fc-8947-e7022cea0548 | -8.27346 | -54.76781 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| becd34e0-cd61-367d-9c9f-6bf9c7760056 | -3.15989 | -54.60097 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 515ef825-d274-3455-ae04-987644df9672 | -3.67976 | -60.5621 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25a338de-4b3f-3ba5-b647-9cf47286bf6a | -6.62143 | -59.99258 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5eb6fbe8-0278-3d36-bd4c-4c16eaf0ca04 | -3.01302 | -51.53621 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3be826fb-ac55-3ebf-8bd6-f8abd54086e4 | -3.70924 | -54.19991 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55b5c86b-5e2c-34b5-b025-715e4bd3079b | -5.90889 | -59.92593 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 334a1815-072f-3e83-a1f5-7704ad84cc2f | -6.60857 | -43.73154 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8aee93e-6384-35b7-a030-a8b5d1a6cfbd | -9.35018 | -50.10081 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0aa4091-5b2f-335b-aacf-fbf69d7f873c | -6.3477 | -57.77004 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ba54c92-1add-3050-977c-eb88c2a891e7 | -6.19069 | -57.78977 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf181aa-22a3-3684-88c9-603e45ad50a0 | -8.25236 | -54.77124 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 729a3395-7ba7-3b80-9b0c-f36c24d14afb | -3.21942 | -53.40982 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ae8675-dd52-3fac-b026-13f472eda95e | -3.0709 | -54.39001 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e4da98-6c2a-3396-981f-6e1721ead25b | -4.28664 | -55.26434 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55aeb193-8c40-3aba-a036-9186be179254 | -1.9161 | -58.2678 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0e2b5dc-8b6a-3c32-8846-90753fe6cc63 | -3.20831 | -53.37288 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd53fef1-65b6-3449-9a99-581b36110d6a | -6.33068 | -49.86336 | 2026-09-24 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24e54b7a-d486-3ecc-bee3-c19a57f865eb | -7.21028 | -60.68732 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c59131ff-6d51-316b-be92-5916e0220fde | -6.11489 | -59.88147 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97594562-9bae-3aa6-a0e7-929b5e13632d | -3.71256 | -54.20043 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dad1732b-da87-314c-8fa9-7af27f8d670d | -3.80515 | -58.88815 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b3111e7-a78a-3afb-8245-ec1cbf2fcc00 | -7.96901 | -45.22491 | 2026-09-24 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7be18bed-1c93-3ae9-afac-5d7e84894fbc | -3.03789 | -59.11686 | 2026-09-24 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18319ab8-9934-33b0-8a4c-c3b4411935a1 | -8.93493 | -45.94846 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa6e985c-ad36-3ef2-a5b3-b632be3ec868 | -3.67594 | -60.58518 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25d0129f-e339-32dc-92f3-79b17f85d5a0 | -4.99001 | -45.54815 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bbf064c8-b6dd-3810-8a14-2c1cffd471a0 | -9.57994 | -46.51283 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9f3d940-a294-319a-b939-120ae474bf18 | -4.29 | -55.26487 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
