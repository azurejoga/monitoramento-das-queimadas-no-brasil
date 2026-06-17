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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b41f66b5-a123-3287-9368-f97e28c2dbf2 | -9.33189 | -45.48071 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ce23242b-3cab-3461-8cad-0d9c8e919b06 | -8.94923 | -46.99634 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84798925-2ead-3859-a770-2e017ed8e8c9 | -8.94878 | -46.99982 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5161e30f-026a-353b-9b4b-cce7e0f607e3 | -9.26217 | -48.54122 | 2026-06-17 05:04:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f86652e-7cf7-3c71-86e7-2b1f679cfd14 | -8.27614 | -48.21391 | 2026-06-17 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4cb1be3-c2b2-3cb7-8836-159e41cb6feb | -8.97282 | -46.98268 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a23cc1a1-146e-3314-ab05-b14fa332353c | -2.73643 | -58.18982 | 2026-06-17 05:04:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05816962-5b24-3640-96b9-543d50b27a6e | -9.33893 | -45.47264 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3b8b1e3-bf1c-3687-bbb9-0736309a1c12 | -6.97867 | -42.88257 | 2026-06-17 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1aafcbfc-7e94-32f2-9f88-f105dbd541b1 | -5.79842 | -45.06785 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 457e0d1a-3023-38e5-bc27-7b0fc4f10589 | -5.80199 | -45.08486 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4443f5f-6649-35a2-b315-d9fead514f59 | -9.33838 | -45.47709 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7e68ff64-0be4-34c5-9081-fd8e80ccb121 | -9.32318 | -45.47387 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c78fc810-813d-33c1-869c-1a79c4a67a06 | -8.98799 | -46.99164 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cbe5d869-53c9-31b7-ae79-82c7bd28e3f5 | -9.32649 | -45.47548 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8b16ab9e-184e-386b-8727-485028edfb81 | -8.93922 | -48.00328 | 2026-06-17 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f7f31fa-b77e-3135-b315-7113c6f5af87 | -6.63643 | -44.57769 | 2026-06-17 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a0689c9-653a-315a-a101-262c643360a7 | -6.97598 | -42.88378 | 2026-06-17 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b8717284-4b89-3507-b5be-052331abb500 | -7.72323 | -44.1614 | 2026-06-17 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a9f3af3-8969-318c-8732-410e98b08f9a | -8.68379 | -47.84994 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3785745d-055c-3024-903e-efc6c6bdc8b0 | -8.6842 | -47.84702 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b28961cc-3c15-3cd7-b6fb-209a50cca26e | -8.9764 | -46.99684 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b96e761-7230-3064-9b95-8ae2580d5abe | -9.21195 | -47.90895 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9d1417c-aaae-3042-ab84-b5b522b53ca1 | -8.97106 | -46.99607 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2895f57-5bad-3d62-b774-2047d357935a | -9.32055 | -45.4747 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1e5bd49-0601-379f-842b-b669a7dbbcf3 | -7.76117 | -47.56226 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39a889d8-3400-3d93-9755-27b2d16a04e9 | -7.8402 | -48.39657 | 2026-06-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e21c5df5-3a65-3460-b4c2-573179c73599 | -5.79616 | -45.08424 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6f10ed69-0e5d-348f-bc6c-bc33ba9f5a66 | -8.98442 | -46.97744 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6131ee-1ec5-34ba-bb6e-c0bb2792f4e8 | -5.79505 | -45.09227 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6383951d-69cb-3ecd-b406-e5414ca805b4 | -7.76077 | -47.56526 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a379b2e-ccd7-3d5e-9d3f-c5fc49db0cc7 | -8.99067 | -46.97153 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b6dc217-3c9e-3a8c-8844-ae13cf592944 | -9.26288 | -48.53578 | 2026-06-17 05:04:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8627411-5870-3240-9a82-c2fe94e542c0 | -7.83614 | -48.39075 | 2026-06-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 930fcf47-b144-35b9-80fb-c0c20ea505c7 | -6.63035 | -44.57688 | 2026-06-17 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13595df8-baa8-33d6-bfae-536aaa87bfd9 | -8.96967 | -46.96515 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b20910a-7d54-3643-a9ff-b06210cae854 | -6.64253 | -44.57832 | 2026-06-17 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 075c9bb4-fb2b-3628-85c2-2048925ed74f | -9.3146 | -45.47395 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90da2037-85eb-3ae9-8cd2-c0169e8e7f13 | -8.88916 | -46.97183 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d510c6-8541-3d25-9c8e-9fa03f9d8674 | -7.35449 | -49.86148 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d53044a0-32ed-3ffe-bb05-f2a24ab58b73 | -9.33728 | -45.48596 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6f2b37cb-00b1-33f5-bfdf-956888037080 | -5.79727 | -45.07615 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aeeef79e-20b2-31ea-8bee-434e6ee6b309 | -8.67898 | -47.84612 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3520e62a-2caf-3861-b3ed-cc0a2f23311b | -7.76582 | -47.56602 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acb60754-ef96-30ea-a16c-a1da7ec32ac6 | -9.29728 | -45.46733 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27ef8b64-2244-31f7-ba02-a62dc5c4207f | -9.30323 | -45.46806 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 010f50b4-5eb7-3105-8dd1-55e4f0769f61 | -8.9746 | -47.01048 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 673a27e5-d3e3-3e3e-bf1d-a86c44296cec | -7.36853 | -49.85518 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dad79b27-5c46-38a2-a2b6-9e11f874f04b | -5.79784 | -45.07204 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4699c22-3cff-3743-a8a9-3b21ca6ab096 | -7.63404 | -50.02235 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fec811bc-d774-313c-9c63-352c47dcf70c | -9.29399 | -45.46583 | 2026-06-17 05:04:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5cea435-29a9-3e9b-a5eb-07411c58863b | -8.45882 | -46.39883 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eb6b75c-f7ad-32d7-9e5f-85ea7dd8132c | -5.80143 | -45.0889 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0294683c-3fe5-33a4-a291-1d9a0028236a | -9.21158 | -47.91183 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d42e2af4-9848-347c-a162-877c9d10f71d | -8.47577 | -51.53281 | 2026-06-17 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a295236a-d5bb-3f18-9329-72626ddff1f7 | -8.9755 | -47.00369 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c96f0825-0f32-389d-9c95-353a81451cf3 | -8.24169 | -47.12596 | 2026-06-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdc47a10-3f20-3630-b212-d2120cc98b17 | -8.9715 | -46.99274 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b0ca1e0-9a53-3158-a05b-a80584450d41 | -5.80255 | -45.08081 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdea8dfc-f1e2-39b0-a48b-768dca6f6eae | -3.85866 | -54.07998 | 2026-06-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dac614f6-0e5f-3877-b72e-3ca97a46d3c6 | -7.35392 | -49.86554 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8466a828-85d3-3750-8d9c-de15c46aa53c | -7.37282 | -49.8558 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c21b921-3154-3705-80fe-b60d473f81c5 | -3.80588 | -48.96187 | 2026-06-17 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd41ec19-8ea9-3afc-b3bd-88af2528fab4 | -9.31128 | -45.47241 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bbe6192-3771-37ce-8c92-46f1579ff392 | -9.20653 | -47.9111 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9dfa9c3d-4317-30c7-bb6a-0c2aea5847a0 | -8.447 | -51.5387 | 2026-06-17 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dc84090-f89f-3d79-adcc-8a0e83019552 | -8.96835 | -46.97519 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bab0e464-7cb7-349f-87d3-2080e0868762 | -8.96923 | -46.96849 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36e43cd3-ff76-3c3b-b9ab-858c08bce1f7 | -2.4707 | -49.00927 | 2026-06-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99082c63-82fc-398f-a72c-14c17f651442 | -7.84094 | -48.39136 | 2026-06-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19ee970b-eba9-3c89-adbe-0987ebe7e1b7 | -5.97909 | -47.07068 | 2026-06-17 05:04:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e72d6e-1363-37b1-a2b4-a6ab4212f31a | -6.98273 | -42.88482 | 2026-06-17 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f046008a-2c31-326f-9f81-214ae3e6d524 | -9.34377 | -45.48235 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| df8b9d04-ea01-301f-ac18-e9f3534365c3 | -9.3226 | -45.47828 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e253ea62-c936-3224-abc3-d27bc1bac94e | -7.84074 | -48.39353 | 2026-06-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b85f5b69-db3d-34a3-aaee-92fee555ce33 | -8.97595 | -47.00027 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a43787-57e9-3187-ae29-dcca6b2927cf | -8.97371 | -46.97594 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af4e7e49-3a23-3f86-8228-eec8558993c0 | -9.21253 | -47.91042 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5209d7c5-fa6b-3d85-b6f2-c909c7aa0e2d | -8.97505 | -47.00709 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a7edd63-8bfc-32fc-8e7f-a2bc62b99c58 | -9.33783 | -45.48153 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9bcd4c80-83d3-3e60-b887-effaa2e1ec57 | -7.35821 | -49.8662 | 2026-06-17 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cbfbfb7-ba71-3e31-b15a-9502b776f957 | -8.98933 | -46.98161 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f06d006c-e3dc-3152-ab0e-7edb72a5ea3a | -9.30533 | -45.4717 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b11657b4-acd4-3119-b850-bc241e2fed74 | -3.50916 | -48.03456 | 2026-06-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc15360c-95ad-3548-b1ef-d2301878e734 | -9.33134 | -45.48513 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1fe1b73a-6ecb-3fa1-ac61-5df4d236bf0b | -8.97326 | -46.97931 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff6f9d3f-1dd5-32d6-b837-eff42beceb5c | -8.99022 | -46.9749 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3585aa5-932e-37f0-9071-ef74214ccc5e | -9.20749 | -47.90968 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5396e464-4c22-3fab-8051-b2ddf02c93e1 | -6.16511 | -48.51043 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f283a800-e0d7-3f1d-a156-60735dd48345 | -8.98755 | -46.995 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a4682274-6adf-3855-8743-dfd0f16e0c97 | -8.8887 | -46.97524 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355d75a8-9642-3b75-afdc-c9fbce32e849 | -7.71691 | -44.16052 | 2026-06-17 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b7049cd-56b9-3c7e-878c-246c15f03fec | -9.31723 | -45.47313 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40fdb66e-cc4a-39f7-a0a8-661a48b30356 | -5.13734 | -47.99087 | 2026-06-17 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 403d1eee-d77e-3c09-937c-e845d9c5e511 | -6.14125 | -48.51219 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a852ab68-67df-3668-878a-aa710a1c13aa | -9.33244 | -45.47627 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7166a4e3-7780-3c9f-ba77-028a558b8542 | -11.26469 | -53.95956 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce49c51-149d-3d66-8605-65b96dc6a989 | -13.60524 | -56.59818 | 2026-06-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6601b9f9-4a12-3b36-a16e-dbdf676233b0 | -12.20957 | -52.78309 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d16831f1-db92-342b-8b37-cecf7802b57d | -12.17238 | -52.77578 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README11.md)
