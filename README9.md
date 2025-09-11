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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 696be1aa-5e6c-3671-abd1-54a8ce05eee3 | -11.34 | -46.4741 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f09ae3ee-8b9b-3162-ba92-6b61bb2c9c83 | -13.1644 | -45.2897 | 2025-09-11 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d96704ea-9e81-3d38-8488-ddc84359b1ca | -13.1648 | -45.2665 | 2025-09-11 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 335e111a-d78d-329c-90c7-757de18180e5 | -8.5275 | -45.7014 | 2025-09-11 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 29dc2758-ea00-3bc3-9899-044714543864 | -10.3696 | -50.5283 | 2025-09-11 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 093e5474-439b-3cea-889c-e862941b076f | -8.5089 | -45.6807 | 2025-09-11 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a8288331-2379-3ecb-b9e2-7570eb9d1f8b | -14.7527 | -60.2321 | 2025-09-11 02:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 853031b1-95e3-37f0-b0f7-c5c18f5544f8 | -10.3885 | -50.5264 | 2025-09-11 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| a1a3e603-2404-30d2-a74e-d3c92584bc8f | -11.0393 | -45.0564 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| acdb9bee-4872-32a6-9b98-a96f7f15c7b9 | -9.0232 | -49.7834 | 2025-09-11 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| baf53031-ca8a-39cb-86da-132fca0598c6 | -22.5888 | -51.8985 | 2025-09-11 02:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| 42bb35c5-64b7-3bf8-bf7a-fd4ca8146a0c | -11.4097 | -43.5336 | 2025-09-11 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a89f36b6-38e5-3110-b7bb-dcf793c11c9e | -11.3584 | -46.5167 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4b142c92-b562-3852-9964-eda37b46ad74 | -12.3976 | -63.8048 | 2025-09-11 02:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 39940368-a523-3362-8d9d-73251fa0f2e8 | -9.0044 | -49.7851 | 2025-09-11 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7fedb0a8-e9bc-368b-92f4-1f3c05c55e1b | -8.5278 | -45.6787 | 2025-09-11 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b2e02a3c-f504-3b21-8fa9-a670f1addef8 | -14.7529 | -60.2123 | 2025-09-11 02:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 30b89c7d-54ed-342f-822c-81bc2b9e9cd5 | -9.0234 | -49.762 | 2025-09-11 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 8bf95489-3754-3ec7-8c78-acef079e33ab | -22.5894 | -51.8759 | 2025-09-11 02:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.8 |
| afed54cd-88ab-348b-a684-6d85fc5848e2 | -9.0046 | -49.7637 | 2025-09-11 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5c4ff870-c7e6-329f-a18e-9ec4a23d2872 | -12.3975 | -63.8239 | 2025-09-11 02:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 061787c1-e4bb-3768-b36a-a068fd352030 | -15.1367 | -52.4466 | 2025-09-11 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 05761377-65d4-3fee-b1d7-15f64ebba784 | -19.9994 | -47.6271 | 2025-09-11 02:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4e139817-2660-34dd-9830-a21d6f446509 | -11.0201 | -45.059 | 2025-09-11 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 9599944c-e8c7-377e-8383-2abaa03bd6da | -15.1371 | -52.4252 | 2025-09-11 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4fb9c2db-18ab-3287-8aa6-9b9da52437cc | -10.3885 | -50.5264 | 2025-09-11 02:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4c3228ec-45e5-3d07-818c-b3d8473c59cc | -11.3588 | -46.4941 | 2025-09-11 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6e995108-1efd-33cc-b919-a89ebe2cc615 | -9.0753 | -47.078 | 2025-09-11 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 09711a52-d03c-36c3-9096-f7b49fbc0de0 | -22.6097 | -51.8941 | 2025-09-11 02:20:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 5a9c7113-a6a7-3b70-9549-7b2b21b26399 | -22.5888 | -51.8985 | 2025-09-11 02:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.0 |
| bdb1706e-85b4-325a-aec1-846907248d10 | -10.3696 | -50.5283 | 2025-09-11 02:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 25c09aa5-d770-3487-9fc9-f83afadd5916 | -15.6233 | -47.5256 | 2025-09-11 02:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3497c736-cc91-38bb-a7a0-afd67af81b86 | -15.1367 | -52.4466 | 2025-09-11 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 08b4087f-facc-31f5-8982-d7624e7f008d | -11.4836 | -43.6875 | 2025-09-11 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 9f0346ff-5906-3174-b76d-a2f16499ad71 | -6.3735 | -45.1736 | 2025-09-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e19fc7b0-e9a2-356c-a187-7d3c6a60b297 | -9.0579 | -46.9688 | 2025-09-11 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 66490e2c-2b7a-3289-b1c5-c3fefab98e73 | -8.5089 | -45.6807 | 2025-09-11 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 4f2fb128-d770-3712-8d5f-1ad2022d6e51 | -22.6103 | -51.8715 | 2025-09-11 02:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| c85383cf-3e63-312e-8bb4-398428c43e22 | -9.0234 | -49.762 | 2025-09-11 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| f821cc90-0eb4-36de-8e5f-1dae69e54f4b | -13.1648 | -45.2665 | 2025-09-11 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 153f1fab-55ff-39b1-a7ed-bdea1fcbcd5c | -19.9994 | -47.6271 | 2025-09-11 02:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b777904b-d3ee-36e0-9cf1-29be0488c9cf | -20.5879 | -47.6774 | 2025-09-11 02:20:00 | GOES-19 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 43.2 |
| e980f26c-99b8-3265-bfcb-2a9097ce0ab3 | -22.59 | -51.8533 | 2025-09-11 02:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| f1af1bdf-d4ab-3415-b353-77a22409f171 | -8.5278 | -45.6787 | 2025-09-11 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 258.9 |
| 743b6d83-f2d7-3c48-8a1d-b836abd14917 | -11.0201 | -45.059 | 2025-09-11 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 6f114a44-5d01-3307-9f8c-3da03dba8e4a | -15.1371 | -52.4252 | 2025-09-11 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ef0be8f5-6ce7-3f53-abef-9a9a415403f9 | -11.3584 | -46.5167 | 2025-09-11 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d3793515-c01d-3896-af79-87dd56e24aab | -13.1644 | -45.2897 | 2025-09-11 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 8f6f9f97-2966-3a5d-aea9-100ce0d0f776 | -9.0232 | -49.7834 | 2025-09-11 02:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 1d4f4bd3-74f5-34ab-800a-f7937c4034b6 | -22.5894 | -51.8759 | 2025-09-11 02:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 227.5 |
| 24cc6f92-434b-31b3-994e-c9f4d2c59d0e | -8.5086 | -45.7033 | 2025-09-11 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e813511a-78c2-3e7a-8ed4-2836fef531a5 | -6.3737 | -45.1509 | 2025-09-11 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d040eca0-c10f-351e-be0d-d5e2cdfc92b3 | -8.5275 | -45.7014 | 2025-09-11 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fce6cfa3-8784-3371-9b70-57c4b04d927b | -11.4644 | -43.6905 | 2025-09-11 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 5e6ff899-af8d-3c05-93be-8dc72be1035e | -15.9865 | -42.9719 | 2025-09-11 02:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8308ff4e-1627-3b5a-9906-3164fc2f802e | -11.358 | -46.5393 | 2025-09-11 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0f503438-4965-31a7-a420-1b49295acdca | -11.484 | -43.6639 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| c6e0f49f-1e6a-37f4-9885-4e5a1f409748 | -9.0232 | -49.7834 | 2025-09-11 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3953263e-c7c1-30bd-90ef-8741cda4b8d3 | -22.6103 | -51.8715 | 2025-09-11 02:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 194.2 |
| 642c0aa3-c42c-3138-9143-2d6195f23d6c | -11.3584 | -46.5167 | 2025-09-11 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 30b92f74-262b-3234-85a5-db8f32ba8a0e | -15.1371 | -52.4252 | 2025-09-11 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 81d505f6-51a8-33e1-b5c1-c4da23f3b640 | -8.5278 | -45.6787 | 2025-09-11 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 09eea76a-cea8-3a47-b798-3efd110104b1 | -11.3588 | -46.4941 | 2025-09-11 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 59f250bd-9d2c-3661-ac7b-bc51e76b8938 | -11.4661 | -43.5959 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a0a227d2-6c82-30cb-ac47-718d234b94c3 | -11.0201 | -45.059 | 2025-09-11 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 949569a8-4366-3735-a96b-f7ada7456b0c | -8.5089 | -45.6807 | 2025-09-11 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.2 |
| e5838b3f-f8ee-32ac-a828-e4dd0212fb6d | -9.0753 | -47.078 | 2025-09-11 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ad884995-2622-3aca-bbbb-ebeef99d3b3f | -11.4849 | -43.6166 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7dd6a3d5-19b9-34e9-a9d7-2eb27afae5df | -19.9994 | -47.6271 | 2025-09-11 02:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cb1970d0-e73e-326f-81f1-f7fef3ccdeb0 | -22.5888 | -51.8985 | 2025-09-11 02:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 255.9 |
| f0405359-e834-3109-9186-22731a6f26d4 | -15.1367 | -52.4466 | 2025-09-11 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 02af9777-82a9-3fa7-ab06-63a25213b094 | -11.3771 | -46.5368 | 2025-09-11 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| bbbaff88-6617-3be5-85ca-5369decc9a29 | -10.5482 | -49.8899 | 2025-09-11 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 18a340bf-49e5-3f8e-a1a3-2b7006150940 | -10.3885 | -50.5264 | 2025-09-11 02:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 154e6d09-726f-3061-9287-065b53a68a46 | -9.0234 | -49.762 | 2025-09-11 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 886a549b-852f-3a00-b627-65f31e500be5 | -9.0579 | -46.9688 | 2025-09-11 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b5688895-4721-3567-961a-4821c14be87a | -22.5894 | -51.8759 | 2025-09-11 02:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.3 |
| 03a082ca-2a0d-3d99-8480-7639418aabd3 | -11.4845 | -43.6402 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 8df47979-56a8-32dd-b604-2331533d0acb | -13.1644 | -45.2897 | 2025-09-11 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 2d217854-6b40-302b-8d2d-88fa26ee73b0 | -8.5086 | -45.7033 | 2025-09-11 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1e7b5c08-908f-390e-a67b-8f0c547b9c75 | -19.979 | -47.6318 | 2025-09-11 02:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| cef804a9-97be-3bcc-a186-4e992406c080 | -11.4644 | -43.6905 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| f67172b2-bae6-3e96-9c12-08c2f9b8d531 | -15.6233 | -47.5256 | 2025-09-11 02:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 47.9 |
| d84a05c0-5f01-3e7a-8a3c-8dbfde1c1dd4 | -11.4836 | -43.6875 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 81549cff-67ee-3072-bbff-65c3cca512b9 | -22.6097 | -51.8941 | 2025-09-11 02:30:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 146.6 |
| d1a73c1b-eb39-378c-bc14-85cc7286a011 | -11.4473 | -43.5751 | 2025-09-11 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 2e61b3f9-7184-3ff3-9f06-a941facad955 | -8.5275 | -45.7014 | 2025-09-11 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b14fdcaf-d003-3853-8f95-36a65e53377a | -15.1141 | -49.509 | 2025-09-11 02:40:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a5146d65-ae28-3254-a669-e9573ead0fac | -9.0234 | -49.762 | 2025-09-11 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| da6d5f7b-ccd3-32a9-9052-bf96010bc5ad | -8.5278 | -45.6787 | 2025-09-11 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| eed0d8d9-efee-3a2d-b19e-e086ce8fc1e2 | -11.3775 | -46.5142 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5de729d3-3a7f-32b6-9bad-635744e30671 | -11.34 | -46.4741 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f1b61f9e-d13c-3d69-83b8-fcd4c275ea09 | -8.7361 | -47.0904 | 2025-09-11 02:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| bb405bf5-a638-3239-8861-6b8c112bf734 | -14.7334 | -60.2337 | 2025-09-11 02:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 9cba42b4-5dd7-3261-b228-1e0722df7843 | -23.6383 | -51.6686 | 2025-09-11 02:40:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| ec6356e9-dff3-32cf-9e7e-d98721e0073b | -9.0579 | -46.9688 | 2025-09-11 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7edee1d9-0ba7-34b0-95d1-3097a4a51b3d | -11.3584 | -46.5167 | 2025-09-11 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4238ca3a-593f-3dc3-b521-72402b7998c0 | -15.1371 | -52.4252 | 2025-09-11 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 14ef5c70-4828-359b-8fd1-3f8fbfdbc026 | -15.1336 | -49.5059 | 2025-09-11 02:40:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 10890779-3b90-3813-9598-72f5dbf3d269 | -13.1648 | -45.2665 | 2025-09-11 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |


[Clique aqui para ver as próximas entradas](README10.md)
