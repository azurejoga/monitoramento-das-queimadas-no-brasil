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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013847de-b1a9-31d1-a6cf-20025959f10d | -19.4899 | -42.8746 | 2024-10-04 02:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 8738c64d-e7e7-3b91-bcdb-2c1474c42b80 | -19.8516 | -42.3738 | 2024-10-04 02:16:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| 60518260-eb3e-36ae-9c0c-092e47eefaaa | -20.121 | -43.5219 | 2024-10-04 02:16:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.1 |
| bdfc3605-31a2-35a9-aeae-61c464a3b3b2 | -20.1218 | -43.4969 | 2024-10-04 02:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 0ef28f3a-2e19-357e-a2da-95991d19b13c | -19.9901 | -48.7144 | 2024-10-04 02:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 138.7 |
| d0c47bab-4425-3417-9369-17bcb7482b9b | -19.9907 | -48.6913 | 2024-10-04 02:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 2ab45156-cc2c-31d7-9c44-cce5f93bdc68 | -20.1416 | -43.5162 | 2024-10-04 02:16:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.3 |
| fc387155-65a9-3953-af1a-05975db9b6ce | -20.0104 | -48.71 | 2024-10-04 02:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e6debdeb-10eb-36dd-b533-b152556bc841 | -20.0111 | -48.6869 | 2024-10-04 02:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 221.7 |
| da45f847-5766-3a7f-a7db-6b8d52e229ba | -21.7773 | -48.3976 | 2024-10-04 02:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 24a50506-4aec-31b0-a003-0e62cf0832a3 | -21.778 | -48.3741 | 2024-10-04 02:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3f158cbb-5952-3355-bc2d-76b6538d2a6b | -21.7981 | -48.3926 | 2024-10-04 02:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 554ac109-d4aa-38b1-8a90-8056c9d1de11 | -21.7988 | -48.3691 | 2024-10-04 02:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 05a6fe44-40fd-3ef2-96d9-779f42318075 | -21.8196 | -48.3641 | 2024-10-04 02:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ca9ef750-81b8-33e2-adae-c19b78b72f1a | -21.8397 | -48.3826 | 2024-10-04 02:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e9d6028f-f743-3ba7-81d1-112e3bfcab69 | -22.2684 | -51.4941 | 2024-10-04 02:17:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.2 |
| 7f4c8975-23d7-31b4-81ac-32c2617d3f97 | -22.269 | -51.4714 | 2024-10-04 02:17:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| c610036e-93e3-3c6d-8f59-287c161854c1 | -12.4572 | -63.8326 | 2024-10-04 02:24:32 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a520c2c3-dd06-3e09-ba0a-c930fcc8e884 | -12.4516 | -63.850899 | 2024-10-04 02:24:32 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ffd37281-345b-3f3e-94d4-b7c9b081d519 | -10.9231 | -68.352402 | 2024-10-04 02:25:15 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f89630f1-0f71-3c97-bf97-c2676334d743 | -2.9014 | -50.7142 | 2024-10-04 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9c5c4927-f76e-3d3b-a51d-b9e9bba91e5c | -10.4724 | -68.670998 | 2024-10-04 02:25:23 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9459c083-b571-32d9-babb-c75bb8b4f837 | -10.4744 | -68.679497 | 2024-10-04 02:25:23 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ba321d43-d83c-3221-b1f6-f41bb66a96ac | -3.2534 | -50.3689 | 2024-10-04 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a1bd9141-4904-35f6-9186-3558d661e596 | -3.3085 | -50.43 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4d8c48d0-aa00-32bc-8508-a59b922c2def | -3.3084 | -50.451 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 221.1 |
| b3a42ca1-b2a4-3fc4-b331-ba75661e94a2 | -3.3083 | -50.4719 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 9f17459d-2f79-3111-ad16-5ac3c7ee2007 | -3.29 | -50.4306 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6606cf9d-8031-3630-948b-ef2b801ed698 | -3.2899 | -50.4516 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 247.1 |
| 2ecbb8fd-e1f4-3229-a25b-86d07b484d3b | -3.2899 | -50.4725 | 2024-10-04 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 7619bac1-acdd-3113-9694-b82b001f5fae | -3.404 | -42.2858 | 2024-10-04 02:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 51e1cca9-599c-37ad-b31f-7d1c000d1e7d | -10.2129 | -68.234001 | 2024-10-04 02:25:26 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b0730ae4-ed8a-3e3d-8e2c-e31172949400 | -10.215 | -68.242996 | 2024-10-04 02:25:26 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9292e4a6-9b6a-317c-b22e-7dbfe2ba4a51 | -10.2172 | -68.2519 | 2024-10-04 02:25:26 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 98e0ec2a-b9b6-3590-8462-9e40f8ac3184 | -4.0949 | -48.4894 | 2024-10-04 02:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6db9604f-1c07-3dfd-9d0e-e190c1d1201d | -4.0763 | -48.4902 | 2024-10-04 02:25:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8b8986e6-672e-3e0c-874c-96668f72d353 | -4.5375 | -43.304 | 2024-10-04 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a68a1f38-4089-3c2f-bb58-c611ae621291 | -4.6873 | -45.8504 | 2024-10-04 02:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 31e9d101-a694-3e9e-a9cb-e662ad02c0da | -4.6872 | -45.8727 | 2024-10-04 02:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 476.4 |
| 774c61f6-0e4d-38af-85d8-5616991e331b | -4.687 | -45.8951 | 2024-10-04 02:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 267.8 |
| baa204f0-f794-355c-803a-c138964c741e | -4.6686 | -45.8738 | 2024-10-04 02:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 294.2 |
| da68bbe2-5a38-3379-834c-9d7b57139103 | -4.6684 | -45.8961 | 2024-10-04 02:25:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| c3d421c5-30ae-384b-9502-97cce3b62551 | -9.5959 | -67.4758 | 2024-10-04 02:25:33 | METOP-C | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fbd08509-0676-31e3-a9c2-15a4bc274ee9 | -9.5452 | -68.508598 | 2024-10-04 02:25:38 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d2e3877f-1d42-3cf9-9b12-a90067c0ca88 | -5.8216 | -44.1196 | 2024-10-04 02:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6f0e5f32-ffbf-32d7-81b7-0d14242513f9 | -5.8214 | -44.1426 | 2024-10-04 02:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8b262ce4-08ff-359a-a8e2-6de302c0f7d1 | -9.0642 | -67.497597 | 2024-10-04 02:25:41 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9579da3e-575c-3b1e-8df0-8a8f6783b68e | -9.0544 | -67.499901 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8d6ae1-069b-3d1c-b9f3-cb96dfe47a26 | -9.0569 | -67.510201 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 518c4ffe-1fde-3be3-bb2b-56ab602f16e5 | -8.9976 | -67.393303 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9afe1e43-d3ac-35b2-9332-0b690efe7c0c | -8.9853 | -67.3853 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c69cf7f1-af61-3ed4-b4bd-32751b436e96 | -8.9878 | -67.395699 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 438fafcc-25ca-3b26-b217-89255d168945 | -8.9903 | -67.406197 | 2024-10-04 02:25:42 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f26eeb5-c9ad-3e82-a3fb-92043773d722 | -8.8377 | -67.628197 | 2024-10-04 02:25:46 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02843e6b-8351-33ab-81d0-d764ebbdb8d4 | -8.8401 | -67.638298 | 2024-10-04 02:25:46 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d218e1d-893b-372b-b8ad-7954955a878e | -7.0529 | -71.7544 | 2024-10-04 02:25:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 3b7f7784-c58f-3221-84d6-791f5b5a496c | -7.0529 | -71.7726 | 2024-10-04 02:25:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2eb70770-976f-3074-bffe-40263fe095cd | -7.4999 | -34.8187 | 2024-10-04 02:25:47 | GOES-16 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| e4c40cf9-711c-331f-ab1b-aa9cc6542d11 | -7.4995 | -34.8464 | 2024-10-04 02:25:47 | GOES-16 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| fc896572-2295-39b6-9cea-cedd0cebf8fb | -7.8541 | -45.3384 | 2024-10-04 02:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ee83452d-7918-3ecb-93df-b9eddbe985f4 | -7.8539 | -45.3611 | 2024-10-04 02:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b65f401e-69f5-3c3f-95a4-883e1aac3e3d | -8.6448 | -50.0518 | 2024-10-04 02:25:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| fc149359-76ff-32a0-8597-8952e014f618 | -9.0853 | -50.9036 | 2024-10-04 02:25:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a2d3e634-0fab-3b35-9b97-fe7f654c8c21 | -9.1084 | -67.4993 | 2024-10-04 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 504e1cab-a04a-3395-82ba-e0d1abba1a72 | -9.0898 | -67.4997 | 2024-10-04 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4a15ad5d-a011-3744-8b4f-89083d4f19ab | -9.1041 | -50.902 | 2024-10-04 02:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 4fe8d2de-1d82-30f3-b62f-2325cea28c90 | -9.3306 | -50.7974 | 2024-10-04 02:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 02235907-d94b-3e55-8767-929ae59e11ac | -9.3303 | -50.8186 | 2024-10-04 02:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| e1ada1d6-e0fb-385a-95cf-06580c448ddf | -9.3118 | -50.7991 | 2024-10-04 02:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| fae802da-db94-3ac3-b42c-df4d83334e9c | -9.3115 | -50.8203 | 2024-10-04 02:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 607c064f-a97f-350e-9ec2-cfe9a671c9a5 | -8.8346 | -71.238602 | 2024-10-04 02:25:59 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e253db75-ee30-36b7-87bf-6f542278d66e | -10.8018 | -45.5927 | 2024-10-04 02:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 77e37db2-2538-3796-a090-0bc930526b14 | -8.2334 | -71.137199 | 2024-10-04 02:26:09 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ac13e421-1c0f-32fa-909a-f8e65336b6aa | -8.2351 | -71.144402 | 2024-10-04 02:26:09 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbe7711-53ec-344b-a1a4-28ecd291e18d | -8.2236 | -71.139503 | 2024-10-04 02:26:09 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e1e03eee-93d8-3c5c-93ca-eb885a0b6599 | -8.2253 | -71.146599 | 2024-10-04 02:26:09 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d8129ed9-ac43-3835-bf13-55f4ddbb5052 | -11.2566 | -60.5825 | 2024-10-04 02:26:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3df65250-e2d8-3433-aaf2-24d219345e23 | -11.6181 | -64.9818 | 2024-10-04 02:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3255ea27-cb2b-366e-b9b7-9b912e8c8bee | -11.5992 | -65.0015 | 2024-10-04 02:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0a9cc8e5-e53f-3f51-8939-beb2dc57cf2b | -8.1831 | -72.985603 | 2024-10-04 02:26:16 | METOP-C | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 261e5a0a-63de-32e3-bb4e-54a8843754cd | -12.6092 | -53.1129 | 2024-10-04 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 8b83d623-1db8-324c-807b-af9462e8872b | -12.5901 | -53.115 | 2024-10-04 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 168.3 |
| bf95315e-dd01-3801-a750-b8d0ab64c468 | -12.5898 | -53.1359 | 2024-10-04 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| ef1d8ebe-5ad4-302c-8303-8257835916d4 | -12.4227 | -62.9999 | 2024-10-04 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8bea6580-287b-389e-980c-c711f0c277d0 | -12.4225 | -63.019 | 2024-10-04 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4c5cdbb8-21bf-3197-baaf-4a83af947b82 | -12.4037 | -63.0201 | 2024-10-04 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 619cd0ec-6dc9-35ac-92aa-827bb5bca552 | -8.1733 | -72.987801 | 2024-10-04 02:26:17 | METOP-C | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab64cb7-6a32-3c47-a16d-ed7420510398 | -7.8083 | -72.787399 | 2024-10-04 02:26:22 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 981062c1-7e58-3497-86c6-ec77948cf917 | -7.7969 | -72.7827 | 2024-10-04 02:26:22 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7029b9-b848-3618-9653-6569e1dfb683 | -7.7985 | -72.789597 | 2024-10-04 02:26:22 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8a9db80d-ce98-3d59-bca5-bf74103c744b | -7.8 | -72.796501 | 2024-10-04 02:26:22 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ec85c2ae-09a3-3c4b-95d6-38740ff2dfc7 | -7.3624 | -72.504997 | 2024-10-04 02:26:28 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4f64cc-dfd3-337d-9d7b-5a52840ce713 | -14.7939 | -48.0275 | 2024-10-04 02:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 35e9d1ae-8863-30a0-b67e-24e7ebc1f4cc | -7.0238 | -71.750397 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b453b27c-60ff-3a63-93a1-8e5b29292770 | -7.0254 | -71.757401 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b57909ff-519b-32db-8f41-c0a6c8592492 | -7.0271 | -71.764503 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82448ae1-8e00-3a8b-9131-424de2e79ec4 | -7.0287 | -71.7715 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31cd3658-062d-32b4-aa65-ad7144ed3c4b | -7.0156 | -71.759697 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8b95810-a843-323b-9d1c-b7e53235a138 | -7.0173 | -71.7668 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d4d5b33-2ba0-3bb2-9837-d9d09bf3d29a | -7.0189 | -71.773804 | 2024-10-04 02:26:31 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README44.md)
