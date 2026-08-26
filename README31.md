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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc93db67-bc3b-3269-a639-ba1d8e15aeca | -6.53921 | -56.25643 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04d45ec8-8e32-3981-84e7-b803fcb5686a | -8.55291 | -54.79768 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 131ada77-49b3-3670-9f86-802c107bc3fb | -6.22763 | -55.617 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5f6bf46f-81a9-387e-be09-037de0743999 | -7.29434 | -52.53505 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 267dedb0-aa2a-3da3-a9e2-72354d1d8cda | -2.72494 | -49.79031 | 2026-08-26 04:51:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2208eadd-d1ba-32db-af0b-ded9f2ed4723 | -6.26409 | -55.41648 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b617ba2c-1012-3175-a4fe-fa43049a42f7 | -8.62864 | -54.75761 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ac33fcc-1870-39a3-b1e6-ef440bfb3346 | -7.03173 | -59.22693 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 504593a5-9fe2-3283-9328-9b40266c59c6 | -6.15133 | -59.93156 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 387e7cd0-a962-378c-bb9e-da07686cba6d | -7.01642 | -59.2376 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11e7d7e9-d8cc-399c-9670-552d9b6fd6cb | -8.55071 | -47.45335 | 2026-08-26 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cc44ec2-b760-3495-bd2c-51dca85e6075 | -6.2645 | -53.37988 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8b4159d-60a3-397f-96c7-e338390ad256 | -6.62022 | -58.49108 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78ba1d95-1fc4-3f80-a671-9ac4fc4c9a24 | -6.14668 | -59.93066 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f321311-150b-322f-996a-88ba0312abb7 | -8.08266 | -45.90447 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 577538b3-766b-3cf6-bba7-a7f7be76721b | -10.03455 | -46.40572 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d226be-e822-307b-92cb-1c82094bf240 | -8.20281 | -54.96415 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d36c5f4-80f8-3e1c-8aa3-393a47c3630c | -8.08664 | -45.9101 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34627d92-eb4e-36fd-ab07-218a28fe454b | -6.68524 | -56.34866 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3499624d-7f60-3986-85a2-4f7e09b14a3a | -3.21147 | -48.93557 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8da11c4-166e-3354-a6a8-f7037d167cd9 | -6.63993 | -58.50224 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1b6655f-2dfa-37b2-a606-283d53b2aee4 | -7.49124 | -55.32364 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4024a5b-874c-3b7d-85f0-0b07eec6a97a | -7.76065 | -44.75373 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7251c952-c9c0-302a-9806-19df55027d81 | -8.01364 | -51.81851 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 330476c9-a742-3d49-8a85-26524fe4c935 | -6.85553 | -59.41384 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c507014c-7eea-30bb-87d0-839ecb09bde0 | -3.54158 | -48.17521 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b236cde-db13-3138-b78c-9153fac4e504 | -8.16814 | -46.198 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72bdc574-7e30-3559-a06d-00054f536e1f | -6.25896 | -53.37188 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0bf86b55-a977-3fc4-84c4-52839c692f55 | -3.21594 | -61.23465 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06787554-3dd5-307d-8712-a235848cc862 | -9.63057 | -48.29721 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b88cd14-8276-3e9a-a273-15616fecb15d | -8.29721 | -47.62326 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd3bfe32-486d-373a-8159-4e50d24faace | -6.14625 | -57.70991 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db9bb6b4-8f09-3b2b-b4ae-bdd8334ded09 | -6.27278 | -53.37048 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bd82ebc-b300-3a8b-9024-52c3e42071ab | -7.54576 | -61.36797 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee97d4c6-bfdd-3274-91d7-94d7fe4fae65 | -6.64703 | -58.51136 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a784406-b9db-30a1-b0da-fbfb2a12da50 | -9.01954 | -50.78421 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb71c1d6-8811-3883-b412-ee49d5322f30 | -7.76181 | -44.74508 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98fd31a1-17b9-370b-9399-0f74ceeb14c4 | -6.25951 | -53.3684 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633ad151-9025-397b-99a1-7d1f93f67806 | -7.43592 | -59.77268 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b89835b-5131-3a22-818c-707ddf6e1064 | -6.26173 | -53.37588 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 438d0e10-f7f5-315e-a247-aded6330b906 | -7.30485 | -49.5407 | 2026-08-26 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4873a5c-270b-31c4-be81-2bc5bf94e55c | -6.93679 | -58.95815 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b240d5-8eee-3f17-9d82-fa83e6802141 | -6.80539 | -59.60033 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 259a9a2b-d361-3659-88e9-a84549e1abc4 | -8.01139 | -51.8108 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63bed0ba-996a-330c-a3fe-c0d4129f24ee | -7.25527 | -49.85239 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28049b54-f3f7-3c70-8ace-51b03f9e26fa | -7.48424 | -55.27917 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9fdf6e93-960d-3b5a-983b-6f9abe61c52b | -8.64446 | -54.74523 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d373e91-9abb-3885-9f7a-4f21f7af1df9 | -5.73824 | -43.27597 | 2026-08-26 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9578808e-3420-35c3-acea-50e4897694bf | -6.25564 | -53.37136 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8a8457a-96f7-3d2e-bf91-04ef714f75cd | -8.02066 | -51.80894 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d424b7-7779-3779-8776-422b56fdf6dd | -9.02714 | -50.78136 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8ea8e62-5ccd-32dc-82b6-1dd364b1e0b0 | -6.37275 | -54.94456 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdbec660-e3fd-3d30-911b-506d57939103 | -3.25723 | -52.23211 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84d2e075-cfce-3c25-8637-0d99a591e079 | -7.39788 | -55.16298 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6700089-32ee-3de1-a614-4cf26559b4f5 | -6.6295 | -58.5127 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2a56f83-9842-3c22-a442-fd2b57fa2b59 | -6.30622 | -53.56898 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e2b1f8f-a0d2-3155-8f56-df30d4ae9a43 | -6.87316 | -43.74534 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17112ceb-fd8f-396c-9cfb-db52dac700be | -7.49825 | -55.36834 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69cbce72-b8ce-34e7-8a22-858c7dbb3c30 | -8.07701 | -47.50364 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b3e93e-d6ae-3c7d-88a6-ea1649e4dbd4 | -4.06105 | -56.33831 | 2026-08-26 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4776f57a-4d0e-3529-b691-4ca24218ec26 | -7.29712 | -44.08879 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2eb47785-b5ef-3587-9e40-bc8599e41d57 | -7.34552 | -55.6611 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95230186-119b-3f9f-ab08-0672255a6115 | -7.13848 | -42.77232 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db48d0da-d3e3-3dbe-86c6-f2ae1dda90b0 | -9.02775 | -50.77729 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b60c1f9f-ba41-3682-9923-83207bba8adf | -3.06749 | -61.21405 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2f02872-3c9f-3df8-8d13-f8f72a66545a | -7.03102 | -59.23124 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c6012c1-7871-375e-8048-561fc778b5a0 | -6.83994 | -52.50583 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef244946-f1d9-3bcb-9a33-959d487a09a4 | -3.53713 | -48.17914 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f0ba38ff-818d-3258-a525-97d1736aaa0c | -8.02738 | -51.80997 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad240f0-c838-3faf-b93c-28d660c5a67f | -7.38871 | -55.15393 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 125994eb-8d2b-3b2c-92da-394e78540deb | -8.22345 | -55.00966 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524e3893-316e-3854-b72f-32cac9bed50b | -6.74575 | -59.6427 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1e64db-9ceb-3093-ae70-6cff3dc45e73 | -6.5389 | -55.08798 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cc25c5-4ff4-3d4f-8646-5f65f03fb432 | -7.7622 | -44.74218 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7595876d-d5fb-303a-83c0-7fc4b7a76be4 | -4.89963 | -56.26528 | 2026-08-26 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b983b73-8a30-34d0-8b78-1f219ddb26eb | -8.57811 | -54.83529 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| faff99e8-5227-34fe-9989-1efa99f1b24a | -9.03698 | -50.79387 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e1a9c9b8-794f-39f6-98db-27276e6595fc | -5.92305 | -43.64272 | 2026-08-26 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31a48669-9f5e-3f82-ab65-25d4701cdee5 | -6.12899 | -57.86426 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20dc3dac-45ae-3c25-980e-51227d70bd79 | -8.39087 | -47.36312 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfb76df8-4523-30ee-8da0-920305036488 | -7.86264 | -46.10524 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed41d7ca-ef8e-379f-97a1-6bbb4ba5db24 | -8.01253 | -51.82569 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2a2a53-8162-34c8-b3ac-907053328e8c | -8.6079 | -54.73566 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7fc7721-48cb-3827-9871-aec5ac70f491 | -6.36026 | -46.11933 | 2026-08-26 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 823417bb-3585-317f-9487-5e4398254486 | -6.23294 | -55.47385 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce224b8-be06-356b-9990-2ec609632d40 | -8.53053 | -54.85027 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd5f9d64-c4f2-3814-8f41-8e8c79fd08d2 | -5.77973 | -57.54686 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb9866f-93e6-35c2-a004-4d8637c42ebc | -6.15215 | -59.92661 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db57be40-3585-3e07-a100-108d6f2acd9f | -8.59884 | -54.74905 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c86f53b7-4760-35dc-ae53-a2d665ef5eeb | -7.2168 | -60.61698 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c42a2f3-dc6c-3d35-a836-01d741db5b90 | -8.6001 | -54.71952 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669f4e74-7abd-31da-91e1-b365f08f6dd3 | -8.27566 | -55.5382 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4050e3d-488d-3e5a-8c35-44025c868cb8 | -6.64413 | -58.50296 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7132f2cc-8bbb-33e0-bdb3-e2b123013869 | -6.87984 | -56.51173 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899029d8-8593-37cc-a295-9b76e9f6b67c | -6.27443 | -53.36002 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a415aeee-229d-3333-9f7e-caa3a02dd781 | -7.39442 | -55.16246 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e49b325-e768-32b0-82e0-240489dc5d37 | -8.61369 | -50.01786 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fee631d-ea99-328e-9d66-92af51b7d95f | -8.5606 | -54.83622 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e1e067-e714-3638-b20c-be0cdb5ea82b | -6.22877 | -55.47723 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12e1ab5d-c2c6-357e-b859-85760d08ba11 | -7.18928 | -42.73928 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
