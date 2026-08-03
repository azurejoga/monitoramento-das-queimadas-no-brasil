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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2ab803-12aa-36d4-a3be-4ffa928e8547 | -2.26509 | -47.00727 | 2026-08-03 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f11316-0894-3427-8083-130f8ac1bc2b | -1.63311 | -54.46106 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 353aa9ad-0dd6-3206-b0ce-4ebedf773aec | -1.63395 | -54.45589 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 547b5c91-eac8-318c-a03e-fc4211844a9f | -1.96572 | -47.95322 | 2026-08-03 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3eef2b4-a636-3288-b21f-2de7b8107062 | -4.51887 | -38.54792 | 2026-08-03 04:36:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37098ea1-6690-391e-96c8-9ba8c77c4075 | -3.89847 | -38.54058 | 2026-08-03 04:36:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef10d590-3c57-3059-bc80-b5c358679b1c | -1.64744 | -54.46336 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9ddad8e3-1b75-380a-b707-ad952efb93f5 | -1.64991 | -54.44802 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 62bf39e7-7a12-3437-b718-324fae34cbcb | -2.75133 | -49.47919 | 2026-08-03 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91d8dc5b-97f6-3872-9ecb-188adf8c0293 | -2.98972 | -47.45186 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0a62316-3eff-3451-b3b8-b00e3f43e434 | -3.1142 | -47.90983 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3039d94f-c507-3935-8efa-c33b5527e36d | -2.09389 | -48.21459 | 2026-08-03 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7eb08341-4f55-344c-89c2-27226cc6119f | -2.41724 | -48.63343 | 2026-08-03 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0271615e-ff00-3b27-915c-76f4b3faeab2 | -1.96627 | -47.94973 | 2026-08-03 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6048b327-2379-399e-b695-dfab95465a32 | -1.65383 | -54.45405 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6d24f6f3-f0d8-327a-adbe-5d0cca352695 | -1.63957 | -54.4514 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 155bb15e-bc4f-38bf-bed7-e0b24ce27756 | -4.51839 | -38.55125 | 2026-08-03 04:36:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22064840-fe3e-3d09-80c5-29af4b1d7e4b | -3.89894 | -38.53737 | 2026-08-03 04:36:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0cd53d6-a013-3ad6-8e5b-fa57e00e30b0 | -2.75316 | -49.46778 | 2026-08-03 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b493bab-5da0-3197-92dc-145404576206 | -3.11475 | -47.90638 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68ccd491-c3b7-369b-9118-a5925c6d98bf | -3.81901 | -43.39256 | 2026-08-03 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2de8d7e5-103d-3978-b6d7-721c52cef3e4 | -3.11089 | -47.90931 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09184d4-9d34-340b-8b52-e20e306cccbe | -7.56043 | -45.09121 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 224903b2-3855-3ee8-ab4d-ab1b9324d3ce | -4.0293 | -49.5144 | 2026-08-03 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db4266aa-6c34-3002-8573-289d2cb8b5b2 | -2.95886 | -50.35226 | 2026-08-03 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a320a4a1-5b92-34e3-8530-125903a401fd | -7.35864 | -43.85117 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea8a3912-39cb-355b-8e78-55a3500af62b | -8.15922 | -47.22066 | 2026-08-03 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 404b5dbf-a9c9-3902-9896-5e4fc263d9b4 | -6.56234 | -55.14611 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a37ea517-2fd1-337c-b282-2b2de3122659 | -7.2003 | -42.95786 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b05471b-e61f-3e52-9c31-47ab13ff4502 | -7.46981 | -44.89701 | 2026-08-03 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c089e8b6-94bb-3ada-aedd-5e0cc05dcb96 | -7.83925 | -47.09378 | 2026-08-03 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b571fe2-1b73-387f-93ff-4c17626752ae | -6.55057 | -55.15899 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51671fc7-dcc5-3cad-b7df-2c5f56143aef | -6.95944 | -52.82557 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f28cf3-1a20-3d8e-9431-9e9210a44c26 | -9.08509 | -46.05324 | 2026-08-03 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 814f9a8e-ffc2-36e3-b6dc-a79e28de2669 | -6.54596 | -55.15815 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b90d412-70e1-3a17-85a7-b1f843da628c | -4.75197 | -43.72089 | 2026-08-03 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 506033c5-e232-37c7-b09c-b6e0511eeb07 | -5.20483 | -46.07483 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b66075c-4879-3504-8b5d-5ec62f411aea | -9.63871 | -49.67864 | 2026-08-03 04:38:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4660593c-f2ee-3923-bd60-82fae81e1218 | -7.86334 | -45.4334 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 943f472d-6ba0-3fde-949a-4a563a657f20 | -7.96367 | -44.91755 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 175350a6-b5b9-3096-a1f7-05f6ea3e4176 | -8.00257 | -46.23883 | 2026-08-03 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69836f2f-016e-3410-8633-d4014ecfed1d | -10.57092 | -46.79798 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a079f2a-ae03-38e7-a366-4443f9876739 | -8.58725 | -39.42148 | 2026-08-03 04:38:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72b892a9-0739-3335-9699-7fa13c3aca08 | -5.73822 | -43.27064 | 2026-08-03 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bed5c644-b1b0-31ab-b124-bc0c08ce1cf6 | -6.07019 | -49.25694 | 2026-08-03 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca0b80d4-b9af-3148-bd7b-e5ef7c5da214 | -6.4368 | -47.98058 | 2026-08-03 04:38:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf5019f9-fa6d-3767-a7dc-5dc3eb0037f6 | -10.5715 | -46.79413 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6322fe7-06bc-3a51-8772-5a59d97990ba | -7.56448 | -45.11345 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf218c0e-787b-3df1-ba5a-ae66d8e25421 | -8.34366 | -45.98303 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd3069ad-6135-3853-a31e-b3037913f7af | -5.3471 | -41.00151 | 2026-08-03 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 285c76ca-b915-3974-aeca-e52316baff44 | -2.95952 | -50.34814 | 2026-08-03 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7756155a-add2-366e-997e-69869aa4fc15 | -10.62093 | -46.81757 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68acae76-0c1d-3dc7-a933-a8cfa2f18133 | -9.95156 | -46.20351 | 2026-08-03 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af473036-62ee-3df8-be64-16d16b81bd62 | -6.96118 | -52.81533 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98a5706c-0de7-3abc-bb2e-b59f0817e7e4 | -6.91417 | -44.005 | 2026-08-03 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c44b9d7-fa50-3d11-a372-82e4b1205976 | -6.54738 | -41.83 | 2026-08-03 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e996e0de-814e-3ed8-b944-8a267ab6c1c8 | -8.17687 | -49.19573 | 2026-08-03 04:38:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef1838a3-0fd4-308a-8de4-0570d5ccc475 | -6.06962 | -49.2605 | 2026-08-03 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5817b87b-5ac3-33df-a1c0-a3879d88f68d | -6.55038 | -55.16607 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4b5dbd5c-9e63-3e1f-957d-54e22b5cb07a | -6.29851 | -44.88292 | 2026-08-03 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 935684aa-0cf8-3edd-8a08-0ce674451138 | -2.81776 | -52.29333 | 2026-08-03 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a90ab55b-3583-3704-ad6e-993c9f898431 | -7.01149 | -47.97613 | 2026-08-03 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80c1a1b7-d379-3a13-8938-2329639e8da7 | -7.32021 | -42.9901 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0e3c18c-2716-3128-b84e-6157146c5e7f | -6.29492 | -44.88233 | 2026-08-03 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e21c54d-e3c4-3331-b40b-38d265d1554f | -7.1761 | -42.33899 | 2026-08-03 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6126d0a-922b-38bb-b57f-da3f95b76486 | -7.55333 | -45.06441 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea2fd165-8bbd-3e8d-bd12-9cd13a987b72 | -4.26847 | -48.1958 | 2026-08-03 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a74cd5ae-3a5a-3cb2-93fc-45d58c1ad80f | -6.55968 | -56.53137 | 2026-08-03 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a1a94d-d1c5-38b7-b57f-8d34251c1163 | -7.96236 | -44.92617 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98d9c23f-c178-397d-a512-49691b66cdc6 | -3.65762 | -49.18714 | 2026-08-03 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a5bbf15-a8c2-3f6a-8755-83b9d81191b7 | -10.57611 | -46.787 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fb7ab16-4fc0-3693-bde1-4aa30d6a4d55 | -10.57266 | -46.78645 | 2026-08-03 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88d99a41-9452-3442-abf6-48e2cfe2952a | -6.555 | -55.1669 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bf176d83-5761-3e7b-9752-04dffc9df535 | -6.43404 | -47.97661 | 2026-08-03 04:38:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc71a2cf-f0e3-320b-ad31-ea247a7b6147 | -6.55896 | -55.16537 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d56eff2e-3708-3505-9b53-c63656731972 | -8.35354 | -45.98856 | 2026-08-03 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf299f9f-0fab-3f65-ba9f-7b1bcbe4696f | -7.9587 | -44.92561 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8a5b87a-beba-3988-b66a-44b099abeca3 | -7.56088 | -45.11283 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36299050-b5d9-31a7-b136-21e9f214f2a2 | -6.30211 | -44.8835 | 2026-08-03 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff67ac13-0c69-3534-87d9-7335fcd4ab8d | -6.55662 | -55.15722 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36cf2aa0-711d-3f58-9e5d-bf94c77ae4bd | -7.24813 | -59.44616 | 2026-08-03 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02d04686-8c64-3b82-a6a9-0c4da73e7447 | -7.96302 | -44.92186 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6c89870-59c2-3e46-9f48-6f8fe0976273 | -6.96031 | -52.82045 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7598109-4048-3c13-a1fa-a1a4cb83e971 | -7.02828 | -42.88544 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee9885e4-aa62-31c5-b692-b0e368498ac8 | -5.20314 | -46.09259 | 2026-08-03 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adc07b52-3b15-37e3-b967-28ec4fbd76c1 | -7.11382 | -46.71445 | 2026-08-03 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00caa447-630c-3b1d-a244-9c0c95038684 | -7.22761 | -43.52312 | 2026-08-03 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f5145379-01de-38f6-99c2-f7ef4ab8ba59 | -7.96799 | -44.91379 | 2026-08-03 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7af6628-6f87-3539-a95f-a31ba7ba477c | -7.35792 | -43.85602 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 757c239a-5132-3e9f-b809-940bf6f68e9b | -6.85637 | -44.8016 | 2026-08-03 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75ee702a-3b6f-3376-8e27-ece1b3208acb | -2.81374 | -52.29259 | 2026-08-03 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b8170a8-7330-3a82-bff4-2fa74fa719d4 | -7.35719 | -43.86084 | 2026-08-03 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78e818ee-2484-30ef-a034-45051328bc2a | -6.90505 | -43.72497 | 2026-08-03 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f67e396c-86ea-3022-8ec2-0f4d452bc919 | -6.54576 | -55.16523 | 2026-08-03 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7520e681-a4cc-3f20-9097-4c413e4e11ce | -7.73429 | -47.63457 | 2026-08-03 04:38:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf2b76aa-3e62-3745-97fc-2f80dd229500 | -7.20387 | -42.96207 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75ad5e2a-9f82-3344-9774-477854dd29ae | -3.58163 | -50.26136 | 2026-08-03 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e90e11-afb4-323b-ba9a-1668b6529e6a | -7.55979 | -45.09543 | 2026-08-03 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 97c1697d-3378-3a22-aab0-e90ebec0b4bb | -7.03292 | -42.88234 | 2026-08-03 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c2d4a1c-ff0b-3567-984f-002c201984bb | -6.03581 | -40.32617 | 2026-08-03 04:38:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
