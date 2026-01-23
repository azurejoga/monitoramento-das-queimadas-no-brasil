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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e262d20-b94e-3c3b-9a2a-3be72fbeb451 | -20.9141 | -49.1531 | 2026-01-23 00:00:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 90a6af69-376c-3df7-bc1c-7e3360f2c2cb | -3.4783 | -39.1924 | 2026-01-23 00:00:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 52a5cd8d-a255-3746-88c9-a90bcc682b05 | -5.6281 | -44.8433 | 2026-01-23 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 84ae7dc0-20f7-31d9-b7f9-81d520a6ec61 | -3.4782 | -39.2174 | 2026-01-23 00:00:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 109.3 |
| ac59f06b-ed13-3f50-9e8e-913cda5f4d28 | -20.9147 | -49.13 | 2026-01-23 00:00:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| f8070cc9-3c38-37d6-884b-e1ebd6070833 | -5.6281 | -44.8433 | 2026-01-23 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a171b0aa-536f-368f-a1f6-2b640f09e9fe | -3.4782 | -39.2174 | 2026-01-23 00:10:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 27cbe8eb-5bed-3476-8600-08a497e4ad4a | -3.4783 | -39.1924 | 2026-01-23 00:10:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 99.2 |
| f024115e-28fa-3051-a76e-a9025e99b138 | -20.9141 | -49.1531 | 2026-01-23 00:10:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| b682dea1-7340-32ef-b3cd-a8dc3c50d2e5 | -20.9147 | -49.13 | 2026-01-23 00:10:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| c39b4917-e88c-3b8e-8c3f-1351ddca302a | -20.9147 | -49.13 | 2026-01-23 00:20:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| b0753c39-eb28-36fb-9a6f-00d9bf7de1d8 | -3.4782 | -39.2174 | 2026-01-23 00:20:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 7d51c1d4-0649-353d-a7f0-68c30ffef2bc | -3.4783 | -39.1924 | 2026-01-23 00:20:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 0df34c00-7e99-3cb6-9df5-0a3976d808c7 | -5.6281 | -44.8433 | 2026-01-23 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2e91117c-0b3e-3622-871d-0a6ff9128d00 | -22.61427 | -49.57354 | 2026-01-23 00:24:00 | TERRA_M-M | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 445629cf-879e-3b18-ae4f-a9e785c4ef00 | -25.17121 | -49.40635 | 2026-01-23 00:24:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| c58157f7-ff70-3396-bd41-b0b4c788a2a4 | -23.05701 | -49.06926 | 2026-01-23 00:24:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a78919d-a1b9-36ec-9a98-af537d95e626 | -23.05569 | -49.05891 | 2026-01-23 00:24:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f6b5d63a-84db-3cef-8a03-9da4061abf4b | -21.77813 | -56.28047 | 2026-01-23 00:26:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 2b67f6ee-295f-3a17-9038-984e69c07676 | -22.03571 | -49.50136 | 2026-01-23 00:26:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| ddb2c6f2-9d3d-3241-bbcd-890b501eede7 | -19.67837 | -56.87931 | 2026-01-23 00:26:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| 8d5e3110-17e8-35a9-be37-85242dbc1eb1 | -20.90793 | -49.15285 | 2026-01-23 00:26:00 | TERRA_M-M | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f80e3416-d4f9-3c23-83a4-397a3abbfe1d | -21.5373 | -57.52058 | 2026-01-23 00:26:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| ac8caf1d-e739-323a-9f92-96c9183d3f83 | -19.32897 | -54.02515 | 2026-01-23 00:26:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2fbcff1d-a1b6-3386-ade6-e0ed877dabf4 | -21.54011 | -57.55517 | 2026-01-23 00:26:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c7e6a265-85ba-36ce-a35b-228d241ece9a | -21.77844 | -56.28702 | 2026-01-23 00:26:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 47d6c6ed-ef37-31ea-9b12-6a3921c5e9ff | -20.90538 | -49.13311 | 2026-01-23 00:26:00 | TERRA_M-M | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ecb5e511-c7a7-3f39-9727-6147bf6efbcb | -21.52952 | -57.52797 | 2026-01-23 00:26:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c8b36a53-4d8d-3a8c-8c32-96b380f923cf | -20.90665 | -49.14297 | 2026-01-23 00:26:00 | TERRA_M-M | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| abca9bba-314b-36e3-882f-3119b867dd35 | -22.03702 | -49.51192 | 2026-01-23 00:26:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8d5077f9-d6fb-314e-9c71-c67d85b958c3 | -8.16057 | -43.19753 | 2026-01-23 00:28:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 8f87ba4a-21a3-3c27-b87e-d5545e084526 | -14.31658 | -57.58831 | 2026-01-23 00:28:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 1b089b27-ddde-33ae-ae89-a91d316fea65 | -3.4783 | -39.1924 | 2026-01-23 00:30:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 731a2c53-1890-334a-b8bc-0d4305e9900c | -5.6281 | -44.8433 | 2026-01-23 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7ed48ed5-d621-32a7-9df4-d8e0e9504218 | -3.4782 | -39.2174 | 2026-01-23 00:30:00 | GOES-19 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 318eeabf-8664-3de2-9551-e0d9e19e3bf5 | -5.6181 | -44.83826 | 2026-01-23 00:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 585bd4f9-8f62-30d3-bdbe-b7691978ce91 | -5.6336 | -44.85553 | 2026-01-23 00:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 83915f32-d552-3d9d-a7ba-ff2f5cbb8340 | -5.61713 | -44.8447 | 2026-01-23 00:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| b56bcde9-4d12-3e36-8e70-36ad76489beb | -5.6307 | -44.83652 | 2026-01-23 00:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f92517f-826e-37d3-85c4-e3420bfc05ef | -5.62101 | -44.85722 | 2026-01-23 00:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| fe615020-3776-3b78-8aff-a97bead3d608 | -1.89104 | -52.68955 | 2026-01-23 00:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a3d6261c-d622-33d6-9fc6-d08d06758847 | -2.82256 | -52.96012 | 2026-01-23 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aeff2cde-5cbf-39b5-9d91-ee5ece4ef6c4 | -10.7433 | -37.1027 | 2026-01-23 00:40:00 | GOES-19 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 5fec0671-f2e8-3563-a9bb-714ff9ff83b7 | -5.6281 | -44.8433 | 2026-01-23 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| bae873ea-5b9e-3c61-b9f8-e0dbef6b4af1 | -5.6281 | -44.8433 | 2026-01-23 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1591ea37-59f5-3865-9e3a-726c595f1c28 | -5.6281 | -44.8433 | 2026-01-23 01:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4df137c9-28d8-3a7a-868b-412d4f02c4d0 | -5.6281 | -44.8433 | 2026-01-23 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| abe7fbdd-2df9-374f-a79e-6af54ec08f84 | -9.8151 | -36.2803 | 2026-01-23 01:50:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.3 |
| 1f64fb98-0038-35ce-9337-0c0d1c6ded32 | -9.8156 | -36.2533 | 2026-01-23 01:50:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 133.1 |
| eb163f85-5494-3d12-8441-8225688d1ff1 | -9.8156 | -36.2533 | 2026-01-23 02:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| c08b9349-5742-3b7d-be96-2ce8b5658b33 | -9.8151 | -36.2803 | 2026-01-23 02:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| c5037568-720d-3de2-bd95-52d0ba4efabe | -9.8156 | -36.2533 | 2026-01-23 02:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 50fe330a-168b-3c48-8341-da242c9a90af | -9.8151 | -36.2803 | 2026-01-23 02:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 533cffb8-40ba-33c7-bf28-4e8c84441362 | -9.8156 | -36.2533 | 2026-01-23 02:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 964142bb-451e-3a76-aeab-d90a106eacf6 | -9.8344 | -36.277 | 2026-01-23 02:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| 06cb9dba-1992-3a19-99ea-546dbe6525a7 | -9.8349 | -36.2499 | 2026-01-23 02:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| b6e9c254-6ccf-38db-8ce8-03ed421e754c | -9.8151 | -36.2803 | 2026-01-23 02:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| d934177f-651e-38a6-94a3-365c8c32cc75 | -9.8151 | -36.2803 | 2026-01-23 02:30:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| 6e5a792d-410c-3223-aa83-547447c0bb57 | -9.8349 | -36.2499 | 2026-01-23 02:30:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| d4867171-76f8-366b-bff9-ed1a00b70662 | -9.8156 | -36.2533 | 2026-01-23 02:30:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| ac33cbd3-624e-3f6c-8350-74f32c365589 | -5.44343 | -35.61109 | 2026-01-23 02:51:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 17a7a48e-f3b6-33d7-963c-16c9cddfa9bc | -5.44227 | -35.61728 | 2026-01-23 02:51:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a5ab8aa-7cd7-3069-82e3-28d9986c4028 | -9.81121 | -36.26511 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 068a3436-cd1c-315a-aca3-fdeca6950deb | -9.81994 | -36.27081 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f4a4e9f5-4792-306c-bbe8-f0acced9f414 | -9.81782 | -36.26655 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b4a0a6be-4fba-351c-8376-639e77ed06fd | -9.81336 | -36.26925 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 96f5e1b4-4366-3d89-93d7-37913233b4f7 | -9.16547 | -35.70578 | 2026-01-23 02:53:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 64c78b22-9a5d-384f-a1d9-16bad4d2616a | -9.16655 | -35.70039 | 2026-01-23 02:53:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fb1ac6dd-34aa-3bfd-9747-a39123ec4733 | -9.8211 | -36.2649 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a87f3310-d1d6-3c40-a692-307cf1bbfda1 | -9.8145 | -36.26341 | 2026-01-23 02:53:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 755b6a84-e19d-375b-b96c-72f30bba8bd3 | -9.16627 | -35.70485 | 2026-01-23 02:53:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 46e93de2-688d-3959-9106-0369f42f72a4 | -12.77502 | -38.50481 | 2026-01-23 02:55:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 37d622fe-e1fc-3d10-9ada-6ac74ad9e1de | -4.51794 | -38.42961 | 2026-01-23 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 29ab87a9-fda9-3ae2-bfe4-6d4b494ed9b2 | -5.00896 | -37.53496 | 2026-01-23 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1d4cc2ae-fbf9-3405-ba1f-e84f5215cb46 | -4.07215 | -39.82421 | 2026-01-23 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 14c8f1dc-7d4b-3a61-9de7-b55224c33f6b | -5.33372 | -38.65165 | 2026-01-23 03:42:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c60d6f9a-c9bd-3351-9759-33a0cb2f6a7f | -3.42776 | -39.1683 | 2026-01-23 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31daad4d-665a-3876-8b22-538b9c70ebae | -4.77825 | -37.81562 | 2026-01-23 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7e91f2f4-f0be-311e-972b-8909f30e8d98 | -3.45034 | -42.2508 | 2026-01-23 03:42:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ee61a0f-a41a-3546-9618-ca11e45c0a91 | -4.54223 | -40.16474 | 2026-01-23 03:42:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76548a8b-22f8-34cb-9037-959250d82d56 | -4.68348 | -38.04793 | 2026-01-23 03:42:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5463911a-ad8a-319d-858f-314ed428882c | -2.88407 | -40.5104 | 2026-01-23 03:42:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a933854c-6c69-346d-a025-918b04b22319 | -4.07489 | -39.82437 | 2026-01-23 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 19db052a-6dca-359d-b503-6a02ef6ebed8 | -5.41016 | -37.85826 | 2026-01-23 03:42:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50fdd813-afe7-338d-b6ef-9c2b1305bdbd | -4.07087 | -39.82371 | 2026-01-23 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3fb270ac-91f4-30f2-9bf8-83e1fd57e70c | -4.52161 | -38.43019 | 2026-01-23 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 878ddf53-7a95-31f1-9195-c22e491ff4d5 | -4.85972 | -37.60029 | 2026-01-23 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7eafa23a-c981-3311-b441-7fd9baa36f83 | -3.37438 | -39.14672 | 2026-01-23 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c37c940c-063a-3d63-9cfb-c158dd93d7aa | -4.07274 | -39.82067 | 2026-01-23 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 662abdde-173c-3398-93dd-e49aea9c70a1 | -3.48534 | -39.20752 | 2026-01-23 03:42:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3e57fb2e-aa81-30fc-870d-f8014b7ce26c | -4.07545 | -39.82083 | 2026-01-23 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71ad1857-3113-3a9d-bfdc-e59659486990 | -4.77471 | -37.81506 | 2026-01-23 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db8dcf51-85e0-3077-80a5-9af6d52112d5 | -2.9849 | -40.29375 | 2026-01-23 03:42:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e14a2738-6e51-375e-8854-fe88dd62c2c4 | -4.77116 | -37.8145 | 2026-01-23 03:42:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| f2f4c760-d3d6-3adb-9969-6f76620ab5bb | -5.00832 | -37.53886 | 2026-01-23 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a9a9c1ec-2891-3643-8957-2d7afae2bc5a | -2.9471 | -39.90654 | 2026-01-23 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16f3406b-49f4-3abf-9580-4e234d568ff1 | -4.53814 | -40.16411 | 2026-01-23 03:42:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33111e4e-3308-36bd-9295-0fcbad2a202f | -4.68567 | -38.04702 | 2026-01-23 03:42:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 486ba329-c19c-347f-8b90-cc8d7c461bde | -2.95122 | -39.90719 | 2026-01-23 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4d30897-ff56-3630-a578-07f36921c120 | -3.45077 | -42.24774 | 2026-01-23 03:42:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
