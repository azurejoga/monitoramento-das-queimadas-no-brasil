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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11a23930-1d5c-3a93-aa71-33c70b90117f | -6.5845 | -43.907101 | 2026-06-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0eadca58-aefa-350c-a7a3-15cfef651796 | -11.2834 | -55.775002 | 2026-06-24 00:16:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62264a41-d39d-375b-b9a0-24d533311829 | -13.0724 | -53.352901 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfeea4e3-1417-30b5-96ec-4ff15104b062 | -12.7847 | -44.444199 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 682df2a2-5d4e-3840-a08a-ba9e7c043cb5 | -7.2924 | -46.2281 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e12daea-ddd6-3696-beb7-0ee1df2dda02 | -8.2633 | -49.351002 | 2026-06-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f8ce24-f191-3f90-8ae0-439b0e523a82 | -12.7797 | -44.423801 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9d8c5b9-a9da-3e55-b9e5-4aff1e5a4579 | -5.8148 | -45.0378 | 2026-06-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d25b8de-5ee5-3112-ad77-04d3e5595e98 | -12.5121 | -48.258499 | 2026-06-24 00:16:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9214da0e-5b65-3685-9ad3-9fe8762840bd | -6.578 | -43.879902 | 2026-06-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb5e2fe-26ac-36c5-baad-cda6fb2b0a46 | -9.9474 | -49.2742 | 2026-06-24 00:16:00 | METOP-B | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9894676-8b96-3227-8639-04423e835796 | -5.8176 | -45.049599 | 2026-06-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80c9dd08-7e89-394f-8c3b-1b42c5584585 | -13.0685 | -53.334 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 601d1eba-1b1a-391b-9d82-cad3b1f77ccc | -11.4772 | -46.7244 | 2026-06-24 00:16:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd0fa939-0f3a-38c6-a222-b688a8a18cdb | -7.5948 | -46.460201 | 2026-06-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c11f045b-0e81-3d1f-96a5-29cc10f117d3 | -10.7023 | -49.605 | 2026-06-24 00:16:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80de99b9-2e62-3bda-a55d-70c40e3bed28 | -11.6256 | -48.487999 | 2026-06-24 00:16:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4883f843-0575-3d08-98e2-23717bc2e868 | -5.7284 | -49.090599 | 2026-06-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e636fe1-5383-3f58-865f-d0f8f4ce4fa7 | -9.2155 | -47.922901 | 2026-06-24 00:16:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c44fec1-b9e6-306d-8a67-14ca21666e9d | -10.3561 | -50.0839 | 2026-06-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7b812f7-6a2e-3439-8cc1-c6c578015e23 | -8.6919 | -47.845001 | 2026-06-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48269116-7f91-3988-ab7a-4742f8857a97 | -3.9479 | -43.113499 | 2026-06-24 00:16:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46032b2c-c163-3020-9da8-93276a881167 | -6.8392 | -47.865799 | 2026-06-24 00:16:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef2ec9e-db7d-3bd2-a938-20cc2ccab3d0 | -12.7271 | -49.074699 | 2026-06-24 00:16:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c48b4fab-6c0c-37f8-8050-5a94d60b5b05 | -9.4099 | -50.690701 | 2026-06-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78db5304-b166-3f55-b3db-e2506da43e6c | -11.9093 | -44.160999 | 2026-06-24 00:16:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49139f73-603c-305c-a6c7-730e8d10dfb7 | -12.77 | -44.426201 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfba159a-4533-3031-bc6b-191ee4d9bcdc | -11.5524 | -48.257301 | 2026-06-24 00:16:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59b573b1-d487-34bd-b827-675ad7228949 | -12.197 | -47.962002 | 2026-06-24 00:16:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0549da0a-0547-3934-9244-67499984b4de | -7.366 | -47.025299 | 2026-06-24 00:16:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 399bb761-bd36-31d0-920b-6920759bae1e | -8.1319 | -47.878399 | 2026-06-24 00:16:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d44e7ac9-1c31-396a-9737-472d8ff928aa | -9.439 | -48.852299 | 2026-06-24 00:16:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b6bdfc0-1a66-3793-acbd-774c4c4f749b | -7.5969 | -46.469299 | 2026-06-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58129a34-33c3-3d78-ad32-ac37d71864b5 | -13.0704 | -53.343399 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7646d246-f1b0-3cff-ae51-f17a85960229 | -11.229 | -43.325901 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e69b8499-f8a8-3498-acbc-17ee41ca8a02 | -8.3095 | -45.381901 | 2026-06-24 00:16:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3f982f-1be7-3d21-9ff2-5470cf455cee | -11.5508 | -48.250099 | 2026-06-24 00:16:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a856b2f7-4a3d-3512-b981-c1b5879ad67c | -7.7988 | -46.450401 | 2026-06-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca8236f-707e-3a4b-8702-faf76bd6ecf9 | -17.7635 | -39.9967 | 2026-06-24 00:16:00 | METOP-B | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fde18504-0081-34ce-8028-c5ae94992b35 | -5.8051 | -45.0401 | 2026-06-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d999930-6b2b-3519-8e0c-ca2dc01a8fee | -12.775 | -44.446701 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d99df60-d05c-3b97-a981-44baa222fe3a | -8.6838 | -47.855 | 2026-06-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4e792c8-3e27-30af-808d-24b89742c006 | -13.0587 | -53.336102 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74dfc526-8e87-3d8c-be57-2bca8e484e0d | -17.2498 | -46.312401 | 2026-06-24 00:16:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53f75b16-f94b-30ef-a32c-88a15a4a1d97 | -4.0469 | -49.765499 | 2026-06-24 00:16:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4f51591-522e-3c5e-89d1-bc2ba4e0328e | -6.8374 | -47.857899 | 2026-06-24 00:16:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9048b51b-9a44-3ec6-b59c-3265f6abc63f | -9.4083 | -50.6838 | 2026-06-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d42991f-191f-3116-84a7-bf53772b3d7f | -7.9167 | -48.287201 | 2026-06-24 00:16:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9679c9-7c6a-325a-9e64-3cc247d3ceaa | -6.591 | -43.891201 | 2026-06-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc733704-9dd1-3a20-b900-94aa20781be8 | -6.8447 | -47.8894 | 2026-06-24 00:16:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc0093e7-32a6-30a8-afa5-43363fe19200 | -6.2589 | -49.879002 | 2026-06-24 00:16:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f8182b6-81ad-3dcc-9fe6-e634de60be43 | -6.364 | -43.5905 | 2026-06-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4e098f-9303-3bee-9a53-5de200cf1093 | -10.8061 | -48.5588 | 2026-06-24 00:16:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 342d3d94-5c23-36ad-8159-857c5dd4bd16 | -4.3494 | -47.758598 | 2026-06-24 00:16:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1ce0d0-31c4-34fe-b234-73441f16cdcd | -9.5799 | -49.108799 | 2026-06-24 00:16:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28fc046b-4fd8-34c1-a6fd-43e314cb2830 | -11.487 | -46.722099 | 2026-06-24 00:16:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5de0f989-461e-3702-9b97-3599d3147422 | -5.7268 | -49.083302 | 2026-06-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d15502b-a9a9-327b-8261-96b1a1d7d02f | -10.1072 | -47.538101 | 2026-06-24 00:16:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 083a389b-b4c9-3e29-8ac7-88b69a3312d3 | -6.3543 | -43.5928 | 2026-06-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1637ed8d-4c5f-379d-ad63-96d393e54626 | -6.9881 | -42.897598 | 2026-06-24 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ceaea0d-8918-3ba1-ba91-5e7ae68330a8 | -3.9576 | -43.111198 | 2026-06-24 00:16:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4822e0e9-99ff-3dd1-9cfc-6d8cedf9d297 | -10.7721 | -54.091801 | 2026-06-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfabf2b4-dc00-35a8-ba30-36455a150f6b | -13.0802 | -53.3414 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2396114-3dca-3033-bfe9-3d150944a07f | -12.0619 | -45.5676 | 2026-06-24 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98916889-78e5-306c-a7f6-e4623568bf1b | -12.7725 | -44.436501 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47f434b4-3b89-301d-803f-ca050614c1d4 | -12.8672 | -44.358101 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11c52840-67d5-32e0-8f8c-0c459e0208ec | -12.833 | -44.344898 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20b3c327-712c-3ca6-99f0-af9a91cd80d3 | -9.4422 | -48.866402 | 2026-06-24 00:16:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5935278-d262-3862-8dd1-f3208c008b63 | -11.2321 | -43.338501 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1f4b42a7-9d97-3da8-a8c1-ab389d544959 | -12.8355 | -44.355202 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da8ec543-10e0-3b0c-82f1-a06a0fccb0d9 | -6.3605 | -43.576099 | 2026-06-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8f1ca31-d6b7-3bf5-945b-6ac733d04999 | -8.6002 | -45.997299 | 2026-06-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 175f92db-d970-36a4-aec3-084fe8e8b46b | -9.2147 | -45.325199 | 2026-06-24 00:16:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b194932b-ef53-3025-a22e-54b13bbc1756 | -11.624 | -48.4809 | 2026-06-24 00:16:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67153fe3-82fe-34cb-a82f-f3bac52ac94a | -6.2574 | -49.872002 | 2026-06-24 00:16:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23ab145-99b3-3f13-a166-a756c92b2696 | -12.0641 | -45.576599 | 2026-06-24 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3ecd796-9771-37a8-9d89-93784b313785 | -11.5426 | -48.259602 | 2026-06-24 00:16:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 052dfebb-4b73-3759-84a9-be9c431b2897 | -5.8079 | -45.051899 | 2026-06-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33a9d889-3b56-30c0-9473-a5a1c4f18501 | -12.8453 | -44.352798 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6cfa36c-f880-32fd-94b4-a977b8943af9 | -17.7775 | -40.010201 | 2026-06-24 00:16:00 | METOP-B | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec0465d4-f48b-3542-a6c2-a2ca3ea96322 | -6.5812 | -43.893501 | 2026-06-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53d61cb5-42a5-3971-bc50-4beb33d2ff44 | -8.6055 | -45.976101 | 2026-06-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 505d54c6-8805-3534-9910-7c3aca1e9f25 | -9.7502 | -47.869301 | 2026-06-24 00:16:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70982348-0893-3159-bb01-fbfd46f6dcb5 | -9.4642 | -49.828499 | 2026-06-24 00:16:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f52138c9-b5b8-3d48-b615-16c88e6330c0 | -6.9843 | -42.881901 | 2026-06-24 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 935212ce-2595-3899-9bcc-d86373a7b3c0 | -11.4911 | -46.695499 | 2026-06-24 00:16:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f68482d-4e12-3754-b8a1-a4a426e5ee8a | -3.8582 | -42.9529 | 2026-06-24 00:16:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc44a61-4b53-3e92-b692-46c980183108 | -7.9265 | -48.285 | 2026-06-24 00:16:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88fd2dc1-1e8c-31b8-bdac-00fd072f8a21 | -17.767799 | -40.013 | 2026-06-24 00:16:00 | METOP-B | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e697931-d7c9-3b98-8b30-8744bb61dc93 | -8.8834 | -48.497799 | 2026-06-24 00:16:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbfcfc2a-1d76-3c05-8b1b-1c6a71df81f5 | -12.8232 | -44.347401 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 768290f0-7d60-3bb2-ad32-ca10752beb32 | -7.2969 | -46.247002 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2708820b-ef2b-3a3d-8df6-43ec40be9875 | -12.7764 | -44.4223 | 2026-06-24 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 67840d1b-b519-3bfa-8cbd-71bb951aecea | -13.0827 | -53.3524 | 2026-06-24 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 30b55168-5550-307a-a353-d2c182a9add2 | -11.2407 | -43.3464 | 2026-06-24 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 27136895-33ad-3f6f-a1e7-4d9cb8624a51 | -13.0635 | -53.3546 | 2026-06-24 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| cfd8568a-8850-3705-aaae-6121667fba66 | -11.2599 | -43.3434 | 2026-06-24 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 11d26719-aa26-3267-a4f3-0456f850b093 | -12.7953 | -44.4426 | 2026-06-24 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4cc3314c-b67d-3b97-b1d4-b2f7bbf3f304 | -6.5924 | -43.8957 | 2026-06-24 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7e061555-7e47-3074-b777-7e094226ca21 | -6.3703 | -43.5898 | 2026-06-24 00:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |


[Clique aqui para ver as próximas entradas](README3.md)
