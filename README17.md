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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e01ab5-f8d4-39d8-b6c7-cd04ef6e420d | -7.0167 | -43.643501 | 2026-09-18 01:02:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfc9e156-9571-3481-85bf-f7a378f85490 | -14.7699 | -47.1562 | 2026-09-18 01:02:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 702f5052-486f-3921-b4a0-f350400f1f3d | -14.9012 | -48.143299 | 2026-09-18 01:02:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4f4ca85-628a-38a5-aa93-ed7637b830df | -12.6239 | -50.892899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 317d039a-079e-31d5-8222-369e9e511746 | -5.1738 | -56.1786 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a008a9a5-b221-317b-8b1c-fc1ab5ba5c9c | -9.7091 | -54.823898 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de90d0dc-dfd4-3257-9a17-44c49dd7a76d | -14.1169 | -46.949001 | 2026-09-18 01:02:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5210cf97-7d98-3057-9e9c-ce49e6ca2aea | -14.8938 | -48.155499 | 2026-09-18 01:02:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7f6a0b-ffcd-35ce-ba3b-67fa8add2eae | -9.103 | -45.728901 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49418508-cce0-3474-95a8-7b8485ab0736 | -10.6366 | -50.271599 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c75a9c9f-01d0-3ae7-94ba-ac75a5fa2aca | -4.4272 | -55.526001 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 741cfa47-65d3-3d66-b7b5-49f84afbecbc | -11.1968 | -55.032299 | 2026-09-18 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85cc9f5b-3ffc-3d69-9cdb-b40da822c3ab | -9.7075 | -54.816898 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3b877c-96e7-324d-a75a-d21970e7f826 | -7.1095 | -55.1283 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5448da3e-8fdc-32ff-a2ed-54b1cc143e8a | -12.3737 | -50.708401 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56ef74e4-4dfa-3af2-aba9-948c251b6db5 | -11.1365 | -49.042198 | 2026-09-18 01:02:00 | METOP-C | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa713747-4a54-3500-be85-31c88e3da75d | -2.7429 | -57.6297 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb2af7ae-2882-3c66-a3ee-05aa30a7f3d1 | -10.6681 | -50.2729 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdf69af5-1485-3091-ac7e-f50f4ea2beee | -3.4787 | -54.719501 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb8e833-f580-354a-84cd-e6d4869349fb | -5.7509 | -57.594898 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaaba190-8508-34bc-a3e2-5cc25a8f97dd | -11.3032 | -43.401501 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d577029-cf10-3023-b60f-3687402ca862 | -7.465 | -46.840199 | 2026-09-18 01:02:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b11303c0-a3f3-3da0-a5c7-57d608722c6b | -3.448 | -58.194801 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0702ea31-a4fb-3e7b-b4fd-d497f2f6b666 | -8.9907 | -50.172901 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b05db89-4ec5-3ca2-ab82-569f95781230 | -12.4566 | -50.884602 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48a34518-3eaa-37f8-891e-a804dcb4094a | -10.822 | -50.181999 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb392749-399e-3616-9700-98772546b3ae | -4.0172 | -49.958 | 2026-09-18 01:02:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9907bed-4a27-350a-a2f7-526debb69734 | -3.2082 | -53.949699 | 2026-09-18 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47f915b8-4757-39d4-b9b2-c93470d12ffb | -5.7473 | -57.5788 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fae9272-b79d-358c-b03b-5378316e893d | -5.8297 | -52.087898 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02c74274-50c2-34ba-8470-aa225a1479a5 | -12.3223 | -50.7537 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4b8e24e-10d3-3166-ae8e-9d1882c18f83 | -11.8214 | -46.796001 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a8645ac-d0ab-360a-93d3-e7a569b1a2ad | -9.1126 | -45.726501 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca88107-9564-34b5-89d8-625a0f2c7d95 | -4.437 | -55.5238 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951cc650-f730-36fc-bff3-c20913f73231 | -4.4288 | -55.532902 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77943be3-b8d2-31e9-af75-a33f5683c452 | -5.6411 | -44.805698 | 2026-09-18 01:02:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a890493-b3ea-3dff-a12c-339d4e4d5efd | -10.6139 | -46.558601 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8659ec0-fa0a-36b9-9f25-63ef57505ae8 | -3.9687 | -56.1367 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed56a885-86e6-324d-9d83-8700e9c0e3a0 | -12.3932 | -50.703602 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c4ef975-bd2e-326b-b5c1-31449fcc46a7 | -2.5014 | -49.4254 | 2026-09-18 01:02:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34cb3f43-8c19-3861-9786-bbf8fcc3bc5f | -12.528 | -47.095699 | 2026-09-18 01:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1018f57b-04a8-3899-a631-c8296754c629 | -2.0528 | -52.170502 | 2026-09-18 01:02:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2050387b-8adf-3ede-aae9-ad6187c216cc | -12.4189 | -50.680901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65888051-473a-3ce3-ab22-31f59d4ecc0d | -12.4779 | -50.8876 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edb24e89-3f7c-388c-8ead-def419961829 | -10.6271 | -46.570202 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af438e56-904d-36de-b3ed-7a00b2df75c6 | -9.9589 | -45.687199 | 2026-09-18 01:02:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd817057-ede1-3444-9089-df1e828354a6 | -4.5404 | -54.9403 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7775c22a-01ec-3167-95c8-9b404c567b00 | -8.5145 | -48.503201 | 2026-09-18 01:02:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d06cb458-df1a-37d8-90c7-b68fbf573ff1 | -2.963 | -50.3354 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd84561-6d01-3e3e-90de-f39eac2b2530 | -12.4663 | -50.882301 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b576f4e-9836-32f1-afd5-0252bcf215d8 | -4.5667 | -54.919998 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ab0a02-7ba2-35a0-94d9-077bd8625880 | -2.9089 | -54.172298 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c78f0e2-9ad5-3119-a28f-61a098a7a207 | -14.132 | -48.723801 | 2026-09-18 01:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3cebf944-48eb-3227-b823-0d650a2e593c | -19.186399 | -48.770401 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13b49f28-5e6f-369e-8c9c-ea4547d39d45 | -6.0229 | -51.811001 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df8a065-4fd6-3f02-9c90-cfcad66fe69a | -9.5623 | -45.427101 | 2026-09-18 01:02:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85f44b11-f294-343e-9391-5aa043c6d09d | -7.6739 | -46.1091 | 2026-09-18 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53eea60c-5b8b-3881-b99b-670f599e28c7 | -12.3358 | -50.766899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e85f63fe-1e89-37e3-8436-e7e79cc54565 | -10.9459 | -54.094799 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4429794e-a5ee-34ad-ac44-4254585ee2c4 | -11.2718 | -54.1236 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5829f2ab-1f3a-3550-a2a8-6f00025c4856 | -19.182501 | -48.797699 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0737eaa-55aa-3f1f-b7c3-08369b796298 | -8.9371 | -51.470299 | 2026-09-18 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801bf8b4-d1df-31dc-99b8-788e9c63cc49 | -3.3654 | -50.469501 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c265fdb6-cad9-3753-a4c8-9b165ff16a9d | -4.5487 | -54.931301 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795e412f-057d-34fe-a0a9-ea643aee5a2e | -16.406099 | -49.964401 | 2026-09-18 01:02:00 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 92906a21-c312-38ea-9879-5204773a8bd2 | -6.5195 | -49.900501 | 2026-09-18 01:02:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94eed2aa-fd74-3e45-82ff-94c13655eda0 | -5.7393 | -57.588902 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d435a8a8-50ea-349d-929e-e59e94739ebc | -10.6326 | -50.254601 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca1de37-4472-36a6-868a-6c1f2d0bc316 | -11.2973 | -43.379002 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 209053ba-c289-3d74-83fd-39a5545c1c82 | -3.3751 | -50.467201 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5d6a7f-1c9a-378b-809c-4b4de0f273b1 | -4.0146 | -49.947399 | 2026-09-18 01:02:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be14ae70-a05f-3437-825e-8805b2354de7 | -12.3956 | -50.669998 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d81f4da1-8263-3777-9d7d-bb98f2601bb7 | -1.7971 | -47.837002 | 2026-09-18 01:02:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d761e2d-fc39-3d7b-8ee7-5b2c34228d94 | -12.2637 | -50.767799 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d907a33-edb8-3d3e-a607-eea0fb13d0aa | -10.6306 | -50.246201 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a145b65-ee11-304e-bf21-300dd49c6f42 | -3.3631 | -50.4594 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d77084b5-a84e-3c69-9253-90d5fb94c9ad | -9.156 | -50.000401 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a20e0ac-33b1-373a-b28d-d6221ce8c39d | -12.4011 | -50.693401 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e89a2ef3-0b4c-3e58-bd84-7ee616fe102f | -21.626499 | -50.014599 | 2026-09-18 01:02:00 | METOP-C | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da782e27-d212-3d57-9fdc-600eefa15d96 | -5.9042 | -53.516201 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b21c35-87b9-3d5a-aa35-792df5334a83 | -19.5515 | -47.6208 | 2026-09-18 01:02:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5a2be5-d6a6-3db5-9fbb-b4fb800bdc45 | -12.6318 | -50.882801 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0cb945f-2ac8-3569-893a-f31345f42999 | -11.2936 | -43.404099 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e38b4458-2d18-35ce-b0c3-f982e188b0d2 | -9.9537 | -45.344299 | 2026-09-18 01:02:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e21fe7d4-1116-3011-a38e-d781861e38ac | -3.44 | -58.205101 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3a42c3-7e0f-3048-a141-1524f266e8e6 | -3.0406 | -51.367802 | 2026-09-18 01:02:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0096a88c-bf43-3a71-8722-bb05129544d7 | -2.9605 | -50.325001 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8659ad0-572a-3c8e-bcdb-256808ae9f1e | -4.2784 | -55.551998 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb814abd-242b-348f-a375-c8e2c0847ce7 | -4.596 | -42.968498 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b53e1a47-d19a-31a6-a710-65d444cc8abc | -7.0263 | -43.640999 | 2026-09-18 01:02:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2028654-9bd6-3cb3-a4af-401801a14261 | -3.9194 | -55.740501 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e16c472-419a-3808-bf36-a43fc5ee5a9d | -2.8236 | -50.487202 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e85329e8-75b2-330b-b0cf-743546ff97e9 | -12.3517 | -50.746601 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4338e554-2708-3000-b25b-2457436386af | -12.4653 | -50.702599 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff08e050-2fca-3c67-9371-7fda27fc3300 | -12.3437 | -50.756699 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8402715c-cced-3240-a540-b8bb52ae3218 | -12.37 | -50.692699 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b87170d-5964-315b-a833-7e1394281d1f | -3.263 | -54.2757 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3f4c91-5fc4-3c0b-84bd-a2e8ae4df9d1 | -13.2568 | -46.9063 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2ea6ae4-5e11-3145-b583-e443a467e9ea | -6.357 | -58.284698 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f31f301a-39ee-3d69-9e63-57048250f990 | -7.6793 | -46.089802 | 2026-09-18 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
