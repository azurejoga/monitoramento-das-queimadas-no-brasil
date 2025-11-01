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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 425f9e87-c9c0-3cdb-b57c-b1f1ccaf4449 | -3.22029 | -50.58182 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3fb52c60-8a0c-335a-a7bd-e7fc4ceaaaa4 | -1.21262 | -54.07188 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 999b7484-fce1-3b8f-8264-bdfa887dc11c | -1.54069 | -55.40083 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01592aab-58bf-342b-bc16-65dcd47898f8 | -1.4964 | -47.80716 | 2025-11-01 05:06:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5266ac84-3d26-342e-a7b0-ef60a39a665c | -2.95524 | -51.51974 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d60daf-b8e8-39ee-83af-45bbb9f98426 | -3.06963 | -51.24719 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23b06d6a-3162-336d-b230-6f1f1b940cdc | -1.50243 | -53.121 | 2025-11-01 05:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed0187fb-0087-3890-9ca6-1c0866805ad2 | -1.25965 | -54.09349 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc128931-55e0-3d7c-8414-2074aa453ddf | -2.89708 | -48.05952 | 2025-11-01 05:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e767951a-7997-39c6-aeb3-61241446a1bf | -3.06516 | -51.25116 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8257b290-21eb-3d28-8a02-49dbb5d75f14 | -1.80534 | -55.16155 | 2025-11-01 05:06:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae2bd563-d4cc-3b64-ab4f-05de5fc3fab7 | -1.13153 | -54.21878 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79619840-5ab7-3fec-ac55-935f235f70fc | -2.05036 | -52.0735 | 2025-11-01 05:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e647dce-7f06-3faf-9798-dc956bd502ee | -0.42966 | -51.75983 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4f67b04-1f51-398c-b7e6-d8f9c627f525 | -3.23333 | -50.6543 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edb5a729-8c3e-3f24-8bac-66a46665c10d | -0.4326 | -51.76437 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42e0017b-78e9-3fb7-abcb-dd4201b9925c | -3.15521 | -50.82351 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c8e9c9-22a9-3c29-a403-d8fee7ac85d4 | -2.92707 | -51.46748 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d62c72f-936a-3f88-b5d3-0ffc82e74be9 | -1.75728 | -55.22842 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c90b733-581e-377c-885c-1bba3d3d7ff2 | 0.0762 | -51.12841 | 2025-11-01 05:06:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c04f2f47-cec7-37c7-83aa-58bc525a8f63 | -3.0388 | -45.81864 | 2025-11-01 05:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 334e58f5-e23c-3327-ba61-3bfed389ed7a | -0.42771 | -51.75677 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb775dc-1494-3ed7-ae84-09ae567d428e | 1.67317 | -50.87792 | 2025-11-01 05:06:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2d4c51-9eab-3965-808f-65641b4c6afe | -3.41128 | -50.00186 | 2025-11-01 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d69fb9ec-f760-3d89-9ccd-aa25d2e972de | -2.92775 | -51.46311 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4b113db-a89d-336a-b9fd-4232bbf97876 | -3.10994 | -45.23461 | 2025-11-01 05:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63883215-8648-3784-b1ab-0fe933ff4127 | -2.04618 | -52.07695 | 2025-11-01 05:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6362260b-afd3-33cb-9df8-aadcbb757117 | -1.78251 | -55.53511 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f76e30c5-c03e-378d-ae0e-2640f3ee6e2b | -2.93146 | -51.46368 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fa5c8e2-fcca-37cb-8729-a6734d2be57d | -2.95656 | -51.52111 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 485dedb2-5d33-3c3e-aec3-4afcc9fa371d | -3.01655 | -51.36724 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12cb756-09eb-39f0-b781-c327dcd07578 | -2.79593 | -43.3492 | 2025-11-01 05:06:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 362f7d47-31da-35a0-a4cf-f6ce0a944ca8 | -3.15832 | -50.82889 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d21bde37-7ce0-3314-a3e1-503884ed80ca | -3.0145 | -51.38055 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f889d000-17b4-303e-9d61-877a61687e5f | -1.37372 | -55.44606 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef4ff4ad-2e3a-3330-9f4d-fcc019dc5b74 | -3.52994 | -47.55106 | 2025-11-01 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68c4191a-7bd6-3b8a-8c0e-0ae0795cc6a3 | -3.06892 | -51.25174 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f60b07bd-c9b4-3732-82cb-ce1b287aa9b8 | -3.03499 | -50.34222 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d2d7ccc-fea6-316d-8cc9-88943e9fb37f | 1.75958 | -55.66655 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98b8b09e-7e8c-3b3f-b451-29a648153ff8 | -0.43028 | -51.75586 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07ced4f9-1589-3378-9752-eb54fe5eb151 | -2.79535 | -50.28657 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1abea266-5ee1-39f5-8d72-903d55fc7bb2 | -1.93917 | -54.18493 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220c4ca6-7c29-30a2-bd62-f62a4c7de37e | -1.19951 | -53.38379 | 2025-11-01 05:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e71dd8-c0d8-319f-9420-c837fb82c5b8 | -3.15907 | -50.82411 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e544c6-c9ac-37c4-92e1-bb3ae07e01f5 | -1.92777 | -54.06196 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2e46e8b-7b78-36bc-8504-053edd749964 | -1.85474 | -54.54754 | 2025-11-01 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80ae1906-3233-3445-8b75-ecdf8ba0c805 | -2.79667 | -43.34415 | 2025-11-01 05:06:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f62ea30-9863-35ea-a3c3-6bbae61f48e7 | 0.59787 | -51.57745 | 2025-11-01 05:06:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf402fcf-65a0-35a7-958b-594d29af3c90 | -2.46509 | -54.75323 | 2025-11-01 05:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2762124f-413c-3301-a912-8da473633053 | -3.07574 | -51.25739 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3799dc6a-9b62-3eee-ad99-f36ba5ebf6b3 | 1.10473 | -52.33821 | 2025-11-01 05:06:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0de129f-d7ae-3b9e-9b4b-02e71aac3712 | -3.07409 | -51.24329 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fe479be-554b-3b5d-a071-fd7b6f64d173 | -1.25633 | -54.09295 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d7f474f-6dd7-35a2-b956-d42f5172dee1 | -1.85419 | -54.55099 | 2025-11-01 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44d0b008-599f-3f87-a1c4-9e81fd77f204 | 2.4425 | -51.40321 | 2025-11-01 05:06:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f269eb6-e18a-30fa-82c1-511b640de28b | -3.03653 | -50.34398 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d89fafc-e7e0-323c-bf03-1244dc9a7832 | -3.22889 | -50.57808 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 40d59e9e-75ce-303a-8511-f4596f6758d8 | -2.52724 | -45.8479 | 2025-11-01 05:06:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d46e29f7-0580-3e4c-98ea-dec4aabc383b | -3.21955 | -50.58675 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8444a5e-f753-3b32-96ef-46bafba91895 | -1.96224 | -54.06023 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de468b72-b770-3b52-b88a-b81fb998fba7 | -3.01009 | -51.38443 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8fafa62-ff03-3f0c-85fa-47e84baa1627 | 1.69026 | -50.89223 | 2025-11-01 05:06:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b1c7fa3-8486-324d-a1bd-07e82c4b5c12 | -3.23281 | -50.57868 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 45fce591-59aa-3362-97fe-0de2800dfddd | -4.6639 | -41.96749 | 2025-11-01 05:08:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| efaf1d03-7799-3a70-90d5-afde168cf440 | -6.87944 | -42.84329 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15637cef-db9a-37aa-b1be-79bf84d5c6f8 | -5.1229 | -43.39193 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e68b440d-5045-349e-857a-a3470f4ef84f | -10.62369 | -52.18202 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59bd274a-b264-39ab-a1ea-70ef45af648b | -3.66759 | -51.71576 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d99d5170-c67a-34f5-bb15-605bf4adaa8e | -4.91936 | -45.59358 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccfec875-65e0-3edb-b309-90b1be83b86f | -10.63156 | -52.18316 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69ca2481-5c8e-3573-934f-5e135f6c240d | -4.64406 | -47.95506 | 2025-11-01 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cda533db-ddbf-3988-9a97-82018b2f7c1a | -3.85633 | -51.89122 | 2025-11-01 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 131f84d3-54ce-3b91-9c8b-25aafed0439c | -5.12239 | -43.38686 | 2025-11-01 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f5ec59f-a9d0-3f5d-be10-5cf51c9ecc16 | -9.02715 | -47.46101 | 2025-11-01 05:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59cad78d-a0c4-306a-a301-8fc1ca12583c | -4.91364 | -45.5932 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91db9d4b-76bd-3840-a67a-e5125221c480 | -4.17842 | -47.64779 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 828a06b4-9495-3103-a305-0cc7ab3e1b28 | -6.04831 | -47.97615 | 2025-11-01 05:08:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60b14550-dc8a-3107-90e5-5de0966c4cf2 | -9.91134 | -50.49773 | 2025-11-01 05:08:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af14b8f1-6b13-3d18-8910-7627fd549e4b | -4.94977 | -48.26539 | 2025-11-01 05:08:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbac1391-3dd4-3398-844b-80772d80bb47 | -4.83899 | -42.73083 | 2025-11-01 05:08:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79dd00d4-34cc-3a9a-aa72-e48d29406f57 | -5.45596 | -45.40686 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0bf51f5-e301-378f-8ce3-ac5cd732f4cd | -9.06686 | -48.83715 | 2025-11-01 05:08:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c25298-4ad8-3aa5-822e-2dfd18ef9d42 | -10.6237 | -52.18546 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40b53d19-1494-3595-ba47-f5308ec7cb8b | -3.53173 | -52.99828 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b70b4bb-10c5-3e44-94c6-4e80bef6869f | -3.60166 | -50.62602 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 961cee82-cae7-3249-87c3-d1bdcc6c2605 | -5.82802 | -44.0611 | 2025-11-01 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7b66f3-f00d-3833-8f03-1cc73f7b9200 | -4.82734 | -45.79242 | 2025-11-01 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e354104a-c2e4-329f-a945-13e8f0f72d44 | -8.85439 | -49.87865 | 2025-11-01 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 05298f69-4e08-35e3-a8db-c4679abdeaad | -6.99351 | -46.5282 | 2025-11-01 05:08:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de9a91b0-b678-36ed-bf1a-84838dc5d9b5 | -3.46841 | -50.94089 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968b55f3-9212-3f69-8efa-b5eed9c82370 | -6.6199 | -47.17393 | 2025-11-01 05:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb4d5d88-9099-3b1c-a20f-57cb0501f8a9 | -10.40878 | -44.35378 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aa0057b8-a52e-3d51-8a49-46b822a4ec8e | -3.58525 | -50.80937 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8726e06a-12cd-37cf-951c-cc910344d282 | -4.43377 | -45.91485 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c6c1c62-b346-3a96-97f9-f0facb3d372e | -4.55604 | -48.481 | 2025-11-01 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb69ae06-f3fd-3190-8b79-581ef51c932a | -4.17657 | -47.64843 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d565bd8a-7685-3e7c-9545-205084a5ea39 | -4.55889 | -46.69062 | 2025-11-01 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69556b0a-4f06-3460-96f8-6b1b1a77f5a4 | -10.40813 | -44.35921 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 02bf18f0-cf28-37cc-ac02-1c00d57596c1 | -8.15079 | -45.43708 | 2025-11-01 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 071e3d01-b18f-3143-9ee7-ccf349ceb045 | -4.18242 | -47.65418 | 2025-11-01 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README26.md)
