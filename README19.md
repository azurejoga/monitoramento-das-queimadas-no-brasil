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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ca18008-9327-341c-95ed-e6cad61715df | -12.65942 | -47.33134 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a58d9e8-1a12-3eb5-ba02-7c1f02bb4298 | -11.77854 | -48.31503 | 2026-09-28 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db2dea93-6017-3a42-819e-7d7d829ee45f | -11.3773 | -43.3933 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4c5c574-ad9a-3094-b565-f1124e4db45f | -8.96416 | -44.15495 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ce352e8-bfaa-3b84-9d53-6983b1c09fc3 | -8.28217 | -45.41247 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64036000-b720-312b-a245-473b426d55c0 | -9.79101 | -44.82607 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 104e250d-142b-348b-8367-5dabe6f54b46 | -7.89042 | -45.44492 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50cc3497-ca82-382e-bf00-74fe77dfd919 | -8.45104 | -44.68022 | 2026-09-28 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0a4f8c0-256e-3c04-979a-2a2c533e31d6 | -7.52727 | -43.98154 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463def0d-5ba4-34ae-86e1-e97164812c0a | -12.10837 | -45.22054 | 2026-09-28 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f472edd-18b2-31bc-9fbe-00e4287a040b | -10.92555 | -50.67703 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ba73b667-f1b6-3bc9-bc45-b10d996f0394 | -9.82373 | -45.26707 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1161d920-2a8f-3454-9ea7-6252c6ed0594 | -9.77361 | -48.21569 | 2026-09-28 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce575002-dfbd-3c3e-bf38-6cba99f3d673 | -13.56071 | -46.36217 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ddc7bd-3923-36f2-a18c-069ec6177fd4 | -6.9366 | -42.86318 | 2026-09-28 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc51974a-ffd1-3080-ab05-edbe6bc6f646 | -6.70218 | -45.5906 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a60173a-585f-385c-a330-a968c9740591 | -12.68878 | -47.33314 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ff0b3d3-4c6d-372c-ac1c-bf37000032e7 | -6.70715 | -45.59557 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26548b26-7733-3ecc-9b3b-58aa0b58f69f | -7.99305 | -44.82146 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 663afd62-00a6-31a9-ba52-d540e01dd5aa | -11.68108 | -44.53911 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ba4a157-fac5-388c-afbd-a9bdc1b8021f | -12.68027 | -46.98189 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2189ad54-1d55-3a7e-aec5-597cd4ad13eb | -10.20543 | -50.00989 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b133bda5-b8df-3f56-bfcb-9a7ae52f5b04 | -10.19982 | -50.00162 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3c1365d-4206-30f2-b1e3-44d439209f8f | -8.01162 | -43.74545 | 2026-09-28 03:49:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1f106c50-7ab2-31f6-8c3f-3b0ab842c8bb | -12.74048 | -47.79313 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b4fd00d-8cba-34a7-a0ee-f952038d37d1 | -10.93267 | -50.67865 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 94bfc52a-f6e1-349f-8a7a-52d68d3fb2f5 | -12.62781 | -47.27582 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38231797-d578-38bd-a3cd-d9680cfd51f1 | -11.13636 | -50.06087 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ee4492e-34ac-3343-92e8-17160035293f | -11.68828 | -44.53915 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4399804-7fa3-3724-9ca2-f2606761ade8 | -10.70698 | -44.43501 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73b5d33-032a-38d8-9de6-991641bd3737 | -11.67899 | -44.55004 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5c57c89-d8f5-32aa-b811-ae5a85d7fcaa | -8.287 | -45.417 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7014f986-679c-392f-b370-1a8c7b55348e | -1.85769 | -47.98132 | 2026-09-28 03:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5fbb6bf-f952-3beb-b725-3e8e1c65fe29 | -8.10424 | -44.0085 | 2026-09-28 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d4c9410-a7bb-3b2f-a138-aa3ea2671a77 | -12.62469 | -47.32139 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a1b1503-83e0-3238-8316-21a79ef542d4 | -13.07388 | -47.44637 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7a9b06d-2b08-3885-80a2-e3af7a0c9e43 | -12.67844 | -45.01926 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 11644678-531e-3584-8aea-2c9c9d11af88 | -8.36106 | -45.44709 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a966f5a-4aba-3208-915f-7b0255d08a5f | -10.94141 | -43.90274 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5b6ef03-4f71-3488-9f2f-4ca897565d15 | -9.16901 | -45.77907 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d992436-6969-351f-b1c5-47451bd84214 | -8.67034 | -48.96809 | 2026-09-28 03:49:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f652bf22-6f2e-36ea-b6d6-151f3eb34f7e | -12.64159 | -47.26609 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d78c2cd-f27e-3260-803c-6926151b13dc | -12.30923 | -46.40945 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35f21bf3-91b2-3a32-9741-05d7cac9006f | -12.68594 | -46.98261 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 478219e2-5871-37cb-b7b7-ca99b7675d17 | -9.99172 | -50.1404 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35c93eb4-af5d-37e3-acef-e0aa7ab9cb4b | -12.74079 | -47.31046 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70d5a24b-57bb-3e09-b67f-3862c4876afe | -7.26688 | -45.34772 | 2026-09-28 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2028d462-437d-391f-b05c-f950afa1291d | -9.82462 | -45.26715 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5325633c-cd05-3414-a765-6178a10d3ca7 | -11.68317 | -44.52819 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a917171-51da-337d-92a0-4c5703f22b16 | -9.28698 | -40.46008 | 2026-09-28 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56236f48-5f62-386f-9344-d376d235a4a9 | -6.7135 | -45.59275 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0160d9ed-a4c8-3eb2-8144-85600170465d | -10.92654 | -50.68366 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e6aa972-9316-3703-9acd-205ea6ea2fe8 | -12.62052 | -47.28267 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03d14ee3-849d-3f26-a1b7-92fa198b97d3 | -7.62232 | -44.60231 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca743d65-44d1-3ac5-b3f7-638611a1a7be | -8.09923 | -44.00804 | 2026-09-28 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a26cd4cf-d98d-336e-9e88-2a760e913efb | -11.68443 | -44.53272 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9326a394-d7cf-32c7-8473-6fc95814751a | -12.63121 | -47.31847 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de781821-34fd-3fad-ade4-2b666b12d2f0 | -11.12939 | -50.05794 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd3f4614-e450-3543-a151-a53712b73a03 | -8.23569 | -45.48202 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc71335b-6621-3a68-b604-329098ef030a | -11.18754 | -44.79605 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a620482a-d2cb-3049-b70a-6b97d8b37f21 | -10.92095 | -50.67481 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0efc7569-4f48-3986-9ae2-2a85d4f4e71c | -11.62527 | -46.78827 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af9b7a7b-b55d-3a3d-bcfd-98e436fa5039 | -11.82776 | -44.98682 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ed9899-9d53-34ca-bfac-3e38c7c95a5d | -12.30807 | -46.4085 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a6a1874-c5e6-3e2c-a0ab-925116f49cbe | -12.3121 | -46.41689 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e13c940-80ad-352d-aedd-6a485380f1b1 | -9.81985 | -45.2588 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20b6e653-b06f-3ba8-af3f-bbbd175c54cf | -7.26135 | -45.34674 | 2026-09-28 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a766423-d0a4-391b-8cc1-8daf4d5a2e8f | -8.97117 | -44.14467 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d285b11-3449-3a6f-ac97-b54aa3131bd1 | -9.62637 | -43.96204 | 2026-09-28 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 390de909-1b91-3c85-8307-05593ce0f07f | -12.65539 | -47.32197 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d67a0df6-3a08-314c-87f5-588e64251fe9 | -13.20485 | -48.32777 | 2026-09-28 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81dd85ba-ea74-3618-982b-9f6f595ad5a2 | -7.98786 | -44.82003 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afe954b3-b53e-34f6-855c-74fbc8204f2d | -7.34839 | -42.0773 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| adfb3782-8607-36b6-9c63-0b9003942491 | -11.68004 | -44.54456 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a3f1bab-74bb-3c6b-812c-c8a11e9b7a3e | -13.57201 | -46.36056 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f74a7ade-2deb-3636-b9fa-9b7a2d1e3065 | -8.28764 | -45.41658 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cf638b5-04d5-39f6-b74d-28c6fe3ca63b | -6.92718 | -42.86151 | 2026-09-28 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e885f099-8082-3d88-b786-0f9e5d1ce55f | -9.77339 | -44.83569 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 906a28c1-68c6-36d3-bd77-118cacb1677b | -6.71777 | -45.6017 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac927a36-bad3-3c6c-ad64-d4c9c2445613 | -10.20565 | -49.99877 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 236a478c-381d-301c-b6e5-8b06f1fa6e1e | -8.23897 | -45.43281 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9635638-0dbf-3e72-a097-dabb3bc6a21d | -12.67864 | -45.0248 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfca8dae-d836-3705-b63a-545cb8b0d1a8 | -10.2126 | -50.00028 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae9679d1-0dc4-3b79-a1b0-01197c9d7d68 | -11.2045 | -44.78791 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 868d5121-0daf-3e6a-89ce-d9436b8a4d18 | -11.44014 | -44.93461 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7888c0cf-320f-3e49-824a-9169a64792a0 | -10.45125 | -45.09452 | 2026-09-28 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96ba8e95-bafe-3e95-860c-e80e726e15c6 | -9.14416 | -45.63758 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 26cc0cf7-921d-380d-826a-ab668ce4b45b | -13.85605 | -46.37597 | 2026-09-28 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f485841e-2c84-35ad-973e-a7652e18f5a2 | -9.14551 | -45.63034 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0d09d2e1-6494-3787-98e9-9b25050b12ec | -10.9196 | -50.70612 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5dcd1347-65d2-345d-a307-83ba656d46c9 | -13.45264 | -48.60053 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69b4dc7a-25de-3dc2-a7ba-b8955115cc7e | -13.10384 | -47.42098 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d03c234f-e5b6-3464-a487-99bea2fda2b5 | -10.7996 | -48.73655 | 2026-09-28 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5025f1c3-e195-392b-8917-9f68db2f6742 | -11.18797 | -44.82179 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cd8ce6fd-f0b3-3901-8b83-c889ed05a0da | -9.82007 | -45.26223 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8778fe53-f77e-3db3-8b00-795d4a9feb53 | -10.89494 | -50.6918 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a0cb156-dacb-3c65-961b-677f8aa9f54e | -13.08039 | -47.44347 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc500da8-64e4-3f2e-9773-d577c2152c84 | -7.99855 | -39.70538 | 2026-09-28 03:49:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e59057ed-c36b-3900-924c-2f319fa82006 | -13.0752 | -47.44494 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32fc49f6-f500-339e-8044-e0a54a67c6d8 | -12.87417 | -44.7832 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README20.md)
