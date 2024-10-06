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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49ce611b-fe2e-3c38-a1d2-bad7dd3409d3 | -12.775 | -50.5149 | 2024-10-06 00:47:33 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f09e09db-2106-3152-a0f7-a999ab762795 | -12.7766 | -50.5219 | 2024-10-06 00:47:33 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a81a0cb-f9e5-3cc0-b907-8e260b35b761 | -12.7668 | -50.524101 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b99710c-ab66-308d-9cec-4a412e15f1ff | -12.7683 | -50.531101 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f135308-9fc3-3408-ae90-bda2770bd9a6 | -12.7554 | -50.519402 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cef1c72-442c-35d1-93c9-ba9aa6205e1f | -12.757 | -50.526402 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6149c45c-97e4-37f6-adc5-8271887c502d | -12.7585 | -50.533401 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35f7e4bb-7509-3e8d-b969-ab7e53fa86d3 | -12.7472 | -50.528599 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abfe581b-240c-35bc-ad65-56613d040bf9 | -12.7487 | -50.535599 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61c8c757-645b-3ad8-b6cb-86986184f903 | -12.7503 | -50.542599 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3463169-66c5-3ffe-b1ba-813eb1746dfe | -12.7519 | -50.549599 | 2024-10-06 00:47:34 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c702831d-8183-383e-aa89-c082bd674890 | -12.734 | -51.966801 | 2024-10-06 00:47:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 693d7fd3-9fd1-32d0-8138-560ceb5c4d15 | -12.7356 | -51.974098 | 2024-10-06 00:47:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b763b6fe-3feb-3bb8-bf9a-3580da82e8ff | -12.7258 | -51.976299 | 2024-10-06 00:47:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 007256b5-b434-3490-9eb1-2de7cca9aa75 | -11.7204 | -47.704899 | 2024-10-06 00:47:40 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b50422-cf90-3e18-af53-b1573b9e6b9c | -11.7068 | -47.690601 | 2024-10-06 00:47:40 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59a2a71c-cd8e-336d-a226-f205b5429d82 | -11.7088 | -47.698898 | 2024-10-06 00:47:40 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ced154a-6dce-3f5c-b3ad-f2de0f87dac5 | -11.7107 | -47.707199 | 2024-10-06 00:47:40 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88526945-ceda-3215-8775-8cbcd44aaa1b | -11.7222 | -47.800301 | 2024-10-06 00:47:40 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4578eff8-7fc6-3b5c-bbb7-1517734e76f2 | -11.7104 | -47.794399 | 2024-10-06 00:47:41 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94c2cf1c-1fa3-3ab9-9b98-c520ebb0b95c | -11.7124 | -47.802601 | 2024-10-06 00:47:41 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 282c0ac4-b890-3ac8-a88c-11c9099d48a0 | -12.1114 | -49.624401 | 2024-10-06 00:47:41 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6354df-8855-3d2e-a69d-1c0dced695f2 | -11.6462 | -47.652401 | 2024-10-06 00:47:41 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72f5855e-50fb-3b98-912e-95bcd459cc05 | -12.4143 | -51.023602 | 2024-10-06 00:47:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03fa241a-ad5b-3d0d-9f39-0bffccd87263 | -12.3777 | -50.951 | 2024-10-06 00:47:41 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3fdcf164-7bf2-3648-bd74-c3a86fad3482 | -11.305 | -46.776199 | 2024-10-06 00:47:43 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a99ace6-9b45-3fbd-a941-0350920de023 | -11.3072 | -46.7855 | 2024-10-06 00:47:43 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d30c44d-d072-3f58-b8f4-c79d7fcadcb3 | -11.2952 | -46.778599 | 2024-10-06 00:47:43 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb2b978-7de4-34ff-bca9-bdd5367b7112 | -10.7974 | -44.761902 | 2024-10-06 00:47:44 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af9fff9d-2ced-3333-bc9c-cf0307bd5eac | -10.7876 | -44.7644 | 2024-10-06 00:47:44 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a432668-ca75-347c-ba38-d71fe5d8ce30 | -10.7943 | -44.749401 | 2024-10-06 00:47:44 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 234498e4-8d25-3018-abf6-3b2fd9d6517b | -11.2832 | -46.771599 | 2024-10-06 00:47:44 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0628321-0580-3cdf-b203-a4155ff75591 | -11.6153 | -48.316399 | 2024-10-06 00:47:44 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aebed614-28d6-3251-acb2-414091613448 | -11.6171 | -48.3242 | 2024-10-06 00:47:44 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1705576-7061-365e-ba0f-2e895992acfe | -12.6294 | -53.104198 | 2024-10-06 00:47:45 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 008d71e3-0e75-3003-9032-2b66e81c8abe | -11.9475 | -50.131302 | 2024-10-06 00:47:45 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5d8af98-187b-37f0-97cb-992bdea58606 | -11.9283 | -50.0914 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f2afd74-331b-3d2b-88f9-4a53e04faf96 | -11.9299 | -50.0984 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83a95e1-010b-3c8f-9f15-b846162c1921 | -11.8907 | -50.107498 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cee27099-fe99-3c3d-92ab-ad21e817a7db | -11.8923 | -50.114498 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2d07920-d066-3387-a56b-db853db1e036 | -12.4328 | -52.473598 | 2024-10-06 00:47:46 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49cb3ed9-3dcc-3cc9-84f7-e6f1de1a92c2 | -12.4344 | -52.481098 | 2024-10-06 00:47:46 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c70c542-2c59-372d-9b32-7ad0008c6a9a | -11.8777 | -50.095699 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74383452-ce95-34a7-b08e-46193568e79a | -11.8793 | -50.102699 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1a6a527-24ef-3f4a-b96a-e87895019fee | -11.8809 | -50.109699 | 2024-10-06 00:47:46 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a12a0edd-0e2d-34ad-9587-2e551992a18d | -12.6161 | -53.476501 | 2024-10-06 00:47:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52d3a635-5289-38e0-a1fb-96cde5d711d7 | -11.8629 | -50.1213 | 2024-10-06 00:47:47 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc3e1516-56fc-327e-b083-dc49658df9bc | -12.529 | -53.258999 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa5c30a-8f1d-3e28-9419-77888c8b3f70 | -12.7049 | -54.093201 | 2024-10-06 00:47:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1c0c722-8f78-318d-872f-6bc917982708 | -12.4922 | -53.1343 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5600812-6c78-3d11-8cec-1841e8f315f5 | -12.5602 | -53.454498 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8302c5-0eb2-33f3-b3b3-de1975a96d0a | -12.562 | -53.462601 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6c07db9-5cc3-3972-870d-ffdff70e04a2 | -12.6951 | -54.095299 | 2024-10-06 00:47:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8e3efe1-1bae-3eab-8368-887dd46a41bc | -12.4808 | -53.128502 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d44cec43-c6a9-3080-af53-9ff2376492d6 | -12.5487 | -53.448502 | 2024-10-06 00:47:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60a29c49-a579-3803-b8f7-2d2050fd6ceb | -12.6671 | -54.0103 | 2024-10-06 00:47:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01022bb0-f02b-3db7-a7fd-b2891d9108d9 | -12.6689 | -54.019001 | 2024-10-06 00:47:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0561d0b-5b7b-38e2-a0f8-6fef614861a2 | -12.4777 | -53.162201 | 2024-10-06 00:47:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cec6ef4-2221-3ce4-9f17-a029ffb2ee60 | -12.6573 | -54.012402 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33090651-0379-331f-be09-04a3a0defc9a | -12.6591 | -54.021099 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f37cdd8c-8c2f-3a1c-a494-6fdc1345690f | -12.6609 | -54.0298 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25001c81-c403-3b57-8251-92079d8a8084 | -12.6475 | -54.0145 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2fe390-03e3-3c16-b6cc-fa15e4d28953 | -12.6493 | -54.023201 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42b363aa-0aed-3bf6-bb15-1ac6e95c3cd4 | -12.6511 | -54.031898 | 2024-10-06 00:47:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6d717d-ccaa-3773-9dee-a33bdd0661d7 | -12.502 | -53.518299 | 2024-10-06 00:47:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05ed28cc-3d9d-3092-ad3f-c7ac80ed9d0d | -10.4735 | -45.168301 | 2024-10-06 00:47:50 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac1007d-0e11-3ed6-9c94-d0bb7c4ee587 | -12.6632 | -54.679501 | 2024-10-06 00:47:50 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8733257a-ca2d-3e2e-b51e-0833467b7cd5 | -12.6652 | -54.6889 | 2024-10-06 00:47:50 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4c68b03-1a3e-364f-aa36-598a81b73a22 | -12.6535 | -54.681499 | 2024-10-06 00:47:50 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aed43f5d-1ff1-384b-895f-071c2451af5d | -12.6554 | -54.690899 | 2024-10-06 00:47:50 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab94c0de-79b7-3a71-9e9c-32ed89768a51 | -10.4638 | -45.170799 | 2024-10-06 00:47:51 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48afa79d-0ddb-387f-b944-a638a831d4c0 | -13.7444 | -60.596001 | 2024-10-06 00:47:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 141bb7e3-92f8-3525-bb3d-46692f2485a3 | -11.978 | -51.8937 | 2024-10-06 00:47:51 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14ea88ff-76ca-30d7-8f65-6fedf15b7198 | -11.9796 | -51.900902 | 2024-10-06 00:47:51 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1b74a26-27c3-35ec-9491-37d403ab4958 | -12.154 | -54.248001 | 2024-10-06 00:47:57 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcb5d54a-7933-3470-892e-22031f60e3dc | -12.1558 | -54.256802 | 2024-10-06 00:47:57 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b43ec094-81cc-36f7-a554-a18e90f61c92 | -11.7201 | -52.930698 | 2024-10-06 00:47:59 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5521f05-6737-3c6d-8115-e0e771abc7e9 | -11.7218 | -52.938301 | 2024-10-06 00:47:59 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9eb5c22-0c3d-3499-b677-cb3045323ff8 | -10.6827 | -48.701 | 2024-10-06 00:48:01 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 436ec0d5-9ee3-3c97-ab60-42f12c07b55d | -10.6845 | -48.708698 | 2024-10-06 00:48:01 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25db0e36-fb36-39ba-a0e7-a124cfc338c8 | -10.6863 | -48.7164 | 2024-10-06 00:48:01 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4147ab4b-78b2-3314-a2cf-63668b3f1d40 | -11.2337 | -51.130402 | 2024-10-06 00:48:01 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15a13523-c033-3d61-a14a-9a3b79b8dfea | -10.6747 | -48.710999 | 2024-10-06 00:48:01 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d86b177-9ad8-3d4d-ae8b-7a55a59dcff0 | -11.2347 | -51.181301 | 2024-10-06 00:48:01 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae4da61b-0156-3ea0-9c14-eb5a18fc1295 | -11.2404 | -51.253101 | 2024-10-06 00:48:01 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24decbfb-3b0e-3910-9b60-a93b79e8c494 | -10.8536 | -50.124699 | 2024-10-06 00:48:03 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 200d0fc2-9138-3713-b31e-246140358fd7 | -11.5292 | -53.427101 | 2024-10-06 00:48:04 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 277d5bc9-c061-3411-a7a2-83d6e59f4c42 | -11.5309 | -53.435001 | 2024-10-06 00:48:04 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aed77152-2813-31fb-8c0e-25cdd1e5b8bb | -11.6935 | -54.5411 | 2024-10-06 00:48:05 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9344e965-cbf4-37c7-b8ce-3908a2961674 | -11.6566 | -54.5117 | 2024-10-06 00:48:06 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cda55bdb-2433-3bae-8ff9-7208e53e6fc6 | -11.645 | -54.504799 | 2024-10-06 00:48:06 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb20dcb4-7826-3d78-9d07-26704710b7e6 | -11.6468 | -54.513699 | 2024-10-06 00:48:06 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab4da6f5-92cd-3b7b-813d-6cb313e21a3e | -11.6487 | -54.522598 | 2024-10-06 00:48:06 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9a97989-8271-3938-a892-1bba828b1926 | -11.2634 | -53.2883 | 2024-10-06 00:48:08 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5f5d91b-820e-3df7-8ea1-e55cf4156fc4 | -11.0536 | -52.508499 | 2024-10-06 00:48:08 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b46d66dc-5b11-3673-ab4c-029cf42b03ae | -9.9185 | -47.680599 | 2024-10-06 00:48:09 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb65516b-fd26-3f43-b018-6b10d4f4fbbc | -9.9205 | -47.689301 | 2024-10-06 00:48:09 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38bc18a4-6184-344e-85ba-5954b099d50e | -9.9225 | -47.697899 | 2024-10-06 00:48:09 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61101ea8-1da9-36d7-bf7f-484a65fa66fd | -11.385 | -54.340099 | 2024-10-06 00:48:09 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82b3f190-2e4f-3334-9cb6-1f27ba9b35b6 | -11.3869 | -54.348801 | 2024-10-06 00:48:09 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
