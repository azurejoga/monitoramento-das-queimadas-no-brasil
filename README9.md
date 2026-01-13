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
| f87635f4-6903-3232-808f-5953a70b6da4 | -9.90638 | -36.08403 | 2026-01-13 11:17:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6bc891f1-33a4-31a6-ba24-fe192b447288 | -10.2 | -36.65071 | 2026-01-13 11:17:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b3aeb8d3-78d3-3bb4-b1dd-42ccfce6724b | -8.45447 | -36.60033 | 2026-01-13 11:17:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d1ef7606-963d-36e9-8d39-cf809085b91f | -8.05906 | -39.02575 | 2026-01-13 11:17:00 | TERRA_M-M | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| c363a347-95b3-3be4-883f-1a5e806989f1 | -8.2892 | -36.73216 | 2026-01-13 11:17:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 77a827c2-cd1c-3dd9-ab91-6457faf65471 | -8.05782 | -39.03158 | 2026-01-13 11:17:00 | TERRA_M-M | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c37de1d7-a5b7-3785-95db-7cb829b432d2 | -10.21511 | -36.86991 | 2026-01-13 11:17:00 | TERRA_M-M | TELHA | SERGIPE | Brasil | 2807303 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f86b5894-367a-36af-9817-abcebaddac08 | -9.39543 | -36.96046 | 2026-01-13 11:17:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 9d3fddb0-2034-39dc-8cfa-7108136947fa | -8.29576 | -36.12748 | 2026-01-13 11:17:00 | TERRA_M-M | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d38b99ec-1c4a-3b94-8bb1-087a72b2a5fa | -9.9078 | -36.07454 | 2026-01-13 11:17:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 32acdf24-d951-3cfd-9f6e-c161ed5f779c | -2.71949 | -47.43552 | 2026-01-13 12:53:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e839fba1-bbf4-3f61-b064-0a324a14f5de | 3.3151 | -60.51927 | 2026-01-13 12:53:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 018df612-edfd-30f5-8530-12386df61423 | 3.43188 | -60.61877 | 2026-01-13 12:53:00 | TERRA_M-T | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 11398a15-1c56-30d6-ac31-564772cae930 | -2.71814 | -47.42827 | 2026-01-13 12:53:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5d0cfddb-6ffc-3f89-b99d-4309d4b137a4 | 3.31326 | -60.50612 | 2026-01-13 12:53:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 56c26d82-ef7f-3cd6-963c-e4ee73f76fdd | -22.0833 | -54.79257 | 2026-01-13 12:59:00 | TERRA_M-T | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 4a90aaee-363c-3c2c-87f7-0bcbcd78ebc1 | -5.7545 | -39.3526 | 2026-01-13 13:20:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 376e058a-7141-3cc4-97f1-87b51364507d | -3.2905 | -42.5507 | 2026-01-13 13:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fa224c13-115b-3665-ba1a-14a6c17ac9dd | -3.2905 | -42.5507 | 2026-01-13 13:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c4cec11b-821c-339d-a1a2-4a1bc1c6ccf8 | -3.2906 | -42.5271 | 2026-01-13 13:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b3018396-22de-34e5-8850-e2652800f721 | -3.3092 | -42.5498 | 2026-01-13 13:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 026528f8-bc84-3f89-b0f1-1f3c739f3506 | -22.6761 | -43.7268 | 2026-01-13 14:00:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 143.7 |
| ddbcbcce-2ad5-3f32-a4b3-0bf77374cac0 | -22.6761 | -43.7268 | 2026-01-13 14:30:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 165.9 |
| 4b0e70f5-f65e-39a6-9354-51d3cf2cf684 | -22.6761 | -43.7268 | 2026-01-13 14:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 183.1 |


