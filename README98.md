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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32c3b21f-57e1-3b90-bb9d-dba560a6ee18 | -8.5414 | -46.22144 | 2025-10-08 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| ed17d379-a3f1-3b76-93a2-c47599b00fbd | -7.53097 | -42.72375 | 2025-10-08 11:38:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 90f55e87-3f38-36c8-b629-676ce0b02b30 | -7.17286 | -39.32125 | 2025-10-08 11:38:00 | TERRA_M-M | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 99e156bb-9c55-32fc-9eaf-318a4d0418ab | -10.42143 | -45.39172 | 2025-10-08 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 148ac5f6-8f71-377a-9fdf-c5fcb3dc6891 | -8.22735 | -44.16689 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e9e15e50-f91a-3e3f-bb57-6a00e8dda38b | -6.3987 | -37.55378 | 2025-10-08 11:38:00 | TERRA_M-M | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 93b722ff-710e-3213-a580-66edde3b06ec | -7.40901 | -37.52166 | 2025-10-08 11:38:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ac6e6f01-8ffb-3908-adb9-af0037c37715 | -6.9989 | -42.8769 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 99d6fae9-60a3-33be-893f-efbdc9b094b6 | -11.83365 | -40.30922 | 2025-10-08 11:38:00 | TERRA_M-M | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 62f7b45e-0afa-3291-8011-e8cc955e8c35 | -8.30145 | -36.88041 | 2025-10-08 11:38:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 19.8 |
| b95c6c05-9d97-379f-8b68-8193e5d7fc2b | -10.92326 | -47.14693 | 2025-10-08 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 258.4 |
| e6a5b145-fdb2-3bb9-8a96-aeb3d67a22ac | -8.23563 | -44.19587 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 58075348-ede0-376b-b09a-00045b1c0d90 | -7.93798 | -37.94098 | 2025-10-08 11:38:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0c8b1692-c4bf-3349-9cb0-ab2896a9d1a7 | -10.43503 | -45.39381 | 2025-10-08 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 24b9b083-5b39-311b-bedd-934502f543c9 | -7.79486 | -44.23959 | 2025-10-08 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 252.8 |
| d8d0be56-04d1-3f3b-ba62-333c6b44580a | -12.2587 | -40.24946 | 2025-10-08 11:38:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 03533c9f-95ea-302a-a663-15dbb8cf336f | -7.48249 | -43.11981 | 2025-10-08 11:38:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 71029bf3-81f6-35ca-a336-96d2983fc19c | -7.78727 | -44.21156 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 14300b0d-ce27-3ccd-b6fd-553dbe2a58c2 | -8.55482 | -46.22966 | 2025-10-08 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5e7f8dba-a5d1-3a91-8b95-1b555908b7b8 | -7.0133 | -42.86218 | 2025-10-08 11:38:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 323.1 |
| 2bbeb622-9d5b-3284-babe-847f547a1e44 | -10.42144 | -46.59287 | 2025-10-08 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 197.6 |
| a91bc296-80bd-37d2-a99e-f901fb1bc8bb | -6.32771 | -37.71826 | 2025-10-08 11:38:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| efa3ecca-4fb2-3184-ba5f-6964e1463a69 | -7.447 | -39.95745 | 2025-10-08 11:38:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 58700aa6-bed5-31e2-a466-95e145eae607 | -7.78536 | -42.41433 | 2025-10-08 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 05480d61-e2f4-32e8-a70c-b4a1b0bc7889 | -7.83395 | -44.95817 | 2025-10-08 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 69b9252a-8063-31bc-a9ef-56850fd075fe | -8.23703 | -44.18916 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 330.1 |
| d5e7bbfd-2cbf-336b-b298-76d2af69e17c | -8.50158 | -46.27574 | 2025-10-08 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 164.8 |
| f48a8c36-8265-3f15-946b-4c1809c1dd77 | -10.91321 | -47.11355 | 2025-10-08 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1031a55d-6e39-39f9-8952-90bc1304e4a6 | -6.75787 | -36.45823 | 2025-10-08 11:38:00 | TERRA_M-M | PEDRA LAVRADA | PARAÍBA | Brasil | 2511103 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 42fc1447-5652-3ddb-aab4-cc56b6bd1a20 | -8.17386 | -43.33024 | 2025-10-08 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| e7cbe814-3146-369c-93d8-d6611ee90091 | -11.86379 | -40.53239 | 2025-10-08 11:38:00 | TERRA_M-M | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 082040a2-e684-3991-8371-b6c99caed58a | -8.18323 | -43.34925 | 2025-10-08 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| cf1a77ac-4204-3c84-8118-6927dfd8130f | -7.72917 | -42.40573 | 2025-10-08 11:38:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| b5eaea5d-84b2-387c-84f7-c2a606b39d61 | -6.96057 | -38.44361 | 2025-10-08 11:38:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9c74e843-c31f-3fa3-94d9-1a55db09db2e | -9.20626 | -40.65968 | 2025-10-08 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 55ecd66d-3f9d-3a6b-a710-ae9daf27a2dc | -8.35672 | -36.94925 | 2025-10-08 11:38:00 | TERRA_M-M | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 19831760-615d-356f-a8f9-13d955a35d80 | -7.89362 | -45.50687 | 2025-10-08 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4476e0d1-7c5c-37a0-937d-f6e0782ebd9e | -7.79799 | -42.40783 | 2025-10-08 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e8d85048-26cf-3ddc-84db-97c02379a943 | -7.01073 | -42.87868 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1063.5 |
| 75d4eed5-7aa8-377c-85c7-ef8dccb9f120 | -7.80147 | -44.1986 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ecef30dd-8662-3bca-899c-81f5bce73f7b | -7.00148 | -42.86041 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| ef92d454-593d-3579-99be-540dad184bda | -8.6615 | -39.6197 | 2025-10-08 11:38:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 25ac6416-8d06-3086-af11-064622d4dd60 | -8.53979 | -46.2273 | 2025-10-08 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4121114d-28c8-34c0-98cc-9c9823ec3a15 | -7.56922 | -39.63076 | 2025-10-08 11:38:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 4852a713-005f-3a95-9c68-efbd7392b4b6 | -8.02729 | -39.54206 | 2025-10-08 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 705298de-0986-35b1-bb68-9c98a5b8960b | -6.1508 | -39.30489 | 2025-10-08 11:38:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ec9f7099-d446-36d4-9d8d-1f2aa4133cbf | -7.45804 | -39.94851 | 2025-10-08 11:38:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| da20c46b-20c8-3544-b1db-2718acc4b163 | -6.57455 | -39.1912 | 2025-10-08 11:38:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 97cde4ae-07f2-3a7b-ad49-88bd613b2217 | -8.68868 | -44.71468 | 2025-10-08 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| aea08dcb-7285-3bf0-9526-01308fd4b4e0 | -7.02512 | -42.8639 | 2025-10-08 11:38:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 149.2 |
| 363384a2-c491-3c76-bde8-e95e27f11370 | -7.78515 | -44.21717 | 2025-10-08 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ead421b9-61ef-33e9-8095-46214632f32f | -6.57597 | -39.1815 | 2025-10-08 11:38:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 800b1fa2-be59-3180-8c5c-e3fae5fbffc6 | -11.79203 | -45.05053 | 2025-10-08 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 3612729e-f6a0-3010-8035-53a731e40953 | -5.40204 | -43.24969 | 2025-10-08 11:38:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a0bf608f-97ba-304f-8897-1c11ac960688 | -7.54788 | -44.31123 | 2025-10-08 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8407a298-2df0-395b-a0cb-53c4a7133f08 | -7.28774 | -41.97488 | 2025-10-08 11:38:00 | TERRA_M-M | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 82c69fb4-7422-322b-8ae7-c4863aa3d00d | -8.51034 | -36.57841 | 2025-10-08 11:38:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| cb474ab6-dd37-3a46-9853-20d51f51ec10 | -7.8012 | -42.60986 | 2025-10-08 11:38:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5fba7df9-1674-37c8-aba5-5e65eb2e75b1 | -8.18587 | -43.33214 | 2025-10-08 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 149.1 |
| efb6bb51-177d-3cef-8365-5ce3679f0479 | -7.00815 | -42.89524 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| ddf58b56-44a2-3e08-86a4-7da488e84ba6 | -8.1032 | -39.46044 | 2025-10-08 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 43244ef1-7d5a-322f-9761-75303d61f1eb | -7.78676 | -42.40614 | 2025-10-08 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| b467573e-8b5e-3eae-81ed-4a4a8900f7e4 | -6.92516 | -37.92794 | 2025-10-08 11:38:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 44133c18-5de4-3010-9802-edc7fee02eca | -10.78545 | -39.54182 | 2025-10-08 11:38:00 | TERRA_M-M | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f98d4cd-de34-3b9e-a607-d74b1799f34d | -10.2213 | -39.36322 | 2025-10-08 11:38:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 54557325-7769-3deb-9b03-192234468c2e | -7.79818 | -44.21901 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9e41e273-716f-3c26-9e07-9402811a02fe | -8.19526 | -43.35111 | 2025-10-08 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 16bfe4d9-176b-393d-b100-97db07b5d8bc | -9.08804 | -37.31135 | 2025-10-08 11:38:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f069c677-8350-3d44-bcd4-176877583817 | -9.24328 | -40.54466 | 2025-10-08 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bc643249-1a11-3dc2-8401-056265f7d587 | -7.5707 | -39.62085 | 2025-10-08 11:38:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 38.6 |
| b7c6dd70-145c-3585-858d-e568241f699c | -7.02001 | -42.89693 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| c70ae9cf-8e3c-353d-94fe-48a60e1e7268 | -7.44126 | -43.1487 | 2025-10-08 11:38:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 0bf1be7e-11f3-3f88-9492-664b9177f273 | -9.08931 | -37.3024 | 2025-10-08 11:38:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5c44ad14-8d33-3eb5-a8a3-0cb8abb4667e | -6.70211 | -42.19508 | 2025-10-08 11:38:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 8ae9ae7b-e618-3668-985e-0cf9202bec60 | -11.7469 | -50.9129 | 2025-10-08 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5505edfc-46bc-32fe-a34d-1387c73a243b | -13.3774 | -47.2411 | 2025-10-08 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2d492716-588a-3270-8a32-7e73ff271b39 | -10.4245 | -45.3907 | 2025-10-08 11:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d57bcd46-fe73-37ab-9e2f-4f896833969c | -12.5109 | -54.714 | 2025-10-08 11:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 97c9bf94-3d13-33e9-b478-5773aa0274d6 | -13.7368 | -45.6569 | 2025-10-08 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 125eecc0-d99f-31e6-851c-f648905bf90a | -14.7184 | -46.0636 | 2025-10-08 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 4288e866-9460-3124-afc4-71cc19e4417a | -11.7085 | -50.9385 | 2025-10-08 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b5f626a7-1ccf-3549-8fe2-b85cf653acea | -12.5107 | -54.7345 | 2025-10-08 11:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a050734f-d28c-310b-bbf4-31023554ff23 | -11.1644 | -54.8804 | 2025-10-08 11:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 2695acd9-ce13-32dd-89c8-20eb9a9b642c | -13.0009 | -46.7795 | 2025-10-08 11:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 86bfabe5-ddc5-358b-a204-d56cfa4dbc2d | -10.9106 | -47.1353 | 2025-10-08 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e0c1f5a1-0baf-3b0c-b273-ac6a9d43696d | -13.8343 | -51.8529 | 2025-10-08 11:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 39a3bd4c-7ca6-3ee5-93dd-4d26f063b2d2 | -10.4251 | -46.591 | 2025-10-08 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| e754f78f-38a2-3385-965b-e4780ef80ecc | -10.4435 | -45.3882 | 2025-10-08 11:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| ce49344f-1ebc-30f1-8894-f0b981d847dc | -11.1833 | -54.8787 | 2025-10-08 11:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| b0efadbc-bae2-3bc4-b399-3f35aa1a2313 | -13.7364 | -45.68 | 2025-10-08 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 3e184102-f089-35de-9e03-ab2beefd7d2d | -14.7179 | -46.0867 | 2025-10-08 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a09a9c51-59a6-3005-b43d-23a883ffe2b8 | -10.9296 | -47.1329 | 2025-10-08 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ad23d3a5-30ef-3478-b38a-4e3f4b3a68e3 | -13.79848 | -45.78902 | 2025-10-08 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 56776868-6283-33da-9004-f3e32bbea1a3 | -13.76301 | -45.76026 | 2025-10-08 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 7c4a9481-a6a5-354f-9a20-b42454f89b12 | -13.35263 | -47.60357 | 2025-10-08 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c3d68e2e-a081-350e-a2dc-eb315111478f | -12.25243 | -47.8501 | 2025-10-08 11:40:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a07f990e-8f1c-3bee-8ec9-4047ae8c823f | -13.38764 | -47.24411 | 2025-10-08 11:40:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 540c196a-34a6-3af7-a4a3-92071956aa25 | -14.91006 | -41.4519 | 2025-10-08 11:40:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 57987ecb-9867-32cb-a5c5-8b7ae4512145 | -12.27328 | -43.11253 | 2025-10-08 11:40:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 90b25c70-0317-3e04-8dcd-fc63ded1a48c | -13.247 | -42.05864 | 2025-10-08 11:40:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |


[Clique aqui para ver as próximas entradas](README99.md)
