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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb18ba3-6914-3971-86ff-cb986b1482bf | -10.56811 | -46.93158 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02367488-aabc-3e8d-9d76-4926d754db10 | -18.42165 | -54.87 | 2025-06-22 04:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bcf845f-6601-37f1-a19c-f63886eac3aa | -18.05897 | -44.49608 | 2025-06-22 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bde98361-658a-346a-9718-927fdae6ff91 | -19.73341 | -44.17269 | 2025-06-22 04:44:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb4d9959-c1c8-38d1-ab3c-33c9d0648f8e | -18.42235 | -54.86591 | 2025-06-22 04:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ebcada0-61f3-3959-89a7-aab3afcfaa40 | -22.95359 | -43.04401 | 2025-06-22 04:44:00 | NPP-375D | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f663ef06-69e0-36db-b25f-5fab013ef34c | -17.65931 | -46.84876 | 2025-06-22 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf27879b-de20-35a1-845e-b6abdec8a447 | -16.09587 | -49.05967 | 2025-06-22 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d6b68bbe-2342-37d2-adb6-d258b5ecfaa0 | -21.19414 | -44.93492 | 2025-06-22 04:44:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ad686b71-3a72-30f4-b778-b2a9c2ccc0af | -19.62168 | -43.8183 | 2025-06-22 04:44:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c7f7357-76ec-3ec6-86ea-d40443ffc4e7 | -17.6554 | -46.85184 | 2025-06-22 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869f961c-101b-3481-881e-3579e7542f08 | -18.05876 | -44.49487 | 2025-06-22 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ecaa79d-ac39-3b39-a39a-8f682bd9ac47 | -21.19485 | -44.93849 | 2025-06-22 04:44:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89230ea7-7a5f-3575-ad72-743e387c949f | -18.05957 | -44.49087 | 2025-06-22 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00105af1-672a-39e1-a87d-ebd86895ac12 | -19.62493 | -43.81882 | 2025-06-22 04:44:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 184af870-2474-3cfc-a182-88be9a983b46 | -19.6213 | -43.82162 | 2025-06-22 04:44:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e613f5-b118-308b-91bf-79d15ea648bc | -19.77855 | -47.94117 | 2025-06-22 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dff63bc-789c-33fb-b163-4e299b29d415 | -17.65589 | -46.84815 | 2025-06-22 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93f6a6bd-d6b1-3ff0-a403-37db170756da | -20.9959 | -51.7912 | 2025-06-22 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd5ee2a1-7228-3ee8-8ea7-4459e3f04b52 | -18.02048 | -43.06291 | 2025-06-22 04:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 570aae6d-a105-3511-a22e-f75e57a1afe6 | -15.07726 | -48.94641 | 2025-06-22 04:44:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a726ea8-a449-3a97-bef9-fb779383bc59 | -18.01529 | -43.06184 | 2025-06-22 04:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f16b687-95b1-3c8f-b5ba-5a9ee82c785a | -18.48895 | -45.07216 | 2025-06-22 04:44:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c1e6124-f0fc-3903-9486-09a9ebc3e25a | -17.65996 | -46.84872 | 2025-06-22 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d88a7f4f-8744-34ab-9ec6-53b09d1748f9 | -17.65525 | -46.84819 | 2025-06-22 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bce575d9-8fc3-3a55-9b22-8c9626ffadec | -19.61983 | -43.81821 | 2025-06-22 04:44:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0eb06305-9578-365c-b67a-f33e38e63633 | -20.85328 | -43.06265 | 2025-06-22 04:44:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0952d354-cd6f-37c7-b018-77cdb54a8e0c | -22.93328 | -47.16854 | 2025-06-22 04:44:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c234c52e-d82a-385d-b671-83494405bb11 | -23.33982 | -46.77304 | 2025-06-22 04:46:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f5a6d1c4-e93b-3005-a7c9-11a8d795f358 | -23.33542 | -46.77238 | 2025-06-22 04:46:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 50df5ab1-58c8-3299-91b1-d72f7a3553dd | -23.1191 | -46.91512 | 2025-06-22 04:46:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 935079ae-5388-3edd-a698-af56cb4b00e3 | -29.86664 | -51.16565 | 2025-06-22 04:46:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 253ab06b-a259-3d62-9bc9-a8162b2f94a2 | -29.86571 | -51.16392 | 2025-06-22 04:46:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 686691f2-45b5-3320-a402-7d3e5a3bcac6 | -30.48656 | -55.70417 | 2025-06-22 04:49:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.0 |
| 4609aa74-53d8-33a3-b100-2fee1a00b4bf | -30.48258 | -55.70748 | 2025-06-22 04:49:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.0 |
| 2e5cb479-329c-34f6-bbca-bfe8872be122 | 2.75343 | -60.36533 | 2025-06-22 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c9e1ec9-e125-386c-80a9-971897a4ef5a | 0.70077 | -51.44255 | 2025-06-22 04:59:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 346ec0c7-92ec-39ff-bd4d-b052b80b182a | 0.69434 | -51.44764 | 2025-06-22 04:59:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c51c3601-66e5-399d-a0de-470e7d88f7e3 | 0.69406 | -51.44641 | 2025-06-22 04:59:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 081fd2c6-e7f6-3130-bf29-31d1e1149790 | -8.0687 | -43.10523 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 71350016-0111-3b92-82d6-5d8cb686b799 | -3.60836 | -47.53902 | 2025-06-22 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9642ba5b-59c4-34e2-99ec-2f8f5078d111 | -4.54167 | -48.00937 | 2025-06-22 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d08327c4-c947-3e25-b9a0-d784fe50f119 | -8.09731 | -43.15346 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f8f10d5a-b120-3788-9767-f449b1391f93 | -6.8706 | -47.23895 | 2025-06-22 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c992f74f-32c7-3b7b-91b7-8481e9d161c5 | -8.11255 | -43.14286 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 62b3da79-2e8b-3290-a18e-1be36d110baf | -3.6124 | -47.54498 | 2025-06-22 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdef5368-c359-3d64-9c4e-922bca39862c | -8.06682 | -43.10945 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b89e4c0d-7d99-3bd9-99a0-9a2fd485c6a0 | -8.09049 | -43.15257 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 499585c6-0446-34c8-b2ae-bc3b07be0485 | -4.53696 | -48.00853 | 2025-06-22 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 439d555c-1089-3e00-9ed5-c7bcd1f328f6 | -8.0981 | -43.14727 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7ff3ff85-aa54-3ffa-a40c-559b70b26489 | -6.38233 | -56.70476 | 2025-06-22 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b14b30f-e479-38bf-a6ce-6811cb18e30c | -8.08368 | -43.1516 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87686724-c0a0-3eb8-855a-9b1f63066a12 | -3.61318 | -47.53971 | 2025-06-22 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 772b9e28-68bb-32ec-b7ce-5f15769027fc | -7.90047 | -46.23218 | 2025-06-22 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49225feb-d5cf-3571-868b-31ea048c70a3 | -8.11175 | -43.14908 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f0a89f6e-9d0d-3817-87fd-9e6ae392b958 | -8.06765 | -43.10314 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c133060f-13e7-3e02-ade6-b97036f74042 | -8.07366 | -43.11025 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bd578bc5-6bbd-3977-8565-a110693a7b38 | -8.10493 | -43.14816 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b3bc6e91-d195-30c7-9389-d5f7fa69748a | -4.54564 | -48.01522 | 2025-06-22 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2d07d5-2f49-3a9a-966b-1914ecfdbe02 | -6.87103 | -47.2358 | 2025-06-22 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b49a01-4117-34af-abda-6b04d1e1fb87 | -4.54092 | -48.01446 | 2025-06-22 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef7fb86d-9d54-3eb5-81cf-6aa35e3ebf1c | -6.52884 | -55.0207 | 2025-06-22 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 528141cb-cf1c-329c-94e8-9e25fe9d3fea | -5.00869 | -56.17451 | 2025-06-22 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f5446ec-4922-399d-af69-266f2c9e8b36 | -5.57477 | -45.21664 | 2025-06-22 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d45ad88-9963-3270-a9e2-0dd1fec182a6 | -5.32377 | -55.94407 | 2025-06-22 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 148315ac-84bc-3f5e-af36-f119387fdacd | -4.6417 | -47.9629 | 2025-06-22 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 908d0385-88c1-3495-a728-e27a997d6437 | -8.07688 | -43.15056 | 2025-06-22 05:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f37c56a3-cd24-388f-9778-a1d410073b32 | -13.80279 | -54.29312 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ac9fa1dd-00b1-3276-9060-b628db74d3be | -11.84127 | -57.76016 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e104e65c-cbc3-31b8-aa41-3f8434205597 | -12.02978 | -57.0866 | 2025-06-22 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be97acc2-ba92-3261-8409-fb9e5ec01a47 | -9.0974 | -50.02459 | 2025-06-22 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cba6178-9468-3564-8a2a-127344efbd17 | -9.46692 | -57.83827 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70af103-b32b-3b83-baa8-c7dc4f7d9ac0 | -11.78738 | -57.2449 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3505e6f-de3c-31e8-a42e-83efaf4b9625 | -9.47644 | -57.33133 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02dc3ed2-d2f7-3e49-8897-e129b3cd0441 | -10.95806 | -49.57239 | 2025-06-22 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fee7985-b5bf-3d3e-a3e7-4c2394d37f8c | -11.61897 | -58.2928 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55e2be9f-9784-37d2-adc4-a1cd26255fbd | -11.42584 | -54.32549 | 2025-06-22 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0c67d85-9c09-3264-adb7-3799df3a234a | -8.41898 | -48.29846 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93d66736-131c-34e5-9b21-7f9d78799d97 | -11.74476 | -54.71223 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7393313-165d-3e73-8346-d783742882dc | -9.8637 | -60.28685 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f1f6871-3d8b-35bd-96f2-38c61c3c22e7 | -11.6162 | -58.28862 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 54779e3d-3253-3df2-98b0-b5071e407b8b | -13.79134 | -54.29577 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a75e7343-951a-307c-9903-4c8cbadf7046 | -11.09631 | -46.6785 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3902d633-091b-307f-aaaf-a8068e24ef96 | -10.45728 | -47.02085 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67af892c-0c54-3e53-96a1-0197eaa730de | -10.60611 | -52.83807 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18912e69-54d8-36ff-af37-331d77036acc | -11.10861 | -46.67281 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bdc75ac-ce62-31b6-8613-37ac36dccb1f | -11.62015 | -58.28554 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b9b768a8-a686-352c-9525-0f4812491e9c | -9.46356 | -57.83772 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9cfda19-81e3-32d2-bb04-c7150d4e080f | -11.10299 | -46.67149 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84124503-ebfa-3251-8d50-386d90aa8527 | -10.85627 | -53.76006 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0aae294-0422-356f-88ff-05b1d7cd8c0d | -9.17175 | -61.40528 | 2025-06-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| a632cffa-9ac8-3b29-8588-c7767ea7a587 | -11.18302 | -54.4034 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b568a301-1fdb-3753-9a33-6fda075d30a2 | -8.59561 | -51.58599 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 05864723-2362-3168-8aa6-7abb023c2f3c | -10.74677 | -52.50918 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ec5c85-74f8-35b4-8a92-014008d8b1d6 | -11.62686 | -58.28666 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb5a01f-a6ee-3468-a7a7-dd5d86332765 | -11.56981 | -52.09868 | 2025-06-22 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d78657a7-92c9-30ca-a913-97d8610759df | -9.464 | -56.05825 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 43181890-ee70-3e79-b046-7734c06146f5 | -9.47596 | -57.82496 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7db2d1a8-1f23-3319-8420-5bebbbcb2bfd | -10.02756 | -54.32037 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309e8701-e1de-3ddb-8df3-c2c1b93565f4 | -9.25466 | -57.52783 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
