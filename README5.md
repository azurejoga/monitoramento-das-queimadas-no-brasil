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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25ee7165-3972-3b59-85be-28d353a01ea3 | -5.5981 | -60.178799 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab31cba2-96e6-3177-971c-d446dd24119e | -11.7942 | -50.989899 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c701239b-4d98-30df-a1da-0b3cb59e684b | -8.2689 | -54.758202 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358c0fda-6097-365e-8f3f-dae2d723179f | -1.7786 | -47.827 | 2026-09-24 00:16:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4658b38c-dfce-3e32-8824-afc749e66297 | -1.923 | -58.258099 | 2026-09-24 00:16:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcb6ed77-ab58-365e-bd28-dfa45aa86da3 | -12.1606 | -47.3741 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68295182-1dee-33aa-bf10-79ca531ca40b | -5.2611 | -49.216801 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2330ff7d-da3c-318f-9415-15bde1554dc7 | -8.4891 | -57.5821 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3af0676-dc44-3dbb-8ae0-d5f98c4a2033 | -12.0136 | -50.306801 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 513ae0e3-7ab8-3a75-9c17-7eacf5c83507 | -3.0411 | -46.922901 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eae34fbc-d400-39bf-b691-bad28d0abbb6 | -8.2465 | -48.2089 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78ccc7a0-bbeb-3eec-8d75-59d7b1564dfa | -3.1813 | -48.018101 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3742a0a2-7240-326e-ad4c-862056ddada1 | -6.6654 | -50.944 | 2026-09-24 00:16:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ed0adc-ae6a-382e-9510-23d74b834c62 | -8.451 | -48.691399 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0d10a925-1c17-36c7-83de-e77397ed85a1 | -8.7423 | -44.264 | 2026-09-24 00:16:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8c01c0a-9731-3c3b-ae29-4ed15472a03a | -11.4557 | -46.7034 | 2026-09-24 00:16:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 139bb328-8ab8-3fde-b15d-45019365944f | -11.7963 | -50.9524 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cedb9f9c-0e03-3155-80e3-0c2e71459682 | -13.2038 | -51.561501 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 825bb078-e9e8-3c2d-8a0d-9df93e8bd83c | -7.4779 | -44.574299 | 2026-09-24 00:16:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7e5d40-a9ff-385a-bbdb-85693bf91bea | -5.7609 | -49.958199 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db54325-fa9d-3d10-a5d9-bbeba4d1d224 | -1.6429 | -54.901001 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4b40888-5479-3fee-9be8-56cc81a37c08 | -4.5032 | -54.9506 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ed0947-9c0c-3256-8dcc-17fb2b573f9e | -15.2381 | -43.244202 | 2026-09-24 00:16:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d0dab965-6272-332c-9044-3ce2ad737848 | -6.4221 | -43.489399 | 2026-09-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f832522-90b7-3ab3-b2af-1d6a29439018 | -9.238 | -47.371101 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf3ce320-d51c-38c3-ae8a-a3d2216a1ed7 | -3.4165 | -53.997398 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ac2f1d-b1b5-362e-9c42-0e7f2d0946f4 | -15.5613 | -42.351002 | 2026-09-24 00:16:00 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1eedddae-54aa-3894-b039-5cd247bd56a3 | -2.9768 | -54.148399 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf4318dd-6b84-3422-aca4-c889e89f853c | -11.4578 | -46.712101 | 2026-09-24 00:16:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9eaafc-ee87-38fa-96cf-a6cd5510027c | -7.1951 | -47.4604 | 2026-09-24 00:16:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecd635fc-2dcf-3741-975e-254563e6478d | -10.7203 | -48.734001 | 2026-09-24 00:16:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f210d03-254e-3c70-b4ae-2b99b9e3b7a3 | -6.6366 | -59.905701 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d340cdb-7daf-39eb-9264-5dedc397d2e1 | -9.8497 | -48.492699 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d35615c-f164-3426-a9b3-dcf6b7d16494 | -9.2636 | -46.255699 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a118842-3608-3d7d-a3b1-598ed38c6bfb | -3.0333 | -50.429798 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98794288-56e7-3452-9e01-dd3c0fdeaa39 | -3.8297 | -59.341702 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f32938f-02e8-39b4-a92c-a92c372b9acf | -4.3037 | -49.133099 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b66f0c80-089c-3db8-a631-e853838f4bab | -11.9581 | -50.753201 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b858a4b2-19d9-38a1-bb9e-c510cebcce9b | -6.5192 | -52.819302 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6e3ed2-8670-3a8c-a99f-0108c5f48873 | -1.2143 | -54.552601 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 842bfb2b-fdbd-399c-acb6-f3b9197c00fe | -10.4567 | -44.947601 | 2026-09-24 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef4171f-5281-3459-a2f5-4c873e56de5a | -3.7168 | -54.1894 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c835f403-1318-320d-a831-fdd8983cdc81 | -10.6432 | -51.322498 | 2026-09-24 00:16:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c090425-e29d-3fc1-b5ec-331b19f5b1a7 | -3.1771 | -47.999699 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb51101-4c07-352b-96f8-93332780e54e | -15.2442 | -43.2686 | 2026-09-24 00:16:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ee2e9aa7-d30b-3cbf-8005-45f6e637f18a | -5.7199 | -49.823601 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e1854a-07df-3746-be86-efaacfd76ec0 | -8.5158 | -50.1478 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e858da-f519-3ff0-b460-4f37710ac08a | -3.4395 | -50.086201 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f83f690a-fa69-35e9-b0fa-477c86e5de3b | -1.028 | -53.727402 | 2026-09-24 00:16:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2cc92c5-563e-378d-92b6-5d1d0833ddbc | -1.6334 | -53.5788 | 2026-09-24 00:16:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2f83f5-ffeb-3e1c-9b71-c83fdfc722c9 | -1.8417 | -55.0527 | 2026-09-24 00:16:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbcf323-6537-3634-9213-25b1b935d2eb | -10.1034 | -46.010899 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bfd365e-29fd-34c5-b0c5-cc79f0b841ca | -2.9441 | -49.181999 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9c2e4f6-fd95-3392-944f-26250a98fa41 | -11.2756 | -51.344501 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4f6e59-22fc-3118-96bf-58e6ca0ef131 | -8.4608 | -48.689098 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4d980509-790b-3fe6-b495-e22cadef1971 | -8.1494 | -49.5345 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac517341-9d49-380a-a93d-5c705becec1b | -11.9514 | -50.769402 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06fd5b65-1a07-3552-ae09-03fe62383669 | -10.2063 | -44.133499 | 2026-09-24 00:16:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2e75629-36a8-30f9-9577-214d636d224d | 1.5993 | -55.9557 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d83a37b8-6eec-38ea-bc87-b0c8c3de9056 | -2.9822 | -54.264301 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1158242-4df7-38b6-8b6f-225354eece62 | -7.0699 | -52.750599 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79eeecd-6519-3174-873f-a9e960b8ae45 | 2.3498 | -50.769001 | 2026-09-24 00:16:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6af368-1501-3d05-a3f0-a8584fa93f8e | -1.825 | -55.711399 | 2026-09-24 00:16:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a765b60-f850-31d6-83f8-6f2cca45be54 | 1.5691 | -55.816502 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f54b809-a161-3a79-9e87-f3daca77f2eb | -3.5413 | -43.458302 | 2026-09-24 00:16:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5f3308e-2b78-3a70-be58-0626d5165ced | -10.2736 | -49.944099 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6d25a95-374b-3001-a6e0-a289c927da13 | -15.2284 | -43.2467 | 2026-09-24 00:16:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 9c79d2be-9a70-3b86-af8c-8468fb99d680 | 1.2744 | -50.834801 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a1d7eb4a-f96e-32f3-86f4-ac8b6f3c05c8 | -8.4634 | -51.4729 | 2026-09-24 00:16:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 654fd560-7165-3e43-a009-e890b68da7f7 | -6.4324 | -59.9478 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9289ea4-44fa-3d0d-9220-24fc8a5b415e | -10.7186 | -48.7267 | 2026-09-24 00:16:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70f0febc-b352-302a-bab0-e06747b5889c | -7.7513 | -50.049999 | 2026-09-24 00:16:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a9c402-4cf4-3ff1-b747-99fbec2de7c1 | -3.8602 | -58.874599 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abfcf2e2-e14f-341f-9877-e2f80398942d | -3.2105 | -53.399899 | 2026-09-24 00:16:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2cf2dca-98f2-36cc-a1f8-779dff28df99 | -11.2556 | -51.393799 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3fffaee-9c71-3756-89e2-5cb90662e410 | -7.5537 | -55.006401 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 388e085a-7c01-3168-830e-daed3d8b070a | -10.0863 | -46.025501 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 015e569e-1e1c-3750-a72e-70b7993b159e | -11.127 | -48.3036 | 2026-09-24 00:16:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 375610e9-c8ba-3798-bab4-8ed17cfa0e2b | -3.1551 | -50.828899 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6effc9-2ed0-33cf-9d31-a27d2763082e | -3.062 | -49.561798 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f9ad7b-5a59-3a44-a819-b977ed422dd8 | -12.6827 | -47.000999 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c855e23-dc4c-3666-848c-9ec6b1dd3295 | -11.9998 | -52.455502 | 2026-09-24 00:16:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66f91dd5-9363-39ae-af1e-99a986e82542 | -8.3474 | -45.616901 | 2026-09-24 00:16:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb7899a-27d4-3264-904c-85a60f37c883 | -6.4246 | -59.911098 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 791d210b-f3d2-33af-9149-ca25d904bfcf | -6.4421 | -59.945801 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa1d7980-f53f-3b49-9faa-dbe5e8676873 | -3.1486 | -54.594002 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01a5c5b7-a706-3ec0-99c4-ba839cf1f86f | -6.6268 | -59.9077 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43327ce5-d60f-3671-834c-fcad7c4d0a40 | -9.1876 | -49.1133 | 2026-09-24 00:16:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cad9e4e4-19a1-3ae5-80fa-ed9a8747ec56 | -5.2629 | -49.2244 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ef0191-d9a8-338c-b594-2aac7abfb08c | -3.8263 | -59.3265 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5b8f08-9191-3462-8f15-612ca3885901 | -10.454 | -44.936298 | 2026-09-24 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e167c11-6c28-300b-8842-5dbbfe189f66 | -12.0113 | -47.797901 | 2026-09-24 00:16:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75bcb908-d65d-3303-8548-cb835fa03a18 | -11.7994 | -50.966499 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 455bd64a-922f-3d44-8812-77dd2af35ddc | -8.2826 | -54.774101 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b91f8ab3-cb9e-3d02-b9a9-aa0d594f55d1 | -10.9713 | -54.075901 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d814316-00f3-39d5-a3ab-c5c240d1e32f | -1.9177 | -58.2342 | 2026-09-24 00:16:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f952b296-707d-31a4-ae79-b8a33569e10a | -12.4211 | -46.942902 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 663b7dd3-37b1-3e65-9d23-8e63504cd7e7 | -3.1601 | -54.599602 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb429e3a-3b44-3471-b283-32c027e846d4 | -12.1587 | -47.366199 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb451a8-4b2a-3215-922f-62e86a4ec457 | -4.4756 | -54.965199 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
