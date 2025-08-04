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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0905ea1-114d-35ce-98f7-5b9df67764c8 | -6.32663 | -45.65089 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6c1aa9b-5fbd-3e94-94bd-cd1f2253a7a3 | -7.63218 | -45.29132 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebfa2ca9-5e32-3692-8c3f-81490aadeebe | -7.64536 | -45.30202 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46d78430-8631-39aa-aa8f-a50b805fa2a1 | -7.9673 | -45.10225 | 2025-08-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac02cf58-a3b0-35dc-9756-7b5e32ce1297 | -3.69176 | -41.13412 | 2025-08-04 04:08:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c3e8c0f-5900-35fa-8c84-77f8aed22a49 | -6.20094 | -43.75906 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4aa2deb1-5644-38a3-8c01-97c2344a3fa6 | -5.54553 | -45.20193 | 2025-08-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b67429b-81f8-3f79-859e-f31a1387aff6 | -8.03707 | -43.11016 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 57ff26c5-adde-39ba-bc60-b2e9f62a2ac9 | -8.00103 | -43.14803 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| ab7b92a4-ca8f-3bc0-a3cd-2653fc1543cd | -6.63332 | -43.66985 | 2025-08-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dafab3db-07cb-38cc-878f-26853e8a47f4 | -7.55542 | -44.89132 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9143d48a-0c94-3064-a711-ef4b0c405508 | -8.36031 | -46.90903 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ca4fa21-e6ac-3350-afd0-d2404e2387d2 | -6.60929 | -44.0368 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b698a80c-4a96-3e27-9009-0d18fba3c7c1 | -8.26991 | -47.37615 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 247704a5-e6b1-3db0-852f-9ef852e19a9a | -6.54094 | -42.80939 | 2025-08-04 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52efcdc9-255f-39d7-9500-ae4affe0f6b0 | -8.01641 | -43.13232 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 228e6461-3c7f-3040-a1eb-356f40cbacf9 | -7.4479 | -48.94195 | 2025-08-04 04:08:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a59ccfc8-28b8-3c59-9e0b-a5931e7af62d | -8.0588 | -43.10273 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e06ff560-5b31-3934-af42-6ddcb127a223 | -7.60868 | -44.06943 | 2025-08-04 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aed278d9-94b7-343a-b2cb-0a8e1d88205f | -8.00437 | -43.14856 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 4117ec3e-1d59-3c67-867a-eb29f7b75623 | -5.88154 | -43.73645 | 2025-08-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 655cab0a-b698-3c3b-8a89-269e82244afa | -7.33529 | -44.68398 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cfe488e-cddb-3921-98f9-1b34da7dc703 | -6.70417 | -43.33849 | 2025-08-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c125e77-5561-31d8-a443-4cf413c6a57b | -6.06724 | -44.67231 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57abb69a-d865-3156-a9cb-f72d8d40c957 | -8.35831 | -46.94554 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0603643b-61bf-392d-be73-9f848327023b | -7.19191 | -44.49483 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69320a13-c409-3b55-99ae-6b87149d9c8e | -7.56363 | -44.41586 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a5505c-4213-3a25-951e-2880302d297e | -8.5522 | -47.46209 | 2025-08-04 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf7a721f-9982-3365-94a2-9cad6917cdcc | -4.13396 | -47.64395 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b8002faa-4046-3c70-ad84-2ae7c0c9fb9e | -10.57006 | -45.27675 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b18b1d15-6dc6-373f-a0f1-ca1b40aae935 | -10.29625 | -45.17903 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe75afe2-af92-3316-aa00-c7e547b7bb39 | -8.31582 | -47.52358 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 296513cc-024d-383c-9a20-77e2db889efd | -6.6293 | -43.67303 | 2025-08-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff8c9755-0d96-31cd-bb8c-8777f5c16207 | -7.26815 | -46.16125 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54650f58-2ced-344b-92e1-2cf94708b0a3 | -7.99765 | -43.16939 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b81d088a-fc57-360a-9a19-5ca5b37a5a2a | -5.88499 | -43.73699 | 2025-08-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3bce44d-bdef-35dd-8b24-b4eb72aea2d2 | -6.54283 | -42.81392 | 2025-08-04 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c38c3092-0c47-3d2c-be38-c71279b9d77d | -7.33401 | -44.69179 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82c3abc9-eae0-361f-8db4-d0fbeebfd5ce | -7.78167 | -45.22342 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5d5c938-9136-338c-8941-0ea704e0750b | -7.55098 | -44.87383 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 903d0167-089a-34b8-9225-3b9a588c4f4a | -8.27176 | -47.36515 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c028c2ea-945f-33c9-9468-d1d00f4ff7e6 | -7.77446 | -45.22218 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4cec7b00-fa1d-3d71-bb30-434e97cf0050 | -7.31253 | -44.66847 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 691bcf12-d56b-3c4f-b8b9-9f43df81f162 | -8.00434 | -43.17043 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 282915f4-d4ff-37f7-8f7c-506772969acd | -8.0174 | -43.16891 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a3ab9759-b86e-37a4-957f-63f0fcaf10ce | -7.8435 | -44.94826 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa6a881a-926a-3d20-aea7-ed27faf1112d | -8.05546 | -43.10221 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 35446748-ceb4-3900-8356-4a2720dadb3f | -8.01569 | -43.17957 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb6d0fa3-d052-3a3f-83dd-16801ebeed45 | -7.21433 | -41.8564 | 2025-08-04 04:08:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5198b19f-3f1e-3eff-b05f-1a763b982081 | -7.28147 | -43.04776 | 2025-08-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3432cd47-77d8-3bca-9b92-fd2dd0ab2ae1 | -8.37133 | -46.91604 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11d6005-e434-3782-9cfe-f6a2ca8a6d13 | -7.77377 | -45.22639 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f891c924-3c0d-3304-9f45-fbe8a9cbdc1c | -7.52977 | -45.04768 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 468076ff-e44f-37cb-b642-e442cbb74ff4 | -7.13666 | -44.07664 | 2025-08-04 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c5d3600-ba23-383a-8bd0-69ad3b1f27d5 | -6.32587 | -45.65551 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b3f7c48-7de6-30bd-a07e-6f1d62d804b4 | -6.70358 | -43.34212 | 2025-08-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9fb40d27-2d4e-36c6-aef1-7bd6bddccfa8 | -7.13824 | -44.08881 | 2025-08-04 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f016285d-9062-3ff4-a946-a1ef909c285c | -9.62361 | -43.85434 | 2025-08-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21bced60-f010-3f8a-ad21-70624bb7f215 | -4.12883 | -47.6475 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ca4614c-1ffc-39fa-921a-9961e098abc2 | -5.87897 | -50.14592 | 2025-08-04 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32d8bff8-ce41-387d-9781-a8ace2f0d5c4 | -4.74492 | -44.4445 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3c6e48f6-1c2c-3f61-8b4f-f480635c1c17 | -7.08203 | -44.36875 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa13bb8b-6434-3f57-bcd5-b23407b22c9e | -4.131 | -47.65664 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a88882d2-a6e6-3111-8be7-8b8d44e67cf5 | -7.99877 | -43.16227 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6193cb9c-f146-3fa2-91b8-91954cda9d42 | -6.70514 | -44.09569 | 2025-08-04 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b0dbdbb-64f7-36ef-a3a4-70cfa56bcb5e | -8.00329 | -43.21409 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea385cf8-aa6c-317c-9398-a08f3025394a | -7.83407 | -44.9437 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df87f3cb-5705-3242-afea-ac1770eaf754 | -8.00036 | -43.21727 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 360cf783-aa19-3e5b-b778-df9b1a2856e5 | -7.56032 | -44.88373 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b28759c-950e-35b6-9d28-35000c3d6be0 | -8.0326 | -43.11672 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7ee0dc7-a600-3566-bde9-66ad051ffa09 | -8.00883 | -43.14199 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| a4c8e446-b579-307b-b508-594cb854a8a2 | -8.73422 | -46.40898 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64cdc119-0911-3b07-b072-1c2568f87aee | -8.02864 | -43.14153 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d648d645-ebf9-3b09-bb43-d350f0605233 | -8.43874 | -47.46487 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd6e4c72-c661-3246-9d35-0c4d150d85e3 | -4.74624 | -44.43619 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7380ae21-13d1-3d2a-aabb-9701d17c5adc | -7.77152 | -45.2174 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e71e1d-bf15-353d-b677-f32127f17624 | -4.7397 | -44.43093 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce8ef15e-dd51-37e0-945d-632963cbdecd | -4.74198 | -44.43978 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fbe5c329-331c-35ee-aed3-c4a1d898e131 | -10.29539 | -45.17961 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c78f7104-371e-340b-a002-f9160cdd2119 | -8.38422 | -46.93076 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dfdbc7a-64f3-3e63-9545-f745e65db003 | -6.95839 | -44.503 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 263e9a69-113f-3436-b312-c113d9ed870f | -6.26325 | -44.06923 | 2025-08-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe4ffd43-06af-369f-a935-44d60a82f56e | -8.00381 | -43.15211 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 7701d087-7ecc-34e7-a856-a3d6e0203fe7 | -5.8862 | -43.72943 | 2025-08-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eae1ed5-0740-3219-905b-eff0cb98606a | -6.7024 | -44.2454 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f56cdf89-eab1-3da7-a6fb-74435c93acc9 | -6.1768 | -44.78159 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e8d6c6d-89f7-3ea2-a172-cdede7119b18 | -4.1274 | -47.65645 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4aaeb051-5d5b-3137-8689-bbd2d4fe493f | -8.03141 | -43.14561 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b3ace5e-2cee-3c51-875c-aa2f16fa74f6 | -7.99423 | -43.21264 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 871b3ba6-7878-3da9-bad2-763e1bbbc410 | -8.01329 | -43.13543 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aa198974-f9d8-3665-bb45-87849ad05680 | -8.04375 | -43.11123 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 7baa5b68-5e6e-3ffe-8435-8fc78624e3ef | -10.56785 | -45.26825 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 757345e9-4cd0-3b3d-9e6a-7bb20b4ff487 | -7.56122 | -44.9006 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0546bdd-ce31-343f-9869-751ea502bfae | -10.59437 | -45.26038 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fde747f-acbe-327d-a152-c4e81f81fe10 | -7.78235 | -45.21922 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5d46470-c904-3c54-89fd-ef645875e496 | -6.64825 | -45.89183 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3472f599-86dd-3bcd-9e63-839f03e99b16 | -6.326 | -45.63142 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0420bdbe-592c-3f48-9ab6-400a35f973b1 | -8.01626 | -43.17602 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8e31ab9-6d74-392e-9f96-99e252adc5cc | -10.60139 | -45.26152 | 2025-08-04 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75a7b7cb-5455-32a7-b56e-14f5bbb1a7ae | -7.53962 | -44.8762 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
