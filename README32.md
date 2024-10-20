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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3701e76c-70ad-3e38-8d47-aad4371e21e7 | -5.57087 | -44.88253 | 2024-10-20 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9073152-8094-3420-936d-0410ae61e499 | -5.56733 | -44.88194 | 2024-10-20 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e94c6e0-d478-3dc6-88c2-2b84fd215067 | -5.43081 | -44.8092 | 2024-10-20 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb921d0b-27f3-305f-b0a9-544da486b1cf | -7.18504 | -44.9601 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e79c9f44-0fc6-3f0f-816e-92a1af0723c9 | -7.18355 | -44.96141 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffb7822d-ff56-37fc-905b-adaeaa1e2331 | -7.18145 | -44.95954 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a2b042b-b817-312c-9829-ee0334797071 | -7.03654 | -44.28711 | 2024-10-20 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c6a3280-b9c2-37d9-bb96-cceae783722a | -4.97184 | -45.90634 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3987ff47-a77b-38c3-b433-0e59e58de620 | -4.97128 | -45.90992 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2c278ef-e317-3025-9b29-a3d44342b0dc | -4.96845 | -45.90582 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c64b56de-9577-3cf3-80f0-9c16e072a325 | -4.96496 | -45.52247 | 2024-10-20 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bdbca89-2e90-3bd3-94fa-e71e7149f0c1 | -4.91461 | -45.82709 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5274685a-b410-3ac6-b8e4-72d87dfb96d1 | -4.91404 | -45.83079 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e1004b40-39c8-3906-83ab-00a1c223f4e2 | -4.91348 | -45.83443 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3189be0c-9776-3902-80ab-5040f2e57442 | -4.91121 | -45.82655 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ee52fef-f489-329b-85ab-3b5af82bc3b8 | -4.91064 | -45.83025 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3859885b-d2ba-3e75-a9c6-16fc87ebbeab | -4.91009 | -45.83387 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37f5d2ec-94cd-3d3e-b3d0-93bc32aa1867 | -4.90953 | -45.83749 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1980286-8366-319d-8d73-30a61b036c5b | -4.90897 | -45.8411 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cc2f209-530c-3527-bb86-277f3c064720 | -4.90842 | -45.8447 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5038a15d-8a0b-35e7-aef6-d2051e3cf0cc | -4.90839 | -45.82231 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64589dd0-0f3a-33f0-99c9-0493146743c3 | -4.90782 | -45.82601 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 652c1139-df27-3149-9b7f-2f548911d51e | -4.90725 | -45.82969 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7368ec34-88e9-3d44-b3d1-52f12af1c8dc | -4.90669 | -45.83331 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b81e04a-fad2-3f79-9c87-3b49e1cc52c6 | -4.90614 | -45.83693 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8adbeae-342b-3105-bc31-24c654edd66d | -4.90498 | -45.82181 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab70163a-6630-3470-8c41-2a5ba4b224af | -4.90442 | -45.82547 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1cc2279e-77f1-36c0-8eb6-bc8eaaee4002 | -4.90386 | -45.82914 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17451026-c0e1-3ad4-898e-057c3a9fcdd1 | -4.9033 | -45.83276 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a66dd50-de90-39cb-8677-34ca77a8bdc8 | -4.90274 | -45.83638 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7db98c7c-5227-3f47-b07a-3fd2d4caa41c | -4.90158 | -45.82133 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51a273e3-82fe-3aa2-a7d6-49e1c682d43b | -4.90102 | -45.82499 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b3cc8892-17f8-39fa-806b-adcf2bebd0e7 | -4.90046 | -45.82864 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 327671f6-86d2-35c7-8f22-8ae5204647b9 | -4.89817 | -45.82085 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02b2e2b7-62ba-3e96-b3d8-2b76f665b082 | -4.89761 | -45.82451 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c48bef68-846b-3e04-b6bd-20b2d86108ca | -4.89705 | -45.82815 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a68c159b-0596-363b-b8bd-5b8688d4bb80 | -4.8965 | -45.83175 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 012eff67-dca2-372b-9077-455cb73dd130 | -4.89477 | -45.82035 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072fdd95-4811-3ca2-a474-2698da37f9fd | -4.89421 | -45.824 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c129816-12e6-3e99-b633-6892c72ae976 | -4.89366 | -45.82763 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 082d70d3-108b-3a56-9d0d-a8462f3b177f | -4.8931 | -45.83124 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1457f385-a93f-39ae-a71f-4f88e2a12211 | -4.89255 | -45.83484 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c8f94cf-4886-3f58-ad22-52ad85d32a2e | -4.89026 | -45.82709 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e710cb0-e388-34dd-b810-347c2b50e551 | -4.89008 | -45.82769 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d0d7dcf-06bd-3572-b051-6c5b9e576428 | -4.8897 | -45.83072 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c408031e-9387-371f-a17d-f6e16d8240cb | -4.88952 | -45.83132 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a1bf43-5c22-3d8c-967d-38358cbe867d | -4.87781 | -45.03002 | 2024-10-20 04:32:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b487c4be-0f4b-3159-9af5-048f0e9b6ee6 | -4.87024 | -45.03275 | 2024-10-20 04:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39e19f25-7cf3-3970-a564-056a6432fc0f | -4.86973 | -45.86889 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fed1350f-2313-3b3c-a0de-82181e231020 | -4.86917 | -45.87252 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef5b2c00-312b-3576-a9b6-5df92a1226ad | -4.86674 | -45.03225 | 2024-10-20 04:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3cf76b2-2dd9-39a2-9a58-56f623a3dbe9 | -4.86634 | -45.8684 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 516335c2-657d-39ae-9a31-465dcd89a803 | -4.86577 | -45.87201 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62247d9b-00d9-3455-beba-7da2252f04b5 | -4.86294 | -45.8679 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a0c74b4-1715-3fd3-af46-e5a5006b293c | -4.86238 | -45.8715 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13c86792-8120-3b71-b569-4bef01575a46 | -4.86067 | -45.86017 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 228e1d4c-c5c8-32be-b1b7-b5f521c8d55f | -4.80173 | -45.7916 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ce3eca-4af6-3497-8699-3a3ae1e95b62 | -4.80117 | -45.79525 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecb0725e-ce68-384c-b22a-314e6aff97ee | -4.76348 | -46.0845 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca42314-acb6-3e56-b361-eb152cb836b8 | -4.7601 | -46.08399 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f383acb8-20c4-3942-bee7-a6892ccd6265 | -4.75733 | -46.10195 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8ee1a08-c172-343e-9ae1-baf3429700bf | -4.7386 | -45.20898 | 2024-10-20 04:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de583a64-0bcb-3e8d-bfba-e6d8ee9d16ef | -4.73514 | -45.20842 | 2024-10-20 04:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbd1dcc5-dba6-3dd1-8198-a6d9a0e2b5a6 | -4.71604 | -44.86686 | 2024-10-20 04:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6d772c-18cc-3e6b-9fdd-0a68dfd84198 | -4.71549 | -44.86764 | 2024-10-20 04:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7e3687f-a9dd-3e24-8aa9-b7f3a4dab2f3 | -4.71253 | -44.86633 | 2024-10-20 04:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feebb96b-e1a7-39c5-889d-8b0fe1672ce1 | -4.71014 | -45.84043 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 796e6928-c1b9-3d75-b815-2297d6b9ab71 | -4.70958 | -45.84407 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50a252b9-f796-36db-92f8-99c25cdf66bb | -4.70902 | -45.84769 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ac1a60d-caef-36cd-95c4-5f0f3c91a5ff | -4.7081 | -45.9654 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73420b64-4a7f-3035-a585-bda44a57535d | -4.70731 | -45.83627 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebdf3687-04be-3425-a83d-06d8307ede24 | -4.70675 | -45.83989 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05a27a73-0693-3c8d-bfe5-025cad803efa | -4.70642 | -45.63838 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12b6d3a-fa3d-3d3e-a8f0-955d4c7efd38 | -4.70619 | -45.84352 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42b498f2-30a3-30c2-bac2-8c46a3792086 | -4.70563 | -45.84715 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7aac0fc-e37b-3000-80cd-26271fcdf398 | -4.70392 | -45.83574 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0123b47d-d257-3456-ac97-b58063d7a05e | -4.70336 | -45.83935 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3448b562-8f5e-321f-ac04-cc66f426db33 | -4.703 | -45.63788 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 544c8ada-7a1b-3d44-82c2-533d267d0aa8 | -4.7028 | -45.84298 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1e5e51-448e-39b8-949d-8606dc20739b | -4.70224 | -45.8466 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d53a14fe-ee72-3471-a864-eae613fd308f | -4.69997 | -45.83882 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a3dd0f4-4869-3dd0-ac36-213c144f05ea | -4.69941 | -45.84244 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 729a6800-5654-3c1c-b09e-4a5b709043f7 | -4.69885 | -45.84605 | 2024-10-20 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6244cb56-1333-3581-98ab-326eff7083c6 | -4.67193 | -44.91671 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97184c86-a146-32c5-8e27-2e1e9495cc3f | -4.54734 | -45.76396 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4037599-e48f-3cb4-8cb3-1e55d3a1d9de | -4.54395 | -45.76339 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4feee8b2-b8f1-353c-a7bb-33e8e23ac89b | -4.49794 | -44.76042 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b6d246a-b806-36a7-b547-87036296c333 | -4.49734 | -44.76432 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed88abe3-3996-347f-a88f-a099642052cf | -4.49673 | -44.76823 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85407016-f1e6-3986-ad18-7ee48cbecd5c | -4.49564 | -44.75206 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61598235-bbc3-388e-94b8-a2b6b0c99c67 | -4.49503 | -44.75598 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 708f577e-e896-3367-8a39-52387d9b3ac8 | -4.49442 | -44.75988 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d3dd76b-dbec-3b8b-b000-4205a7cbc3f0 | -4.494 | -44.90633 | 2024-10-20 04:32:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2f10851-5247-3767-a94c-78bd9e1c2be9 | -4.49382 | -44.76378 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae2c655-94c7-3d5a-acab-d67cac49edf1 | -4.49366 | -44.90317 | 2024-10-20 04:32:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b03deb-e63a-3500-9727-2a4e2c031a39 | -4.49305 | -44.90704 | 2024-10-20 04:32:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e1eca6c-37bc-3f24-b11c-531fea1ae239 | -4.49212 | -44.75151 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61395652-a523-3f84-b732-65d686937fea | -4.49151 | -44.75543 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4abcb085-da94-3433-93a0-e519874f4691 | -4.4909 | -44.75933 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ae9db36-8ecd-392b-a0af-e9b18f5ece33 | -4.48799 | -44.75488 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README33.md)
