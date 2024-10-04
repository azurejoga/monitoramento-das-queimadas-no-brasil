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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbbb1d01-dd73-3c95-86b7-17ed1eaaec59 | -18.03868 | -42.61315 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 89e50e44-111f-37cd-8dea-58e54ffc0a67 | -18.03805 | -42.62095 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5614b9c0-dac9-399e-b89b-718a5230fdb3 | -18.03402 | -42.62022 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d19a237-4048-3f20-b2f5-8a52bfbc6f9c | -15.59177 | -43.65509 | 2024-10-04 04:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a2c1c65-f960-33f4-980f-0f867a056205 | -15.95569 | -43.36828 | 2024-10-04 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2554b37-f1dc-3941-99b6-0805c93d86b2 | -15.9551 | -43.37428 | 2024-10-04 04:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c785f7dc-b85b-3754-b015-2e16f421c198 | -15.59235 | -43.64922 | 2024-10-04 04:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d0f5686-7944-3627-9e64-819c7e4a2da4 | -17.74314 | -43.81661 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 01a8c596-3554-35d5-9334-10960c032b64 | -17.74266 | -43.82164 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f1eae06a-9863-347d-ba71-61dfaf65dff9 | -17.74179 | -43.8105 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6bed6d1c-1bdc-3e63-a191-4a85f6a6330b | -17.74133 | -43.81567 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c3e02374-cb75-3fd4-bd2c-5caa0ec50c56 | -17.74088 | -43.82067 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c70e7853-c0c9-3717-863c-df8c254c7604 | -17.73812 | -43.79921 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ef12a65-eea8-3d3d-89f1-1686d29a387c | -17.73704 | -43.81046 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9bbf2ac2-e687-3c64-8d09-33a2eae379b8 | -17.73655 | -43.81572 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c23b69b-2847-30a0-aae7-6452ab06bd0c | -17.73606 | -43.82082 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| af8e78da-74bb-359b-bbca-9b6d0d0218cb | -17.73518 | -43.80968 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cfb32283-fc79-3424-aea5-e30eaa12e3c2 | -17.73471 | -43.81498 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4f40fa1-2c77-39db-8258-981e3c31ba42 | -17.73425 | -43.82009 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78c1b2e0-fed4-3afd-82c6-f41da948a274 | -17.73037 | -43.81029 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25674eb4-4ff4-3c56-bc5e-2400ec8d7d40 | -17.69328 | -43.77769 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 43cc2689-bfb8-3056-90f2-5a8bf1305ff2 | -17.69274 | -43.78351 | 2024-10-04 04:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 486133b7-9ef4-3bc2-9eb8-3bec118c60e6 | -17.91261 | -43.44498 | 2024-10-04 04:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3a0cc11-7db3-35f3-92b5-8ee1b22867ef | -18.58709 | -43.96019 | 2024-10-04 04:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fa0fb45-9aa8-3cdf-8b29-7aa9322eb148 | -18.58667 | -43.96493 | 2024-10-04 04:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f50229e-65b5-3c80-a68f-a19717b2b84f | -18.33408 | -44.01458 | 2024-10-04 04:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c029199-9b65-3407-8749-f589bbf8b7f8 | -18.33268 | -44.01585 | 2024-10-04 04:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6071e34-6351-31bb-a793-0fbd58fb34c3 | -18.32709 | -44.01834 | 2024-10-04 04:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 090f527c-1ebd-3511-a74c-e91b875323d3 | -18.32666 | -44.02298 | 2024-10-04 04:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bb177ac4-f9ac-3efa-be00-354cfb745618 | -18.32607 | -44.01546 | 2024-10-04 04:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74e42957-f6ee-31cf-aa89-bb2bfb460aeb | -18.26879 | -43.4346 | 2024-10-04 04:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac1b5824-32bd-3a03-923c-da124769ccb9 | -18.26324 | -43.43617 | 2024-10-04 04:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9be685c-b346-35eb-a074-47ccf8a5f346 | -18.26199 | -43.43391 | 2024-10-04 04:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6b6ae24-84d2-367d-b535-75885b7c6dac | -18.26359 | -43.43194 | 2024-10-04 04:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9f937eb-1e14-3727-b871-6d3b0f56454b | -13.6628 | -43.72998 | 2024-10-04 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3353ceb1-98be-3a4d-aba7-e1664ad90196 | -13.66224 | -43.73524 | 2024-10-04 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4c9a50e-0e60-3fc1-a5a2-131c675479d4 | -13.66054 | -43.731 | 2024-10-04 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76b770a5-a0ee-3df6-875f-560bdb52fd11 | -13.65994 | -43.73624 | 2024-10-04 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f348f0c1-b368-37be-8a91-e2128ec42861 | -13.47883 | -43.77747 | 2024-10-04 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb13ae2b-eddc-3b94-a8e8-6e3c59e5fdc8 | -12.36711 | -44.61717 | 2024-10-04 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6b896d3-98b9-3168-8a53-e83a44ac5fa4 | -12.36516 | -44.61594 | 2024-10-04 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef661186-1369-3a87-bf73-22bfdee5778c | -12.36118 | -44.61644 | 2024-10-04 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3bbf590-e296-3436-9129-495724287fd9 | -14.90975 | -45.12992 | 2024-10-04 04:57:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 238b8667-b146-3416-9f87-f8e8b13710b0 | -14.90382 | -45.12921 | 2024-10-04 04:57:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78125875-96a5-3abf-abd4-93d9b4bc8ea4 | -14.16627 | -44.651 | 2024-10-04 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e87ed8-b99b-38d4-ae6a-821c56d9730f | -14.16577 | -44.65562 | 2024-10-04 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7891c0af-f98e-350f-8329-8e1e4448c8b2 | -14.16458 | -44.65359 | 2024-10-04 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8941212e-3cbe-3184-ab70-119aea1617fa | -14.1602 | -44.65046 | 2024-10-04 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c07b6cb7-6624-3fd4-af43-5f4b276adf45 | -14.15851 | -44.65302 | 2024-10-04 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fb688fe-860b-3d6a-8d69-2e5609218082 | -13.99158 | -44.03114 | 2024-10-04 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb755b9b-c86d-3057-b6bf-7ceb7449abf7 | -13.99102 | -44.03623 | 2024-10-04 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 11f7852a-9f84-3e54-b9f0-b0311c9063de | -11.83165 | -46.27034 | 2024-10-04 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6d93a509-b0e2-36da-b8d4-3bc4f4309443 | -13.15254 | -46.31789 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7aadf9c-373f-3100-a695-f90efcd1f0c8 | -13.15217 | -46.32099 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66122bff-9899-3fd9-a7f5-d0258cf59abe | -13.12894 | -46.30846 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f394657-3c31-3535-a407-1f4b8c657da2 | -13.12856 | -46.31151 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2507a1dd-c804-3ac4-9cb2-c9ea57ed5a62 | -13.15182 | -46.324 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9938bce9-8226-399a-91d7-9c27ea0b3b7a | -13.15145 | -46.32703 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b843e580-4fb0-3166-a852-a4fa02d7b29e | -13.14766 | -46.31311 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6b8237a-89d1-3ca7-ac4b-bd3ba971142f | -13.14375 | -46.30016 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ccf6215-9480-377a-953e-d61689787afa | -13.14339 | -46.30318 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57f36670-3011-324c-b26f-9a30fe2cb938 | -13.14304 | -46.30616 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aace4ee6-0c88-34ff-ae26-d3dac15d900e | -13.14269 | -46.30909 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e5a6358-606c-3a0d-bfee-bb233d6a2357 | -13.14091 | -46.29984 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22526ddd-d38a-3de6-91bc-73be3204dc1a | -13.14054 | -46.30283 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eab4d426-e345-30e8-9af2-af0a29c450cb | -13.14017 | -46.30577 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 176afd94-a1bf-324f-8d47-07d1d0a5d1f4 | -13.13838 | -46.2995 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48d85570-0b47-3868-8348-9338299b0daf | -13.13803 | -46.30248 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3aa89821-4cb0-32ac-b3b5-2bf893ddb903 | -13.13767 | -46.30548 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4b04ba83-4e82-32a5-8f2a-5f9f4b1fa2ef | -13.13514 | -46.3024 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38288dc4-0a17-3cc3-9d3d-c4622be6a8d1 | -13.13477 | -46.30543 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbf0be2d-36aa-3828-aa91-a953f3130df3 | -13.1326 | -46.3023 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6be4d64-a1f2-38bb-9c07-85ad0169a96b | -13.13224 | -46.30538 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 088844a0-bec4-3555-b542-57c2d288b26b | -13.13189 | -46.30839 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8dd56473-1e4a-3924-85c7-90ed16a08e75 | -13.12932 | -46.30544 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8759294d-5e4b-388f-82ee-e41e70e0112d | -13.12606 | -46.31164 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77d8d3d7-c8b4-3229-a834-970c3dcdb7b9 | -13.12267 | -46.3151 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea6706e-4ec0-3a53-ab59-2aeb92b6c33b | -12.89499 | -45.66059 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cde9f570-2f03-345c-90a8-ef2fb4731b18 | -12.26915 | -45.9659 | 2024-10-04 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14164483-087d-372a-be45-bf15fdc70ee6 | -12.26872 | -45.96939 | 2024-10-04 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06e22607-6423-35a0-a26e-fdc484e565bc | -12.26374 | -45.96508 | 2024-10-04 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e29c11a0-7bac-309a-a691-26ec92b2f841 | -13.15718 | -46.32465 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7141ce61-9cb4-3359-922c-2b3c271860e2 | -13.14729 | -46.31625 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dab80d0d-57ac-3de4-8b4b-c4a1848087f3 | -13.14234 | -46.31206 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6c9b7a9-f5c3-3926-bcc7-2833c59595e7 | -13.13732 | -46.30843 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09892958-6f20-353d-890c-d57a62d7781e | -13.13439 | -46.30841 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| da2b4423-9f2b-3751-a1a8-d379b4f2f966 | -13.12643 | -46.30848 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56cef064-24bd-30a1-9836-a86b1fa74a06 | -13.12569 | -46.31484 | 2024-10-04 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7ec1c03-3061-35e3-8099-6893f089ac6e | -14.20497 | -46.46973 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73434f79-8656-39ff-b34c-d1e8d769a2b5 | -14.19993 | -46.46606 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca81c1aa-ae69-3870-aa36-d598223caeaa | -14.19955 | -46.46934 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc7b504-3a97-300c-a84a-57f84701a35e | -14.19917 | -46.4727 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e937c86-e98a-37a1-b266-b1370a88a240 | -14.19877 | -46.47614 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75538fa5-aea0-3cc3-9849-e3432b749c5b | -17.61597 | -46.98127 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b01e2245-649c-3335-a902-c2e704d6a01a | -17.61054 | -46.98061 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f8f65c6-ef5d-3e05-ab2d-6055c53ab9a5 | -17.61019 | -46.9838 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0bbbfbe0-d693-3049-b549-b498effeffb7 | -17.6055 | -46.97633 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f28a4c8f-fe95-3e1a-b808-a5db48ae41cb | -17.60513 | -46.97977 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69ae991e-c4c0-31d6-840d-7a3f5e1c6d5f | -17.60478 | -46.98292 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b40c2f14-d3e8-3609-94cf-5ba7ce4ec81c | -17.60013 | -46.97506 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README151.md)
