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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0978d293-beba-34d7-b89b-e4e0f6c7a931 | -4.42609 | -55.07965 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44e1cce9-e28a-30cc-aab0-1f9833d88ed8 | -5.47336 | -48.86576 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a34b0dca-522a-3af7-925c-5928c99cb3e4 | -3.00876 | -54.19279 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eb61a54-959c-31d6-837e-d9aa07611bc1 | -3.5911 | -50.03384 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdd7870b-0504-34d1-ac0a-3a127349651f | -6.91112 | -41.69526 | 2026-09-23 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9cf5a8a4-d2d0-3d7a-bd6b-86e2501f3c50 | -3.58727 | -50.03326 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7648cef-2b5a-304a-a25a-6dc794c4cd69 | -3.81925 | -52.39732 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b45282de-5942-3d5e-a72c-336cf773da4e | -5.80805 | -49.15326 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c006be6-08bd-390f-9e18-379b4273f9ac | -5.40718 | -45.84175 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcea1d3d-3785-330a-ac97-6a0a59543fb4 | -6.67477 | -42.56949 | 2026-09-23 04:25:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 30b21bc2-1a2f-344c-af65-583af8764901 | -6.62194 | -43.749 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 689e2546-c12e-31a4-92ac-cd3ece56a42b | -3.85198 | -52.30844 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3984e234-710e-3974-9a0f-c753d44cc2cc | -5.74962 | -51.9311 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 522ba9a9-2cbb-372f-b570-76839750d697 | -3.6277 | -49.99487 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a0603ec-0a3a-3f11-98bd-53c264c31b5b | -6.97187 | -42.60266 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 25029999-79a6-3882-8ca7-f45c4f9a6ff2 | -3.00608 | -54.17712 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02bf897f-ba4e-3fef-ad60-11e373dba023 | -5.7956 | -46.10041 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eba576e0-af64-3142-a937-97e8abc67915 | -6.89698 | -43.63113 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b365084-a2fe-3c66-88e1-f9903533ec23 | -6.61607 | -43.73997 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9950eba2-8076-371f-aaa6-4d1fccb8c054 | -4.38144 | -55.0267 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d952761-b405-3b0e-bb14-2fe635d3d6b5 | -4.2211 | -48.61854 | 2026-09-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82c13936-e8d5-3eed-8f7d-3dee4ad2367d | -4.83476 | -55.76961 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0238308f-a659-36c3-a8a2-dc26562b760c | -6.10515 | -44.15093 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3e9107b-8c8d-360a-bb18-c3d3c6de0e89 | 1.41245 | -50.74998 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0db9521e-d26f-3bcb-b9ce-e4e3cfc1388a | -3.20475 | -50.91743 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1dfb11b4-ff95-3227-932b-63c9b579f2ec | -4.92954 | -45.80532 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d2cf065-ea1c-31a3-9568-d4385388949a | 1.43733 | -50.82633 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c72b59-9009-342e-800f-edacc88f14db | -5.75787 | -45.11363 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f1fe188-9f8c-347f-9f23-72dd6670441d | -4.56806 | -47.7612 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f49058a-a3b9-38fb-8e40-07c299900b5e | -3.20882 | -50.91809 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acfa9571-b49f-3f89-82f4-6e33793f774d | -7.03116 | -44.65724 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 36c40386-09c6-3832-ae32-d37687d98315 | -6.52937 | -43.54655 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1774309-22e3-3327-8a5d-00b8721959b6 | -3.24358 | -47.25131 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efb3975c-361c-3f4b-aa2a-40de8ade5aba | -3.87066 | -51.18726 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f831fd8f-da6d-378c-8884-870a7bcd377f | -4.00505 | -52.08841 | 2026-09-23 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36591117-3391-34bc-96ad-0730facc6690 | -2.95896 | -54.08363 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b01b061-f367-3339-99c0-4b6e2702d4c0 | -6.61668 | -43.73597 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| eb58e77a-49f2-3126-8971-09d9826ae1fc | -2.63156 | -51.70218 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0efa3b06-4157-3c3a-ae79-adc5c6783671 | -3.59185 | -50.02909 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7882b228-480a-3ba1-b186-06614181f2e5 | -2.83299 | -50.47595 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a75801-bb82-3ae5-9363-5ece8b91ef88 | -6.98829 | -42.59583 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e159db9c-30c5-37e0-b5bd-39403b8ef36b | -2.9544 | -54.07984 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3de90699-99c3-3c7d-931e-f28b06fec690 | -3.25686 | -53.96414 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a666db-7d90-3dff-a25f-a60520522240 | -3.4508 | -50.61066 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4112d300-b113-30d7-8c1a-c82ed43a4c00 | -1.21591 | -54.55236 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63f25484-3247-3f5d-912b-5c6cc5fa83ec | -3.22777 | -53.95377 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeaa295c-6778-35f3-b995-79eca43e5767 | -4.99949 | -49.47412 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aff80386-d07c-38d7-a02c-3be7de714e7a | -6.11205 | -44.15205 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00a2044d-5961-3ee5-97c4-fb57d736618c | -6.57996 | -44.14362 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9beea66-43b8-383e-aa1f-9c874ad52ed5 | -4.4588 | -47.91741 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b424b719-08e4-3260-9a03-9d5901e65455 | -7.02888 | -44.64925 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ffaf75d5-637f-3c6d-854e-95db79407b5f | -6.00118 | -44.25943 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46b2e55c-a151-3a53-af78-17dcfedfc430 | -3.62389 | -49.99426 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcaf96e5-68a0-3f79-8873-8e7b2339ccaa | -6.44368 | -48.467 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afa85a3c-99fc-3638-b6a6-62250c90c52d | -5.80451 | -49.15269 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 225b0fd9-e052-3e45-bc39-800cf5df752c | -6.52224 | -43.54551 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c5a0c38-2ff7-314c-9391-e9379d2042d0 | -5.29195 | -49.26972 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cca4b06-42bb-37fa-8e6c-bcb2ba990061 | -6.89283 | -42.91928 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad94e047-bb2c-318d-809b-2817a0a3b780 | -4.10016 | -56.19984 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dae4a65-c41e-3415-b8cd-6571bba269bf | -2.23871 | -48.74681 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c09d2cf8-2b13-3e88-b432-2635df9d9b9d | -5.8296 | -52.02578 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7dbab83-7270-319f-a0b8-8015939f690b | -3.22508 | -46.93847 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 37c98841-4727-3724-afad-8eac0575e99d | -2.54956 | -49.10479 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d21352b7-05e1-3e7a-a4e2-8a678530b7f0 | -3.23277 | -53.95458 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227bdebe-01bd-3563-aaf2-bd573158a537 | -3.52322 | -44.32979 | 2026-09-23 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b627baae-b8f1-3388-afef-b2a02e0bfd8d | -7.08281 | -44.31754 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd11b4dc-8e2f-30f7-a3ad-0f1cef5b2edb | -1.72062 | -49.9846 | 2026-09-23 04:25:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 332bfaab-cd43-32e8-a19e-99030334f708 | -5.4152 | -49.27188 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7dfba948-673f-38a8-b498-93383f25e9f2 | -7.03458 | -44.65775 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be2f8c47-9b99-3cb1-8aef-21ffe2b95f99 | -3.25372 | -53.95201 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f7d293-af7c-33a3-ab6b-378d7b88e94c | -4.2193 | -50.66147 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc04080c-c871-3fec-b479-1f5998eca009 | -6.33877 | -43.3694 | 2026-09-23 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b3da3a0-10ef-310c-8ebc-88753e420112 | -5.77638 | -47.15681 | 2026-09-23 04:25:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dfda2131-3010-3306-bc7b-301e4134f6a8 | -6.1671 | -44.17994 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a201e50-4db0-3152-b21e-359d6cf20841 | -3.22236 | -53.95541 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81b515c5-0876-3640-8583-bbed305a6f5a | -6.57938 | -44.14745 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c80095d1-c2ea-35ca-a8ad-be4e4becf707 | -5.77136 | -43.76808 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9bfd7d8-4cd4-3d2f-8768-c7737810dcf2 | -1.63342 | -55.12498 | 2026-09-23 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21772679-091a-34b8-bce6-1a546afdfe2e | -2.17209 | -48.31887 | 2026-09-23 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 472970e2-013f-30b4-9ea0-8bd821d36be1 | -3.58802 | -50.02851 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d02f0af1-9c13-3479-bb79-ec13cedb1038 | -4.57836 | -45.65876 | 2026-09-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69b736d2-3b17-33c4-af37-73d4e4026f10 | -6.18577 | -43.34718 | 2026-09-23 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2f5792e-5fb0-3e27-bdee-b3103f0abfd8 | -6.38855 | -42.27829 | 2026-09-23 04:25:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 46ea824a-d629-3ac2-b528-979a788c3253 | -4.41858 | -55.48104 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef13524b-603a-3828-93d9-ffb3ab208017 | -2.76215 | -57.03473 | 2026-09-23 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a085e3c-95d7-3085-90a2-d6c6fb5785fd | -6.57759 | -44.6654 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dea7604-fd22-348c-8fdc-52c1fd8e520e | -6.61374 | -43.73144 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 4ca957d4-1724-3ff5-90df-502e3d922cb8 | -6.97253 | -42.59812 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 134111cd-aa16-36bf-b6e5-9c9c123b918d | -6.91916 | -41.12635 | 2026-09-23 04:25:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89292139-1a06-3519-a23b-45f1642ec182 | -4.25327 | -51.12251 | 2026-09-23 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42ad0cf3-8aff-3e6c-808e-5a28532c14a6 | -5.28397 | -47.25794 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8d2a1c01-21f5-3c92-867e-77495765f39d | -6.61314 | -43.73545 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a26ba329-c488-374d-b035-6e7685ec8871 | -6.60667 | -43.73038 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d2b90a6-5b77-3b7c-9d3e-27cc15d86ddd | -5.69819 | -47.39283 | 2026-09-23 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 095963ed-7c1e-3a36-9530-42cb283ef8d8 | -5.41726 | -47.47176 | 2026-09-23 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66b14ce8-1a6e-3fdd-baf4-525d99b8881a | -6.62082 | -43.73249 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2c41378f-98ff-3651-b7db-75073fa7d36e | -6.61428 | -43.75191 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 325640cb-5518-3951-b50d-d34f993afd46 | -6.1716 | -44.12624 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94ca0292-de7c-3cdf-8a6d-4d9a79457e3a | -4.28421 | -48.61134 | 2026-09-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3c47fc9c-4ff5-3875-b757-b18eaeadc0bd | -4.15145 | -50.4588 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README55.md)
