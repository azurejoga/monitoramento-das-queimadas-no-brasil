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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba32768a-4cf4-34df-a12b-5b97373fced0 | -9.77572 | -44.81937 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dfa8b3e-e315-34f0-a771-5ce0bb07a6a4 | -11.08241 | -47.50151 | 2026-09-29 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a37466c1-f784-3590-bfd0-56e94f75ffe5 | -12.31649 | -50.25513 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb3f73d8-a02f-3fe8-a510-c847dc36a132 | -11.3983 | -47.45119 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0d623c9-9508-3228-88dc-aa36805d6cd5 | -9.08826 | -49.88198 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9dbf0a5-0798-3de9-bd9a-0fa30322600f | -13.19345 | -48.56219 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77e4b223-459e-3353-999e-440a9a7b4a9d | -12.55983 | -47.16084 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f006967b-633d-3c64-85c5-6ffe374e4198 | -12.77828 | -54.02425 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7940f16-a455-310b-8b37-1351326d70a2 | -11.99166 | -50.93943 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4b26acc0-a039-3319-8669-0a14b0686a20 | -7.40963 | -40.22263 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5a73380-1e6c-3b07-8564-c5c78f5d9847 | -11.39563 | -54.0438 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b618ed1c-56ed-32e8-8974-d8acbce003f1 | -11.00628 | -54.14251 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d64578-547d-3bc0-8ba3-e0acf4b25a8b | -11.39676 | -43.43814 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c76e668f-d7c6-39a8-be0f-7699f682a12e | -11.38383 | -54.04625 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4107a23-5195-341e-b152-61c88d218080 | -11.37284 | -54.05493 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e95ae52-7dce-343f-aaf7-eb8a52ac9314 | -10.81755 | -48.72438 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c49cfde-146a-33d9-a727-856616d9d34e | -6.14692 | -51.73925 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b38b2c4f-1997-38f7-8cc5-d1a999eb856c | -6.13977 | -53.05722 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c861d3-3923-3f6b-adfc-5c8f24a69616 | -11.37964 | -47.45241 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4715f563-a8f1-3f97-b9f8-10977da8d8a3 | -9.16852 | -61.40046 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce46a5a5-a321-33bc-a4ce-e52a67fe6b84 | -8.21949 | -45.45529 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cd98174-8804-39b6-9c1a-6239db2efa25 | -11.34322 | -54.11784 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 367a2cf7-3721-30fa-bac3-33243183b068 | -7.54202 | -47.11812 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e1e3573-ca92-361b-91cc-87d3b2b6b301 | -10.26186 | -44.63334 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bb94706-0824-3128-b1cd-2d76ed580a88 | -6.68316 | -46.98974 | 2026-09-29 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb990062-092c-332b-a31a-9c0e58be46f8 | -13.06807 | -47.44946 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 932a87a7-8f5f-39f5-a27b-4626057ff144 | -12.15492 | -50.40022 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b11761ad-d7dd-3215-971d-938362c150f4 | -11.39957 | -43.44015 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef9d1b47-a601-32fd-a187-967cc83a44be | -11.38243 | -54.04301 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bd80243-bb42-3582-b5be-76ad9d0b3529 | -13.17886 | -48.56387 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56aa1d5e-1768-3694-ae01-1e01a6c51272 | -11.71217 | -44.50705 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3eadbad4-5c8f-3978-a877-c0fe34129825 | -11.35442 | -54.05172 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8881f6d-d1ba-37dc-8305-ed2918b9714f | -12.79557 | -54.00994 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73afc1f4-2949-34e0-a982-a77b05be0133 | -11.8674 | -47.08683 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cecde639-6b14-37fe-b58d-ba7a69bb50c6 | -13.86735 | -43.99539 | 2026-09-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e8e4b2e-f366-3967-ae5a-20c6925040ec | -10.25387 | -44.60237 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca83451e-2342-3c2f-b4de-ea9ecb2315c2 | -12.91496 | -52.03861 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b47114-1628-3a76-b9e8-f0d3f8c18598 | -10.69683 | -44.44653 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90a4b457-021e-38f5-84c1-d8b6ec037366 | -11.37064 | -54.04549 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c0f24b-4229-37ac-84df-4ab4edd779c8 | -13.47777 | -48.61106 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 517f230e-7c86-334e-9739-bae2d2d6c248 | -12.02032 | -50.92588 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c5cfca5-708d-3c08-88e3-0246013f2625 | -13.52391 | -46.90188 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07ebe2e3-fa74-3fa8-a568-a24092586129 | -10.69746 | -48.75869 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b89bf4c7-4b92-318e-827f-91df245d174c | -9.79036 | -48.1938 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25867100-2090-394e-bef8-00e1be916223 | -11.3954 | -43.44791 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 684e495a-3f15-377d-af5d-0ffdb558b42b | -12.60086 | -47.28315 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88a093a5-dc25-326c-85f4-7358d3321cf5 | -12.04025 | -50.95094 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b3dcd64-1cc5-3e93-a131-4d747862b45b | -8.22137 | -45.46958 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abab7064-8fee-3326-a6b6-3ff36434a807 | -11.40449 | -45.42182 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d1c49d-43e8-3af0-93ae-4372b63d2745 | -11.85756 | -47.07631 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de571048-8944-3d0c-a3cd-1689214d2478 | -9.85708 | -44.9403 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa3bf7ce-ede7-364b-958d-89c61e62f615 | -11.43415 | -43.46473 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3ffc184d-14ba-3269-85d3-c4ea424c438a | -10.26975 | -44.63848 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8db1801-b1eb-32de-b70c-34d2fdb34a23 | -12.71995 | -46.98695 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cace9dab-5d47-389d-85ed-5fa563722634 | -6.32056 | -52.62747 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44f1945b-6184-3b08-81d1-bcb50632bca3 | -12.01639 | -50.95057 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5fddd30-4eee-322c-a5ed-e7af8bbf6539 | -12.65783 | -46.99288 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d754c10-b43d-34ef-afbd-b0bd31bc4b26 | -9.79381 | -48.19431 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2aaa34bc-f2b1-377a-a04a-88e853b208ad | -7.26423 | -43.37346 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eae1f5d-860e-31da-be5b-dc4118037a51 | -13.16835 | -48.56227 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d147b5a8-0dc2-3ed7-aa05-6e60a1506055 | -11.35074 | -54.05108 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5764cfb-4ad0-3bfc-961b-240329bf98b6 | -10.27931 | -44.63156 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 183da309-7f76-3849-8367-6e8cccfdf1f2 | -7.46531 | -45.80137 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b48e1a3-7af0-35c8-96fe-93020bbd6e35 | -12.03877 | -46.50516 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7fa7aab-4769-3b86-af7a-072ed50ae4f3 | -11.39301 | -43.45411 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93df18e8-72b5-39fd-ad76-29f6a2b0d35c | -7.24789 | -43.36234 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9702a598-63c3-3283-a2f9-5037d3785c7e | -8.54645 | -47.84983 | 2026-09-29 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95c0b454-183b-3185-a748-8b3772125073 | -12.03914 | -50.95794 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c82688f0-942c-31e3-8bfe-33a8bdbf4c7c | -14.10876 | -46.29343 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 92054aa1-3b82-36bf-907e-99c034bb9817 | -9.95301 | -50.14647 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d87d81e2-1002-35ca-ade0-3b77b56930bc | -10.26211 | -44.63474 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc163cf2-7746-3ebe-99d2-79bf2994b160 | -11.00704 | -54.13805 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66f0ea21-1e94-38e4-a9ae-3ee4edc164e0 | -13.18587 | -48.56495 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c73deb65-c2fd-3e07-bb09-0b940759fbfd | -10.71446 | -44.42673 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56e45471-2247-3d4e-ab00-24b1b08c8fa6 | -12.75903 | -47.34996 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5395d90-a815-3ed5-895a-29653ac61f5b | -10.2624 | -44.62947 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dabb6a2b-3b53-3733-8a92-89137d29781b | -14.11275 | -46.29399 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87af2efa-7d75-3397-9137-1f5f1b456360 | -11.3493 | -54.03722 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5668b1ba-b3d5-3463-a06a-52ee6c4784d3 | -11.9972 | -50.94753 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b96263af-a7ad-3bd7-93f1-6225d379195f | -11.34767 | -54.11404 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe9fd44-6815-3180-a245-0d5d9727d68b | -12.27699 | -50.26694 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cb7b717-0981-3dfd-8c4c-eddc31e447e1 | -13.43676 | -48.61783 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7d79749-c445-3756-9645-d58dc28af3bb | -11.33952 | -54.11718 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d5d10b5-b684-3cc2-b75e-6875714a3b65 | -9.14514 | -49.97052 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ee19ae-9025-38bc-a676-9da66c13c2ee | -9.13405 | -49.97591 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9e51806-0d65-39ad-b7ad-dd1a8b9b4ace | -10.59785 | -46.21232 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6398eb5-ea84-33e6-9366-c612fe5afdff | -10.81468 | -48.72031 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc6712a4-d7a2-3d5d-800d-e18f5f120313 | -11.42282 | -43.44328 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f45045ad-04cb-30fb-ad11-803949218879 | -10.70652 | -47.82505 | 2026-09-29 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d316751-f1d2-37e5-8260-2c579d80c011 | -11.43158 | -47.42624 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1892d32c-ed45-36fd-b969-8af80b380739 | -12.69355 | -47.25399 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5ad1b82-91f7-30be-9c63-71d14456f889 | -7.4648 | -46.68538 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85e48b19-1754-33fd-8683-620034e53771 | -13.17121 | -48.54303 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1caa34ba-94de-3a48-9ada-033447817057 | -8.3668 | -45.48438 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd994927-567d-3743-890f-ef3bc9432c8c | -11.71056 | -43.45758 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b948c746-348c-30fc-9677-2bf822aa32da | -11.40671 | -48.97308 | 2026-09-29 04:51:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e916a014-39c6-3467-97bb-4029332d8c59 | -11.38687 | -47.45349 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4db768f8-7329-3ace-a56e-a1110f25de05 | -13.53951 | -49.17884 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04e79090-fc51-3927-96db-0ce9ee9e8ac7 | -11.9003 | -50.61983 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 322f02aa-9900-34bd-8f30-a9fa1422a1c7 | -11.14467 | -50.07473 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README47.md)
