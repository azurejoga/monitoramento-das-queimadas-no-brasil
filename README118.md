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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94136b8-dc7e-3b35-8b62-ed840bf0d802 | -11.75374 | -63.8278 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7228b420-7f43-3f05-b4a7-f1ac10d0ff48 | -11.75309 | -63.83166 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f24d049-6e78-3b46-8ce2-4bb0ee887f38 | -11.75091 | -63.82333 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f043760a-b107-37b9-b56a-091c950c1282 | -11.75027 | -63.82718 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86f74d98-e34d-34a8-81ae-b57361a19525 | -11.74963 | -63.83102 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68e06a7c-f528-331c-9881-7ffb94bdc823 | -11.749 | -63.83485 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87599a1b-9b26-3104-87fb-5eeccf47fb13 | -11.74745 | -63.82272 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efb93ff3-1bf1-379d-bc47-9480232a62d2 | -11.74681 | -63.82657 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d22d3df9-3944-3626-a53b-e261d442d6fc | -11.74554 | -63.8342 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56f3c703-f117-35dc-ac16-5271d4aa9583 | -11.73991 | -63.82524 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39d36ce0-ed55-30e2-99e3-7b34a633c388 | -11.73926 | -63.82907 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 989ec847-cc5e-319c-84e7-a0f46276fe1f | -11.73861 | -63.83295 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3083b45d-885c-3721-83c0-469caf39bce9 | -11.73773 | -63.8169 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 494133d2-5929-3a5a-b69b-489c53e49cef | -11.73699 | -63.81388 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b41d4e11-0a65-3507-a3ef-87b6cb89973e | -11.73491 | -63.81248 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c48b58-9506-3da1-a0b1-b03fe54e4f36 | -11.7316 | -63.7815 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ceda73e-7316-3d3b-ba08-b3a055c13c3a | -12.50326 | -63.94772 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee29aad-61dd-326e-ab77-3bbab8ebdd95 | -12.50172 | -63.93556 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d87d5d-3910-30a8-ba11-c78d6d53bca1 | -3.82917 | -51.40321 | 2024-10-12 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f2f5f92-759e-3ea1-a604-92465e34ac59 | -12.4998 | -63.94712 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de29350-fba4-3a8e-9fe3-3668bcc7ad11 | -12.49634 | -63.94653 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9ea30f1-27d2-3013-9784-9edc600f3381 | -12.4957 | -63.95038 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9135cf6f-37e2-31b8-bd4e-c5b32906ed67 | -12.4916 | -63.95364 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bfeec50-9c30-3bf0-aa16-2fef9607824d | -12.48749 | -63.95689 | 2024-10-12 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 141e4c5d-6e42-3d3d-b7c4-52be525b2f87 | -7.49077 | -64.28006 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b50d194-a25c-33b2-82ed-af3a6fea8360 | -7.30958 | -64.6717 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16e26cd9-a9bb-36c1-aabf-26159ee5eae6 | -7.3088 | -64.67637 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bdb1358b-e4bd-3b50-bc62-803574d06394 | -7.29895 | -64.66512 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6a1162ab-1c21-3629-8225-f249b1a42ec0 | -7.29514 | -64.66448 | 2024-10-12 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 11ac1e1e-dd4a-3eeb-8a66-7c685d146ef2 | -8.16391 | -64.11423 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c962c44-9cd1-361f-8d6a-53146b2cda7e | -8.93444 | -64.24154 | 2024-10-12 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 345406fc-94c9-30c9-8f4f-0e8d8c4e3a21 | -9.1962 | -66.09299 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f677a6-88c4-3ad5-8555-8ab7444e92be | -8.70684 | -66.99969 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 575ef633-8114-3531-af3c-ab0c7f303b57 | -8.70422 | -66.99783 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 114d22c0-06ed-3402-9d00-04c44eeafd77 | -8.70349 | -67.00195 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e8dd82-fbf6-38ae-8fb2-7c7a3465dcb4 | -8.70252 | -66.99891 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a845973-93ec-3e35-a7ef-dcaaff9a4e16 | -8.70183 | -67.00303 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af43855-26b0-3d1f-ab95-dc623dc6993e | -8.69917 | -67.00119 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0c899e-23ed-3605-b672-84637ac65292 | -8.69844 | -67.00532 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf52815-3cd8-3452-a7a2-c582be548bdb | -8.6975 | -67.00227 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3a624e-c197-305e-afbd-c41a88713fdf | -9.8715 | -67.29846 | 2024-10-12 05:25:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8e27b65-6d36-3146-b51f-1e6e9c0c4633 | -9.86443 | -67.26308 | 2024-10-12 05:25:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9cac72-38d8-3ba4-aa4c-a6e8cf1c07e6 | -9.61337 | -67.1506 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5de3673b-6288-31b6-8657-8a672355285e | -9.61266 | -67.15466 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 953d2432-92dd-3b22-a1ef-b774264a675b | -9.448 | -67.14667 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4e5ef32-19cf-30f8-8e7c-fe1556ba7940 | -10.09166 | -67.13908 | 2024-10-12 05:25:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cf88ce-bb23-3bc7-a11e-d2e2b78b3db6 | -10.09097 | -67.14311 | 2024-10-12 05:25:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c7411f-1a35-3a58-be5d-5a7fa2c6b841 | -10.09002 | -67.13835 | 2024-10-12 05:25:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c319df-9529-3e4e-af6d-88c653315ccb | -10.0893 | -67.14237 | 2024-10-12 05:25:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53abb20b-70eb-3e15-92e7-216dcbac8aa3 | -10.0874 | -67.13831 | 2024-10-12 05:25:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be7c80c-5880-33ad-9374-de12f247f36e | -18.14004 | -56.45583 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 85c0a968-29a7-336a-9cc2-9d8097dc4467 | -18.13614 | -56.45067 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc3e6840-590c-3b39-937d-52cc3ee09ea7 | -11.25693 | -51.42904 | 2024-10-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a40643f-c1e9-3446-af88-b86c3899c06c | -11.25433 | -51.42984 | 2024-10-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eef689e-f64e-351f-a5c8-95f623e68951 | -12.99938 | -53.62582 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47f3154c-11ca-3ccf-ae3f-3a1e58efd2b5 | -12.99862 | -53.63173 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9166d57-14ce-3df7-8072-7f2140427e93 | -12.97107 | -53.52629 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ed6f046-62d1-3714-b505-fc1f6d119981 | -12.97034 | -53.53213 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc19fe07-96d2-3cdf-bbad-f80f1a64f771 | -12.96961 | -53.53796 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38f2fc5b-8d58-3e95-909c-a651a4861ff7 | -12.96601 | -53.52565 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2b0a2da-73dc-3434-b621-f8d6c5c51106 | -12.96528 | -53.5315 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db7030a2-3608-3f04-ae90-f6db95c26e6a | -12.96455 | -53.53732 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6453b5dd-d1bc-335c-a69d-9e945054c18e | -12.96383 | -53.54313 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eabe6353-1de4-37a9-8e57-9d2b93b675bc | -12.96096 | -53.52501 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f9e8bbdb-7c88-3fb3-bcde-85ff39b86154 | -12.96023 | -53.53086 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 319cbb38-9acf-3947-83e7-be3288a6a346 | -12.9595 | -53.53668 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9d02fe1-a2b9-3baa-a1d5-fb8263115396 | -12.95878 | -53.54247 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9916563-213a-39fb-abe5-e4f8515c265d | -12.95591 | -53.52434 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8be86b61-315e-30b6-bd92-c787da8a2e6a | -12.95518 | -53.53019 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd876d02-493d-32fc-86cc-935231117352 | -12.95445 | -53.53602 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ce2f15bc-78c1-3669-bd8b-aea055b6a580 | -12.95373 | -53.54181 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5911a3d3-7bfa-3093-8216-eed9dc22abc4 | -12.95086 | -53.52364 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0d5f25c1-25a3-33ce-99b9-ba8c5944e0b0 | -12.95014 | -53.52948 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6ad99646-8378-3fa2-ac7f-2b510ec5691a | -12.94941 | -53.53531 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bb656089-045e-3abc-a4d5-c6e9dc051b8e | -12.94869 | -53.54111 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01e76074-9732-350f-a2ae-4ecb19e43847 | -12.94581 | -53.52295 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fcd200a6-5c15-3366-944f-389db6a29cbc | -12.8646 | -53.52342 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44933be1-6760-37c1-ad62-d7d28a93de6f | -12.85955 | -53.5228 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bf9cb0c-d0d3-3313-b1ce-f637bc0cae31 | -12.85882 | -53.52862 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22640eb1-4e87-3a97-971a-9b1c8e1ee4a6 | -12.85449 | -53.5222 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65da3673-87dc-3b37-a0f9-6776302187d3 | -12.85377 | -53.528 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92ab0cd6-a6a7-3a2a-aa51-80e343007b40 | -12.84873 | -53.52733 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee664878-a830-36ba-b49c-bba0367e3240 | -12.84369 | -53.52664 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3abd3388-5bd3-35cd-a9ed-c4f9f313a488 | -12.83865 | -53.52594 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a1cc6121-38ef-38ff-bc37-fb9679355fac | -12.83361 | -53.52525 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e00ca797-5792-3de6-ba0f-412a34f3af07 | -12.83289 | -53.53105 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b8c5857-0b64-383d-8055-1d694ed5161d | -12.82857 | -53.52456 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dc583dc-fbf9-31ef-94c6-ff7aa6135217 | -12.82353 | -53.52385 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4df3e08-ac11-300e-825d-e3d02233ed4d | -12.81995 | -53.52309 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa7134c0-9840-3428-83ed-e3fa3b4200ab | -12.81849 | -53.52314 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22c142af-032b-38c8-9fa4-2f128c663847 | -12.81492 | -53.52237 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65f30ed1-ac74-3c0f-b943-969fc9331fca | -13.01763 | -53.46562 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b943ad3-16fc-3b25-abbf-947aa2dbbb1c | -13.01726 | -53.46871 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e5f5eff-1333-312a-b77f-4f2557c3c59e | -13.01689 | -53.47177 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c69514db-3d48-346e-9712-5f8eca3b886b | -13.01466 | -53.46664 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93fa7711-7b8f-3ada-8be4-db55f38bf14c | -13.01427 | -53.46971 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1841ae31-1281-39e6-9da4-9be1750b62c0 | -13.01388 | -53.47277 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7cfa8c9c-9e52-3214-be5d-02e3fb1982d5 | -12.98979 | -53.50016 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e9a424e-c7e9-3110-8abc-033714a4ab0c | -12.9894 | -53.50317 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8da04081-0327-3984-9659-b4130b19359c | -12.98903 | -53.50617 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README119.md)
