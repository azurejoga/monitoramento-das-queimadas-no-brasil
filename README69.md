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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d2715da-80c3-38ba-bca5-7e7fbf1173c0 | -7.12677 | -43.6895 | 2025-08-27 05:38:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3a397007-6612-3d9b-b979-22422dfb011c | -6.17594 | -44.042 | 2025-08-27 05:38:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7dc03b4-1ece-363e-8eb2-9c451a675751 | -7.6429 | -42.66523 | 2025-08-27 05:38:00 | AQUA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7ee46b5d-8545-38e5-928b-beaeec67b668 | -7.64026 | -42.68282 | 2025-08-27 05:38:00 | AQUA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 84abd18c-7dc9-3821-87d4-534056fbd0fb | -6.22619 | -43.35347 | 2025-08-27 05:38:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 76c4426b-9950-3280-b04e-e0122bca5f83 | -9.4064 | -60.5133 | 2025-08-27 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6d8c1d1c-c5b3-32a6-935d-2d7adaff23b0 | -10.0977 | -62.9085 | 2025-08-27 05:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 39c1a7e1-750a-3a9d-ae7f-7ccb67926da1 | -9.4062 | -60.5326 | 2025-08-27 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 5c4cd961-1d40-3bcc-9e49-28c0719397d5 | -13.06719 | -46.32392 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1f51cd2b-717e-3b36-a9d1-fac8e97ac30a | -11.24325 | -44.99376 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7be38a34-6a4f-33f6-a236-77fdb21be2d9 | -11.8145 | -46.8178 | 2025-08-27 05:40:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 197f2744-f28d-3192-bac4-a17d4c998a23 | -13.37595 | -46.88394 | 2025-08-27 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e5ab4c35-4574-3e5b-b04a-83fb9234ccd8 | -11.81635 | -46.80637 | 2025-08-27 05:40:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f22c5c08-23f7-34ce-b621-7ae3518b1fd4 | -12.74995 | -48.07986 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 408d2d14-786b-3ae3-ade3-309f2ed779c6 | -9.94345 | -46.37025 | 2025-08-27 05:40:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6f96ab23-f175-3fc5-b905-f146deaecd39 | -14.4035 | -51.92765 | 2025-08-27 05:40:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| fb710406-6c2e-364f-bd3e-cce664274d90 | -10.32146 | -46.77113 | 2025-08-27 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 81a28dec-cf77-3e9f-8870-0a12d873f74f | -12.89844 | -44.63979 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d298baf0-ed53-3c62-9eca-259c239500fc | -15.08957 | -48.63035 | 2025-08-27 05:40:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5018588a-b0ed-3ffa-b6f1-ea80594f0678 | -10.79556 | -47.08026 | 2025-08-27 05:40:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e7bb2f26-7530-3891-a1d3-73f8e0384442 | -10.78734 | -47.06612 | 2025-08-27 05:40:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3f31731b-8133-32fe-9665-cf4e4d3abf94 | -11.32809 | -43.29063 | 2025-08-27 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c421672-c162-32f8-ad10-533f50037665 | -11.03622 | -45.13369 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a58114bf-31fd-35cb-bb11-a5d8a3954a85 | -12.9045 | -44.65936 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a2cdc712-cfd4-30ac-95cf-7409f8cf0af9 | -9.95316 | -46.50044 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6cdff797-4a88-3771-bdac-0d6ed64af500 | -16.73613 | -47.58514 | 2025-08-27 05:40:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| be4471bb-04ef-3bd0-9b99-d0c7388b463a | -12.93093 | -46.3211 | 2025-08-27 05:40:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef6d5371-84c0-3790-aa05-106648e1dd3b | -10.79752 | -47.06796 | 2025-08-27 05:40:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 658802c7-b59a-38f5-8cc8-a2fc75b2e4ea | -12.95236 | -44.58322 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 73e6ec39-c7e5-302c-a257-1f046ac3e8f8 | -13.37411 | -46.89528 | 2025-08-27 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c1c9f48a-9430-3cd8-8ea5-ce842e98966b | -10.78536 | -47.07844 | 2025-08-27 05:40:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 5a7d9c2d-572f-3d42-bdf4-a15aa4d1b4e3 | -11.25671 | -44.96684 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8415365f-df37-37ff-a8ed-2a24af161d3f | -13.16857 | -45.28441 | 2025-08-27 05:40:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| afa0e65a-5301-3091-bc1b-c0be87e34a00 | -12.7393 | -48.07821 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e97a9600-ce39-35f3-a2e7-99c03abd8c3f | -11.13084 | -46.34472 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 13429c59-3f01-3f33-be72-84cdb8082b8b | -13.97953 | -46.34645 | 2025-08-27 05:40:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e137e1e9-0f5f-3a60-a88c-93a2b3e21617 | -12.8041 | -48.10854 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a4063a3e-dc19-383e-b15e-7bddd64398c5 | -17.77151 | -44.48435 | 2025-08-27 05:40:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef2a29d2-2ed8-35a1-8a83-a7627087d139 | -11.1326 | -46.33381 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 385be9c0-a23a-3e46-8b61-48bd01cd5ff6 | -13.07067 | -46.30239 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2aeb67a-451f-3eb2-a0e4-d4c1243b9545 | -13.06889 | -46.31339 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 07a6e154-f233-3ca4-99b1-d3123b9f6a3c | -14.41111 | -51.92411 | 2025-08-27 05:40:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8e0c9626-d699-37e6-9b29-f5ddc87eb649 | -13.06549 | -46.33438 | 2025-08-27 05:40:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d6a882d5-545a-3b10-9791-83d1b531533d | -15.08641 | -48.6226 | 2025-08-27 05:40:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| af494a26-44e3-3d5d-a0c3-976140c5c3b8 | -12.87711 | -48.09952 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a9ba40a8-d2ab-38c2-9bad-f800ac585d1e | -13.44413 | -46.85533 | 2025-08-27 05:40:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 28a3c89d-1630-3848-ba40-0811eab2adf9 | -12.79346 | -48.10675 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5430d249-40f7-3699-96cd-2cecc2d412dd | -14.13024 | -45.40182 | 2025-08-27 05:40:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53ed4ed5-2b74-38b5-9937-87e5a6241f67 | -16.73776 | -47.59217 | 2025-08-27 05:40:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c81a4c24-4618-3f53-a4e1-289b503f6014 | -12.78283 | -48.10498 | 2025-08-27 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e9cdc7ca-bca6-35df-9bab-e98e91a7e312 | -17.77287 | -44.47515 | 2025-08-27 05:40:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5dcb8c95-d962-3ddd-81af-797484573465 | -16.73434 | -47.59625 | 2025-08-27 05:40:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 85ba516e-d467-3453-a1dd-7be33359dc03 | -11.25522 | -44.97635 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61fee000-e223-3cce-bc49-c96161a3d0f5 | -11.0347 | -45.14334 | 2025-08-27 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82ae6c06-58e5-387a-a1f1-c9ffaa129cda | -21.13615 | -45.88498 | 2025-08-27 05:42:00 | AQUA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 41403a0e-8ddf-3879-acfa-0f9896bd53bc | -21.57973 | -47.4918 | 2025-08-27 05:42:00 | AQUA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 65287fdf-c1be-3b91-bdd0-030265766bf4 | -21.42771 | -45.49005 | 2025-08-27 05:42:00 | AQUA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 1b87c5a1-d2d6-3567-95af-6c63c99eeefc | -20.67503 | -47.53532 | 2025-08-27 05:42:00 | AQUA_M-M | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9b8b508e-e751-335a-9bb4-66e9dfa651db | -21.4291 | -45.48066 | 2025-08-27 05:42:00 | AQUA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| f2d7d62c-79d8-33fe-8c8f-0ef6c3321b3b | -20.75902 | -44.75288 | 2025-08-27 05:42:00 | AQUA_M-M | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| c254b7fc-bbd9-30be-a919-933fbed8bafc | -21.58136 | -47.48173 | 2025-08-27 05:42:00 | AQUA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 608b9112-1b72-391f-b71b-2d461a6514ff | -1.42418 | -60.4008 | 2025-08-27 05:42:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef955aa5-bae8-36ff-beb4-79cabb870a72 | -6.70014 | -58.55941 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5699299-ab50-3373-a828-7908b7ff95ce | -6.81495 | -58.95927 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bda0579a-d3f2-37e1-bea8-30d045827914 | -4.96056 | -55.81514 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 155ad768-c1c6-3c75-9426-01e4a722eca2 | -4.55979 | -55.95909 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc67ba62-a2ba-3ae9-84d6-89b5618b234e | -7.25709 | -57.6741 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed2b72d4-df10-3a85-8a11-de477b17410e | -9.18939 | -60.80133 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1b662255-855f-3138-a98f-2778be7dbc01 | -8.88438 | -60.76408 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a0b2e90-bae1-3224-88d7-ff33a4c14a67 | -6.62705 | -58.55289 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df104767-206c-376c-8404-772c236a9ae3 | -6.90808 | -59.35991 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b11cd5d1-f3b7-3a41-9d1f-efa4de85e8ae | -5.7609 | -53.7711 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e32d0d21-1f24-3f27-9fdc-6aad62948927 | -6.83702 | -58.96258 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 37d8af2b-534e-3ced-9737-2451f2de696f | -8.88841 | -60.76466 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b399f508-b96e-32b6-a31a-69b1bd6c150b | -6.68925 | -58.54589 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a048b00f-9aa1-3182-a2d7-17834d6e15d1 | -6.30926 | -59.89283 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a9e1ac2-52f1-3c65-a83e-ab8473f9c7ec | -9.20515 | -59.44151 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e26d22-fa24-3dea-bb82-7fe7812db574 | -9.59137 | -55.38372 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90828971-8bc1-3695-8caa-d1b050b8bfe5 | -8.96662 | -63.38531 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f905bb09-ac18-3bda-84d4-2a76be30809a | -8.60983 | -64.07664 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c10c4542-b6da-326b-9339-612739efe2ab | -9.18501 | -59.45644 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4e9887b-e419-381b-955e-d3bd0505d29e | -6.24781 | -60.00393 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feb15c63-56b3-3394-b104-89fedef3c266 | -6.87531 | -59.8986 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc27e7c6-eded-3e61-81c2-8a20f109cd25 | -4.1173 | -56.3435 | 2025-08-27 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e014197-e876-36cb-96e5-a7d5b611f70a | -7.47915 | -61.35801 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3ecd9b3-d8a4-3b25-929d-bbed1bf2d80e | -8.61289 | -62.65032 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e414d8b1-99be-3cad-bfb3-c268c82e68cd | -6.90934 | -59.36258 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d15397-76ea-3f63-b78d-627967e64d1a | -8.34673 | -62.93751 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d087f851-9195-3d9c-a387-bac38b1ddedb | -7.169 | -59.74276 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a43618-af7d-3637-863b-abb1b20c9d32 | -7.36487 | -70.14311 | 2025-08-27 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ec39b7d-e3bc-3e59-a4d9-518409953ef3 | -9.39989 | -62.4864 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890826b3-3590-30ad-9360-aa69feb69a90 | -8.25356 | -61.46099 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d9fda44-692b-3c1f-98f5-36e0c6a2b2bc | -8.33904 | -62.94043 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8fb4997-d06c-3ece-9cf9-6b8f37d3b6a7 | -7.56045 | -63.84709 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82dfb0ce-5224-3d71-b136-6090584bf14c | -5.7599 | -53.76712 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2379715f-064a-379f-ae85-4ba00e468e5a | -8.95439 | -63.37148 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ca90090-8bf9-3eeb-a4bd-8ffbd8c48857 | -9.18889 | -60.80488 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5bd1b617-f79e-36f4-9129-54eed34bfeb9 | -9.27372 | -56.90641 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c1d9440-6810-32fd-adf3-f6e389f045f5 | -8.8878 | -62.47795 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d812023a-8cee-3b26-910e-4cd55f8a985b | -7.16958 | -59.73884 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README70.md)
