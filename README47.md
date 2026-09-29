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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd2454f-8f51-3a89-9bbb-35e603705bd0 | -11.96281 | -50.92742 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f32c9af4-1b44-3853-87b5-49b73e61d5b1 | -12.15658 | -50.41138 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7025a4e9-00e7-3ef3-ae22-4c5d54a6b114 | -11.39789 | -45.40981 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c7d6d0e2-316e-3e58-90ac-77105fd676ef | -12.73301 | -47.26934 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9cbdec06-404b-3753-a396-2fed7a6b2d1e | -12.38894 | -50.22282 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c3367d3-8e49-31a5-97a2-c9da16375caf | -12.91083 | -52.06408 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8069c26-2e17-3454-b5ab-a9d0e635df33 | -13.48128 | -48.6116 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b65883d1-c055-37ce-8859-28d0d1648455 | -11.38169 | -54.04741 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48f800eb-5009-3955-b2b1-f34a0e5bafe5 | -13.22204 | -48.56275 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca1175c0-c71e-3ae4-97fa-1a80f9de6880 | -11.35224 | -54.04223 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75c0cf60-10de-3eaa-b665-1ab23305acf0 | -9.07328 | -49.86882 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5fb4654-0a44-3a03-875c-cf8b42312ea7 | -11.93237 | -50.88251 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f55d65bc-d695-3443-b589-0e3eedb7311e | -6.32051 | -52.62829 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abe02c48-950e-3e6d-aa2c-b8c5e4ccd307 | -12.14226 | -45.00184 | 2026-09-29 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db65c824-2f0a-3463-86df-fd15ff99eafc | -11.80918 | -49.0535 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 973e3c7e-3463-352d-a97d-ab86b5d40ad6 | -10.70886 | -44.4236 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ef2370-0652-3199-85f9-50f629c935d4 | -10.79988 | -48.74834 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c1393d0-35dc-3a30-ab68-e6c3da264073 | -6.91086 | -45.59304 | 2026-09-29 04:51:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a73daf-6843-35fc-b6fa-ddf22a434175 | -11.37507 | -54.04171 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b041aa3d-0a77-348e-a6b7-bf585265e8cb | -11.39893 | -43.44506 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2936a45-880a-3b56-9f0d-81a54f829fc0 | -12.17613 | -50.68992 | 2026-09-29 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 867ecaf0-b215-350c-ad25-d818da690f63 | -10.43547 | -49.37257 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 165919ed-15f8-3a94-9a56-05254c5a6820 | -8.63861 | -45.34677 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43ac392a-f089-3e28-866a-dd61ba22706c | -13.43325 | -48.61731 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39716988-ee50-3485-8528-b538e6531a72 | -8.54703 | -47.84605 | 2026-09-29 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2870a3ca-91e5-3dbf-af49-b507f9468d1e | -11.17118 | -44.79292 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e6397693-1ca3-37c7-9ad8-04f26f7e14f0 | -13.1426 | -48.54259 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b07da3da-9288-3d3c-861a-b581711db93b | -12.31368 | -50.29474 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e05e09d0-0495-3c12-8c43-907d3c1ee309 | -11.44343 | -43.46601 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff04bccf-a5a2-3257-9c40-132f83b5db42 | -12.04251 | -50.93679 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b32049d-9022-351d-9e18-39e783fc3cbf | -11.30632 | -43.54826 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a41668ca-13cb-33bc-bdc7-cb2a76a2f370 | -11.18723 | -45.14257 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3eb10ef1-311b-332b-b12f-1ba44138cdbf | -11.43879 | -43.46538 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5fd3327-15d7-3c73-94fc-367058a6ce84 | -6.15216 | -52.90704 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8565cf-622d-35db-b636-b8bfd5cbb240 | -12.01253 | -50.93185 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47a2c5e6-49b7-356d-87e8-8935d98180fc | -12.39561 | -50.2239 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1c027c4-09d4-3b18-926b-5d46e02c672d | -13.4807 | -48.61549 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d7b790a-6e59-3c2d-8612-006087b49123 | -10.71766 | -44.43542 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d0af07d7-e179-368a-8a47-b075ad12a3c0 | -10.8141 | -48.74679 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85fa9dd4-906f-3ae7-b3bb-0d6e4d44a634 | -8.73104 | -44.91901 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c9975a1-2b39-3134-8541-f7c436612942 | -7.63529 | -45.51646 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b63ba291-5765-3fb8-b175-b7268d2ab492 | -11.38685 | -54.03925 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55e9637c-d85c-30c2-bcb0-37b16ac1cd80 | -9.14348 | -49.98101 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6078d9c4-170c-3aa8-bc4c-bf840d78b703 | -11.93842 | -50.90889 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8080ce9-147e-37d1-9062-d7cbcfb4a017 | -7.84838 | -45.81341 | 2026-09-29 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| daa6e29e-4f42-39d5-9477-28d9ba985e7b | -12.78189 | -54.02489 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80af9b05-b380-3189-ac19-341fbf088282 | -12.00514 | -50.99953 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13b41451-6bb0-3cc9-bb01-e5b141e2bca7 | -12.60023 | -47.28759 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00b569d9-db00-3377-8f09-84b0dfbea8a2 | -13.86674 | -44.00028 | 2026-09-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44417c72-00db-3d9a-9953-5b20e10da703 | -11.40145 | -45.414 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0083f75-cabe-3a7a-86d8-a8b38665685a | -6.16064 | -52.91085 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e254a496-0010-3a23-adab-13f865bfffc0 | -12.71473 | -46.99783 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6064df54-8389-3b47-8e5b-9448b6469781 | -11.41947 | -43.43285 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 680cacfd-6daf-3426-81b7-28d79c8d897a | -7.34543 | -47.24996 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27aaea0d-9bf2-34c0-a305-5dfb676e95f1 | -9.78573 | -48.22405 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d7b49e0-010f-39d6-a9ba-b65e36f6a9cc | -8.36222 | -45.48857 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db01c56e-3279-31dc-ae34-2df44ef15515 | -12.95459 | -46.64201 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4ca4a10-9277-3dea-bdd5-b53484c4fbc3 | -11.39364 | -43.44927 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff7ba301-c04c-3326-929e-a4e78fa56572 | -11.01076 | -54.13869 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e7207c-b42e-3a21-aa59-2cda8d2ba57e | -13.17651 | -48.55561 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10acbf58-5556-3696-bf41-1a463f0f5808 | -12.74895 | -47.28989 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db76da48-ed87-3d6a-b88f-5d8c80046749 | -12.76792 | -50.67367 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87bcbfa-b222-3c2a-97b0-91a5e99825d9 | -9.96411 | -50.16263 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1e849d2-bef0-385b-a8db-93e7ea66bc2c | -11.12689 | -50.05737 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63dab309-3483-3c66-8f13-2c8a871a9820 | -12.93571 | -46.66412 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32994db3-e962-30cd-b48d-cd5761095475 | -11.34832 | -47.33724 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b23e6bb-1a4f-35b8-a7de-db1b67c4ffb5 | -10.01299 | -45.17793 | 2026-09-29 04:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24c73a44-19bd-3b3f-b313-708974aa8cb3 | -12.01017 | -50.98947 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44deb395-0937-3256-9beb-377fb709fc9d | -7.99063 | -43.25962 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4191653e-f264-38ac-bdd8-899fbd70af87 | -13.73634 | -48.9769 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6baec7b3-fae0-3a39-a12b-5d2db1466a8e | -12.02575 | -50.97751 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b62de7ff-f88d-31a0-af52-a22afe065886 | -11.38271 | -43.38773 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 059a8f4d-118b-3c1b-b607-f742d2829285 | -13.51628 | -46.90068 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef33a801-bd09-3ad7-ab2f-5104c9520cd9 | -11.34397 | -54.11338 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e1147a5-f9d6-3c5f-aab9-20b47cdf1c76 | -11.67299 | -44.53547 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 292cf73c-e8fe-3b02-a427-35e0886f5091 | -6.2998 | -51.73148 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf2342ce-e937-31d9-8895-30b9bbb655e0 | -13.20803 | -48.5606 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a62a8223-0ee7-31b8-9900-ce883aa8e5c1 | -11.98218 | -50.95594 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f861bc4-6d7f-361f-9aa7-bb05ed43d46f | -12.01746 | -50.96526 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8775973-9286-33fd-b9be-cc8a3b9543fe | -7.2423 | -43.37011 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1e59a636-7a8c-3163-8429-28fbf9821a5d | -11.18775 | -45.13881 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4de9458a-ebbc-32c5-81f8-40d080cc0f72 | -11.8748 | -47.08799 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 918f87ce-0694-32de-8b0f-48075e78abff | -7.99297 | -43.25774 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a2d4d51f-0695-306f-8c7d-c273266940e9 | -7.26362 | -43.37768 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea76f080-c37d-3f39-b059-4048f33719d7 | -10.92837 | -47.58881 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f44c8024-c63f-392c-80db-4e71a0c13039 | -11.92735 | -50.89256 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a4dde5-f1cb-3fc3-b14f-6b5cc3872dd1 | -10.4242 | -53.83233 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50c01c6-9da3-3654-a243-48a284dff49f | -11.38223 | -43.40611 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 841f788c-fa6f-3023-8283-876007bd4b19 | -7.82797 | -47.92266 | 2026-09-29 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62fb086d-9f5e-3620-b6ad-478a01e32d34 | -12.95387 | -46.64698 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7f64ca5-1374-37c0-8f65-ffa17689c7a2 | -11.98331 | -50.94887 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f65dbd57-6b50-3e6e-a4ee-49a545eb5031 | -10.23211 | -46.53318 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59b3f24e-1f1a-3619-a71c-109349788628 | -11.16247 | -50.0486 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5caf8293-2f35-37b7-bbdb-628793febc71 | -6.32126 | -52.62325 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| faf2e0d3-1718-379f-beb5-88c663f97605 | -7.49308 | -44.55657 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80402885-ac15-30e3-95cd-e953db8b5e3c | -12.67172 | -46.97644 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dfed128-e1cd-3627-b4b6-eafb51c32673 | -11.3658 | -47.44596 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a183e9e-243e-3e74-9141-3ffca6658672 | -13.17243 | -48.55894 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c6f7685-7e01-3df4-846e-5a02c9663a70 | -11.41081 | -43.42667 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53d03f2f-b0f2-3f5c-8233-90abc7d9d358 | -7.27776 | -46.79678 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README48.md)
