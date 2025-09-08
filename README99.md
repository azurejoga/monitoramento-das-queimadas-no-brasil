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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdb5841e-e818-31a4-a5d7-01b77eaa27a9 | -8.0592 | -45.4998 | 2025-09-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 471.1 |
| 8eb9ee19-65c8-391c-a7a7-50753db39e67 | -12.884 | -62.1062 | 2025-09-08 13:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e9a0deeb-c117-36a6-80c0-cb2e19f84264 | -12.6153 | -56.9742 | 2025-09-08 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0bb40859-b3f7-3f16-9b55-a5116759ff15 | -11.282 | -46.5269 | 2025-09-08 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| aef78ead-f379-342e-8779-72fec4dd17db | -6.4683 | -43.1848 | 2025-09-08 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 7b52356d-3564-3888-8e15-44a6401d42aa | -6.1024 | -44.144 | 2025-09-08 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c57223f4-291e-3afa-b1f3-45e770edae00 | -15.044 | -50.1118 | 2025-09-08 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 475b1178-6f75-3e51-b35a-5af53b737922 | -5.938 | -45.7479 | 2025-09-08 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 31c2f7e8-dd78-390f-bb2b-6f8627a99e13 | -14.3492 | -60.3046 | 2025-09-08 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0192c098-6268-383e-b08c-5ba22eb9814b | -9.481 | -60.4902 | 2025-09-08 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 04ca68e5-ab2b-34a3-9587-25b5ecf65c15 | -14.2968 | -44.8617 | 2025-09-08 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 27be8a03-aeee-3617-8ae7-f6bf46f22ed0 | -5.7113 | -43.8972 | 2025-09-08 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b165feb4-17a0-32ac-83fc-73d8e4b68ce8 | -11.4268 | -43.649 | 2025-09-08 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| f2f2c408-8572-34f9-b227-0825fe385327 | -16.3345 | -52.9387 | 2025-09-08 13:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 66dc667c-f58e-3c0f-88b0-43810f41fbd4 | -5.8672 | -45.3024 | 2025-09-08 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d061dcf5-9246-306e-89f1-04dcb0e6352f | -16.9814 | -45.837 | 2025-09-08 13:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 77f099d3-48f7-34c2-b7c1-8915fe88c34b | -10.8911 | -55.7131 | 2025-09-08 13:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| c3f20867-427c-3324-8146-357489d073c7 | -12.8223 | -52.8806 | 2025-09-08 14:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 90ea3b30-0711-3de5-836d-7237ea19be5c | -15.184 | -47.9852 | 2025-09-08 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1e1c0276-cb1a-3aaf-91ba-5ea7c0c0aea0 | -13.3178 | -51.7477 | 2025-09-08 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 67330e76-d931-3920-a069-3d42f2665e0a | -15.2545 | -52.3666 | 2025-09-08 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| ca5eff41-d50e-3b68-95f5-d82461b69157 | -5.711 | -43.9203 | 2025-09-08 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 65232562-194e-3b5e-ac9c-f1a750afdf55 | -15.7377 | -53.5928 | 2025-09-08 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| eab789d3-1c47-3824-85fb-d9a8c2a7782b | -16.3403 | -43.0394 | 2025-09-08 14:00:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 8dd96f6d-f37b-3799-a23c-5120e5d55dde | -12.6343 | -56.9725 | 2025-09-08 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1e39a477-8f14-34de-adb4-50a96e996eae | -14.349 | -60.3243 | 2025-09-08 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d2750865-9527-3f14-9d65-79d4740f7e06 | -8.3179 | -47.4621 | 2025-09-08 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3796f641-c5ed-322d-ac44-6be2805c6cae | -12.8651 | -62.1074 | 2025-09-08 14:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d9b02e58-26e9-3903-a466-79306e18bcc2 | -13.2986 | -51.7501 | 2025-09-08 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 58833f1d-1a6e-3c01-993c-abd3a663f137 | -14.714 | -60.2551 | 2025-09-08 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0493d448-6f8b-3c09-b2e1-d3a9edec354f | -16.3073 | -58.0852 | 2025-09-08 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 232c34ba-6fcc-3202-a3b2-b9d63dc28afe | -16.9416 | -45.8452 | 2025-09-08 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c3cb7906-b999-32d6-9100-59e2c1ca79a9 | -12.9477 | -54.793 | 2025-09-08 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7527a81e-c74d-3f0d-a013-5ccbe6b3bd23 | -11.3014 | -46.5018 | 2025-09-08 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 366d3c87-0ddd-34d6-a4e6-31c1abe9c3db | -14.4359 | -48.4644 | 2025-09-08 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 5b27240c-c57a-3657-a638-3f4e2beb5b8f | -15.2136 | -44.0255 | 2025-09-08 14:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 862fdf23-028f-3638-a26e-48fa308a4dd9 | -6.209 | -40.9894 | 2025-09-08 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 9d936507-0eb2-3bfb-a5c6-d769e74bb4e4 | -5.8081 | -45.6448 | 2025-09-08 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 18f6e072-d166-3b4a-b448-5e4b1f5217db | -16.9024 | -45.83 | 2025-09-08 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| bf3e406f-68f3-346e-9a5f-1d00d8848633 | -7.7296 | -44.735 | 2025-09-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 190.8 |
| d410961e-9564-31e1-a2f1-f8a9fc4d5c11 | -16.9814 | -45.837 | 2025-09-08 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 546a9219-2621-38db-b382-7e28f555d254 | -14.5648 | -53.0925 | 2025-09-08 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| dbff5449-8bb6-3455-81a9-6a34324a90c7 | -15.2541 | -52.388 | 2025-09-08 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 037302a0-3ed2-326b-aa33-abb2a7622cb3 | -9.74 | -51.14 | 2025-09-08 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5add6dab-cd84-3593-ba1b-150d6d3a06a8 | -10.8911 | -55.7131 | 2025-09-08 14:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 4007a158-f842-34c6-9f13-beb46fc72a60 | -11.3011 | -46.5244 | 2025-09-08 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 23fbf248-185c-32ca-912c-86a15ba10761 | -16.9615 | -45.8411 | 2025-09-08 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 124.4 |
| db062f60-8534-3e29-bbaf-b187e2052123 | -15.044 | -50.1118 | 2025-09-08 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 128.9 |
| c50c1470-aa9c-35c8-bdbf-f2e7e9b16080 | -8.3239 | -46.9533 | 2025-09-08 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 24972509-10d5-38a0-9dc9-e34fd23b62df | -5.938 | -45.7479 | 2025-09-08 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f7deedc4-df5e-3582-9f46-960a1ecc60ac | -5.211 | -43.2833 | 2025-09-08 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 47e35b28-0599-3842-a3dd-702156a57ce1 | -6.2087 | -41.0137 | 2025-09-08 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| bf9c422c-50e2-3662-832a-9e80754aeef9 | -16.3345 | -52.9387 | 2025-09-08 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 79943837-1521-3dab-a119-d3100dc455d6 | -16.9029 | -45.8064 | 2025-09-08 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 74c428a4-e19b-3d2d-8a42-3d6073c11b80 | -7.5035 | -48.2116 | 2025-09-08 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| edeba68f-9567-3362-aa91-de922d809e5a | -11.2007 | -54.9992 | 2025-09-08 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4934230c-0254-3ad7-8970-e1f886bc9d51 | -14.3681 | -60.3228 | 2025-09-08 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 60c0c001-347e-3eee-b1f9-2db43d051c6f | -7.6559 | -47.9593 | 2025-09-08 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| c12ae188-800b-3a1f-bf28-ab780b73df84 | -14.3492 | -60.3046 | 2025-09-08 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 16a8a276-6ed2-3e58-b3be-2b67eaedbbaf | -5.73 | -43.8958 | 2025-09-08 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| eb842c8a-77e2-30d9-83e4-6bb5c8cd8114 | -5.7113 | -43.8972 | 2025-09-08 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 285.5 |
| 1f7a9bac-6bce-3dbc-9ae0-1eb1837b3c91 | -6.4683 | -43.1848 | 2025-09-08 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b1dc5474-37b7-3c66-9ba5-4a2d43eaf1cc | -5.6106 | -44.7078 | 2025-09-08 14:00:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ffa94be7-9953-3501-b83f-c23efa352fe3 | -7.7484 | -44.7332 | 2025-09-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b0ea7a91-d59f-37f5-94d9-e72a6e8e783a | -8.1998 | -44.7794 | 2025-09-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7fbe6c31-481e-3560-87a7-1b43ddfe3c7f | -5.8672 | -45.3024 | 2025-09-08 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 0da666d7-d0b3-3afa-b202-4ee6d9eb8b35 | -11.4268 | -43.649 | 2025-09-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 456dde8e-a51f-33bf-ac06-66d670fa5bd6 | -7.4367 | -49.2747 | 2025-09-08 14:00:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a875df12-9c04-342d-98b6-f9a416888212 | -5.3671 | -44.7703 | 2025-09-08 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ce172c0e-7d3c-3614-b1cc-6ab70958c1ec | -16.307 | -58.1055 | 2025-09-08 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 83166af3-e473-3dda-9c63-5bb1ce1a4648 | -6.62 | -53.3373 | 2025-09-08 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8117f23e-a954-369d-a754-d8278d8d3cec | -9.481 | -60.4902 | 2025-09-08 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 651c688e-c3e2-392d-9f80-1b88b718233b | -8.0592 | -45.4998 | 2025-09-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 2d7325f5-f668-3381-8dfa-5bb13a6d4832 | -9.4611 | -46.4566 | 2025-09-08 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0db2dd2a-4421-34a5-9df5-24fb95367242 | -12.8411 | -52.8994 | 2025-09-08 14:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 295.0 |
| 1c9a3338-7272-334b-a145-f604b2da0afb | -12.6153 | -56.9742 | 2025-09-08 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8223395f-efa5-34ef-b2ae-b900bac1bece | -11.2005 | -55.0195 | 2025-09-08 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| de8776a7-46f7-3c64-9340-1d3661d7531c | -12.884 | -62.1062 | 2025-09-08 14:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f815eff8-b8ed-3ed2-9278-3d8a640d1685 | -9.8278 | -53.2976 | 2025-09-08 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 454483a5-263a-387c-aceb-8ba7bfde2eff | -5.8485 | -45.3038 | 2025-09-08 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8c44399c-112b-39f9-a93a-aebfed396ce5 | -11.1384 | -48.3906 | 2025-09-08 14:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 49a54766-b6d0-3eae-aa85-a54a59158f63 | -12.948 | -54.7724 | 2025-09-08 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 194130be-a133-35ae-90c1-6c383dc7eaee | -10.8722 | -55.7147 | 2025-09-08 14:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| fe07b69d-497d-3797-aa92-5571dc4cd16d | -6.2236 | -49.4241 | 2025-09-08 14:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 454.8 |
| de5ecdf4-a7d7-341a-b713-d7f8e47d6744 | -6.8708 | -47.9129 | 2025-09-08 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c70df71f-f2c7-36a9-9e7d-57ac94689506 | -7.4367 | -49.2747 | 2025-09-08 14:10:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 94eff451-30be-33d4-9bee-6911b4863c32 | -12.8223 | -52.8806 | 2025-09-08 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| e2b498bf-b0db-325b-8abc-5479b88081c7 | -12.8651 | -62.1074 | 2025-09-08 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b4f9387c-e2f2-3e4c-93ef-0eb7da725d9f | -5.6106 | -44.7078 | 2025-09-08 14:10:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 9df0a372-a32c-3f50-8bc5-d5c9da4bd2a3 | -8.3239 | -46.9533 | 2025-09-08 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6c91a54a-6ab1-35be-a790-6a73fac993f2 | -11.2005 | -55.0195 | 2025-09-08 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e50c9691-a7bb-3589-b1db-bdd82bf49732 | -16.3068 | -58.1257 | 2025-09-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| fdb52d84-e546-39eb-afcc-9d0ea1df0d6d | -13.3178 | -51.7477 | 2025-09-08 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c1208c46-d215-3e9f-bc5d-17b388b477e8 | -9.5127 | -48.244 | 2025-09-08 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b8300058-a09c-3899-a8c1-e2ca39f07d14 | -12.822 | -52.9016 | 2025-09-08 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| eb3f4771-6c82-3336-83fd-2f1342fa9fe7 | -16.3403 | -43.0394 | 2025-09-08 14:10:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 149.0 |
| be939d5c-2b06-387f-9220-ada503f6c7e9 | -16.3345 | -52.9387 | 2025-09-08 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1cef9466-c511-3739-8bad-d379b9bc517c | -15.6359 | -53.8586 | 2025-09-08 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| bf8c38db-8b81-3ac5-8079-e8023ded6bfd | -7.7296 | -44.735 | 2025-09-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f9402482-b1ad-3664-b8ad-c77772a0250d | -12.884 | -62.1062 | 2025-09-08 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |


[Clique aqui para ver as próximas entradas](README100.md)
