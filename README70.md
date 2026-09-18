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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a8a8c7c-bc5f-3e64-a22f-e23ce2d53a87 | -10.1044 | -45.64008 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b577234d-bd09-3b69-8381-a0b56f53c525 | -4.79522 | -56.12067 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 607a5688-0119-388c-9340-dd89de6e5ade | -8.81049 | -46.9401 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f6b4e9c-ab57-3562-aa83-16a48bf01e50 | -10.40311 | -48.68299 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f26f249-10af-3dea-ba01-f481b19aab81 | -9.91498 | -46.54198 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 468eafd6-4779-3c55-87d7-ec6c087f86b9 | -13.4716 | -46.89931 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eac382f9-08b4-3c90-b6cc-596f4f49cbbf | -11.31583 | -43.42397 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62a4b0ca-9f01-3d18-a34a-74f3549e9177 | -11.29268 | -43.3983 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18b51f31-a809-3eb2-841c-9e224bbda4a8 | -7.81784 | -44.90752 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20c43139-a61e-3306-a984-556d3e3cab61 | -10.12068 | -46.30292 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2e156cb-fa83-3fe3-973d-a51809c2ad0c | -10.29091 | -45.32059 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95029a18-4b53-3ac2-91c2-7a1c8ba5ca6f | -8.88293 | -45.87998 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa7977d3-5c69-31e6-8833-c65971681fac | -4.80425 | -56.08297 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bcf0012-feed-3ec7-a98a-16946e38645c | -6.02609 | -51.80824 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 872ab2a3-3c5a-3588-afde-546a83cd4662 | -7.68054 | -46.09517 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf7aa3ad-ad70-3a0a-b000-fb19d7758e8e | -12.53233 | -47.08198 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6de3e82f-de62-3343-9b13-54f35756a708 | -10.63016 | -50.25427 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9745d12-090d-321d-bdb9-d4c3ab9e3c28 | -10.5156 | -46.73325 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1c86c5c-e530-34eb-9aca-09253abed38d | -9.93985 | -45.2893 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fbfe991-b1c6-36f4-8607-9f48773818ad | -6.93336 | -43.11925 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb36cf16-9163-3831-ac31-22c0fa0e5323 | -9.23965 | -45.91137 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da552e8-f529-36ab-8842-a8e0b29cd1c3 | -7.61958 | -46.17595 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffde60fc-79fc-3fd5-bfd7-6354e7b58f82 | -10.89103 | -53.994 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 164bd27f-2baf-3276-9edb-99b5a44e62ab | -11.27826 | -43.5111 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 562fdac6-495f-3306-8fb8-fb4e72861248 | -8.44754 | -45.83769 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 418f81af-99e1-3a45-b49a-920a4448f3af | -5.17686 | -56.18287 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fe687b9-1a96-38f4-b313-d54775977a79 | -7.79545 | -44.8732 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91b2b7d6-a3f0-3af9-a307-06c207095210 | -10.63642 | -50.23614 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 328e8ab7-a6a9-3a8d-9fdc-a026b0c9575f | -8.88327 | -45.88557 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5d6d1dd-fc89-343f-a823-5ace9103c539 | -9.18919 | -46.75679 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b83a83f2-2db8-309e-89e9-eae8416353a8 | -12.17031 | -46.9921 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5b36647-edb6-3eec-8c43-a746a73235e5 | -10.66953 | -50.27188 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e5e40de-5b39-3da6-ace1-e2bccf1b2b36 | -12.16901 | -46.97166 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 795500ca-0b41-3b12-a808-fca9a6723a15 | -10.83363 | -44.9625 | 2026-09-18 04:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| affb56e5-93c6-340e-8c4a-a01144aad099 | -12.16555 | -46.97799 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2fe33a7-26a8-3203-8f87-384855dc7715 | -10.67466 | -50.26123 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58a67cc2-66c4-30cf-b0ad-59d176f9064b | -4.52033 | -56.07988 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c07a590d-5040-3f09-8d35-13abcdd0a3bb | -7.75177 | -54.75229 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5faa86b0-745a-3542-be63-d2476a5ffc55 | -10.02902 | -45.56969 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d00a727-bd1c-3cb3-952d-f3fbf653e02b | -13.36184 | -46.299 | 2026-09-18 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d816f57-1cb8-3fb0-9bdf-ccdbb3b71ec5 | -5.83714 | -52.03175 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4873dde4-6891-3fd8-8b9a-96033f92e5c8 | -10.79119 | -46.16877 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5d3841e-1786-37bc-880c-4f88b656631b | -9.94988 | -45.33397 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018ffa2d-06e2-30e9-b330-c1c096b900d5 | -9.9442 | -45.3422 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94dbc65a-e2cc-3769-b707-c655ac0381b9 | -8.93543 | -51.46434 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02de6abb-4cd7-3d2b-9ee7-867613b47268 | -10.12099 | -46.30043 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4265e53-31aa-3f55-956b-31bd2007b12f | -10.10383 | -45.6443 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1675ec31-5233-3674-8ff4-ae6b71c4e9fa | -8.8486 | -45.91594 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c13c9be-45ce-30ea-99a5-9614086839a7 | -10.1084 | -45.64276 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 210fe0f4-99c1-37b8-bef2-1d0a08580380 | -10.09253 | -48.18752 | 2026-09-18 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00a24337-8afd-3186-8deb-1c312287730c | -12.31703 | -50.82656 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 591c3e30-df34-3b55-8efd-9297ed1c31c7 | -12.13109 | -45.1586 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b2a895f-5da6-3b01-9621-9f1e7eda5043 | -10.51866 | -46.74123 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a660c6f-328f-3c97-b627-bc517e43f0c1 | -9.72227 | -54.80732 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 66162081-a9c1-3887-8acc-eafaf9b8c9e2 | -6.43852 | -44.95042 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 091981c3-0c83-38c2-bed5-1ba6fbe0358e | -10.67523 | -50.28041 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7dd392b-300a-33ab-9cef-8f31732437bc | -8.48347 | -57.62498 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba6c4a6c-ae62-39bb-8b5d-71677d991dcf | -6.9975 | -42.15457 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0f38f468-b253-31c0-a157-25d11abae758 | -6.77101 | -47.87068 | 2026-09-18 04:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5031f687-fc62-3783-93d2-ca6c21b77f11 | -12.39939 | -50.69838 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a842dc2-23a5-3fff-9b62-7309a3376904 | -10.67694 | -50.26922 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6185b0b6-b520-3b31-8d4e-18bd28952bd6 | -11.80683 | -46.80238 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eeee047-98f5-3f91-8a9b-28e43e119e25 | -12.53645 | -47.0826 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae32053c-5840-35da-86ac-701c6d93fa2f | -13.25699 | -46.89915 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| baf97528-46ad-30b6-9355-ec6447b51ab1 | -6.77761 | -46.47328 | 2026-09-18 04:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a085d34-1031-3ae3-897e-846052bda08f | -10.1212 | -46.29913 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8648b132-d167-395e-ba3c-0487b90cfc55 | -11.27786 | -43.51421 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a10e0e02-0565-38c4-80f2-8732e0257e90 | -13.23159 | -42.33292 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 6f18cb24-8785-3165-87ce-af74ea345cf0 | -9.92223 | -46.57946 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f51d19b2-13b6-3d62-b7c4-c71e046c2890 | -8.78067 | -46.89527 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c5a0720-b11c-3dee-b70b-79dfb4ad64dd | -9.57233 | -46.56781 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf23babd-6839-37fa-b3ac-8b0e0da4e475 | -10.67922 | -50.27721 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 014b5cde-73c7-3ce8-ace0-2c5fa79b8678 | -7.94022 | -49.56334 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc7a2ca-dd83-3ffa-8519-ead6965bb743 | -5.86733 | -52.05856 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 990a1f65-93dc-3d4c-aeb6-0cd2c6369dae | -12.39004 | -48.47259 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5997af76-dae2-39e8-9c24-b0c7c4ee7b8b | -8.7382 | -45.40853 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f4f4594-21d4-3839-b271-e15ebff1d732 | -9.95186 | -46.60647 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18754806-92dc-31ab-be53-e24089d069d1 | -8.4446 | -45.70905 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8909d26-19c4-3e8d-b726-35d8accbb84f | -8.90673 | -45.01605 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46a611d7-7b01-384c-b479-d9548deb3523 | -10.64384 | -50.23347 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23330fb1-ee61-3ea3-a693-308ce5709fdc | -13.25034 | -46.91247 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73508cf8-10f1-3a59-9646-35348a7edc58 | -7.01902 | -43.62627 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20d4f879-eab9-339e-a930-c50679132b77 | -11.35849 | -43.9504 | 2026-09-18 04:57:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 841ba015-7d66-3dc8-85c6-43d060baad0f | -7.58385 | -46.30624 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16d4271e-65ec-3b16-b377-3bb444c32632 | -11.31847 | -46.76086 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86234712-f24c-3954-aa3d-072b4c3601ca | -9.17764 | -46.75159 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 328f7737-f657-311e-b4a8-0a3649ba0a47 | -13.24955 | -46.92169 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0d7f6439-1331-3ae5-83a8-a059d545d34f | -10.37233 | -50.46058 | 2026-09-18 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 529ae793-4cc3-339e-b20b-7f56517e7884 | -6.43129 | -47.25173 | 2026-09-18 04:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72b35624-57ee-358f-bc97-b0027e67f368 | -6.02218 | -51.81122 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1be4033-5522-3566-8939-f97ff9e65e21 | -6.61472 | -44.2002 | 2026-09-18 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d009f1af-90fb-3e76-b97e-2a17be4dd6da | -10.63871 | -50.24414 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c82c6c32-7763-3a45-afb8-d501253eebe6 | -5.89054 | -49.77948 | 2026-09-18 04:57:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b53c70d2-0101-3af5-86f9-f2d25bd5ccba | -12.52718 | -47.08883 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bbd4d0d-d9f3-3136-909b-34acedbd13d7 | -10.66436 | -50.46456 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0de87a1-8950-365a-a79c-0b4345ad85dc | -11.31792 | -46.76477 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c85ee2f6-9b89-3873-b9ce-acfa08885ac5 | -10.6701 | -50.26815 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8dccd02d-abcc-337a-b621-37de93ae3ab8 | -10.64613 | -50.24148 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 60af123f-1e87-3c7c-8525-e5f6bda11575 | -5.86848 | -52.0514 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a03c6c5-379f-3557-9392-cd95ebc40d1f | -7.68107 | -46.09148 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README71.md)
