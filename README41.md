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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fe7bb8c-245c-3198-a8bd-7adc086595d3 | -5.21777 | -44.49018 | 2025-09-26 05:01:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20617510-e232-3df8-b35c-6046c76d6dc5 | -5.73934 | -44.95705 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7004f244-3bcc-3b96-af74-ca7dce29d8e5 | -3.32311 | -48.70754 | 2025-09-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a60ea65a-9593-369f-aa6e-66a3d11e1bdf | -6.85436 | -43.19182 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a24c707c-cf87-3ede-a2de-2ace777aeb5b | -5.74732 | -44.97377 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 174fc7d9-2794-3324-a4e0-45461dbe5b0f | -3.05699 | -48.71206 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c88756c-34a3-3904-bef6-1ff2eb5a010a | -5.62663 | -43.93467 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 201ad89d-9b98-314e-aa26-9b8410c7e923 | -5.69244 | -44.44879 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df954882-5ed6-3afc-b8fc-478c8f92e511 | -4.78971 | -42.75026 | 2025-09-26 05:01:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7515f75-b452-3308-8c22-bb5ed1bb622f | -2.69307 | -54.94882 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee741761-3e5c-3fa2-9e4c-bf7cff8ce2ca | -3.68681 | -49.04295 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ada7c24-12f2-35da-a083-eb9dc817b50c | -5.73751 | -44.96993 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c0361702-7f15-3166-a34e-aebfc9bcfece | -4.78958 | -42.8201 | 2025-09-26 05:01:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 062558be-284a-38d3-bb32-1ebcf4530b48 | -6.95981 | -43.24226 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 129d1fbd-bedd-399b-b500-053829bd0c00 | -5.628 | -43.9248 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e6c45ee-de0e-32ef-a670-b29282f601ee | -5.48232 | -50.12974 | 2025-09-26 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9744eb0-4084-3286-bb8c-7ec38354dc69 | -2.9244 | -48.30605 | 2025-09-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d9f7741-230c-3094-a002-86a858daac93 | -7.11582 | -43.74556 | 2025-09-26 05:01:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5b70340-eaca-347b-8ede-f50b3213fe89 | -5.63992 | -43.93108 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 294f7797-147d-3a96-ab64-b7a0d91dd707 | -5.5283 | -43.87677 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 68f93c85-b3e4-3fa4-9d3a-fd26ea48c42f | 1.009 | -59.51112 | 2025-09-26 05:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20813971-06ec-37b9-8051-9ee58e1a31e4 | -2.95816 | -48.59375 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e75796-73d6-330e-bc5b-ead2aef92002 | -2.19127 | -54.46836 | 2025-09-26 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457d07d0-9723-3b4a-afa8-f78aa55db248 | -5.74789 | -44.96962 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| b338c3f8-6523-3260-be80-8e1f20c35acf | -5.63293 | -43.93537 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6dbe89ca-b6ac-372a-b507-a36633438a08 | -5.73633 | -44.97821 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| b76c765b-341d-3470-8781-9701ab7169db | -3.64291 | -48.32273 | 2025-09-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24ab6cc7-56f8-3bda-b4df-b32a8ee5ea2c | -5.12158 | -45.50097 | 2025-09-26 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80db1a52-d771-3453-9dcc-fd00d69c72ef | -5.46706 | -43.06697 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9271cb1c-43d3-373d-94e1-ecb9f71934a2 | -5.42925 | -45.13778 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de9234fc-06b9-37d3-a141-fd21f389c74a | -6.26001 | -42.49467 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f0d3412d-f1f8-328e-b133-108439198e4a | -5.73286 | -44.96043 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a1cc1058-9e72-3477-b3cf-266b62dbe54e | -3.63501 | -49.16668 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efcdc969-f954-3112-8bb7-8da5790c98bc | -5.73977 | -44.98526 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 298f8f89-2161-3bf7-afc4-5d3bddab0b22 | -5.46159 | -43.06976 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2106e144-5ad9-34ad-9722-5fb782ea2da1 | -5.73907 | -44.91664 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de55eb96-0d11-3a8f-a4d5-20fd2dd630ca | -5.74088 | -44.9771 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4b612c19-6b45-3634-b5a3-711ac8ed8147 | -4.16902 | -44.27677 | 2025-09-26 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bb79e60-f839-3bff-ac8b-17730c838bd1 | -4.7957 | -43.04683 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52ef3e60-4740-3445-b9b4-9aecd5e45f0a | -3.80965 | -41.56332 | 2025-09-26 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d3be8f86-72b0-3398-b79a-65a3776c64cd | -7.27087 | -42.9824 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb126065-ef64-3323-bed5-d37ef537ed9f | -4.79716 | -42.74554 | 2025-09-26 05:01:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af57a371-afbb-3bfa-868a-88f28008b241 | -5.22777 | -46.09185 | 2025-09-26 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fb599f9-6735-3a4d-8916-08ed41fea564 | -5.73575 | -44.98228 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| d9ca9543-a929-3ee9-b8e9-8c0cc183ba53 | -5.46321 | -43.05819 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6ed5d8a2-ed10-32c9-ae12-2d7a5f158c33 | -5.75734 | -44.91526 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 595ea747-5416-3aa9-9f35-e183d6cc4775 | -3.63562 | -49.16269 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f16c417-730f-36f9-a9be-5cc9c94c6444 | -4.48442 | -47.68275 | 2025-09-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5213304a-928a-3ff7-9b13-a2f220a47c2f | -5.74165 | -44.983 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70ebffb0-faeb-3d8d-9ad6-4dc86ba1162a | -5.7434 | -44.97072 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ce94bfc7-89f4-3936-bb2d-8f12c095828d | -4.48118 | -47.67151 | 2025-09-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5409727-af78-38ab-b369-5f58eb0e1753 | -5.96939 | -44.12579 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce801504-e8c4-377b-ab32-be997db369a7 | -4.81427 | -45.64372 | 2025-09-26 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93b029f6-61fb-34a5-a348-916776012486 | -3.81605 | -50.79456 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c44ce1d-1f64-3c4f-a9a7-d931f74b4484 | -6.87893 | -44.5037 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebe4ea86-0237-3e5d-a2d9-986b339e965c | -3.33341 | -50.2041 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5819340c-2ea2-354a-857c-12844710cfe8 | -5.7562 | -44.92319 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47fb83f9-bce6-30c7-87c1-27cf29bf7592 | -5.74107 | -44.98705 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c1d43686-c706-3904-86b6-d42c378ba702 | -1.08951 | -54.10901 | 2025-09-26 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2ef6f47-4923-3083-8210-78a85b5a54bb | -5.74401 | -44.96646 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 2f3d5f07-5aeb-362d-86bb-af5b80c0d2db | -3.84985 | -50.972 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67be161-e219-314a-903a-41888c13f851 | -6.25492 | -42.48025 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 773b3e11-01f6-39fe-b500-f03d9b09982f | -2.79404 | -49.59766 | 2025-09-26 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fead5bc9-6585-313e-a90c-d82ea8e4d038 | -1.34409 | -54.64822 | 2025-09-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec3a7a4a-85ff-310c-bc30-23fd61512166 | -3.63801 | -49.16485 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c63b1c-2156-3873-9f44-994548cb98e7 | -4.75041 | -43.27491 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaa21a66-06ae-37a0-8a10-4873eb037fb5 | -3.33045 | -50.24989 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7761bf2-dfab-3f1d-ba53-a588c92b7884 | -3.44669 | -44.1291 | 2025-09-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 96a45228-85a3-39d1-adc9-c358dea2b55b | -4.81983 | -45.64444 | 2025-09-26 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50baa7d8-1860-3d08-9cf7-02f0142d63bd | -3.80467 | -47.58216 | 2025-09-26 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 184acf62-76a0-37b7-a134-b78f663aa867 | -5.64062 | -43.92607 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57d7aadb-5615-30b4-b3a1-869533095211 | -5.63924 | -43.93599 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78038a32-6148-3295-a386-9a078d2fdb3c | 0.64349 | -59.91055 | 2025-09-26 05:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13e4f64b-1df4-31a7-bb07-6fd814961c93 | -6.88838 | -44.76059 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1414b5cf-775f-3e3b-8002-dabe20d608ae | -5.74462 | -44.96216 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| eee3bb2d-0ec3-328d-a794-e25ac4c934c0 | -5.73165 | -44.96897 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c1572e80-d960-3813-a531-c868da2afa86 | -6.93571 | -44.63968 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb2b1902-6187-3c56-9d21-7ae04e66a3bf | -2.37957 | -47.71936 | 2025-09-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41dc3f5a-a9e9-3d28-8283-7d5ad23cddb6 | -5.80203 | -42.80734 | 2025-09-26 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 18ce8eee-0f9e-31d9-9821-45bc4089e25b | -2.94279 | -49.33628 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4d867a8-918b-3503-addb-304ee8d26ead | -7.682 | -45.98721 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8e60796-3595-3acd-bec7-1ab9827b1bfb | -7.30976 | -45.75789 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d895361e-d360-325e-bccb-6c7c0ad2be53 | -11.9772 | -46.60832 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3133b31f-9adc-39d9-9c37-98c2d3819f3a | -8.32328 | -49.53108 | 2025-09-26 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb40aee-2ebe-3dd0-9a5e-54aa965ad63d | -13.6404 | -48.08745 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed9ab38a-a490-3f59-afc8-4e98607fdd7a | -11.96531 | -47.87818 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf2fdb7d-b207-3c89-8542-13ecf2caaec7 | -11.24285 | -45.55734 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ec410e7f-ae21-3abc-bc00-2bad29bd2406 | -10.62261 | -53.89318 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f991c862-f328-3e27-86c8-e4d38c609ba6 | -12.06937 | -47.98194 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39c4eb1a-6084-33dd-bb13-2d959dbda136 | -8.71085 | -50.05513 | 2025-09-26 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa1e6853-0790-31df-8b84-37e5b042d7ff | -12.25168 | -60.50742 | 2025-09-26 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbc35c9-736f-3d82-8005-495b0b0cf7a7 | -10.10177 | -45.30723 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 188760c1-e55f-3787-88b0-01b7e2e555c0 | -11.42986 | -44.98028 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c803aa0-8635-3865-b4af-614e53befea0 | -7.7959 | -46.01751 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f548337-63a6-3bb5-b5ca-234d92f68735 | -9.69197 | -48.94686 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d46b0455-0c49-3427-ade5-47e18a55e2cf | -10.40591 | -46.18637 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4c0eefb-81a4-3de8-92a7-ded90cbe4251 | -10.39751 | -46.15673 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4dbcb6b-411b-302f-99d3-2339c3b420ed | -11.23675 | -45.55659 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a7659000-6bf1-37df-8c68-f40ceccbe084 | -10.39351 | -46.14325 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7301b7ce-515b-3051-b940-5450bb8a4239 | -8.0843 | -55.21956 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
