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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2498368b-16e6-3ee0-b2c9-a4a60e3886fc | -11.74786 | -51.0216 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d1bd2a-a3bb-3bf0-8013-8fc8adc06ce2 | -11.12372 | -49.4544 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 109c6815-6158-32fd-bddd-972adab043e3 | -6.06918 | -57.80536 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1b06155-620a-321e-8dce-de0faf6ed46c | -11.66577 | -43.48772 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d3d9adf-0927-3384-ac04-26faa6d55466 | -3.61072 | -60.56467 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2fa68f6-ccd6-338e-ab3c-f3aba94d1901 | -8.27642 | -54.7719 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0626cd01-3bb9-3fc4-be3b-2f1f9ee8708b | -6.14344 | -59.92989 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82624b8b-1aab-3806-b014-deecc329ebdc | -3.53071 | -59.61436 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03f33bfa-bff2-30f2-80bf-d55345972a31 | -7.42809 | -49.83378 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ca282774-1855-3de4-b493-c007dc19cae6 | -4.09477 | -62.09047 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 970fb09a-0a9c-3568-95b0-b3c08ba8b456 | -6.67701 | -55.05344 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4030098a-76ce-3879-9f03-e12d64ac2d08 | -4.08809 | -62.08471 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c5af8ba-0990-34e5-b125-7ba6f904d96c | -5.76171 | -45.10605 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cda7a08a-90ff-3d05-81a6-4f8960e8f36a | -3.60903 | -60.56676 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a60bb26-812e-3d47-9a7d-71138231cedf | -6.39246 | -60.01907 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47201d0a-1a8f-377d-a977-447d8419762f | -4.52971 | -54.97273 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c760533-14d2-380b-8f3b-61558f6e4bee | -7.54836 | -48.69557 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c91f3f-ca55-3c7c-9e6f-1baab630cb0b | -11.89205 | -45.77058 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2f50ad47-cfcd-334a-bfe6-2ebcbf3b1989 | -12.30589 | -46.39419 | 2026-09-23 05:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8b367ec-9dec-3ad2-ad2f-38733379a54c | -6.12759 | -55.81883 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df96ea15-088e-3fbc-8de8-85266c863b79 | -6.74825 | -59.46544 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a8d0881-8e4d-30e7-b31a-6fff5b20339b | -6.62307 | -43.73278 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cfb09c5-53e0-3a1d-9b07-05268f47908e | -4.53612 | -54.93267 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4813138b-2ac3-374f-a072-e2fbdee89193 | -3.96061 | -59.35108 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a6e5bf9f-2fe5-3e9c-acea-7124ec7d709f | -6.17233 | -52.05117 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be5fb7a-09eb-3767-8930-40ebbe09a029 | -6.18266 | -52.79742 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35f711d8-d936-327d-97ec-a00c6b60f320 | -7.04522 | -62.93258 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e2d666-9fd4-363e-a917-f84c34dfde18 | -10.25493 | -50.20987 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eddb198b-5863-37bd-9c74-1a727e5edd13 | -5.82729 | -52.02586 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57471b7c-0d74-36e4-9c22-567bc5b7f40d | -3.44052 | -56.4955 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53ac28bb-bc5e-3893-9c3e-4ae159853ca3 | -4.5025 | -54.96011 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bfd6f52-3a92-3dd8-905b-8cc3b11569a5 | -3.77243 | -60.74539 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e778e24-eab6-335d-98ea-f17c15a50c86 | -6.67965 | -58.56033 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5909760-d9bc-38a7-a8b1-573de57fa46e | -7.55931 | -55.01896 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26f88721-1429-380b-b8d3-07aa493deb0e | -6.6711 | -58.55884 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 026be844-8c96-36f1-b885-1739c1d32d69 | -6.34576 | -57.77037 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ddf4b40-a50d-327b-b241-081e954594a1 | -6.57387 | -44.15682 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6c21265-87e6-3444-af8f-41f4bde4746e | -4.32545 | -55.43366 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbe6be03-c2d6-3e60-b50e-048738256241 | -3.22553 | -61.05745 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3fbc254-11dc-3bc2-8f25-eb46fb3b58e5 | -5.11763 | -48.79842 | 2026-09-23 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3249c7b5-06a6-3a51-bb09-3bf6716ce9b4 | -10.47083 | -45.10774 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ca601f8-d234-3d1f-9e36-3b63410a25ab | -6.31262 | -57.74252 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5195ad1-b854-3c39-9e98-2e527215b7c8 | -6.934 | -46.55872 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab5f6b28-01e4-3a00-864e-51699834381c | -6.018 | -57.76707 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eae5db2-f604-3fac-9ae5-e1d53d9ada42 | -6.74746 | -59.46999 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 251c2c1e-d77e-303d-9c3f-a4f0f88f437d | -6.27964 | -47.65244 | 2026-09-23 05:04:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ff7d8fa-7e32-38ca-8b71-1c6dd2055ee8 | -3.90554 | -55.83149 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 577a82d2-f257-3e8a-a3e7-fc5857608bb5 | -4.5384 | -54.94123 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e48f99c-18ab-34c0-91b8-352c0051e692 | -5.80805 | -47.76367 | 2026-09-23 05:04:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cc4dd16-ef76-3a8c-acaa-c03cc044e2d0 | -3.29304 | -57.8595 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600a4987-ba5a-37f8-b82c-4a0f277d6161 | -4.30728 | -55.59298 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbf8fc32-d0e8-3cdf-ae07-41595e521561 | -4.45555 | -55.06871 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3e42607-4099-3dfc-aaf0-df8f8e1fa7c1 | -11.28793 | -51.37454 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 11589c81-ebbb-3115-8e8e-497ac282814d | -6.84473 | -45.55467 | 2026-09-23 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 062ca0b2-3b49-32f7-adb6-996c2d718914 | -5.87717 | -51.94791 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c0e08db-5463-3327-95f1-2d5248ff985c | -3.16081 | -58.11891 | 2026-09-23 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 07e3da4d-30a2-3061-ac19-7ae7bb49f7c9 | -8.08553 | -44.33997 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0041f8ea-5a73-37a5-af04-3b19dfbd0d75 | -6.33505 | -55.98534 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52f6de52-439e-37d4-9eac-ae80236128b3 | -6.34132 | -59.94741 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0a75674-38d3-3c1c-b77e-35b0608b778d | -6.61021 | -59.94741 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7ba8df3-1bbc-3e1d-a93f-34581cea4865 | -6.09407 | -57.68238 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29043a21-68ea-3896-a14f-42814fbc4baa | -6.32789 | -43.93832 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f20fbfc6-f5e0-36df-a703-de9ed8fc31ac | -6.6234 | -59.98732 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 851280a1-4d8c-365e-971d-042765e9b8ca | -7.42861 | -49.85483 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d648aa6-0996-39ad-93ac-1e84aa6274dd | -3.89512 | -60.5906 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f5a1fd-f122-3f29-831a-bf597980ef54 | -5.87887 | -52.06242 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c176fbbd-02a0-33f0-bc64-def5cf7a39e0 | -6.69713 | -59.95425 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 066e059f-900c-37d1-9267-1e32e565e837 | -8.80858 | -44.27108 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc8106cc-3c6f-3ef0-9a32-39c9201da527 | -10.54372 | -43.97717 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e6f9ac-b6c0-351c-b50d-3be1a7171d8f | -7.17859 | -48.23514 | 2026-09-23 05:04:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc58e73b-db85-39e5-a24a-1c003d84a9fe | -6.13647 | -43.85722 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bde75bc4-efea-3f37-b6d5-62a9012ae42a | -8.45862 | -48.69424 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2adcb407-d8eb-333d-978b-249c72e1f9fb | -10.26154 | -50.23965 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4667556f-a147-35ad-8e33-7508d5a42972 | -3.4633 | -60.26369 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67d4f748-0f6d-3029-8b88-e6260646ca38 | -8.45995 | -51.48277 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 082e7896-f6be-3c02-b99b-8c3338764764 | -7.29132 | -59.52705 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2acc4436-362e-365e-98d9-b94d30229ba3 | -3.68863 | -60.57479 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a9e3fe-4e1c-347f-b3dc-6169fe3d2a24 | -12.12465 | -47.38618 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cab6458-0ab5-362e-89e5-f30aaf55d797 | -5.21733 | -60.0569 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bacad40-319d-3ed4-a72e-600948615364 | -6.67803 | -55.06938 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca40e0ff-709d-3658-b2b8-94f50d87164b | -12.30543 | -46.39669 | 2026-09-23 05:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 19e60e1a-66d9-3c2e-8a8f-90b3497f2e76 | -9.09452 | -61.43519 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e19fa8e0-3028-3f7d-99c3-26f1dd57f583 | -7.13043 | -48.42412 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c91a9d1-64cf-3506-a673-7a97a02ec5ce | -8.18422 | -61.18934 | 2026-09-23 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eac6f27d-c8d2-3e47-84c3-34be03c5922e | -8.2363 | -54.6749 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6570015-595d-3a32-af69-469f7e77a453 | -7.08966 | -52.74955 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34165a90-d41a-32e8-a431-05a1cd11acb9 | -9.86603 | -48.39595 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f650fab-0771-3627-b504-6df3c7b6e87f | -6.67349 | -42.56667 | 2026-09-23 05:04:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 325d524e-f57e-363f-8793-0c2ecbe97e6f | -13.73101 | -48.97047 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8708591-e56e-3ed9-be3d-04218ed436a1 | -14.60116 | -45.62996 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d531b3f7-f183-3270-9cf5-c6e29a7c1a41 | -14.63542 | -45.65377 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 716b03cd-c160-3de2-8c1d-b6d5504b7519 | -14.6256 | -45.64613 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64097f38-c7df-307b-845b-9cf605ffe8b6 | -10.65935 | -58.76115 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26509cca-b9f9-3391-8d89-a7ba399301e9 | -14.62539 | -45.64922 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa51337f-77b4-32be-8673-c939c09bfc54 | -13.92961 | -47.83361 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| caf2b3c0-95c8-38b6-93ca-3fecc4638060 | -14.6216 | -45.63578 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5764fc6-88c9-3f17-b74e-01f278c929ec | -14.62921 | -45.65962 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59012174-6860-3bc1-96d6-313382de352a | -14.63122 | -45.64346 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09407eaa-4a61-3d58-81e1-a7b6d1fe7b9c | -12.41326 | -46.97019 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e7588942-ad65-390d-b62c-1308dc2c3ab0 | -12.10217 | -50.03773 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README97.md)
