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
| b46ce3e9-8a1e-3cbe-994a-2d7a145acb6e | -7.95021 | -43.90642 | 2025-08-04 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55801afc-c15b-3123-bd47-231a05652b17 | -6.61435 | -59.95938 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79877ca9-5169-3c6d-9328-0e41f60dfbeb | -7.64367 | -45.29637 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae074972-94a6-3a58-b56f-19aaaa5bb780 | -7.96835 | -45.10281 | 2025-08-04 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eab9fb81-3872-390b-bf0f-0d30934f3425 | -8.01637 | -43.17053 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a5fb9444-4004-3d09-9fe9-698ffb87d683 | -11.22594 | -48.43983 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d9e7b65-f9b4-3d5b-ac8d-58a73951aec0 | -8.51716 | -44.74653 | 2025-08-04 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07c0933f-0fb6-3415-a7e0-d6fbf1a540a1 | -6.62686 | -59.96153 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2dceef2-27f5-356d-9c42-a779adc23838 | -6.15583 | -57.91852 | 2025-08-04 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d727374-8a92-37f3-a6ed-80ff12fc3896 | -7.54398 | -44.87542 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9f62c49-0f9c-3243-b8f2-e3c023117089 | -8.26831 | -47.37626 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 673e367d-a2f7-3600-80af-aca982dfcc4d | -8.55311 | -47.46149 | 2025-08-04 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3d443dd-03f4-31af-83c7-8425cc5cb378 | -6.67671 | -59.16601 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6a943b-8b71-3e99-a1df-14fb16014815 | -8.51202 | -44.7419 | 2025-08-04 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f716af43-13c3-3542-b12b-1493b9e00842 | -7.02342 | -59.82904 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 386df5cc-bc8d-3040-8e3b-07c80cf8730c | -11.22195 | -51.53223 | 2025-08-04 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4e9d28d-6218-3fc6-8276-e3b33a184252 | -8.73388 | -46.41503 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a040532-0e64-3286-bd2f-f4d25c5c68a9 | -7.02279 | -59.83276 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0f232c5-6f9a-37f2-ac85-4d18a2717627 | -8.38603 | -46.94557 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f1b29fb-4e61-3779-b636-892932401616 | -11.41302 | -56.86337 | 2025-08-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f87b349b-e316-3d99-bbf6-fb46150a4ff1 | -12.69385 | -48.08422 | 2025-08-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73070d6a-8e92-33b0-8c54-944162ee69b8 | -7.51619 | -61.3246 | 2025-08-04 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e550c10-fa5b-3647-8f13-85b5e3682926 | -7.78318 | -45.22076 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d8f6185-ddf2-3b4f-89eb-6572824743a3 | -10.22802 | -54.26795 | 2025-08-04 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d90b1d8-0f99-395e-aff5-d6fe8decf3c9 | -8.73428 | -46.41208 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14fb971e-60e0-3b26-a5b9-12a0518aaba7 | -7.01742 | -59.8395 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fcfc81b-c5f1-365f-8bb6-84f0786e74d5 | -8.73857 | -46.41869 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f68fa4a-36c4-3886-9b65-35d0463ad578 | -6.64934 | -45.89226 | 2025-08-04 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c96e62e-7335-349c-9e4c-a802ef0b544c | -6.64784 | -45.88688 | 2025-08-04 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42cd133e-5ec4-342e-82ef-12ad74e08cff | -6.62079 | -59.97225 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23eac6b4-e157-3719-adb5-ae48f0769f95 | -7.44026 | -48.93579 | 2025-08-04 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed20209-43b0-300e-acbe-90d7ea2f4777 | -8.26899 | -47.37127 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2328645f-f2db-3c63-9305-577ed96eeaf2 | -7.19705 | -44.49088 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e47b204a-a4fd-3787-9d52-f740085152d3 | -8.03644 | -43.11387 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 35670580-3a55-3b27-a0a6-747d8e40c5b8 | -12.70153 | -48.10056 | 2025-08-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7434a5f-8636-38f0-af41-d26759c6600f | -10.33349 | -50.06788 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4737da13-6a93-3a2d-bdbd-6ae828724f56 | -11.41049 | -54.71918 | 2025-08-04 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8714eb2b-e354-30ac-83d5-cf04c1b6639f | -7.38353 | -48.08005 | 2025-08-04 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 461f6a73-c655-3e98-bd28-c623e901616f | -7.54389 | -44.87392 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae07079-55cb-33ed-b9d7-c60af3974d63 | -8.73349 | -46.41796 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be023ee3-376a-3f9c-83c6-8bcf2b4203fd | -6.67276 | -59.16534 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99cf909d-8cdf-307d-9522-0ee6e52eda3b | -7.40602 | -45.2701 | 2025-08-04 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e1d7518-a2bc-36d4-8c0c-b251c7d974b3 | -7.03257 | -59.84994 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a01516-e163-3944-880b-8759e2c7a0a3 | -8.0008 | -43.14392 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 80554515-0780-3f80-9a40-e8dae4a360ad | -7.99325 | -43.16415 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 9521bb4c-f701-3217-83f5-f9676e6d7d90 | -8.03708 | -43.10893 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| feb58096-5541-3b19-be5e-17643e030585 | -7.36762 | -44.18946 | 2025-08-04 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f2acb90-4bd3-3ccc-b09e-b558fea6ca51 | -8.2668 | -47.37481 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95d3f6b3-beea-3486-9c00-2a238101d075 | -6.65267 | -59.09706 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1840fb10-248d-375d-88e4-53f754d49a50 | -10.32893 | -50.07089 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e674cc49-69c4-35f5-842e-4cf6920ae1e7 | -11.93652 | -44.96309 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2e1582f-a244-346f-9bf5-8acebd02a170 | -7.01394 | -59.83507 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b50aced7-bd53-3764-ac27-01933825220b | -8.00639 | -43.14977 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 52d11994-ea0c-31c9-b6bf-7d7752a65b80 | -7.99894 | -43.15839 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0be8d046-f5fb-3e3f-a984-5b8d47d98107 | -7.01583 | -59.82399 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9fa303d-44f9-302a-9b3b-a3a883925caa | -9.7502 | -63.19658 | 2025-08-04 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21d235e0-e6f3-3b5c-83cb-93a2513e1436 | -9.39273 | -45.5059 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f77bafd-f7ab-35d5-ae8a-a3e0d6497039 | -7.4439 | -48.94017 | 2025-08-04 04:57:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe4a3da-9683-39fa-91ce-8939fbb77b03 | -8.04333 | -43.10978 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| df24927d-d39e-3d6a-9316-fee9274d7f9a | -8.36171 | -46.94194 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54fd909b-1749-3674-bc0d-6e2476023ac3 | -6.62559 | -59.96919 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6fe57bc4-e672-3403-a402-08a8ac3f6781 | -11.9949 | -57.21168 | 2025-08-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc181d09-5d11-34fd-bf3d-74f808556ca0 | -11.78477 | -44.99932 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9659618f-a609-3699-849e-04558e97cb2c | -10.25023 | -50.16165 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b84bd11a-2ae7-3611-b12b-cc43f121a7dc | -6.62207 | -59.96458 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6ebd120-8f7c-3a47-a0e1-7641b3bf5571 | -7.53794 | -44.87826 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69c9dd8b-66e2-3b84-b768-443452e24134 | -6.6198 | -59.95238 | 2025-08-04 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7d146f2-8a30-3269-baba-67cf250c713b | -7.31785 | -59.61845 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc52097b-77b8-3564-87d7-07c39942227a | -8.007 | -43.19401 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ccdf7e39-f859-3606-a2c9-9b013268a348 | -7.7827 | -45.22424 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2ca0f2f-969c-3f2e-bccb-a09c1d88cce5 | -7.01993 | -59.8247 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0588e955-7b4a-3829-b0de-264e6ffcb652 | -7.01931 | -59.82835 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cc96b73-f1e1-38ec-b5e1-05f3e6d4ae5a | -6.64284 | -51.45212 | 2025-08-04 04:57:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd8d6500-1253-39b7-92b2-7be844c1da28 | -8.73588 | -46.39997 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa49d637-3441-3698-b7c1-78cb94733108 | -7.19657 | -44.49442 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c625d92-ce56-3f12-a514-bb4dc5529cfb | -11.41242 | -56.867 | 2025-08-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7a33d07-4d98-3691-b39e-5982a44b1c3b | -7.00919 | -59.83814 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d06e10f-c5fe-379f-a595-58b794a4219b | -7.01805 | -59.83577 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa09b406-9576-33bd-af0b-22c2af68232f | -8.26432 | -47.33459 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef69f93b-005d-37a8-a1c3-c9892ff8e4ae | -9.34989 | -48.25085 | 2025-08-04 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc360ac-18d9-3294-8b52-bb8a487c520a | -7.77725 | -45.22364 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba07465-1397-3244-b702-e2a566ea7036 | -8.00761 | -43.18923 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16484b73-b550-3cef-b697-866a0de32f00 | -8.27295 | -47.36548 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5784dab4-771b-3bc2-8163-64889d556a86 | -10.25425 | -50.16223 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d921025b-05e8-3780-9da6-07453c3593d8 | -7.53788 | -44.87673 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd697edd-14d8-3cf2-b596-673fe6dac7b6 | -11.2223 | -48.43253 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d7c04f0-901d-36b8-958b-31f30e9dfdb0 | -6.37663 | -53.31747 | 2025-08-04 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60ddf123-e86a-3cb2-a1da-194aa5c7b208 | -11.92313 | -44.97592 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d703016-fa19-3ae2-9f36-cc05174b32b6 | -11.78429 | -45.00319 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc276f29-431c-3c33-b71e-ea0834996e54 | -7.99196 | -43.17365 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 4228e0d2-3cf2-3bd1-b4f3-10b4126cd979 | -11.78464 | -45.00076 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138e5457-c36b-340a-b8bf-c96ce2d1825b | -10.32944 | -50.0673 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00326710-6cec-3197-b268-fcc463d773c9 | -8.36465 | -46.92045 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77641f82-d5ce-396a-92c1-d5e2d794d637 | -8.5477 | -47.46578 | 2025-08-04 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d80c9e33-aaeb-3f10-a228-c67c67bc5b46 | -8.01511 | -43.18017 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df4c36c7-9a7f-3891-ab8a-7b61d4dd99e3 | -7.02216 | -59.83648 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60fa7291-8dc0-31e2-ac85-1dd5ebffca52 | -10.57397 | -45.26952 | 2025-08-04 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b65337c-709f-3680-90ce-a1737d6d225c | -7.43971 | -48.93963 | 2025-08-04 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18a1caba-61a8-3eef-9af8-2df97f1c6449 | -11.75296 | -44.96977 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11e84ce-f8f0-3c28-a407-3acbec432885 | -7.64273 | -45.30326 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README23.md)
