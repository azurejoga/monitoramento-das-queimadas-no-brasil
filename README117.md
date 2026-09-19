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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a331a1a5-0ee5-3a28-8fa4-f19359c3b8f2 | -11.4354 | -51.4563 | 2026-09-19 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 9b50c6a6-c4f6-3463-9c27-98b9059005af | -11.3604 | -44.1521 | 2026-09-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| f70d9b95-a433-33a6-9aa6-9409eba74980 | -11.3237 | -44.0639 | 2026-09-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 99e6be2a-7b8e-3bbf-81eb-8b3c53ff4a82 | -2.9157 | -57.7983 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 204.2 |
| 04060ebb-d156-3996-ac49-95f4ae21de47 | -12.2688 | -49.1907 | 2026-09-19 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| fefdad81-1233-312b-9e28-a4949c0d9f8f | -7.0448 | -42.0906 | 2026-09-19 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 192.9 |
| c7ed2e1e-9f89-31fd-b40c-3bfb11d9478e | -9.238 | -46.1894 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4908d714-e175-3c35-ba9c-8e4a515fff7d | -6.9224 | -55.0376 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5f9dd35e-b176-3b4a-a40b-7294274c7f8c | -8.7731 | -48.6868 | 2026-09-19 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 2a1e57f3-b5a9-3f7f-be22-7e13ee00a67e | -10.911 | -53.984 | 2026-09-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 52f4d586-c963-315d-ace6-df615bbb7cc4 | -8.3365 | -50.8608 | 2026-09-19 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 3131cbaa-6981-39fd-8783-c01787c01658 | -2.458 | -57.9033 | 2026-09-19 14:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c89521cb-e7d7-3e03-b8c7-75a878c55161 | -10.9301 | -53.9618 | 2026-09-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 59db8520-d738-3421-9d2d-0cbdd85388ab | -11.3813 | -44.0554 | 2026-09-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 06fc6ae2-aee7-32cb-ac49-8cc81a5c235b | -6.941 | -55.0366 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 3dc755a6-7da0-3d65-871b-9e6f677fc052 | -8.6643 | -45.3241 | 2026-09-19 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| be5ccee5-3058-3549-869f-c47b6d3ebdca | -9.6013 | -45.9003 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ee5b9ed4-766d-3ae3-8689-b18f98610f5b | -7.026 | -42.0924 | 2026-09-19 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 24f6da1d-69c1-3918-a9a2-a1bfc29aa579 | -11.234 | -48.3571 | 2026-09-19 14:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| cf6f008c-4fd4-3d6c-8017-8393506150f2 | -4.5772 | -42.9746 | 2026-09-19 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 59a18370-1d4d-3308-9ebd-10e4eb6023ee | -10.8732 | -53.9874 | 2026-09-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| c3bd75b9-0925-3faa-8cd4-5545ce8286fe | -8.4296 | -54.7262 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 63f5f5aa-3170-34ca-881e-a4b935dbd96a | -10.8921 | -53.9857 | 2026-09-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f232cb8f-517a-311a-91e3-e5ef6030bd24 | -8.7734 | -48.6651 | 2026-09-19 14:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 13d3c8da-71d1-3cb0-9935-fe3734d6580a | -11.8549 | -50.0437 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 9df3fb3f-5caa-34e3-b7c4-4ac516ffd83b | -11.8934 | -47.6322 | 2026-09-19 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 90bbea78-ca2b-38a4-8051-7f10f260226b | -11.9115 | -50.0801 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 429b8fbb-9948-3d8e-addb-6b9344e9ec9a | -11.0223 | -54.1379 | 2026-09-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0ed4379e-6764-31e9-a7e0-53ce9cb0893f | -8.5986 | -44.5762 | 2026-09-19 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 46911612-9153-3cb9-b4d8-73aa49bca409 | -12.2879 | -49.1883 | 2026-09-19 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| c38594f6-fa31-381b-8280-58b43514de40 | -10.6703 | -50.6465 | 2026-09-19 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6eacf86f-fc41-3a76-9f54-74035f22840b | -13.0173 | -46.9352 | 2026-09-19 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 410cbed4-db34-3ef3-b732-8cef3e6510ce | -10.7991 | -50.9093 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a53fc2db-06db-3fb1-9eee-f25ae0a3a50d | -10.7736 | -46.1643 | 2026-09-19 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| c7762199-28a2-356b-9f6e-73685d454e6c | -11.7823 | -49.8152 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 8e811f29-1447-3bc0-88d9-df0845a256a6 | -7.7847 | -44.8441 | 2026-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 76277b82-5703-38d7-8613-ffdc6e9fb2ac | -10.5667 | -51.3349 | 2026-09-19 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b9179040-da9b-395d-8096-648dd786cf7c | -12.2883 | -49.1664 | 2026-09-19 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 45c42f08-5c63-3705-8976-7465b75cfb5d | -11.318 | -51.7218 | 2026-09-19 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| dce2224a-3400-30e0-921e-65e1a93bbcf0 | -2.8791 | -57.799 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6838636b-668c-32e4-80e1-46ac2628e275 | -9.2414 | -45.9411 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| fc42b652-46aa-3a46-80b7-542fe0eb76fb | -13.892 | -48.592 | 2026-09-19 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9d683b70-877b-3330-a550-96aebb95c8d5 | -4.5585 | -42.9758 | 2026-09-19 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dc79cecb-7f7c-36e3-a60c-922083e1daf9 | -11.9493 | -50.0971 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 50e59460-8ae6-35ff-8e37-17fb5c02470c | -12.5761 | -49.1071 | 2026-09-19 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 195.9 |
| fee7b9d2-7618-3bf7-aa08-3a35b1f649b0 | -7.7118 | -44.6451 | 2026-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 6527de9f-4909-3890-b3c3-e03e6697a1d8 | -12.1471 | -50.8668 | 2026-09-19 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| eb883688-09b4-3508-8684-d313d291f309 | -10.932 | -50.8742 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 160a1230-1053-3941-a5a5-2d54e7717cc4 | -3.9902 | -41.2759 | 2026-09-19 14:40:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 168.0 |
| 38cc4b92-d6ec-318e-861e-bdd3e70a57c3 | -10.567 | -51.3137 | 2026-09-19 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 441249d9-3a5c-33a8-9a82-9e844f2851d5 | -11.6796 | -54.4665 | 2026-09-19 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c784440b-c8ae-30e4-9ba3-257e18d1bad1 | -9.6202 | -45.8981 | 2026-09-19 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 377.2 |
| fe0686d6-ffd0-3b0a-8314-dcf67243e39d | -8.45 | -45.8674 | 2026-09-19 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 439c5222-3624-3be5-91fb-42649233f5d1 | -11.318 | -51.7218 | 2026-09-19 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| b4614c23-ef37-36d0-9640-ba7814a08fd5 | -11.0608 | -49.7909 | 2026-09-19 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 69a3ddc9-aa63-3708-8d0a-2f51f519a3e4 | -11.0611 | -49.7693 | 2026-09-19 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 32fca05f-44fc-38e5-8851-91825e0286e5 | -6.2585 | -41.6617 | 2026-09-19 14:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| e665fd1a-a39c-3ff6-9d84-df11a9f7e09c | -6.9224 | -55.0376 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7cbc5802-736d-3499-a84e-25a5b805a9a9 | -11.8937 | -47.6099 | 2026-09-19 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c0ee3303-b49e-31dc-b172-4720c7413320 | -11.234 | -48.3571 | 2026-09-19 14:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| aa9117e8-9c87-3cdc-899e-3491dc8cbaa2 | -2.458 | -57.9033 | 2026-09-19 14:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c895e275-d446-322c-b691-1d7f6fc73966 | -10.1145 | -48.4205 | 2026-09-19 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b1b5a29e-8ac6-3c42-8242-11d84e505584 | -6.3319 | -45.6062 | 2026-09-19 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 2b90211f-50f2-3d41-b524-c32d188cacfd | -10.8921 | -53.9857 | 2026-09-19 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5a706e90-5492-376a-93e6-39c02dda3343 | -7.8595 | -44.8824 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 990e9e1e-4363-33e5-a3f7-b6d903878a63 | -8.411 | -54.7274 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 1063396f-5943-3318-81bf-a218c32e8516 | -11.3813 | -44.0554 | 2026-09-19 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 3fa60c7c-14dd-3b0a-8a6f-ee0d0377cd41 | -8.6628 | -45.4379 | 2026-09-19 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 72be466a-58b4-340a-a525-72e9c83d62af | -6.2034 | -45.3453 | 2026-09-19 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5bd05198-28ab-3960-95e4-9582de994dd0 | -10.6703 | -50.6465 | 2026-09-19 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 3ba2f93a-964d-3d7b-ab0c-ece0e89af589 | -9.0355 | -48.7487 | 2026-09-19 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 123.3 |
| e64cdc04-66a5-321c-903b-3042ef2da3c6 | -7.0448 | -42.0906 | 2026-09-19 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 172.5 |
| 7d35e9de-2bae-34cd-bec4-60bc09a5bbf6 | -11.299 | -51.7238 | 2026-09-19 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 69539040-c5dd-3bbb-b388-b1e119c0807d | -7.6572 | -46.1237 | 2026-09-19 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 1a61146a-4a8b-30a1-af4d-6e39195ef68f | -11.7823 | -49.8152 | 2026-09-19 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 789c6ab1-d3ca-3f03-883d-456b173c69f5 | -9.6087 | -45.3772 | 2026-09-19 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6f3a9421-5768-3cdc-813e-4e9eba58d5e0 | -7.5703 | -57.6962 | 2026-09-19 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8fb8a044-0628-394e-aea6-8633258dc2d5 | -1.2357 | -55.73 | 2026-09-19 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3a7ec6ed-6723-3ff0-b2ad-e07a508e9d10 | -10.913 | -50.8762 | 2026-09-19 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| c8b4f53a-9e67-3580-bfa6-34c65b3d25d4 | -11.8746 | -47.6125 | 2026-09-19 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| f476441a-c481-31a8-b4f5-8fd507f30429 | -13.884 | -47.9929 | 2026-09-19 14:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 4c5ac680-2084-3a03-a6ed-6ef4c1ed0851 | -12.2883 | -49.1664 | 2026-09-19 14:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6cad2bdd-fc24-3fd0-90e6-5aa49c90bc24 | -6.2582 | -41.6858 | 2026-09-19 14:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| ae1abb01-e5f8-37cb-8a77-55a3c6b16bab | -1.254 | -55.7496 | 2026-09-19 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d976b463-7fb7-3794-9a88-a728cc821358 | -13.68 | -48.5792 | 2026-09-19 14:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d6e4f468-79c0-3062-84c7-15146b558558 | -8.4737 | -47.0053 | 2026-09-19 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| bb8db1fd-df51-3bc0-a350-cdacbec5d940 | -12.2692 | -49.1689 | 2026-09-19 14:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 520e1c2c-c78f-3674-ac19-29c8ce237d4b | -6.166 | -43.374 | 2026-09-19 14:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 13851812-36ba-38a1-ad53-91c2c0b19f14 | -3.3183 | -57.8677 | 2026-09-19 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 887fae4c-c690-39ab-8f8b-0b84051250f5 | -8.6171 | -54.6126 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 813a74d9-f209-31dd-bc77-3ae780bb1049 | -3.7536 | -40.1942 | 2026-09-19 14:50:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 06331718-4b6c-39d8-af03-d030e30e94dc | -7.7626 | -46.7612 | 2026-09-19 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 345.9 |
| fe18d7c9-fe64-3df5-a89f-2d15d7f13d91 | -8.7919 | -48.6851 | 2026-09-19 14:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 273.5 |
| 2a2036d7-beba-3e31-a428-d5a962d18c6c | -7.7847 | -44.8441 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.8 |
| d6db2b88-38f9-3612-b3d6-c6932516f1ae | -10.5667 | -51.3349 | 2026-09-19 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f4c2e28d-cb1e-375d-b9a3-ff2b5e33fd84 | -3.4462 | -57.9812 | 2026-09-19 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 35126ad9-1047-304b-926a-569f01f5c13d | -8.4797 | -57.6282 | 2026-09-19 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| acc9fc66-fa10-3cf4-b6d4-60bc8e368e7a | -10.7736 | -46.1643 | 2026-09-19 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| c10bfb4f-402b-378c-9ddf-fae23948664c | -8.4314 | -45.8467 | 2026-09-19 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| f8b11319-f3c7-38d6-b913-04a43bb8f5d2 | -9.6013 | -45.9003 | 2026-09-19 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 431.6 |


[Clique aqui para ver as próximas entradas](README118.md)
