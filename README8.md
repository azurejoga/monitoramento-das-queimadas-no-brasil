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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6680bef6-c48e-3a34-a5cf-662367cefa8b | -5.5884 | -60.180901 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6eeb6c-3b49-3d69-94e1-a9df3836870b | -6.7092 | -44.1637 | 2026-09-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbeda45e-f926-3465-9ef3-09ebfe611c34 | -12.1886 | -47.008099 | 2026-09-24 00:16:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 097610ac-842b-3ef1-ba22-ca94d48723eb | -9.0454 | -48.138699 | 2026-09-24 00:16:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddc2f24c-96f3-3f02-85b8-86fb96f8edb1 | -9.8595 | -48.490398 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0371b5ce-4e3a-39c4-9b12-502afd42e12c | -5.2513 | -49.219002 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f5910b-31b4-335e-ae16-5b5cf78973be | -0.9331 | -47.547798 | 2026-09-24 00:16:00 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75743b99-f3bb-374b-a5fd-55ca2e419112 | -4.3001 | -49.117401 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2577d08-7c62-3f50-ba6c-1abd09ac3a96 | -4.0972 | -56.179798 | 2026-09-24 00:16:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b57bb6-cca6-30a7-becb-f7a08b209a8b | -10.0956 | -46.064499 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea90866a-dd17-3699-a64f-348214965639 | -8.7391 | -44.250801 | 2026-09-24 00:16:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f25efd3-bf4d-3302-ab2e-cb62b8b12351 | -8.2563 | -48.2066 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50baec7a-cd5c-3b7c-8968-b3f24d036c71 | -2.4474 | -49.217701 | 2026-09-24 00:16:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 971bbeb9-e664-3a6c-8640-0340a5b7d115 | -9.0752 | -46.071602 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff6d3161-48ef-3df6-9768-f8b2b0464f08 | -2.5584 | -54.7155 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbf00ee-c7b4-31e9-b878-dc366005b21f | -10.1333 | -45.532501 | 2026-09-24 00:16:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fdc8bfac-b784-3583-8db7-e3ea844edda5 | -12.1635 | -50.750999 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 161019d4-7b9e-3e28-92b4-3c574379e434 | -13.0743 | -47.3955 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d355f006-d566-3ea4-b6fb-98d4842eb1e3 | -4.0244 | -52.073002 | 2026-09-24 00:16:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb1857e1-2cfd-3131-9f96-8d3c04f742b9 | -9.0874 | -46.079201 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9193cc3-4be0-3a61-80ff-b3a617a908d6 | -6.4084 | -43.475601 | 2026-09-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd872757-6771-3426-bf96-6f9448f7541a | -5.957 | -49.959 | 2026-09-24 00:16:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fffad71-3da1-3e95-b6f2-0bf0e069f882 | -19.185101 | -47.348701 | 2026-09-24 00:16:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ded361f-25c8-38d5-9607-9a5f8f61cc1c | -8.2367 | -48.211201 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42f850b0-f18f-39d2-b34d-5e9f231a0e82 | -3.2395 | -54.310001 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0514b89-cffa-3326-84b2-d5e3d3f737a0 | -2.8141 | -46.697899 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e020e9a7-6361-392c-aa85-087b8af84e22 | -17.4247 | -42.4627 | 2026-09-24 00:16:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c28e41c1-bfca-3d5b-ad4e-156029bda90c | -7.4175 | -49.8517 | 2026-09-24 00:16:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98367c29-65d6-3ef9-b652-e27e3a346c92 | -6.4377 | -48.460499 | 2026-09-24 00:16:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 80ea0ab6-cc9f-3c41-b068-5aefbae5a0f0 | -9.0776 | -46.0816 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af657880-a52f-35e4-a48e-35b641c8a97c | -2.3808 | -48.5219 | 2026-09-24 00:16:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7953051d-78c1-3fb3-bc92-3037e71f7316 | -3.1737 | -48.029499 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1a0bec-a83e-3cfa-a50a-c75535860ca9 | -11.274 | -51.337299 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c782d866-022b-39da-ae8f-4d3fff628959 | -10.0789 | -46.037701 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e16c54c-38da-36a6-b0e4-5978120bb5b9 | -11.2426 | -51.381802 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91cc64e5-a6a6-3062-8ab7-b2aa5b4a0867 | -7.5213 | -61.444302 | 2026-09-24 00:16:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9065762-7845-3904-8988-ae10bb24d103 | -12.0234 | -50.3046 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14a88da8-bde6-3e25-ad2b-5f8b126c1dc3 | -8.4625 | -48.696701 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f45199ca-dea2-392c-9b20-b5ac76f393fc | -15.4604 | -47.8946 | 2026-09-24 00:16:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 770ef7d7-9e43-3e2d-ac25-3c1d81783b37 | -1.8202 | -55.324001 | 2026-09-24 00:16:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 089c83bc-3c9e-3f9f-9437-16eee1447f03 | 1.5974 | -55.9636 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748c3501-7abe-3b78-b41c-8d222a8cf879 | -5.5675 | -42.301998 | 2026-09-24 00:16:00 | METOP-B | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f31b913-ada7-30e5-af27-d57084f3a47d | -12.025 | -50.3116 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4e03706-e6b0-3a8a-a2b1-00f8702e59bf | -13.0627 | -43.277599 | 2026-09-24 00:16:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 779549f5-5001-3d8f-a1dc-ce238ea7b948 | -1.8231 | -55.702999 | 2026-09-24 00:16:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9400522f-4ec1-3314-af0f-817ac73d23ee | -2.8239 | -46.695702 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8071e7ef-d798-3be2-aa54-70298fef1d9e | -3.5595 | -53.486801 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49d600a1-8839-3add-a57e-c8ef3578b2d5 | -2.3905 | -48.519699 | 2026-09-24 00:16:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e15169-9fad-3720-920d-88d1918c244b | -8.8724 | -49.7201 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 330ea05e-df3f-37dd-ae0e-9bdf24e09e84 | -2.8899 | -54.082401 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b2784e-29ce-3d78-85e0-1f88d5128ac0 | -7.2632 | -46.784199 | 2026-09-24 00:16:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4211682-e0dc-3ee2-9ffd-e7941271e2c1 | -4.0622 | -56.207401 | 2026-09-24 00:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750b3ff7-0853-3d6b-9379-c335e563389c | -10.0886 | -46.035301 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 649b3390-1293-37cd-8377-6d59adc50e34 | -12.1471 | -47.3606 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40c549a6-d7ff-389b-bb24-a5955e85d611 | -12.0015 | -52.4632 | 2026-09-24 00:16:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f89a68-681b-3166-bea4-55ccb22a3055 | -10.2768 | -49.958 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb8e40da-5170-3f38-9418-d3517376c2f2 | -2.5717 | -54.728901 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c576314-f124-37e4-8adc-0761da738803 | -6.4479 | -59.9254 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf607f1-a8a2-3703-ae1f-13df5bafde52 | -4.061 | -49.063599 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf1c66e-41b3-3d22-bb2e-054d65277a61 | -5.2359 | -49.286701 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5b3da3-2cfb-3ebf-82eb-1147bd6893a3 | 1.294 | -50.8391 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 10427485-2f80-36cd-8f9b-a0a9ac6ba21f | -10.2654 | -49.9533 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8143d025-35ea-3dd4-a215-cb501a465786 | -2.8236 | -60.194099 | 2026-09-24 00:16:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd163870-9567-37d2-8937-f26194f2685d | -10.556 | -46.6987 | 2026-09-24 00:16:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0027625a-264b-31a5-9bec-a1f9c1acc05d | -14.9638 | -47.528702 | 2026-09-24 00:16:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bff8375f-e013-3266-8822-c1d988125c73 | -7.5851 | -57.6437 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe68eabb-23c8-3cfd-9f66-6c2bbf2a5632 | -6.4285 | -59.929401 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08d8a6d2-f1d2-3aae-a07b-5b82b46622f0 | -2.3884 | -48.510899 | 2026-09-24 00:16:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44507906-b506-3728-be10-7c05b16080e7 | -3.4182 | -54.004799 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162a68fa-edbc-3818-86c3-e7d82e127557 | -1.331 | -54.6595 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45479f85-ac7d-3a93-844a-01792b61571a | -9.0156 | -49.805801 | 2026-09-24 00:16:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c417289-73d9-39b4-8482-07d410ebddc6 | -6.6074 | -59.911701 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f103bca-91b7-3b05-b99e-7ce56f616f53 | -9.0436 | -48.130798 | 2026-09-24 00:16:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5a79d37-4601-33dd-a6bd-f73a91061b46 | -5.2279 | -49.296501 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff74ded-7fb6-3196-9b68-3a1906dea387 | -4.0213 | -52.059399 | 2026-09-24 00:16:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10aeb283-e40a-3f41-b64c-49fbdf989603 | -5.2531 | -49.226601 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e34dfdd-d900-3875-bf78-56967b62c754 | -10.0933 | -46.054798 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec375e77-8dd4-3525-a01f-dd0a4a2163f8 | -5.1098 | -60.223 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 496f8608-a316-334c-8c90-bc2f53b821b2 | -14.0063 | -42.915401 | 2026-09-24 00:16:00 | METOP-B | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a7696ab4-ef5c-3809-8f06-39775f1e7fd8 | -12.4152 | -46.9618 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e050b59d-e3f0-3270-964a-bc5860857f9c | -3.7291 | -59.3951 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d34c70c6-53df-3493-a1bb-a6a613089e72 | -8.0906 | -54.9772 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14e22a63-8481-3633-b063-758e00f60002 | -3.2313 | -54.319801 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d755a2da-df07-3db2-82f4-703ac20ad62f | -3.7932 | -52.418598 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c533cd-acc1-3d35-92ce-edfe9eac5f78 | -12.1423 | -50.748402 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ba0c65b-18ed-332a-9eaf-cee72f3e36a2 | -8.31 | -50.3769 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a265a84c-fb8f-3aee-a3e9-b2fb7b306a4c | -10.2876 | -47.533501 | 2026-09-24 00:16:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14dfbb75-2d80-3723-b4c5-680bf15e7f2d | -10.5734 | -46.685101 | 2026-09-24 00:16:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 056bbb3b-49e2-3b78-b968-36d7fc06f50e | -12.3489 | -48.187599 | 2026-09-24 00:16:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21320926-16a5-37da-a57e-5b6b9de4db0f | -6.303 | -51.119099 | 2026-09-24 00:16:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85d00d2-d133-34af-983b-c0cbb2085f82 | -11.7927 | -50.9828 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b2685ee-04b6-3ac4-8754-875de9562b20 | -17.9652 | -47.841301 | 2026-09-24 00:16:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 638b5d38-4610-3e01-8524-a7a3b61d8c87 | -8.8227 | -50.456902 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e04a074-239b-3317-9c66-ed7e66bc2132 | -12.1453 | -47.3526 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39aa79a4-90ed-33da-a7db-d522e2a48af2 | -11.9628 | -50.7743 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 696e4854-fd81-38cb-8824-96eeb4c5cf61 | -2.924 | -48.7351 | 2026-09-24 00:16:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 435e3101-b7f0-3b07-908f-dd2f85ca42b2 | -10.089 | -45.993698 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b240e0f-7ceb-3e37-a7f2-9ccda5cb8b43 | -12.0902 | -50.745399 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0adb1d3-c995-3469-bdc1-40354d6461d4 | -9.8364 | -48.48 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab7341b5-1974-338d-ad4f-5061ed247780 | -3.2139 | -53.369598 | 2026-09-24 00:16:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
