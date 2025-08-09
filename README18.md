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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2485e9c9-6242-330b-80db-dee8ba8594d5 | -6.55275 | -43.19168 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 569c88d4-57a3-3d01-a66b-6691f4030004 | -6.05392 | -43.74696 | 2025-08-09 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 975c451d-15ea-369c-b1e3-7b581d04bdff | -8.07394 | -46.83946 | 2025-08-09 04:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 896026e6-a7ce-3519-92c3-b172a5d980aa | -6.68665 | -43.35268 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b6045540-a86b-3741-a82c-d417dc4ddade | -6.66889 | -43.34267 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f0f9289-f7a4-316b-ac5a-be8ed1a27eaf | -4.87011 | -47.75617 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b67cc262-9e6f-3030-9c98-2827192881a7 | -4.17025 | -48.57528 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5c60b95-27ec-3ad7-b928-7f641d1749db | -3.07134 | -40.81805 | 2025-08-09 04:40:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91a81ef2-cf7d-3b49-bc7b-dee23f7ccdf4 | -9.08062 | -40.48139 | 2025-08-09 04:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a8992ad5-735e-3299-93ca-862bcf8df87e | -5.90234 | -57.71524 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77a1bf96-fb81-3e6a-8bbc-cfaf6795f4e3 | -5.58926 | -42.27695 | 2025-08-09 04:40:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5dccaf1-e6a2-3d57-869a-7e62c7a26a37 | -6.31855 | -42.35777 | 2025-08-09 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fe639b2-c995-368c-8c99-ac3cd42907f4 | -6.20051 | -55.61604 | 2025-08-09 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67bb25a4-ccb4-3196-be68-c0cab339aa8d | -7.25161 | -44.32424 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc81fcd9-ac22-32fc-9d1f-5c0c493c3c44 | -5.08432 | -48.31262 | 2025-08-09 04:40:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adb3576f-293e-39c0-a2ca-f6a0b9b72f4a | -7.11263 | -46.10638 | 2025-08-09 04:40:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 846ae713-0f3f-32e2-b4e7-85c24a7cad5d | -4.62608 | -47.41796 | 2025-08-09 04:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8914ac65-acab-399e-8ca3-f843a39110c2 | -5.22327 | -43.1932 | 2025-08-09 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fa67ac9-eff6-3c2c-8c6d-2eeb113e1087 | -5.42184 | -44.01012 | 2025-08-09 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83c420ab-c885-3095-ab5c-b4dd0c356716 | -4.05224 | -47.31492 | 2025-08-09 04:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b412ba0b-f906-3551-8549-a49611644c2d | -5.48333 | -42.16836 | 2025-08-09 04:40:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c76b3c1f-132a-3a17-a5e5-c3ad3c7f7c70 | -3.82202 | -41.56338 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8101d790-ce7e-3671-a742-7cab15cd3145 | -2.494 | -47.56991 | 2025-08-09 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d783c3d9-508e-3a3d-8dc3-bd23208aa666 | -8.11296 | -47.43475 | 2025-08-09 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14383413-1903-3839-8983-29bae41270d9 | -6.13725 | -42.97076 | 2025-08-09 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 27b6e538-348a-3497-8b17-1dac85f676e8 | -6.59617 | -43.38678 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 194fc2fe-c73d-370c-a61d-ad019fbb58ee | -4.21177 | -48.1627 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30b6b4e0-bc20-38f2-9f10-770650f229c2 | -5.88091 | -57.74831 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10fa262b-4272-36d4-8c1e-bec0a75617c2 | -5.41777 | -44.00948 | 2025-08-09 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04e71286-c754-3899-a5bf-036ee591cd56 | -6.92863 | -44.69618 | 2025-08-09 04:40:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af47be3f-0301-3099-b538-7c53f095b618 | -5.48401 | -42.1636 | 2025-08-09 04:40:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0d80f58-d57b-3fd1-bd71-df922cfb50d0 | -3.06645 | -40.81731 | 2025-08-09 04:40:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7cb1229f-b5c2-3e84-84e6-f2c9b14099e5 | -5.27466 | -44.95332 | 2025-08-09 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2972f22c-33bd-338a-ada9-e7c6a5b4a71c | -6.60594 | -43.38021 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6540426-e797-3987-9382-de057c0d945c | -3.98666 | -47.89092 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7cc27c5-3ece-3d3f-9562-8331eadd872d | -3.82131 | -41.5683 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| befe714b-ba1e-363f-8213-765441119073 | -4.00624 | -47.94067 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4189e521-e219-3213-9625-7ecf2ff907e6 | -6.25112 | -44.82772 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0535692c-2010-3d88-89a6-e4ca852ffc31 | -5.27918 | -44.94928 | 2025-08-09 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5c5c204-f8af-351a-a531-fcae9cd4d1a9 | -4.87348 | -47.75669 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d7fea66-e5b6-3402-b6f1-521010e0b5eb | -6.68005 | -43.32717 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 09dae79c-5a6b-3394-a4e6-4a93342d8307 | -3.51206 | -47.22184 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f9199e8-c4ba-39af-8347-a620930b9469 | -4.11158 | -38.17329 | 2025-08-09 04:40:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dd691a84-66f3-37c4-bf6e-db7e96899b61 | -4.29578 | -48.05779 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5944e7ab-1784-35e9-983a-3fae2f8016ce | -6.13848 | -42.96229 | 2025-08-09 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 2df39c67-0922-3e90-bc1d-079e9c1bc0d2 | -3.84304 | -47.75385 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32a81643-34de-357d-9f5b-b6b3a2d10a4c | -4.29638 | -48.0758 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41a61a26-bdbe-3645-98bc-22ed4f25c885 | -6.59559 | -43.39082 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ef1b12a8-3dfc-3bda-86a4-5021a7498c20 | -5.90521 | -57.71356 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7fc1cfd-768f-3f7b-976e-fac1c9c3e4b3 | -5.84385 | -42.95599 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abd97603-a8dc-3a90-83a1-85034b12b6e4 | -6.13786 | -42.96653 | 2025-08-09 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b65d707d-cbef-3c8e-b1c8-fb4741877133 | -8.10948 | -47.4342 | 2025-08-09 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc9c66f-2276-3043-8519-432777303574 | -5.88558 | -57.75185 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 20a5688c-c599-3cd9-846a-a3aa67ae2803 | -3.65197 | -48.324 | 2025-08-09 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4aa561d-51b9-3d88-b675-1f34c4b1af96 | -4.17303 | -48.57925 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f2da94-7e93-3880-824b-f6e5584d3cac | -4.99954 | -56.03896 | 2025-08-09 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 646a91ae-c8a6-3854-b0bc-eaca3ddd1b02 | -3.18244 | -48.80875 | 2025-08-09 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa582e31-e662-3b31-9362-45874c9900fa | -4.87546 | -47.40725 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b615799-921e-3b9e-9f89-127778f333b1 | -6.34442 | -55.56503 | 2025-08-09 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0df8542-1f6a-39f4-9881-1e5ebe3df97e | -6.94057 | -46.0605 | 2025-08-09 04:40:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ee08033-9af0-3fae-959a-e7b2823dcde8 | -8.05749 | -46.33414 | 2025-08-09 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1016103-459b-33e3-a25d-0febd1947d70 | -3.43016 | -49.04202 | 2025-08-09 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0264ca5-9af8-38ff-9df7-d692999b5dfe | -4.47604 | -48.11472 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d918b55-5509-30b6-a0ec-09b92732ee41 | -7.25307 | -44.65434 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e851f030-0876-3bcc-9e8a-2748539da127 | -6.62556 | -47.28676 | 2025-08-09 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 18f79609-1621-3907-803d-0f96bd29f9de | -3.82022 | -41.56644 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 434225ac-67b7-39c9-81a1-3b832fef75a1 | -6.96587 | -44.49532 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a2750b8-98b5-3b7c-9581-c2590390e60b | -6.06821 | -44.87865 | 2025-08-09 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7208819c-023c-379e-8dd9-5549eae8aa55 | -6.0581 | -43.74762 | 2025-08-09 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e88bd168-f6a1-3a78-8ec2-ea09007000ee | -6.6221 | -47.28622 | 2025-08-09 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3384c8b-aa96-33f2-8014-9f72776e5366 | -9.0773 | -40.00661 | 2025-08-09 04:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 524cda8c-afcf-30e4-9237-41c7694cdb56 | -6.0927 | -59.92434 | 2025-08-09 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67b5f41-50fc-3290-92ed-bdefc4476114 | -7.29202 | -39.64003 | 2025-08-09 04:40:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89d15955-ff96-3adf-b4bb-4db9a99ddc04 | -4.02535 | -48.05825 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42409f87-49ab-386a-822f-3bd1f54ce767 | -5.27604 | -44.94402 | 2025-08-09 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc4de7c4-3b4e-39fb-aa11-7216aebf221b | -6.67323 | -43.3433 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52fcff66-d13d-3f86-a19d-cd8ca4a271ba | -7.2636 | -44.52331 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4be30ad6-ee8b-3912-9b17-7fd744d2d4f8 | -7.60739 | -45.29274 | 2025-08-09 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d39f2b5b-7780-3ebe-a78a-aa9940623a09 | -2.44821 | -47.32555 | 2025-08-09 04:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c89cc227-afcc-3062-b752-7fd66b5eed09 | -4.47549 | -48.11821 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3220dab-ec0b-39a8-9700-5359a933aaf9 | -7.17391 | -44.40181 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cf67e89-6c7e-3c1d-8eda-2b1b2f44e1de | -6.94424 | -46.06102 | 2025-08-09 04:40:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28068543-d97d-36ad-84c1-f2a5e7876748 | -3.9638 | -47.88375 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f4d98f79-5ff9-3599-9bac-1e8f4e5884fb | -6.09193 | -59.92861 | 2025-08-09 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0df626e-5bdd-3753-b923-686ede1583d2 | -8.05879 | -46.32558 | 2025-08-09 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf78d84-87bd-393f-ac80-8aac628a2589 | -6.06433 | -44.87809 | 2025-08-09 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f2ea4b2-ac17-30f2-8a58-88604247f45f | -7.26443 | -44.66073 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68155c4e-05c1-30ec-96fc-888b962cdfc6 | -3.27996 | -48.81342 | 2025-08-09 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4558f48a-eac8-326d-ba47-4f7b08fb35ef | -7.57848 | -44.40878 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e45d380-3d35-3bad-ad43-d8585f54776d | -7.40171 | -47.13721 | 2025-08-09 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9502444-4b73-344d-b6a5-60e75ae6595e | -4.0248 | -48.06174 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 122b4160-5953-3d5f-bf4b-ec64a8f094a7 | -3.23062 | -46.78772 | 2025-08-09 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4caf329c-7b37-39fc-9f5d-25f21d19a770 | -8.08107 | -46.8406 | 2025-08-09 04:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89e7e253-2b0f-3891-afeb-98b71080a89a | -4.30026 | -48.07283 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e73f63e1-6d24-373c-8971-dfc9be123b72 | -4.47658 | -48.11123 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1f422d5-f68c-3134-8342-797723b31e68 | -6.68445 | -43.35713 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 60081b6b-1bb0-3e94-9db2-bf0fe7ee6cd9 | -5.83945 | -42.95535 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8525508-5edd-3142-b28d-66b9e20511be | -6.92466 | -44.69559 | 2025-08-09 04:40:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 994212e3-c21a-3e53-a7bd-d18e50c6f02c | -7.62821 | -49.84563 | 2025-08-09 04:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac4aaeab-6105-3347-b883-73fbd3c87318 | -5.28283 | -41.10687 | 2025-08-09 04:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
