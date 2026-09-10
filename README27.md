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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14f3b0dd-f244-333b-9fdb-8903d3708fda | -10.90857 | -47.84586 | 2026-09-10 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd0343f1-e5f2-38b3-be37-f0563c203849 | -11.47976 | -49.69229 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bda9fa2-0ad5-34e0-b35c-275f60d5547b | -12.85741 | -44.33757 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 84803e52-9137-36ec-8f38-36b149419c2a | -10.75538 | -45.94753 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c13bfa2-b17c-3483-aa18-d4942eabf7e5 | -10.75484 | -45.92951 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 587eae40-2945-3299-a041-b28585121ac2 | -10.91138 | -47.85019 | 2026-09-10 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e3e481a-3c1a-329e-80f4-b47b89139671 | -11.48278 | -42.24113 | 2026-09-10 04:27:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3c98691c-e094-35fb-8eaf-2262463791fe | -15.71898 | -42.24535 | 2026-09-10 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40bec8a6-cc92-3450-9f84-1309f0d07bfd | -10.66578 | -46.06179 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 650ca9c8-45d9-355c-94df-9207389c1084 | -10.66913 | -46.01927 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc61b232-26a5-3d32-9e4c-4a63b924cfad | -10.22653 | -45.25239 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d954bc-79c2-327f-b921-c4cb3dc39479 | -16.35435 | -45.06292 | 2026-09-10 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 280dbfcb-df76-3234-8d30-ac59c6eb76c7 | -10.54755 | -47.11467 | 2026-09-10 04:27:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 837e1a77-e931-3c00-b2a5-ab3e8e18bbb3 | -12.82822 | -44.34468 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9a27bfbc-6c0e-382d-8916-28537a3072d1 | -12.82993 | -44.33327 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3433989-87ca-35df-a1bb-b710f864af43 | -12.84309 | -44.33923 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 3e66539c-e2b4-3fdf-b1f9-a37f6410749e | -12.74485 | -48.37115 | 2026-09-10 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00b403b3-e333-392b-9deb-37476df25f8b | -10.73444 | -45.90827 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba213527-3602-3f5c-b8c1-84892b93ff8b | -11.87656 | -44.85194 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8489e4c-73d4-39f3-850d-7dbed7181ba0 | -10.43466 | -48.80929 | 2026-09-10 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f615c992-7474-3d1a-b625-a915387c29dd | -11.33712 | -45.74698 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b88f6f42-0a6b-38d8-a15f-87e7064d73f0 | -10.04977 | -44.88464 | 2026-09-10 04:27:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ffecf3f-894b-3951-8672-2358c8b94666 | -12.77282 | -48.68447 | 2026-09-10 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 546d29dc-6557-35f6-9810-31e2aadbd518 | -10.7675 | -45.9566 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abbbefbf-45ae-3624-baf3-6317a65f40c0 | -12.82879 | -44.34088 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| a7ed8623-2066-37f2-bcb0-83b33edcf5e2 | -10.82691 | -49.44762 | 2026-09-10 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1647b039-9a24-3c2f-b459-3469675d3035 | -10.66911 | -46.04079 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9442c2d7-afdf-33e9-84d0-026b92331735 | -10.22982 | -45.20973 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8858fbd-4442-3884-8369-bf379a52c68a | -13.4382 | -43.83736 | 2026-09-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8b1358ec-e365-3d2f-9992-22dc2a0b55b2 | -14.91589 | -44.66798 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bea7969-eee5-3caf-abde-68bb92b757c0 | -14.11965 | -44.0139 | 2026-09-10 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb46898a-a215-3ba8-a4e2-71d6ba2252d0 | -9.88589 | -47.59812 | 2026-09-10 04:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dfb4b0a-9812-3aa9-9c74-baec00656799 | -12.84996 | -44.34031 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5e7a34c8-f8c2-325f-b21d-dafc55c14cf7 | -10.27493 | -45.22405 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 089c0bde-2be4-368b-be89-41285ec52a39 | -10.22927 | -45.1916 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa1af85a-d24c-35bb-b320-1e10cd6c640b | -12.84252 | -44.34304 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6b2fbaab-d930-37cd-b7a7-5a6126cd1cd4 | -8.0848 | -54.85982 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d7168f02-8d34-32a0-b250-8ea611dfe3b3 | -10.26826 | -45.20134 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aa61aba-807b-3251-8a11-51df10189548 | -10.81264 | -49.28843 | 2026-09-10 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e5b9b4-8455-314a-b90c-bed4202686bb | -10.66856 | -46.04429 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ce7ba30c-3296-39ab-9336-ced8a0abfeed | -10.1135 | -48.81216 | 2026-09-10 04:27:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c3a30d-4238-34a7-b862-ab923613acdf | -11.21691 | -49.93888 | 2026-09-10 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b693b3b1-9709-33c8-b88d-faeffe83775c | -12.86163 | -44.61218 | 2026-09-10 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48a43f86-f2a1-363b-9db9-4bb9d8ce6c7c | -13.43761 | -43.84138 | 2026-09-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 838c4673-d278-3536-8397-be29facd0876 | -12.76588 | -48.6833 | 2026-09-10 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43fd3f08-bb95-365b-8915-9c0205526617 | -10.55212 | -46.09356 | 2026-09-10 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a37500ad-89f5-3d63-9025-9773bb2e5e67 | -10.74822 | -45.92844 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba8746db-938a-355f-b64a-2619e815868b | -10.0654 | -45.47749 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7622948-bf12-34bf-ba5d-bf9fde20b126 | -12.82936 | -44.33708 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 8b2effb5-b0a0-301b-a3df-498a8204e0f2 | -10.73553 | -45.92279 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62a94678-7d1e-3292-9db4-171b83c6c4b2 | -11.848 | -44.85862 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1561ff-88c3-3ee8-be51-3c55095c6a9e | -10.55819 | -46.09814 | 2026-09-10 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8843f74-6bf2-3945-b53e-a269fd43e90f | -14.91475 | -44.67577 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dbccb97-f4a7-336a-8efb-fe4019077cce | -11.21238 | -49.94283 | 2026-09-10 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f90699ba-43dc-32bc-a480-f75b6b158692 | -10.42408 | -45.11749 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78d7c587-571c-3519-b9b0-492c73cabd94 | -12.82536 | -44.34034 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 940649d4-1a17-3351-ae00-8a96740b9947 | -8.08549 | -54.85612 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c33a04f8-5616-354a-9bf9-e93be7ef8c02 | -10.23483 | -45.3077 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97129ecc-d61e-31ef-b5f0-18d975a9bb75 | -11.19114 | -42.79075 | 2026-09-10 04:27:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9413f724-2b90-3716-a573-72621a14118f | -10.73884 | -45.92333 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| baac5d59-7a38-3ed1-9925-7c6361c65329 | -9.60045 | -46.74899 | 2026-09-10 04:27:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e2471f3-79d0-337e-9f8b-ec56573273e8 | -13.5376 | -43.30604 | 2026-09-10 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b36c7d2-bab5-3a9b-aa62-639e2010593b | -11.33436 | -45.78609 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e56bd4f7-315b-3955-a297-080e6b6c20a2 | -14.9113 | -44.67522 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 677d0472-39e1-3252-b5ed-a69e34df2492 | -16.39615 | -43.21116 | 2026-09-10 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 942badcf-19ea-3752-a7ac-dbc0dd9c84a8 | -10.7719 | -45.97166 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad995fd9-a830-3397-aebf-13b6636f0c02 | -10.06374 | -45.4665 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eca45c32-90a2-3b8a-9232-ffb08df1b966 | -10.9126 | -47.8427 | 2026-09-10 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c05de224-80cd-3728-9a2e-3a5261c4f388 | -14.13081 | -44.01149 | 2026-09-10 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d08a7db3-96d4-3489-868f-02895cf9c325 | -12.64529 | -47.08919 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f65e451-0f25-3bd5-aa7a-d379ab93f5e1 | -10.27103 | -45.2054 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3512c877-95a6-3c26-8d5c-5cb397ca126e | -10.23259 | -45.19212 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35c50a0a-db22-3109-93f0-3db9c3119371 | -10.12899 | -45.72065 | 2026-09-10 04:27:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6afb8e5f-365c-344a-bc17-8079df196db7 | -10.55268 | -46.09006 | 2026-09-10 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 054be3d3-cb17-30ea-8e5f-6275dd07835c | -10.43824 | -48.80992 | 2026-09-10 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a4dae71-258e-37f6-a192-8ed3c9dd16ff | -12.82479 | -44.34415 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e06a942-0016-3fff-8938-5c7b54fa872e | -10.74096 | -48.1829 | 2026-09-10 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3de8b934-bf49-3c52-9ab2-e5ecd6f51afd | -10.67302 | -45.99479 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b7026afb-2093-34b3-af1a-5e8ec5510112 | -14.90784 | -44.67469 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ec17390-35ca-3664-b927-f899473f8a1b | -10.54696 | -47.11829 | 2026-09-10 04:27:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b02a552-28c2-37e9-b8c6-869a29cff013 | -11.86594 | -44.87637 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cd5c0a2-81be-3d42-90a4-86d07c0a754d | -10.0665 | -45.4705 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20f11a01-cc8c-3f54-bd36-27b97e1fbc31 | -10.07865 | -45.47958 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d97511f-51a4-3522-bbb4-1584682e7e27 | -16.61596 | -43.32 | 2026-09-10 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbba6b68-1d35-3749-aa7d-548a1d0d9798 | -10.07479 | -45.48256 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f5e21af-2e3f-3f3d-9bd2-73962a095b57 | -11.21613 | -49.94349 | 2026-09-10 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d30907a-c692-3b56-823a-2a6b32e29275 | -10.23591 | -45.21429 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b9c35c4-9dda-38f8-bc52-43e250f2e36c | -12.84595 | -44.34358 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 55395fff-9af5-38c9-8b41-630754e1d3e2 | -12.64795 | -42.29672 | 2026-09-10 04:27:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52b3caa2-fc75-3e06-8117-04e589bf4793 | -12.76935 | -48.68388 | 2026-09-10 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 302d4b1d-5978-35e2-b917-2e568f8f0ee5 | -10.42895 | -42.74531 | 2026-09-10 04:27:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a9a33af2-1e1e-375e-86d3-b874e9faaf5c | -10.07148 | -45.48203 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ca5fb20-4959-330a-85ae-9cf51580a1e5 | -12.83279 | -44.33762 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 60200a03-91b3-32fb-a5c8-3d877e5bc76c | -15.0862 | -43.11686 | 2026-09-10 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 13.9 |
| e3026c02-84e4-339a-8470-98c0ed724002 | -12.84195 | -44.34685 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a231479d-0ebb-34f4-81cc-19d72c1fb940 | -8.08008 | -54.85492 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cf9830fd-43e8-3824-9191-f3c50042b37e | -11.85641 | -44.87114 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab8ba068-4342-332a-9df6-62cdb6c749e9 | -10.40299 | -49.44916 | 2026-09-10 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79836f7a-b052-3d3f-9eb3-35d9e47fb8a6 | -12.83966 | -44.3387 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ae0893c3-e2b3-37cb-9773-1b0acedc17a2 | -11.87712 | -44.84829 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README28.md)
