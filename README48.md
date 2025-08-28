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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4eb2d0a-8f4c-312e-96c3-01565aa2fbd5 | -0.75411 | -47.75392 | 2025-08-28 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 931d8a6a-81d5-3149-8e3e-eed285b8cb7c | -1.35388 | -51.6539 | 2025-08-28 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f5785d9-e4c4-3381-b58f-e790f44ffd82 | -2.38259 | -47.62579 | 2025-08-28 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a80ff6c3-86ff-34f9-b50f-346eb1d153a7 | 0.77549 | -51.33064 | 2025-08-28 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d1a0c11-257d-32d9-9ec1-56634e0438ef | -0.75307 | -47.75284 | 2025-08-28 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83a6e19-5184-340a-b03b-51d4d7f1f3c9 | -0.75251 | -47.75653 | 2025-08-28 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c7ae315-7f6a-3175-b143-15c739c00a87 | -2.44308 | -47.33026 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a172891-11aa-36eb-860d-545ae6443145 | -0.75718 | -47.75348 | 2025-08-28 04:55:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25537918-440b-3d99-a8ba-f58a1bc0ac08 | -2.44681 | -47.32449 | 2025-08-28 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e9a0e1-e09c-3431-be6d-11c95f7cb777 | -8.29369 | -45.17148 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e72a8946-5130-3c19-b27e-928e56d8a60b | -3.98401 | -51.06113 | 2025-08-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 360503b6-f7bd-3868-a115-a67c648c7642 | -6.71936 | -43.09387 | 2025-08-28 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 819d5f13-b897-3ee7-b0db-a6969482d9d2 | -5.15695 | -47.84915 | 2025-08-28 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7427444f-ff8f-3d52-865c-d064c4e42b4f | -6.25571 | -60.01662 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2795eab4-1509-39ff-9453-274f709ee1af | -5.23197 | -46.09077 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bed353b-c9e6-3158-a4e2-ae1bea26e814 | -6.0075 | -57.85284 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a83bc6d0-378f-35fa-9dc1-36f6e003f940 | -6.36743 | -44.05353 | 2025-08-28 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0df1cccb-2054-3b4f-b6c5-29fe89d266e0 | -5.45935 | -47.9058 | 2025-08-28 04:57:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca05ad5-3a6f-3267-b587-79758f465594 | -8.90698 | -47.32657 | 2025-08-28 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f64e8a-93ff-3e1c-9629-3e5bab31d082 | -9.05601 | -54.94274 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 214b4922-f26d-3043-82a1-71e42b9827cc | -3.40545 | -52.72476 | 2025-08-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf49dbd7-aff8-3aff-b097-e075622142b7 | -8.29203 | -45.14153 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e77883e-2086-3a18-a4a9-31fcedf48931 | -6.1648 | -47.28058 | 2025-08-28 04:57:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ec9393e-08e0-32c9-a40d-88275e839198 | -8.29988 | -45.1246 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cd37edb-b1f4-312d-87f0-011da4f052a0 | -8.29225 | -45.18243 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6eb6901b-cb05-3de0-8703-d04e87e00b3b | -7.47018 | -59.90481 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53cb5a0-0978-3ea4-b4f0-0df16413afa4 | -6.2396 | -60.00988 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbda9192-aa44-3104-a5a0-35ab6d49a3ff | -9.86124 | -44.68663 | 2025-08-28 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29820847-d1cb-32c9-8510-702a13d1d8a1 | -8.26571 | -45.17144 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc33875-f2d6-3f7d-99f4-bfe46a939c49 | -7.6748 | -45.00317 | 2025-08-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d35cd287-812b-3059-9361-541d6cb582f6 | -6.15962 | -44.3957 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d7778e-f3cf-3cde-af6f-c27242433afb | -5.315 | -55.88054 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc5e0f1-f074-3046-9b09-a498a765f47d | -8.90685 | -47.32853 | 2025-08-28 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6664be93-f103-3fd3-8e06-f9524883e32d | -7.62639 | -61.03019 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b272a3b-95e1-3661-8aa3-1334c7fcfa20 | -6.88215 | -43.61275 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9b04cee6-5e26-36fc-9522-c23586c7e20e | -9.95927 | -46.50174 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 639000fa-d4e2-3bc3-843a-f45a4dc01c00 | -8.49659 | -44.74764 | 2025-08-28 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47d9c675-d2cb-3a6b-a65b-891549bec772 | -8.28771 | -45.17443 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ce35802a-e86b-3d90-a022-34a751aff587 | -9.43337 | -48.25247 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1de08fe1-19e1-392a-957e-4c104b7fb0eb | -9.19166 | -46.74457 | 2025-08-28 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40de8ad3-5004-3ffc-b8a6-4d8ec35bed88 | -3.98425 | -47.88429 | 2025-08-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4b92f08d-8f79-373a-9fbc-21cc21a4079e | -7.73118 | -50.28179 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 962dcdeb-ad81-396b-8edd-d436dda6af4a | -3.98255 | -47.88642 | 2025-08-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 445faf33-017f-3691-b4ea-9787a5b52cb3 | -7.41205 | -60.62504 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d027509d-be58-3d61-85ed-7d5544ff0095 | -7.20132 | -44.06362 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39a58bfd-6968-3d1a-a031-0d223a0102ee | -6.88043 | -43.62568 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb5b14b5-cd35-39af-aabb-3b6cc9bf3453 | -8.44156 | -43.69133 | 2025-08-28 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b26221b-71b9-328f-b6e3-f4a93aceb55f | -6.94953 | -44.08474 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78f239ac-dbc1-318e-8972-fb985b6a48c9 | -6.87676 | -43.60751 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7bf7319f-0706-32aa-ae2c-fdcf8d679ded | -8.28868 | -45.16698 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f3294837-278f-314d-9dfc-04904e64b0c3 | -8.90219 | -47.32589 | 2025-08-28 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ea75ec8-710c-3ef4-9f71-c59e9752c0ca | -6.87733 | -43.60316 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 343d49d8-6b3e-364f-b690-2926a3b39a26 | -5.83997 | -45.30601 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba133b84-6762-396f-a11a-a16fc331f69a | -7.75346 | -61.0813 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21cd72a6-3a14-387f-b7a3-fea6d8c40534 | -4.12541 | -56.33528 | 2025-08-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8f051dd-0f10-3686-8c87-cea061253c70 | -6.91011 | -62.93366 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d7fc8f1-86e4-3c3e-8b9e-ef806817cb4b | -4.48161 | -47.6689 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6977938-575a-3808-abb9-a73dda92e6ef | -5.56497 | -52.07386 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04383f4d-3bb5-3a31-9166-4a438b5bfcec | -5.99715 | -57.84673 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b5cd236-16fb-3e44-bced-c5578c7f099b | -8.28967 | -45.15945 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4cd88dc0-e83e-3fc1-81da-43baeaa276d9 | -8.453 | -43.65914 | 2025-08-28 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b8740a8-591d-39fe-a199-c2f636511fc4 | -6.90077 | -62.93403 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426582fe-7c8b-3c84-845f-c9d813cd1405 | -7.59924 | -63.34557 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7867e3b4-add6-3fd9-aaab-f7f1c6da5e61 | -6.87334 | -43.63337 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d1b97e2-482b-3553-85fd-88e87a7fdf5b | -6.19762 | -44.16236 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 849e4b45-200f-3db2-a782-6bc91212c0ed | -8.28705 | -47.21403 | 2025-08-28 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d09cdf38-fc85-3a3e-8d7b-2a2791bce6d5 | -6.88272 | -43.60846 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f1b66676-28b1-3b7a-9715-6d772acaa377 | -6.90958 | -62.93663 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24d1d62a-0e49-3c2b-bbf3-fc76fe06cc30 | -9.45378 | -51.96206 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62cd66e2-1346-3e5c-94d2-f0996160c702 | -7.00936 | -54.99981 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4634457d-5165-37d3-840d-9791fd264f38 | -6.90399 | -62.93873 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 339c106c-6cbe-3f5d-b3bb-a6f51801b67a | -6.71319 | -43.09311 | 2025-08-28 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f682645a-5df6-3b24-aaa1-7893059cfe95 | -7.90897 | -55.42239 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 581ca04c-2dbd-382a-9b5e-783c8b666b4f | -4.95726 | -55.81298 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76b4e201-c919-30f2-a67d-271d1d3c68c4 | -8.08652 | -44.99393 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 321502f7-c581-3b11-abc8-a282e2be06a3 | -3.73178 | -48.35694 | 2025-08-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 193eacbb-8837-3b18-8004-72dd5f503cd1 | -8.38669 | -44.97492 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd1c42b4-bf69-3c52-83e2-73aba2ae3c67 | -6.43827 | -44.57658 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ac90f76-84f7-3dd8-9363-7351f00a5a41 | -7.60439 | -63.34642 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f21800b-6ffc-359a-8789-712a300289ed | -6.88753 | -43.61801 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e96791c-3809-38f2-bf27-e5c80487f078 | -6.0777 | -44.00106 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a369dda-07fa-3478-a955-1d0d9bf626dc | -6.87562 | -43.61612 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d91c91ff-2c88-3f69-ae8b-8df3c093bddb | -9.45923 | -51.94972 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a265a512-99a2-3a3b-a5a0-0f8916e6475c | -1.88126 | -55.5243 | 2025-08-28 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2274ce7d-1e80-30eb-b10e-ee5db308b667 | -5.20379 | -46.06462 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f07f4f52-8b8d-3cbe-ac6b-4ab7d5a25c9f | -6.18359 | -44.00825 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c82b1424-ef4b-3dee-87a1-cd85f5e703a2 | -6.44331 | -44.58125 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8765073b-7fd0-3384-9e2b-2ce284c97dcf | -7.20114 | -44.06462 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eaf54a1a-07b9-3aaf-a2d5-79e65d6ca5a3 | -7.05918 | -44.36523 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c60f9399-754e-38e7-9e48-9366defbda69 | -8.28708 | -47.21598 | 2025-08-28 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62f3af64-9dff-32e9-b7f2-e7f3b48f1f17 | -7.62565 | -61.0345 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0289a5e-ffb8-3269-b404-ea13965f9c2e | -8.23371 | -55.56422 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a90f73-2cbd-36d2-afdf-8f58894997ed | -6.16497 | -44.05928 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f27dd93a-a9ad-3f3e-9e01-9d96ef00df48 | -9.45293 | -51.95493 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c7ab2e5-f075-3353-9d3f-939f7ab3be11 | -6.87448 | -43.62475 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fc7e755b-e49b-364c-84c4-ff319d1d2f74 | -6.86064 | -43.6129 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3658195c-b3c9-30c3-848c-017aa4c366a9 | -8.28918 | -45.1632 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| faf91a8c-80c6-31b1-b118-d970f159043d | -6.44485 | -44.57001 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 016774c4-822f-3f2e-9f23-e5cbbd8f2673 | -9.05546 | -54.94622 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3bf674c-245b-3250-b6da-427dc5910086 | -8.27672 | -45.17282 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README49.md)
