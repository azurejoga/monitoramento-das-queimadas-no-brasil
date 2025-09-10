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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe1ecd07-1177-303e-94e9-c828dfba911e | -8.86001 | -47.27625 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 551c0f40-572f-37ee-aa64-565ef5136e6d | -10.02741 | -51.66452 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c63b04-99ef-3d5c-8033-1db5282e7aeb | -7.76274 | -50.76295 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d00a144-79d8-3131-80ce-06dcce831fc9 | -7.35988 | -44.30751 | 2025-09-10 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f5e1cf3-4c25-3ad2-846f-89542c922106 | -8.34125 | -44.84064 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 008905a8-4053-3e2f-827e-e8d2ddcbbd74 | -11.25994 | -50.64325 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab60870-a841-31fd-899e-0ed1ffbfcc0d | -6.84832 | -44.91391 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da75643c-a7b1-3920-9661-3f23951d9b3b | -11.44759 | -43.62644 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08d0f2d4-61e1-3824-bd31-7deaf481c051 | -10.84283 | -47.75474 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48bad372-3f29-31b6-a606-4d0922ec82a3 | -8.78166 | -44.40643 | 2025-09-10 04:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a1372e80-5662-334f-b66d-5e9a68a7d836 | -9.56664 | -48.01242 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| add27157-26c1-3897-9ade-8bba8b08d686 | -9.74658 | -51.09053 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61d5a6dc-466d-3831-abac-e803afd5fe9f | -7.66875 | -50.27436 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c5b87f-ce27-3e00-bd0c-fbcfef457aef | -8.04805 | -48.68286 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e41d8a5d-245d-30bd-a241-29bdaf38a7b7 | -6.40192 | -47.3364 | 2025-09-10 04:42:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 582680e1-fadd-36f0-b836-980f37a26e34 | -7.71525 | -45.1457 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8720e6b0-c3d3-368f-8271-d2b3f7ac06dd | -6.21526 | -45.61934 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2a5d756-02a3-37cd-a456-075cc7a0b2d8 | -9.07567 | -50.46405 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48cb6f39-80c6-3f4a-b3af-f9cea927288b | -9.08341 | -47.05482 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0607385a-5edc-3cc4-ad41-4e0c752522e2 | -8.63237 | -53.11443 | 2025-09-10 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd36bd8e-dcca-3343-b24e-b1141be4a0d4 | -10.30598 | -48.8152 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 604de00a-c1c5-3b71-ba76-3c6cedd235ec | -5.80409 | -51.73384 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a78ddc5-e81e-36e5-8810-396118464b9e | -7.78901 | -46.06254 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae561d94-d4d5-38c9-9ed3-74ef8aa652b5 | -8.49437 | -44.64194 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aca656f5-5f87-3941-98c9-dbfdc3d7cce7 | -7.79948 | -46.06884 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a19aa361-8d44-329d-ad37-2fb7e58250c9 | -11.15291 | -48.35287 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76e39863-ef62-32c2-8838-db3c60476ba6 | -6.42644 | -44.43753 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f8828b6-2031-3a1b-824d-d6f48cd3d17b | -7.97811 | -46.3313 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9d8c084-c525-3c89-b956-573a18d030f5 | -6.38338 | -44.44936 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16722f0d-fd09-34a1-ade2-decdb0f41b4d | -8.20878 | -47.15521 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a6bd035-5513-3438-8b10-0080e54d6f94 | -10.30031 | -48.80673 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40587a2a-6a9e-32c6-8e06-ff5c6c25dff0 | -7.56091 | -48.22894 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23de7929-1ad7-36ea-a5ad-35bdbc1106fa | -6.87731 | -47.89065 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c65a3b2-8dfc-3c92-9c0b-c52f485a36f2 | -7.86822 | -46.02674 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c56868a4-e917-3e1c-b7ca-9d5f9dfb5147 | -9.06042 | -50.47956 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99f5eb7c-9801-3794-bd01-8a5a9f611290 | -7.54282 | -48.2113 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6e59fee-498c-374e-bf8f-43f91b4e77d6 | -10.60281 | -43.30398 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ad5c78a-3bad-35e9-bc79-d7b48114fcac | -6.51961 | -44.84447 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1b328f5-0c94-3b1e-ad29-fd3fe1a4bfdc | -9.06186 | -49.82345 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e11d3c-e898-3e0c-84c5-124c63caa0cf | -8.72397 | -50.03812 | 2025-09-10 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 156bc508-6784-31ad-bd05-e5560b22961c | -11.8339 | -46.74734 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8551b84-2798-3929-aae7-93253fb84f42 | -6.87322 | -47.89359 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7456bc9-7ed7-3764-8f69-d48aa81e4705 | -9.69288 | -46.80887 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccafebf5-c229-35ee-9bda-6fce86d97106 | -9.06107 | -45.76189 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dec36cdd-0e4f-35f9-a5bb-736ecba60b37 | -7.9934 | -46.3297 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d51af04b-e7ec-34c5-bb6a-adf7b6f632d0 | -10.00473 | -48.08939 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2b088716-85e6-36d1-877f-c80c27a93619 | -9.71296 | -48.08888 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b8345d-bc03-318c-871f-fc4f04a486dc | -9.05196 | -49.8072 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b3bc52-4979-36f7-8429-fd238a628a8a | -10.71955 | -48.29218 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0808e2d8-b979-3942-97b1-2ae6712142be | -9.91146 | -49.86848 | 2025-09-10 04:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e79af5c5-773d-3fab-a56e-2d9c806c0979 | -9.60819 | -48.04234 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee9895b9-53d2-3ce2-b3be-3cf5a1d3d39e | -10.01754 | -51.70399 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee1971bf-5b5c-39f9-9217-4fe7347cb84b | -10.7432 | -48.91921 | 2025-09-10 04:42:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae07a1c8-4e3c-3f04-94b7-ef759bde0f57 | -6.38635 | -44.45704 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f974820-0e13-34c4-96c9-57335c3d3a8a | -9.69131 | -46.86974 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c305447b-b9b0-3198-b8d2-dc3c1ddcbb6f | -6.58478 | -44.01578 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8738b18c-c29e-3aa2-970c-831575f516d8 | -6.44118 | -44.06043 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73bd53c9-53b6-3e7e-ad88-19371e5b9fef | -6.41978 | -44.48365 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4f00fdf-eddd-3417-93d0-e2a89fa50109 | -10.84341 | -47.75081 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b58cdf-8733-3168-9e7d-214743ea94ab | -9.89282 | -46.47616 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c6572e8-8296-3c0a-a710-ea54a5f3f53a | -8.75378 | -47.09652 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc4cc67c-ac21-3d05-9c63-3ff71d07872a | -8.72065 | -50.03759 | 2025-09-10 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 987fc8a7-6ca3-3fa3-b686-27c8f78e8e9d | -12.08334 | -45.47627 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51c8f2cb-c434-3ab0-97ce-0a7acc7afe56 | -7.77548 | -46.05124 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dddd4cd7-2d05-3421-a125-90c96286a37e | -7.85463 | -46.01535 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 010bc0d8-9ef9-3467-ad41-aa5d2986669b | -9.93296 | -47.87357 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 907f9bf4-5d0d-3e9e-a3c1-55379311413f | -9.14946 | -46.05679 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ff3ff5b-cabc-3494-b628-43f6d182baf8 | -12.02854 | -45.85885 | 2025-09-10 04:42:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9109c047-eaab-33ec-862f-42be9e81b09f | -6.84884 | -47.91581 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adab9c9f-d229-3215-90f7-ec6e7afa5695 | -11.85395 | -46.76853 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d4c1182-4059-39b4-9546-5af535a46fb2 | -6.68707 | -46.41086 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49dcd9d9-51cd-38ab-b0da-9231ba19a524 | -6.67525 | -44.54607 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2edf27f6-c70d-3349-aa06-c0dd4d458064 | -11.1454 | -48.35565 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9745a13-e02f-3e0e-a18a-9e4229d3156b | -10.6517 | -48.60653 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6fad82d-cb57-3e8b-993b-34288e63928e | -7.85979 | -46.25937 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c279aa1b-989d-3602-91b8-a8698ed39717 | -8.49813 | -45.66285 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc4b2411-5bae-3436-bcdd-c869a1350931 | -11.75824 | -46.46628 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6530f709-49ce-3412-9853-27acfec6ffeb | -11.11695 | -48.41401 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de5589e-7b5d-360c-9955-fa2153efeefd | -11.49603 | -50.41067 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2907419a-d518-3084-9e25-83718904c733 | -6.85282 | -47.91266 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c7d5031-3951-3613-b09d-c7735c3bb651 | -9.75844 | -51.05961 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e638541b-012b-347f-a655-059e7ee60174 | -7.54882 | -44.65611 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1b68b15-b813-3051-885b-b6bc77da1b52 | -11.46008 | -43.63763 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0cda2ce-7d4b-3293-8ec6-3d38eae1d38d | -7.66858 | -47.96013 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31ddc926-a1c0-3736-af53-4145cbebcedf | -9.74046 | -51.08587 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96e408f-e9ca-3c4b-8c70-4a06139863b4 | -10.57799 | -52.03761 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c57209c7-990c-39e9-a644-2bfd8504891b | -6.86076 | -47.92878 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e5d6af5-2aa6-3d11-8c80-7459bdb1d5f0 | -7.25534 | -44.46019 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 536e7b9d-a76e-356b-87b2-07b11143d6b5 | -7.73654 | -50.73315 | 2025-09-10 04:42:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12c475b2-2e53-3401-9136-00d641a701f0 | -8.69811 | -48.88563 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1046687f-45eb-34b4-92c2-bd07d7543a3d | -5.65552 | -51.26761 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46832d06-59da-32bb-813e-2aee4704a9fa | -11.3342 | -46.53016 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79f68223-d248-3160-891b-ddaf377844d4 | -8.81182 | -52.01028 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ab25965-3a77-3799-bc92-7e835bef9471 | -10.39092 | -48.828 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a3c50ac-6fde-3ba5-afc1-48ceb8688215 | -9.52213 | -54.63997 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93375e5f-eaa8-3b18-bba6-d76ca3985d60 | -7.59419 | -49.29018 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f153dd6f-bcb1-300b-8499-32ee9f8c2738 | -8.57969 | -48.95061 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91a7ba4b-c15f-3186-b011-4f6d2680b5cc | -8.04751 | -48.69695 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 183eacd1-9160-302e-813b-dc50d9447072 | -9.01216 | -49.53891 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce7d3e4e-f8bf-301e-a821-8366cb06db34 | -11.11492 | -48.41753 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README59.md)
