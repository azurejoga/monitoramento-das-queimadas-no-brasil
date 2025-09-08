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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fcc278f-c7ca-3d1b-93b7-cf28091e6339 | -11.90816 | -50.98401 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e42ec86-9ba9-39c9-90ab-d5da406fc0a1 | -16.44219 | -49.28607 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4318a30f-9ca3-3b6d-bc2b-a16c3037d91d | -12.8351 | -52.9029 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4638475-c886-3c34-b6b7-3139429dba94 | -11.38609 | -50.42439 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df50c8fe-f604-393f-9a7b-60f82f57b280 | -15.96644 | -48.10564 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c035e337-b194-38ff-923a-db289d3e8245 | -10.99894 | -52.0581 | 2025-09-08 04:53:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b991ec5-4b53-304c-bfe6-c793e853ad8b | -15.00077 | -48.00661 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f77bc4f6-618c-37f1-9e41-272ac804744d | -13.00808 | -45.21509 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54784f59-2ed0-3f4f-92cd-fed5a82999b7 | -11.79334 | -62.74221 | 2025-09-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59242440-887b-3ce4-9832-3a65cece926a | -12.42208 | -63.89193 | 2025-09-08 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef74014e-6d23-317f-933d-7d25a39dcff6 | -13.54522 | -48.10999 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 048ff8d8-4b6f-36a1-ab60-8fb7d70bd368 | -15.73929 | -53.5359 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fab39e1b-891d-3130-9f79-4820f65171ac | -15.83362 | -52.26247 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bacc3d18-ceda-3f15-966d-15999f532383 | -15.49977 | -52.76981 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b933464a-8366-3a9c-90ed-96dc34dff5a5 | -14.7822 | -48.11108 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c42a78f-5622-34f2-8585-e6814e285960 | -11.36117 | -50.38946 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1926828-e78d-3f96-89c5-302ecf092b6b | -15.73313 | -53.5311 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9359e0c0-08d8-3d3e-91a4-4cb19c4896c4 | -15.5118 | -52.78355 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6608c7df-5998-3d3b-8120-2dafdb3937fd | -12.17393 | -43.94799 | 2025-09-08 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc8d1fcd-620d-369d-8132-9be17faa2e67 | -16.35394 | -52.93798 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ae470e-0223-39a1-8126-ef26f6e9a238 | -12.19861 | -53.90653 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f25a83a5-0b70-363f-872b-6b423aca519d | -11.86192 | -51.05888 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54351e78-dac1-33e8-88a1-3ccf542102db | -13.83187 | -46.29422 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 485245f5-1e03-3eaa-b8e4-6085eba09352 | -13.64735 | -43.80992 | 2025-09-08 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 77d38ecb-8ee1-32fb-950e-e174e5de0594 | -17.58877 | -44.5345 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bda7c00b-1f88-380b-ae35-b0d4b6f44828 | -16.94017 | -45.85303 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a5c662e-865a-3e99-8c0e-777f10b94da6 | -12.1964 | -53.89898 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adcac26a-0af6-3bcd-94a4-0d6856d4c445 | -15.2575 | -53.8008 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9612d78-06eb-318c-aa6e-b3bc6f228405 | -15.25361 | -53.80389 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49a01e70-32c6-32b2-939c-21d824c2f125 | -11.41008 | -50.38788 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 496f238d-6daf-3bb2-9b73-befb3ef68cec | -14.50502 | -48.81028 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c8b1b0c-4e0c-3fb5-853d-a1843cd35cdc | -14.78729 | -48.14256 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc6ab7c7-de71-3bbf-8c5f-53cfa9917523 | -9.1382 | -65.95689 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ef62dca-d9e4-3b51-91ad-406466aa2a3e | -12.72017 | -56.57291 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 287706b7-3f31-37d3-b587-cd7204905435 | -15.09286 | -50.11142 | 2025-09-08 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5dd8469a-7573-356e-9c00-b423ae32bbaf | -11.1197 | -52.02293 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51368d71-af7a-3c95-b86b-859fd5a47af4 | -11.38244 | -50.42384 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b243f82e-e5be-3ba8-9743-80242163c61f | -12.61394 | -56.97159 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18874d86-a4fc-3e72-8db3-1860139605e4 | -16.93669 | -45.78706 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bb6b6f6-b88e-33cd-9b42-3c15853194fc | -9.68707 | -63.17094 | 2025-09-08 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d970ef3-440a-323d-b0ea-b1b523ae0b6e | -15.73436 | -48.37649 | 2025-09-08 04:53:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 722117b4-f254-325d-ab45-88204281ac4a | -15.27292 | -52.38578 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c4bfb2f-9af4-39df-aea9-55f5c03e77c0 | -16.93818 | -45.77353 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9641e49e-4112-3470-b5a5-09ba5ace6c4f | -17.66846 | -44.19147 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a37963a-a29b-3491-9fb9-b4ec66140561 | -14.81927 | -48.10272 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b087324-582d-36d9-a5d5-62953589d9ae | -9.442 | -61.82108 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c04102f8-d110-3c0d-8160-92efe484d493 | -17.15211 | -48.67988 | 2025-09-08 04:53:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922f7f67-5cf8-31af-b136-a106cf141c48 | -11.20781 | -55.00767 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb6bfbca-346f-3a18-a1bc-36f01765e77e | -11.21507 | -55.00518 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f478c8ad-567b-3c70-874c-350765ae6415 | -12.85669 | -47.98306 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3dc55c9-eb47-3f87-98c3-8a225971730c | -9.13059 | -65.9611 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48fa5517-4352-35e9-a400-ebf90f176e63 | -11.63153 | -52.23353 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8ca5286-a245-390a-b176-4b738f5735bd | -15.66873 | -53.86641 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760dd8a5-3e96-3ea2-be50-de68668ad279 | -14.58872 | -48.08295 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2e88c5e-d035-3e6b-8229-7d01c6829b62 | -14.45918 | -53.51101 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2c12ef2-55b5-3afe-b036-626da7f1ef36 | -9.62896 | -64.2073 | 2025-09-08 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aa8a220-5261-3f9d-b407-47359d1ba9df | -12.85238 | -47.98225 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3716eaea-3c42-38cc-b073-2c4faa7d7834 | -15.68836 | -53.55434 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5ee2d8e-6e16-33c6-b87a-00563271b9f9 | -15.71309 | -47.51007 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71a5527d-c1b0-3d9e-ada4-9a9172d22009 | -13.83533 | -46.2944 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba4e2e8c-5543-3fdc-b1d1-6ff5ac7906f4 | -16.91015 | -45.83252 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d7f248a-7cba-34c6-bf05-9fceebb4a386 | -11.00968 | -52.05601 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cb05821-290e-34a3-bdbf-6e8d8b25272b | -15.37992 | -46.42321 | 2025-09-08 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db731731-ef33-3fae-a3d4-ed6b16f35677 | -16.44168 | -49.28999 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 011e6c3e-c207-372f-b5b2-c19df2547beb | -11.19913 | -55.06155 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0644f17a-88c7-3ad7-bcb3-da20518a8d10 | -11.49979 | -55.54409 | 2025-09-08 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d0fa0f4-d669-3f73-b6db-e51391a927ca | -11.20331 | -55.01431 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a471dd80-8954-3d34-814b-b2143effe471 | -13.72425 | -46.89887 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73aafa29-b4df-3599-b6a6-dd885b6ecdbf | -12.63795 | -56.97986 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdb43925-5650-34b4-857f-42f7a17b5fc0 | -15.75271 | -53.58363 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d84caca-5255-3933-b78d-b16b47bb7c63 | -14.52053 | -48.75681 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18e267a4-53b1-3622-b089-c37e6039df5a | -11.45131 | -49.25853 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1bf2e64b-2100-35b5-8fef-1d7c71c11078 | -16.3396 | -52.93987 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39a2df59-a139-3699-830d-b0f9dd6acb46 | -15.24859 | -52.38207 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cee7554b-79b9-3d09-8b08-507e90df4c81 | -13.81771 | -46.28656 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 96ea5011-106a-32cd-96ff-66f51f73b480 | -16.51856 | -45.10427 | 2025-09-08 04:53:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c69588-c576-38ee-b70c-7106b6afc51e | -15.38025 | -46.42039 | 2025-09-08 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ed72c4e-a28f-3c09-bd90-28f9550ff410 | -12.93113 | -54.76621 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04a4d802-8d17-3ea0-94cf-515a163d2577 | -12.813 | -56.51995 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55a24542-a423-3dde-9a6e-b8fc00f3dacb | -14.88027 | -55.81565 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0232fe70-066e-3f7e-bb5f-0ab19e735dc1 | -17.64651 | -44.7802 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e1a2687-0db7-3d99-a8d9-477493ba6575 | -11.04798 | -54.17261 | 2025-09-08 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84504198-2f95-3c28-bc5c-25b6ae8a585e | -15.19131 | -47.96042 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9884b38b-e4da-344c-9970-4fdf57419aa0 | -14.60102 | -48.09239 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04330033-4597-394b-8ba0-67f99f4f7b79 | -11.90673 | -64.97135 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f610ddc-351d-3153-80e2-32186f5e9b08 | -15.11647 | -52.34959 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58447e92-ced1-35e7-9376-c45f1b31335b | -12.94814 | -54.80894 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e2f2703-717c-32f3-ba5a-7c0cf75b0a5f | -13.01349 | -54.82674 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f0d5d31-fb2a-37a7-9272-b1c687ebd24f | -12.35639 | -63.64053 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b0ca005-e8b0-39a6-9724-38d0097c7b97 | -15.69229 | -53.574 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6ff32c0-34cc-37ab-8530-97c17ba0eba7 | -15.68891 | -53.55065 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 455a0b51-092a-39af-a6cf-3bb767c4e3f9 | -15.17228 | -55.98857 | 2025-09-08 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b98041d0-a7d8-3bf3-b428-f576d3e34190 | -13.67153 | -44.22583 | 2025-09-08 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36511781-7d07-351d-b3d1-f558bdd92ee0 | -11.38369 | -50.41513 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aaf55307-e624-38cd-83ee-d6dd30d47d02 | -11.22508 | -55.00684 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3045560-1664-3d6f-8793-cf45678926bc | -9.93536 | -60.10656 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2027a537-0946-3d57-b58f-1f690fbd59c6 | -9.94685 | -60.14494 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fd9fed5-c67c-3186-984a-57c851b08501 | -15.68554 | -53.55016 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 353e2123-3f8e-3dcb-ab63-db861e5d6f54 | -15.76595 | -53.55534 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f8c5b3d-b175-3f04-bcf6-c6e0c7e9dfab | -15.74713 | -53.59784 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
