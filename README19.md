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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af9754b7-d281-3c09-a656-b5cf29676487 | -14.16701 | -46.08215 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f54c2b3-abdb-30d1-b4e3-3dfe43d8727c | -11.47202 | -44.99463 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41cbf7c4-5fc8-3afe-831c-6a52f578c706 | -11.43862 | -43.50801 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 324dc417-c27c-3b73-855c-0656beb5eafb | -11.81587 | -44.97532 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caa516bc-4ba1-3b62-8c51-bb1477cffa33 | -9.92245 | -43.68779 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a241068d-99da-3881-a8ee-7bf6562bec5a | -8.53551 | -44.7059 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 841aa6c2-9cbf-3a02-bbb4-14081eb2f9dd | -14.16484 | -46.08428 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b75a6da1-67e1-3a48-8b3e-019eb9c2fe5c | -13.12959 | -47.43062 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8ecd0b7-8bf4-39d0-9468-830fffe9a34f | -11.60084 | -45.03669 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e1a0cf3-4dca-3b01-9a29-945e142bf554 | -13.27851 | -47.2331 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3b6f034-00fe-3cff-a349-de974d4b7034 | -11.98455 | -46.65042 | 2025-10-01 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b325ef-8f09-3dd2-aeac-8ec3a1ca903a | -11.99765 | -46.65323 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 196f0faa-166f-3e9c-84d7-17d9d3aa64f0 | -11.52351 | -43.55964 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37c990ae-4d07-34ea-96a7-abed3c4d12f9 | -11.18295 | -41.01286 | 2025-10-01 03:30:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 250b04b7-af27-3919-bf4d-6aa44954815c | -11.84476 | -44.99218 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7d6bd813-4bdd-3ede-9bc8-5c19c143f2fc | -8.55683 | -44.76927 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0a36790-447d-3404-81c2-4e304f1acb0a | -11.3768 | -45.07942 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 45a12a89-3dd5-3d94-bf62-428d8c5d97a7 | -13.58417 | -48.04277 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89d958c3-fd9b-3718-ad5a-b9b40bd37bda | -13.33342 | -47.33861 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50c7713a-59e7-34c1-93d1-f176a1d95cfa | -13.32576 | -47.84413 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6c9b1cbc-b754-3bac-91e8-cb770f738b71 | -11.42149 | -43.50464 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c745e0a-fa14-38e2-b3d8-92a64bc4c721 | -10.83093 | -45.38466 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcfa2c55-07ad-3033-8053-b228893a3bc9 | -8.53343 | -44.717 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a42fb7e-43e1-3de8-bd6b-84424314c563 | -8.53751 | -44.69516 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e8901ca-0f03-3a4b-b5a4-dd0a2042d4c3 | -12.75973 | -46.91096 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecc09934-4cc0-30e0-8f06-a3f1b5b03d7f | -13.76781 | -47.95577 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 149e08dd-c32e-3bc9-8da1-e09603c706ef | -10.32753 | -42.4627 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 3ca0d8f8-3367-3bc4-bcb5-85d63d0b7db5 | -12.85071 | -47.02165 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc2f97b6-beee-3312-9159-82425c73af02 | -9.93594 | -43.64983 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9676e94-8ba1-396a-8b17-8fe5a9c62231 | -11.98184 | -41.83855 | 2025-10-01 03:30:00 | NOAA-20 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de6503e8-4bf3-3088-97bb-72bf0257548b | -12.87723 | -44.68708 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c8741e3-10dc-3af1-9ea0-5003d1ef35c2 | -11.37782 | -45.0744 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 2f9f99a8-bbf4-33ea-aa64-0365bf45b868 | -13.97951 | -44.91422 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5a3b21d-04ee-3e9d-b35d-0b83ca9fffab | -11.39495 | -44.90488 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52449d97-f61c-3d22-95ea-6e64356a49a9 | -9.93758 | -43.64131 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbff0d28-c5fa-330a-a2fb-aace629d9ef7 | -13.37438 | -47.3222 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc88d3c3-ea67-3f8e-946f-619897287932 | -11.42585 | -43.50569 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8328d66c-c70d-3b63-9afa-64350e81fa8b | -13.76061 | -47.96941 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8def2616-0bd9-36d9-84dd-f68ba5dd971b | -11.60171 | -45.0324 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 787f340c-2bf4-34f8-91b6-3ef9c460c8b6 | -13.32577 | -47.34661 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3db02ec1-a548-33bb-be5e-07a498c55309 | -12.77023 | -46.86441 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27d6c772-7767-348c-b787-52fa6e2cf0f5 | -11.65726 | -45.32069 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 929e9efa-809c-338d-b307-e48875ff9a43 | -10.21535 | -43.04454 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ba6d3ae9-aff5-3e75-bbf0-df124791cc60 | -10.73842 | -45.37811 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b767c58-cf84-32ac-a258-da4d8873a690 | -11.83321 | -44.98537 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c709c159-8c0c-3d64-87c1-905d40d2f692 | -12.82169 | -47.02332 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f6400093-7717-3483-b926-d54e6cf7b2c5 | -11.37886 | -45.06926 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| cdb18ae4-182e-3acd-90aa-177920d8bc88 | -11.83134 | -44.96275 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3610618-3e21-3513-8340-b06a52e84e62 | -11.82001 | -44.98672 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cafa93be-8f18-3a7d-b29c-b7cc363ec1f1 | -13.16022 | -42.3544 | 2025-10-01 03:30:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34bdaf20-70ad-3a53-a34b-d36c4451ce6c | -8.88937 | -45.05666 | 2025-10-01 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 385d47df-84d7-3cd3-8d76-147309302080 | -11.84896 | -45.0034 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14c6cf64-fb6e-3ff5-b0b2-c77e93024a54 | -13.76512 | -47.96821 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1332e21a-dc26-3ada-bef8-1edab5ef309b | -10.82112 | -46.64413 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f520378-3cbc-310f-8fc7-6c1b84f87f17 | -11.84056 | -44.98098 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 023a1e79-56ef-352a-8648-0e01b059a4ee | -13.76205 | -47.96293 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0dba3451-a763-3300-8d30-d6d5e62ed6b0 | -12.948 | -46.42826 | 2025-10-01 03:30:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bb4b7e21-d540-3ad5-a1fc-744c8d459d43 | -11.84998 | -44.99832 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a217a82-10c2-33f3-a315-4b13fa27fab2 | -11.46425 | -45.08183 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 043cad68-42ea-3fa8-b146-717272255c44 | -8.56107 | -44.71232 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87f37f21-50ef-35a5-ad3c-e919886d2e7b | -11.13284 | -43.38432 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 259358a3-8e63-3fca-97f6-f8d9e4403089 | -14.05787 | -44.37433 | 2025-10-01 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1474ae61-cd6f-39f5-b8e5-0f51399cbbed | -12.87837 | -45.2737 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2244ca7-2816-33fa-ae1d-a85d1499f41a | -13.76969 | -47.98145 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e57037db-2f9d-3e98-a828-4b8bedbaa7ea | -9.94018 | -43.65962 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b986d8f-6695-3546-9b29-8918cb754947 | -12.94913 | -46.42288 | 2025-10-01 03:30:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a87ca2ba-cac6-33dc-bea3-eea80c75d110 | -11.52389 | -43.56243 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4728644-dc6c-36ac-a0e5-9cb23e73f0ca | -11.49136 | -43.51121 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c2455d5-41bf-32f2-8858-69bbcf8dc5a6 | -13.32457 | -47.34589 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 765b9d38-778d-35c0-9bee-1eded5b66153 | -11.46525 | -45.07693 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1a93cd0-cfc0-39dc-9ac6-0684b24c0da0 | -11.42661 | -43.50173 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e01a8d91-527b-34e4-a802-8f4b29b3e699 | -14.05928 | -45.03255 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aac8c3f-dfd5-3a12-85e5-c05671f9cacf | -14.18887 | -46.10421 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 565d2f7e-a8e0-3389-9ae4-10d9be85911f | -11.98243 | -41.83551 | 2025-10-01 03:30:00 | NOAA-20 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ae0b423e-21f2-3053-b23e-af49f062af0e | -9.9292 | -43.65292 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 450e927f-56b2-3921-9fda-ce9553392128 | -11.54478 | -45.07121 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5086ff16-8ae0-3b01-a7be-03ead5deaf11 | -9.26549 | -45.68711 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce154716-7a8f-3709-9689-22c12817511a | -11.94532 | -43.91796 | 2025-10-01 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d2aaa0-6c66-3b85-87c5-afb3124fc811 | -12.88041 | -45.26372 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a595bc01-3882-3453-b497-15fa4335f460 | -11.20064 | -47.20295 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b73139ae-b241-3996-9c2e-d3d21ff4ee3f | -13.56122 | -47.28168 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8c09b69-8142-3895-bb4c-3a14def9a180 | -12.82329 | -47.01583 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 48256edf-55f4-3b3f-bc05-c719d0d2dcfc | -11.96081 | -46.591 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19100a31-6580-3c32-9e3a-a349e888670e | -10.83195 | -46.65522 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 896b3034-a4fe-3445-8af1-c5863a5e4d49 | -10.9057 | -46.53872 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 627b76a4-1d7a-3290-b043-af51e3a0336c | -11.84257 | -45.00301 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0f8d3be3-169f-3b41-8b9e-ad3725e4a5d7 | -10.90783 | -46.5319 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9e59377-4510-3e99-9df5-50dfa793ee21 | -9.93507 | -43.6226 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d085b910-c9bc-3492-8949-3288d9a6bc21 | -12.00843 | -46.63528 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa9d7ba-05e2-3927-ba68-f95153d1fff7 | -11.6042 | -45.05222 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 836706bc-c096-3d8f-9ae5-f99ede960aa2 | -11.41936 | -43.50861 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 938a4a15-183c-38ff-8aeb-90c6c7a9d570 | -11.81488 | -44.98018 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96c5d885-9f46-3755-a11a-94d4a0f02147 | -14.1889 | -46.13533 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d0c0bf9-24f3-330f-97ea-e17dab49b03c | -13.31891 | -47.34485 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d93dd85-d972-37a9-a5ee-123fb6608cb9 | -13.66874 | -46.79257 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60b230b8-63dc-3b8a-84df-3ff9f010e96f | -10.90158 | -46.55822 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 69ac3175-82f4-3d38-8cf3-815d3c0c0f10 | -11.83951 | -44.98617 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a61444ca-07cb-3e4c-9f02-fd1ca6adc3a9 | -14.05609 | -45.03928 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc153fa7-c665-3413-a26f-8503576240cd | -13.65498 | -47.31361 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfaaf3f0-1ac6-357a-afda-a195a794a531 | -11.44432 | -43.50917 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README20.md)
