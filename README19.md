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
| 9d53974a-c11e-31dc-8d18-e070d2eee9f3 | -14.98516 | -43.08994 | 2026-09-21 03:25:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 24.4 |
| f37d66c5-f279-383f-93dd-43db49f73cab | -9.46276 | -45.39242 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 316468ed-4ef9-3dbd-8446-a47a74787f34 | -9.46132 | -45.39979 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 82bad4be-1175-356a-9526-f57fd8b960d2 | -11.68003 | -43.41946 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db2ff41b-1582-3d7f-a6c7-1819d46acdef | -9.44051 | -45.41069 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 40f0c5ce-030a-354f-8d00-f04e9f3b82ef | -11.33882 | -43.38155 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc23e2f0-5d35-3d53-a119-8d78970b8890 | -11.15131 | -42.82189 | 2026-09-21 03:25:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0f812ae5-be2d-384b-98c9-9b64b17cd77c | -9.45983 | -45.40741 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c9161136-0e51-33b6-a88a-ac15b75d7fca | -11.33787 | -43.38641 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6797b419-97f9-3a14-be5b-7d7d3749ef5d | -11.67616 | -43.43866 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a52e4c42-2347-3a5c-9055-e74b8d514132 | -11.67428 | -43.41818 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 620f369e-ca37-39d2-b75f-996d3f3879e3 | -15.52712 | -42.6547 | 2026-09-21 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9fe212a1-3472-3784-94db-a30f27be0cfe | -11.15042 | -42.82638 | 2026-09-21 03:25:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5a8941f-549f-36a2-965b-c40427e87b56 | -15.54903 | -42.63075 | 2026-09-21 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e86a41d2-d73d-3a0d-89e1-bf6cf24ceee7 | -14.986 | -43.08591 | 2026-09-21 03:25:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 328179d2-40a1-3d90-a1d8-81333d994bba | -9.44406 | -45.41241 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f11ad255-c97f-38e3-a769-7656572b08a2 | -9.44855 | -45.38961 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2834aadc-9136-3794-86ee-5cd274529826 | -9.44204 | -45.40321 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6ba767f0-cf98-3e1e-abaa-d8d96c2a1e90 | -9.44708 | -45.39708 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1399ba5b-49a1-3602-b033-ee5b7875ccf0 | -9.44556 | -45.40476 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0919b44a-f13b-306a-b0ac-07e7d67d5211 | -9.46907 | -45.41586 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6af315ce-42bc-38fe-9fb1-909b5202f178 | -13.17566 | -43.57037 | 2026-09-21 03:25:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 0d591144-5177-3e16-baac-2515010c0217 | -9.43909 | -45.41767 | 2026-09-21 03:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1a350dea-82e7-32dd-9de0-7f5fbbc5e0b8 | -13.71524 | -45.51412 | 2026-09-21 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0fcf4669-0c1c-3fe1-afe9-f811c7ad0f5f | -11.67522 | -43.41337 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c2ad30b-0b73-3d03-946c-201248bd6f5b | -14.22846 | -44.63792 | 2026-09-21 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b125a9c8-f193-34e7-a227-bab0b21d8d62 | -11.67907 | -43.42426 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd8b0df7-6491-31f3-ae64-998444c39cc9 | -10.47821 | -45.08973 | 2026-09-21 03:25:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97791e6f-bc9b-347a-95ee-a572c4b4ec84 | -14.22951 | -44.63287 | 2026-09-21 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cac5884e-3842-3de7-908f-e5f1f6101054 | -9.53471 | -45.40044 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f3c3930-e413-384b-b67d-ca931fc4b9b0 | -9.46343 | -45.40716 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| db347997-b924-3024-b981-8b651ade9db2 | -13.71165 | -45.51373 | 2026-09-21 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 881ff65f-d042-39d3-91bf-b0b59a84378b | -14.22556 | -44.63444 | 2026-09-21 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc0d5315-5e63-36c2-a7dd-c015a00bc10e | -11.67488 | -43.41348 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead243d1-c127-3f9c-a8a7-98b410e6b20f | -11.68131 | -43.44469 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79aed0e7-020b-3e5d-8902-8b171eee2622 | -9.44908 | -45.40499 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a9b688d-3769-3b16-a2e1-183a19d57320 | -13.2876 | -43.55284 | 2026-09-21 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47fce9c5-fba1-331c-ac00-7aab3d940191 | -11.67391 | -43.41827 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6ee5bdd-9b51-35bb-bcfb-c68f4c540e49 | -11.15638 | -42.82753 | 2026-09-21 03:25:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 667588bc-4a81-3feb-a96a-23ca6bac95c4 | -11.19878 | -42.86378 | 2026-09-21 03:25:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3de8fc70-eb8e-3dd2-9309-3f05279dfb62 | -14.62218 | -42.91544 | 2026-09-21 03:25:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a9a6cc0-5db7-39ad-a59a-4285dc239a32 | -15.52168 | -42.65353 | 2026-09-21 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 89ef5af4-4846-3c8e-9ddf-b7093cc3b2fe | -13.17661 | -43.56573 | 2026-09-21 03:25:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 1001d7f2-dbd6-3232-9c92-f40f149feb50 | -14.98365 | -43.08591 | 2026-09-21 03:25:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4e8eae5d-287e-302c-9f65-7b7f60521d1c | -11.14535 | -42.82073 | 2026-09-21 03:25:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b90a2cb-861b-3c24-b7c9-ed1c9aa79a6c | -11.67335 | -43.42298 | 2026-09-21 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a033f372-7619-3b2e-a82c-8a1728371891 | -9.46494 | -45.39974 | 2026-09-21 03:25:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| fc811814-b820-3a59-9045-b6a2a03d4eee | -19.67958 | -46.2969 | 2026-09-21 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 73fa648d-6ac8-3b43-9924-9419a08cbac4 | -19.41903 | -46.39711 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3316d25-bbfa-391f-bee2-b88781e4581c | -19.41182 | -46.39948 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3293fa04-53e2-3667-8e56-4209be458338 | -19.41035 | -46.40582 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0484cefe-a052-3911-a797-4ac34713e40b | -19.68279 | -46.29735 | 2026-09-21 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a9a7d2c9-ae78-32d1-b269-a1293c46647a | -19.41315 | -46.39374 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b177502e-7e62-3a6b-9417-7c2345c7b5cd | -18.98054 | -43.75594 | 2026-09-21 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3000dd56-0db3-36ac-9af1-3b97000335ed | -19.41637 | -46.40862 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3972f423-17f2-3519-951d-8d7d4261f6a8 | -19.41499 | -46.41459 | 2026-09-21 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec46224d-3376-38c4-905c-f7b011cccdd5 | -18.86659 | -42.00531 | 2026-09-21 03:28:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab75f5ce-6041-3f41-bd15-1f12b2034f0a | -19.68399 | -46.29231 | 2026-09-21 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d235e556-e463-3e26-b3de-cb8d55c8c47d | -18.97525 | -43.75292 | 2026-09-21 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12b13571-1521-3e92-b72f-06e24832bed4 | -19.68077 | -46.29168 | 2026-09-21 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cada0baa-7f7a-3c17-ad15-dcb7d6e5f648 | -18.97436 | -43.75719 | 2026-09-21 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dc7f83a-d082-3a78-bd67-37e533e89afd | -18.97511 | -43.75463 | 2026-09-21 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 246e02ba-a016-3533-bc0b-061a95c37c21 | -10.4486 | -50.2644 | 2026-09-21 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b8bf2886-6509-3e05-bf29-0447eca6acb4 | -15.4663 | -48.4757 | 2026-09-21 03:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 58330633-f3d7-3b38-91df-c1bc75739f48 | -7.5703 | -57.6962 | 2026-09-21 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 89275069-43d3-3b92-a547-7e5df710c6de | -11.9969 | -58.0622 | 2026-09-21 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f648b246-c878-3ed1-9fb6-fb4a0192ea28 | -10.4675 | -50.2624 | 2026-09-21 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ec174587-3c57-3bcf-999d-f5b697ca9ff9 | -10.4483 | -50.2858 | 2026-09-21 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2bce8c0a-b507-36c4-9a97-bd033e8ee896 | -16.03 | -52.5135 | 2026-09-21 03:30:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e94934c3-9eea-3266-813e-10410aea631a | -10.4672 | -50.2838 | 2026-09-21 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 25d0c7ad-32cc-3a41-a516-1a39235a7f42 | -7.4283 | -44.7639 | 2026-09-21 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f0f26afa-27f1-369f-8fbe-2dc178ef00a1 | -11.8014 | -49.8129 | 2026-09-21 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| aa08059f-42f6-3845-8d6b-050804f20a6d | -10.467 | -50.3052 | 2026-09-21 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 850a21ee-2f57-36ee-8d7f-39eadb20477b | -7.5704 | -57.6766 | 2026-09-21 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 324658a0-71e4-32b4-a8cf-4ee22318ba95 | -3.3823 | -50.4486 | 2026-09-21 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 64a713a6-844d-333d-a38f-4169bb14cabe | -3.0717 | -61.2764 | 2026-09-21 03:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a1f8740a-888d-3924-ae89-7197d6fb044e | -7.428 | -44.7867 | 2026-09-21 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b0214aa3-4b1f-312a-9e5b-61fa6122bc1e | -7.5888 | -57.6953 | 2026-09-21 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5edf00a1-5b80-3600-84f4-04bcbc6d51c0 | -18.0303 | -50.9385 | 2026-09-21 03:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 88a22a1c-47c5-3aa1-ac9c-e792e718c1a7 | -7.5889 | -57.6757 | 2026-09-21 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1a2e49b4-5d37-31be-8f27-c0f44dd53a14 | -13.1798 | -43.5749 | 2026-09-21 03:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| cde7f10d-abf0-3440-aeca-61419e873d3b | -3.3823 | -50.4486 | 2026-09-21 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4ea37500-45fb-3d53-af75-684935fc89e4 | -16.03 | -52.5135 | 2026-09-21 03:40:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7cdca9dd-941b-3b63-b75c-25a9f5a8dbce | -7.5704 | -57.6766 | 2026-09-21 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4b64e49b-7b1c-30b5-9c8c-db7463bc2576 | -3.0717 | -61.2764 | 2026-09-21 03:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6599e751-0760-354c-9ee4-76566837fd37 | -7.5703 | -57.6962 | 2026-09-21 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bf5ccab4-d4f3-3e41-ba4c-65048fae7d78 | -16.0495 | -52.5106 | 2026-09-21 03:40:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9876707c-4509-304a-a376-8bdb01c84c96 | -7.5889 | -57.6757 | 2026-09-21 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9fb9cb26-3904-3a29-bfe0-5c0b8a468c27 | -11.8014 | -49.8129 | 2026-09-21 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f8190ded-fe29-34c6-b508-9bea1f510927 | -10.467 | -50.3052 | 2026-09-21 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1991d5fe-348e-3711-87d7-212950ad5cf7 | -10.09 | -50.2581 | 2026-09-21 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| bee82d81-bc29-39d9-a6da-b6129b1a866b | -10.4672 | -50.2838 | 2026-09-21 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| b22d33c0-42ff-3399-b603-47b586f74761 | -10.4859 | -50.3032 | 2026-09-21 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 83953e74-a022-3c6e-aa23-81b43ab99343 | -7.5888 | -57.6953 | 2026-09-21 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7f8fb007-552c-33be-a7fd-a6fa2a94a21a | -10.4862 | -50.2818 | 2026-09-21 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c112eb6a-04d0-3da8-9bd7-3d607b00bb29 | -13.1798 | -43.5749 | 2026-09-21 03:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7fe30b15-deaa-3913-9bfa-e3e58d84caaf | -15.4663 | -48.4757 | 2026-09-21 03:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 172504ee-c4de-3ba5-95d2-434f07c6882d | -7.5704 | -57.6766 | 2026-09-21 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1860688f-19cb-3aab-be9e-baacce3f75cc | -3.0717 | -61.2764 | 2026-09-21 03:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d91638d2-813c-35b6-9483-20cb8c0a6575 | -10.09 | -50.2581 | 2026-09-21 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |


[Clique aqui para ver as próximas entradas](README20.md)
