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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34c8fbf5-9631-3751-8a1e-ea960b9302d5 | -12.43839 | -44.39808 | 2024-10-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a38a7474-fc91-34cb-b70b-af4609f46493 | -12.43324 | -43.74946 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0dcc6b0-a7de-3448-a55a-3a74e7a0b2be | -12.42813 | -43.74846 | 2024-10-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70f5bcf3-697c-3ca2-837a-c9312153598f | -7.26401 | -43.95475 | 2024-10-27 03:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 270cff7d-d1b8-38eb-923e-b0561da3532b | -9.44325 | -44.46395 | 2024-10-27 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccc13199-267a-3a4e-be29-1092d9bf1959 | -9.08687 | -45.0455 | 2024-10-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99ee19e0-f047-30ed-a619-daa8ef7a7da8 | -9.08608 | -45.04963 | 2024-10-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf6228f-3995-3fb4-9429-c17838572fd6 | -8.78861 | -44.72337 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 792260b8-ac23-3ed3-a7a9-dfce1eb6e00e | -8.78851 | -44.72239 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74861300-4cfa-3043-8d6e-0fba3878b832 | -8.78783 | -44.7276 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c539f2f5-ad27-33f9-8e00-57b1c0151959 | -8.7778 | -44.71688 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32b7bf45-7216-33f9-9c0b-8b5c6481ef37 | -8.77122 | -44.71997 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a26f97b-493e-32f3-8699-47e21eee3159 | -8.77044 | -44.72419 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 450f23df-60f0-37bb-9e7c-3f653a95adef | -8.76966 | -44.7284 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77363e52-9d8b-3bf2-a382-a4c0fb428d3a | -8.76199 | -44.7051 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8bea3f4-1f84-3044-993a-63ccd23c8b83 | -8.7612 | -44.70933 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2be867b4-524b-3f42-b809-0f0caeac77f1 | -8.76041 | -44.71355 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d0ff204-bcd1-3a0e-b78b-f3897c479064 | -8.75962 | -44.71778 | 2024-10-27 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22892a35-068e-38e3-b67a-f4636a49136b | -8.54657 | -44.95277 | 2024-10-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f1b6e0-c7c1-3595-b8b3-be7baba13642 | -8.54323 | -44.9511 | 2024-10-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c24ec5d-c983-3f08-adfa-977d03906dcf | -8.54245 | -44.95536 | 2024-10-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2efd9153-1a85-3d9a-82a3-bbd43dc1d08e | -8.54068 | -44.95156 | 2024-10-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 495af6dd-098d-3289-aaa3-8339bf1672b1 | -7.87578 | -45.37669 | 2024-10-27 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d5b6cab-2986-331d-9840-d1323fe1daac | -7.8696 | -45.37579 | 2024-10-27 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4d9740f-60d3-3ed0-ac2a-8e2fbe5f6d9e | -7.85632 | -45.41265 | 2024-10-27 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6b03073-8fe1-3aac-bd16-a68f9c59b9d5 | -9.9841 | -44.40103 | 2024-10-27 03:38:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90ab0429-5a6f-3512-b7b8-20158fae93ff | -10.76832 | -44.79496 | 2024-10-27 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f1778f0-04c7-38f1-8264-c2b0043a147b | -10.76757 | -44.79885 | 2024-10-27 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a4cd596-77d6-3da9-bd21-b4a932847de1 | -10.53792 | -45.1454 | 2024-10-27 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8e22cc88-dee7-3b23-9aee-7f5704e91f11 | -10.53712 | -45.14962 | 2024-10-27 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1d2668eb-e360-37ce-915c-045af3f93ae7 | -10.44182 | -44.57367 | 2024-10-27 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b4d3096b-18b1-3471-a54b-fc69bcdcdacf | -10.44017 | -44.57302 | 2024-10-27 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a656149-3fde-390e-86db-22c9af1748af | -13.27655 | -46.04028 | 2024-10-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e304359f-7a27-3739-957f-bafe9aac8acc | -13.27243 | -46.03062 | 2024-10-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c9dbc64-76f5-343a-93bd-da15e434aacb | -13.27157 | -46.03486 | 2024-10-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27a4e2c4-547c-3fa0-a38d-1168ed07bb1b | -13.27074 | -46.03903 | 2024-10-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3030c77b-5108-30ba-972d-28d860b99b75 | -13.26494 | -46.0377 | 2024-10-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1ef1c65-8257-3583-9e8a-3ddcbc88db9b | -7.93761 | -45.69023 | 2024-10-27 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| caf06a30-4bb3-3779-abd1-427b3ba3b696 | -7.2389 | -46.05315 | 2024-10-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ff90a71-87ed-36b1-b3c6-63d2c04a26c7 | -7.23242 | -46.05204 | 2024-10-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f00b0dbe-4ec3-3313-afc8-55e2d3c6e043 | -7.09373 | -45.29999 | 2024-10-27 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7f78c0c-2247-31db-9b4e-ff3f78b394d0 | -6.88091 | -45.8886 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a376702-f0f8-3ead-94ce-0795d941e347 | -6.88055 | -45.88669 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8318842d-d3ee-3192-abf6-c46beef3f3b4 | -6.87447 | -45.88746 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 267d66d1-36d3-3dcd-9ada-e1de4d0da842 | -6.87411 | -45.88555 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b18f91b1-a16c-3555-b2fe-72da524cb29d | -6.86369 | -45.87408 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 97a5688c-25b8-37d4-a875-9aa6d8223010 | -6.86327 | -45.87208 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6705c6e1-7f7f-3322-a06c-2e3dd20da69e | -6.86232 | -45.87726 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 112fd65f-3aa9-3c48-a2e7-3abd5c0e45ef | -6.85002 | -45.87599 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 952a0cbb-8f7e-3582-99fd-ef1630702fc0 | -6.84959 | -45.87418 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43e52e71-a7de-375e-99ef-03b99dd9ca4f | -6.84451 | -45.87001 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4fdae0b-7020-33a7-b8fd-d7e58beff9d5 | -6.84313 | -45.87312 | 2024-10-27 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92eed538-cf34-3563-9826-65fc7e53184e | -14.08731 | -47.20901 | 2024-10-27 03:38:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60bf241f-8080-3ca1-8ec1-2bfad44cdfbe | -17.53149 | -39.46903 | 2024-10-27 03:40:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c7ad5b6-337c-3018-b8cf-175301e2e876 | -17.52788 | -39.4684 | 2024-10-27 03:40:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fb4b1cb3-4d23-301a-97a9-180e762e81cc | -16.28863 | -40.10651 | 2024-10-27 03:40:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 925c1c63-bdb1-303c-92ce-a032612da9f7 | -16.28784 | -40.11105 | 2024-10-27 03:40:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1b866506-d137-309d-92ff-258cbae44a35 | -16.28778 | -40.10854 | 2024-10-27 03:40:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| aeef67bd-dac0-39e7-aa0a-ffe3805a0bb6 | -17.15377 | -41.082 | 2024-10-27 03:40:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b7dac118-5262-3dd4-8f8c-08e96297dfa8 | -15.26577 | -43.06674 | 2024-10-27 03:40:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1523d802-d409-3ab4-972d-f2b0928397c6 | -15.20087 | -43.53288 | 2024-10-27 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bcc9709b-e062-398d-9880-41d3f9b070f9 | -15.20069 | -43.53669 | 2024-10-27 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 932dd2ab-afc4-3983-99f5-289ed423dd05 | -15.55288 | -49.77193 | 2024-10-27 03:40:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d47359a4-1037-3c2a-ae03-b3c2f08444a7 | -19.17996 | -51.44768 | 2024-10-27 03:40:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 892c4c98-edb7-372a-add8-fc531c34da57 | -29.66088 | -53.83474 | 2024-10-27 03:45:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dc66e07a-11f3-3b6d-8157-57fe2292101e | -0.9815 | -53.7192 | 2024-10-27 03:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2c4b192b-99bf-3cfe-b362-73a87fb38f93 | -0.9815 | -53.699 | 2024-10-27 03:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 38ea8234-09fd-3fff-a13a-d7a38aff4d51 | -0.9998 | -53.719 | 2024-10-27 03:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2f579745-5d3f-3b19-a2e0-29728a5e6769 | -0.9998 | -53.6989 | 2024-10-27 03:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 478a2b0a-0097-3e1a-9acb-4e34cf64d00e | -2.6321 | -54.2975 | 2024-10-27 03:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f8f4281c-043e-3b53-8946-2d38e880c06f | -2.7033 | -49.33 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b000df68-e25d-3d6d-842e-0d0d2c59ec45 | -2.7034 | -49.3088 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| d2ad3982-4648-3b26-818e-eef50f51297a | -2.8144 | -49.2631 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 30e583fa-0683-3552-a4c5-96e94efa3896 | -2.8145 | -49.2418 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b6da9588-9cef-3527-8e2b-506da4d749f3 | -2.8329 | -49.2626 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| ef8716f2-8241-3a65-9aa7-128fd56f3d03 | -2.833 | -49.2413 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| e0a92c3c-9763-30ff-afea-3803e1a9fe50 | -2.8514 | -49.262 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 1425570f-dbce-3419-b1f1-7c75458e26d6 | -2.8515 | -49.2408 | 2024-10-27 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| b3be690d-f552-377f-b013-cb4db6d8a006 | -2.9161 | -51.751 | 2024-10-27 03:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 3e2d5415-7535-3bf8-b575-7dd44f6663ab | -2.9215 | -50.274 | 2024-10-27 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 0564bc75-1b3a-3294-8c82-f08fe1b9bc89 | -2.9345 | -51.7711 | 2024-10-27 03:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8125be5d-2fbb-343d-8393-5ef1a04797f5 | -2.9345 | -51.7505 | 2024-10-27 03:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 314bc72d-766c-388b-bb35-8ca807836363 | -0.9815 | -53.7192 | 2024-10-27 03:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| bd58eb26-6c93-3e00-a776-d35b682e9377 | -0.9815 | -53.699 | 2024-10-27 03:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 807022a8-2659-3e25-bf5d-9ab314560abd | -0.9815 | -53.6789 | 2024-10-27 03:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| c8ea49d0-71bc-3538-890f-0539f642c185 | -0.9998 | -53.719 | 2024-10-27 03:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| ad2728a9-1865-357d-b581-adacb491bc23 | -0.9998 | -53.6989 | 2024-10-27 03:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 22fa767a-e6d7-313e-acc5-b5bc234e5598 | -2.6321 | -54.2975 | 2024-10-27 03:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c9ac0d2f-b474-3107-bc3b-6f74c2bbb4cb | -2.7033 | -49.33 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 26e3662d-377c-3fa5-8168-d225d1c8f412 | -2.7034 | -49.3088 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e503861c-c961-3ccf-a4b2-47ca908b22de | -2.8329 | -49.2626 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 8816b3de-2c6b-36e7-8476-053affb151c0 | -2.833 | -49.2413 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 59d02750-7d35-3b6f-8dbb-d3c7d4498a0e | -2.8514 | -49.262 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d35ba6da-7859-300f-9d2d-30ae1caf0a4f | -2.8515 | -49.2408 | 2024-10-27 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fe59fc3e-6071-347b-b1eb-a02b7e1befaf | -2.916 | -51.7716 | 2024-10-27 03:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 832cf079-04ed-3731-be04-67364754c60b | -2.9161 | -51.751 | 2024-10-27 03:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 60f8e5ae-85b1-3194-8731-2db98fd42d20 | -2.9215 | -50.274 | 2024-10-27 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ca6c6bbc-4e0e-3529-b13f-0841482f5802 | -2.9345 | -51.7711 | 2024-10-27 03:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 26372494-e13b-3608-b611-24cc1dbedaac | -2.9345 | -51.7505 | 2024-10-27 03:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0124c26e-493b-373a-a097-f7db8e189183 | -2.95102 | -40.01211 | 2024-10-27 03:57:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
