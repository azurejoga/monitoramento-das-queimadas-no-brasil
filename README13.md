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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34e2d3bb-9c19-3c7f-aa98-fee7e5017f16 | -3.87382 | -42.51497 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 137ef937-099e-3605-a4b4-9559b2780b98 | -2.92367 | -48.30015 | 2025-10-12 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24ad2cbd-072d-35cc-b0fe-1e78864fed12 | -4.42191 | -43.46618 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6629694a-aee5-3708-b0be-24dae06d95d6 | -3.34765 | -42.15445 | 2025-10-12 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a095eaa9-f57c-3989-97fd-2a0143e5d562 | -4.41859 | -43.46566 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14e7f203-8ed5-3271-b272-c5b81aa8267a | -2.43775 | -49.36586 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02ba5f5a-667c-3db8-a300-d38ba5594c9f | -3.1453 | -44.43042 | 2025-10-12 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daea7403-0a6d-367c-8490-383b2ecfc5e7 | -3.60781 | -44.45984 | 2025-10-12 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd2082af-4533-309b-bfe4-7c5bbc509d17 | -3.77146 | -43.89751 | 2025-10-12 04:12:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25d5fd39-9973-30b3-bd6c-8c1cd987c4d4 | -4.01263 | -38.73192 | 2025-10-12 04:12:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| adde99bb-0688-3bed-8ed9-64aad7720718 | -3.52954 | -48.91564 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bcd53a84-cab9-3200-bd71-674e451693c6 | -4.01497 | -42.06559 | 2025-10-12 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e9808b6-ccdd-3258-bad5-9a054313a7f7 | -3.53396 | -48.91635 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a19a151-4b30-380c-8cf0-539e0274a2f7 | -4.41196 | -43.46463 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53775e01-5d6f-3fd2-bfd5-f7830d4184a6 | -3.45157 | -45.60424 | 2025-10-12 04:12:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd7cd61e-ac83-3047-b904-ecc1d02acac8 | -2.43856 | -49.36099 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a997943d-dd08-3802-91b2-04ef729707ce | -4.38048 | -43.29606 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1b04d60-0a91-362e-affa-49eea1c7c33f | -3.53767 | -48.92144 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a96543c-b1bc-3440-9c0a-65f975551fac | -3.19591 | -49.48193 | 2025-10-12 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bb7a3cf-7899-3904-815f-a9c9b27ee880 | 1.17089 | -50.89991 | 2025-10-12 04:12:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d86031a7-4267-33da-8dc5-50b7b03dff96 | -3.60309 | -43.8454 | 2025-10-12 04:12:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 196306cb-ab30-3fc8-a43d-0f13142fcde5 | -2.43694 | -49.37075 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1e953d2-3791-379e-bc5a-78962cf51223 | -3.48211 | -41.60001 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a8b3751-ccb7-3eae-9cef-999126b6774d | -2.26685 | -47.85042 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c0f45ad-6be1-3b7e-9ae3-532162328aa7 | -4.42747 | -42.12706 | 2025-10-12 04:12:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dabf530e-3e64-34e2-b50a-5a3bd8be4287 | -2.79243 | -49.62223 | 2025-10-12 04:12:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e4873d8d-2b19-3b65-b0bb-d8706f84d0e1 | -3.60335 | -41.62944 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b994ff39-1cd0-3b64-97c0-318da76eb50d | -3.60057 | -41.62544 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d2f3e6b-9ce6-32d3-af79-40eeee9ea9bf | -4.01551 | -42.06215 | 2025-10-12 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f370499-7352-31a9-8785-5a9845e3d202 | -2.71775 | -48.35668 | 2025-10-12 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ed002e1-3236-381c-81ad-82d3f4b7b51d | -3.19672 | -49.47702 | 2025-10-12 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c989676-170f-3e03-895f-a7446fe5fc24 | -3.60667 | -41.62995 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5705a42e-848b-3019-9799-9c6ac94c5765 | -3.51107 | -45.84522 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c13dcfd7-0998-3105-87d5-ee8f3bb2d2a1 | -3.53004 | -39.77755 | 2025-10-12 04:12:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b5811db4-f5ff-3911-8d61-b4f3c63347f9 | -4.40594 | -43.52432 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faa7243f-cb04-3323-8d54-f078030358d0 | -3.95728 | -44.27312 | 2025-10-12 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0c377b5-502a-36a1-b187-ced8808c5117 | -2.44705 | -49.36731 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9149745f-eb5d-3490-aa74-7cb06ba4476c | -2.4533 | -49.35834 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2151bc81-73e9-3169-bc01-8449c3b2b704 | -3.22232 | -44.12154 | 2025-10-12 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a07695a3-2f77-377d-a318-45794804173e | -4.41246 | -43.11364 | 2025-10-12 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c0eb63f-2208-3409-a0fa-1a9000bc72f0 | -3.60554 | -42.75057 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c023f7b8-be7f-3c84-9647-a49a23377950 | -3.52882 | -48.92001 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac59fa73-72d7-3c8c-b3b5-adc8a1f94203 | -2.4525 | -49.3632 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e4e64d-46b0-3d6d-a000-e0a9907b6a46 | -3.9505 | -44.27208 | 2025-10-12 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4c2675b-efbd-3b61-b54f-7ec968fa3951 | -4.40907 | -42.89816 | 2025-10-12 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 771dc801-f16c-3ae5-b461-ecff9902b1d0 | -3.76811 | -43.89698 | 2025-10-12 04:12:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9787fa31-1029-326b-bc7f-255441ce1fef | -3.97784 | -42.82674 | 2025-10-12 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 71039439-a370-320a-95a5-267c540adbc5 | -5.26507 | -43.10382 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76f86235-047c-31b0-99a8-7de8b9b18b1f | -6.76986 | -42.82042 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b7bf184-0991-3c99-ad3b-9bcdfd0e3b04 | -7.27051 | -42.97057 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dae4d79f-1c3c-38b9-8d69-a4c2625e4a32 | -7.43619 | -42.97514 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80f3dd6d-5a12-3e46-aace-b259c497a32c | -8.83197 | -46.04279 | 2025-10-12 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4865bd2-23fe-3cb0-b5bc-ed39a969ba62 | -5.30774 | -42.8746 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e4ddb02-c3af-3259-9f30-c50c0335eb02 | -7.40649 | -42.9705 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 555c3c4b-6710-3c87-bb2a-b9b4bb2717c4 | -7.85841 | -44.53118 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c0e36566-de13-3ba3-8fcc-2208de125f90 | -5.42606 | -41.37188 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d40eb39-326c-3233-997e-3f11a1923d78 | -6.04149 | -42.47218 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b346e0f-0ec3-3138-b6b6-7f01d9906d50 | -11.72905 | -44.28822 | 2025-10-12 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24597412-5b44-395e-908f-9f9cafce00d5 | -11.7514 | -43.31046 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 629ba69e-bfcf-3594-82ad-8a1eaa077098 | -6.76656 | -42.8199 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d9bc153-5376-3a0a-8ac2-fcaf9e2ab098 | -7.15276 | -42.50005 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9fcc5893-66cf-3bf5-a223-87b53d921ea0 | -5.48785 | -43.07228 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afa58f51-a0fb-34b6-b7f8-2b7df7aea2e9 | -6.24466 | -42.93488 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1001bdc1-92de-3341-9259-89fe4c87eb03 | -7.74598 | -43.16947 | 2025-10-12 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ddaa408e-1a94-3ac8-845d-4d05a658a874 | -6.98676 | -42.031 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 06e4984a-b3aa-31c0-96dc-a9f6c69ac20c | -7.52445 | -44.29677 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efb6e3cd-f54d-3483-b23e-28f22b55e2d4 | -5.46958 | -45.23451 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5166d0c6-ea3c-340d-ac61-5e16f031945c | -6.57285 | -44.71056 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e9e602a-075d-332a-a5db-b1d1fd832c55 | -9.56271 | -46.90855 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ab2c9d-56e2-351b-87f0-807fbd699898 | -6.59244 | -44.40145 | 2025-10-12 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b19fd46-9d35-3199-8592-bdfff0d374e5 | -7.43013 | -42.97066 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 31ea1a08-77c0-377f-ac0e-9b6b81e446c2 | -6.24957 | -42.92506 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33684a69-20bc-3e4f-92b7-3785ee851384 | -8.70188 | -40.54377 | 2025-10-12 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| acaf2658-b75e-37ae-8abd-6630e52a70c9 | -3.19348 | -52.2368 | 2025-10-12 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42c21b55-885a-3dd2-96c6-a556c3b67bc3 | -7.5424 | -43.83841 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48c46988-35c7-3ec1-b53d-dd7607552ab4 | -6.25374 | -43.02798 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5db3297-1946-3203-a1cf-153f2480e5fe | -5.93651 | -43.9423 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d7d4c1a-f856-3fb7-9905-dc0e589dd223 | -5.93319 | -43.94179 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cbddd0f6-8040-36ee-bdb2-3004cccfcc59 | -7.86953 | -44.52568 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebcee971-618a-385f-bbc6-089a23396f86 | -5.583 | -41.10608 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9fd049f-1c78-3a0a-b1e8-5beaf111b270 | -5.6557 | -42.78169 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1eaee62-f4fe-3814-bd0c-3b64d7452865 | -7.51944 | -45.13808 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb37134-a48a-3489-909e-4647fffc6e76 | -7.69885 | -42.37691 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb15b807-442b-30cf-8f5a-746c781ffd70 | -7.07663 | -42.74821 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b49915d-7236-3a69-a71a-e2f33d6a5a50 | -6.58075 | -45.97919 | 2025-10-12 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d1bc7df-a920-373f-b7cc-35b2c30b8ab5 | -7.7986 | -42.43564 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9fe71921-1b3c-3cb3-a125-4e02f8d7b1c2 | -9.26437 | -40.43625 | 2025-10-12 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73ac164a-624d-39bc-b55e-359c2941f1e2 | -6.75633 | -44.65486 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 881e7110-c741-3fa9-ac22-ac01afb9475d | -5.91114 | -45.43266 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2e7da05-9055-32c2-bb0b-83f31946ab9b | -5.97905 | -42.14875 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d26317b-85f5-3534-b9e2-32dfef6ae21b | -5.49499 | -43.06987 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff7d2105-4b97-3911-8250-246b6a63a9ae | -8.63527 | -47.00121 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c40380-1a32-39db-9a29-baef8a247576 | -5.65072 | -42.77035 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 664d8802-a639-3248-b123-7e5b0820a003 | -7.74306 | -44.07686 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1363bca2-0801-36cc-8e4f-a73ed799b348 | -5.93983 | -43.94283 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a89cfcd4-ff45-33a3-9507-9f041d44cb01 | -7.85458 | -44.51225 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58c86f02-fd79-3bac-bf2e-37053a3c13bd | -6.31871 | -41.59975 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c014dee7-9118-3800-9af0-4e79838726c0 | -10.97113 | -43.0313 | 2025-10-12 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f611644-a608-3af2-aba3-fa965b1f893f | -7.42699 | -45.16491 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3d6007c-02ea-3cfc-9f10-a52dd00b8403 | -6.11939 | -42.23173 | 2025-10-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README14.md)
