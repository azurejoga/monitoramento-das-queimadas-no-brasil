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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3716208-3ab2-3696-8769-60384ff0570e | -11.08811 | -44.00109 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea37114-50cc-3ec0-86e4-3dd191265e69 | -11.75723 | -44.95198 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e811ed0a-664b-3b0f-bd3a-346577ee3478 | -6.95858 | -45.28766 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 18614993-dff6-3e69-81ee-cb85c074bb50 | -11.83182 | -43.59805 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13fe46c1-520a-309c-8856-4dc0097a9f1e | -11.99099 | -43.4951 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b86d627f-6775-3be7-84d4-5b09a6e8bc21 | -11.27307 | -45.19857 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e4daa0-9fcb-315a-a0e9-f7cd4437f330 | -7.24798 | -48.07178 | 2026-10-09 03:45:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f5413a3-2d28-323c-8337-bb5afceca2bc | -12.0025 | -43.48909 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6dfcf75-17e4-37df-8a4f-9d75df595077 | -11.75796 | -45.48436 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b33e065b-1ff2-34c6-aaf8-c81e5c962a18 | -11.65044 | -43.68927 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1faff9ae-318b-306f-8360-9e3300d5d1ee | -11.45509 | -43.38077 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de540bed-2482-35a1-989a-7e7b94016984 | -11.3125 | -44.84139 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c93f0e3-9282-3681-925f-367d12a83fec | -6.88246 | -45.90125 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 62d1ffa6-fab2-3065-b3e1-856f3334bbb6 | -12.53852 | -46.5268 | 2026-10-09 03:45:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 937c8c5a-fa59-35dd-aad0-12dbf7490099 | -12.00563 | -43.47249 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41f08f50-3462-3287-a28b-c14ba2433bb4 | -11.99401 | -43.47915 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b7eaaf8-38c7-3e59-84cf-f30bc0fa26a1 | -8.91289 | -45.1736 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffcac4f-5f58-3e1c-85b1-f6a886c4eb59 | -8.40534 | -46.94518 | 2026-10-09 03:45:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aad84533-3b3f-30f0-8720-d995f7d12515 | -11.60988 | -43.68005 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8b46f23-6f5c-3d5a-a4fa-d5230cdddb42 | -9.83685 | -44.78841 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d37b0ae-d26a-3d34-ada1-0017f8c35d25 | -11.25917 | -45.17918 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 658c13b0-e7b3-343a-9bdd-0868f4a48323 | -8.73463 | -45.16008 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb572652-e8b6-359c-b6d9-f7aa9de8e5f0 | -10.87583 | -44.80429 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb6842df-f6b1-38fb-8602-9bb2d4c682d8 | -10.8828 | -44.79807 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e02e27e2-e4c0-3174-baf6-ae373de5e386 | -8.96807 | -45.16153 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7eece7e3-4f95-3fc6-b777-33e709dfa741 | -10.87655 | -44.80055 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b841f681-c727-38e8-b5be-b7ef4b26efff | -11.45955 | -43.38468 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 642b7dfc-4a89-3674-b03d-7df79585d09e | -11.29808 | -44.82684 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 973cc371-9007-39ea-9ba6-57ab2710e56d | -12.00837 | -43.4579 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74133c1c-e678-3396-aed8-7385b11c21ce | -11.0774 | -44.08503 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f11d0e3-275f-31bc-a94b-b267b09e2bca | -13.16214 | -43.27777 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 97f1569f-f805-33fc-b8a0-765c228c276d | -14.95346 | -41.43146 | 2026-10-09 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4f17e3d-16dc-3811-9a87-141b09c9b036 | -11.3153 | -44.82677 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 171dacff-b703-3c1c-9733-bd52dd47ebd5 | -11.65222 | -43.67978 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 250a9930-de8f-305f-840d-9ba43176bc27 | -11.3132 | -44.83772 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| c0a292f0-8cae-34d1-a2c9-26593b0e81cb | -8.32395 | -45.45254 | 2026-10-09 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 97555175-d34b-3eef-bae0-21562d73a1ef | -11.07083 | -44.09064 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a237cde-35df-3a94-9a29-016d57a5b360 | -11.08316 | -44.05513 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9aae488-5860-3e02-a9e0-0cbb94461c7b | -8.96545 | -45.1754 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 25681ade-5f3e-3375-918e-36903213e58d | -10.19111 | -36.32225 | 2026-10-09 03:45:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce739a93-7521-3134-a13d-42d8504b7a60 | -11.75654 | -44.95543 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c5039e6-ec66-3689-96e7-e316ad316a98 | -13.7858 | -42.61163 | 2026-10-09 03:45:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f7d1928-871b-3550-8613-7baeebf7db87 | -9.89404 | -44.79594 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ffd1f20-e1ff-39d2-80fa-288d29d391f1 | -8.73955 | -45.13412 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fdf74c61-56b7-340f-903f-7e1bbbffb62b | -7.47303 | -42.84916 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25951041-9f60-385a-b119-e10820e7ede9 | -12.37004 | -39.47774 | 2026-10-09 03:45:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c85cc84-e8d7-3368-8856-fd6a8e975347 | -6.95863 | -45.28612 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| dbc409d9-b6e2-3759-bdfb-ae8e930dd69c | -12.01189 | -43.49432 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d36d22d9-01fe-3eff-917e-84b230f99a97 | -11.99245 | -43.48741 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e81d934f-e8a8-35bb-9208-0cf1e89e9552 | -13.38269 | -41.33213 | 2026-10-09 03:45:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52e0c08d-bf3e-3439-8049-e70d6feae2a3 | -14.25734 | -43.66757 | 2026-10-09 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf4c5ec-1221-3aca-a9e1-b599b6eb2f97 | -11.6174 | -43.72409 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf76982f-cb7e-32f3-ace9-d8590aadbfb5 | -11.64184 | -43.70694 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef078707-521d-3a7a-93a3-643c31363a32 | -8.97066 | -45.91437 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36823248-e9b3-3ec3-af50-38e30d48dcf5 | -11.0595 | -44.06417 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d447561-36fa-3b3c-bdff-33b5ece3d9e4 | -11.7856 | -45.59015 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2bf5352-1872-3c48-87f9-59fbdbdc7561 | -8.90527 | -45.23455 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7a03e36-4365-3be7-9091-275dd887e26c | -8.96388 | -45.1515 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efcca97a-25ca-3176-93d1-373f0fc4ef96 | -8.4119 | -46.9467 | 2026-10-09 03:45:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b67e705a-226c-3251-b682-65751a03ee3b | -11.28384 | -45.2037 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e4f4602-3e4c-3643-882a-50c6408196b4 | -9.01977 | -44.37347 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45150260-5d3e-34ae-b04d-748ad6858152 | -8.90564 | -45.21275 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96a73521-7b46-328e-85ec-0289f88c6361 | -8.97155 | -45.90964 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4082015-3699-3d33-90c2-222a2634f314 | -8.96923 | -45.91713 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddc6b129-15d7-3a23-9377-038c85b931de | -7.50928 | -47.33869 | 2026-10-09 03:45:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3046ee2-1fc5-3342-b475-b23f06da634d | -12.02582 | -43.47522 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 613d8c0b-ee08-3371-a48f-7bfb9597b64d | -8.90157 | -45.23469 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fe3a924-c111-3619-9b01-f8eaee4ecee8 | -6.8797 | -45.91603 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 797612ab-3b63-3010-b08a-28ce40141c18 | -7.18067 | -44.28525 | 2026-10-09 03:45:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dc23a85-2063-3e4e-bf67-a1f9a397eaf3 | -8.73379 | -45.16452 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c22a9cf2-dde0-3174-8b9f-3051bb4a0c59 | -13.36723 | -43.88683 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eeffd49-ee8a-3a87-9021-f75015154dc5 | -12.00405 | -43.48088 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c925fd-1bd5-351e-9a2d-0709de08296e | -11.8363 | -43.60205 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cfe0382-9be4-3c9d-9872-9083a0282d57 | -8.72287 | -45.1576 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7d2c796-922a-30a8-a3a9-c354c7ae3182 | -6.88686 | -45.91299 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a889902e-456e-309d-8ce8-15293975583b | -7.40409 | -44.75961 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d71e984e-5eb1-3b75-8002-8bcc0bbce26e | -11.25129 | -45.25077 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f519e5a5-ee3a-3b9b-93ea-5487c1b58197 | -14.44028 | -43.9313 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdb0c06a-4e78-30b1-955b-9bfc89e5bc37 | -9.07944 | -45.10962 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43503764-f0e2-3f50-8356-346eadf5fa95 | -7.34587 | -45.30965 | 2026-10-09 03:45:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a1699e5-4012-3790-94ec-f3a5969ef7c6 | -11.23877 | -44.87314 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eebcb03-4aca-36d8-851c-e072b9236b02 | -8.74216 | -45.1526 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f48933e0-ffc0-343a-90b3-0c9b012935df | -8.72454 | -45.14885 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d3fbb10-28b0-38f0-a983-b907955ce2bd | -8.95965 | -45.17379 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c2e55c4-31f2-34af-8a1c-2270649acb4f | -13.40839 | -43.72792 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f7c90de9-406e-39ed-b2d6-47730265d4b4 | -12.00671 | -43.46672 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ff3daf1-41ff-3a82-b69f-1625e6eba7a2 | -11.1426 | -46.14254 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c57c777a-db1e-36ff-9c09-eb02052bd3af | -11.77753 | -43.5328 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eaf29d4-d3f8-38e1-9586-e1119e435a79 | -11.84754 | -43.59807 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5779c9af-d609-3cfa-89c7-90a682371764 | -11.84869 | -43.59201 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c569040d-1e89-3e0f-93c9-832a0b804a27 | -8.89733 | -44.933 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a82481e6-9595-3cb4-a4c5-4ef510a9abaa | -10.19051 | -36.32595 | 2026-10-09 03:45:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b8cc989c-9d65-34c3-ae46-0601ae0c50d7 | -8.32312 | -45.45699 | 2026-10-09 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8d1a1a0-20e4-3d59-867a-43c72128ebd6 | -12.00173 | -43.46569 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62776ecb-0078-3705-99fe-037bee7778a5 | -11.11498 | -44.00314 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f078a8a7-0050-325d-b7f5-17047b813463 | -11.05994 | -44.06835 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85826d15-a621-3daf-9fe6-9390a1015b2d | -7.40493 | -44.75506 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a041d8c8-b55b-3840-a47c-6ca31f322dec | -11.08252 | -44.05844 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 711be9a4-7df4-394b-b435-305d9ed6ac21 | -11.11274 | -45.68533 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c13937a9-6325-377a-a825-8165683274c3 | -9.93704 | -43.56353 | 2026-10-09 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README65.md)
