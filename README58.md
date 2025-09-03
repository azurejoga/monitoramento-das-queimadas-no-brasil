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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 625431b9-77f2-3d2f-b925-14bc75beb399 | -6.72745 | -42.26842 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eaa0eae5-6f5d-32e2-b593-8ae3194d2345 | -6.41452 | -43.75747 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13c3b18b-5909-32ef-bf68-b6c4b4b53799 | -5.86339 | -42.97623 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bf13a79e-33e4-33ca-bf5b-23d5a1479906 | -7.53672 | -47.43657 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb301510-6699-3f55-8d9b-1c9c76603b8e | -10.48654 | -53.64869 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 916e8326-c7bb-3542-a98e-a6c736cb0b4d | -7.69703 | -48.74035 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 23.9 |
| a72a6659-dba9-3b3f-9599-b3f7627a45bb | -7.53332 | -47.45962 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7bf44b6-8afc-338b-8b3b-665bffc2cbab | -11.6777 | -52.18955 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aad42e19-b205-3dcf-a7f3-e84f31021134 | -7.79536 | -45.44034 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64f725b2-8a6e-3999-8d3a-4a9733945ca3 | -6.41382 | -43.76252 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef9b887f-cc3f-36f1-8e56-1b1829ba3850 | -11.5841 | -52.11305 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59dec1fe-6b45-317a-84bc-b1aa5ebbd077 | -9.94637 | -51.62177 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 664a482d-acca-3987-b6f6-0309d050bc67 | -6.80516 | -52.81361 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0160a03-81aa-3d9c-9d01-a95aca9b4177 | -9.69316 | -51.03886 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9aeda4c-e502-32e8-9908-565db494e572 | -11.60607 | -52.08062 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fcc6bb9-2fdc-3b8e-afd9-9ebaf936d3a5 | -7.78969 | -51.08012 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80c78e1d-f843-3caf-b6ac-b033629c8305 | -11.08078 | -52.02525 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c68105d5-c856-3e38-9c20-5d641437bd3b | -11.80441 | -51.54494 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3594e7ec-2fc0-3d7f-9c51-9cb2c923dac9 | -6.84111 | -52.8268 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8447250a-50ff-3dfa-a220-a9bb1a89dcb5 | -6.27819 | -44.51196 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94ce3986-7944-3f68-9c14-dda70442bf75 | -8.36251 | -48.30249 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77b228e-d08e-39c2-9d86-fa379b2caf2b | -11.18948 | -55.01559 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e59a36e-54cd-305a-a7b4-6ad7d1ce376f | -10.10401 | -46.2522 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a036ef9-e7ac-38a8-a397-47fa4b442259 | -7.49929 | -45.33794 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99b6465b-eecb-3515-85b8-e4d9821d80d5 | -7.69997 | -48.7448 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 835ca266-c6d5-368e-a274-75005dfdec6b | -11.44815 | -47.30494 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 174343ee-b5d5-311f-8039-f2a4bae29ee3 | -7.11857 | -44.75265 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8fac18fb-6d4a-319e-8c29-01e4683f779b | -11.64622 | -52.0403 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec22b23-0da3-3def-bbba-518df8d8218e | -5.86625 | -57.77412 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4f92d808-2ad3-3897-80f3-dfe124b3c0ac | -6.7934 | -52.8006 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9b8bb28-7487-3ea6-96c1-9735a719790d | -7.90032 | -46.45865 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b799f4d3-30d2-3bfd-ac59-9a63147d0ed1 | -6.74352 | -45.91345 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c02914c4-8143-31e3-8b04-3c143be48b56 | -5.59798 | -51.95085 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c724f57-5e1c-3c54-bf62-463dcd93be28 | -11.62918 | -52.06276 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bca01061-0315-3e36-994a-1c5702ebba59 | -8.8806 | -45.83297 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e8819bb-c927-3d1b-934a-ee2e6be3d8c7 | -10.48255 | -50.34306 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04e12c72-0867-3528-9703-5cd2ced5bc18 | -10.28926 | -54.25902 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30cf2fa0-c697-3257-ba99-a010fb1ccd61 | -7.63451 | -46.54573 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d32ede04-9428-3a0f-bc97-acf1fba0904a | -10.20538 | -54.30085 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1eda380-a870-346d-99ea-7e8f32fd7e89 | -6.54877 | -44.56277 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7404716b-169d-3775-a76f-3e50907cb48c | -7.49988 | -45.33383 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea6d9d9-b7ef-387d-914e-5f09cf9266ea | -5.70591 | -53.69127 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdff57ba-36fe-35a9-ae75-6bfc10c1d0dc | -9.29618 | -47.08732 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1fba767-815e-3fbe-b5e7-dec494bfdb86 | -6.84787 | -52.82786 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c861d0f-2309-3de1-a2a6-0aac39da821a | -10.28519 | -54.26229 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d9bf8f-395e-318b-90b6-ccd548f6efad | -9.33806 | -55.22682 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 107476a7-50f3-30cb-b9f8-88dce2f9eb4b | -5.9008 | -57.73362 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d1ace66c-736a-319b-87f1-f0abdcca7548 | -7.50619 | -45.35146 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7027932a-ce6d-334b-9386-21580430338c | -5.90457 | -57.7386 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a9e426db-3605-32e0-a053-cf074a49014a | -7.91041 | -46.44596 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 010355b0-eceb-37d9-8f18-68178e90bfa2 | -11.65822 | -51.69948 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d6b47d4-e77c-3c91-95de-8ebddc7e0414 | -11.21733 | -55.06577 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92b8ad76-c375-3446-9c4f-e97cee4b6937 | -6.03702 | -46.02048 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cc2bfb8c-2798-3b83-adca-a6fb32c4c1b3 | -10.47204 | -53.63132 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c83dc0b2-27b7-333e-84c7-92276b84d84b | -9.81886 | -48.31661 | 2025-09-03 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ead9fd9-fb8e-3d2b-9118-882e9c3d5353 | -11.1972 | -55.01274 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 214dfcee-e542-3dc5-ab0e-316b8252763b | -6.03649 | -46.02403 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 589ea5e6-b7df-3667-adea-b5faaf779a0a | -10.49109 | -53.64194 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b9c2041-892e-38a5-af86-9c3d7e56ca10 | -6.2445 | -42.62384 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 36d1aab1-0d1c-3cbf-8d66-1d6d0380f2e9 | -11.60614 | -52.12376 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b6774b-347d-3188-b042-260bd6a3cda1 | -8.07239 | -45.38293 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 519f20dc-88d3-3567-9054-ce9397c3fcae | -6.82926 | -52.83609 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10287223-1dc3-3d00-91de-8ee406e3e1d4 | -6.21988 | -53.59043 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8d1c45a-965c-3ea3-b2a9-9e9da834a12f | -11.44864 | -47.30138 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d05de8e3-f3ff-3e4a-b633-36f3dc74c850 | -5.91273 | -57.7174 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3f4822d4-48d3-3629-90df-f5606f402d16 | -4.52951 | -54.96942 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79c4e94e-25f3-3feb-9b3b-8a802a40fec5 | -10.49331 | -50.34093 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e289b3-d356-36a1-b375-929abe9aa019 | -6.79224 | -52.80784 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c8cabf1-c294-303a-b38a-d9128ba629b5 | -7.48546 | -44.8325 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a747fd20-f3e8-36fd-9da6-9b12fc7e4d88 | -6.47419 | -45.40657 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ac4ae3b-2e49-33ee-a437-bbcc0177b145 | -6.54636 | -42.95671 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13635860-a325-39d3-bce9-e4b63efd48fe | -7.70529 | -48.73359 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1ae02c91-4506-3cef-8fb0-9bc10ec663c3 | -6.76655 | -43.72176 | 2025-09-03 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d80335e-1986-3714-8d8f-406fe8cf7941 | -11.61871 | -52.06467 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 088966e1-7db1-3def-80de-603adfd8a8d9 | -8.34816 | -52.52699 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77297ba1-3d50-3e0f-85ba-7a1a7a5c8796 | -6.24701 | -42.60563 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c848c04d-7b47-35bd-9c56-f11e30754632 | -8.09498 | -47.58808 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2f73f2-10a7-39c6-857c-a9b43cf9cdd5 | -9.25976 | -56.89998 | 2025-09-03 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7ff369-1fee-3331-b888-3a95487fdd9c | -11.82303 | -51.44566 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 705cdfed-2169-34f3-bbac-4eb748f5acf6 | -6.73445 | -42.25657 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 576721b9-647d-354e-939b-908c8afb0479 | -9.95906 | -51.62735 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803ecda4-3748-39b3-9c8b-aa9b72599b78 | -6.69456 | -48.40117 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d5ad22f7-629f-3098-a816-8ddf13c0bb3b | -6.70524 | -48.40255 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2150b0a-1707-385d-be6c-f49202a7b434 | -5.91795 | -57.74125 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4313d652-96b9-3d6b-8c1a-57f4ca4c23c5 | -11.5995 | -52.10114 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f464a6e4-1a64-37e3-90e6-d375d3938964 | -8.36643 | -52.54074 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ae8616b8-b738-3d84-be90-2aa6c535ce3b | -7.72407 | -50.24674 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7df1be2-be1a-346f-9537-8d4cb22b9b31 | -9.74915 | -46.91303 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a06d8652-93ac-347a-8d7d-a5f439f1de1f | -5.90746 | -43.23183 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fff764f5-5e1c-3291-b995-06e429904eb3 | -8.21588 | -49.56968 | 2025-09-03 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a3a7a1-c527-38e2-bd9a-0a43c8462939 | -6.34246 | -53.44016 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda253b7-5073-3a50-b4c8-cbb2fdf5e5a8 | -9.15346 | -49.65028 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17dcf5db-55f3-3334-a90e-20e5ef4e03f5 | -10.13047 | -46.25051 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf3f342-f79c-397f-b2c0-6a3a2523210a | -10.95395 | -50.77203 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d817b7d2-806e-3751-8dc6-1500eae9078f | -10.28126 | -46.49746 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44d375ad-04ca-3dfe-9ee1-f4822ef1a020 | -11.26815 | -48.9417 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df83a184-1595-35e3-bb5b-51b9970b0e12 | -6.45596 | -44.67858 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a904c7a-15c3-3327-a1a2-4e8d821f43f6 | -8.3674 | -48.29456 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61f1faa7-c64e-3fec-bb91-cd821dcaa3d6 | -6.57953 | -44.57205 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0742b45-734b-3b27-9fe6-88883d84402a | -9.63153 | -47.03947 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README59.md)
