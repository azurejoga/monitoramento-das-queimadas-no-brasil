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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090316e7-b29c-3f70-92e1-b8ede030aca6 | -3.47795 | -47.68599 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2709aaee-63ac-36f2-9cd6-dc019a0f770b | -4.94457 | -43.78038 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63d458d9-d33c-3826-a9cd-a271acb6882d | -6.24587 | -35.14877 | 2024-12-03 04:06:00 | NPP-375D | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a89d694-fd36-35aa-8204-b214a902f141 | -0.60251 | -51.69129 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13a0bd53-d775-3012-b8a3-7d633d8be4ae | -5.11448 | -43.2118 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31bc76d0-3071-3fac-88c0-00f862dc8e7e | -5.12094 | -43.20848 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f93cfc0-8b96-3aac-a812-f0c039313c84 | -3.4622 | -42.00246 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4a197270-a87e-3181-b876-21f51eeec4ff | -2.66122 | -44.98457 | 2024-12-03 04:06:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca45d55a-3fce-38b4-ad97-39c21d927a94 | -2.48314 | -46.56915 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad658c78-3c29-325d-94f8-8e352e345d7d | -4.01612 | -47.00608 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 232d8205-9f19-360f-8812-c01a30451e83 | -3.82894 | -46.61927 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c535d9-536d-33fe-b66c-6cc753427ef0 | -3.54458 | -50.18469 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ebf9668-5c67-3f01-9584-ea97ddd4d0d6 | -2.59094 | -46.27096 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b680b6e8-a3f4-3fe2-a893-a2c90c263672 | -6.03112 | -42.52303 | 2024-12-03 04:06:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e3b60bd9-cb55-3d0b-89d2-0ea4e9582bad | -5.14142 | -43.23491 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53cd7d4e-403a-316a-82c6-f16013611349 | -3.20161 | -46.36556 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d770b2ae-dab7-3636-9b43-c205412ba876 | -3.34137 | -51.2047 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4caaf52-efea-34e3-8507-fd2e4d5bd7e0 | -3.50092 | -39.31675 | 2024-12-03 04:06:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6bcd2edb-7123-3d4e-9c3b-1618992f5130 | -6.11811 | -43.95654 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97ce6270-fdc0-353a-ae60-2a5186a4f9b4 | -2.43049 | -46.48569 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 754aa3a7-eec7-3a11-907a-71dd56cc6870 | -3.8338 | -46.61616 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 561c091f-db81-34c4-af75-682818f35a0d | -4.07807 | -46.68167 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09f7a2cd-83fd-37be-870f-2e4e1bdd6c8c | -3.54572 | -50.17773 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 642ac631-956b-33df-9a45-8a3d23f5e83a | -2.23111 | -46.38526 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac0aa56-560f-3b54-8e6a-427d38f033ed | -4.34415 | -43.74704 | 2024-12-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8acf80-4479-34b7-a502-c3e395731a9b | -4.06035 | -46.81701 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ddca5c7-eb7f-39b5-adf3-3b38e6e65b03 | -2.68039 | -46.11687 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 989dbab1-e141-3958-8078-f9a7a6797767 | -2.33026 | -45.85927 | 2024-12-03 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c50ad9-24ce-3bfc-b90b-a01c5b99b5b1 | -4.52738 | -45.73988 | 2024-12-03 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee950de4-be34-3eb5-9bf4-338762a4023d | -3.24838 | -53.65842 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc1a21d9-1cdb-3383-93df-fba2ce250775 | -2.58787 | -51.92092 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f41eecb5-2eb7-33fe-a15c-6c902c95ab8e | -3.34465 | -51.21648 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b929030-334a-3987-9001-c6b94eff2dc2 | -5.43282 | -45.5431 | 2024-12-03 04:06:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 903cdf33-54d7-3254-81d8-835a37b255fd | -5.79983 | -46.48719 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5fd77e84-46ff-3774-b184-a3a25e23ddbf | -3.2834 | -50.33328 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2907d961-15fb-38e3-8c1e-d666096ae00b | -4.09241 | -44.85733 | 2024-12-03 04:06:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1922ef2-93a0-36a9-8c62-21e8621b410f | -3.85156 | -46.66699 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a717dbbb-2044-3644-ad73-2fc8085268ca | -2.63621 | -45.77057 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b5b5aca-41ce-34c7-b999-d6c36d714f09 | -5.22363 | -46.10368 | 2024-12-03 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193e52e7-897c-3046-9a8c-5a54080c0aba | -4.04324 | -46.8678 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00db05c7-3fd8-30a7-b381-8f6ab32eb9e8 | -2.85342 | -45.8337 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b7f3765-0dd5-3533-99c3-38e38ee74faa | -1.96182 | -45.83562 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f91e87-ffc2-3044-a29f-88f6fc97c75b | -3.86575 | -43.35636 | 2024-12-03 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 342fbff0-91b1-31fb-abc0-a56fb7965d94 | -4.03623 | -46.93763 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c8e3d01-ef28-3b8b-bc34-cd0e9303c851 | -3.01395 | -45.6175 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e41ee829-6e84-310e-9356-601aa8685437 | -4.52822 | -45.73475 | 2024-12-03 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf73e565-ddb4-3697-a276-5034293f0b48 | -5.38051 | -43.07381 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85929b3d-2ee5-39c0-98fe-c09d2660e213 | -1.07811 | -53.46194 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b8c1c5d1-ac2b-308a-80cf-89f8bd982c55 | -3.90165 | -45.0103 | 2024-12-03 04:06:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34a097b4-76b8-3db5-a822-6a2b7da5a65a | -2.20898 | -53.78472 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d77ebbb-352b-3a2c-a0c1-2d6d518cf568 | -3.25474 | -53.62249 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35a71a3a-141b-31ee-b408-c59ca08106ec | -2.42797 | -46.48641 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0874aa32-385a-3912-859a-e09fadc78e88 | -3.58991 | -53.05046 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 005c8515-7f8b-393e-a6d9-3098700e7380 | -5.19733 | -43.73515 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3de7bf5-f44b-3e58-8691-e8d722e15a5a | -4.25774 | -44.14726 | 2024-12-03 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7868d57-4e66-314c-ab45-54255cf18983 | -4.16944 | -48.59212 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62bdd27e-c75c-3019-9d4d-54efaa13eeaf | -2.48015 | -46.56026 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 843a2e24-6de3-3574-a351-c8e186e107f7 | -3.95622 | -44.05157 | 2024-12-03 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d3633e-4b12-3686-83de-a95695194f65 | -3.75298 | -48.15598 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 015b8a94-4f85-399f-afb7-bb8734fedd25 | -1.74207 | -52.62352 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8235589f-775e-31c7-932d-85840f9a5af9 | -3.25423 | -53.66002 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 560dfbd9-4a17-3e5e-9291-80e0fb80f416 | -5.38422 | -46.36258 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b68af063-bc54-379a-b286-f06d5a687567 | -3.92504 | -52.38509 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3af34ce5-5295-3573-a898-64b5f0129892 | -3.28244 | -46.13484 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a07d0bcb-3b8c-3b13-b838-06d0902a6518 | -3.70154 | -51.83237 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f551a94-4062-307e-92a6-79f2536dd2f8 | -1.07223 | -53.45464 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c02f74eb-8d67-3181-8d69-15073f2e3d6b | -3.89783 | -45.00969 | 2024-12-03 04:06:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20cb4939-957f-3a73-9b66-404b010ceeef | -3.02031 | -54.03341 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 955c4c78-c914-3cbd-a19e-53ea09695ee5 | -5.80045 | -46.48352 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3d53220e-ebfb-300b-ad74-1940adf79f6c | -2.62219 | -46.96109 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f45264a-4421-3344-b6e0-ed6da5bc0a03 | -5.70022 | -45.04599 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2f397b0-df20-3bb9-b50e-5d8ae39e35f5 | -1.75257 | -52.80182 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 387ae67a-1fe3-3345-8336-a76ed6a8dbc7 | -2.21146 | -53.7793 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afa96125-32be-3967-9244-7d09fd80c46d | -1.3662 | -47.68339 | 2024-12-03 04:06:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12ad349b-0d51-3060-bca9-cbf2591be2c7 | -3.16186 | -46.55175 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6abdebed-b4f9-33f4-98c5-164652ba7c2b | -5.80575 | -46.47687 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e5bf69c2-1e95-3c1a-8f77-5b156ce9d355 | -3.33544 | -45.60819 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98fdd578-27e7-3d9c-8431-aa1b02a47136 | -3.28413 | -50.33007 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53e355cb-0897-30d7-a371-1cd038be9f41 | -4.19285 | -51.18896 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2436ed8-712a-3e49-8a6e-ad97e2ffedf3 | -2.93025 | -46.77861 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 602f6773-d096-386a-8f9a-5d58598a85fe | -5.53053 | -46.46084 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9bb9b84-07aa-3a56-89b9-19c2923cc366 | -1.94521 | -53.34484 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 936ef625-b7f1-371a-8f54-f0640b45ed4b | -4.94521 | -43.77642 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a405fc-80b6-35e4-a62b-f08ee0f1c444 | -2.8545 | -45.83458 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cb82861-724a-3318-8055-1a753a8c327d | -2.66493 | -46.10654 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ed7879d-0f7d-32de-8c6e-aac6629a998b | -3.25369 | -53.62844 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f2a0eb4-c6c6-3159-9935-61477ef31077 | -4.0541 | -46.99141 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baa43bf5-eea1-38d0-afb4-803fde37d04f | -4.43469 | -45.35131 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f812e23-05d4-3d39-8f1e-72af5b1e568b | -3.46557 | -42.00299 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 52c36916-70c0-31d9-8797-95ee6c393e31 | -3.60227 | -45.59811 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079fbd4b-acff-359e-aba9-6cb1df8d9186 | -4.92859 | -43.03748 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06062f5b-06fd-32f3-92d0-911fc1aab50f | -3.08437 | -53.38517 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ce6b2f17-b04d-3695-bace-914156cee774 | -5.81102 | -46.47036 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a80b923a-7c67-3777-bc84-a50d15ac35e3 | -3.54713 | -50.17767 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f4d669b5-a0b3-3c4a-aad2-6af7a4ec6edf | -3.54171 | -50.17671 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b17d26c4-bcad-36e3-859b-e5e69ad886fd | -3.68453 | -40.15703 | 2024-12-03 04:06:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd2f4ed4-7e30-3b6b-a435-aaae5e70ebc2 | -4.80376 | -44.9966 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08bd7e5d-6b75-3de0-851d-e63d50adc37f | -3.34649 | -51.20991 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 753a97e9-cea0-3005-897a-016512dfe9ad | -0.61198 | -51.69186 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d151876e-2088-396e-8a6e-028be7d5c51e | -5.82607 | -46.35561 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
