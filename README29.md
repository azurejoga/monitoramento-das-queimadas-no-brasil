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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5828063-9fdf-3e0b-a478-0057c72babde | -8.32674 | -54.75186 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce734fd1-f5e1-36c7-afcd-128c4fbbc9db | -9.23493 | -50.04293 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9938870-5d06-3a16-9bf3-0545cf2c7d5b | -6.5251 | -56.2017 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04dc23c1-1f6d-38ac-8310-326c58df518f | -9.39943 | -45.49681 | 2025-07-30 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 35de6f0e-3a2a-36f0-91a9-e0cce970c523 | -10.61126 | -45.24594 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a65f0c8-030a-32f5-9844-fd4f367e4d53 | -9.70556 | -48.21641 | 2025-07-30 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bdcc054-1f55-3799-bfe9-39b623411815 | -8.33012 | -54.75241 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d501269f-e86d-368a-93b9-0c6f25579a13 | -11.46832 | -45.11103 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6318f538-b439-392d-ae81-e14bf930ad41 | -6.53102 | -56.21155 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da5cae9c-298a-3dd6-9a4b-f19161d44a89 | -11.34367 | -51.255 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b465aa3-51d9-3acc-9886-f56e3f245e8c | -8.51479 | -43.31869 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 0eb0e460-2b96-35d8-9f43-4348a3c386b0 | -13.06791 | -47.38681 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec9800de-075c-3f10-8514-06ef89ab2060 | -7.78087 | -45.0054 | 2025-07-30 04:51:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83de4b43-ccb1-3c5b-a81e-d6fac59b40a6 | -7.93601 | -44.08521 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7416556f-ecd9-3d11-8bb3-15c3b060486f | -10.46458 | -46.73125 | 2025-07-30 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79b6e41f-5e37-3630-947b-172f54f3a3fa | -7.93556 | -44.08866 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0b22aca-04bf-3afc-8d4c-a5a161f5f8b8 | -6.50107 | -56.21095 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16dc0bb6-2ebc-3133-97f1-e7af5bde8674 | -6.96119 | -58.37727 | 2025-07-30 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b84eacaa-ec3a-32eb-b18d-c4c8dec9dae6 | -9.04348 | -45.07177 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cb8930-d7d4-36e1-a685-347a82df47c1 | -8.96109 | -46.73829 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55be32e1-69f4-35ca-b2e5-cf9c9cf2ea0f | -8.32615 | -54.7555 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1fdb4c8-8896-33b8-9f88-6b21c878ce21 | -8.3335 | -54.75298 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f6cc21d-2a4c-3c1a-8352-c2cf43d5eb69 | -14.09659 | -53.98024 | 2025-07-30 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcfb35d9-dfcd-3f0d-a07f-830c241779db | -6.55658 | -56.19248 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b0582fb-f04a-3144-aaa2-9f5af60097d1 | -6.53032 | -56.19247 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67da34a0-b5f6-3a18-b322-f29ff4b32358 | -9.14505 | -49.84617 | 2025-07-30 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e01418b0-0d47-3ecd-a69c-e6a2c7590dc7 | -12.5756 | -49.79762 | 2025-07-30 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 172a5459-f320-399a-8203-94220819a613 | -11.37617 | -48.99831 | 2025-07-30 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a16b2c4-1892-32a2-8e8d-3dbbad173ab9 | -6.54493 | -56.19489 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8401061-5acb-3ace-91e0-9fafed020bfe | -7.78167 | -44.99978 | 2025-07-30 04:51:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d45a6529-b026-3434-bccd-7ba38b4a070a | -8.62926 | -45.88099 | 2025-07-30 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d3860189-7671-3adc-bc13-af535989c607 | -13.08654 | -47.31315 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea53f15a-6c39-3f49-9657-a03a7d5293f9 | -6.54928 | -56.19125 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e434d89e-6458-3e89-a6df-c4ac68285d19 | -6.54421 | -56.1992 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dae83e5-5085-3ffe-8952-8bdd5d8b3b9c | -10.82165 | -49.37954 | 2025-07-30 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f059eabe-111b-3496-926f-362c637f91e0 | -6.52718 | -56.18882 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0de5d013-5a7f-3a32-8f35-75cc30bc9447 | -7.73775 | -51.09128 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ade7d689-63da-36e8-a427-a40a7d4928c8 | -6.54999 | -56.18699 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f77bfb-b9d5-3663-894e-42bd7a58df10 | -13.0875 | -52.13995 | 2025-07-30 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a148c0bd-edf6-3e5b-9271-c6b914f95729 | -12.62129 | -48.06082 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07ca271b-6ae5-3311-9bc6-eaedbeb9bfcc | -9.82954 | -41.49896 | 2025-07-30 04:51:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| efe79cf9-aed1-38eb-959a-b2e3ae11ac8c | -8.40664 | -50.11365 | 2025-07-30 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2863892-978d-3ab5-95d3-c70ea9409667 | -6.50247 | -56.20236 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f874f4e-82f8-33ed-a1c2-e337bcac2d6d | -12.81036 | -45.4393 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7ee2306-146e-304b-89b1-4b13b6a58eb4 | -11.46273 | -45.11361 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e1c9aa2f-03fd-3bc1-b1b6-61c4d4a98a8e | -6.56094 | -56.18881 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94c8c88d-2b04-3497-8bd2-3a22a19e71f7 | -6.48516 | -56.01175 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dab44322-6223-30af-900b-3633bed34151 | -7.94174 | -44.08261 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480cda74-0310-301b-acbf-01086e6605eb | -11.31352 | -49.9548 | 2025-07-30 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38bd4322-4289-35e8-bbde-277d33b42045 | -12.95121 | -48.25694 | 2025-07-30 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f15e0a43-120f-3770-96a9-554712a8202a | -12.4797 | -47.27626 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b629107-08b5-3048-9b7e-8b55c313fc2d | -10.61203 | -45.24004 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d4181a4e-0f3f-36e9-b072-a0f57b92594b | -9.20995 | -59.67275 | 2025-07-30 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 921e5234-b577-367a-9e6b-a053e4137e99 | -8.88558 | -47.34076 | 2025-07-30 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f573e80c-6c10-3e0b-a6ea-93291a3cc0eb | -12.57945 | -49.79819 | 2025-07-30 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cf5c7d1-10ea-31ff-9fe5-4e7724a731fb | -10.42705 | -47.25114 | 2025-07-30 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 523c549b-08e8-3def-8c09-2e766326b5d0 | -11.33719 | -51.24696 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f81e4be-f55f-3356-945a-463f60b490a4 | -12.7073 | -47.78975 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a130f4f7-c8d0-37b9-9e36-239d38c82021 | -10.62334 | -45.23259 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39ba76b2-a3a2-34a9-a272-903aa75f5e8a | -12.72973 | -47.0053 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f0fbd34-9261-3551-b51c-9799fca819ed | -11.91979 | -44.5432 | 2025-07-30 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f001ce40-068e-37be-81e2-eeb9c2ac2740 | -9.25964 | -50.23132 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 302ef79b-db3c-3459-baa5-a4d8405d29ab | -11.52238 | -54.68605 | 2025-07-30 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b42e9e6-6ce7-3bf1-af99-7119df7ccd27 | -9.17681 | -48.85034 | 2025-07-30 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d030dc20-7f2f-38f7-b21d-eb346dcaae0b | -9.55854 | -40.33354 | 2025-07-30 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 207768e0-30b4-3c1a-86ce-4ebe5f893f1d | -7.10167 | -63.04797 | 2025-07-30 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f41b01ce-5948-3a89-897d-d6b0a65aa93c | -8.67473 | -51.21494 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fb5468a-107e-3297-b4fb-59cada18e529 | -10.7114 | -48.85983 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73ca5589-7595-3c7e-aedc-31a2bff145a8 | -12.80959 | -45.44558 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cca1de8d-1f12-3a04-a08d-db540f40bcfc | -13.0879 | -47.30248 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7315aa7b-435c-3b80-bf8b-2ac7b257258e | -9.26325 | -50.23185 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f813f82-c4e5-3230-80c6-f3530d20c861 | -10.62255 | -45.23858 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bad1afe5-c3a6-3365-a0e7-3576b318ac58 | -6.54127 | -56.19428 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbdda54b-ba71-3406-adca-f0165e912e57 | -9.04269 | -45.07754 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1935f99a-bfd9-3307-ae04-382587b92405 | -6.96094 | -56.37648 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 953c460b-1765-36c0-bf3a-646d5cef348a | -9.23429 | -50.0472 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed69bf96-2a64-369f-bd2c-0747d45405b2 | -9.83594 | -41.49982 | 2025-07-30 04:51:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7fffb5c4-dc0f-30a4-a059-2b2219bfe7d4 | -8.95597 | -46.74221 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bef833ec-6b56-3c73-afa2-8ea89f1cc793 | -11.27805 | -52.46916 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc7e7bae-b4ca-3006-bfd4-e0816e963bd6 | -6.52672 | -56.21394 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 975314c1-cf73-3df1-b58f-24aaacb5f3f5 | -8.5163 | -43.30727 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 491b5269-d9b6-3d92-b84a-2e1d79bfa76f | -10.69876 | -48.86322 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8f87920-8107-3e58-8e05-889b1e2c2df7 | -7.00401 | -52.8835 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72b60ae5-fd75-3f3d-8c07-8ca99b7e6cf6 | -11.45715 | -45.11612 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8137c1a4-2c5d-3144-9d90-320d35ab03d5 | -9.6284 | -48.55138 | 2025-07-30 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 568e50e9-be83-3492-a6e6-582ac7ba185b | -6.50403 | -56.21585 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b72d571-15aa-3c78-a0bd-55fab99a94bf | -8.30741 | -55.1082 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e11b550-f32c-34a4-82f8-fc53293d8b61 | -11.46312 | -45.11049 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5310b947-558c-3f30-8688-aa558c3fe169 | -13.08235 | -47.30436 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b19f840c-f035-331e-8f07-421824326d66 | -6.48939 | -56.21344 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ec0bbc43-b681-3452-a196-4e6445643550 | -8.32277 | -54.75494 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca5e80e7-e091-3869-874f-7f5f9a679de9 | -11.27468 | -52.46863 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee8ad89b-26b4-37fb-89ae-80c58fcb3942 | -13.06252 | -47.38286 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 175d9a13-3d15-30be-a3cc-7fb7d78258f9 | -6.50022 | -56.19315 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33ae2ed3-9cb3-32ed-90a6-fed42c933986 | -11.34425 | -51.25102 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1338a30b-ba08-3147-be48-0a2f075caedc | -6.52816 | -56.20534 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42bfa6d3-b65b-3dbd-9fe3-1ab0b98f3d13 | -10.70742 | -48.85924 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d856d427-c964-30d8-958b-8433f906cc61 | -9.74084 | -48.5781 | 2025-07-30 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d15d45d-947f-32ee-a9e7-83ff39a7a1fc | -12.47579 | -47.27092 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba83bc89-f5ea-3e53-8d96-d1fd866ebf8d | -8.03795 | -46.91248 | 2025-07-30 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README30.md)
