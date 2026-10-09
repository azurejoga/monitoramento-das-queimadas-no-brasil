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

## Dados Diários - Página 281

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cf047e7-233d-37ba-be50-64a9f024a1fd | -9.1832 | -43.38054 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| a2424800-7218-303f-a3ef-b3ae3cfdde28 | -9.00274 | -41.15798 | 2026-10-09 16:01:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 79714613-e776-3fd2-9170-c9eb32ddf895 | -7.48299 | -42.85102 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 10517f05-3118-3e31-a41d-026280b2c33f | -9.93113 | -44.79032 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 201c370f-69f3-3f09-b7fa-c6b86fa21ae8 | -11.05022 | -44.07917 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 074c80c7-b08c-354a-8b60-a82145875323 | -9.98605 | -45.92583 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e486650d-c214-3589-803a-62dd47246c0d | -9.42496 | -40.39637 | 2026-10-09 16:01:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d180aa9d-68f2-3524-80a1-b4879244f57f | -7.39906 | -44.75028 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42f7d379-895b-3df2-bd27-3c8b192fbcd6 | -6.88405 | -44.91367 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b816c226-23e8-3e39-96ef-a75105bacd27 | -11.25255 | -45.24488 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12b4c3c2-5360-37d6-8f2a-d9536766cf53 | -9.21397 | -46.67351 | 2026-10-09 16:01:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b6c1fbf2-a226-3ce2-88ff-cdbbd245fb97 | -10.99537 | -45.39505 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15bfb757-c853-3e60-9a5d-f0e06fd2b092 | -10.49238 | -47.33441 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 726034fc-cacb-3075-9348-ba0ea45b93be | -6.01619 | -40.98113 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8c52a1ae-d08c-3c5a-aab3-42922a0b516b | -9.11845 | -45.82987 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ef6263d1-7cf7-354d-b71f-3fb475fd6364 | -10.49327 | -47.2171 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 61f4337d-cd7c-38e7-b56c-1d97132ac8ae | -10.93532 | -45.37812 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5506e516-e672-3a86-b3b7-7350eb91a37e | -11.20313 | -45.26142 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7fd64f99-8996-3409-8cee-a220ae02ba95 | -8.94683 | -45.12577 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 47e16137-ed23-3f54-b1db-2a23781ff096 | -5.31089 | -40.80858 | 2026-10-09 16:01:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 181978f6-1dea-3131-ac5c-19f3013e8c0e | -11.11763 | -43.99893 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 75ee0ad1-b572-3ed0-80f4-0daf9431d64e | -10.28812 | -46.60542 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e09865c-3720-3930-b2d7-68eb290ec52b | -5.03067 | -42.73635 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ccd6e05d-b0e8-3802-9034-8c89bee751c9 | -6.3754 | -38.26439 | 2026-10-09 16:01:00 | NPP-375 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 3cf20e11-952c-3ce0-bd2f-a2832f190e3d | -6.99458 | -43.80708 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 077459aa-e685-3914-98b5-ee8f5c044e6f | -10.90994 | -45.39509 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6ac23cff-378e-3f7d-99e5-9cf720717715 | -11.21171 | -44.8561 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8286a832-61b7-30a6-a2c3-4119cc3f092f | -9.87506 | -47.48059 | 2026-10-09 16:01:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6c8c901e-9510-3e3b-9050-05254db49a97 | -9.07964 | -45.09859 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1bb57f87-129e-31ff-ae39-0ba200b1b775 | -6.0073 | -40.98206 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c627a4d7-20e9-388b-9939-4539dbe443a2 | -6.88367 | -45.02917 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b2b43170-14c5-37de-99ec-eb162c4c7568 | -10.85943 | -45.53175 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5ee865b3-eb43-39ee-b76f-f89b609b8fd0 | -7.21902 | -44.17036 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f49fd46b-2fc3-324c-a5e9-3b07c9005c95 | -9.91985 | -44.85966 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d851fb5c-1261-3986-8a68-3549a5095052 | -9.15201 | -44.78375 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2121443-17aa-375f-8533-990d33945a54 | -9.90427 | -44.83375 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2517cb19-1cf5-39e3-9165-81a35ffde7c0 | -5.48435 | -42.846 | 2026-10-09 16:01:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 6fa19d32-28a2-3b6a-9d09-ae9fa6a7b838 | -9.74712 | -45.68634 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 808614cf-76cc-303a-964a-0ee72be0fde1 | -5.5232 | -44.11005 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc14dcce-a907-323e-ad50-0f69ca89d1ff | -9.74631 | -45.68952 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4b4f3ed1-c432-3130-b7bb-f3004c78b2fd | -5.99889 | -40.98215 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 98c24b60-2777-3894-99ef-7774fb28b8a4 | -11.22251 | -45.31678 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 59dd6204-724f-3dce-8be5-7a13ce4a284d | -10.48771 | -47.23093 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 176db8a7-5865-3f5b-8e47-ba6015b8bc1c | -9.66796 | -39.04794 | 2026-10-09 16:01:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5c33ad90-4e62-36df-9905-c5db10ff080f | -5.84053 | -42.41193 | 2026-10-09 16:01:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7e44731b-1120-3544-b88a-7c92db5f00a2 | -11.0403 | -44.04622 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 0f389fe3-0b1c-35e6-a619-2a26a8a9e8b6 | -9.0941 | -45.1147 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0a0d29b7-2177-390e-bc02-f0edf793b644 | -10.48544 | -47.21118 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bd884076-f2ca-3021-a71e-abe368ef0465 | -9.77619 | -45.92942 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 31cafa94-4145-325a-8bf0-d0241e8b2109 | -9.72843 | -45.70202 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d8774e8-03c4-3f4a-957b-4a94b6f7de96 | -10.49875 | -47.32709 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4fb98645-05e5-3618-8581-07b57b9c4582 | -10.89518 | -44.80306 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 85fa119d-16cf-356e-82fa-9ab0af17236b | -9.83661 | -44.79064 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50a5bf27-3362-3136-bb7d-2d195eb453bd | -11.06119 | -44.02246 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1249e1b0-2858-3297-b5ca-bfa47927a7ab | -5.45 | -42.89163 | 2026-10-09 16:01:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 6b1c6c25-3869-3a7f-8906-406d81d86da2 | -8.99806 | -41.15865 | 2026-10-09 16:01:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d39f76c6-9236-34b6-9a31-3ffad5e6d3a9 | -7.42842 | -35.09021 | 2026-10-09 16:01:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e8d23810-f01a-3507-9f2d-eb19d5671220 | -6.04448 | -37.5724 | 2026-10-09 16:01:00 | NPP-375 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fe38a9a2-1e50-3164-8e54-eb0cc770413a | -9.03529 | -44.381 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bdd5aa06-f83e-381a-a1c2-1b3ada068bbc | -5.70055 | -41.75031 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| dd8ed346-2676-3dcc-9be3-8c81930957e0 | -7.47777 | -41.17546 | 2026-10-09 16:01:00 | NPP-375 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 977423dc-1b0b-363e-a8db-d4ad877d3bbf | -9.17949 | -43.39475 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 7f1d1069-73a0-3e6c-8ece-010e7ca82bf2 | -9.92156 | -44.87333 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8a20682f-0e8c-376d-8493-3f0bbd412435 | -5.98699 | -41.37766 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| aed4df64-b9b8-35d8-84ed-8eb3a9bfb243 | -7.64602 | -39.91936 | 2026-10-09 16:01:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 5118a7d1-1b7d-3d0c-a747-4c24d543063e | -5.78083 | -42.05929 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bdad3e2d-6429-37ad-8603-6c55fde4a9d0 | -8.98332 | -45.95837 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d873e9fa-2a1d-36f9-87f1-f7e19c28ff29 | -6.58941 | -47.36363 | 2026-10-09 16:01:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8adef574-3ae4-3aec-90d0-e83f8a0d0e70 | -4.98963 | -43.1635 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6df82062-e804-301e-ab00-ff000f53f52d | -4.57697 | -40.66991 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 8b7d7b70-7aa7-32c0-a86e-629515e7641c | -8.39497 | -39.55807 | 2026-10-09 16:01:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c002e90d-5ceb-35f3-8402-33fd50507581 | -11.21178 | -44.86278 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f80738da-ae0f-3dee-ac68-51a35c4fd69c | -6.00189 | -40.94303 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2e156bbd-7262-3514-9b00-9a5763c3329d | -8.89424 | -45.40246 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 356be148-1483-3ee3-9059-a1f7a67d1e60 | -11.04334 | -44.07147 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| dd1ac460-1031-3b0a-90ff-883a73c1c06c | -10.70091 | -44.20638 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d064ef1-9fc0-305c-afc9-033683f3cca4 | -8.98124 | -45.15255 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 402cbb4d-f31d-3523-af9a-04e114628de6 | -6.07903 | -43.9948 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f388f891-b15c-33c8-8487-a542a1de34de | -10.53103 | -47.29524 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93aca937-142c-3e54-a19d-684d3b257ebf | -6.88451 | -44.90526 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8dce3e1-703f-39d8-9f54-ffb7dc5704f7 | -11.07247 | -44.11515 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 400.7 |
| 413d51de-40b8-3d28-8a7d-4ef051278c3b | -10.94807 | -45.37674 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a68e12ab-1326-33d5-b30c-ed087d0225c0 | -6.96849 | -45.27898 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5a23407-44cd-3580-b48e-8eeddcc35033 | -6.59039 | -44.29889 | 2026-10-09 16:01:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc7b91ca-89db-3e78-a723-673ccbf050f2 | -3.60803 | -44.56754 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0fa2abf1-5179-3a55-b6b6-2bceb1b6174e | -3.59055 | -41.71332 | 2026-10-09 16:03:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b3560212-3537-3f98-8117-e5bff47fb028 | -4.16641 | -42.95991 | 2026-10-09 16:03:00 | NPP-375 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b6bf90d-b193-3a5c-a654-e864051c15e1 | -4.50606 | -43.62485 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a0edced-abf5-34a2-b6ab-a8b4cfc09b4e | -4.04486 | -44.52211 | 2026-10-09 16:03:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e88bb30-16a0-3134-8f65-64927c395dc0 | -4.35673 | -44.35577 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c581eef-80b9-3e15-9066-fd3b776cbc94 | -3.17143 | -39.59008 | 2026-10-09 16:03:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bf1d6d75-8015-3a98-a418-45acaa4bc8f4 | -3.18189 | -42.97118 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 87a3c33f-8cc2-3eb1-93eb-7bdc3e9f9499 | -4.15086 | -44.3323 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cb4631f9-e8fd-3d1c-aa43-4b31d947072d | -4.15137 | -44.33574 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 71744f9e-f9bc-3a37-a237-fa8eb82e81c6 | -4.49879 | -43.64817 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afd9ef13-8f08-312c-bf7a-7c5ffcc845d8 | -3.22526 | -40.03159 | 2026-10-09 16:03:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9ad884ff-21b1-3700-afcc-73c5fd3c5900 | -4.09199 | -44.12029 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a36b91e7-3835-3737-aeb7-d9242c66d1c6 | -4.50651 | -43.62795 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2fd30c63-28c6-306d-b953-07c9d3b76679 | -3.65939 | -44.80083 | 2026-10-09 16:03:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77a02492-d13b-3dd3-8ca4-63851e04c68d | -3.66616 | -44.77028 | 2026-10-09 16:03:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README282.md)
