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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6a059eb-48ab-34c1-89ce-2e5574f9dcae | -20.37683 | -43.95167 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 89c6b5ac-de4d-3877-ac18-880e80c47689 | -20.37605 | -43.95583 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 456c9314-018c-3b81-ba86-4de761f05db2 | -20.37526 | -43.96006 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| de54bf8e-d219-3ecd-95ae-6f4cc2d2c85d | -20.3745 | -43.96413 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1c205f5a-eb0b-3e2c-acfa-9032c3b082ec | -20.37444 | -43.94187 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 079ee6d8-84c4-300a-8d23-9562f9ea7e4f | -20.3713 | -43.93612 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b9146fcf-3fd0-38fb-aa6a-ccbe236ed6f2 | -20.37047 | -43.94053 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3219b848-ace9-3784-8ff2-5be863e19a6e | -20.36874 | -43.94978 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 504d119b-8441-3ca9-8a44-7f60b3eab8c4 | -20.35765 | -43.94142 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1f063600-0d9a-386d-a643-729fc3489743 | -20.22706 | -44.44445 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 55600fc9-af1e-3ea8-9563-b9a78e736b39 | -20.21938 | -44.43904 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef84c00f-7fca-3f23-a1ce-16010fffaef0 | -20.12451 | -43.864 | 2024-10-08 03:45:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13f6a3d5-abe6-35b7-b0e6-39368e480128 | -19.83051 | -43.79845 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5e326741-0f63-335c-8021-ddb4dd3a423b | -19.78423 | -44.29587 | 2024-10-08 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 961b5637-f97f-34ef-93b2-ed0345e452f7 | -19.74204 | -44.28733 | 2024-10-08 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56ab2787-1d85-32b6-b4b0-186e9aa0e125 | -19.82085 | -43.84973 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a3247e5-07b3-394a-94d1-0c6e01b92598 | -19.82009 | -43.85376 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f532e9-49b2-354c-8601-0a9021f74fb4 | -20.15909 | -44.79285 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7194e793-b21d-393f-8484-b4392a953b41 | -19.82567 | -43.80177 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33b76ea1-46d1-3f14-9f8a-702b632f9d1c | -19.81752 | -43.84493 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20ac5903-cef6-32aa-abf0-cdb6b908a361 | -20.37277 | -43.9508 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2cff8151-dd98-33ad-82c1-c67cda47ce6e | -20.37202 | -43.93227 | 2024-10-08 03:45:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a4649ec0-64fa-32f9-9200-2aa86845d6a5 | -20.37198 | -43.95502 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f7016908-69de-3702-b766-a12a3c4349b3 | -20.36956 | -43.94541 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fe11788-01ad-3948-b67c-4d6399baa61a | -20.36796 | -43.95398 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43f0f842-0241-3577-80ee-c272afd40eb5 | -20.13679 | -43.86596 | 2024-10-08 03:45:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fa525ef1-294b-367c-93e4-2af3801227b6 | -20.13194 | -43.86929 | 2024-10-08 03:45:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7bba92c-dfb7-3e40-8752-65308df0c7d7 | -20.12932 | -43.86086 | 2024-10-08 03:45:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| be73bafd-819d-32c6-8862-8e307e7278ce | -20.12857 | -43.86484 | 2024-10-08 03:45:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f987e6e4-de39-3cdf-87d6-5dcbd4841ee1 | -20.36395 | -43.95283 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b540275d-abf6-3718-88ed-6a8ad024b0d9 | -20.36316 | -43.95705 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a74092f3-1c3f-3372-af65-effc0c5d3c84 | -20.36162 | -43.94275 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f546abb1-88fc-30e6-8870-bc59f961430f | -20.35849 | -43.9369 | 2024-10-08 03:45:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 099a9518-0330-34ce-9c66-8c798afe5789 | -20.22359 | -44.43982 | 2024-10-08 03:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aa35becb-8676-3c5f-93f3-1390c15b2573 | -19.82159 | -43.84578 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90395e9f-0383-3129-8b50-8549a3e4e098 | -19.74623 | -44.28823 | 2024-10-08 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3864f82-dacf-3ffc-b2fc-a93b2ea69a50 | -19.90782 | -44.10307 | 2024-10-08 03:45:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 358a7165-f0fb-37c3-b6c0-484639321927 | -19.92976 | -44.00919 | 2024-10-08 03:45:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef097694-318a-3818-875a-eac0fe431505 | -21.95273 | -45.36269 | 2024-10-08 03:45:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba16036c-2352-3ec2-867f-84717cbc9223 | -21.94941 | -45.35671 | 2024-10-08 03:45:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c74da26d-9491-3392-9e4e-a1cf602fd021 | -21.68476 | -43.98105 | 2024-10-08 03:45:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6e1cc85b-63cb-3d93-83f6-a3762026df3d | -21.68078 | -43.98018 | 2024-10-08 03:45:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1845fb6d-8470-37bb-8432-8055095ca674 | -21.67708 | -44.02205 | 2024-10-08 03:45:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8fdc8532-5ae3-3af7-ad07-f39ada989134 | -21.66704 | -44.09779 | 2024-10-08 03:45:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c486be1e-7171-3a7b-a648-2c53d4be1b33 | -21.49423 | -45.31259 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54eddd97-4298-379d-ab3a-19d07ad90632 | -21.12843 | -44.16967 | 2024-10-08 03:45:00 | NOAA-20 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b1164c8-f164-3e42-bea5-44827b7ed492 | -22.59831 | -44.17199 | 2024-10-08 03:45:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e202cfb9-5bc3-35d1-8c6d-c6e23ceafcc6 | -16.34853 | -45.67581 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce5e62a2-fcae-35e0-b17a-d9ceb331fcc2 | -16.35021 | -45.67733 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63fe1643-ff79-35f1-a161-17f9342b9aae | -17.58667 | -44.51025 | 2024-10-08 03:45:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd7fcfdc-9f2a-370c-b32f-8df4565bd004 | -17.58571 | -44.51518 | 2024-10-08 03:45:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e14dde0-f0da-3916-964e-676ff45a4c39 | -19.27083 | -46.13232 | 2024-10-08 03:45:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2cf62d3-0df2-31f1-8a74-8c1f1bd27b41 | -18.21895 | -45.05473 | 2024-10-08 03:45:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73148f24-22e6-36f7-8a44-b4d979abb525 | -20.31907 | -46.26959 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e2b6b12c-ec64-3313-9a6e-f5744aa74bd5 | -20.3144 | -46.26839 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f06aab89-dfe6-37e0-883c-ab7ed92f6388 | -19.66209 | -46.23191 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57512a48-4d5f-3c85-a312-750ac4af4551 | -20.31797 | -46.27499 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e36b8a04-44d1-3784-8ac6-9336e3503157 | -19.86228 | -45.68782 | 2024-10-08 03:45:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cad5fc78-116a-315e-bc18-fbb200b50ad7 | -20.75999 | -46.36855 | 2024-10-08 03:45:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 446cc78f-95e5-3a01-b0a3-8ab2d0c70cbc | -20.75893 | -46.37377 | 2024-10-08 03:45:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8bc2d7-e233-3700-886a-e0529dd4e7d3 | -20.65088 | -45.92182 | 2024-10-08 03:45:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 74a263a9-6a23-371e-a9c6-05a5506d501a | -20.64985 | -45.92699 | 2024-10-08 03:45:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9671fc77-7374-356c-9643-e15f078e1109 | -20.64528 | -45.92603 | 2024-10-08 03:45:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 771d6859-f848-39e6-9b91-8cacee482ce8 | -20.64419 | -45.93148 | 2024-10-08 03:45:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbbec17f-38a9-39c3-ae51-0bd6ac3b828e | -19.86683 | -45.68892 | 2024-10-08 03:45:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c59a1ee-3fc4-34fe-9204-3be38863d582 | -20.3133 | -46.27378 | 2024-10-08 03:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d8974c7-69ed-33ad-bf54-5e86cbe58993 | -19.85872 | -45.68188 | 2024-10-08 03:45:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f993527-7f6e-35c7-b370-d254c9e3ae9e | -19.85772 | -45.6868 | 2024-10-08 03:45:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c9315f-8d73-32e8-a337-4881e20983dd | -19.79003 | -46.50832 | 2024-10-08 03:45:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f538c184-c784-3685-a15f-94f53cfef77b | -21.57845 | -46.85515 | 2024-10-08 03:45:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 046f45b4-9488-37d8-8660-1e30ab46aae1 | -21.57802 | -46.85497 | 2024-10-08 03:45:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9066b5f4-8677-33df-abd8-bcd49d2a40aa | -21.20284 | -45.79489 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4b384295-f003-3d4a-9aa4-a570a7a1a535 | -21.20185 | -45.79982 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 27ffc794-5104-3c52-99eb-c6285fe44bf4 | -21.19839 | -45.79372 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95385750-684f-3a8b-a72e-ab76f4a62240 | -21.1974 | -45.79866 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7289b966-a853-3ab9-898d-375d1725d58d | -21.14938 | -45.82747 | 2024-10-08 03:45:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0fe2dce8-93ae-3538-ae52-9b4565a7d2c6 | -20.9789 | -46.08127 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 26156f35-c114-3501-a709-4e9ffe8b3a33 | -20.97788 | -46.08621 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e192c7b8-dd7f-3477-9ca6-44992360dd3d | -20.97464 | -46.08317 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 976567bc-83d7-3124-be61-9605735bc23e | -20.97326 | -46.08538 | 2024-10-08 03:45:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f01ae920-089a-3560-bd1d-c01e1a775a76 | -22.12231 | -46.04154 | 2024-10-08 03:45:00 | NOAA-20 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e61eb2a-a44d-3adf-af46-cf0baaf7e963 | -21.82141 | -45.67911 | 2024-10-08 03:45:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 11d689fc-daab-32b8-a605-ea27091b3651 | -21.82047 | -45.68377 | 2024-10-08 03:45:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0b36d15d-d400-3f92-864a-2d200145ea02 | -21.81737 | -45.68199 | 2024-10-08 03:45:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 89802198-ccd7-38f1-b1c6-8fa663871bad | -21.81644 | -45.68674 | 2024-10-08 03:45:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84097039-3bb0-3715-bad9-123c2d2564a7 | -21.81607 | -45.68277 | 2024-10-08 03:45:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4f7f66a6-5e96-3ae6-8a60-bf558964375d | -22.40766 | -46.6196 | 2024-10-08 03:45:00 | NOAA-20 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 842b200a-f201-357d-9ee2-afb6333006a9 | -22.58717 | -46.08854 | 2024-10-08 03:45:00 | NOAA-20 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94dd0844-68c0-3364-b2bd-0d0c79aa9396 | -22.49547 | -46.12712 | 2024-10-08 03:45:00 | NOAA-20 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 33a78363-0fd4-37e8-8167-b42907b8b1eb | -22.49406 | -46.12398 | 2024-10-08 03:45:00 | NOAA-20 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ab26830f-6d87-3775-822b-f6d3e9a6755a | -16.18311 | -46.43737 | 2024-10-08 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8dc271b-375b-3faf-87f8-5b948f095810 | -16.18246 | -46.44065 | 2024-10-08 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be2b630d-49c1-3d33-8c93-9a803c0ab38f | -15.7379 | -46.02162 | 2024-10-08 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99806d18-8a5e-314d-a32f-4663bc94b5af | -15.73287 | -46.02045 | 2024-10-08 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9c3563c-ed77-3fd5-8a69-8f82b7ba1b1c | -16.55975 | -46.46093 | 2024-10-08 03:45:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6e4fea5-f829-3b0d-833e-fa122853e9ec | -18.31804 | -47.24821 | 2024-10-08 03:45:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79deb7ff-cb4b-3ddc-80c2-d50d4ce45495 | -18.28809 | -47.15705 | 2024-10-08 03:45:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9696ae8e-5dbf-31d2-a335-506c728e3ebe | -18.2808 | -47.14012 | 2024-10-08 03:45:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d98bc483-56d4-3c1e-ac32-30e448d6417f | -18.2852 | -47.1449 | 2024-10-08 03:45:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8b34809-63ed-3a58-bc3b-a0f3371bb351 | -18.28882 | -47.15349 | 2024-10-08 03:45:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README41.md)
