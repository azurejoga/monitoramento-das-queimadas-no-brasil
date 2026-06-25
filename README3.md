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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d48ce82-5b15-31d6-9a69-319d01b44c30 | -9.9808 | -47.736198 | 2026-06-25 00:23:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 259ffe5c-a31a-3338-8407-69de16457802 | -9.19 | -45.3283 | 2026-06-25 00:23:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f86ee517-c454-3e09-ac70-3a7997ad69e5 | -5.821 | -43.590698 | 2026-06-25 00:23:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b77b7c87-52ec-3876-aa61-3c3c52f8b90a | -12.3174 | -46.742599 | 2026-06-25 00:23:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2429913c-5bc2-3e48-b32b-bb0390263d4c | -6.7639 | -46.301701 | 2026-06-25 00:23:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd5f8bdf-9c00-3831-8dae-1cf634723c74 | -11.2558 | -43.333599 | 2026-06-25 00:23:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d8893e2d-0b71-3fe9-aed4-614bde1299db | -9.5805 | -49.125099 | 2026-06-25 00:23:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e7761e8-5ab8-3bee-a92c-e7d78c25cb82 | -7.7381 | -44.178398 | 2026-06-25 00:23:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 645f13b4-0259-36ed-a34b-ac45166340fb | -6.9928 | -42.900799 | 2026-06-25 00:23:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9114a8eb-947c-3325-9e7e-7b66b6af041d | -11.19787 | -49.41713 | 2026-06-25 00:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7cf52656-f9e8-3a01-9af1-f55b9b8c2436 | -6.76788 | -46.3189 | 2026-06-25 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 8c304e16-b543-33b7-8380-3c46e0090434 | -9.57726 | -49.1258 | 2026-06-25 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f987551e-317f-31ad-973c-4171775ecdbb | -9.98892 | -47.73812 | 2026-06-25 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| fa1e8985-d18d-325a-87d2-a6f2789e620d | -7.7573 | -44.63936 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1d87d8a8-a32c-3d53-a91d-39552fab879d | -7.75262 | -44.61072 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6bdb8029-3891-3a57-aff2-952e3c08a226 | -6.75468 | -46.32077 | 2026-06-25 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 0e772a24-ab47-3eb3-ac98-9a5184d8c423 | -5.81205 | -43.58294 | 2026-06-25 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8804ad5e-b3af-3038-b589-afb5c0d9f7e7 | -6.9912 | -42.87778 | 2026-06-25 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 6320321f-b63c-3b40-a2dc-c2018644d82a | -10.59496 | -47.11722 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 16d79a05-a8c8-3f0f-b98a-aad73dcf66d6 | -9.19672 | -45.32431 | 2026-06-25 00:24:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 08632085-5a8b-33b6-a9d8-1c1738b46eaa | -10.77592 | -54.11292 | 2026-06-25 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f6221e77-bca1-3ba0-90a1-332412f0b2d7 | -11.63802 | -52.8619 | 2026-06-25 00:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d565971d-26e1-3f52-859e-9b552b12483d | -6.76461 | -46.29771 | 2026-06-25 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e97598e4-9a42-39cf-ad97-8e4d5e3b64e6 | -6.75138 | -46.29962 | 2026-06-25 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| bcdc8f3d-6c9e-3102-844d-ca28893c6221 | -11.31965 | -51.41618 | 2026-06-25 00:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3dc8ecb9-4f73-3aa8-b342-6232e640f6ec | -11.58086 | -54.71378 | 2026-06-25 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e4dcc174-bd74-301c-b2ab-9aff1811c292 | -10.93751 | -56.85949 | 2026-06-25 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 58fb352b-9f3b-3f69-8ae0-7a5877172f41 | -8.12346 | -47.88791 | 2026-06-25 00:24:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 411275cf-5c9d-3a75-85ad-333f89552776 | -9.53038 | -47.7579 | 2026-06-25 00:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d1dfb3ad-d591-31bf-98c9-cbfe1221ef6e | -9.18311 | -45.32668 | 2026-06-25 00:24:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 483a0249-c8e5-3020-87b7-6bb85a484807 | -10.16387 | -56.62466 | 2026-06-25 00:24:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| aa715949-0223-3bcf-aa65-383a02778124 | -9.36217 | -50.54001 | 2026-06-25 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd606cb1-549b-329c-8198-8f68922bc455 | -11.51346 | -56.12206 | 2026-06-25 00:24:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 45ffee21-8550-38a7-8a8e-d0049d0081d2 | -6.99498 | -42.92419 | 2026-06-25 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 5e43ec74-a0ef-3b39-8e27-2523c61b4427 | -11.50449 | -54.49846 | 2026-06-25 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f8585b63-8daa-308e-a1fd-0f0c35498445 | -11.50583 | -54.50889 | 2026-06-25 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b778c23-d12b-391e-8bd5-484b5eed27ff | -10.61373 | -47.16275 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5292727d-0326-3398-a759-906db1dc7a1f | -5.80821 | -45.05972 | 2026-06-25 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 3129bea2-3dc8-3fb2-9b2f-5b346b4186e8 | -9.62182 | -49.01542 | 2026-06-25 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8cf6dc43-b51b-3f89-80f9-fdc98d95ff28 | -10.16358 | -54.89509 | 2026-06-25 00:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0383bfd5-9b0d-3a70-af11-87830927adcc | -9.5755 | -49.11399 | 2026-06-25 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8692659-a576-304c-9705-e7805dd9ce9b | -9.464 | -49.82801 | 2026-06-25 00:24:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 99ef297c-793e-38f6-a102-df1fd9e8398d | -7.73782 | -44.6132 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c71be983-a290-3ca4-9e2f-945db29d43ba | -9.37146 | -50.53863 | 2026-06-25 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fe2f97c2-8fdc-336c-80e6-1e33ba0d1fc7 | -9.98848 | -47.74458 | 2026-06-25 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 33431fc0-da68-3c8f-877d-61bc349a1e71 | -6.98872 | -42.88543 | 2026-06-25 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| b134326d-1bd4-337c-8393-5ee77992a73d | -8.68252 | -47.85645 | 2026-06-25 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| e85c6630-56ba-36e9-a409-84be69433f76 | -11.50003 | -52.92459 | 2026-06-25 00:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d435fdd3-8f87-34fb-99de-2670488d2f0f | -11.49111 | -52.92586 | 2026-06-25 00:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4af36d16-99db-37e1-9f1d-816904cd88a3 | -9.45435 | -49.82951 | 2026-06-25 00:24:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 13748961-bfd2-3ae0-b789-67ff7495c0b4 | -10.1263 | -52.10804 | 2026-06-25 00:24:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f482e859-6a48-345f-b145-b677e76cace3 | -10.61608 | -47.17808 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 38186c7b-c230-3638-954e-bb225d63fb85 | -10.59982 | -47.14875 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| bf0d5f7e-987f-35a3-850a-4d06c100e11e | -9.58734 | -49.12424 | 2026-06-25 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 81a01956-edb7-3b90-b9eb-d50b37a0d963 | -7.74251 | -44.64171 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| adbd9fea-b0fe-3cc4-bfb1-e3625247f5f8 | -10.36003 | -50.12133 | 2026-06-25 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 94d9b434-85ef-39cd-bd5d-5cc69ff9aa6c | -11.30538 | -54.71512 | 2026-06-25 00:24:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5594aafb-a595-3283-8028-8cb33a59ae70 | -10.59744 | -47.13327 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b3065a5b-b21d-3d3f-a216-dd6cbc91fee7 | -10.58343 | -47.11892 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 59bcd547-fa4f-3a49-b7ec-3855056e664e | -6.99774 | -42.91666 | 2026-06-25 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 507637c6-bebc-3d1f-a145-446359fff463 | -5.80866 | -45.06518 | 2026-06-25 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| bcc8632e-aacf-3370-bf67-896a83f5288a | -10.12753 | -52.11698 | 2026-06-25 00:24:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 22269112-25b3-3de5-879c-21436d24107c | -10.35854 | -50.11117 | 2026-06-25 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 028ce358-c104-3f66-912c-745921a2fdf8 | -7.7384 | -44.61885 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 56141d08-006c-3787-9d69-66954151bafa | -10.60222 | -47.16429 | 2026-06-25 00:24:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 300a73b1-9718-3e8a-bcd0-2d5768a562ab | -10.37719 | -47.34491 | 2026-06-25 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 04c1a50c-02b6-33eb-a654-af859737de77 | -9.21031 | -45.32174 | 2026-06-25 00:24:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bc94a998-4ded-3b10-9bef-0956ec16c13c | -8.68474 | -47.87122 | 2026-06-25 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 594d7103-37c5-32df-9519-0ebb532adbb1 | -11.91107 | -56.86415 | 2026-06-25 00:24:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 03a3c12d-0f17-3151-8bae-d54262501590 | -9.88722 | -52.44318 | 2026-06-25 00:24:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4d5b045-22c2-3de9-8724-4ddfbfacaed9 | -10.37535 | -47.33962 | 2026-06-25 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f5e15a6c-9ec1-3765-9e0f-c0fa4bf3ce8b | -10.36584 | -47.34679 | 2026-06-25 00:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| db9aefe7-e045-3c76-a46b-d0c4f93aa121 | -7.75322 | -44.61651 | 2026-06-25 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1a1e0dbf-f35c-3cae-bfaf-9fcef6c72246 | -7.63765 | -50.21448 | 2026-06-25 00:24:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8d43fdaa-3388-3c5f-834d-ccec55f50ca4 | -6.97415 | -42.8808 | 2026-06-25 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 02fe5947-496f-3df0-9579-edb5c9877cf2 | -5.82335 | -43.58817 | 2026-06-25 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4890d0af-a673-3205-83f4-7d92c347aac5 | -10.43083 | -46.72961 | 2026-06-25 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0333d6ff-eba3-311e-8fa0-b438673c3bf8 | -7.628 | -50.21593 | 2026-06-25 00:24:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9e669d0d-b392-3849-a6f3-c8b7ecd3f88f | -12.7562 | -44.4724 | 2026-06-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c0a87e2e-71a7-3270-89c8-a81e30e3bf30 | -12.2158 | -55.5171 | 2026-06-25 00:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5bca49b0-bb35-3571-9b55-6b7d8ee06015 | -13.0635 | -53.3546 | 2026-06-25 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2363a846-3d7e-3857-8fb8-3e0ce5eebdec | -12.216 | -55.4968 | 2026-06-25 00:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| f5334e7c-9085-3e01-a524-016063c29e76 | -17.3449 | -42.6084 | 2026-06-25 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 8f2497cc-4a71-3ed3-814a-eba12fb35c47 | -17.3442 | -42.6333 | 2026-06-25 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ce8e93c9-043e-347e-a98f-ff69f12f1ac9 | -6.9791 | -42.9034 | 2026-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 063ac3e8-f27c-3902-9ae5-c5ee90426ab7 | -12.7373 | -44.4521 | 2026-06-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| ba9f8238-b046-39b4-b1c6-a4b868988822 | -12.235 | -55.495 | 2026-06-25 00:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 954ecf16-9c56-3318-abcc-a85066c35173 | -6.9793 | -42.8798 | 2026-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 9aac496e-9fd4-385f-af2b-751c658d6cb5 | -8.6889 | -47.8664 | 2026-06-25 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c5530dff-b283-31e5-8884-68f94f532461 | -6.9979 | -42.9016 | 2026-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 7b9f58df-5f45-3ba9-bfef-7574529ed31b | -12.7369 | -44.4756 | 2026-06-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8b61d9ed-f3ba-37d6-99d4-088b895f5d6f | -8.6892 | -47.8445 | 2026-06-25 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3fd7f496-d9c0-3e1b-a986-190fa2e5bf59 | -7.7498 | -44.6184 | 2026-06-25 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 10e51c0e-ebb8-3b99-9b55-6e125e8f2346 | -6.9982 | -42.878 | 2026-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| a90b0d32-54a5-32a3-af77-bee01bfaf84a | -12.7566 | -44.449 | 2026-06-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 166cd4b9-8326-3ada-ab55-d703af00c74f | -12.2348 | -55.5153 | 2026-06-25 00:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a6bbe931-1df3-3e69-a53d-e36a958c9cb5 | -12.2158 | -55.5171 | 2026-06-25 00:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 1e1125ae-9ff0-317e-9be5-012dcab038bc | -12.235 | -55.495 | 2026-06-25 00:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| f2d6959d-ebd4-3db7-a7c9-d71d1c1febb7 | -17.3643 | -42.6284 | 2026-06-25 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d52a0b37-f8ca-3a0a-bcf8-9cb52c47b7ac | -6.9791 | -42.9034 | 2026-06-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |


[Clique aqui para ver as próximas entradas](README4.md)
