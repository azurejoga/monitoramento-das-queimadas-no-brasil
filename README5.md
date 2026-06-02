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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe2161b6-2269-388e-87d3-b2a480c9e438 | -11.21996 | -53.8264 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18a71021-ae48-3acb-a21c-53b7011cad6a | -12.01708 | -49.27537 | 2026-06-02 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 149ae361-5547-3b99-a4a8-739d227e245d | -12.17789 | -54.54416 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b11297-a29a-34f5-8a09-6da51e7afd10 | -12.55357 | -57.18174 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d52f8411-8144-3b0f-8c46-6fa03e378759 | -11.61685 | -55.18055 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2890f5b9-c5cf-32da-9c6c-6ab125584328 | -11.87914 | -61.04802 | 2026-06-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae73f1b-9867-3399-bcca-3a7e7ee4a593 | -12.18198 | -54.54089 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ad92323-88ff-3df5-8f9c-7d1e46cddeb6 | -11.61755 | -55.17641 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e91d69ef-72e0-396a-855b-9040075a3c4c | -11.61972 | -55.1853 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84f6a2e2-dc8e-3293-a7cd-06250da7803b | -12.30458 | -57.40945 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4bc6442-61fe-3e74-a86a-75eb2917ea28 | -11.97005 | -47.37167 | 2026-06-02 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa206176-d3dc-324d-80a2-9caffd1d53ae | -11.62899 | -56.85863 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3a5fb12-90b9-398a-a2c6-3da90f0f094a | -16.15737 | -58.47224 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ed44ca53-0a85-32d7-8d80-a3c52f15dccc | -12.29781 | -57.40078 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e2e52e0-7c98-39f1-8267-ea367b75abb3 | -12.29718 | -57.4044 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca6b5bb-3f1b-3d1a-b1df-8951264546e9 | -11.88185 | -61.04447 | 2026-06-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab2002dc-693f-3dda-aab9-2afd6b29ba46 | -14.18752 | -52.8769 | 2026-06-02 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1b8d598-c8c5-3450-88b4-32bec2748fc6 | -14.7633 | -52.67415 | 2026-06-02 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55709ef4-d133-3fb9-92e6-268938072380 | -13.98379 | -53.85852 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0859acdf-2902-36af-a371-3ce64df76965 | -11.32752 | -51.40413 | 2026-06-02 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6acd528b-ae41-3427-95ff-4c51e6fb5062 | -10.03701 | -59.34752 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f85bae67-4c61-3549-96ec-d20e26447b77 | -13.98205 | -53.86942 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24e59294-0b44-3d2d-97bd-0934d42213e2 | -12.45397 | -46.52908 | 2026-06-02 04:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed4c53b-cc34-3026-8eb9-aff9a328e1ed | -14.07817 | -58.13962 | 2026-06-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53c47668-0a32-3a2f-86f3-cbc68147ca42 | -11.62282 | -55.17376 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32a79d22-b6b5-3915-a957-7e758cc21fbe | -11.97075 | -47.3665 | 2026-06-02 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 714ac462-84c7-38e5-92e4-72a47b9a2738 | -11.62214 | -55.17791 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3acab3c-c583-330f-b0e8-0ef01be2134c | -14.8615 | -56.54757 | 2026-06-02 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf773e84-c680-3ff1-bcd1-96120e3b3c69 | -16.91488 | -53.62112 | 2026-06-02 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ec633e-8128-312b-84bd-29debf1dba2e | -11.66538 | -54.58431 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 015660aa-e8ea-3750-a8f6-a3b78914244a | -12.17444 | -54.54358 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 790ce724-2aa2-3ec2-9a25-83f087166eef | -10.04302 | -60.43692 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b37f7c9e-0cc6-3530-9e30-9547fb0a0fb3 | -11.47431 | -57.10104 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ffeb4d8-58b0-387c-bcf2-17d30073d23e | -14.08276 | -53.38779 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa368354-a35d-3918-b878-42ce5c59d871 | -14.19082 | -52.87744 | 2026-06-02 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54e20a38-c15f-3007-ad74-975bbc219cf2 | -11.28417 | -57.87151 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c453931c-ca48-3752-be45-7abb5fe6048c | -11.6235 | -55.16963 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaae8a93-5c3c-37e2-9f05-000d36533c1c | -11.62042 | -55.18115 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b293c98-0f8b-3307-bc01-35cabb7ce75d | -14.76605 | -52.67823 | 2026-06-02 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9669fd-0f7e-3d19-975b-67a23ce6df33 | -11.64769 | -52.86131 | 2026-06-02 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a35256f3-0230-36b2-89d8-5f2af0deb3c6 | -12.54963 | -57.18098 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5879ecab-b48c-3ce7-a0df-0dcfee994b05 | -11.99858 | -47.76618 | 2026-06-02 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e547a263-f2ea-3b9f-b3ae-d88c96abbfa0 | -11.62146 | -55.18206 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d794ba76-bbcc-393a-aa36-93efd435b3a7 | -12.55053 | -57.17582 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbf187ae-8d12-3fda-9017-fc2aa25bac44 | -12.1713 | -59.75473 | 2026-06-02 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb1be8be-4429-3b76-b77c-44a17b6ba74e | -11.6254 | -55.17348 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd56ba5f-308b-3353-a37c-f71df3e6e285 | -11.57192 | -54.57724 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f18107ed-91c9-3806-ba0e-0e811f26818e | -10.028 | -59.34781 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 886e5ff1-3854-306c-a838-73e391b764df | -11.62687 | -55.18651 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f66558dc-1b7f-31ba-a096-cc85c349f7e0 | -10.03226 | -59.34666 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b1eaabf-5a04-3868-a73d-00aae78f9a55 | -11.6247 | -55.17761 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1537ac4c-026a-3e31-b31b-36189c669613 | -16.15803 | -58.46856 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4183bdbd-c6ef-3ffd-a296-78a6fe21df62 | -12.26311 | -48.80587 | 2026-06-02 04:49:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ba8d00c-fc15-316b-ae3d-7714eef9289e | -10.04057 | -60.43419 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bb6365a-e244-3d3b-b82c-e995322024c2 | -12.05395 | -48.08025 | 2026-06-02 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89488b7-b158-3bf6-b2a7-c53ef0704e5f | -11.88104 | -57.8441 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 898e209a-113a-3625-b928-51c36b1db8a2 | -13.95854 | -46.1884 | 2026-06-02 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42e00942-c4c7-3cd7-9d21-a193ef7e5ee4 | -11.32475 | -51.40009 | 2026-06-02 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ed3afe7-a7a0-3af9-b191-cbe85dfc7348 | -10.85562 | -53.7513 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e25c8fe-42bb-3fc9-b627-3b082cbce809 | -10.87633 | -53.73598 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a356c4c7-210b-3554-8465-b268502b7871 | -12.17162 | -54.53913 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5d2a4ad-0ec2-3b99-b40a-a6e73440991c | -12.30119 | -57.40513 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11b2b979-2668-3a3e-b1d1-e4f983604033 | -11.62329 | -55.1859 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa039e55-bece-338d-bbc6-c02260df849d | -11.61431 | -55.18085 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c5e8eb-0903-3326-b800-15ba51dc17e8 | -14.07409 | -58.13884 | 2026-06-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3de5d698-0103-30dc-b2d2-7684d3359d3f | -12.30315 | -47.90699 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543d3852-420c-329a-a164-5a748b774929 | -14.7622 | -52.68124 | 2026-06-02 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faab9238-1c08-3372-8eea-07eef68202ad | -12.73524 | -54.19084 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98c65ddc-927c-37d3-ac7b-b788eba24f85 | -12.17098 | -54.54299 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb14349b-1608-3f8e-af85-f93c6371dcca | -10.56909 | -57.32506 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb546292-a415-379f-a5dd-bc9eb122d140 | -11.79069 | -57.01937 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cada0840-49b2-3002-b492-ca592e15bcd9 | -11.63254 | -55.17469 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 54135734-33cc-3abb-bc75-4fa9fb1b94e8 | -11.62112 | -55.17701 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 456ccda6-3402-3950-8a47-73e03badb26b | -14.76274 | -52.67769 | 2026-06-02 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d56d5d42-3870-312a-8af3-47f102037822 | -14.18696 | -52.88044 | 2026-06-02 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0310e0ed-d7eb-3a55-a293-064ce355ef88 | -12.00007 | -47.76812 | 2026-06-02 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dba2723-81b6-30bf-82d1-42a9b50999c6 | -12.05358 | -48.0827 | 2026-06-02 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd18a714-1e45-3d3f-93da-af68792f0d5d | -11.88064 | -61.05076 | 2026-06-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d9a67a8-3ea3-38c4-8a6b-376f837ddfbb | -11.93745 | -49.30229 | 2026-06-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40f62621-9b0b-377e-8307-bfab14c728d0 | -12.17508 | -54.53972 | 2026-06-02 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f66a9b-86c3-3c73-a776-1d8d1fb7eb00 | -11.4737 | -57.10457 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8cc1ee6-117b-3d24-9e7e-d2e6acd713e6 | -11.624 | -55.18176 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bae65ae-b33c-3781-8dd7-6f05f5edbd0a | -10.87557 | -53.7356 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ab84ead-b182-3f5a-90a2-d42dcc53a585 | -12.3021 | -47.90358 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ca7ce6e-4cae-3d0e-8c1e-ecccc5394832 | -16.15811 | -58.49141 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e139c268-4b6d-35c3-b0c4-250f6efc2ed0 | -11.87611 | -61.0466 | 2026-06-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37eb1d8d-e81c-346c-89df-5b159389dcf5 | -11.32806 | -51.40061 | 2026-06-02 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21cd3c8c-d39c-3803-b6b6-78d733e1288c | -11.27147 | -53.96158 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e4c9571-5ceb-3446-b3f6-5bb918660c45 | -11.4777 | -57.10522 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc74d7a-0301-3c49-b507-7016ecbd51a1 | -11.62967 | -55.16996 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfaaccb8-6476-3e27-b89f-4a2d40d95176 | -12.54659 | -57.17507 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3f900e2-ea80-3fdb-a0b1-1d559d60090f | -10.57255 | -57.32956 | 2026-06-02 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7658e7db-b10e-3313-b2c9-9fe3626e2300 | -14.07945 | -53.38725 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c95928f9-72a0-3804-bdad-8389966a5f62 | -13.99324 | -53.86385 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52cec3b4-50c9-31ca-bbae-f60faef903bb | -11.57127 | -54.58119 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e48b017-8bfa-39f7-bc50-fabce37628b3 | -11.61789 | -55.18146 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 32f3e96a-d471-389f-b7e2-a6399645f16d | -12.2993 | -47.9065 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 225b45c1-3dc2-3508-83f8-7d3237b03464 | -12.28962 | -52.50415 | 2026-06-02 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31092806-b21b-3976-940f-c28857540561 | -12.01352 | -49.27485 | 2026-06-02 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7da86e38-507c-3078-9bfa-4d8e57ac350d | -11.62609 | -55.16935 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
