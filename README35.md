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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb808a2-8cdd-3362-9d0f-2dd1d71736f4 | -10.89902 | -50.27789 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 692014ee-2497-35e7-b529-fe192b3b7bc7 | -4.78105 | -47.17723 | 2026-08-20 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a80aeffd-7ad2-319e-8ed3-cf895f749f99 | -8.50198 | -54.86789 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09c19606-0fc4-3c92-96cc-af9053cc2548 | -10.48344 | -50.32003 | 2026-08-20 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 478cebda-a4ce-359d-beea-8d51499530ee | -10.25519 | -47.00157 | 2026-08-20 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6469b3f2-2a57-3083-adcb-8eecad2d45ed | -6.4407 | -52.72641 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ab85b7-78a1-37ed-b3a8-dcedc5c23f50 | -7.74926 | -49.46811 | 2026-08-20 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf2e3a5c-b2f2-3d86-a4b5-6c6422c35357 | -8.51033 | -54.86725 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2ababb8-8f23-3368-8577-f5c859ac1669 | -8.66677 | -54.65645 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 311826d1-c54c-3463-b021-d01c660c064d | -6.37861 | -54.9427 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fde659e-30a5-3e8d-9232-61e2031b39c8 | -6.43926 | -52.76555 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43decdc6-5038-3f89-bf9f-2a90bb0b22fb | -7.59917 | -45.17258 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb70f2c0-c13b-3d10-8ab4-5158c3f782b3 | -8.46524 | -46.95548 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3da500a5-0eb8-375e-9707-94f892ab84d8 | -6.95227 | -52.80723 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1d9e58b-26d4-3165-aecb-42d6809b3fb7 | -7.95735 | -46.92071 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79a12963-1d3a-3160-900d-ed509a398f28 | -8.66458 | -54.59299 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14ab3394-68e1-36a4-8017-9cfb163eebd5 | -8.67399 | -54.63938 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 874c5a84-b3db-35d5-a0c6-b3497839aae3 | -6.95168 | -52.81063 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64142128-1f4d-3ec0-b990-c62418d3c917 | -6.3777 | -54.94766 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33e5b834-4f52-3284-9200-3eaaaa8c0469 | -8.57099 | -54.67836 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27dad45d-5ed8-3b3b-8dc2-befb2ac0e680 | -10.81045 | -50.28896 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b4c81b0-4690-30b2-9bdf-f188c4223c89 | -6.44592 | -52.7596 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 748b6f41-fd3e-3877-a436-cd6814d7b1e1 | -8.5718 | -54.67411 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 091b10ce-4eae-38db-8012-595169024578 | -6.73672 | -44.66837 | 2026-08-20 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f661bf53-6e1e-335a-ad18-749631a4539e | -12.25676 | -43.15832 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c17c70a4-17dc-35aa-a706-76835b219671 | -11.34761 | -45.98058 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64cd3d89-4930-34de-85b4-dc26dffb64ee | -8.56047 | -54.76634 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f6ec6e6-44ac-30d4-8af6-d41548182bce | -11.43227 | -47.24932 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00ffc3f0-7988-3f02-9ef4-9555fbc82bf8 | -7.5397 | -55.58277 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 758d6cde-3245-37aa-803f-42c075adcff1 | -8.56 | -54.67174 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c871e16-d0ea-3615-bf86-eef6fa441482 | -9.50161 | -51.68001 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5aea5683-21a1-3893-8437-2f5675a23cdc | -11.80793 | -44.80928 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46a69217-56e3-38fa-9216-909d36a273c1 | -11.46606 | -46.56466 | 2026-08-20 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faf6d6f5-e800-3668-a95c-72bf8efc8aa8 | -6.78009 | -42.88051 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b187e537-b67e-3afc-b8f6-39a298c4fed7 | -10.83102 | -50.29696 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e3252af-802e-3eb5-b873-bb24fd522d48 | -6.73789 | -44.66114 | 2026-08-20 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 449d2010-2e49-30df-afa8-9f9b0ad62a3d | -6.2657 | -43.278 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffe5bbf4-29f0-3087-9160-79c3e9514107 | -12.25696 | -43.16537 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ef718e7-2417-389e-b3d0-e25180475b7f | -7.01354 | -47.97245 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16b41b3d-8293-3ba9-8a7d-08fac48a7592 | -7.01265 | -47.97484 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2136ef51-1e9b-38bf-af2a-c0b25d79b2a9 | -8.66993 | -54.66069 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aeb049e-7a05-30a5-a3c8-c23230ab80c0 | -7.02322 | -45.89058 | 2026-08-20 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6858d03-a8d4-33d1-a059-b30e9e6a744b | -6.78286 | -42.8845 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 14c06f9e-2b20-3a76-bca3-3a580d2fcb04 | -8.52997 | -54.86185 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c729d97-3018-3982-9643-61e69c97b1e1 | -9.49771 | -51.67419 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37f525fb-5eb2-3310-8946-9e0609fd32ed | -7.18195 | -43.11115 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb22f498-ee3b-376d-9a55-fc8028c3fb67 | -6.39012 | -54.95023 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2faaf7d9-b5d8-359d-b5f2-7c10a0572f10 | -7.49141 | -43.81792 | 2026-08-20 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e7c8662-c1a1-3790-a5c2-45f28172ff90 | -8.1011 | -51.67165 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efeb7826-65b5-3499-b028-4d48826a94da | -6.51716 | -43.61937 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee3ebca-de86-324e-b6f8-b2e057768c8e | -6.9537 | -52.81069 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5cd226b-7700-36aa-b24c-c2df8e78015e | -12.37861 | -46.45636 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81030ccc-9331-3391-9dca-292441f02c1f | -10.7427 | -50.35726 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d796a60-9341-3f2f-8b51-5d393ccfbce1 | -8.6727 | -54.6492 | 2026-08-20 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| cab3b9d2-42a9-3816-b268-738d8cac728a | -8.6729 | -54.629 | 2026-08-20 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5a7b2643-6e1c-3e33-b275-09bb390099e0 | -8.654 | -54.6505 | 2026-08-20 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba088b24-4ceb-3a17-91e0-2c94f5952b39 | -14.44137 | -45.61568 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e3d153d-dcea-3178-8731-db7e3031488b | -13.26934 | -51.63533 | 2026-08-20 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c8b5265-efb6-3f63-908e-32a0cc682d2c | -12.80462 | -48.45076 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2aeada9-8b31-3fbd-9493-610aabc67d89 | -14.73 | -47.15867 | 2026-08-20 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 684ec437-b8b6-396a-9be7-ab58e4469cd8 | -11.22477 | -55.05236 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b94c283-a484-34a2-b721-3a9aa199d71c | -19.7136 | -46.22944 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e3ca9f6-f73c-3130-9e9e-448f4484275d | -18.79268 | -48.55394 | 2026-08-20 04:21:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31b8f9d6-b4c3-34da-9b7d-5e29d3a7c659 | -11.19438 | -54.00336 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 971d391e-035f-383a-8ad4-c8ba590d736a | -14.44742 | -45.62037 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63550887-f973-3c11-ac1a-9fd97436f7b9 | -11.21598 | -54.00783 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e3596c4-9b93-38f0-a404-5b9cb3773c30 | -14.45131 | -45.61737 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9bdec9a0-019b-30f3-892b-84f8a5793960 | -15.71118 | -47.79915 | 2026-08-20 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a81b85d-698a-3401-aa8e-c9f0c49140db | -15.35059 | -49.65998 | 2026-08-20 04:21:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be92b8ca-b640-33ad-a60f-d082e0c6c50f | -19.24075 | -42.19537 | 2026-08-20 04:21:00 | NOAA-20 | IAPU | MINAS GERAIS | Brasil | 3129301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 8c56ae2c-bf54-3166-804b-4ffb17bccae9 | -13.54718 | -52.22672 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5aff176f-47e8-3f05-8c52-b93cad45f471 | -12.80094 | -48.44999 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55837c77-27ec-3ee8-917e-022d824b5a45 | -14.97373 | -46.59273 | 2026-08-20 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59d1189d-a4dc-36ee-b558-7482c591b144 | -12.81143 | -48.42553 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71d0f083-755e-3aa0-892f-1678bacb6a34 | -14.23087 | -51.92615 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1185aebc-4a57-38fe-90ed-1cac0744d965 | -14.20385 | -52.88795 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a95d7e2-a1b1-33f1-b8b9-2ac0e324ecec | -18.55372 | -48.2908 | 2026-08-20 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fb99a49-4729-3cd0-8df6-0ada0760d47a | -15.71559 | -53.78151 | 2026-08-20 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0292a1a4-d900-3d1c-b1e0-ebda90c91085 | -13.78374 | -43.17848 | 2026-08-20 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb3157c7-cba6-371a-b6a2-97a3af46e1d7 | -11.41321 | -54.31596 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c107dc48-dfec-37b5-ba49-b10f979f3f66 | -16.07958 | -54.97926 | 2026-08-20 04:21:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c01edf-1aac-399c-8f6e-3432cc24cc59 | -12.81881 | -48.42681 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3eb946a4-0886-30c1-bca6-512380691ca0 | -14.3146 | -51.91072 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7f6c10a4-1aaf-33ff-b2e6-852227c18c26 | -14.01731 | -53.66028 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7c7b21d-b9ab-3f95-862f-bac0f7a9e950 | -14.31907 | -51.91154 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ea92b061-b36b-3e96-8f77-d868001e3f32 | -13.63191 | -51.77501 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd2fb43f-69fd-3b51-950b-4ef6e0c0cdea | -12.76951 | -48.41139 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dd4326c-6d68-3f1f-afba-64f4558f1ffc | -19.71427 | -49.14544 | 2026-08-20 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac44046f-3d4e-3e7d-bff2-cd70e07d6c23 | -11.21979 | -55.04712 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d54058d-64e9-3f50-8f64-080d112c79b7 | -14.45245 | -45.61024 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da23c1a-9660-3664-8c77-0ee49857be0d | -15.5881 | -43.74095 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b215c596-4db5-3b79-a2bf-4adb530322a3 | -12.76476 | -48.46117 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38646bd9-1ec2-3dcd-907a-1621ed18b803 | -11.2045 | -54.00918 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9af2ad6f-f254-3c23-bd06-8887ddbe3203 | -12.81261 | -48.44045 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e528fd4f-a9ae-33db-918d-1fb3d7c308d5 | -15.3803 | -52.72804 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0340f22c-318a-357e-897b-8b74865d4790 | -17.94058 | -44.4058 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28b32f6c-4a37-3ce9-9091-e0f5ffe85e20 | -11.41288 | -54.3152 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbffc7c1-2f16-3adb-ba70-e70060328688 | -11.41912 | -54.31253 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a869aec6-e741-3e6d-9c09-6f18fcc03e2f | -14.45188 | -45.6138 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d110b77a-55ee-36f8-a343-e8e36f4a741b | -15.2167 | -52.81276 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README36.md)
