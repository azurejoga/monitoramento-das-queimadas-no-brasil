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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cae4e74-9e4a-33cb-bbf9-96147f2799a5 | -6.17599 | -42.61242 | 2025-10-15 04:57:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d86687a-714e-35d8-8aa4-2a24fc3c68f7 | -5.87056 | -43.86186 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 895edf41-1150-312b-8e51-4f4eda337d0e | -6.59225 | -43.92461 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53161050-2c16-3569-8cb6-60f92bdde873 | -5.86585 | -43.8539 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c89b0e0b-895e-38a4-81c1-5013ee24e1ff | -6.73897 | -42.15232 | 2025-10-15 04:57:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0247ddf2-1e15-314a-aafb-0fb513ef729c | -5.8763 | -43.86258 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bd33432e-9b60-3ced-a9a3-a6ab32dcf303 | -6.90067 | -43.97001 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f721420-3981-3b96-a71c-4d634a8a66cf | -5.16442 | -45.16696 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac952d7-30d9-3a04-8122-c82b05572cd1 | -5.65066 | -45.87687 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5c7d3ce-58b3-31fb-8622-ba9d384fe79d | -5.47756 | -44.65876 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28829e95-2cd1-34b9-937e-f59f702537d9 | -6.85198 | -44.37082 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f2e8f6e-be91-3778-a6b0-98f27f2c4791 | -8.21096 | -44.01212 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c9a7d97-9e38-34a3-8627-cff7d568a45d | -6.55019 | -43.93218 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eb22241-5e8b-3279-8e05-e2be42eb2748 | -8.22132 | -43.31624 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9b836c84-a2cb-3546-ac3d-f43d33d6da8f | -6.44692 | -43.81944 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4cd3ed7-adc3-30e6-857a-42cd39ee5e7f | -5.47972 | -48.65739 | 2025-10-15 04:57:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d6a5d77-c5e6-3001-982b-3ab514ff613c | -5.73759 | -44.98621 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c583e6e9-1f0b-3a74-a0fc-11e102566910 | -7.93943 | -44.13847 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf9950c9-c085-31d7-8a76-1f5d32c95932 | -8.20151 | -43.99351 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7ae7e01-42ce-3fb5-b1fc-a6b093413b4f | -10.05593 | -42.6147 | 2025-10-15 04:57:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8304f8fb-09c0-3ba4-af37-411d15728f18 | -6.83076 | -44.64892 | 2025-10-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33a1087e-109a-3c24-b640-847eef00a86c | -8.2207 | -44.07047 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61714046-1120-34d9-b84d-e1289aad169c | -6.35092 | -42.65799 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8508a78-c7d4-36cd-940d-aa2fbb188a16 | -8.28116 | -43.39388 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eab67c8f-9777-306f-9c9d-d75a0ac773eb | -5.15394 | -45.69701 | 2025-10-15 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ac206e1-01a4-36b3-ab11-f67115f02eae | -6.63321 | -43.9254 | 2025-10-15 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9647c0cc-2103-335e-82c5-8b06377fa98e | -8.46033 | -44.186 | 2025-10-15 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 28a91b67-c57c-349b-ba58-257f85cdd959 | -5.4259 | -44.21954 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cb9d88dc-6456-3e58-b987-d93f57f12867 | -7.16214 | -42.49607 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e3cc917-0d9a-3f6a-baa6-f897fdf0620b | -6.31282 | -42.99019 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e55fd16c-2d86-39ad-a8ce-2dbc4fe01412 | -8.21457 | -44.02974 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f79886-ebb3-3d73-ad30-7a69ebeeabea | -5.26362 | -45.60944 | 2025-10-15 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e04ae15-1ea0-30fc-ac92-60f50f12bfbb | -7.95099 | -44.14008 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 488e8652-2a3d-3319-8627-db54f8a175bf | -8.24926 | -43.34606 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d8f12181-c6b6-338d-b4e0-7758aa8f2775 | -5.48026 | -48.65374 | 2025-10-15 04:57:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9e4c664-eec1-3208-9d60-27d189e6dabc | -8.25536 | -43.34702 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c9e333fc-4208-371b-9509-215151e49a90 | -4.91976 | -48.1671 | 2025-10-15 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 626373cd-deed-3b4f-bb73-189321a61648 | -5.77035 | -46.00616 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ba92e3d-0fbc-3ac0-89eb-2db4d491667e | -9.96565 | -49.8106 | 2025-10-15 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e9e1cc-0b3d-3b93-be98-265a2afd528a | -5.87111 | -43.85794 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 203206a4-8d22-397e-bd2b-b9c8e0e785de | -7.79438 | -46.02222 | 2025-10-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6f18232-a00f-3214-a657-f2e8bddbc6d1 | -6.57956 | -42.95819 | 2025-10-15 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b64a180-3c40-3111-a3fa-39a5a346d870 | -8.20585 | -43.99966 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dd3a7f4-a7df-3a81-adf6-e4d731be0332 | -7.57157 | -42.68299 | 2025-10-15 04:57:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7bc61f81-5b80-378b-a2a2-6dfaa5cd315a | -5.34628 | -43.74538 | 2025-10-15 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a11399a-c381-326a-82ad-7994cb9ec554 | -5.83849 | -42.32935 | 2025-10-15 04:57:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 9329cd69-e31f-3313-b52d-ad7414ad05bb | -5.58387 | -44.74363 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5b51a13-2ca5-3f7f-8f3f-96962c3a68b6 | -6.55126 | -43.92419 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90801bfd-a004-39ef-b674-c16b66d4789e | -6.52728 | -42.20116 | 2025-10-15 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b735eb0c-8833-312a-ab66-68a6f9fb118b | -6.1741 | -42.6169 | 2025-10-15 04:57:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 50a32f97-6c5d-3e88-97e3-9646778e35d0 | -5.40925 | -44.21707 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3d837f-3b40-3e9f-8151-b7c20d15c53f | -8.21949 | -44.08167 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2417ab7e-e526-313c-a076-8e56b87e990f | -9.01395 | -62.00227 | 2025-10-15 04:57:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48209dc4-0065-36a6-8357-6539fc763c0f | -6.30528 | -42.99201 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb3aaa82-7b6e-3fd3-bc56-4d480a7ff96c | -11.71634 | -44.27583 | 2025-10-15 04:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44097a95-81c6-3909-8913-94337fc3a033 | -7.48058 | -42.15129 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 406a51d6-fce5-329a-8a32-7a1119bb6539 | -5.86999 | -43.86592 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e67bd91e-75bf-32df-98ae-147ae0ae0ef8 | -5.43507 | -44.23034 | 2025-10-15 04:57:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7a19398a-4632-32db-9f20-3c46f0e61a02 | -5.85848 | -43.86484 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5904256-451e-373d-9d01-a29f1fb724f8 | -5.42482 | -44.22696 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a769ff4d-f5ad-3b69-a96e-ce6ef9c71d1c | -6.05751 | -41.88884 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6658af63-60ce-3bba-973d-54fef7450623 | -5.68024 | -45.16821 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c8079fc-ed8b-3d66-812b-27ef95c869ac | -8.28695 | -43.43781 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5942ac9-77a1-3241-9e8b-ed392feb8421 | -8.28799 | -43.43864 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ec4a33f6-418d-3447-ae2b-b69180444350 | -5.27289 | -45.16947 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5aa78cf-d940-37c8-b033-efd97ac49e9c | -5.11805 | -46.05096 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc6fbc9-77d9-3621-b1f1-afcba5bf8528 | -6.63437 | -43.92649 | 2025-10-15 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd97e01d-eb6b-3231-ab95-5554d3b85d4f | -6.44745 | -43.81544 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91ead8db-369e-333d-a88d-535f7d2db39a | -5.85904 | -43.86087 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab9f2aef-9cd1-3f13-9a33-106926ffac03 | -8.45936 | -44.19346 | 2025-10-15 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 68a335fb-59bc-34fe-9e01-ddaf33fb7aa4 | -5.18274 | -46.17656 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41e98da6-ad9e-32c9-a98b-e087a0dc6d41 | -6.44763 | -43.37575 | 2025-10-15 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cafb326c-4b7f-33dd-8c59-1bc75f1d2739 | -5.84539 | -43.95857 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1dd683a-817e-3e51-93cb-d063c7299229 | -5.82591 | -42.32734 | 2025-10-15 04:57:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12323d55-9374-35bb-9584-e7ad645da45d | -8.25475 | -43.35171 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f34cea03-b26c-3413-9dc1-e202cbb98f28 | -7.57594 | -42.69899 | 2025-10-15 04:57:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3759508-f1e0-320f-833c-871cf951aa35 | -7.75162 | -42.46196 | 2025-10-15 04:57:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 107a9e31-1ffe-39cf-ad2f-5c139c7cf2b3 | -8.28634 | -43.44244 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6855851c-c11c-3fd0-a519-437c96a2d515 | -7.08296 | -41.95123 | 2025-10-15 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5f28328e-052d-3c04-bb8f-109015151bfd | -8.22531 | -44.08253 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67f65b6-23da-3efe-8308-261182058d25 | -8.22061 | -44.07338 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf6c0b40-3d84-3187-8e36-bca44a62175d | -5.42491 | -44.42533 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 632ea5c0-7786-3381-bcdf-e6c794ef0203 | -5.92129 | -42.82191 | 2025-10-15 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 50708f70-beb4-3fef-877a-ce4001e44fcf | -5.46775 | -44.65001 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc92644-3bae-30c7-b062-581484b8990b | -8.21542 | -44.0183 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e9ff49-d6b2-3718-8c30-2b42a9c00899 | -6.55071 | -43.9283 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c67cfd3-bb3e-36eb-9689-2b37a049df0c | -8.46567 | -44.19036 | 2025-10-15 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7c0a978b-e845-3171-bec2-2d63a172b981 | -4.91453 | -46.70701 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1399539d-20b1-3f2f-9f1a-b627ea34840a | -8.24316 | -43.34515 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 8c96881b-5e9e-3342-bb44-8dfa12c59e81 | -6.34255 | -44.01766 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04b83d12-b18c-379c-9810-5bb833f82abd | -10.7217 | -44.17125 | 2025-10-15 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82f9477a-cbdd-3f22-8f73-87c0473e9ca2 | -6.22755 | -44.16244 | 2025-10-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed374f49-858a-3321-8f1a-655f590e34b2 | -7.95567 | -44.14918 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e27c392-eed6-3c0d-ab5a-4e33d75f18a1 | -5.24832 | -44.47327 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b438772-2d12-3464-91b5-f804f1d91ed0 | -8.21436 | -44.02667 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66d2c40a-781f-3d11-8810-6699f5169839 | -7.7459 | -42.45576 | 2025-10-15 04:57:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 13f5d820-e520-3a58-a2bd-ebf5db3df6e6 | -6.22636 | -47.03698 | 2025-10-15 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7718356b-057e-3482-99e6-73c30f47b132 | -8.20886 | -43.32136 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 06992bd4-0ee5-39e3-a807-59b3e88d8f33 | -6.23265 | -44.1672 | 2025-10-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c2b9f17-8d5a-3da1-b82c-d1bacf1860b1 | -7.93997 | -44.13437 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README46.md)
