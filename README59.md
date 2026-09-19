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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f46473bb-bbf1-39ef-a1b6-efaae018fe14 | -10.86794 | -56.19946 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b28964a0-e532-3b4f-b580-c8f9f57e2917 | -10.09474 | -45.64547 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13f11621-abda-31c9-89ac-0aaf4cd4a5b5 | -9.93833 | -45.27784 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e1c51d0-1337-3359-91c0-4f13dc429511 | -13.879 | -48.60873 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 921739b2-40f3-3b66-a2d4-da4b82a83710 | -11.2839 | -43.51283 | 2026-09-19 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 843532fe-f52c-3f9a-b7ee-0db367118f2f | -10.20577 | -46.58822 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9593a64-47d4-3040-9a01-fb4d6876fd46 | -11.96821 | -45.77255 | 2026-09-19 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9d943b02-9071-3684-8c53-2c029bdb1956 | -13.73788 | -48.79179 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2988052-50a9-3bc2-94ad-1dbfa64fca36 | -12.12753 | -46.98115 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b552c72b-f1e2-38dd-9567-6b4b77c9cd7b | -11.46773 | -45.7154 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b475843e-84cd-38dc-a0d9-58dee2bad95d | -9.25303 | -45.92578 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15d6950c-d0fb-340e-a158-c21a1c450c3b | -11.12425 | -45.29285 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f7fcc0b-10b8-3c34-abac-02e33bb0a2d3 | -10.92973 | -53.96082 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8a9b4b9-6ac0-3d6a-86c6-d94dc90ffeb3 | -14.39762 | -47.27511 | 2026-09-19 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba46f8bf-e9c0-37b0-8ad5-9c613c420d21 | -12.70002 | -45.9568 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 239362b0-4167-31a5-a360-15ec263973d4 | -14.79952 | -48.54206 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0cb9668-dd05-38a1-84cc-0656517c1324 | -10.86522 | -56.18552 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c6f20cb-ef1a-3018-b56b-67630e6626c8 | -14.9264 | -49.92133 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 43705857-8974-36e1-aa1b-86981cebc730 | -10.99151 | -48.32207 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c14c2b6c-9427-3a70-87eb-5baefe31a710 | -11.47093 | -47.65065 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a05b0cbb-b396-3cbc-917e-d7f3c0cf1d68 | -9.60944 | -45.37589 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e73a2201-759b-3a6b-ab04-b949f3b781e1 | -12.68859 | -45.96278 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d460eaff-0abf-364d-99f2-0f13e0023c4d | -9.70118 | -48.32875 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fc351bd-bbd7-372c-b56d-c394a126ca1c | -12.34921 | -50.70492 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7eda0949-4405-3bcd-a736-b63cd7679262 | -13.02012 | -46.93695 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dad82b4-4b6e-373b-8d96-760e2f862f79 | -11.41375 | -51.45028 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe6bd494-4c8b-334d-95dc-0ae0f77056e1 | -13.58983 | -46.9498 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c7ec78c-1cc7-390f-8497-1d0f26741375 | -10.92353 | -47.85809 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70caf561-a282-30b0-9b20-8ba9a23499ff | -9.91016 | -46.56975 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de1b816e-eb40-3f03-942a-4ad646754a59 | -10.64562 | -48.70747 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae23cfba-c573-3693-80aa-11e857c0f4f5 | -11.22229 | -42.83399 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8f09eb5c-017e-3866-b420-9c283d909f4a | -10.85588 | -56.20447 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 081f2892-52a7-30cb-b5db-f3314102b78f | -10.36404 | -48.89248 | 2026-09-19 04:40:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5eeb3f12-1cb9-31c1-893b-7190e1a95cac | -12.14253 | -46.99472 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 735dec02-2263-3a58-bb3d-ea580a065d55 | -11.8767 | -47.61206 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c149504c-96cc-35f3-8f40-8ad93f6924f9 | -14.67334 | -46.68331 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8937c0aa-739f-39f4-b894-f23b3b668acc | -8.71514 | -50.08226 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef52d715-8a75-3d1c-a2c0-d427f78565d7 | -8.84247 | -50.45211 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732c31a2-8882-3f95-925d-fa26ca2c3cce | -9.86272 | -48.34831 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47bc7959-152b-3e52-832c-907056326138 | -9.74702 | -46.08364 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3853d6d-4c80-3935-b061-599e3627e2dc | -9.70177 | -48.32511 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c358de1-c6c4-3cac-af86-be2f12846c96 | -11.08323 | -48.27449 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e663b534-3735-32b8-a8e8-fe845a2e226d | -9.73075 | -47.1272 | 2026-09-19 04:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32f481b0-f806-3e4a-bdbb-cef1d832ded4 | -9.56356 | -45.47038 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 806e32b2-047e-3371-813f-3c64697ffa6c | -14.92362 | -49.917 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dc29b75-8dbb-3b01-b930-6c640f37ce49 | -9.76569 | -45.06316 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0e1a557-4ed6-3899-b94b-85ec1ea02275 | -12.48533 | -50.04399 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a9b7b3-3106-3fa2-a624-c77b8990b93e | -16.09344 | -49.64661 | 2026-09-19 04:40:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e183f5be-63c6-33d0-a2de-1d0cfd893756 | -9.05106 | -48.73621 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49606ccd-2de1-3305-98b7-93e7fce9a601 | -11.11965 | -45.2999 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 334acd7f-0a01-3c9d-bc36-c19eaf9d8cf6 | -9.94516 | -45.27906 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05360a6d-e057-3c87-a56a-3a91db1b70f9 | -13.00503 | -46.96796 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88d15bfd-ff79-3bb6-9dd2-33609822856e | -9.16051 | -49.98794 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 362fb93e-d4d2-39db-a827-2ea33c35be87 | -9.66786 | -54.31495 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16dfa65-59c2-3350-8d5a-5cfce50d7635 | -9.56527 | -45.48192 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460915d2-4a33-386a-9f56-ce5c76332c11 | -12.69433 | -45.9482 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da98367f-5be2-399e-a8b5-152ca66a3fbd | -14.66313 | -46.65873 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6a793a79-92ec-3635-b846-136bafb5a80a | -11.19568 | -55.0363 | 2026-09-19 04:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36090cbf-03b8-3574-89f7-41a54dde6502 | -13.00673 | -46.97911 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8ac77b13-9761-3cf7-802b-c100112c73da | -7.58107 | -57.68643 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296cf773-033b-3bb8-8166-1c548166c088 | -13.80345 | -48.67315 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c1bdb33-c5d8-3eb1-9e51-8c42a76fe75b | -9.1591 | -49.99627 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bebc60f-fd96-3b5a-9609-01288dd71eae | -10.85875 | -56.18888 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac699dd-8983-3f45-8dd3-43bfb613399b | -9.04948 | -48.72441 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d49795-8051-3ebb-8e4d-5af0c33f2518 | -12.70232 | -45.9418 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8f57a5f-0cef-3089-aed1-3f2ef97dff51 | -12.33488 | -50.72397 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5677881b-43d1-31c0-b5a8-4239bc90b83b | -10.13952 | -47.68689 | 2026-09-19 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d8bd10c-2317-3ab7-830c-5526f6ac03e1 | -13.63066 | -46.95281 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a5576f0-c048-382c-849f-fef525d82de2 | -12.48456 | -50.02471 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a76cc5c6-1592-3ea4-8eaf-9bbe888ee8a7 | -11.07864 | -48.30283 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 392f5dbf-7445-3cbe-87ec-ef0fead0c13b | -12.59022 | -49.10454 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c23736f1-1139-3f6f-a102-3076c491b9bb | -12.13699 | -46.98636 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 23e292d9-2111-3377-a3e3-c7fa38f479cd | -9.36167 | -48.28918 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 622e5d63-a251-3957-b4ad-1726a4ac57bf | -10.17989 | -48.52246 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fda9359-96d0-3dd7-b404-138272e76a75 | -8.31513 | -50.91753 | 2026-09-19 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de3a17c3-c11e-35aa-b82f-6980c931c947 | -10.80325 | -50.90347 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a2f3a39-2d67-3a48-8333-318184c74be7 | -10.00045 | -50.2799 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66cb0f6a-038d-332f-ad96-38db136aa512 | -12.28734 | -49.15991 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 82079934-bf8c-3d62-96b7-540dd2dcae6f | -11.94319 | -50.10922 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ad2438c-4bc3-3cac-ac56-15dbb1ecf04d | -9.91683 | -46.57082 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8737dfc1-d953-376b-87a8-dcdb7658c1b3 | -10.8019 | -46.64281 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a05a28a-fc66-3806-ac2e-cf3ccace3165 | -10.55535 | -51.31164 | 2026-09-19 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8f0866-2270-3f90-88fe-9c1e528029bb | -10.90633 | -50.84285 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93cbd56f-83e6-30fd-a247-8109bef0b4bc | -10.59398 | -46.54481 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa5693f3-2385-3b6a-9e84-a70dd284dd5d | -10.52544 | -44.84899 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d9b5215-c265-3a66-be5e-1d3609ed1011 | -11.22939 | -48.36109 | 2026-09-19 04:40:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af5212dd-f57b-35d2-b98d-f283124716ce | -12.69144 | -45.96705 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| eaaaee98-75d8-35a1-a11b-2ccd10533e17 | -10.93667 | -53.9483 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63d99eeb-a7c7-3686-9862-3514115fbc40 | -9.99754 | -50.27506 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51fb79e5-c1a6-3f7f-8ba8-f23c6bb9121b | -10.53191 | -46.74494 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff908544-b876-3017-b5d7-9adcf3978de4 | -13.74399 | -48.79654 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 637b4c25-323d-3546-a4cb-4cf1d1a44865 | -10.70748 | -60.73511 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b53b31c-2c59-3620-9b80-efb5420ce869 | -11.08199 | -48.30339 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 00bfc34b-68a2-30f5-8bcc-c57290696f06 | -13.7424 | -48.7851 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd3a9046-4966-3d31-bb73-7131d5f9dfee | -11.96763 | -45.7763 | 2026-09-19 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4b759a0-cf7d-3997-ba83-089ee209a7d3 | -12.12754 | -47.00305 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e89bc74d-1143-3386-bd78-29867bc48c67 | -9.35184 | -50.11642 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8559f14c-b64a-3ab2-99e2-ce4e784ca37f | -9.95235 | -46.54047 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 764cca73-746b-3d42-a6db-5b0f7d70390f | -9.56696 | -45.4709 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75b216e1-ac46-3b27-99ea-0c21dbf666ab | -10.85756 | -56.19738 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
