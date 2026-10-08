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

## Dados Diários - Página 249

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf8b08a8-4815-3915-9555-7a06c442a498 | -10.30564 | -42.37926 | 2026-10-08 15:41:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| cc15dd53-a96b-3106-9e02-cfdaff5a6219 | -5.28364 | -42.7338 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 7f022d9e-3405-3f34-ac74-36c5df91b057 | -7.46504 | -42.82162 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 55cdc2d8-db6f-309f-992a-088291d63460 | -8.19643 | -46.37041 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| bbbbef64-0db4-37e0-8357-606226d536d7 | -6.3284 | -46.55142 | 2026-10-08 15:41:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bfefc586-24dd-3043-abbc-dc586e830bec | -6.8336 | -39.56226 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| ff523978-bec1-34b2-8923-2b1322f266ac | -9.97972 | -39.53241 | 2026-10-08 15:41:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 28.0 |
| f2314df7-19f3-3ea5-87e7-070f81bffda0 | -5.72968 | -45.15959 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5a96abcd-414e-34a5-a648-fef3b9e24793 | -7.87123 | -44.15023 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 091e801e-d470-3138-8a8e-dcda366d162c | -6.14763 | -38.34672 | 2026-10-08 15:41:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 09a58447-121a-304e-b495-35d19214ba97 | -9.82929 | -44.78244 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a32f13cf-0c62-3944-b661-8878e5008448 | -5.44362 | -45.68428 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b0d6dbd9-4ed2-326f-b2bd-dae60a79a7fd | -7.70271 | -45.43502 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 13bcd3b7-21be-3bce-bc15-56f5353383dc | -5.72942 | -35.51125 | 2026-10-08 15:41:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f7e0cffa-5714-37b8-984f-6df3a5318d19 | -10.58185 | -41.20231 | 2026-10-08 15:41:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| f30bdf83-640e-37c7-a2af-246ddeb0ee38 | -8.96096 | -45.13411 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f228d512-fe17-3dfe-a620-39e067715c06 | -7.24495 | -43.51004 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e03b5099-0b33-3c6f-8039-72dcccfa3b5b | -6.8552 | -39.46066 | 2026-10-08 15:41:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| acede8d7-eb43-3251-8beb-c1178f26619a | -9.88418 | -44.85324 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 69039052-ec12-3e7b-ae71-2191eb24ea98 | -8.65731 | -44.87896 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a76e836-1e1c-344f-b240-cdfea64f0be1 | -6.91868 | -45.88348 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 71ba11bc-4cef-34b4-99a6-8510a5e74362 | -9.37218 | -45.93623 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 62f0b1bf-33c0-359b-841b-16862bb86a60 | -8.98997 | -45.9108 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ea32af4b-da09-3ad6-9af7-7d9b243b0d3c | -10.943 | -45.38338 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| befe3839-184e-3d2e-984c-7dd91fb84e59 | -5.34249 | -45.76876 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fed1d32b-291e-3444-9de6-0410bf2dbf9f | -6.81864 | -34.91738 | 2026-10-08 15:41:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| cea07be7-34df-369b-bebd-605e743c5d3a | -5.72242 | -41.71714 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2d44e2bf-d7a2-3fcd-a2ab-0722fe2ab005 | -6.39117 | -42.5374 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2a82c038-03e9-30ae-96f2-ae836396778f | -9.93691 | -43.57731 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2d9a7f43-5cb7-33c6-817b-faa358a0f15d | -6.32759 | -43.8269 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f4de872f-5415-3990-ab8b-f0beafc35dc1 | -5.75867 | -42.07637 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f69fc7ed-7dc0-32ae-8f7f-89e898d28347 | -9.88485 | -44.85883 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 0f11a72f-2c31-38d7-904e-556a7ec45621 | -6.23261 | -43.73964 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96a966c3-5ab2-3168-8357-8eda5487bcc7 | -11.21387 | -44.87297 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 99f86a27-0570-3764-a99b-2817f54c30b3 | -7.8575 | -45.14983 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 74da254d-26c1-3579-be86-c6396bdf999a | -6.67151 | -45.35 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 090b42a7-96c8-3b4b-a3f1-24a38789eae3 | -6.88583 | -43.70626 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9b3eb2ef-132c-3738-9889-f80856b7850f | -9.89137 | -44.85796 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 10ac584d-fe97-3940-b875-de6a1d314176 | -11.26588 | -45.18283 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4cddddf6-2554-389e-99cf-88411c452326 | -6.99274 | -43.21128 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d764c32-b163-3e51-a0e0-b7b26e739519 | -5.71675 | -41.6413 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0f89e66c-1729-3ce4-81e7-bcfdd76930e2 | -11.13666 | -46.1585 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d0db303e-9aa9-3b1b-9145-a24288cb42ea | -6.8558 | -39.46488 | 2026-10-08 15:41:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 123.8 |
| dada9e31-f14f-3df6-a8a7-e79fbbbcfbf7 | -6.92812 | -43.66728 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 73a28003-ca59-3a40-9703-e89d65f6fcde | -7.47366 | -42.84324 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 8664ce9b-d30f-3911-8d5f-6dd2e9995430 | -8.07474 | -45.61531 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7ad29c79-2f56-39a5-9421-0cd62a88e92f | -6.31474 | -43.34153 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 631ab3c1-b005-3394-8856-4a36bd62d3b0 | -7.11146 | -42.52965 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 622f0f32-f877-3d08-88e3-9542ab56ef12 | -7.46457 | -42.85971 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0abe048c-a4ac-36d3-baa1-e27522f9babe | -8.66697 | -36.66836 | 2026-10-08 15:41:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a5b5cdf4-30d8-3ac3-b906-e6296e1498a1 | -9.07709 | -45.1175 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 400113ce-f34a-3ec3-969d-3aeddba14d16 | -7.40724 | -43.74487 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0aedc04f-3eb5-36ae-b8c6-294e28c89315 | -6.85083 | -39.46129 | 2026-10-08 15:41:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 0cc40e74-07e3-31c7-befc-56667f8162d0 | -5.47664 | -45.63614 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 308161fe-592f-3d43-93b9-9a9a5ede2f64 | -10.90511 | -45.54257 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 26c34d1f-03e9-3c91-b181-5229e5801934 | -10.08187 | -45.9997 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 26e3315c-4295-30d8-86ce-1dc0ee71f028 | -5.43188 | -46.64569 | 2026-10-08 15:41:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8b0f1770-d2a3-31d6-ab07-478da6a8c8f6 | -7.40032 | -45.65453 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 267d11d2-cc3e-3da5-9331-6fef6637964f | -7.46796 | -45.77832 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 60f83e7e-5e27-3e20-b865-3356079896b1 | -6.63639 | -44.88903 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a1c8e00b-6486-361c-9f9f-d1d4b60f0197 | -8.93163 | -45.16578 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 50712e9e-bb5c-3e78-8be2-73ace1095077 | -6.5365 | -45.37846 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b367e898-4482-3969-b3b8-56c89269b67d | -7.48154 | -40.65147 | 2026-10-08 15:41:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| cc04b9c5-d874-3837-adb3-949b3d5aa20d | -5.28272 | -42.72735 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| c7542eb7-1054-3c4d-8d4c-e4e93a099336 | -5.69975 | -41.73789 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cd753f8a-b408-367d-83c4-9ee6bdd13424 | -6.8264 | -39.54266 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e91ec228-3853-33c3-b682-a96e820c350b | -6.43281 | -44.81381 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11f5aa98-1ba6-3722-8ed7-d773a83a1cca | -5.74143 | -42.0661 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b4fa0d85-e537-3773-964b-c417b8069dba | -6.97156 | -43.89764 | 2026-10-08 15:41:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd13e1af-6398-3419-a3b2-73507e9ce42e | -8.60571 | -45.63982 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 24c67aca-f227-35f6-9595-f09b5aa3bc49 | -7.20179 | -45.35265 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10d71a30-4aba-3f22-b89a-00eeb50e04da | -4.74755 | -40.49994 | 2026-10-08 15:41:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d296a29f-cbd8-3ec6-954d-3a69a5bea159 | -6.17011 | -44.85358 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a949ef20-53c7-30fe-a0f7-3a66257e29b8 | -6.99731 | -44.13099 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b498185-1f96-3b26-ae3d-532d36f327f5 | -7.08576 | -43.0908 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| edb9fea8-8b5b-3859-b5e4-b2808e48d16d | -6.15271 | -39.44688 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3e9ec733-8d7e-33b8-9a25-baf6560a3cfe | -6.82073 | -38.54636 | 2026-10-08 15:41:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 9f9787a8-e7b5-315b-9561-616a949b0e8c | -11.20592 | -44.86245 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 84f14ec6-f084-371f-acf8-30f3f1660054 | -8.21378 | -46.39555 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 288.6 |
| f905fe69-31d2-3a89-9e54-34baf4b50cb8 | -8.19814 | -46.38419 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 5247527d-f98b-3420-9f9f-8b091887cd0e | -10.90356 | -45.52951 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 9b50bd84-fd0f-33d5-832b-34ac2ab5ef2c | -6.81247 | -44.1857 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76d48e2c-0071-3069-9eb4-519d7404f68d | -9.07646 | -45.11234 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 047244b5-bbd1-3764-91d2-94c59b1c8f7e | -8.94107 | -45.18758 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 7fcab97a-9dd7-38c6-98ff-5833b98c80ac | -8.96016 | -45.13616 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4d87f6b6-6b91-3d65-b7ca-507421d4f4e7 | -11.20416 | -45.22505 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 155b1362-7e82-3805-8e53-999021f269b3 | -7.48991 | -42.79691 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 47d841c8-677f-311a-a0ac-5e77919fc7c1 | -10.07437 | -45.99634 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 733b8f07-1777-36d8-b68c-99093091f9a2 | -7.378 | -46.23298 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3494bf28-e48b-3961-a742-b0d1d7a09b5f | -6.15155 | -39.43854 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 8fdc22f3-f7e1-3420-a7e7-bb39307d14a6 | -6.07059 | -44.10432 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3e43aff8-58d0-373a-8fa8-f5075a2adbb0 | -8.42312 | -35.77045 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 846cd496-fe16-362a-a9cf-e59edfa64304 | -11.08599 | -44.00566 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 46791887-6308-3e18-bede-f5c2e2cd0d26 | -2.92727 | -46.72765 | 2026-10-08 15:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ea020b80-acd4-3dfa-b554-7b1a45cfca05 | -4.43227 | -43.904 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 690f7925-fbe2-3cc3-9677-06d5295af6e3 | -4.52067 | -44.01683 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1beb5c24-f428-359b-976e-b1de3c592e6c | -3.78306 | -41.6726 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 5ea6b538-1e74-394b-a01a-babcab9d8ad5 | -4.01057 | -41.77218 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9d521929-2571-32ec-a456-2a5445e4a96b | -4.01386 | -41.77443 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1b52393c-a87f-3e90-8153-f9a9c593cee6 | -4.10057 | -44.11036 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README250.md)
