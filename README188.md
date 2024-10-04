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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb6ff742-50e6-307b-a518-56746a7eab1d | -13.1787 | -48.6295 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 161.2 |
| d91ccce0-c103-3553-8fa8-9d0621015da5 | -13.1791 | -48.6073 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b567ee00-ce9e-3bfa-bc25-c8ac7d36f9da | -13.0594 | -51.1409 | 2024-10-04 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8b6e6a82-367a-37d0-b211-5ca101341fd2 | -13.1636 | -46.3231 | 2024-10-04 12:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 91fa7fac-6f9a-3977-b6f4-ebd9e9e24a05 | -13.1599 | -48.6101 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 11e9490c-f5a3-30b4-9b7f-f2bbdcebb715 | -13.1779 | -48.6737 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b133f6e0-b635-3c19-88a7-98e37df07d95 | -13.1443 | -46.3261 | 2024-10-04 12:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| d58fba00-ca50-3876-b56c-fd842660bdf4 | -13.1447 | -46.3033 | 2024-10-04 12:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 93d80230-e163-3a80-bc45-e5827d1e92fc | -13.1163 | -51.1765 | 2024-10-04 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9b1728ad-318b-3dba-a5a6-09810df2bbe3 | -13.1595 | -48.6322 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 290f9d12-128a-3e59-9c7d-df0b5a5d4061 | -13.079 | -51.1171 | 2024-10-04 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 373.3 |
| 256e5ab2-a40a-379d-87f9-cf3a87d58bdc | -13.0786 | -51.1385 | 2024-10-04 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.5 |
| ea60d311-c0b2-357a-b109-cb4a73c71aea | -15.6304 | -47.2063 | 2024-10-04 12:06:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e97bb5e7-c6e6-3471-abc7-668bf71c2e37 | -16.613 | -57.1965 | 2024-10-04 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.4 |
| d7ecf065-0b69-3e21-a35f-a76f9e3d8a0d | -16.6133 | -57.176 | 2024-10-04 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 168.2 |
| 83f8f500-4d1f-398a-90d7-c102ba4d8baf | -16.5935 | -57.1988 | 2024-10-04 12:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 228.5 |
| 774d9b23-512d-3bd2-a3a6-4b4c451e0ecd | -17.1574 | -57.3993 | 2024-10-04 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 2ea692de-4628-3d05-8655-491abe148f9e | -17.1378 | -57.4016 | 2024-10-04 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 0146065e-8e56-3306-9e91-97a5077feac6 | -9.9822 | -42.0976 | 2024-10-04 12:16:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 335f2372-6bee-37aa-9ced-6addc17d1e63 | -9.8353 | -46.7502 | 2024-10-04 12:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 964ccef0-0d02-3d16-a0fc-b3098da6fffc | -10.2761 | -47.6995 | 2024-10-04 12:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| d2b38676-bf81-38bc-bb5c-51ec28b0c006 | -10.2571 | -47.7017 | 2024-10-04 12:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 4601b57e-b19a-371b-b509-658a8e8ae200 | -10.2378 | -47.726 | 2024-10-04 12:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8832719e-2c33-397f-a44c-4bc0983c0eba | -10.7309 | -47.7126 | 2024-10-04 12:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9f193519-bed2-34f6-bd1d-fe8ecf7a772b | -10.7352 | -46.1918 | 2024-10-04 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0f41765f-d34d-3a5d-8f39-4a81bc4da35e | -10.7355 | -46.1692 | 2024-10-04 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 301.0 |
| d93662dd-c24d-3968-91b2-fb07e2ed88cd | -10.7359 | -46.1465 | 2024-10-04 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 2a532690-dd20-391a-8606-3efa2e0cadeb | -11.0349 | -46.4917 | 2024-10-04 12:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9d443f5f-8291-34aa-9e84-649581eb0a72 | -10.8992 | -46.6442 | 2024-10-04 12:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a6840708-35aa-3ec7-9e7e-6eb73e4f8ea8 | -11.2779 | -43.4118 | 2024-10-04 12:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 72bad831-fc97-39e2-b42b-c447f09ab3db | -11.2369 | -46.9597 | 2024-10-04 12:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 912e1a4e-7f90-3776-843b-c5eaa32b396e | -11.2783 | -43.388 | 2024-10-04 12:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 29076659-2cb5-3eee-a1e3-fdb7512e031b | -11.2971 | -43.4088 | 2024-10-04 12:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 8cfa20c1-99ab-3f20-aa60-32fd64b19c46 | -11.3341 | -46.8349 | 2024-10-04 12:16:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ca506ee4-4b3f-3f41-ac8b-b9283c335250 | -11.3536 | -50.5304 | 2024-10-04 12:16:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 863edac2-c6e6-3438-87bc-4254f1805f75 | -11.3849 | -47.2312 | 2024-10-04 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f692cede-216c-3105-8685-2b3dfe9add1f | -11.404 | -47.2287 | 2024-10-04 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| e102edb0-e42c-37ec-a170-62890c7bde7b | -11.9105 | -50.1447 | 2024-10-04 12:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a018d53e-e277-3269-8940-7c7dfaea33ac | -13.1591 | -48.6543 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d2b92c30-d9ce-3324-8a07-724fbe4b133c | -13.1447 | -46.3033 | 2024-10-04 12:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 4803e8c3-6721-34ef-b4f4-f045364da243 | -13.1587 | -48.6764 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 292307dd-60cf-3c18-b7af-e64eeebd9209 | -13.1595 | -48.6322 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 4b3f1f14-a8c3-35c8-9d85-e63298c33d32 | -13.1254 | -46.3063 | 2024-10-04 12:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c0871598-be3a-39ec-a8e7-5f184830ab28 | -13.1779 | -48.6737 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| bdd5060b-87c4-394f-adcc-dd0a2c56fb89 | -13.1787 | -48.6295 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b4becd15-2111-3471-81f0-64a73a1c79a4 | -13.1791 | -48.6073 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b84c65ce-ff38-377f-9a07-ced45caba138 | -13.1599 | -48.6101 | 2024-10-04 12:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 49665b17-2b2b-3d0a-bd20-7e11b5bdaf31 | -13.1443 | -46.3261 | 2024-10-04 12:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 34e7b731-1eb9-3642-8806-90465a35e1ce | -15.6304 | -47.2063 | 2024-10-04 12:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 376d31c7-563e-30dd-865e-530efc8c00b7 | -17.1574 | -57.3993 | 2024-10-04 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| a0e6a1dd-d688-38f6-9958-70e3ff177fa4 | -8.1951 | -43.6703 | 2024-10-04 12:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 879413fc-297b-3e14-8ce1-0d7a85c6fb5e | -8.1948 | -43.6936 | 2024-10-04 12:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 6ed60aee-4765-300a-a4a0-c2ee30761359 | -8.1762 | -43.6723 | 2024-10-04 12:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| da75637d-c0f7-3a14-afcc-e6fc115039dc | -8.1759 | -43.6957 | 2024-10-04 12:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b2413f37-91ea-3a97-a7ab-26f22ee6e8e9 | -8.834 | -48.3115 | 2024-10-04 12:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9b6371d8-9c0c-3894-bbb7-9a3c3dbddbec | -9.1041 | -50.902 | 2024-10-04 12:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a8438fa7-c05d-39f4-9689-afde8170756c | -9.1039 | -50.9231 | 2024-10-04 12:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 36267da8-3da5-3c88-8f4d-f1242e9c813d | -9.8855 | -47.2124 | 2024-10-04 12:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c27db6c4-189b-39d7-b84b-0a445ea2b0cf | -9.9822 | -42.0976 | 2024-10-04 12:26:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| f2b6f755-78d5-33e1-b61c-9885c16a8575 | -10.2571 | -47.7017 | 2024-10-04 12:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d0b9d201-e0fe-38c5-8985-e2c6e2e55783 | -10.2761 | -47.6995 | 2024-10-04 12:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e0b420a7-d6b2-3780-85c5-e871f6f25699 | -10.2378 | -47.726 | 2024-10-04 12:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2541dbbd-9b6b-3904-b921-b1f141ff9b8a | -10.7309 | -47.7126 | 2024-10-04 12:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| fe189ca6-728c-3713-a384-a329ac1aaed7 | -10.8018 | -45.5927 | 2024-10-04 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| e7d91826-d223-3937-a065-78e07570cc20 | -10.8661 | -46.3331 | 2024-10-04 12:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| aefa2b62-1907-355a-93b3-c8e678ef6ec6 | -10.7118 | -47.7149 | 2024-10-04 12:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 35ff0c06-41f9-36a3-9d88-8aad9c659407 | -10.7352 | -46.1918 | 2024-10-04 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 923b4558-0594-3e85-bc20-12d838b87203 | -10.7359 | -46.1465 | 2024-10-04 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.6 |
| ea6102fa-6e57-3362-b200-3446ce49232b | -10.7355 | -46.1692 | 2024-10-04 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 357.8 |
| a8185229-b0f4-3ad5-8700-ce095dfcb7c3 | -10.847 | -46.3356 | 2024-10-04 12:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d2ff8b7e-fe0d-33a2-be44-2accee3cdd5b | -10.8021 | -45.5698 | 2024-10-04 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7b36b1da-8170-3bb7-a788-5c77a05d820f | -10.8992 | -46.6442 | 2024-10-04 12:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 4bd8894d-a988-3e02-8f98-936883eda7ab | -11.0349 | -46.4917 | 2024-10-04 12:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 76798c91-90df-3537-915b-cc0bc0ba73c2 | -11.2779 | -43.4118 | 2024-10-04 12:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 8c420c94-fb73-334c-92d9-8c6be84ff979 | -11.2783 | -43.388 | 2024-10-04 12:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| d639cbbf-efed-32df-9f52-6bec1fd94c95 | -11.2971 | -43.4088 | 2024-10-04 12:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 918c4227-d40f-30a0-a160-65d7e0ed8209 | -11.2178 | -46.9622 | 2024-10-04 12:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9fc1ae54-8039-3019-b5ba-787412bbe643 | -11.2369 | -46.9597 | 2024-10-04 12:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 491.5 |
| 988d384f-29b5-3419-991d-52a70c2c8084 | -12.7815 | -50.5758 | 2024-10-04 12:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cb791197-f22e-35d2-aee4-cca87dc9292e | -13.0786 | -51.1385 | 2024-10-04 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fdd8f6f9-97e7-3aff-863b-cb1294b233f5 | -13.1166 | -51.1551 | 2024-10-04 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 266.2 |
| 1bfbbe37-1bce-330f-83a0-7f910af2347c | -13.1163 | -51.1765 | 2024-10-04 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 2825ac41-ea5d-3a19-8c2e-9eff67b44241 | -13.1443 | -46.3261 | 2024-10-04 12:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 32f2fd99-fe80-32d0-a52e-d13832b476b9 | -13.1447 | -46.3033 | 2024-10-04 12:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1a1f3c29-e8e7-3c57-830f-e90fab9ae58c | -13.0598 | -51.1195 | 2024-10-04 12:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f89e50e4-cf1a-3abd-8e0c-4bc33aba1733 | -15.4247 | -47.6736 | 2024-10-04 12:26:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b16ab4ad-f012-30ef-a48b-4205ae95504a | -15.4051 | -47.677 | 2024-10-04 12:26:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| cea9a26a-ce52-36ab-b107-71ad9bd256fa | -16.6133 | -57.176 | 2024-10-04 12:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.4 |
| e35164c9-1f1a-3420-9465-ffa4d35541a4 | -17.1574 | -57.3993 | 2024-10-04 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 3ecffd0c-4bce-37a2-a2f1-5f11ce84def9 | -18.7952 | -46.6393 | 2024-10-04 12:26:50 | GOES-16 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 35369c0c-6e1a-3ee4-b348-59ef8f73851c | -19.1134 | -48.2833 | 2024-10-04 12:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 749fe91a-8167-33f5-8151-cd70d4eab4c8 | -19.114 | -48.2602 | 2024-10-04 12:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 89356b01-cf88-391f-8494-cb7ee0e7e24e | -7.8166 | -50.5219 | 2024-10-04 12:35:51 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 08cfa08c-33b8-3c08-b8c3-603f1fcd767a | -8.1948 | -43.6936 | 2024-10-04 12:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 02ee14ff-0bc9-3afb-afa2-bbc04e45088a | -8.1055 | -44.7891 | 2024-10-04 12:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3263a773-72d6-3aae-a6e7-7c999750fcc9 | -8.1762 | -43.6723 | 2024-10-04 12:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 98bee81d-3d61-38e0-8b4d-39353e8ed39d | -8.1951 | -43.6703 | 2024-10-04 12:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 164.2 |
| bea79f83-72c8-39d0-b4ae-8e5d50d76e43 | -8.1244 | -44.7871 | 2024-10-04 12:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bcbfb3eb-ca33-3649-9f9e-a97cdb6b9c64 | -8.1759 | -43.6957 | 2024-10-04 12:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| da06d27a-7217-30d2-94d4-82a94bf11439 | -9.1039 | -50.9231 | 2024-10-04 12:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |


[Clique aqui para ver as próximas entradas](README189.md)
