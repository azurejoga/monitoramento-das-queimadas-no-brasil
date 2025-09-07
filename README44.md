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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee4f9b6-9c3b-3431-bf96-b78591ef969e | -12.28954 | -47.24495 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a13d0ff-1068-3087-9960-53495223e054 | -11.73502 | -46.70135 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cee81736-8489-31de-bdb9-b0da47aa84c3 | -8.68539 | -45.3082 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 86f56d12-d772-36fb-9866-5e74a75818d9 | -11.25896 | -46.51423 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e67e03d8-d2ae-3743-b0d2-4df6991660a0 | -9.83634 | -46.55155 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08054ec3-d209-3950-9191-f0d369459066 | -9.18782 | -46.03678 | 2025-09-07 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f8a9b8-7b04-3393-b165-0e23c0583dc2 | -11.13804 | -48.38283 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce2dfca5-749a-3367-a23e-293250e41148 | -11.40221 | -43.56684 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9c97e58-c4b7-3af4-8180-54b235e14b47 | -8.58067 | -45.47681 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88bfcfaa-d048-35ba-86bf-4b7e5e385cbc | -11.2091 | -55.0132 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 710565c6-5e68-3ca2-9e79-b60241cf02e2 | -6.48613 | -43.98058 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48d5e345-1380-3f02-8b97-273fb119bede | -11.0069 | -52.05005 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 985b41de-4648-3baa-bbef-b85a53ebd0ad | -8.6817 | -47.44889 | 2025-09-07 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afea74c8-4af9-3474-a2af-cdcc6a127ab2 | -6.20232 | -42.62165 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c125aec-ec50-3c97-87b0-11fb283bd73c | -6.43482 | -43.61241 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c08118fa-6f7f-35aa-8531-3af19988f9ca | -6.43487 | -43.63421 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc060703-5b9d-36ec-8e6d-df5ef62819ca | -11.20849 | -55.01651 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b9281e2-79b9-37de-8af5-1724c36a027a | -8.42254 | -47.31365 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a015ee04-8206-3084-81c1-740a53ea86fd | -5.48198 | -45.91008 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb7fc372-0462-305a-9058-6aeea26baa29 | -6.88477 | -45.58773 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f921f8ea-217d-3c7e-bace-e88fc717a485 | -6.59494 | -43.97995 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d1b0e00-03e7-3d53-b935-55a44cee389d | -8.30671 | -55.10339 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a353551-4427-39d1-9309-94942ea04383 | -6.22706 | -43.5735 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e6bc655-ffae-3446-861b-b5ec794dd65a | -10.14929 | -48.74001 | 2025-09-07 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da162d39-4367-3ecf-9064-622f38056a16 | -8.69208 | -54.67934 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9adc653c-704b-3b1c-8dcc-9ea15e42ddc0 | -6.01518 | -45.88758 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e64b69-a689-39ff-9a04-02101c8a299d | -5.67683 | -45.43124 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0f24dce-559f-3c08-8d24-b09e964cc613 | -7.74795 | -44.01185 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1c5b3db-010b-359e-a268-d14da623b381 | -8.5035 | -45.06165 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62cff729-261f-3764-a738-fd31f7f7488f | -6.06534 | -43.30418 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69cdc8cd-6ca9-31b4-9cd0-5d01137a76ae | -6.52389 | -42.41703 | 2025-09-07 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 004813fe-a2c9-3139-8b3d-e1afce1e2e7f | -6.55646 | -42.95907 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f9e6791-b479-3b8b-a7cf-4eefb1b6bb98 | -6.23165 | -42.59154 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de836eb0-f9d3-32b4-a283-16abbd8e7069 | -6.94639 | -50.97001 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 686b2e19-7218-32f0-9a93-60c470421383 | -6.19926 | -43.59821 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff0d8593-acb7-3841-91c8-f8a6a4b33b3d | -9.41973 | -46.77175 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0e8396-e013-3af4-b356-5adb1182ecc0 | -8.34721 | -48.27543 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da40beed-6033-3dae-92e7-055a96963909 | -5.97438 | -44.731 | 2025-09-07 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06b5cc8c-1ac5-326f-9c55-ff51eaa055fd | -6.17057 | -43.19146 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1898d230-d901-3745-ad96-8421e936a7b3 | -6.23031 | -43.53047 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f28e4d0a-5619-3bae-9bf5-185054c6485c | -9.84025 | -46.54853 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7755c1b4-6680-3725-8a35-d4f9caef0075 | -10.37906 | -44.96587 | 2025-09-07 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 52f0d58c-6ac1-31af-858d-ba534106c082 | -6.63012 | -53.17227 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efeacfcd-86ff-3da0-96e5-4b1d89485861 | -6.19544 | -42.62064 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d5bda01e-df44-3bdd-b1bd-ba4feddb557e | -8.43414 | -47.30773 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e5ba606-b335-3d75-967f-8038f9f8ae87 | -6.14866 | -43.19909 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9c726c0-7609-30f7-bac0-6cd706e81dee | -6.87764 | -45.54698 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13803fa4-846d-3d23-a632-612c8d9e0d60 | -8.3436 | -48.27485 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2812a6a6-0bc0-33db-8f5a-edc5d8841616 | -5.95317 | -53.80407 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 107bcde0-80f1-3147-b525-376b205d3358 | -10.1558 | -48.74534 | 2025-09-07 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff407aa4-2477-37ae-8395-a28bdce7ea8b | -6.6561 | -47.71382 | 2025-09-07 04:19:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7ba65b1-6dbd-31d7-a499-d431173ac1a9 | -7.68845 | -44.97488 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 429a53bf-2dfd-3ecf-a032-f1087b27c60a | -6.27791 | -53.42676 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc115e3a-0e98-325d-9653-62c0a16a92f0 | -7.65896 | -44.81746 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43ff534e-dd7f-352b-a0cc-505c408df33c | -5.94785 | -53.80305 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34fd766f-15c1-3415-be0d-e6c89b019385 | -6.60215 | -43.97745 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94a991b5-cc4d-3ebe-9b6c-461fe99b736c | -12.82345 | -48.01421 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c797293-f492-3a84-819d-b29fb8a1aef2 | -12.816 | -48.01692 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9117871-df92-3068-86ff-332e18f03f43 | -6.08776 | -43.29294 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 071aab27-f2fd-3357-9a10-04f8fffdf8fa | -8.93747 | -48.65108 | 2025-09-07 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd33cf66-5f61-3ef7-b80a-3be31af9ee45 | -6.88141 | -45.60877 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d43e5ec-db4a-38c8-8145-ce264210b5f5 | -11.59381 | -47.16029 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b047050d-c29c-3d29-9621-bce2854c3ec0 | -6.89419 | -45.59284 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ee4b36c-67df-340e-947c-6f195a3efb9f | -8.44109 | -45.02685 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83063910-e03c-35b3-b969-f241ece13a33 | -8.3829 | -52.53539 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15748f3d-5290-3961-b09b-6c2df5182498 | -8.02134 | -45.4477 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29f13a88-7195-30d5-9f53-9f5249f226d7 | -11.62366 | -47.1573 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e105058e-fa39-3eb3-960a-aee853fa70f1 | -8.37045 | -47.51007 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b385355-9f45-3574-9df1-15b168627057 | -8.14648 | -44.86974 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bf7489c-b65e-3795-8c7b-13ba3bc1c462 | -7.68812 | -50.28466 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e4cb569-81c3-3910-b670-21326c5c499f | -6.3844 | -43.02755 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b5f73d8-310a-3237-980f-b983d3b2d5f6 | -6.19722 | -53.26969 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfd7fc8d-6831-32d9-aecc-c364009287b6 | -6.13177 | -44.2497 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 141e068c-04fd-3bf1-b6ba-9d9fc431008a | -6.11192 | -44.76369 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d911dafd-e5a2-3d0d-8095-1194601eef57 | -6.14529 | -43.19856 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd97f377-8bbe-36e1-bf8f-10966859894d | -8.91289 | -45.82329 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5f45e78-1a5b-39a9-b3db-3ebef7091cbb | -5.69093 | -48.13414 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4a2c2341-8b4c-38ff-83fb-afaab4d15017 | -6.18856 | -42.64243 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20bdeeba-8625-3edd-b49f-fde7fb078fbc | -7.74088 | -48.82206 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c929669-5a06-32d4-b995-01f0e1fce43c | -12.86937 | -47.99022 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 003d96f0-b190-3e34-968f-f61c93f35826 | -11.61971 | -47.16039 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cbf31f8-e6c3-3665-bbdd-ea276bd966a2 | -6.1871 | -45.4262 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 804f841b-39c8-3ab4-a59f-ee97fc7e8878 | -6.1946 | -53.25424 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b3287b1-f83f-391c-9d65-5c4317b81af1 | -12.79767 | -48.02171 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec2a58be-09d1-3a47-92a1-285c87140faa | -6.2308 | -43.29273 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdd29bec-81dc-3c4a-a533-e5015cc08d19 | -8.15143 | -44.85984 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b38c041-94c7-3822-9cdc-a36fadbd9eb0 | -8.01748 | -45.49348 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f48abd2-6e36-3739-badc-38ad7a5f08b5 | -6.60099 | -43.96301 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56e0c303-eb30-3ccc-9460-1516919c74b6 | -8.70664 | -47.87222 | 2025-09-07 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f12ee291-0849-32fc-8a12-d4eb7d082f7a | -7.41798 | -44.9246 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 522642d9-c146-37cb-b87b-dc8798b6e7b8 | -7.67877 | -50.29024 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bd6642e-4373-3be9-a7b4-87a1b9792956 | -7.43343 | -44.93415 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a0b382a-cbcd-39cd-8686-e89412f2b4bc | -11.11128 | -52.02472 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9532ff4-27de-3d5e-9e5b-6e8d1430ac00 | -7.61344 | -44.6752 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79d5edf2-c6fb-33be-8641-0a424b0af96a | -7.23942 | -44.82908 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4ac77bc-da93-3b98-84a7-d1bc3500fa6d | -6.19975 | -53.25499 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3fc3eb8-3863-30e3-81d2-46e832f7c5eb | -6.22462 | -43.2881 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36cf2720-6ec3-3316-98cb-8047c5555c22 | -6.91987 | -44.33392 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 768c5bb5-89eb-339d-b08f-d52815502279 | -6.86657 | -45.55231 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1880636a-bc24-336b-b53a-7fca93a640bb | -7.57703 | -44.66942 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
