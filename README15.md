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
| d600335d-ff2f-3c85-9f1a-59583c8eb0ef | -3.82293 | -52.36338 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e5cccd-0639-3e50-904d-d185b48ea748 | -3.72086 | -45.55013 | 2025-11-02 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| fc1ba9fc-0fea-326b-8145-7a4491b3ae76 | -3.61601 | -54.23705 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bb6ceb3-b22d-3ecc-9ad2-e34fbfb8d19a | -5.52237 | -41.08846 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d995f43c-c3fd-368d-98ae-f100e714d0fc | -4.12099 | -49.16159 | 2025-11-02 04:48:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e4fb4a0-5f5f-3702-bcdf-a444f57ff7dd | -3.56778 | -54.58845 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ad184c0-0e02-3012-8097-a1b053fc2038 | -7.2331 | -44.94144 | 2025-11-02 04:48:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e21160a-08cb-3277-9eae-017f97e236f9 | -3.22493 | -50.58413 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07ced19d-9ab4-3250-90d3-23895d3fed53 | -2.57098 | -54.01143 | 2025-11-02 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63b635b5-6d6e-3076-a3ef-60d0c34113e9 | -5.40595 | -44.93547 | 2025-11-02 04:48:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58e275a7-7280-3795-b05a-f2942425f8a0 | -3.42716 | -45.91265 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 090db03b-dc3b-31b3-b497-a42e016eae7a | -2.70517 | -54.65408 | 2025-11-02 04:48:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef2ff327-e64d-3478-8779-d560307e3c2b | -3.55469 | -54.57195 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3dfe6cb9-1ecf-37da-8d15-fc0ff5488aca | -5.04048 | -43.61586 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe635c71-abb8-3514-99da-97254dba0c20 | -3.89688 | -52.20919 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1488270f-6900-3490-9e78-2972ef109e6b | -4.67496 | -44.61827 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c879fbd-8b00-3dc2-a0fe-86035f32b5bc | -3.72629 | -51.70574 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 852075f0-c60b-3954-b152-7fd0cdea8c81 | -3.30772 | -50.01707 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48bc82aa-a7cc-373b-a2c5-f3356de9ea48 | -4.32062 | -45.63893 | 2025-11-02 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae593436-93c0-35a5-a093-320b946d4642 | -4.57953 | -49.5927 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6351c95-99bc-3932-a7b4-2ca0bd223cba | -6.47598 | -42.05597 | 2025-11-02 04:48:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e54d4634-c429-3365-9e51-b83c009672d2 | -4.11816 | -49.15747 | 2025-11-02 04:48:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 439b5f99-844a-3456-8449-9345236390da | -1.2849 | -49.38879 | 2025-11-02 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d4378f4-62c6-307c-94b6-90493daebf72 | -5.52894 | -48.10851 | 2025-11-02 04:48:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 352afeb5-26d7-3487-96d9-253fd5d33e78 | -3.2393 | -50.79192 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 668e97d5-1a84-3960-94c3-fc3bc7b8535a | -2.34509 | -47.54021 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d00c02f9-7342-3d3a-b089-547c00f52fcf | -3.77058 | -51.34337 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c30cbeac-2684-3b18-9bb0-e4c072f76aa8 | -3.96028 | -52.22608 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b636ab7f-3e45-36f1-bb45-590d61bbf315 | -3.89342 | -52.10012 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a864e13-c99d-3fc0-ae23-e24eb7171af2 | -3.3842 | -49.98296 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee59668a-bb77-3f2d-a241-fce692592a8d | -3.72743 | -51.69861 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af841aff-85e7-3b44-b6cc-18ff393b56b5 | -2.31829 | -48.58691 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eea419e9-d253-3417-ae9f-05051956d039 | -1.75016 | -54.44505 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3363a4e-2983-31e1-9715-952b2b3c8ede | -3.83354 | -51.31382 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 142bbcb9-8d95-3fe6-b47b-21e2155954c0 | -2.4442 | -49.03153 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c10a680-aa91-3afb-9adf-d742c063d043 | -3.14078 | -49.42039 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1063c51c-c96c-3218-a02c-37ce501b2436 | -3.50395 | -49.95173 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae33a8cf-55d0-36d5-9528-05a80aada27d | -4.18357 | -47.65427 | 2025-11-02 04:48:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f8c6611-b0c2-3fed-8ee7-d4b42cc097cc | -3.50244 | -50.47603 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9bb35f5-de87-3073-a7d5-07ae9754cf1a | -5.526 | -48.10396 | 2025-11-02 04:48:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e7d7cd1-ede6-3ed6-b6de-bd825f4fefda | -4.08851 | -54.23018 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3e902f-dd73-37ed-8d5e-a6ca0fe1ed46 | -3.01919 | -49.44118 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a8fbec1a-c7b3-3c52-a434-9adbf940ae23 | -3.29209 | -50.20221 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f431232-db05-37b1-8ede-5e7e52cdf0fb | -3.89854 | -45.74762 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e8e53c4-d542-3d39-adcf-bfeb4bd5057d | -3.95934 | -49.29768 | 2025-11-02 04:48:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8fe15a8-49d1-34b5-be1f-570ec0e5c2ab | -3.45478 | -50.22035 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4909d11c-3e1c-3c29-b548-c02733ddf833 | -2.82724 | -49.13052 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab74c746-dbf4-3eb3-a1e8-143109ca3e75 | -3.93206 | -49.96197 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb0388c-f5d2-3f81-a6bc-199418f2774b | -2.29108 | -47.86499 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5eb31f-7725-3466-a4a4-26435d0ca5f7 | -3.46824 | -53.12654 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373b793d-78f0-3c90-922b-bef92d30a25a | -3.68941 | -49.54927 | 2025-11-02 04:48:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c196ad14-29c9-3bdc-b044-7bab63f3e9fb | -3.59704 | -53.53709 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 238e0ba9-2aaa-323d-8faf-4cdfaa963ae4 | -3.23875 | -50.79538 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41a1beda-158d-336a-b9c1-58666fd92f79 | -3.27601 | -46.50718 | 2025-11-02 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ee2b72-f75b-365e-8420-068a66fa936b | -4.108 | -51.09944 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 681d9a63-17b5-304e-b53c-a7fd656a5560 | -3.42718 | -45.90932 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7423a052-6d46-3ff5-bbb2-90516276facd | -4.14283 | -46.27728 | 2025-11-02 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faaebf85-67ce-38b1-bd43-0ac6a0813146 | -3.01889 | -53.96786 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6383bcc0-1322-3dc9-a8b3-71e00d0ba538 | -2.13406 | -47.41278 | 2025-11-02 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 800208ec-5d43-3aa6-8eb4-327676885517 | -3.56988 | -54.58597 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d66a40c-c0c7-3664-934d-dd32a13a1cb5 | -4.14304 | -51.15114 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0de8255-b4f9-31ac-85d7-cc2e4470cdc4 | -3.87741 | -51.18828 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a269d2e-5000-3580-ab45-1175b629e91a | -3.01864 | -49.44468 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c893d685-a0e1-3c1d-80ee-4951a7eb8329 | -2.11003 | -52.77688 | 2025-11-02 04:48:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45c5acbd-d7c9-3ef8-881d-90349c2071ae | -4.30158 | -45.89364 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 729e421a-b993-3896-b522-5c931aadb235 | -1.42144 | -55.23428 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c431ef3b-8dfa-3ae9-be4d-b990f704ebff | -2.34862 | -47.54075 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d70f7de3-8d35-37a0-a991-1f8085fe73dc | -4.57867 | -44.79106 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b95a30e3-fd2f-339f-a6df-ed80072ee5cf | -3.13144 | -49.23868 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1369f757-e8bc-3194-9c0c-7dc3dfd03a62 | -4.10369 | -54.11452 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 363eead5-1aaa-3800-bd05-9fea88bdd565 | -2.87981 | -51.75335 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80bb5c48-6de0-3d28-91ec-83aaa0b17602 | -4.12381 | -49.16571 | 2025-11-02 04:48:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d415c127-bc91-3e91-87c1-745c30bda2bf | -1.79999 | -55.44626 | 2025-11-02 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ac45e2-7a31-355c-b22a-78dbd0aeb5bb | -4.31134 | -45.89672 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00f285a4-e12e-328b-b0b9-372950749ddd | -1.49598 | -53.12239 | 2025-11-02 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 88496781-6dae-327b-a52c-796856b86d2a | -3.0153 | -49.44416 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9a25df7b-773d-3ed2-a1b1-e08c37938303 | -4.67866 | -44.6231 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36a90314-488a-3338-8ee7-9102a93a2adc | -2.31206 | -48.58223 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0ff5ad8-61b0-3c1f-b769-3b3187d74ed3 | -3.82174 | -51.69163 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cba357d9-2e03-39c0-9784-d38c95b9a4e1 | -3.72435 | -45.55424 | 2025-11-02 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cfd094f0-640f-366f-b772-b713be6b68ac | -5.52348 | -41.09359 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf61bb3c-9655-3a56-90a1-690c258efc66 | -3.71388 | -45.89085 | 2025-11-02 04:48:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52b3eb74-7776-3bcf-9c53-ca3fa7c9b5cd | -3.81849 | -50.93973 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99187977-b24f-3d45-917e-e0f85967a7c1 | -3.38693 | -49.96566 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cd33eaf-4d70-3fe3-b921-aca36cca1ae4 | -4.65168 | -46.83721 | 2025-11-02 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afaeeeb9-d30c-3e1f-994c-e241c92f5b93 | -7.17568 | -41.93556 | 2025-11-02 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 607eefdf-0299-38cb-9887-a9b72641908f | -3.51979 | -50.32318 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aedaa71d-c3e8-3fad-b2bc-e176e0a7fb50 | -4.13083 | -51.14205 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8dd10c8-d273-3cd9-ac9b-f495d886eece | -3.3781 | -49.97847 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d26fc37-225f-3394-b6f9-4b1a8b020254 | -2.64116 | -49.50397 | 2025-11-02 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c903f3e5-bb5b-3063-a16f-1289bf5ab727 | -5.52185 | -41.09228 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99526a00-4edc-3d6c-9819-fa6a0fc5c051 | -3.28553 | -51.54856 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a17826b-00bb-3eb5-beed-0053bb1c601c | -3.42903 | -50.10307 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c742d25-ad0d-3967-9640-4e41848bbdcf | -3.12808 | -49.23816 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fb5c772-a127-3cfb-b1a9-9b2bc192094b | -3.32339 | -52.56353 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de2077fd-6268-32e2-855d-499af814b9dc | -7.29731 | -41.5743 | 2025-11-02 04:48:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a03c070-db92-3e71-aaf1-1a80a7962946 | -3.60383 | -50.62617 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86d29c20-c214-353e-ada0-4c7c68bca548 | -3.55589 | -50.159 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285e0911-6a56-319d-8f45-a9cfe2921c5c | -2.31036 | -48.59309 | 2025-11-02 04:48:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02338dd1-559c-3e58-bb65-724f57bd2cf9 | -3.0239 | -51.23673 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README16.md)
