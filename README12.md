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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb06b1b7-5e6f-3820-a0b3-dcb29da9c323 | -4.80827 | -45.77404 | 2026-09-20 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d32148e-e23f-30e9-86a5-d8b451e9376b | -6.30554 | -41.76264 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d54f3583-79e3-3ab5-91d3-6525679d31be | -5.64165 | -43.37749 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f10e14ec-25cc-365c-87d7-5e5283330424 | -5.10891 | -37.68629 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89b2d7a1-b1ff-355f-8f98-b2e4f9963c3a | -5.41404 | -44.27673 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 392f374f-e6f1-3be0-9b67-2975fc3e5f5f | -5.41292 | -44.28337 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33d53fd0-26e5-3f66-aa1b-f5cc0252e52e | -6.15552 | -43.83089 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d87419fe-a6be-32ed-8b36-b040efa7f460 | -5.40534 | -44.28619 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 154bd899-2288-38d4-84b4-19e4bf40a0c2 | -4.68099 | -46.40452 | 2026-09-20 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b649db3-4482-3775-bdb9-99204995ed0f | -7.05325 | -37.98215 | 2026-09-20 03:42:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d53056f3-bcc0-30bc-a6a3-9d273aa76f94 | -5.45448 | -44.31851 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 49da9b27-1527-3713-b9ca-8cada94c0de6 | -3.85246 | -45.42727 | 2026-09-20 03:42:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6aeb9f5-7d0c-3a42-901e-ce160e60834f | -5.93536 | -35.61875 | 2026-09-20 03:42:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0b0076a6-6e14-32ed-8209-53d24d3a384e | -6.15093 | -43.82716 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbba5cdb-377b-3620-9c36-b8c220f26556 | -5.8315 | -44.13647 | 2026-09-20 03:42:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fcf1845-3688-3524-adc2-37fd6a78594e | -4.84605 | -40.5264 | 2026-09-20 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5363ee0-f2eb-3d44-a952-ee2310f26685 | -6.15448 | -43.83678 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7b30e59-c54d-32af-a8b1-8a1a891e165c | -5.40707 | -44.27635 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb46a20f-69aa-3936-823f-eb8de33f516c | -5.41124 | -44.28375 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32e84ccc-d2eb-3732-b64a-de1ed8c11cd2 | -3.57363 | -43.47536 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f496e8b8-b06d-3cfb-862f-deb7d09ddbad | -5.62446 | -40.85453 | 2026-09-20 03:42:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b2f0d18f-5fe0-3d71-9b3b-e550b055b091 | -5.62022 | -40.8541 | 2026-09-20 03:42:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a384575-5785-36b7-a6f0-9ef8f9ab6418 | -3.41427 | -39.28195 | 2026-09-20 03:42:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f36e7a8e-e905-3261-9623-99d10f7f302b | -4.1024 | -39.0747 | 2026-09-20 03:42:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 60037fab-0d33-3a9a-89ad-a04efe8b75ac | -5.66819 | -43.37577 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32292c27-ae1b-3a0a-a3cf-9a1680083bc7 | -3.34467 | -42.7717 | 2026-09-20 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99fdfd76-c1a8-3a7f-bb3e-4ff8432c7bec | -3.50338 | -43.35557 | 2026-09-20 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 208a3ea2-2f35-33fc-b1f0-def6c725ee99 | -2.82966 | -46.71117 | 2026-09-20 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21ddb751-39fc-35c6-81da-4fd52ad7290a | -7.08224 | -34.96122 | 2026-09-20 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 846f2a92-a716-3251-bbcb-f08e46017ba1 | -3.56687 | -43.48397 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e52a8ff5-35ed-30e1-9f5b-a9d27d21b5da | -5.34371 | -44.82781 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b35dada3-baf3-3aaa-9bc1-7972f6821025 | -5.35356 | -44.83652 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e90124bf-4d74-3346-91ef-cf14f2e5b204 | -4.56091 | -42.98312 | 2026-09-20 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 066b05d2-c553-3a4c-a4fa-68ef218c6dc0 | -4.81242 | -45.7733 | 2026-09-20 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb1b189-dbc8-3e0f-a762-453cdad1f045 | -4.84475 | -40.52179 | 2026-09-20 03:42:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eaf12f17-f65a-30f2-95c9-626c27c2cfd3 | -6.31141 | -41.75476 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 95556b36-5239-33a8-8af0-645db6489d19 | -5.5761 | -36.25877 | 2026-09-20 03:42:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9838f25a-847d-3bda-b625-5373c2cc620a | -6.02501 | -45.41027 | 2026-09-20 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c41b2a5f-8242-3fae-944b-682887e420d2 | -4.68718 | -46.40548 | 2026-09-20 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e76b3efb-2841-3306-999c-e4a6dacc34ff | -4.29577 | -48.63205 | 2026-09-20 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82358d96-f072-3822-9727-a4813fff973d | -3.56791 | -43.47769 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5603a364-dba3-3a65-8f80-2d944c4f6eed | -5.40704 | -44.2858 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa528f6b-ebe8-3dab-b338-da726d495a82 | -6.2595 | -42.72292 | 2026-09-20 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 445b57e2-e982-3732-b337-65f3c243d193 | -7.4364 | -44.69048 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9163ec98-bad4-3243-b4e3-b84593d9931d | -10.14066 | -45.5604 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9487347-400a-3f3d-b186-80748e5eedc3 | -7.44343 | -44.74301 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0b6f4999-d40d-30cc-9319-19da1ebf9ad2 | -11.8647 | -47.65372 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55407740-c1ca-37fe-8a67-c825c283975b | -13.0342 | -46.92466 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f817be8-cef0-3999-ae19-327ecf24cd32 | -7.05962 | -47.5382 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfc7bc1a-602b-372f-86a9-344af26f0894 | -12.15338 | -47.03301 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d1462184-ad93-342a-9356-53c540d47acf | -7.39221 | -47.77466 | 2026-09-20 03:45:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fb38122-b0e3-3f04-b925-d21615b91545 | -13.02264 | -46.92505 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92bd4679-0193-3940-b71d-e438fc8508b9 | -13.02823 | -46.92238 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 11983c13-9038-39c8-b649-81fffeb77fef | -9.5392 | -45.40824 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17c8d9b7-68fb-33e9-ac16-8ce080b83347 | -6.78137 | -48.66057 | 2026-09-20 03:45:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d12d42b-6eab-30c7-943d-10c3fffaef89 | -8.44176 | -45.83117 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e8ad70-98be-3ab1-83eb-d754439494a0 | -9.22287 | -43.17491 | 2026-09-20 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1d45bfc1-8e81-37ba-9b69-cd741ef7e263 | -13.22498 | -46.93967 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| edc848db-bd03-365d-9d81-a32887c41889 | -11.44325 | -45.34021 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0caba40c-0efa-3e70-ada6-35896a972f26 | -11.83853 | -47.63095 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d932b9e7-1ae6-3d9f-b7de-4aecead202f2 | -10.29706 | -50.26755 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 149ccc34-9e12-3145-bc32-6011f8445cb0 | -6.73879 | -44.04054 | 2026-09-20 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2da36150-092f-3fed-b4c0-dc8100d379a0 | -10.29532 | -50.29238 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13f9c23d-ec18-3910-9a84-972a8d2495fd | -6.30197 | -47.61535 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d45a1a1e-41ed-3eee-986b-a8021343da06 | -7.16048 | -47.46628 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3a307f57-5815-3172-8324-c78f2f970302 | -10.49283 | -46.26974 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| df84a680-ad05-356a-bc58-d7d408c15e05 | -11.86875 | -47.66432 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db38f3b6-9186-325c-81ce-350503dc35ca | -10.3052 | -50.24335 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2ca133c4-67ac-3b56-84e6-353286e6de53 | -9.23595 | -46.24089 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56f407c7-3d8f-38de-9a9d-a42881886b78 | -12.31492 | -50.7193 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b33435f4-ebae-3566-a387-61724299b3c1 | -8.77208 | -44.25426 | 2026-09-20 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afdfc261-2793-38e3-8398-588fcb317ef2 | -6.20505 | -47.52145 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b657f850-9326-38b0-9273-42a97fa7e36a | -11.84851 | -46.86948 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b4eff296-76d2-3dbc-9848-c2d92849c2f1 | -12.11941 | -47.02644 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f93c8a2b-fe0b-37db-a38f-c4ae009eff52 | -11.02538 | -48.30593 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1edf3ab9-1170-3148-a8c5-0ee75a4de17a | -8.18781 | -40.82229 | 2026-09-20 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3abfb18f-bbdd-311e-843b-9a835c59ecfc | -10.93562 | -48.31406 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 018aae24-615c-35a7-84a7-5304cfaef513 | -8.02073 | -43.3344 | 2026-09-20 03:45:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7c0d3acc-3b78-3dc7-9bd8-8878134918d7 | -10.60217 | -46.52468 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 633c2af1-234d-3abf-a2a4-c4790b055779 | -11.48528 | -47.77522 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 822230e3-fb12-3723-8de0-ec72fb8f3646 | -9.81382 | -48.32304 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 40eae55e-981b-3e19-9609-54194804b695 | -10.85523 | -50.17141 | 2026-09-20 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a7d51ab-b02b-386e-b375-eb5515bb4779 | -7.17057 | -47.44698 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 23964afb-fdab-3e8d-8d78-9263734dce3e | -6.31808 | -47.63748 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1e564526-2ab3-387c-b1ba-4f9d90bf2106 | -7.4369 | -44.749 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1f916781-7639-357d-b96a-1cf0302c4015 | -12.12843 | -47.04062 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d740c14c-9f6d-3696-9d7e-99718437073a | -11.03364 | -48.29679 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 966df7bb-9042-3bd0-9c75-9e676ba3e80d | -9.01766 | -44.92079 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31b82552-9406-39f1-b0a3-2216af2558e9 | -10.30097 | -50.26432 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| bd1e5f9e-d5a1-340b-b3e4-c5fe3b931047 | -12.31345 | -50.7262 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4f82db28-3ea0-3ce0-83a7-8af461c99830 | -7.59273 | -46.97288 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdb23baf-ba29-3eaf-bafa-e633c08f7bb8 | -7.09648 | -42.08252 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e19c741-8a80-30d8-9320-89e851c742e4 | -6.99583 | -42.19684 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e8742dec-7838-385b-8407-6420f926a0c1 | -10.31569 | -50.21333 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 2e9bd12a-c8f5-3250-8dd9-1b9711921717 | -9.26161 | -46.19675 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b9107c6-3e3f-39fc-907c-a0d48536685f | -9.25544 | -46.21432 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b02d959-3430-3c99-a216-b0a3b53a6376 | -11.48883 | -47.7574 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1db7d95-8102-375d-b3a2-4af1c02b4689 | -12.37059 | -45.8021 | 2026-09-20 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f06b35-b65c-3f65-8954-f645c753c977 | -10.60548 | -46.52195 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c7aa84b-52d9-3d77-b403-80cbd1ec32ab | -11.86789 | -47.66871 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README13.md)
