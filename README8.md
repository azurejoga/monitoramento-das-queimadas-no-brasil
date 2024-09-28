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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e631ad3-a6f3-3668-8f6d-d9b2ad498970 | -6.359 | -44.7188 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef701d04-c095-3f27-b37a-771768d27f98 | -6.5773 | -45.706402 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f83fbafd-c27b-3a11-a68b-0093d3856b13 | -6.579 | -45.7141 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 037fd3bd-8c58-30db-a97a-9a784f340bb0 | -6.5675 | -45.7085 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24798117-29be-3fb4-a5e0-e679375aab66 | -5.8933 | -42.778702 | 2024-09-28 00:14:37 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f10e3ef-028f-37cb-b1a8-0ceff7491fa3 | -6.0329 | -43.626701 | 2024-09-28 00:14:37 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3feec9cc-858e-39ad-8ea4-a1714fc05e12 | -5.9274 | -43.340801 | 2024-09-28 00:14:38 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e992f65-cde4-30d9-a5ab-374d15376961 | -5.9258 | -43.3339 | 2024-09-28 00:14:38 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6fecf2-38e0-3290-bd4b-9a305a27f0ba | -6.46 | -46.154499 | 2024-09-28 00:14:40 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aed397d7-1a4d-35dc-a57f-e4909675a42e | -6.3949 | -45.951099 | 2024-09-28 00:14:40 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5965c77-accc-38dc-832e-29fe5fc31052 | -6.0948 | -44.687099 | 2024-09-28 00:14:40 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7f1ce1b-c223-36c0-bc83-6acb9d9aec12 | -6.0964 | -44.694199 | 2024-09-28 00:14:40 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6386e3-38a5-31c8-80dc-694274b5cef0 | -6.098 | -44.701401 | 2024-09-28 00:14:40 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1dcbd4d-85a2-3ab5-a0ff-cab2939bdf1c | -5.6968 | -43.1404 | 2024-09-28 00:14:41 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8adf038b-f04a-38f0-9de8-d0d5d3292814 | -5.6983 | -43.147301 | 2024-09-28 00:14:41 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| eebcebec-c6a0-3aa0-9790-d125fce3ed5a | -5.8305 | -43.642899 | 2024-09-28 00:14:41 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0feae59-ecc7-32ce-a9ae-73dbd8ec2bc8 | -5.8321 | -43.649799 | 2024-09-28 00:14:41 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04d86bbc-42c4-3c77-ab99-af2cbb8fbd7b | -5.8783 | -43.8559 | 2024-09-28 00:14:41 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3d5a478-d6e8-3511-8d6e-df7a9ab1a4ba | -5.8685 | -43.858101 | 2024-09-28 00:14:41 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7f8d572-c38e-30ea-ad9b-edb4617ae6c0 | -5.7886 | -43.731499 | 2024-09-28 00:14:42 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7376e00-501b-36c2-a27a-7c2247c2e708 | -5.8003 | -43.967201 | 2024-09-28 00:14:42 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 376481be-e75f-3fab-9f93-e49417e8a3cd | -5.8018 | -43.974098 | 2024-09-28 00:14:42 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7568d0e-b344-32ff-8d54-9d6b26bcab67 | -5.9832 | -44.555599 | 2024-09-28 00:14:42 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78451ee9-2609-3a6a-b287-ffab370e5876 | -6.1748 | -45.418999 | 2024-09-28 00:14:42 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57dd7756-408e-3b1d-95d7-ca0380b7f546 | -6.1764 | -45.426498 | 2024-09-28 00:14:42 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 092786dc-1289-32a0-836b-f799069edda3 | -5.9718 | -44.550701 | 2024-09-28 00:14:42 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6c99035-67d8-3017-a05c-efacf7744b13 | -5.9734 | -44.5578 | 2024-09-28 00:14:42 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| baab45cf-4422-36e5-953b-1dd1e6246fb2 | -5.9749 | -44.5648 | 2024-09-28 00:14:42 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f87d3bf3-b35e-3f7a-9bdf-bf8177f3f70e | -6.165 | -45.4212 | 2024-09-28 00:14:42 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c66a1a-b188-3e3b-ba26-43c00ea9aca4 | -6.1666 | -45.428699 | 2024-09-28 00:14:42 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3e58630-8717-3abc-b06d-b192315ae34b | -6.1683 | -45.436199 | 2024-09-28 00:14:42 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d173203-3542-38db-9a72-686f792ff852 | -5.4481 | -42.587799 | 2024-09-28 00:14:43 | METOP-B | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5df0e7c-2f3d-30c5-9b5b-8269ed6e11da | -5.4497 | -42.5947 | 2024-09-28 00:14:43 | METOP-B | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 352387e3-86d8-30ef-9928-be73fdb96ecf | -5.7951 | -44.127899 | 2024-09-28 00:14:43 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1cc52d-eda9-3603-af08-7176d18c7416 | -5.7966 | -44.1348 | 2024-09-28 00:14:43 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4e4be87-d4b6-367c-abd9-40f5084d6cbe | -5.7177 | -43.920399 | 2024-09-28 00:14:44 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faf1fd6d-d3df-39ee-8458-fc9bafec54ed | -5.8102 | -44.3801 | 2024-09-28 00:14:44 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a36e06b-ef33-34d5-8f26-d345e6ef9888 | -5.6309 | -43.946899 | 2024-09-28 00:14:45 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7e80807-49c3-3529-9608-f5fdcc3f423c | -5.7639 | -44.4491 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d902f72b-7247-3476-8ae4-04dda7ae9f4b | -5.7654 | -44.4561 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd602230-b604-35eb-b479-699b4165b7a2 | -5.767 | -44.4631 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed099e9f-532c-368e-80cf-ecc643e67c6a | -5.7686 | -44.4701 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cec84cd7-46f4-3655-8719-fb9bd35f5997 | -5.7541 | -44.451199 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b544d6ed-abfd-3a8f-ac04-9e7a36b868fc | -5.7556 | -44.458199 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0173d6f8-73cd-354a-8cb0-491f28d09df7 | -5.7572 | -44.465199 | 2024-09-28 00:14:45 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59d41abf-41ef-3870-bded-649367aa9955 | -5.6443 | -44.190399 | 2024-09-28 00:14:46 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2b6286f-4695-3e76-a398-28908248daab | -5.7885 | -44.836899 | 2024-09-28 00:14:46 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1aee8a2-1ad5-3012-a171-c69a26fd1d37 | -5.7901 | -44.844002 | 2024-09-28 00:14:46 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bed96bb-5065-3b2b-829a-69dea9602d1e | -5.9781 | -45.692001 | 2024-09-28 00:14:46 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1acf624d-4e0a-30dc-ba61-1d60822d1a39 | -5.5787 | -44.081501 | 2024-09-28 00:14:46 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 919cdbdc-5068-3f6e-9270-e063ab2e7880 | -5.2998 | -43.070702 | 2024-09-28 00:14:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d38bf03-6a92-37dc-abe4-a1497bc2be35 | -5.2983 | -43.0639 | 2024-09-28 00:14:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1450ed9c-dff2-3430-b5ef-39edfa967db2 | -5.4014 | -43.429401 | 2024-09-28 00:14:47 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41fd0f2d-6f80-32f1-b73c-5c0ac4a12b79 | -5.5544 | -44.202999 | 2024-09-28 00:14:47 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0df2bb3b-54ee-3365-855f-8acf241f715d | -5.1323 | -42.8769 | 2024-09-28 00:14:49 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1696ba48-ae9c-3123-afff-1c9cc8c029f6 | -5.1339 | -42.883801 | 2024-09-28 00:14:49 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 823d33db-44dc-3b92-8cc8-bf3ce033cfd3 | -5.1354 | -42.890701 | 2024-09-28 00:14:49 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d87eda0-7de2-36ef-9c53-fbf4ee3eed2c | -5.7679 | -45.531601 | 2024-09-28 00:14:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d48ec5c0-a1fd-3f67-9a91-7f5a16f7e905 | -5.7695 | -45.539101 | 2024-09-28 00:14:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58e4ef46-9287-3071-98b0-2b0e0d1eb7cf | -5.7712 | -45.5466 | 2024-09-28 00:14:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9ef82c1-b697-3e7e-8327-ea3e42cedcd4 | -5.7581 | -45.533798 | 2024-09-28 00:14:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89edc745-79a5-382a-8c68-baa82c14a0ad | -5.7597 | -45.541302 | 2024-09-28 00:14:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 748219e9-58e4-376e-9dd8-ffddc373f872 | -5.7614 | -45.548801 | 2024-09-28 00:14:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4653a976-bc35-34b3-86a5-60c8193edd4d | -5.5547 | -44.665001 | 2024-09-28 00:14:49 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35737378-9a90-3d06-a957-8bdaed8b259e | -5.5433 | -44.660099 | 2024-09-28 00:14:49 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86927b04-531c-3a99-97ba-d7aa9312c161 | -5.5449 | -44.667099 | 2024-09-28 00:14:49 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41424357-14da-37ec-b6f8-ad0604ad4e37 | -5.5465 | -44.674198 | 2024-09-28 00:14:49 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95ad2247-e8ec-37c5-b3c1-c82322c5a849 | -6.1126 | -47.241199 | 2024-09-28 00:14:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cebc813f-4c9d-3ce1-bb92-0eb2e8fe682f | -6.1145 | -47.250301 | 2024-09-28 00:14:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaaa6ff0-8327-3cbe-beee-edc481a92f41 | -6.1165 | -47.259399 | 2024-09-28 00:14:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3139aa25-3166-3a50-9605-35555b0e8c19 | -6.6432 | -49.7533 | 2024-09-28 00:14:49 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991968c2-31dd-3672-b8a9-f57b8f9fcc45 | -5.9392 | -46.542301 | 2024-09-28 00:14:49 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7db946f7-5e71-3002-91f8-1db60c92e56c | -5.941 | -46.550598 | 2024-09-28 00:14:49 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1c9ad95-a1f9-34fb-b2b3-772ae529a8b9 | -5.9714 | -47.1115 | 2024-09-28 00:14:51 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 221c4976-0242-3bd9-901f-f855c0beb8b5 | -5.9734 | -47.120399 | 2024-09-28 00:14:51 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2436fff3-645c-3580-8d0c-7430fd5f4f6d | -5.9753 | -47.129398 | 2024-09-28 00:14:51 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67f57694-187a-30fb-b75d-6fd395daeee9 | -6.0311 | -47.431801 | 2024-09-28 00:14:51 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23395ae0-b595-3460-8e88-e396443b953a | -5.3918 | -44.626999 | 2024-09-28 00:14:51 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4427580-a985-35be-b25c-e145993cb422 | -5.3934 | -44.633999 | 2024-09-28 00:14:51 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9436664-8152-3b7f-822b-2f013a45a737 | -5.3414 | -44.447102 | 2024-09-28 00:14:52 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58857c23-32bc-31a0-999a-731f00b72982 | -5.7966 | -46.547199 | 2024-09-28 00:14:52 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4af635b-78b1-3e1d-9004-e4be1d93f7ed | -5.7984 | -46.5555 | 2024-09-28 00:14:52 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2af988f6-370c-3d91-aa29-211d0e563b8c | -5.7107 | -46.4366 | 2024-09-28 00:14:53 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2d8e8e-ca8a-3620-a506-ba9b9de3e9c0 | -5.7124 | -46.444698 | 2024-09-28 00:14:53 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daec2fd0-f042-3c34-b93a-a094cb02576a | -5.7009 | -46.438702 | 2024-09-28 00:14:53 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1822f5db-b77e-3c62-b8b8-e0989dd5a401 | -5.7026 | -46.4468 | 2024-09-28 00:14:53 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f60f9d45-4eef-36ee-84cb-60e2f472c44a | -5.6678 | -46.335201 | 2024-09-28 00:14:53 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaefb018-36e8-388f-88d9-9c851ac209b7 | -4.8648 | -42.878799 | 2024-09-28 00:14:54 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df1256c2-5488-3ff7-84ab-15625523e4cf | -5.2138 | -44.4753 | 2024-09-28 00:14:54 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55c647b4-5939-3097-b06e-9f50e4b662ae | -5.2154 | -44.4823 | 2024-09-28 00:14:54 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff6f50f5-b1f2-3a2e-bd35-a3afd28b8c7e | -5.242 | -44.601101 | 2024-09-28 00:14:54 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc800e1-d63c-3c3b-a0f1-436e53dd58ed | -5.2435 | -44.608101 | 2024-09-28 00:14:54 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b07f76fb-6130-3186-bfac-ea9d3c20a158 | -5.2573 | -44.715801 | 2024-09-28 00:14:54 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 438ba635-53ae-3a4a-8399-1b3309aae568 | -5.2589 | -44.722801 | 2024-09-28 00:14:54 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75c55f67-0a6d-32ea-bbed-e81e79e67618 | -5.5957 | -46.241501 | 2024-09-28 00:14:54 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d2707b6-a413-3907-9648-0e94d1cfc9ab | -5.5975 | -46.2495 | 2024-09-28 00:14:54 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47a0b9df-28bf-3a96-ad2d-32454167dc8e | -5.2036 | -44.5215 | 2024-09-28 00:14:54 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6500d93a-9efc-3add-adc5-8fb584fbc140 | -5.2475 | -44.717899 | 2024-09-28 00:14:54 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d364f249-a51e-3847-9388-23472b74cd5f | -5.3883 | -45.350201 | 2024-09-28 00:14:54 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b036114-12c5-37af-af41-a42740a63b40 | -5.7543 | -47.056599 | 2024-09-28 00:14:54 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
