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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14730f4c-b5e3-362f-aa5e-c6ca54db73c7 | -6.74709 | -43.04444 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7fbcf69e-933e-3b6c-b06b-8aff45c1874b | -7.16623 | -49.51242 | 2025-07-04 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbd75f5f-aa10-38f8-94de-5ee112ba83e8 | -5.86988 | -50.1474 | 2025-07-04 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82a24748-4e59-3b69-a08b-3f3812c8e667 | -7.89598 | -46.58059 | 2025-07-04 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7541478f-f97d-33d8-8ce3-d806164f2c45 | -6.27857 | -43.6801 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4996d528-3e0c-3861-94f8-16da2518a9a0 | -5.75166 | -46.0799 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50b33394-1210-3065-bb17-6830aecc9c73 | -5.78332 | -43.61456 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8055a8c3-2a82-39c4-a0cd-723b1158e24a | -5.91536 | -43.44909 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9a1bd243-f71c-3965-bd40-95d26cabf577 | -7.87259 | -47.13548 | 2025-07-04 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 770e2963-f61a-3aab-a77f-42a155b20d5f | -6.74119 | -43.17881 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b02146c4-7761-3a8e-9ce3-fa34eced655a | -7.21784 | -43.08635 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 40eb6356-9e11-3e57-a2dc-043fab30105a | -6.84805 | -43.3075 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79fa1024-f309-365d-9d1d-75af3a783cb3 | -6.6111 | -43.88905 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 990ac63a-fb6d-3b99-81f6-b96fb89b8e5f | -10.65024 | -44.48414 | 2025-07-04 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2079c91-5175-355c-b105-3458dfa1303d | -7.95096 | -44.84552 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c46f8cb-1d32-397c-bbeb-ca1d6717ef97 | -6.89318 | -43.21147 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d52705f-5563-31af-8c71-6036dffdf136 | -9.74588 | -48.35152 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 906a4f30-1c53-3fb1-8f31-acbc617270d2 | -5.88069 | -42.62772 | 2025-07-04 04:38:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cd4f0608-24f6-3a81-9c35-7ea3e554cbfa | -7.65416 | -44.3443 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47a7fc02-32cb-309f-91f6-a0e39ea4c4d1 | -6.88751 | -43.2196 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c2e277b8-013c-389b-8429-71ce74f67fad | -7.77088 | -45.15593 | 2025-07-04 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b2b62c8-9e7e-3a52-a00e-bffe2aacf2dc | -9.08423 | -48.32863 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0c8657f4-efda-3367-be22-a7aa64f723f0 | -7.11128 | -43.92138 | 2025-07-04 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07fec60a-0b4f-35c7-8206-9c5756e6f161 | -9.75781 | -48.27295 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc991e9e-1074-3cb9-8abc-8507784930ea | -7.21957 | -43.08904 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 02fa497e-d578-3615-a7bb-dfacbb88c7dc | -7.22856 | -43.09032 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 390c60b1-f353-359b-9b01-927595250ff2 | -7.9464 | -44.84863 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7120d10-c516-340b-97f9-b6bd0d0e03ae | -8.44827 | -49.63322 | 2025-07-04 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| faa7705a-1532-3c95-b0fc-81ad9e2f9f24 | -8.66339 | -45.75331 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab188c31-d262-399c-80db-d4a60d945824 | -6.11365 | -46.18489 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55641a59-b396-333a-94bd-016a4522092c | -7.22233 | -43.087 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4fce68e4-296f-30ef-b04f-ae611f457838 | -7.35265 | -44.84067 | 2025-07-04 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fdfb15f-6196-3f28-b4a6-aae61a1d01ac | -7.10928 | -47.84782 | 2025-07-04 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a4f5e422-313a-3c9a-aa93-eef9718e08dd | -7.88131 | -47.88264 | 2025-07-04 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f56edc8-e26d-30dd-ade9-757457432f5a | -9.18066 | -48.84796 | 2025-07-04 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01283e85-87aa-36cd-8ead-0f8e85dd6d02 | -7.61246 | -45.74662 | 2025-07-04 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd922482-0283-3b6e-b5d1-c42ae2dbaede | -5.28541 | -45.16999 | 2025-07-04 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9a0fc06-f562-3f7c-a58d-dfc02f6e50c0 | -7.8997 | -44.5351 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c754a572-f38f-3041-8229-ac9d54959f39 | -9.7863 | -48.57097 | 2025-07-04 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fead0e59-efcc-3cc1-b456-0209fa92bebc | -5.91981 | -43.47858 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b53c02a-4153-3c6a-81d7-8f7b52c5fe88 | -6.80448 | -44.75296 | 2025-07-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33a4ee2-72c2-306f-bd69-953a5038ae39 | -4.82315 | -47.3165 | 2025-07-04 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01f06cc5-4612-3665-8e79-770de3a62527 | -6.63005 | -56.27358 | 2025-07-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0023a6df-3807-3c49-9021-0546a4355b29 | -10.64595 | -44.48351 | 2025-07-04 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9e9325c-5757-33da-8238-b2c307d02944 | -7.07746 | -43.21404 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78b4b9a5-e15b-33bf-a692-dde5014f3403 | -5.88003 | -42.63236 | 2025-07-04 04:38:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1d93dd27-057e-3ff3-b4f8-345a58be9469 | -10.47434 | -45.11494 | 2025-07-04 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afce1472-db55-39db-8279-f08159913c3a | -8.48478 | -49.85648 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e45161c4-dc62-3e20-82ca-49ca279b02b2 | -6.11426 | -46.18073 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77e4557e-73b2-3421-8107-6f841f22a2ad | -7.08472 | -44.16736 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28831ba3-88f6-33fb-9b07-91a6c6db2a49 | -7.19488 | -43.42575 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e1ced4c-75ae-3bf7-994f-7c3d599cf1cc | -7.09698 | -49.17471 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cd65b492-5ca8-3516-b157-5ca6d9eabcd6 | -6.74245 | -43.13908 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aeac0a66-8918-32be-bf88-4248b6604d1d | -9.79491 | -47.74165 | 2025-07-04 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70473d35-6b4a-3692-8079-60e4ba3565a4 | -6.66116 | -43.17355 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8922ccf0-20a7-3f77-b529-d2c6a9b08f1f | -6.84868 | -43.30326 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b49acd1e-d8a3-344d-b269-9a55b5af624b | -6.66774 | -47.87197 | 2025-07-04 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d8cb007-ebc9-3059-90e6-01c616f04343 | -6.00913 | -44.53098 | 2025-07-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7af0aec-0244-350a-ba18-ef2ce53f4aa6 | -6.75592 | -44.62798 | 2025-07-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c7efd3-932e-3dd3-9f41-7ffd51f5303f | -9.78686 | -48.56727 | 2025-07-04 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 338edc1f-69f2-30ba-8b1e-07a594eefbe9 | -8.58777 | -48.20888 | 2025-07-04 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4136ae6f-66a3-3cba-a0e8-fc25f0c81edd | -9.75723 | -48.27675 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a41ccd7-219d-3001-bc6e-a74b915381f7 | -7.025 | -44.04127 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2adad427-c5d0-3527-9894-8179476cb2a6 | -8.85795 | -47.95409 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbcca29c-00be-3d5d-b186-0dc104d265aa | -5.32906 | -44.24327 | 2025-07-04 04:38:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b7447a-3bc1-332a-8ebc-1aa6f7ac2d92 | -7.22729 | -43.0994 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b8d12493-258d-3e97-8f7f-dc1f6d855631 | -6.66578 | -43.16838 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba33e452-35c3-38d9-9f6c-ccd3e87d43ec | -7.19446 | -43.58463 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c454ed7a-007f-3bf8-a620-200dc167c6f8 | -10.00827 | -48.67604 | 2025-07-04 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6238fd09-2b3e-3d3a-8abc-77783dcb5dd7 | -8.48863 | -49.85353 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed18a103-cf5c-310e-a0b4-6f4ff8977e7a | -6.49525 | -43.6427 | 2025-07-04 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3dea349-227c-301a-9ac4-408b98e714c3 | -7.12882 | -43.16473 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b548db10-43fd-3efc-98bf-842228552037 | -6.72022 | -44.33408 | 2025-07-04 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 519b48ae-bd0a-305e-9fb2-d7ebce960941 | -7.63506 | -44.32994 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dc87667-19fb-396d-819b-f1b3133024b5 | -8.23104 | -45.53773 | 2025-07-04 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce940246-540c-3150-ad6b-bd617ab2536c | -7.0889 | -44.16782 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7bd940d-004c-3ec2-97a9-ad5aedee22be | -5.74802 | -46.07933 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 705ecf15-5d66-3f8e-9a7e-80b3576ec16b | -5.27444 | -48.09743 | 2025-07-04 04:38:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71f9a7ea-2e27-30af-89ba-03dfb54f907e | -7.1003 | -49.17522 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d31dd5ad-a1be-30ae-b07a-574a1e5e612a | -4.82259 | -47.32016 | 2025-07-04 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42595f0d-d1e8-31f5-9b2e-ce464e5b4224 | -8.63078 | -51.56759 | 2025-07-04 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ebb6f0e-601a-30c6-aa56-8bd7f267afdc | -7.221 | -43.09604 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4aa13d40-b00c-3306-b03c-004051a5f1f5 | -5.78757 | -43.61515 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8196be9f-b000-3bb3-9477-a0c3cd0ba1b7 | -5.8732 | -50.14793 | 2025-07-04 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a3a703b-31b6-3300-8778-b6b22bdc6996 | -5.6556 | -46.59121 | 2025-07-04 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ddb130c-6f78-3ec8-90a1-99a3f4107f86 | -9.20149 | -45.33514 | 2025-07-04 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047d9e49-5c87-3fe4-9c49-c91225c08aa6 | -6.60688 | -43.88844 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| efdcd205-7f97-37ba-aa0f-292981faa75f | -9.803 | -48.25309 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e7e74f9-2008-3047-89b0-94b9081ffcb7 | -7.08418 | -44.1711 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45083ead-e765-3afc-8d8f-904f88d43adc | -8.53081 | -54.77294 | 2025-07-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7c7662b-955e-3c06-933e-a538a4b0e6f1 | -6.89796 | -47.05309 | 2025-07-04 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b9c04e-3fb3-3c4f-9c8e-2b1f71cd6cc5 | -8.44496 | -49.6327 | 2025-07-04 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 929680a0-99d8-3f98-9cb0-b3bdb443a192 | -9.61309 | -49.01746 | 2025-07-04 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50006721-10fb-39d8-afe9-a44a0ac3d251 | -7.65886 | -44.34113 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a828d2df-efa1-323a-b61c-8a587387c071 | -6.42046 | -47.2218 | 2025-07-04 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72eba1ee-3f1e-37f0-b204-9628f6c68865 | -7.21894 | -43.09356 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6566e174-b742-3df0-a27b-56b40f09165d | -5.91966 | -43.44973 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| be0011a6-bbed-3396-86e2-c483fb6c1d64 | -8.58436 | -48.20835 | 2025-07-04 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 120a5975-732b-3241-a217-591b046fe199 | -6.29139 | -43.94724 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4807f7f2-936e-3a40-912b-2c5c08178204 | -8.66519 | -45.7561 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README16.md)
