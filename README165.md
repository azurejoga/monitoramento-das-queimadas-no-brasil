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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a985f9a-d97d-3c9c-b582-df3fd958cfec | -5.75626 | -43.71779 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 363f0fa5-2668-3a1e-9f54-9ffbeb28f413 | -3.56828 | -43.46942 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 6fd870c9-530a-3b92-9b38-3197cdd21f92 | -6.18948 | -47.61042 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f246bcec-467f-34fb-ad1b-cfbcb5ec4018 | -3.92423 | -38.36469 | 2026-09-21 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 05f42170-d190-3ec7-87c4-f13273a84665 | -6.45099 | -44.59775 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5b48e2bc-35b8-39e9-8ca1-1b179f788b25 | -2.55733 | -44.07794 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ab353c28-7cb4-337a-8323-973f1ff95107 | -1.82151 | -47.84214 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b5f721f1-917d-32ce-9aed-3c7719bd2bfe | -6.21203 | -45.36167 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7e59c912-5b1c-35cf-99e3-559ece860881 | -5.75931 | -43.70965 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 74742d09-7425-33c4-a0a2-975ed62cd0d5 | -6.86387 | -44.56483 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 85d6c47b-5c8d-3d53-8536-a0158c7d60bc | -4.6052 | -40.39217 | 2026-09-21 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bdd9fb74-c7dc-39f9-869a-fafe6863b4da | -6.98739 | -44.69137 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ff8ddc74-fbbb-3752-b0c0-fbc7290d4521 | -5.02032 | -42.97395 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e52b6473-ce3a-3874-a303-ac4019e03e60 | -4.84891 | -40.52019 | 2026-09-21 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 49510a37-7849-3e1c-8820-939704f138f8 | -8.48734 | -47.01968 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3c9e7149-81c1-31ae-a9db-ab53d1e6dc0f | -4.22352 | -48.61834 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9c6f3f1d-6365-300c-bc71-052372938fdd | -7.13102 | -43.10216 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c19be32c-5228-308b-9e99-d587b59d8797 | -8.44935 | -47.64942 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81f28ab6-f0ea-369d-80d7-95f151ee8d38 | -5.91161 | -38.09048 | 2026-09-21 16:03:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 35f2d578-abc1-3828-a01d-c44fc3d8c156 | -5.73958 | -43.71994 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| e6649760-b8e7-3163-a3e2-b16bc3e2bd51 | -8.49915 | -47.0255 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ccbf4d7e-24b1-326a-916e-0bf0d525656f | -6.2298 | -45.43811 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| dd883619-ec73-32ab-86bc-9f21d8e7105b | -3.18385 | -42.79588 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5a7c4597-299a-356d-89ea-58d365950f44 | -7.741 | -46.78673 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcdaa00a-d05e-30b8-9f1e-9fb5e84705fa | -7.37724 | -44.62714 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9650381b-72d6-3656-9ceb-58894a32556c | -8.51176 | -47.42388 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b82f5af7-d87d-3bb9-86af-1c030e729cbc | -7.58825 | -46.72537 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88b3241a-fe38-3983-b521-3f4ed71c0094 | -1.15598 | -47.92129 | 2026-09-21 16:03:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29ad0c17-4ce8-383f-a242-c860d4a21027 | -7.34677 | -45.3497 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 72b04b63-8764-3e90-a2dd-6cf9318460a3 | -4.39689 | -40.73337 | 2026-09-21 16:03:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 260fdda3-c07a-345b-a60a-7b62371e3efd | -7.88522 | -44.84623 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e6b07cae-56f9-307d-8b5b-3e12d49b2ee4 | -3.21727 | -42.46922 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64563fcf-e4a6-39ae-8207-20be9420675c | -7.43892 | -44.76638 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 610bd9e0-a6a6-34a4-a068-e096608727fd | -7.34063 | -44.46489 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 64641fed-7713-37bc-b10e-0fa52d34b1f0 | -5.79595 | -47.21663 | 2026-09-21 16:03:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 15fa7693-0155-3664-82ec-255b637e94f5 | -6.93375 | -42.91884 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| c1796fdf-20f0-3e62-a56f-63b0bdbd29fd | -8.80498 | -48.75686 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 80a8261a-7127-30d4-9355-218853c9a9a6 | -6.46924 | -48.42234 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 33f7f728-b7cc-3db7-a3bd-2b4ed8c8e0c0 | -5.61515 | -44.83976 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f2740751-8ff8-3b35-8356-d7f2004df807 | -6.00186 | -44.78191 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70b0aa5e-dc91-3850-9238-7e51728af056 | -4.90295 | -43.46246 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70d1bc6c-a8ac-397e-8cf5-4fd291e6098e | -8.38499 | -47.27533 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3b9973a-0406-330e-ae38-4b356e38d47f | -2.94122 | -50.49484 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3a37a118-002e-3b14-aac5-0deb0fc6cf22 | -1.45332 | -49.7534 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| e507f9ec-218b-3dcc-8980-612ce438135e | -6.29571 | -41.75751 | 2026-09-21 16:03:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 594dac30-95e0-3ee9-8aa5-d5bd5c5dce46 | -5.85198 | -41.12507 | 2026-09-21 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| c177bb25-d9c1-34a7-bf64-b84645bfef75 | -6.25443 | -41.65537 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 87eb2db7-7701-31ed-b376-327ab7a370ab | -8.45785 | -48.44971 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ae099377-547b-3d2b-814b-ff5424bb3267 | -6.92066 | -38.73653 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 779c003e-f2d9-3216-b0cd-15be972b917a | -3.17391 | -51.35659 | 2026-09-21 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b67b7af-42ba-3355-a3de-5d0dbd23da03 | -6.92165 | -42.89196 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 78c279da-a753-3773-90b6-c1a0828e392e | -6.98409 | -44.68924 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbe863bd-4d28-33b2-8861-fb5ea5214a0e | -5.23079 | -49.32577 | 2026-09-21 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7e0120ce-a3f4-32f5-abf7-9db7fc78f6b2 | -5.79174 | -43.77461 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e313482-1634-350e-9d16-a8f79046e315 | -6.90721 | -41.69906 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| d4ff2647-bb76-328c-978a-2b918f76903b | -8.42364 | -45.85699 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca49dfc2-9184-3768-98eb-258f8a45e3e0 | -6.40233 | -43.18373 | 2026-09-21 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f3471712-873a-3964-ac1f-c231b2279f53 | -4.57849 | -42.93923 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4947865c-345a-3962-864d-2d3d42a50a32 | -6.83537 | -44.06815 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b933a7a8-d83d-3d6b-9804-f48d4980d1b3 | -7.11416 | -43.56416 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27192447-710f-3331-a5c1-fa87da85bf13 | -5.34426 | -45.96128 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 613ab636-871d-3ea1-a249-9d3e3d9cee68 | -5.61066 | -44.84035 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8c98570d-f535-3337-9eff-9adcd5e5d5c1 | -8.61916 | -47.30348 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8e274ad-d0fc-3acd-a30c-4ec81ae9c3ae | -8.00665 | -44.80938 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 65f3fb2f-7f85-3988-be95-eab93339b4dd | -8.39561 | -47.18056 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 56083c8a-99e4-3b24-82e2-4bbaecc1ed71 | -3.70433 | -38.84269 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7990eb80-06d2-3bd4-929a-99d8451f0494 | -6.77986 | -43.7053 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6de4e321-5283-3a99-9b11-a74fa93fceb7 | -6.03748 | -44.8575 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 141a2bf5-ba65-36e3-a35d-158c5619cfc9 | -3.3929 | -43.07477 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6d23aac0-82b0-3edd-b4f8-9e1304fe0f05 | -3.84384 | -40.59737 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e90efaa7-6d2d-35af-9a6e-d5da970d06dd | -7.37663 | -44.62284 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e376366-89fd-39db-957a-408739ff9e9d | -4.31801 | -43.90497 | 2026-09-21 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| eb6ba465-52c3-32b9-a2db-d63b5ec62a26 | -5.73902 | -43.71614 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 916ba576-5fca-3e15-8e15-3482135e8aad | -7.4023 | -44.80526 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 00486939-289d-3518-8240-46a18f1e48ff | -5.80957 | -43.87043 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5b064913-d917-3042-8fd4-ad3632b663b7 | -7.75334 | -46.71824 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6571bdd1-6b86-3864-aa1c-3ac96581a986 | -5.98939 | -45.25503 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66925d14-5cd1-38b1-a8eb-fef4cb9c0268 | -7.11837 | -43.56364 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a73d8578-8c29-3802-9cf5-f1d19ec9bea4 | -5.37206 | -43.19085 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70af7135-cf70-3426-a888-07a65062f833 | -8.41513 | -45.86957 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ab82a872-6bd3-3ab5-bfe1-8ce7a7b5bde4 | -2.17402 | -45.59273 | 2026-09-21 16:03:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 07200c3d-5c7b-3f7f-b091-51b97bc5b5cd | -8.50504 | -47.02828 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b07fc2e7-f012-33c1-a129-bb54b8d6a037 | -8.48626 | -47.02442 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 08f75d50-b601-31ae-aa71-f78072948551 | -6.17907 | -47.61575 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5996e53e-32d8-3a11-8a4b-bb80326d9c2a | -1.16311 | -46.77936 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d1d4cf64-aba0-3ce1-a783-5a9dde442f63 | -5.42579 | -45.70973 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81891807-7452-3add-9b77-4ad47925f7c8 | -5.9979 | -44.72286 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| addb2799-f55f-3ae0-92ab-03dd23137ddb | -7.50822 | -46.22525 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f2a0984b-7a82-31c5-ab42-fbed93971536 | -6.92477 | -42.94176 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 4942ae83-8fac-379a-9be8-0085d8da208e | -7.05835 | -43.65913 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bf8cb94f-8a61-3624-95e0-2e20fa2e8eec | -7.17095 | -37.71738 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 85cf005e-fece-31de-ad8a-ab5b4051185f | -5.8006 | -43.86777 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7bd628fd-fb90-3253-8629-79a9581f885f | -5.44108 | -45.74948 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5583c7a0-6109-33f0-ba60-26a61826c0cb | -6.22625 | -45.42675 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b4aefdb4-af12-308c-a1c5-28df19485347 | -5.99342 | -44.72344 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3cd9a7cf-0873-3ccb-88a5-669fd132b9a7 | -6.81704 | -43.72414 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 410b0fb1-e49b-3844-a932-a4cb83347803 | -6.23302 | -43.74843 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 427064dc-1425-374c-ae92-8663cea20290 | -5.40894 | -42.96933 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ec1e0e75-70ac-3198-9585-3ed799a29000 | -6.18624 | -35.69487 | 2026-09-21 16:03:00 | NOAA-21 | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a07687ea-936b-3014-a6ba-3331adba18b2 | -3.22034 | -42.46428 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README166.md)
