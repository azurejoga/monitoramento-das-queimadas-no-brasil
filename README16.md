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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d26950-9358-370a-9167-0568f6f85442 | -6.59463 | -44.28307 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1179305-27e7-3151-88f5-d08e4d6ee38e | -6.42719 | -43.08694 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b0477769-b5d3-3145-b47f-20f5ac488cc3 | -3.93925 | -47.56688 | 2025-09-25 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f08130b9-8906-3236-b00e-4bded692f5c2 | -4.5238 | -43.64044 | 2025-09-25 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c3cca3ca-9781-3b7d-aed2-293034b8e1b9 | -5.53116 | -42.73233 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe11601b-433c-339e-99ba-b5a3475f905a | -7.25944 | -43.01105 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a0032f42-ed60-37e0-bb6e-e2ddd698032e | -5.52346 | -43.86965 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1c0a1ddd-0253-3060-b558-fa769ba1d306 | -2.989 | -49.28552 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 014eecb7-bf5b-312d-8879-497aca6b1be5 | -3.79236 | -41.73666 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d5a7062-8e5a-3b1f-a331-0893b6ad5c01 | -3.68101 | -45.8349 | 2025-09-25 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6bf8622-8b66-359e-be56-95c8d617dba0 | -3.01501 | -51.35189 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e19a93d-e5c5-361a-b3a3-e71c3a7fa545 | -5.54154 | -42.80202 | 2025-09-25 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b026565-668f-382b-a1d4-346ea128be64 | -6.43117 | -43.08749 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 731d5539-b0cd-37f0-b59e-2716f68e0c8c | -5.30356 | -48.36875 | 2025-09-25 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15df5120-46cf-3383-ad17-16dffce4d30a | -6.84327 | -43.17596 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fc66b64a-f9a9-368f-bb6e-d91af93f6e93 | -2.26021 | -47.85323 | 2025-09-25 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9daf3c0a-be71-321e-ab2f-33255d02231c | -5.61665 | -43.00093 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b63a351-2452-3787-b67f-1bc9a4b17153 | -2.9237 | -49.07763 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afaab54b-05bc-3a35-beb6-2d20ba3c48c5 | -5.88744 | -42.82544 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3e8e9b0-9add-312a-a57e-bd12d4e61975 | -2.25197 | -47.884 | 2025-09-25 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e3a1473-5e1f-3ad2-88a7-11305dff6602 | -7.2623 | -44.91029 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8309adbc-334f-34e3-9024-7df44f8df505 | -4.30892 | -48.09406 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9b83d57-c91a-34a3-ba2c-39c090c2231b | -3.17861 | -42.94798 | 2025-09-25 04:32:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee67675c-6cf1-3381-bd8e-9608593c2d9a | -5.42705 | -41.31947 | 2025-09-25 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50dad9c4-6199-3681-9a3f-95ba4867f094 | -5.3979 | -48.84986 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77131c62-51cb-354d-939e-bf37d45f280d | -6.72835 | -43.97377 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3bd6db4-73b0-34fe-b413-a14c29cbe710 | -4.61036 | -43.91556 | 2025-09-25 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a196d88f-d989-3e99-a17e-0766fff8301f | -5.24501 | -43.07417 | 2025-09-25 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8133fa2a-dcfe-3b66-bdfd-80524cd6927a | -5.23157 | -43.69734 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a533d92d-ab58-3bb6-9046-0edb5a648b52 | -6.30471 | -42.5388 | 2025-09-25 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 06033ae8-03fb-3d91-b5a6-45f61b0d56f4 | -5.73272 | -42.28878 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 413e1136-8e5d-3e13-bd6f-82bacb00e021 | -4.2921 | -48.26543 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcbe2d92-f94c-3ec0-bc9c-c24e5264bd57 | -3.73928 | -49.05075 | 2025-09-25 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bd26992-72fc-335d-9cae-db41714e867a | 0.91701 | -51.20715 | 2025-09-25 04:32:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22b91bb2-ec36-3352-9ba5-9d361cbc3aeb | -5.45715 | -47.34467 | 2025-09-25 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bf487c-ded0-3fcc-9f02-df974e8d1654 | -2.91791 | -48.30361 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f187bd32-ac05-3f41-993e-5b5c89724c31 | -6.13627 | -43.45052 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffd362cf-83a6-357a-9d2a-85b281d87603 | -5.97488 | -43.77875 | 2025-09-25 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf56e5cc-d077-30ba-9ba4-38596ae03af8 | -6.09918 | -43.96227 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cde7954-794d-3bac-8393-1105e486fb04 | -3.30928 | -42.17389 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 79d741a0-3179-32a1-8e66-0ec64c73f2f8 | -5.95526 | -42.90667 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f2d5ff0a-22ab-3b49-8363-a75b66aba7c3 | -6.35182 | -43.35097 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 993c897b-4ca1-385b-b9e2-01d92c74046d | -6.84724 | -43.17658 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e34b231-4f60-367d-8f15-143dec3b8dda | -6.68448 | -43.13128 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be9b3f31-3a1d-33ee-bdf9-b21c33871d02 | -4.79455 | -50.74166 | 2025-09-25 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ebfd08b-2d05-3a5f-a0ba-898717a05e85 | -6.15801 | -44.72866 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 195b2b98-b8c5-3e27-9aca-b2292f2f843f | -6.79929 | -41.75802 | 2025-09-25 04:32:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ad434c8-70cf-323e-8551-fb50cc8a61c3 | -3.99658 | -38.33432 | 2025-09-25 04:32:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 400532cf-25c5-3781-bc4a-fc8863d0f292 | -1.27056 | -47.86968 | 2025-09-25 04:32:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 825cdd58-8088-3abd-a08a-2114978c93b0 | -3.61292 | -38.76205 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9a367bf-d2cf-3eff-b343-5ad874fddce0 | -3.78759 | -41.73991 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5fb78a68-0a0f-30f2-a2a9-b04410645b7e | -5.54103 | -42.80547 | 2025-09-25 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73120942-7f14-3a8c-bdb2-52f470eeae46 | -2.70625 | -54.65094 | 2025-09-25 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 990126e9-07c8-3956-8537-fbb8b4c0413c | -6.25656 | -46.11033 | 2025-09-25 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26f8c95c-f123-3e05-b829-1a84e9d613bb | -5.81879 | -46.35279 | 2025-09-25 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 184fc443-b073-30ce-a53a-6996bce9211a | -4.25688 | -48.5969 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a247f9c8-8ecb-3646-b04c-342452c6a8fe | -6.55544 | -43.83186 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77cd7057-97fc-3bdd-84e0-4464b47cf94b | -5.79009 | -42.80756 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0ccdf3e1-c786-3398-a55c-7ba0b0705c05 | -6.59726 | -44.62182 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b024a13-f087-3993-af84-bf8f930ecdd1 | -6.57502 | -43.65433 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7af5647-1728-3beb-964b-6cead52fdb3a | -2.91871 | -40.38901 | 2025-09-25 04:32:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 38795c7c-399d-36fb-9025-7cfa25e8e55d | -3.39849 | -47.49895 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8bba36b-a520-30ec-8faf-0eb34c008e5b | -6.75287 | -44.63062 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e431252c-cab4-3845-921f-dc24b48bb6b0 | -5.89144 | -42.82614 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a30cbc7-6036-37f4-bfc2-9c0ce4a5be76 | -6.40282 | -42.94732 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8dd85975-a0da-37ca-ae46-d748f0fb3f62 | -2.91418 | -40.38834 | 2025-09-25 04:32:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c94ec7d5-d1fc-365d-b5d1-24414b8bc808 | -5.79062 | -41.76649 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 975936fc-a811-34bc-b14d-32b44b768a4e | -5.93225 | -42.9246 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9a2c7d11-331b-3d64-8a72-b4fbb4bb2b9b | -7.25893 | -43.01461 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5bc6d829-08fe-34db-ae47-0acbe00bb9dd | -5.70498 | -44.99416 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb0debe-1e92-36ef-9ce5-6f4ef9416ccc | -4.80676 | -43.53341 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1398b70b-f319-3fcc-ae93-6371ce2bdb06 | -1.69738 | -47.29802 | 2025-09-25 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 023aba21-64c7-3340-a785-a15cc157ad13 | -2.26505 | -47.19426 | 2025-09-25 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c49b34ce-7dff-3a3e-8721-4b99be964bf8 | -6.89457 | -44.76156 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5549ac23-400f-3de5-9796-3731359133e8 | -2.92643 | -48.31209 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa24537-c8ba-34e5-be06-a9a426492f1b | -7.28435 | -42.98197 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebf74f17-4fbd-3f7f-bac7-e2776e1759a2 | -4.57185 | -48.02256 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd971d8d-1a22-304b-b721-b0bdcfd97c67 | -4.28878 | -48.26492 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7781dbf0-3936-3798-bb33-0179788fbd61 | -3.21132 | -54.95866 | 2025-09-25 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4f0953b5-2523-3a07-8269-c176a7f2dcfd | -2.63917 | -48.04092 | 2025-09-25 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a955dec-92b4-3015-9872-35a5223199bd | -6.686 | -43.637 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b08053bc-275d-3739-9562-5235fff10e48 | -2.83485 | -46.72525 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6feda66a-7ec8-3907-b9d9-5938177cabb8 | -1.94746 | -52.08323 | 2025-09-25 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a652c4-73f3-3435-b5a8-606db806f1ee | -3.73589 | -49.05023 | 2025-09-25 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc81e32-da8b-3641-bea6-0f926ef26a4c | -3.78874 | -41.73224 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58037e07-1ce6-3cba-9925-088b2a335f7a | -5.24915 | -42.85695 | 2025-09-25 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43b91d67-30ea-3c83-86ab-79e1be1a165c | -5.53167 | -42.72877 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84c8024e-951c-39cc-8c27-7a9e9feda14e | -3.82686 | -50.9723 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e1b25d3a-f5f4-39eb-8f4a-14d0ef6c77ac | -6.488 | -43.79203 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e85eb8eb-916e-32dc-8a59-a11e087e471a | -6.41873 | -43.08914 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b3ae543b-06d5-3810-8c06-85fa07e15cf0 | -6.41822 | -43.09253 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4f0981b3-b993-393a-acd5-93b9d3c4cd87 | -4.52227 | -43.64208 | 2025-09-25 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 81ab6123-dd24-3d1a-ac61-c578126164d0 | -0.90966 | -47.54567 | 2025-09-25 04:32:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e038814d-8013-3200-872a-a4c660326e76 | -3.80481 | -41.56766 | 2025-09-25 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 485323df-fac0-33c7-b102-387a1f291cb4 | -5.95526 | -42.9348 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b3fc124-0963-36d2-a13b-4e889fa29e91 | -3.15207 | -49.47651 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed9a40db-8e3b-3743-b889-fe5e3db0f043 | -3.74487 | -38.95478 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8716060-0b6b-33b5-9e37-026c068b5cd7 | -7.27167 | -42.98365 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7876194e-bb0d-33dd-82ff-a1f249a78337 | -7.26291 | -44.90611 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73177e7e-21f3-3e00-8788-9612d7cd471b | -7.98701 | -43.58178 | 2025-09-25 04:32:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README17.md)
