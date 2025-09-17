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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 940526f9-8e75-3b13-986b-8e913f1e6c20 | -8.65602 | -46.40633 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1858bb3c-2882-312a-b907-ac0f1dae5888 | -5.04898 | -46.00731 | 2025-09-17 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ef04f5-55ed-3331-a6b9-96258b398c05 | -4.63883 | -46.07119 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f0c3ced-89d8-37c6-97ee-fbd1498d43f8 | -6.9646 | -44.55438 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb74c5cf-ee05-3c59-9541-591d809df27d | -6.22534 | -43.90989 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9609e304-0e2b-33d4-ae88-24b8659bf85b | -6.64095 | -38.91491 | 2025-09-17 04:10:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67790d33-843d-36de-a175-b70f3aaff342 | -6.92011 | -44.80241 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 909796e2-a597-3087-8bf6-0268dbf93bd9 | -8.43737 | -47.68191 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eaf8eaea-60c0-3b66-a79a-70649e97d507 | -6.96919 | -44.4594 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65f17d06-94a1-398e-85a4-e8e1bb4284d3 | -6.04583 | -43.13776 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f055575b-6709-3aa4-bef8-05ce628da5a0 | -6.95611 | -44.56125 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86de34b5-a466-341a-8eaf-2c7e17fe4875 | -7.98082 | -43.94051 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7a2588f-4a5e-373f-b13f-be7190101dfb | -6.1952 | -45.12128 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec8d4a65-89e4-30ca-a725-018d8f4b9fc1 | -8.78339 | -47.80883 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2124b8a-6c49-33d6-b0cf-2e8a6c498279 | -7.52925 | -44.7338 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc058611-b79b-3efb-9094-fb5dcccc5db8 | -7.31271 | -43.96837 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 567cebfe-b2a0-33b3-a494-6e288a0a3cac | -8.96134 | -44.19781 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13bed919-a1b3-3083-8de1-93da80415f4f | -10.22562 | -44.9789 | 2025-09-17 04:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f06bf7e-32cf-3118-8b29-2651b66454bb | -8.68501 | -46.37838 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cff85d07-18f4-3daf-ae06-6a1d6d909128 | -6.96702 | -45.54639 | 2025-09-17 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af549a08-6ac4-37d8-b636-76d070ce06b2 | -7.40281 | -50.00925 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe1dc858-1cec-3919-95c9-cdefc60ace58 | -6.19146 | -45.12073 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c54165e-d548-343d-b445-d83f6f1da1a7 | -6.67786 | -46.30799 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 24ade922-1d9c-3c24-90fe-09bbb50bacc7 | -7.68138 | -44.47044 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c075f10e-457b-32ae-b47a-608183d46759 | -8.65584 | -46.40883 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a69133b-9669-373c-ae51-fb0bf8f60f5f | -6.2212 | -43.91321 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5327a5e2-afbd-3e3c-b720-c8a1491f4f4c | -6.41867 | -43.60133 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28cf955d-e154-361c-9b93-d84c47be1039 | -5.77195 | -42.77673 | 2025-09-17 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09296838-f051-3541-84fb-a6b531b84e5d | -8.95881 | -46.32135 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bccf5d34-0b0c-3595-80c9-61b67617db38 | -7.7696 | -44.72421 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3fef95a-c1ac-30cc-bf20-ec379c068b97 | -6.3469 | -43.15504 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58e13102-7887-3ff6-a7c8-be790ddcda9c | -7.88034 | -48.15964 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5d91bf4-1b8f-3d91-8c0f-f5daa6891ae5 | -7.58014 | -44.58283 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eae0a044-714c-3be0-9603-e6c06bc502db | -5.53111 | -42.18328 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7bf2eb4-293f-34bc-8c92-c29b445909de | -7.25899 | -46.6119 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c3a7c50-a4d4-3c28-a59c-b9e299d3065d | -8.98704 | -45.75982 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87aaee9a-e5b2-38bb-b23b-db9b2541b527 | -6.52412 | -44.13644 | 2025-09-17 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e3cdfe-2b88-3f2b-8356-8e38d593a1a5 | -2.83094 | -48.66099 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4657c892-c56c-3a97-81c3-9743e186a58c | -9.76056 | -47.33361 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c9d8308-7461-3ff9-a5ab-6bda59739a2a | -8.1672 | -46.77049 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c918ec08-c3a5-3d18-bdcf-2b5410371dd1 | -8.98469 | -46.23766 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75c0cd7a-98d8-383a-8c88-322b9f78d4b5 | -6.42701 | -43.30707 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6479b173-ceb9-3d4d-a469-ff7493475b47 | -6.39807 | -43.35573 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59a252ac-fc73-39e6-b510-76591b19a483 | -8.16185 | -46.75326 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45ed66e7-142f-32da-9d43-71b84f35a1db | -9.05597 | -44.95856 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a4b01f1-67b9-3944-b1fe-a530d663f758 | -6.29495 | -35.20192 | 2025-09-17 04:10:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 138976e9-d62d-3969-a7b3-66207291666b | -7.0653 | -44.35474 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8724e85c-1e23-3f47-b99b-d6bac6b88d18 | -6.16965 | -44.50873 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5976fdb8-ef67-3050-a0d0-6f38fc46234d | -6.29591 | -42.38764 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04b8d531-16d8-3738-a9d3-2e6665bb2c7b | -7.72248 | -45.30066 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a5d6963-ecc7-33f4-93e7-7ab0c7829fba | -7.68846 | -44.4716 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed4e7fe9-0a9d-3ee0-bd9a-f7146173565c | -8.66055 | -46.40466 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 148b2aef-f1cf-34d4-8b8c-3f0c56268c0e | -6.7689 | -43.39931 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0c6ac1d-138a-3bc6-90c8-f857afd50880 | -6.88267 | -43.97239 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d417da2d-22a0-3a1f-9e3a-d197261cb115 | -6.28488 | -42.38255 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 350776fe-2b3f-3937-b3a8-706ec82df073 | -6.88392 | -43.96467 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2609eb7b-ee51-3cc2-9cfb-e7e67484076c | -10.29526 | -45.36472 | 2025-09-17 04:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d43709f5-4c6b-391c-bf9f-0ab3b3587e37 | -8.92773 | -46.27182 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c019efa1-ed37-3258-a931-6f4c986aacb0 | -3.61223 | -41.35772 | 2025-09-17 04:10:00 | NPP-375D | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6cfb3618-9b79-3d74-b56c-11e22c29dd74 | -6.11195 | -46.33554 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cadb9e6c-ad23-39ba-a011-cb659a6ef197 | -6.125 | -47.82721 | 2025-09-17 04:10:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb195c01-9219-3825-afb8-0a4ba1e44d74 | -7.56562 | -43.94854 | 2025-09-17 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b33c32f-071f-3009-83c7-21a6b5c6a98b | -5.3465 | -44.82323 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4652681f-77d5-3701-96be-9d62bf72f75a | -6.61973 | -44.74388 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0120be91-3f3d-3f66-8faa-a8894f49af52 | -3.42157 | -47.60444 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fddc6fe-bca7-343d-8a06-6d476ff06f9c | -5.32625 | -44.99686 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6003c1a3-1bb4-3a21-9dc1-6acc0be73064 | -6.19818 | -45.12636 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6ddfe98-c2ce-3b92-a9ea-c5b2b75b1941 | -6.88329 | -43.96853 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 324b60b3-6a45-350f-99e6-0b18ea20f778 | -7.56992 | -44.55626 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6fdfa5f-136e-365d-806b-9146a1237843 | -9.05516 | -44.87543 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 897d25c8-94a1-3b6f-a994-57af7b8f3eba | -7.57591 | -44.58629 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81789309-64d3-36ca-b3de-9295834be12d | -6.39644 | -43.34401 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e2f84b8-e5de-3766-baae-173d31b09c4f | -3.17952 | -48.81105 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 01b5ce87-f5fd-3384-86ee-25713feb517a | -9.59543 | -45.66343 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab76d82-ce0e-3371-9fc7-184d3e2c0f9c | -6.35031 | -43.15559 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33fe111a-6a7e-3c17-a6d8-5703bb7aeed5 | -8.43669 | -47.68576 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 620fb548-3db7-398e-aad4-9171116de5c7 | -9.75529 | -47.34004 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3e06c0b-7a24-3d8f-b906-d38c81d65505 | -7.6971 | -44.48533 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d589a425-5ee4-3446-abb4-bc69b74973e2 | -5.47477 | -45.34462 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 603602fc-c132-30f8-8c84-989d8971280a | -7.57146 | -44.56898 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8480959e-96a5-310f-861e-2810a749a06e | -8.16496 | -46.75922 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1906eab5-58d8-3140-b428-54aca5d4273f | -8.98835 | -45.75772 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb02bd6b-64cc-3a24-94e9-90f1563526a3 | -5.63154 | -44.83346 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6799a52-c037-3bcc-bd24-82fcb07f1db5 | -6.97932 | -44.53189 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d806880f-07ea-3066-9587-0d9886a14d24 | -7.68121 | -44.66932 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe47efc-09b0-3049-919a-fd1bb81503aa | -5.32921 | -42.70707 | 2025-09-17 04:10:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5d493aeb-9737-3c35-a936-16a31ecc6e95 | -5.61633 | -42.89731 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4de25680-df08-3d89-8cf3-bee82029d3f7 | -5.59939 | -44.11729 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29388ae4-a7a9-30a2-939e-c5d7fbbede38 | -6.52867 | -41.82253 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a64b964d-0785-3e49-9e7f-cc0068039fc9 | -7.02939 | -44.15857 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e9b948c-9e03-34ad-844e-f3459ae55675 | -7.57281 | -44.56089 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cb8f2d8-2de2-3b53-9805-fd4ff424049a | -7.66858 | -45.12957 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f7f1e87-ae5c-3810-9729-4b28c3193c84 | -7.09249 | -44.54528 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd04804b-ac91-32cb-9401-8ae1ec996dd9 | -9.05484 | -44.83354 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25b3df1c-3b8a-353f-b5c1-0ad3f25e0d7c | -9.12988 | -48.11112 | 2025-09-17 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fec25547-2ae8-32be-a38d-f38345223478 | -6.81728 | -43.03125 | 2025-09-17 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd47790-0b52-3c97-97d6-a0cfca8bdd09 | -6.43103 | -43.30396 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c598305c-19aa-3440-90d0-b99321dc2b2f | -7.68191 | -44.66512 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2710b279-b4f9-3ea4-b88d-20f149e30996 | -8.96101 | -45.75535 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90ecb890-14a7-33da-afeb-5bdbe0c6daf5 | -7.61464 | -47.46461 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
