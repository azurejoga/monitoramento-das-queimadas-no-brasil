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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3824b5c8-670c-328b-810f-46d4d52977ae | -3.97261 | -42.49416 | 2025-10-17 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 11840b64-7a7e-3db9-b65b-cd32ae81b47c | -2.73241 | -48.30786 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ce5ceb0e-a377-341c-8b14-316f975f8705 | -2.87362 | -50.71681 | 2025-10-17 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 36deedd2-d97a-349d-af85-78f3510649de | -0.90698 | -47.54945 | 2025-10-17 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae6c2980-3f2b-3d5d-840c-b619bf278958 | -4.11417 | -48.02655 | 2025-10-17 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 699ce2eb-28b0-3bf5-a324-6d0f0a153353 | -3.23025 | -45.95102 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 979766ce-0eea-30d2-8a46-b4138ee19d93 | -2.7385 | -47.1374 | 2025-10-17 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4900fc90-021f-36fb-ac23-fee50df5b24a | -4.05187 | -47.5032 | 2025-10-17 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c089e4-5a5b-3ec4-94cf-feadb7198d36 | -3.29313 | -43.23931 | 2025-10-17 00:16:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7402923d-8a07-3989-85d0-eda629fc4540 | -4.25743 | -48.55037 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2e0ccbb8-ab79-3f19-b13b-fb5be621c677 | -4.11266 | -48.01558 | 2025-10-17 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 47effcc6-332a-36eb-903d-b39415b4d79c | -3.5896 | -42.83761 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cfa4b70a-41bb-3df1-8d71-f045938ee9e8 | -4.43481 | -50.55273 | 2025-10-17 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 53e6a20b-6ecf-36b6-9be5-1a9edf6bd2a3 | -2.70789 | -49.40604 | 2025-10-17 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 404c15ee-dda2-3129-b889-fbfbef0f4e12 | -3.24275 | -45.97633 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 268.5 |
| 6eb3eedf-d669-39ea-a76b-8b1ec96037cc | -3.52974 | -50.30811 | 2025-10-17 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 55772147-1880-3497-844a-d74ed40f027b | -2.53746 | -47.8055 | 2025-10-17 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9951a9c-7f46-39b4-976d-7dfe84d1f8ee | -2.86623 | -50.75062 | 2025-10-17 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7e30753c-b493-368d-9790-bea033171e06 | -0.89784 | -47.55074 | 2025-10-17 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 435fbee8-3261-3843-a45f-22be8d499090 | -3.53763 | -44.31277 | 2025-10-17 00:16:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0784d1d3-ad45-343c-9eb0-fd3e045257d5 | -4.02632 | -45.31763 | 2025-10-17 00:16:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e013abc0-bf78-3cfe-bc44-b5ca8efdd081 | -3.27749 | -45.83635 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e24bff26-4767-3bc5-b0e8-90a0e670e9e4 | -2.96483 | -48.59007 | 2025-10-17 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8847bd3f-e11c-36e9-bb08-7ba54fb839d2 | -4.01722 | -48.97002 | 2025-10-17 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 54f3c322-bd73-301e-9609-565971f4267f | -3.53173 | -50.31425 | 2025-10-17 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a69e0eda-9558-3cbf-80a8-d5b2ff22ac71 | -4.01737 | -44.18628 | 2025-10-17 00:16:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4e07beb-a942-37c9-bf26-812f69b2e005 | -4.00037 | -43.27597 | 2025-10-17 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 05d86e7a-3351-321e-ab4c-3d240338636b | -2.86408 | -50.73449 | 2025-10-17 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 879a1520-fd51-398c-88b3-555307d54ae7 | -2.65179 | -48.39169 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3f41d89e-5338-3449-b59a-e6132a8afd05 | -3.1599 | -46.31795 | 2025-10-17 00:16:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d6c08310-9b8c-3749-afcc-ec5d4e4ddfdc | -3.24153 | -45.96746 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 1d18a505-da44-30fd-a538-045541d1c2ac | -4.41628 | -45.73254 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a038a6d-00ec-3f9c-8c74-995575511575 | -4.56539 | -46.61825 | 2025-10-17 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4bb30379-0b3f-3907-a764-8c979a50dc45 | -3.98228 | -42.49277 | 2025-10-17 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 2892529a-e511-3ce1-bed9-305b2c90fd9f | -3.23268 | -45.96872 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 375abeef-869c-3043-83bd-467bf715c7d9 | -3.12683 | -50.20985 | 2025-10-17 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a04067bd-1fb8-3bda-848d-16ef30273045 | -4.13641 | -44.63772 | 2025-10-17 00:16:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 31755e35-d1a3-399a-b501-81ea9c3e5c7d | -3.2339 | -45.97757 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 4123e969-5df6-3372-b54d-819dbd986f94 | -4.55631 | -46.6195 | 2025-10-17 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c433df4a-c7ff-3541-9fc0-632c35eead1e | -4.95709 | -49.56974 | 2025-10-17 00:16:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 797fe94e-4e36-3887-bc1c-d1082a4ca670 | -4.46501 | -48.26988 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3efeadba-77a1-31fc-bfaf-7e0c22e573ea | -4.56667 | -46.62755 | 2025-10-17 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d86f6547-4d9d-39c0-8cf9-6ebe83adcb50 | -4.35888 | -46.72618 | 2025-10-17 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| acc3421c-30ec-3ca0-9c83-011c39c7b056 | -2.60341 | -45.02715 | 2025-10-17 00:16:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 49103ff9-4e72-318e-9ae5-6586696b814e | -2.75186 | -48.30521 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cf5b5e89-c5f3-32d5-a0cb-a4ef266f4b30 | -3.62267 | -42.76293 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 60f22a0a-be27-3d7e-a008-6d631dff8ce2 | -0.89653 | -47.54128 | 2025-10-17 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aec01a4e-d51e-3a44-84d2-40ff17bf7a4b | -3.59104 | -42.84793 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82725825-6f7c-3776-90ed-83fdf957c9f8 | -4.54501 | -48.41044 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fceb00a7-cefc-3236-aa84-ebb4ba0b6c61 | -4.53497 | -48.41181 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 62590b8f-aded-359b-8051-f2ea01ff2544 | -3.40602 | -46.89687 | 2025-10-17 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8db6279e-dd34-39f7-8d30-ca336d40543c | -3.51949 | -52.50579 | 2025-10-17 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7b2bcac7-0d0b-35f6-95b2-9d3cd68635d1 | -2.92562 | -48.30214 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 417708c6-d2b6-3eae-a6b8-3780c94993db | -4.55759 | -46.62883 | 2025-10-17 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 07faf450-5b36-340c-b9ca-796aa97b90e9 | -3.24397 | -45.9852 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80af386c-0092-3448-a0e6-f240fbd4c5aa | -3.77582 | -43.4447 | 2025-10-17 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| ebf8d364-05cf-3e68-857d-1c9c1290482e | -4.41292 | -48.94255 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2ed82a68-6bab-3a1f-9568-e393e391b701 | -3.98379 | -42.50346 | 2025-10-17 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 9c038bce-49fb-3c93-8f0b-8d1336086186 | -4.13517 | -44.62886 | 2025-10-17 00:16:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb5e4bf9-22d2-32ec-a1c7-e4d37a9066ec | -2.74986 | -49.40031 | 2025-10-17 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b54fe2c3-8b04-3381-a81e-bb923b1c5754 | -3.60125 | -48.98152 | 2025-10-17 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fa173ab7-daed-3d45-a3cb-b7b1a865f522 | -2.73761 | -49.38901 | 2025-10-17 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3c38192c-fc8c-3370-8544-460aa46406dd | -1.49658 | -47.81424 | 2025-10-17 00:16:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b292da77-e102-38c0-a061-d0593568576f | -3.99195 | -42.49138 | 2025-10-17 00:16:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 155580e8-35d2-3db5-9925-67510ac04698 | -3.50573 | -52.50703 | 2025-10-17 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 12dfde98-8d07-3ff8-9b42-52db0484cf5a | -2.74362 | -48.31741 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| eb82e71f-04f5-3f29-b302-13724c6ab023 | -2.74214 | -48.30658 | 2025-10-17 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 090329e3-efda-339e-8f6e-e6a73e942c47 | -3.50264 | -52.48399 | 2025-10-17 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 415.1 |
| b6c6347e-015d-330f-a0e9-fe7ac256959d | -3.53407 | -49.00957 | 2025-10-17 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 641ed0e2-70ff-3e4f-a609-1a322b4dd7b2 | -4.371 | -48.71053 | 2025-10-17 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e3081f16-c9ac-3b02-9d52-62b955697992 | -3.54268 | -49.01459 | 2025-10-17 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 072d88f7-6ca2-3f29-bc94-45e1c291d528 | -2.7481 | -49.38763 | 2025-10-17 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| de6fb2ad-aa43-3118-b1f1-9b6437e9eadd | -3.24032 | -45.95863 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 959dc247-c081-3f8d-9c9d-558502c6894d | -1.73225 | -54.4436 | 2025-10-17 00:16:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 34bdfe31-7882-3c5a-8f38-8785f85a25bf | -3.84325 | -47.06669 | 2025-10-17 00:16:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bd6e92fe-1551-32a2-a0a8-a836e8c8f0fd | -3.27627 | -45.82753 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 665c5b8a-57cf-3a52-86c7-d04ffd20e413 | -3.23512 | -45.98643 | 2025-10-17 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2b60d2b1-d567-37a0-9e34-29590d981c53 | -3.45184 | -41.85259 | 2025-10-17 00:16:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fb8e53f0-7531-38f3-92aa-89d86beb4d4f | -4.04245 | -47.50449 | 2025-10-17 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ca581f07-3e2e-365a-b36d-2053ace4439c | -2.73937 | -49.40178 | 2025-10-17 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d499cf74-d024-325a-a60e-b3c0d86377df | -4.14631 | -47.66061 | 2025-10-17 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 909070b9-6593-3375-852d-14398f44c1e0 | -3.23752 | -42.07557 | 2025-10-17 00:16:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fd638c3e-95f4-3443-9411-69704aab7611 | -2.87578 | -50.73289 | 2025-10-17 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| a87be2cf-6fec-3a5e-bd2a-549c15e711e8 | -3.62415 | -42.77335 | 2025-10-17 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 70e456cf-f035-39ea-8eb7-e5ed68880ed9 | 1.05007 | -51.22563 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3776d0c7-f278-3390-a9cc-108aca112915 | 1.09692 | -51.14031 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e6bf3c38-862c-3425-b568-bfaad3940f16 | 1.01675 | -51.13867 | 2025-10-17 00:18:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f3957824-2131-3a4c-ab19-b0bfb2d2b53d | 1.15444 | -51.13958 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1a73bcb6-21f9-32e2-89f6-2f7abbaf661d | 1.09481 | -51.15524 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bff94731-1816-3fb5-88ed-9b1c11fd6ae0 | 1.05224 | -51.21058 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8d333074-3d51-3197-b2dc-4a3172c29d22 | 1.06144 | -51.22722 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5e4e63fe-2cc1-32dd-adbc-f15696d2af5e | 0.88012 | -51.1284 | 2025-10-17 00:18:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c7b92b27-d674-3073-abe7-cc3aa5378d6f | 1.09902 | -51.12544 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 21a33763-027b-353a-b72f-6019713f05a2 | 1.08845 | -51.20031 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b5f0586b-081c-3381-b4eb-fa677083b0d3 | 1.06361 | -51.21213 | 2025-10-17 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 539dba50-5fca-3dc3-8b70-e5850b8d6258 | -3.2359 | -45.9862 | 2025-10-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 214.2 |
| ab857766-cd61-30ad-adee-cf594a1f8eba | -10.514 | -43.3815 | 2025-10-17 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| c0a7bcaf-48c5-36f9-82fb-32c18b660216 | -2.744 | -48.3238 | 2025-10-17 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 19bd25ce-62ee-3b87-80cd-768a0211ae4d | -4.4061 | -43.3816 | 2025-10-17 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 3cd49a13-e014-3a1d-bb39-bdee1d9ab303 | -10.4302 | -45.0232 | 2025-10-17 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |


[Clique aqui para ver as próximas entradas](README13.md)
