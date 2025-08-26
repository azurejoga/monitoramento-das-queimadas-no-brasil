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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 027bbfe0-31a7-3eb3-9f98-856151cfcde8 | -9.23428 | -60.81975 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed45e2aa-8fd8-3532-93c7-68867ee5c841 | -8.33359 | -50.57207 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0754a182-abe1-31fb-bac4-cee74ecf1b11 | -15.57121 | -43.8606 | 2025-08-26 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfc69469-2f58-368e-bfcf-76f2f9196469 | -12.6682 | -47.86653 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c519bbe-2e9d-38e5-8c8c-fb811242c06a | -14.34463 | -51.94778 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 45f36b35-82c9-3f78-904d-1e0c6ceea398 | -9.16622 | -60.77624 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc1856c1-5cd6-3bd7-bf93-efc03569a31e | -12.7017 | -47.88436 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8e00eaa-48e6-3a5f-b35e-d8ba3fb83014 | -9.19784 | -59.51088 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82dc0810-a61c-3b3a-8ea4-13336126bab5 | -10.10067 | -57.76585 | 2025-08-26 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f0e49a1-2f30-38d1-9297-69338700bf5d | -8.54944 | -62.62515 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0773eb2c-5235-3a2a-825b-b1cb037c5ec5 | -13.45182 | -46.99229 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57338b89-27a1-3f0d-95c0-82d8ab526196 | -9.27036 | -56.91066 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3864d92-15fb-3424-bb2e-3c724224805d | -6.76788 | -59.66991 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 66904f98-b5af-3667-86ed-4f99139e34b5 | -12.93463 | -46.31917 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b666672b-c32e-3a59-a04e-7724d664b8f0 | -9.1834 | -59.50812 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c89d520-3c2b-3c28-849a-8a0a9da7cc1b | -9.85119 | -46.46231 | 2025-08-26 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a75903d1-a960-3125-8772-8ef949b2682a | -14.3312 | -48.64457 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fabea76c-12d6-3d0d-8c6d-b466fee67553 | -12.44352 | -48.71203 | 2025-08-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dfbc353-2f1d-308b-8926-7ad1fa2cf4d4 | -14.4792 | -51.94997 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2675fa2-db46-37e9-984a-994ccd263ec8 | -9.234 | -60.91179 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c6d65bd-fafa-3eed-9c61-e64b78010ea7 | -8.98651 | -65.43379 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d6ec81c-c714-3000-afc0-2e414fdd803f | -14.9729 | -52.88244 | 2025-08-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f95923b4-04de-32be-b3e6-3331cccf49c2 | -9.18539 | -59.44278 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62ae152c-6346-32a9-b49e-c0ffa008a4e6 | -11.54526 | -51.91983 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69763210-f898-3921-939f-67fba3c3c0ad | -11.54195 | -51.91929 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b619dc0-11ef-3abf-a3ae-a9e1a513fa07 | -11.44555 | -47.29853 | 2025-08-26 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d63ced2b-05e0-37ff-aae2-c331a5bc880d | -9.2387 | -60.91605 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f47f1f44-bb68-34dc-a431-1e38772e0055 | -15.02328 | -48.16596 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f56fe00-2e80-3207-84c4-7faae4f2015d | -11.56138 | -52.09882 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd990f00-b1f1-3de5-81ea-2c235152622a | -11.54157 | -50.45532 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb5117d-af72-3870-bc7c-5f39313d1ed7 | -7.38618 | -64.36073 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3107016b-7e51-3ae0-aac7-dab9166e848a | -12.73637 | -48.15659 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17924ceb-0036-3622-b843-8190741511fd | -10.94218 | -55.30793 | 2025-08-26 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15bf8077-92fa-3a71-a27a-4589b6b857d9 | -11.14855 | -44.76137 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de2ca932-f449-3840-b95d-aa28164cfdc7 | -12.67284 | -47.86206 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cfd92b1d-7a1f-340d-88a2-3bae706be067 | -13.43444 | -47.01857 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3edd0823-efe0-36d9-a07f-07daba51bb9d | -12.70492 | -47.89 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18a47831-1cc9-3d7d-83da-37e60650d23e | -6.87763 | -59.89851 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11f69e87-c3a4-3547-a6b5-a00f8bc8ed76 | -10.76952 | -47.06615 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 909aa8fd-85dd-30b2-84fb-992297ce5cfe | -9.15823 | -59.5367 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a43f514b-af48-3935-a0e9-231e7a0e4bc0 | -11.15877 | -44.76913 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 3c22d919-87c6-30c4-9abd-b19f219bff1a | -7.37271 | -64.35803 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50c3c46e-324e-3648-a893-c2674c768083 | -13.0607 | -46.31226 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b70856a6-2268-342f-8c0d-922a031fd0a5 | -13.05196 | -46.31111 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5cd8008-8e12-3fc3-a73f-9bdb6474e1c4 | -15.08363 | -48.54868 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69b836b2-4ee3-3463-ad1d-2b5905273bde | -11.54096 | -52.12072 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 70677401-28ab-33b9-8e99-3b192751619b | -11.06025 | -52.00394 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76b401a1-482b-38e2-9fd5-ec981e7cdec7 | -10.87623 | -55.7911 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9064dc50-9117-3e03-b57a-6c7042cb1a1b | -9.16796 | -59.51086 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7a6ef6b-cd89-3c3f-ae07-7dffcf2a097d | -11.16076 | -44.75362 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 4e079699-3e12-31a8-ad93-e5595c865bc1 | -9.40868 | -48.24564 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 898307d7-672b-3b9d-b2ca-cb1726e6c2db | -8.10425 | -62.87593 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 653e9d35-0e10-3dcb-b36e-381f746f094d | -9.05721 | -49.5578 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5365dd6-b4cd-3198-acbd-da2cb7ed3e7b | -11.61708 | -46.22551 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed4bf64c-41f5-37c1-a309-4bb0ef17d673 | -12.67243 | -47.86432 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 039489d9-064b-3f9b-86e0-f7c52884aef8 | -14.2442 | -53.04627 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c8d8292-f87b-313f-a50d-89e14dace6f3 | -9.15331 | -60.78717 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6fa8c80-55e1-3e92-be51-76fbc4a2f3df | -10.59531 | -54.88831 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7fd1750-680b-37e9-837c-bb7b59fec119 | -11.30012 | -55.11795 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f24053e-5bff-3699-bc2b-64a50822e007 | -6.83874 | -59.35891 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f444845-6525-357d-9b56-410b4b55d746 | -7.64639 | -61.46381 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d78b39fa-c2f0-3f52-8563-30541387c97e | -9.00035 | -65.40145 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95859729-a756-3365-8bac-611d2849b672 | -10.76552 | -47.06545 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e395685-4208-3881-94a6-eae3d228c566 | -9.23163 | -60.92493 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 210f91fc-fe53-3163-847d-1a5402b6cc04 | -8.84471 | -62.45786 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3229abc9-405c-3cff-b94c-e61b19dacc28 | -8.86547 | -52.05168 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8267a4fe-9e8f-32bc-8d2f-a68c9fc1d0ad | -9.16577 | -59.5311 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aeab96d-dd66-3e52-a5be-77c8863dda8a | -8.55291 | -62.63971 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f944acd-c0f2-36b0-abfe-32af51242cdb | -9.19007 | -60.79404 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169abde7-f46c-35f8-aca9-ea89c898168b | -13.58441 | -48.20287 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 78908815-146b-361a-bd0e-ca7606b7e033 | -8.86436 | -62.43971 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba032359-dde1-3256-8998-0742a376612b | -11.54151 | -52.11721 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0798743b-7265-3d1f-94c0-f21e0f7b1919 | -14.34797 | -51.94832 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16ecbe0a-0fe8-3743-ac54-9a057a03255c | -6.75907 | -62.87594 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc5889ac-a474-39c6-b9ae-299d316fe60e | -14.40063 | -53.28021 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 994451ba-bd94-338a-a98e-cedc237cce8a | -9.27165 | -49.62075 | 2025-08-26 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbf9116f-58b4-3fff-8ecf-191df09d1f0b | -8.85183 | -62.44166 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 655691bf-0371-35a3-928d-08b023468523 | -6.82052 | -58.96283 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2bce7a62-685f-3899-a949-91df866da239 | -11.51833 | -52.13506 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e517cb74-33d9-38f9-b9c7-6fc009847d5e | -10.42002 | -64.38721 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4b9ee6c-d954-3163-ba35-f5b26adc8347 | -13.44763 | -46.99161 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1dc6b25-2415-3f4c-88ad-7119d23827f0 | -9.16859 | -59.51501 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 11b8df46-80dd-3abe-8c00-46de8d47e383 | -11.15944 | -44.76393 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| fea0f547-b462-3a45-8774-b06e7650aa8c | -8.98312 | -65.42433 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c65e162-1564-3a41-aaa2-5a5f4145b8e6 | -8.85932 | -62.43428 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 74f14b08-6891-3346-ab52-aba2c78e8ff1 | -9.04915 | -49.56433 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447c0ac1-58ee-30b3-a688-6ea9d4831361 | -8.97346 | -65.43645 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f9b09d29-b109-3e5f-ae87-59affb80928f | -7.47929 | -61.35793 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bd76eed-19e4-3f82-9a81-718860be2a41 | -9.16128 | -60.77678 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e613b85-1151-3aa8-a3c0-03a51a613c69 | -7.35598 | -59.66629 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d174686-3306-3b73-922e-87c8f950080a | -11.04811 | -52.01636 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a90ef0bf-8537-346d-ac81-5aa28089be82 | -11.55696 | -52.12691 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 668f276f-dc2e-3bf5-a2d1-e7744d64748d | -11.55089 | -52.12233 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9b2bc5a-c928-3eb1-9216-a9005cd40d7f | -9.80082 | -64.26112 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 601bb29a-9d18-385a-8a11-3a66dab34eb3 | -9.26752 | -56.90284 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47404a23-6165-30ae-a716-8b84105fffe8 | -8.11072 | -62.87415 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46d076c6-a7f7-37f4-81a1-4ea7b20cb6d9 | -8.11036 | -62.87712 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f94e00d-0783-3d86-95a0-887ab83d9ed0 | -9.16107 | -59.55788 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| c8eafabf-58c8-364d-87d6-9af11f85a09b | -8.55722 | -62.64977 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70564165-aa25-3c70-b358-855cc4f1baa9 | -9.64884 | -59.63354 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README63.md)
