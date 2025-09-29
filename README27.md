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
| b71cdee4-a25a-3854-9b1d-a2c0a4d57565 | -7.58679 | -44.78603 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b637aadf-f798-3661-bc6f-7a1c71a1a2d6 | -8.26496 | -45.49558 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2f0ee28-f569-3479-8dbc-9f2b10399cd1 | -6.06167 | -42.46764 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 430cd862-62b1-311f-a49b-1e12ab273d52 | -4.31169 | -48.08444 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50487ab2-10c6-3323-bd8a-fe06412e024a | -6.06738 | -42.60345 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8577a75-1845-3203-896a-5a67ddd258c3 | -5.74917 | -42.87792 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b723ea47-0747-34ac-a36f-f49fabe84a51 | -7.29369 | -42.83556 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8cdd0b7c-6876-3a3e-bea5-78ccd9c3a565 | -6.14017 | -42.6552 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36e76a30-4453-3d36-aab6-906accbcdeb2 | -5.02801 | -42.54181 | 2025-09-29 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d0e6350-ab15-3ed8-b52e-ad7ac34487bf | -8.25088 | -45.48878 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c37555b-3fd1-3ad6-a6b1-3107c41bb801 | -7.81672 | -46.99553 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c723e9f2-cc38-388f-a724-40bff727db20 | -6.27878 | -42.49132 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7375fd49-466b-34ae-8523-bf4409ceb48e | -5.73244 | -42.83041 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e01c49e7-b740-3c48-a697-a55f21d614c5 | -7.24679 | -43.00797 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 775df409-ebb5-36fa-afea-0b2ee6dcd6c9 | -6.46384 | -44.00868 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2a8005fb-6309-39a2-93a2-6d5588062485 | -7.37363 | -47.04586 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f65a8556-e562-386c-92d7-d33a2c7d25c4 | -7.59037 | -44.78667 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb75b84-a28b-3360-8db6-e69b6587cfb8 | -7.11009 | -45.53855 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 413bc697-cf41-359c-a4fb-f113fc791c5f | -5.69516 | -42.61031 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 742fc836-1ae6-321b-90ba-599ea43238fd | -7.86476 | -41.05566 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89b6df4d-1d05-325a-881e-183a5efdcc1b | -5.68612 | -42.63473 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6edee4c4-c818-3fc2-bed4-0c13237d1447 | -6.57382 | -43.42255 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db907ae2-d325-32ae-aa4b-1385559654d7 | -6.12235 | -41.81039 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d8bd6d3-91e9-3382-90fa-b0df201833a3 | -8.25385 | -45.49382 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba81d408-8190-3cf9-9c46-e703064c0b16 | -6.74182 | -43.381 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6291fe8a-3cf9-3d51-98fb-890522c1c90a | -6.11353 | -41.8232 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 525fd62d-e232-348b-8414-02b82c3c7eaf | -7.58905 | -44.79478 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b9c0707-0ffe-3557-8e70-8d1cd5f8b64f | -6.33232 | -43.35454 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 523ebbd9-b354-35db-a7e8-d382f480dbe4 | -8.27717 | -45.50364 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 630cf3cd-71ef-3311-995c-402339b4d553 | -7.85052 | -44.59193 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 057decb7-859c-3890-99e8-2c2b9246a1ab | -8.28828 | -45.48289 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 294e0d3d-2b68-3936-82b2-7f64409e4e35 | -6.25898 | -43.63589 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47afd3cd-2670-3bec-9c9d-408e01b59a91 | -8.27091 | -45.50571 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40893732-523b-3857-846b-519070fd5e9e | -7.24285 | -43.01104 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 63e667cc-b4ad-36ed-a0a5-7160d55dd091 | -7.0259 | -45.18519 | 2025-09-29 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d0d6cc7-aceb-332d-9fd7-b66dc2652406 | -4.75147 | -42.69508 | 2025-09-29 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d013fc0-ec7a-34c5-8607-55a777a1e8e0 | -7.73647 | -44.94954 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 711c5b61-c291-3b26-bde5-2910257406e9 | -6.10211 | -43.67038 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 745eaf32-b55b-31d6-89c9-be941977b6a3 | -8.15921 | -46.33645 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e3dcb78-4444-3d09-ac12-d39a6aa6e379 | -5.7681 | -42.83241 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 914dbd01-aa0b-3085-ba89-b4d6f6e8bde2 | -4.15122 | -40.00364 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 277f1673-7d4d-3015-8083-d87cfe89bbb3 | -7.81137 | -46.90559 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e800e299-2042-3e9c-9d9e-3f64a82a17ba | -6.09804 | -44.49496 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f90f91ec-a239-305a-9420-6cff739113b4 | -4.39499 | -47.28567 | 2025-09-29 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09542178-0a4e-3cbe-b326-59e8939563ce | -5.17853 | -41.24952 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8f126f5-2ccf-3628-9631-1fa5df97740d | -6.69167 | -42.73577 | 2025-09-29 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b7917108-3998-3823-a4b6-399bc9a2c9a9 | -8.30167 | -45.49362 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| da9707fc-bc9b-3539-9c5f-86c8b97d6c63 | -3.86028 | -42.69838 | 2025-09-29 04:06:00 | NOAA-20 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f29fa07-d2f5-397c-b54d-d4d48e057f6c | -4.99585 | -45.13831 | 2025-09-29 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf9c6d5f-6ba2-35d3-ad14-e4aa677efda5 | -8.25828 | -45.48994 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eef59475-0ce1-387a-8d66-f27ffa43b039 | -4.14076 | -40.00912 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cacd3b77-f8a2-38b3-9e5a-a5a877ad4916 | -3.83722 | -40.46992 | 2025-09-29 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61137310-d6a0-33f2-bb0d-a13b010335ab | -6.13738 | -42.65108 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05556769-1701-302e-817a-359304f6d46c | -5.72848 | -42.83348 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5db2d7ff-d785-35ed-bcc6-01c1291bb628 | -7.29705 | -42.83609 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ce8f7ec-d284-35e8-91d3-6a537eba0771 | -7.56535 | -42.41561 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2990c4b9-3cec-3825-b586-bb53614e7142 | -3.34471 | -49.22527 | 2025-09-29 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce651565-5de6-3de2-aecc-a4d361408942 | -7.75767 | -47.001 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a540a42-a37c-35b2-bc23-5667ff92a957 | -7.02959 | -45.1858 | 2025-09-29 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e278372-e473-3355-8be7-051c511f3f36 | -3.49737 | -52.47288 | 2025-09-29 04:06:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e74dfeb4-54a5-3dfc-be14-0bb8ca93484e | -6.21244 | -44.21459 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20dc9cf2-5ab1-3e98-807f-a559188537aa | -7.22812 | -44.78214 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| dbafe8cc-fe20-30bf-a3e3-c1c6b87442ba | -5.66613 | -43.04842 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7cbaa119-d951-3b9f-9d2d-f2277ec37185 | -7.75359 | -47.00029 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b456283d-58fa-356e-ba80-044c4f39c1a2 | -5.71601 | -42.84636 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| f8dff5d8-2915-3570-8926-b4d46082ce2b | -6.44656 | -44.02604 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b6e476-7b47-3d72-bf2b-573775775fd0 | -5.14947 | -46.07767 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2ba56d2-c19f-30ad-b397-355210786bd9 | -5.73645 | -42.67551 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e76a4051-f52a-3f6d-b562-5dd84951283d | -4.91923 | -48.16094 | 2025-09-29 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b82f21a-00ae-3078-b08e-b24eb15bc054 | -5.30405 | -43.16255 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df5487af-1360-375f-a454-bb6946339934 | -6.67334 | -44.60314 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04356d4f-6058-3998-a372-edc2f6cd808e | -5.51391 | -42.72895 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9952202a-a44f-32a3-8fdd-1cea499959da | -5.77957 | -42.89023 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e63d8707-53f9-33de-8c7c-0189de255361 | -6.75023 | -44.74438 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae0033ec-8987-37e2-8bdb-52f65801c371 | -5.8132 | -42.8323 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 914c1a98-ff04-3739-b831-87737a599c0a | -5.74124 | -42.88411 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ca2ab8ee-aa96-3166-b15f-0db270179dca | -5.16348 | -45.01337 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64fb0591-0505-3620-a331-6f91cbd116b0 | -5.69343 | -42.62104 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 205506f6-26b8-366b-b1ec-f4bf3c500bad | -7.29877 | -42.82541 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e6a92be5-7971-36cd-8f21-a8fc049be51e | -5.38463 | -42.30613 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b26a162-ff2f-3d31-9694-3bd9c618801f | -6.98305 | -43.77709 | 2025-09-29 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85bbafb1-443e-3f59-a6e8-50cc8dcb7738 | -6.57706 | -45.09627 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ad754e2-77e8-3e68-8946-cc2c087dc0df | -6.2782 | -42.49491 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b173325d-b7ef-3d69-a17d-cff6f3fe2fbd | -5.09079 | -45.48485 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b53be32-a24a-3a74-b874-8d263298cc0c | -7.24622 | -43.01158 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ca71ba4-1233-38e0-ab78-ad4dc7ac05b1 | -5.55371 | -44.84136 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca4d456c-6148-37a6-854f-ae833ebc0721 | -4.70862 | -41.98235 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b85a5794-c73b-32c0-9d4a-f696dcad6337 | -6.68054 | -44.60429 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a08fd455-7023-3954-a185-a325beae810f | -6.12898 | -43.48328 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88352995-96ea-3ddd-9bc0-f920b193fb51 | -7.18626 | -41.69932 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05ebcf39-37c9-34a9-9e14-87a0bbc33ea5 | -6.25019 | -42.46123 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0be89fe3-1f36-3446-aa2a-6e7758178d95 | -5.56634 | -44.85678 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87499eff-7685-3f17-9c4d-7462df0b6262 | -7.29312 | -42.83912 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ad7c2c5-cb7b-314c-84df-8a50d676944e | -8.27122 | -45.4939 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b21480ce-77a1-3937-8fc5-dae4e4f2fb58 | -7.51052 | -44.30069 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3a9187e-b9cd-345c-b9d2-ecf3a0af949d | -8.27343 | -45.50325 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 37d43b34-8e35-3285-be8c-e163998178f3 | -5.50995 | -42.73201 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| afd431fb-efd1-34a0-8e62-8e1d92ed35cc | -7.89258 | -44.5769 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5116fc12-39be-30aa-b81f-873df2913e2f | -5.48941 | -45.10759 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7173ea0-e295-32fd-b9e0-f2d3f4e45ba4 | -8.14746 | -46.4055 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README28.md)
