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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63c43b2e-b23b-34ae-8782-56af3d617772 | -8.96236 | -47.97432 | 2025-06-18 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf37fe96-3f43-3d9e-be23-23f6e1cdd420 | -7.18922 | -43.20398 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d949b2f3-cb2f-38dd-bc14-5bdba36ac61d | -17.68104 | -47.85872 | 2025-06-18 04:17:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e8cb31f-4be8-305a-8bf0-0e2d569ca91c | -6.1235 | -42.53369 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 70e3a614-faf9-3ed1-a128-cc627a496e96 | -7.30471 | -44.3955 | 2025-06-18 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cdca64c-35fe-3cf5-9ac6-c22bc7ea7fcf | -6.67548 | -43.21888 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| be82859f-bb76-3f31-b1a4-11466e455bbc | -9.40764 | -48.42113 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3966dcbf-ced3-3208-93db-53e349ae12cc | -8.07691 | -43.10883 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d2816aa2-0a0f-3537-8ffd-28b4485eb0f8 | -11.64172 | -54.14265 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e4823ec-1ea6-3962-a189-2630c5921f95 | -11.13624 | -53.94001 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 97a1cc0a-0eb5-30c6-ab6b-99452b306e51 | -10.98486 | -45.1024 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f00fd2c-25cc-3514-8d11-970b90b4ac20 | -16.65708 | -45.4952 | 2025-06-18 04:17:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68945ac8-a7b0-3dea-8050-85e0ae561d06 | -11.79388 | -43.79108 | 2025-06-18 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23340c9c-3fcd-33ed-aa9b-dae21d63030b | -10.63154 | -49.42563 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c450b70c-bebb-3da1-8f2d-ae12240635ee | -6.03621 | -44.05145 | 2025-06-18 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cab9d51-bd1d-32fc-a204-e6563bfd7680 | -9.32336 | -47.83086 | 2025-06-18 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cd7cce1-9669-3530-9177-44207493b2dd | -11.92872 | -44.55082 | 2025-06-18 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ec948e-bec7-36a5-ad8d-623984f87a0b | -9.50985 | -55.96571 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9e62146-c31a-3c7a-8c67-9720948b1b37 | -7.48525 | -49.58124 | 2025-06-18 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d4faf0-8fd0-3597-aeef-24b272909e37 | -9.88707 | -47.81238 | 2025-06-18 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8afb33f0-ba63-3464-91f7-4610e900c2b7 | -8.72122 | -49.02837 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c55a696-453e-3898-9203-d7b5a269bf94 | -6.67044 | -43.18607 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f479ecc-9106-3b27-92f8-182bb2c1dc6b | -6.61424 | -41.77594 | 2025-06-18 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 219b1855-79d1-3cf2-98dd-dad66ebeac6b | -7.00394 | -44.07166 | 2025-06-18 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05b5d51e-e91c-3b5d-b633-79138c5e75c8 | -10.63565 | -49.42633 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98b85f8e-a4b8-3575-ad29-548c59c080c4 | -11.13217 | -53.93163 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7c38f2b7-7911-3457-be75-ff7dd3de646f | -6.67099 | -43.1826 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15e4e6df-ea74-3746-9965-d8e6e07d1942 | -11.13006 | -53.94263 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9ad9c8a1-bed8-3004-bbe3-3f0424b897d5 | -11.33862 | -45.21124 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5747337-248b-30ee-aaa5-2f6242bc533c | -11.57825 | -44.84208 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0be410e-27ca-3580-a6bb-bffb9004f515 | -6.12738 | -42.53072 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 78745852-edb3-3e9c-a1ab-4795dc37f68d | -8.72945 | -49.02983 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cccb6445-8536-3769-808e-ee489959fb4d | -9.96594 | -47.9424 | 2025-06-18 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b78556a9-e876-3c18-a139-51c5366060a8 | -8.72727 | -49.02836 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d7910b4-cb23-3cd5-ac03-751a57bdabda | -10.3583 | -57.24209 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9927e44a-34fd-3b7b-a6f8-3daf65b49149 | -7.5461 | -45.65598 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 771a8492-4ed7-369d-982f-8fcf74501cd2 | -6.41208 | -44.79984 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c000bd3-78cf-31f6-a61b-69574ca5f76e | -16.31196 | -58.24726 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c0f886d7-4892-33d2-b369-58f91c203f4b | -10.59299 | -49.46455 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fda4c223-2214-3e34-87cc-f939509cabe7 | -10.91999 | -56.85089 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52d2a8e0-8a46-3c3a-8d58-6488e750300a | -8.72596 | -49.0254 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f74bdc3b-c0a5-3912-b2e6-9715748962ce | -11.57082 | -44.6741 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a31f584-e753-3bae-bc5d-9d0584f2ffe0 | -6.03956 | -44.05198 | 2025-06-18 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58177e16-e2a0-3a10-94f6-388b07ed903a | -8.72246 | -49.02098 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d332c752-e41d-3b33-8395-5ee3d5709a22 | -8.07636 | -43.11232 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c970fc86-07b9-3dd1-9a01-1077b1528ceb | -10.65958 | -49.36227 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80830c42-27b8-3c28-854f-41d370ba0aba | -11.64241 | -54.13905 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 064580e9-3981-35a5-ad4f-c145a6fc0dd8 | -5.61326 | -45.97913 | 2025-06-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dba75a9f-de4b-3baa-9056-9b8b3d8d35e5 | -8.07358 | -43.10831 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88c9571d-ff88-3fec-9aec-8ecd4c67a2b3 | -7.44001 | -44.90377 | 2025-06-18 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 379084f3-bede-364a-8c47-dc06c9c4af55 | -16.65375 | -45.49464 | 2025-06-18 04:17:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a55f0072-7327-31d6-a138-f100c06ebbf8 | -11.9099 | -44.17936 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed67e55e-52c8-3371-8a28-cc7053003335 | -6.94781 | -47.26627 | 2025-06-18 04:17:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74fc0620-c1f1-3e55-a029-b7d104d28c92 | -11.66686 | -44.62077 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5794353-c058-3c3b-8667-1e2eeac0283c | -8.55153 | -44.98803 | 2025-06-18 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9be8be4e-d244-3ef6-8348-6425723c7350 | -6.74487 | -44.01616 | 2025-06-18 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f600ba65-a957-3bec-a112-fab8b448c517 | -18.52906 | -48.96765 | 2025-06-18 04:17:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40c56299-f33b-38ee-870a-18fee8e37e5b | -6.50456 | -43.63706 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9453faba-2285-3717-bd2a-81981b405a09 | -16.78614 | -49.11251 | 2025-06-18 04:17:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0c4bc27-7754-36ef-9a44-2dd77b2cf383 | -7.23271 | -43.09695 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ae4c38b0-2e7e-39db-8df5-65a4af5d4f07 | -10.59362 | -49.46083 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cffcd56a-333d-3888-a8fe-89e167eecc85 | -7.16353 | -43.47073 | 2025-06-18 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f796217-b2fe-349a-bfa2-9dacd278d818 | -8.22523 | -46.09665 | 2025-06-18 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05d63090-a245-3a53-bb81-b3d44bfe8f43 | -7.54734 | -45.64829 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb609e06-ab8e-3da1-8f65-6cd352250727 | -5.91573 | -43.44741 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a420918b-308a-338c-9eb1-f4bc6ae237ea | -10.98936 | -45.09579 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98dc4f5f-4fa3-30b3-a4bc-434430d6753e | -7.54672 | -45.65214 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66249d2b-86d6-3e12-9d34-e28c84603378 | -11.07472 | -55.05346 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecbf9ea2-aaec-33ab-bc4a-4bd8b4d2c488 | -6.33895 | -43.74628 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 069db02a-9321-36f6-a73e-cfdc5baa237f | -11.13076 | -53.939 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9a629e9b-3903-3fb0-9bd2-0bd21a188dca | -10.65196 | -44.49583 | 2025-06-18 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d98bb360-1350-35ba-baf7-04fe8aa8d008 | -7.21302 | -43.22207 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d2e9262-475f-320f-9d35-366ca2e6ff70 | -5.91241 | -43.44689 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| afee418c-f088-34b5-95d8-9c75de6bda81 | -8.67447 | -51.46317 | 2025-06-18 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac6607bd-a219-39f4-8db1-65a7b19a1783 | -10.72871 | -49.56157 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d9a262f-fa4d-398a-a1ba-2901e923bc0d | -6.12962 | -42.53823 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 011f99a5-74d9-3239-9474-1848f54db4d7 | -9.4928 | -56.09125 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1e3d8400-b6b7-370b-bfb0-783545a26a4f | -12.20727 | -49.65529 | 2025-06-18 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffe8cfa8-eabf-3ebe-85f2-ae1d96b807ab | -8.07025 | -43.10778 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0617b2e6-cca1-3fc3-9405-1a909b9a049d | -11.97038 | -49.51093 | 2025-06-18 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c9de355-4d28-3490-b0f1-ddd8d31c7312 | -11.14242 | -53.9374 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 96a9e7a0-4c7f-3afa-a61e-1defa64b951f | -6.13672 | -42.97013 | 2025-06-18 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa8efba8-aad0-396a-acb4-d2e839887dc0 | -9.87959 | -47.81087 | 2025-06-18 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe27a342-5c06-37b6-8f89-9d74c2b77972 | -15.99341 | -49.82227 | 2025-06-18 04:17:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1edad8c-6c30-3ca3-b30c-c5082d6ea3e4 | -6.61085 | -41.77543 | 2025-06-18 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1003f972-206b-3735-90a6-677806823a61 | -7.20908 | -43.592 | 2025-06-18 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0551fe-8cff-38ab-9bbb-ccb6f9d12a48 | -9.82113 | -47.15588 | 2025-06-18 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a71ea3b7-3871-3691-a905-e6e7ed9f4b15 | -10.93186 | -56.84727 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64bee8b1-956a-3039-8821-198f69f08ee9 | -10.86397 | -53.76468 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de2b028a-b4b2-3f93-8c26-d5523fd4d68c | -6.65993 | -43.18797 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a12778b7-41cb-3f3e-9caa-b07684f59cb4 | -6.65749 | -43.1877 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6e82d764-56d8-3a17-abad-85554fd10540 | -7.54547 | -45.65983 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b36763-b5d4-3554-bcaa-6f6e86c8b290 | -7.20746 | -43.21407 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd64a992-da63-3da4-a0be-bc59bd6b2152 | -6.12683 | -42.53421 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f2ae18e-544d-3d27-a41f-c39a516e233e | -8.24555 | -46.3903 | 2025-06-18 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d501961-deee-3170-9bc5-c583b64a85dc | -11.22016 | -50.77822 | 2025-06-18 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 955da689-895d-3e40-b1fe-2771b9fd8126 | -9.48745 | -56.08454 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f8317a4c-4321-339c-951a-25774e474534 | -6.14005 | -42.97065 | 2025-06-18 04:17:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07554325-87b3-3d5e-be20-a47788d26a24 | -11.66354 | -44.62022 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aab1cd2-70fb-3c1f-bf23-62afd5bc656c | -6.68978 | -43.6841 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
