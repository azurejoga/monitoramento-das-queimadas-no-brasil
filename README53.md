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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6271660-54ac-3683-9288-28d38ae23157 | -21.65594 | -54.83352 | 2024-10-05 03:53:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50851c9e-78ad-38af-b049-5d60648f61d1 | -21.65577 | -54.83401 | 2024-10-05 03:53:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f20f8c25-4ced-310e-bb8f-bb5ce2a0644a | -23.98458 | -48.91843 | 2024-10-05 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c8f04e-065f-3a84-9ef4-9ceaa8a487c3 | -21.96248 | -41.51649 | 2024-10-05 03:53:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f5f8954-9901-31fe-a472-8487d821680c | -21.96186 | -41.52027 | 2024-10-05 03:53:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 47b8bdc1-12bc-36d3-bfb2-22249f58c910 | -21.95853 | -41.51964 | 2024-10-05 03:53:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58c6b24e-4f3e-3773-b2da-7443f77f8fbe | -21.93562 | -41.55434 | 2024-10-05 03:53:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| acbe1b0e-fbc7-37f4-9e2f-1327784053ea | -21.93228 | -41.55371 | 2024-10-05 03:53:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d94a7587-0613-3776-a426-d77f4f4b716c | -22.32742 | -43.18695 | 2024-10-05 03:53:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60dd8ede-8d37-33ee-b5d0-85756a431e18 | -21.44647 | -46.5557 | 2024-10-05 03:53:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6073cd5d-0167-384c-8e98-501d09dbe4df | -21.44567 | -46.55989 | 2024-10-05 03:53:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 59e16d3c-3667-3a50-a04d-c11689c60d43 | -29.81367 | -51.17568 | 2024-10-05 03:55:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| e57e5fc5-1bde-3d70-aede-653395302934 | -4.0794 | -47.9502 | 2024-10-05 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 758753fd-b404-3cdb-b137-a1c18c0ff278 | -5.8216 | -44.1196 | 2024-10-05 03:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8ed8d1ee-f024-33d4-9cfc-dd255713f830 | -5.8214 | -44.1426 | 2024-10-05 03:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f0ef6561-b211-3bd1-8b73-c1bd14f47e0b | -6.9514 | -59.0666 | 2024-10-05 03:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 425cf3bc-d122-36d8-92d8-afa1ff5243fd | -7.5193 | -63.2558 | 2024-10-05 03:55:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7d3a335b-ce3e-3b18-a4e6-1406335c2b79 | -8.7844 | -44.8085 | 2024-10-05 03:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| d34daea6-75cf-351f-8d90-9817fd51deae | -8.7841 | -44.8315 | 2024-10-05 03:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| e14c9237-f763-3fea-ba1d-3c6c20317ac5 | -8.7655 | -44.8106 | 2024-10-05 03:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 2f1e1ed1-7cf3-3042-8d0d-f26659fde049 | -8.7652 | -44.8335 | 2024-10-05 03:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 24c23c8e-293a-33c7-ad93-11bc391bef00 | -8.7772 | -49.955 | 2024-10-05 03:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 89816c87-ce8f-3841-8b8d-0d076963dbf0 | -8.9853 | -49.8083 | 2024-10-05 03:55:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a513a2dc-f7f7-3108-be86-246f223d6db4 | -8.9851 | -49.8297 | 2024-10-05 03:55:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e7bd7c70-a531-35bc-8016-5ebd5fb9c973 | -9.1759 | -61.5794 | 2024-10-05 03:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c418f42a-ea54-3546-8a24-b6701fe6e9b0 | -10.332 | -50.5109 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e6e6b7f4-c1f2-31bc-bf7d-6cc557c57920 | -10.3318 | -50.5322 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 05dce4d4-7ed6-3442-9705-6d1c13bf1359 | -10.3131 | -50.5128 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 240.2 |
| 5306a942-a807-37d4-b4e3-a94d159d2436 | -10.3129 | -50.5341 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 5df97fdd-8707-3d45-9197-6782777de5b0 | -10.2942 | -50.5147 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 95f81968-1cb3-34c7-bcf2-b67a024550ea | -10.294 | -50.536 | 2024-10-05 03:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3f9772b1-5412-38e5-bc3f-2c60d1fc30d8 | -13.1056 | -46.3321 | 2024-10-05 03:56:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1194536b-389b-373c-9731-23e9445422e4 | -13.1052 | -46.355 | 2024-10-05 03:56:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 5789c260-62dd-3341-a311-3969a371dbc9 | -13.1047 | -46.3778 | 2024-10-05 03:56:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 213.7 |
| ca7085fc-74d1-3b29-aad0-e9786718840d | -13.1245 | -46.352 | 2024-10-05 03:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 9ee803c2-e858-3e03-a05c-44002688faa3 | -13.1241 | -46.3748 | 2024-10-05 03:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 137.0 |
| fb58cf91-3660-31cd-9d08-1e58ca4eec41 | -14.0567 | -45.1847 | 2024-10-05 03:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9bfbc867-4110-387e-962e-579ef10854ff | -16.554 | -57.2237 | 2024-10-05 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.8 |
| bc501c28-5cc3-3f5d-81cb-8cb0b298a295 | -16.7647 | -57.4856 | 2024-10-05 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.9 |
| a9790c3a-3222-3b0a-840d-4c05ae22fe13 | -16.7644 | -57.5061 | 2024-10-05 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| a8fdd575-c600-3f2c-8561-f9dc5c6a9b88 | -16.6871 | -57.4536 | 2024-10-05 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 94a2418b-417f-3678-8788-0abb94b0dbbc | -16.6598 | -55.5219 | 2024-10-05 03:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 02922a2c-62b0-3c28-8739-4b0477dc9a9e | -16.6405 | -55.5035 | 2024-10-05 03:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| f30a9e96-3566-3b22-9836-1b3b45fac7aa | -16.6402 | -55.5243 | 2024-10-05 03:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 851df67e-c4c6-3036-bb63-b490d798dda7 | -16.7843 | -57.4834 | 2024-10-05 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 270d3a82-dd9e-3dca-ac5b-67e836f1ff05 | -17.012 | -56.698 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.3 |
| 5b06d5d9-cc7d-3b0b-b1bd-c9d1dca2802b | -17.1433 | -51.7206 | 2024-10-05 03:56:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 470ef69f-5156-313e-bbf4-d56ba024106a | -17.1235 | -51.7238 | 2024-10-05 03:56:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 3b570dd2-56c5-37f0-9a38-b22f98d187b2 | -17.0313 | -56.7162 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| b4a0590a-1934-3ee6-a1af-d8d09a4e58be | -17.0316 | -56.6956 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 332.7 |
| 598fe14d-dad1-3c29-853d-3864d9bc8766 | -17.0319 | -56.6749 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| a8d6df01-b680-32dd-bc67-0f6c4e4fce1f | -17.1178 | -57.4244 | 2024-10-05 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 03083c58-50ba-32b9-907e-c3f70543a1d3 | -17.1375 | -57.4221 | 2024-10-05 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 864afe65-574e-3906-9cfb-9b864e5a50ba | -17.1182 | -57.4039 | 2024-10-05 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.6 |
| ecc2fbbf-4736-3836-ab9d-04438f55427c | -17.1378 | -57.4016 | 2024-10-05 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.4 |
| 7487170e-ef7a-3f8d-b3f7-693ccea65837 | -17.0123 | -56.6773 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 30daea16-e13e-3b73-a8e2-5827641d5432 | -17.0512 | -56.6932 | 2024-10-05 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.6 |
| dfb2949f-0572-3ea9-b8af-3ecaa86d68dc | -18.5058 | -52.841 | 2024-10-05 03:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 042c9d79-89f0-3ac3-a784-8a832fae2bfb | -18.8816 | -43.5785 | 2024-10-05 03:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| f6f1cd91-6293-3bc2-a56c-489f9d143ec5 | -18.8809 | -43.6032 | 2024-10-05 03:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| 17eeecdd-4ab3-3fd5-b28e-79d72db6cf38 | -18.6981 | -57.2915 | 2024-10-05 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| e7acdf3e-c1e7-3e14-9ff8-a8938f0ebaf7 | -18.6785 | -57.2734 | 2024-10-05 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 72c194be-61c0-3832-8799-430dd4f534fd | -18.6782 | -57.2941 | 2024-10-05 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 6ee42c8b-4346-3329-ae25-14a1899bce9b | -18.6586 | -57.2759 | 2024-10-05 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.7 |
| 278b195d-c30e-39ae-8ab1-6fd0b0e51205 | -18.6582 | -57.2967 | 2024-10-05 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 96316da2-2608-304e-a725-57c16ff6c020 | -13.1 | -46.39 | 2024-10-05 04:04:09 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d4c1ec5-ab95-39ad-96a7-db2a1a1db4c5 | -12.78 | -50.51 | 2024-10-05 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f5570bb-51ce-3359-b642-9883c3cdc2b6 | -12.78 | -50.57 | 2024-10-05 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58726b00-04a9-3406-88ce-59f15e1391eb | -12.62 | -53.12 | 2024-10-05 04:04:14 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 667247cb-20c6-3e5b-98b4-d63904e26035 | -8.78 | -44.83 | 2024-10-05 04:04:35 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 598e98e9-d5ef-32ee-8d9a-1e30e5407d9e | -2.9014 | -50.7142 | 2024-10-05 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 88066595-1152-391c-bc0e-c83b2d8a14b7 | -5.8214 | -44.1426 | 2024-10-05 04:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fccd7d43-3115-3317-9501-e18203b46988 | -5.8216 | -44.1196 | 2024-10-05 04:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 93d54f46-f3f9-3361-978b-654123e50536 | -6.9514 | -59.0666 | 2024-10-05 04:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3a1a5874-65ba-33ce-8510-29a10b951888 | -7.5193 | -63.2558 | 2024-10-05 04:05:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c85965a3-a13c-3669-9547-08bb27a01b61 | -8.7844 | -44.8085 | 2024-10-05 04:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5d4decb5-5e71-3b58-9e60-6511f75fd9ed | -8.7652 | -44.8335 | 2024-10-05 04:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 93a2b70a-9f80-3e82-a137-0ff2e03d5e72 | -8.7655 | -44.8106 | 2024-10-05 04:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 36a344ea-75e1-30d7-9c9e-f9291c71f251 | -8.7841 | -44.8315 | 2024-10-05 04:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a9688b23-dcfa-3e7c-83c4-098029361802 | -8.7772 | -49.955 | 2024-10-05 04:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| b022751c-93ee-3c91-b522-3f3778730f19 | -8.9853 | -49.8083 | 2024-10-05 04:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 308308da-84b7-3d83-abd7-65f602770ae0 | -9.1759 | -61.5794 | 2024-10-05 04:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1dd234e4-ae80-3828-bbf0-30111bb13f07 | -10.3129 | -50.5341 | 2024-10-05 04:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| af786fce-6caf-3c28-a05c-e7ca27fb3d34 | -10.3131 | -50.5128 | 2024-10-05 04:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 099ab960-6f17-350a-8b19-a119541f39c1 | -10.3318 | -50.5322 | 2024-10-05 04:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 650096b6-94d0-3051-a600-27939e81208b | -10.332 | -50.5109 | 2024-10-05 04:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a068cb05-6e92-31c2-8532-51775ad96c94 | -11.2361 | -47.0046 | 2024-10-05 04:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| fd7ca1c4-092a-3f27-9c19-5cd799be41d2 | -11.2365 | -46.9821 | 2024-10-05 04:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 07def158-6ace-3306-a396-846edd73bcce | -11.2556 | -46.9797 | 2024-10-05 04:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 43c1ccfb-8545-3464-a2d3-7263a11f1ceb | -11.2566 | -60.5825 | 2024-10-05 04:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3612a4bc-dff2-3f44-b256-31e58d6d26e8 | -13.1047 | -46.3778 | 2024-10-05 04:06:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 90f95afb-2a8a-3a9a-8e4e-57bd01ad0831 | -13.1052 | -46.355 | 2024-10-05 04:06:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 8d94a1e2-bdd0-3ff0-9402-afd99aa3c0c5 | -13.1241 | -46.3748 | 2024-10-05 04:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 85fba75b-ce24-383f-9ae7-9b9bdc96cb92 | -13.1245 | -46.352 | 2024-10-05 04:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 02824349-31d0-36ee-8982-18b5b19f2d04 | -13.6328 | -51.2604 | 2024-10-05 04:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d8dd588d-5056-356d-b2c9-f40c54b19b55 | -14.565 | -48.7995 | 2024-10-05 04:06:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 237fccd7-47db-3a4e-bdf3-1a322de27f23 | -16.5345 | -57.2259 | 2024-10-05 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 532168d4-34eb-38fd-b44a-dace2d154844 | -16.554 | -57.2237 | 2024-10-05 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.4 |
| db2cde17-d5df-37e5-a5da-91f80b49ccdd | -16.6402 | -55.5243 | 2024-10-05 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| fa0ae8c3-500c-30aa-ac61-23fa1128b454 | -16.6594 | -55.5427 | 2024-10-05 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |


[Clique aqui para ver as próximas entradas](README54.md)
