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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ede639e4-dc46-33c8-b35a-947b3d7ab344 | -6.88293 | -47.8941 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 461fc182-0f68-302c-a233-62149bed14a1 | -11.66365 | -46.91157 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58d8889d-5c07-3cdd-8931-df5ce723df70 | -8.09032 | -54.74804 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ad582b-c1b7-3ee1-9f77-c314279633c9 | -7.08201 | -45.20171 | 2025-09-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a0d35a0-f52a-3f83-912f-ce7d4288e338 | -10.00175 | -51.70722 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e63a770b-1877-36e9-bba5-d11f3a5cb470 | -8.51902 | -45.71706 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5dff2f6-7b0a-3cd9-94c5-cc589bb1cc8d | -8.34598 | -45.05984 | 2025-09-10 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9c3467a-cb24-3746-a2df-b638144f7e56 | -8.06919 | -50.18644 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f8b49144-dba5-34e8-8b38-493d39b23b65 | -9.06717 | -46.98776 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bcb02fe2-3ade-342e-bdee-b65cea65bb1c | -6.85737 | -47.89664 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6174be2f-9569-37ae-a6ad-678e02f984b9 | -10.27469 | -48.82267 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 257fb146-2bba-32ad-9a35-18f4e899700b | -6.88937 | -47.88416 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 710a7dc0-2fac-3979-9c46-b1c3ba2f246a | -9.0661 | -50.4788 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38ad0738-d29f-3c1f-9248-905c3a1dbf9e | -9.06511 | -49.834 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0d47e152-551d-39f9-bfcf-99ce9c71286b | -12.17061 | -50.61972 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5019df6-fef2-3c2c-a65e-4839e6bfd13e | -10.01565 | -51.69549 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f14a8d2f-5b58-3328-9908-0b25aaeb9f9e | -9.01638 | -49.5421 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d743741d-c1b2-3027-9bdf-90b560e9fd03 | -10.01081 | -48.08264 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c488b44-65d8-3aad-837b-9f480eb042f4 | -11.24006 | -49.40798 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67392d42-2881-3eb8-a72f-d1e1603e30ce | -11.49925 | -53.84023 | 2025-09-10 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4567378-d24f-3cc4-a524-ac0090cc6553 | -9.82937 | -46.04969 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e59390d-04df-355f-9ce7-e61e69eaf3a6 | -11.16195 | -48.35671 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e0f1d0d-2735-395f-b2f7-fcab043afd20 | -9.06446 | -45.74796 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37fe6cb7-28ee-365e-a00c-90175d9350c5 | -9.75546 | -45.4116 | 2025-09-10 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 75d38c66-6ed7-3e23-92a5-503bb0150be5 | -12.99716 | -48.03915 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd3c03ea-d30e-3c1a-ab3e-854243899629 | -9.45424 | -46.73931 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b77d954-b4cd-34f9-825d-996ab3eab061 | -7.84407 | -45.41462 | 2025-09-10 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5d9e503-d95e-3280-a073-d7e5ac02e46b | -10.86441 | -55.72082 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fda51fe-574c-3728-b874-6ddf1f311382 | -12.02658 | -45.8569 | 2025-09-10 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8ad5a70-3933-3919-a13c-a7a7d293518b | -9.44132 | -46.70908 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed1082ce-8f1f-351b-a574-6adf60bb1ba0 | -8.4645 | -47.29686 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3108bf2-5198-33b6-a81a-433e851de93a | -11.80209 | -46.76344 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed259e9f-6142-318e-88d5-48b228a74d72 | -11.94065 | -50.76787 | 2025-09-10 05:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b07e87c-a064-38fe-bad8-0d808f40e0c2 | -7.78238 | -46.05751 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9efe93e-32f5-3419-bdf3-effb8edb4676 | -8.03894 | -47.28066 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9251bb93-9247-3e78-b561-c5c381399f5d | -10.56416 | -51.99584 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a27f68-5643-312e-b04e-c6e88eb0cf54 | -10.00668 | -51.70118 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50feefe1-1b13-3a20-8cf4-1ea4bc6c335f | -8.21068 | -49.51249 | 2025-09-10 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6fb65cf-d3ed-3d39-988b-15f3adda5b37 | -12.21076 | -53.89516 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75aaa99a-b033-3be2-a5d0-19a48ed91a10 | -11.46675 | -49.24603 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28f7f1fe-e38d-31fc-88fd-cae9d9bff8c2 | -9.30977 | -46.72536 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dacab57a-21ae-395a-988d-068244ab0cae | -6.85287 | -47.92905 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f460b62-affa-339d-ae36-f6f6678d6b48 | -8.84824 | -47.25985 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 617c183e-9163-3e74-81bf-0f1300764396 | -11.10794 | -48.45312 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31836107-5619-3a9c-8f0a-7179824ee672 | -9.08538 | -47.05728 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b73d9ed3-65e8-396c-88ca-e55b5f0619e2 | -7.54325 | -44.66007 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21e160eb-a15b-3ca9-adcf-f733eee34076 | -9.05758 | -50.47737 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7cfc6b8-fee5-3c32-89cb-617b766f380f | -6.87292 | -47.89352 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10855c4a-80a5-3136-9276-848b801141cc | -12.02599 | -51.00177 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e1f8d48-d6f5-3c1b-8233-27d25b0202da | -13.01617 | -48.01733 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c75d0f42-e0a5-324b-b420-5bdc21f48319 | -11.10845 | -48.36959 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f26993c-7d21-367c-a4e2-868282346bb2 | -10.27613 | -48.8117 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8a30ce5-f43b-36ad-bae0-61882bd44554 | -6.84854 | -47.91125 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b82e85c-4f5d-388f-82f9-0b85e2ba7177 | -9.07355 | -46.98136 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77872039-190f-3a54-ac9e-d5480ff07a86 | -9.39253 | -49.21888 | 2025-09-10 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c8eec0b-70d3-3fc3-b902-b7cbb01bd2db | -9.09721 | -46.98355 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efaff575-81b0-3ff8-bc81-8f0c9ec0d221 | -11.29394 | -53.96469 | 2025-09-10 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 241cc39d-26f0-3f25-ba48-45510c38e95d | -9.67074 | -46.62973 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4f6d453-730a-36fc-ab20-1ea464b90d06 | -9.45352 | -46.73867 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af25fe7a-086d-324a-94de-453c931a8825 | -5.72992 | -51.69046 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acc290c0-3216-3e81-915b-8ea905a797c8 | -9.44039 | -46.71602 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d808d4f0-4fb9-3f94-9a75-2aae77ab7d4b | -10.97037 | -46.79967 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 021bdd9d-2545-3716-955b-9036d4cd4eca | -8.28035 | -47.4686 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58896f25-cfa3-39bb-be19-51d59932a6bb | -7.73776 | -50.75794 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b57c3354-27a9-3d28-82d0-59843f9b2a0b | -4.88511 | -56.04208 | 2025-09-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3003fa6d-73b1-389a-8543-d16922d9e67b | -7.86156 | -46.26056 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50569677-9321-3cb0-85f3-469d31edd877 | -9.09344 | -46.96977 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6108d3db-17ab-36f5-9c8f-a5dba4ab5b09 | -9.34565 | -46.75222 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9797e9f0-d00c-3937-93f5-699e55f43e8e | -11.11339 | -48.45087 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e35c8f8-16b5-354a-8078-b7db29b20993 | -9.60712 | -48.04167 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0ccf4f1-de44-3b7e-bafd-959ea3749b9d | -9.06248 | -49.82002 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8970954-9145-3aa5-8d8e-429d99ea177b | -12.00664 | -50.98215 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| d29a9dee-edae-36d7-8f11-9e42b34ba091 | -9.00612 | -46.06104 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d06f5606-9162-34b3-a620-720df7a2a7e0 | -8.00238 | -46.33463 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ef2cd3f-20d1-3103-862c-c23549ecf1b0 | -11.68206 | -46.90231 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24af4a90-9cfc-362f-ad59-67df031e6e8c | -8.66424 | -45.74017 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d17b3ef-ed75-38ae-b424-3f0c5010483d | -9.09895 | -46.96999 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3c37d821-8cae-37f1-8fde-187f865457a4 | -10.01466 | -51.70247 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01cf6773-63b1-3f08-8ee7-560128cc6f95 | -5.728 | -51.65248 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccb6d1d5-8923-37b7-9e55-aa0d716f5c2a | -9.08613 | -50.46022 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee56f9a2-de13-3648-a670-b0edd1b39571 | -10.31156 | -48.80679 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d15d1ce7-4ef9-3051-b61f-3317c9b2f440 | -6.74503 | -51.96077 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44fecaba-f8ba-358b-a639-a765ffd41fb8 | -8.20093 | -47.15199 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 910b2c61-44c6-3760-9e49-9f95b38332ba | -10.56532 | -51.99365 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 944eca73-498e-3c05-b1d3-28cebb9b2efe | -9.10614 | -46.98569 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc4b3027-a6e1-3995-afa8-79fe25131e40 | -12.18915 | -53.86583 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 649a2816-0738-3aa9-a047-6994a1b41aad | -8.51952 | -45.71308 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1440b9a0-bfab-3342-a82e-6f058e093b80 | -8.3858 | -47.99209 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06090269-76f9-3122-8228-483473bf092f | -9.82885 | -46.05381 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bdf2b32-4dce-3fe0-8fdc-2fd59f911483 | -12.18304 | -53.88237 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a66a4c-269e-3050-bcdb-d9fabcb69590 | -7.10219 | -50.76173 | 2025-09-10 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5623bddb-ebf3-3bf4-b704-3bafbc831e33 | -9.21113 | -50.55365 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd8f679-a3d4-346b-9a7f-745f4d3c4f26 | -9.80776 | -47.76516 | 2025-09-10 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d394180a-6621-3b75-9069-ae1b2b907f17 | -8.86237 | -45.85249 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b1f7051-301e-3b24-abab-0edc1efc8061 | -9.51209 | -46.54626 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8979f5e9-7314-345f-8c2f-f4ef3317ff75 | -7.74246 | -50.72492 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91c0fd78-f9a8-3cf8-8f53-5ad3ee8a773a | -9.99777 | -51.70655 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9783f71d-9ef1-35be-ad32-fd8987a3d035 | -10.05125 | -59.36482 | 2025-09-10 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe3515e8-637f-368a-bc77-b953643f8ac6 | -11.49454 | -55.4998 | 2025-09-10 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8be3ab87-9321-3545-96e6-4ea8940d82cc | -11.18356 | -48.37416 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README91.md)
