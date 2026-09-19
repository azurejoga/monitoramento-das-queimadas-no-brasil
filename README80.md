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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b39b6d3-97f7-3326-9e2f-64216a7fcdd6 | -10.30964 | -49.95572 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63cfd58b-1808-3d78-bddb-4600dcaac699 | -7.86557 | -50.2293 | 2026-09-19 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99c007a4-0dd2-3508-be67-2f00cc18b95c | -3.36707 | -50.44545 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3912da0-8607-3895-9583-03908ac78884 | -10.82164 | -50.16647 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2bccfb1-a0d3-3698-a7a2-c0b85b74189f | -6.36091 | -58.28094 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1b15262-8750-341b-836a-fd64a11d85e0 | -8.77424 | -48.67067 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 748494ab-26e8-3acd-a818-d34eabdddc46 | -5.88698 | -52.08438 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39eae983-28d0-361e-9f92-8d0c8bfaa8ae | -6.67579 | -50.90682 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1044d8f-1ff2-36f9-ae10-8d255fcea921 | -6.94203 | -55.04415 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fff5f86-2103-38d7-a10b-cd0025a80483 | -4.82456 | -42.88076 | 2026-09-19 04:57:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8f36249e-bcf4-369e-9069-a276dbb0a440 | -9.94363 | -53.98875 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a073d2-ddca-31d6-8728-94c63e71eb1c | -4.56837 | -54.90863 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dbaf889-22b8-39cf-af39-548c60d25c36 | -6.78256 | -46.4667 | 2026-09-19 04:57:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9869984a-7733-3ae1-8f35-aa882f009e60 | -3.04374 | -51.37468 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5616449-afd8-3acc-a0ef-33c7a5724000 | -7.91044 | -54.76125 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff703d83-633d-3abb-a00e-f3f668ffd4b4 | -5.99741 | -51.79356 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fbf182f-de02-3fd2-aa7d-bfed6d06597c | -9.94863 | -45.27691 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 053ebb01-d88a-37d3-8a98-571e41d577e7 | -9.71613 | -54.81175 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5311051a-9dd7-357f-b56d-49842478d8cd | -5.90193 | -52.0974 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd9fd0cf-bffd-387a-8f86-f1fe3bbce4e9 | -5.81241 | -52.08304 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a649a1-9843-389c-af80-3a5e6674597f | -7.37803 | -47.75305 | 2026-09-19 04:57:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 844bc4d5-071a-3a31-8f50-6e4785ce200c | -9.80125 | -48.3337 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c35e573d-79cc-3912-92cc-e680b99e1750 | -8.75747 | -44.22689 | 2026-09-19 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a60ddb1-d5a0-36c0-9e43-2fca56110a08 | -3.6978 | -60.59768 | 2026-09-19 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aa99a01-43aa-3534-93aa-ea454827d2ae | -10.35453 | -49.00279 | 2026-09-19 04:57:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 256b4a36-b5e4-30aa-a2f2-2ea122c9ba98 | -3.37783 | -50.44337 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d627f45c-9e6b-3dbb-92fd-34f75ea89679 | -4.49575 | -55.48939 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8363bf8-4324-302d-873d-3e0b56db6ac2 | -10.00307 | -50.28085 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 974e5439-f2ff-3abd-a410-7fcbee1c750a | -2.63963 | -54.69277 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5452cc3a-7699-3a56-af64-2e4d86e9401b | -9.45798 | -45.43813 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 179032ff-c781-3f7e-97fc-250687d215a4 | -6.44537 | -44.94678 | 2026-09-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2e301af4-bf63-33d8-99e3-797c1b5f3a9c | -10.93147 | -47.85478 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64d5b431-fe4d-3bc6-b3d6-802d2357a92d | -7.77478 | -44.86871 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51b93b13-5335-3a88-a475-e6dc3f85230b | -10.821 | -50.17092 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2e49638-d570-3005-b0c9-5f19caaa5156 | -7.56652 | -57.67466 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 536175ec-a850-37dd-86d2-dc75f60538e4 | -10.50105 | -46.27205 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bc8c750-df29-3e56-be5f-185581fe4ab1 | -6.98848 | -49.76069 | 2026-09-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67593d4f-7c73-3488-b051-9947b3f1e29c | -10.50839 | -46.72056 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e64ac03-9934-3fc8-aae9-60301716309a | -10.57768 | -46.54856 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a686cc3-d78d-386d-9d15-379f2d7aebba | -5.86648 | -52.06329 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e218a5-bab1-3cd9-96f3-3b3f55156c4a | -8.75992 | -46.91679 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a18166e1-7599-3e49-83a0-36ccc0082e0e | -6.44821 | -58.15442 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14eaf9a1-fefd-35c8-ae5f-0570e87ff8e0 | -6.57788 | -44.16381 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84696870-f647-300f-9640-c765a84b051e | -6.3667 | -58.29747 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30810815-f9bd-37e5-a4d1-5226432188ff | -7.63993 | -46.10635 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 12d026b9-a9f6-3f0b-ba6d-b141e750733d | -8.89185 | -62.44117 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2ef0499f-669f-3d8c-8fbf-45256a4280cd | -2.89253 | -57.78677 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4284b47b-0ef4-3d69-8347-f2561c940960 | -7.64322 | -46.11642 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 305d5e48-08fd-3bd6-8ecd-611dd32741cd | -10.52677 | -46.72336 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e08cf9a-120e-33d1-bae4-8db8fd1b0c90 | -5.85445 | -52.07526 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee3e2061-7e2d-37d1-bc75-a462ebde8d46 | -5.88975 | -52.08836 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a270bee-71b6-3b4d-8d8d-20f3c9c8de01 | -2.93667 | -54.15624 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a894561-ece0-3e78-8a93-de14cfceb1fe | -10.53512 | -44.84652 | 2026-09-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3346ec94-d720-3d31-a4b1-04ccb7f2ba1e | -5.8748 | -53.61737 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b82c54-aaf1-3143-a8c9-0e4452003d36 | -9.24619 | -46.21347 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e9ce25e-98c2-30bd-ac3f-fbd3584b82c1 | -3.37444 | -61.3054 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017710ba-9a98-3d21-a4ef-a57091bfb39e | -4.55346 | -54.93399 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c239054e-53d4-35da-a8e9-04119e697831 | -11.08215 | -48.29118 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 008cff5c-e881-3e84-a716-d36549109429 | -3.37496 | -50.46158 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 095bf9f8-00d5-3ab8-8457-a36d3081f712 | -5.73374 | -52.23771 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a68e84c-687f-34b4-b803-b60d086d9a66 | -3.18589 | -61.11678 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00eb9e4c-6ff3-39d6-904d-d4dae4f369c2 | -7.0947 | -46.44876 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3d8624-09ee-39dc-8351-41dd130caa7d | -7.2234 | -49.63775 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f11dc12c-fbf6-3cb2-9656-31ec8786f956 | -7.4973 | -55.01658 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69e9e6a-afca-3a8c-95c6-098c01b254c6 | -6.72258 | -55.62962 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2137e0c2-015a-39da-aba2-2f49d0ef9c30 | -10.13689 | -47.68781 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b202d4ac-22be-3bd7-bd86-975769c4ed56 | -7.49388 | -55.016 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9ad41b3-3a2c-3b96-be80-ce5dbe718c93 | -3.04097 | -51.37068 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 565e36c1-3c39-3de8-9145-2b2180d92b8b | -6.10033 | -57.68966 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7841f8e-7bf7-30c4-84f5-9273b91438dd | -9.98484 | -50.27808 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf4dc25a-d10c-3223-bd3f-5610177b4297 | -8.3659 | -45.65714 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| def9df93-6d8e-311c-bb74-ccadf241e26b | -7.86671 | -45.12076 | 2026-09-19 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b45e248-fe71-3702-bb5b-5e46ebe79391 | -9.90968 | -46.59072 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3e7bab9-9618-308d-9d15-a86f9e942200 | -8.24116 | -50.65625 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4be82a6-0090-3719-80aa-9b78ab413a21 | -3.72988 | -49.04279 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd4bc09-cbc3-3ba9-bea4-c94f743daabc | -7.77892 | -44.83941 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c929977-dff2-3ed5-b153-4572f43eb0c0 | -10.27152 | -53.93449 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf5be2c5-c7c9-3e20-ab48-30d68e374ca7 | -4.50993 | -54.97578 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 774186ff-24c0-3b52-afae-a273947ec8db | -11.04565 | -48.30859 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b9ffcd9-52b2-3753-851b-6c33df4079b6 | -11.30602 | -46.7915 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0be6bb6e-d8cb-3309-a309-53ebc93c007c | -7.02306 | -44.65863 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fa3c28d-8d51-326d-8922-6f18c052dbf7 | -10.55711 | -51.31124 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c3eb935-3b72-3622-8c65-a9b3bc1d8798 | -2.88037 | -54.07124 | 2026-09-19 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4a89d3-84b4-39c8-82fc-fabf0eb2d423 | -4.25463 | -48.53917 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e684d422-653c-32d9-82fd-f5bb37b79831 | -9.48788 | -54.48133 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c769ad-9e8e-3ce0-ab6b-9998e7ed3317 | -8.14812 | -54.81376 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cb64422-d045-34ad-8f06-15fc6e978a0c | -10.92865 | -47.85594 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5db02ed3-ac1a-3ce0-9968-a2ec836291e0 | -9.89188 | -46.54991 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71e0b3cf-d9f4-36d4-8486-952bf0614046 | -8.31775 | -50.92124 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11299429-3df3-39b7-b5cd-fd6c45a5ce01 | -9.4748 | -40.31749 | 2026-09-19 04:57:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1c1e4a8a-7df8-3348-9651-dbec5c62a765 | -3.00662 | -52.70479 | 2026-09-19 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 522c886e-ce5d-3258-8c24-9d420810a26f | -10.9971 | -48.32184 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7204428-b338-3e8e-abe1-cfb7e0f7b6f1 | -8.08558 | -50.96214 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e004ef-fa93-3695-b43d-00ed8edc18e1 | -9.24522 | -45.9337 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8eb5f94-7bb3-331e-9105-c8a0b613ae10 | -7.00231 | -49.76714 | 2026-09-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc2e9339-fc90-3b81-ae70-84c470b087d2 | -10.82598 | -50.16257 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03f2f62e-7daa-3c53-bd02-61d1cc13fdf6 | -3.49927 | -49.5109 | 2026-09-19 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc67f80b-c60b-3751-a9d0-38f10d544c97 | -9.0437 | -48.71902 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99fb8010-65e2-34bd-b9a8-b4a4254a2f26 | -3.44462 | -50.66453 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5b5b091-b882-387a-b9d9-f98f1188486f | -9.7597 | -46.59375 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README81.md)
