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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f499b05d-c59d-37f9-9aba-a8e26d613fbd | -13.44333 | -44.41209 | 2024-10-30 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f3ae244-9d9d-36b3-8fc9-4d3571cba7da | -13.32408 | -44.1776 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c5b0ad-42d3-3ba2-b218-89ff15ab4c1e | -13.25775 | -43.6787 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5107206e-70fc-33ab-bfdd-3de166beb62e | -12.8868 | -44.61642 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c26de8df-7471-3ba7-be42-a38ab1e02702 | -12.88287 | -44.61957 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f4076de-6ef3-34cc-ad9c-7c9ac0e28d71 | -12.88231 | -44.62326 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0c43d8e-feea-3953-8a4b-f56512654836 | -12.88005 | -44.61536 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1c5eac4-2dd7-3492-a6b9-c51335582000 | -12.8795 | -44.61905 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eff10efc-4675-3f6a-8b38-0e0108ece00d | -12.87894 | -44.62274 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12159c9e-8091-3a1d-b18f-25bc2a8b2178 | -12.87668 | -44.61484 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 461f2519-8e55-3fce-a5ec-01bb5bce3b35 | -12.87613 | -44.61853 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02d4d18d-06f4-3c92-b163-82c3f2dbb6cb | -12.87331 | -44.61432 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb6891a3-6b1e-3c1e-b538-134804e54790 | -12.87276 | -44.61801 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a943ca3-6956-314f-8890-34b5512ad77e | -12.86994 | -44.6138 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c57e7c66-2137-33d1-96cb-a6eb56089e63 | -12.86938 | -44.61749 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47703dd4-d9b5-384a-9f27-3d11ebab2056 | -12.86381 | -44.63162 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3287b7a5-75c5-3093-980b-c0750b430ecf | -8.73591 | -44.46968 | 2024-10-30 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f442fb51-2f36-3d53-8a45-17a619c9be85 | -9.415 | -44.49746 | 2024-10-30 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38d22eea-147a-30b1-920f-cb4c48444927 | -9.16542 | -45.35763 | 2024-10-30 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97774dd3-6349-32cf-8a82-6383378ab94f | -8.89952 | -44.22474 | 2024-10-30 04:21:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e3193807-6ebe-3297-bd36-3faf8af89036 | -8.84735 | -44.38659 | 2024-10-30 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| deb7bb2e-d40a-33f5-93f8-d35de60945b8 | -8.55001 | -44.63676 | 2024-10-30 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8dd386e-3c0c-3e7b-b224-a20d1cc066ce | -10.77353 | -44.88148 | 2024-10-30 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64e2725b-d1e8-3b9b-bfd7-e5f854cf4427 | -10.71599 | -44.92314 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b28be70f-05c5-346e-a344-9f9e8908bfbe | -10.71545 | -44.92667 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bbcf24e3-6384-39ed-8fc6-20df19197b2c | -10.71268 | -44.92261 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 73820cd6-ef02-3314-b432-ea87d202bc76 | -10.71213 | -44.92614 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 90661971-48bc-357b-9953-beae90ee8938 | -10.64075 | -44.88234 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4ebdab5-b44f-31bb-a576-ea37ad7299eb | -10.63743 | -44.88181 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2db444c-cb43-3c06-815f-6102fe2b4b05 | -10.61164 | -44.93852 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81756d8a-3c73-3b45-9648-b0130ee8509b | -10.6111 | -44.94203 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79a5c262-d9d1-367d-b666-8fad0a9d1bf7 | -10.61055 | -44.94554 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3d11534-d162-3346-b1a8-3e588ffa5e15 | -10.60833 | -44.93799 | 2024-10-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0f39a0d-a359-3515-9a90-627c96ef8cb7 | -10.51214 | -44.90113 | 2024-10-30 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 642f462c-e7e3-3f95-884a-009224ac2cff | -10.50808 | -44.90431 | 2024-10-30 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e342748-068e-3609-afb6-14e251386cc0 | -10.49667 | -45.11082 | 2024-10-30 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96dc2836-d159-3412-b7c5-a1c02d77f6a8 | -10.49391 | -45.10679 | 2024-10-30 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7b256b2-6fb3-3321-a2fd-c0bae6d9a092 | -10.91451 | -44.64943 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9db3836-e67a-336a-896b-5f5e9051bc72 | -10.87767 | -44.53777 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30eba75a-5b47-37c4-ba0c-c3f7ceb5e0c1 | -10.87433 | -44.53724 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44250e4d-e230-3ae0-9b94-2bcc6053f60c | -10.87378 | -44.54081 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e5cf7df-cf36-3d23-b4b4-3d79fd246511 | -10.83569 | -44.69927 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5702f163-7ab2-3529-81a8-7ec0f085e8a3 | -10.77224 | -44.6237 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0b12dfe-11df-3d66-9ab2-12af4a720c87 | -10.60773 | -44.63399 | 2024-10-30 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89e48e4a-e10c-3655-bd01-2b721e9d839f | -10.6044 | -44.63346 | 2024-10-30 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff8a2fa-13b2-3741-aa11-b6ca8aaa8269 | -10.48859 | -44.59007 | 2024-10-30 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80a0489f-9340-3e48-9c8f-2bf1227a1e8d | -10.48472 | -44.59309 | 2024-10-30 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d1a2748-0e2a-36f9-b2d8-630fa84722c7 | -9.90026 | -44.76819 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5778a9a5-1bee-3f0c-823f-9b38daefb704 | -9.88219 | -44.4222 | 2024-10-30 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5d0a7ad-7e66-38db-ba3c-46e4939c76cf | -9.86027 | -44.78363 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e00bcdf-e8d8-39df-a490-26e384655524 | -9.46603 | -44.91435 | 2024-10-30 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f0fc785-3a22-34f9-beb8-96fe364130e9 | -11.66512 | -44.96429 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c8ab0c9-aa64-3cac-88b1-d2629c95b080 | -11.41944 | -44.94768 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2110fe9d-9516-35d7-a6a6-ef2c625b61ea | -11.38611 | -45.14164 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6344fa1-6394-3a7d-8226-61c7e54cd8fe | -11.38502 | -45.14867 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0718e98a-8fa5-3a7a-ab79-104ff0539d55 | -11.38448 | -45.15219 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65c69218-2218-3024-86b5-e74712c084d8 | -11.26926 | -45.08346 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75128d84-f8b4-37df-b9b7-ed90cecbd0ff | -11.10738 | -45.18358 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0033d369-a7bc-3e47-827e-29f13f6f8d5f | -11.10407 | -45.18305 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebecc0d7-3768-3ff9-99a9-c5d24046a7cc | -11.0597 | -45.35913 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f504ee11-3ab4-3760-ae26-7d70033920cc | -11.0586 | -45.36614 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f08598f0-d647-3fc0-b1b6-1797f82de6cc | -11.05806 | -45.36964 | 2024-10-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78cabe4b-cb91-3b7a-84a0-720fcd64de38 | -12.90075 | -45.06102 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59321525-5825-3fd1-8e7a-110346e251ba | -12.89796 | -45.05688 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 478b4882-4974-3c64-b5cf-af5aef6689f8 | -12.89741 | -45.06048 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d7a72ee-3303-34b4-a38b-864e2676dac0 | -12.89686 | -45.06408 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0d00d0e-ac66-3c7a-b4d0-a15bc504f59e | -12.89462 | -45.05635 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d129d34-c954-3167-8dcb-a43e39c7dd3a | -12.89353 | -45.06355 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b8f65ad-5af5-336b-96d6-e46e7c573051 | -12.89128 | -45.05582 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10e5eba9-bcfc-36ef-b54a-798f8bcf30dd | -14.16927 | -46.26854 | 2024-10-30 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dffb1087-5427-3068-bd65-28505681ba86 | -14.16872 | -46.27208 | 2024-10-30 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e27f47ce-0342-36e9-bcf6-c6cc7e7cf116 | -7.85441 | -45.42777 | 2024-10-30 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d37612c-5c18-30dd-b30d-201d1c35cbff | -7.81571 | -46.61092 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b552758-f957-33fd-9cf7-08f1027d6b15 | -7.63097 | -46.21046 | 2024-10-30 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 297ac854-0b20-34e3-b8b5-e70ac860e87f | -7.58052 | -46.43859 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9766f776-b547-3202-af5c-ed262f0b818c | -7.57657 | -46.44167 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23956e59-c283-3ab3-8231-0fca66a0856e | -7.57261 | -46.44475 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7ed8972-07fe-3e1a-a61a-2e52d1618752 | -7.9566 | -45.70531 | 2024-10-30 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e27d0a8-491c-3a40-b061-159200b13df6 | -8.3467 | -46.60977 | 2024-10-30 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45c760fd-3556-34fd-9b93-52af1e1928ba | -8.28906 | -46.79506 | 2024-10-30 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbab818e-44f4-3f83-9a0f-0a7f8ec2989c | -8.28627 | -46.79082 | 2024-10-30 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3904a4ea-97ca-3f31-9fa0-c8e5045cc5e2 | -8.28568 | -46.7945 | 2024-10-30 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbb4f056-cfa0-30c3-a390-ca85d2435946 | -7.88225 | -46.8972 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e6ff739-2499-3e8d-8a17-0564c11898e5 | -7.88166 | -46.90093 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ea05b6c-76e1-338a-96c1-434b2e504f31 | -7.88106 | -46.90466 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f05052c-9f90-310a-9ca8-8f3122cee5bc | -7.88046 | -46.90836 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4839071c-a4bd-376b-9f77-940811a00ce1 | -7.87483 | -46.89985 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40aad0d6-5c52-3fa2-8317-59fb70d931ca | -7.87423 | -46.90357 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8a7aa4-b852-390d-a450-fb623ae3cbc0 | -7.87363 | -46.90728 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f840ad4-37f7-3f59-a276-cfc49998f8ab | -7.87303 | -46.91099 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4aec2ba9-9696-3cc2-aaa5-d347aac25c5f | -7.87141 | -46.89931 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248ac591-82ca-3efd-8a07-f17c446eec84 | -7.87081 | -46.90303 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16214b96-96f2-32b6-9c22-16a8634ac35a | -7.87021 | -46.90674 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e34074b7-143b-391a-a0de-2b7cb6abd8a7 | -7.86859 | -46.89504 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02d0d00d-eee8-3703-963d-23fbfb9a3eb4 | -7.86799 | -46.89876 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f73fac-69e3-330f-9d28-fc50d917e623 | -7.86739 | -46.90248 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5887cf3-cc53-3a2c-86be-19f0bff660f3 | -7.8668 | -46.9062 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08f1a0ed-bc97-3cf6-8e54-803a93117b87 | -7.86518 | -46.8945 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b097dfec-0a7d-3795-b762-86114c9fd180 | -7.86458 | -46.89822 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e39e2374-5373-3fa7-966e-451bc37a9fa0 | -7.86398 | -46.90194 | 2024-10-30 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README50.md)
