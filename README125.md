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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e13489-48cd-33b4-9344-4dd8e3ef4e0b | -3.3821 | -61.2901 | 2026-09-19 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 911616e9-4cfb-3ce8-b66d-66145cbad6e6 | -12.0086 | -49.9606 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 223.5 |
| f0e8b7db-ef20-3196-8059-9e1dc37c52c9 | -3.3637 | -61.3282 | 2026-09-19 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 07ef07db-38e7-39a8-9cc2-764745b74bf0 | -8.6173 | -54.5924 | 2026-09-19 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 195.8 |
| 1a62cc79-84b7-345f-9c29-de0499583e51 | -10.9168 | -50.5992 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fac87d4c-bacc-3730-aa0b-1d069ab5c6e9 | -7.7847 | -44.8441 | 2026-09-19 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 2d69cba3-c38e-3397-a7f7-900f524c1da3 | -11.3082 | -47.2634 | 2026-09-19 15:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2bc48238-ca56-37dc-bf6d-b0b8698aec8d | -6.9224 | -55.0376 | 2026-09-19 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 51c9b826-4273-39b1-a4f1-30c8fb53d36a | -5.6408 | -43.392 | 2026-09-19 15:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 2113630f-5187-33f5-b90e-7ef965871cf7 | -11.8746 | -47.6125 | 2026-09-19 15:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| ebcc49e3-f0d4-366a-95b6-afe2630871da | -12.0089 | -49.939 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| f3370ea3-44df-33ae-a385-3be5664e695d | -11.9109 | -50.1232 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| dcb9afed-4836-3f01-9f70-31ef8232e0ce | -2.9157 | -57.7983 | 2026-09-19 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 7d338127-aee8-3bf8-8eb3-38b78c2e9f81 | -5.7429 | -57.6009 | 2026-09-19 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ef61074d-6365-374b-9235-30b7bc110161 | -10.6703 | -50.6465 | 2026-09-19 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 5b7ff119-030e-3ba1-9790-cd287c9fd9fd | -10.913 | -50.8762 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| f0461cb9-4be4-3b81-8596-769273a10ecd | -9.2676 | -48.2472 | 2026-09-19 15:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3304e33a-9895-3a73-b6ca-4372063ccc4c | -3.1513 | -58.6633 | 2026-09-19 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4135bf63-a995-3dea-af2e-91b833ca3a10 | -3.6619 | -59.2676 | 2026-09-19 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d2d8e9a0-668b-3b04-92ef-09012440f91c | -12.0277 | -49.9583 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e8d5717a-404f-3856-8c72-793218a9e2b2 | -3.7311 | -60.6018 | 2026-09-19 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 16d04660-d1a6-372c-bcab-c5ba8f0ab38b | -3.3311 | -59.8101 | 2026-09-19 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 19745443-0593-3367-9066-23e4357a7be2 | -10.8469 | -50.1795 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 251.3 |
| b869fede-af40-30bf-87a0-9f6e1732715d | -11.9299 | -50.1209 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d82a21a4-cc9f-318a-b5d6-424f028c1106 | -9.1523 | -49.9853 | 2026-09-19 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| b937adf5-99dd-3334-8604-ff1326b457a4 | -8.1688 | -54.7432 | 2026-09-19 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 267.4 |
| c4e6d99c-f6ad-30b0-898b-18d0ffa73907 | -12.0082 | -49.9822 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| ba635b14-1c69-333f-8bd6-5cbd15c02608 | -12.1093 | -50.8499 | 2026-09-19 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6b345ac6-e715-3e56-8688-f5027ec3183a | -10.6703 | -50.6465 | 2026-09-19 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 2476ec63-db79-3b86-8330-cbe277ef61cb | -12.0086 | -49.9606 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 4385cf52-87b1-3dd5-ba57-28ac440d966d | -3.6076 | -59.0769 | 2026-09-19 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 524d1107-10bf-3cbb-8d19-6e22791c7873 | -12.0082 | -49.9822 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| bb31c723-6952-34e1-80f3-b59cef37bbd8 | -9.3611 | -48.3032 | 2026-09-19 16:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8cf535c6-a398-30fc-8f80-6b539f745efe | -10.567 | -51.3137 | 2026-09-19 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| a14fed81-2980-3854-ab18-04a86a9070a2 | -10.7991 | -50.9093 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 53732b1c-0a9d-3187-9cf3-20019eb79bd0 | -10.7133 | -50.258 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 3260beae-e974-3c22-bb8a-4831a4521465 | -3.3638 | -61.3093 | 2026-09-19 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 207.2 |
| fab28043-3f14-3c51-ad33-558f4dcb1c20 | -12.0277 | -49.9583 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 75c74cd4-6912-34bb-9d59-49566c0954c2 | 1.3817 | -56.0636 | 2026-09-19 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 218c51d6-bc2f-32cf-b977-befef40cee4d | -10.913 | -50.8762 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 26698c57-0162-34ff-b6a0-e9541b8e60a5 | -10.7733 | -46.1869 | 2026-09-19 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| cb246f18-e614-37b4-8e91-a9c745695c8c | -11.4718 | -50.2388 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 84fff8fb-9863-3462-9b37-c25344e66ca6 | -10.8367 | -50.9266 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 60486495-5434-3762-8c0e-6163e5c4ff10 | -11.7313 | -50.68 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| b69a8647-6f94-3e90-96c7-572997eefea9 | -12.4841 | -50.0532 | 2026-09-19 16:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b81fd7d6-d65c-3b60-85f8-c7acd70fc986 | -3.3638 | -61.2904 | 2026-09-19 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 401ebb1a-03f5-3d59-930a-30e6f56dc327 | -10.6189 | -50.2466 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 7ce9aee3-1afa-3617-a510-44bbcdda8b8f | -6.5056 | -45.0723 | 2026-09-19 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| fd37afa4-8d58-36a4-bdf5-5b0dbb3ed172 | -9.0358 | -48.727 | 2026-09-19 16:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 4532fc28-6b08-392c-b4ba-6cd812cb1af6 | -11.8549 | -50.0437 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| d0071fcd-cba7-3c15-925d-35556ddfc19c | -3.7311 | -60.6018 | 2026-09-19 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b1e2ff71-c1cf-3099-a85b-57b7ae048f67 | -7.6572 | -46.1237 | 2026-09-19 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 624.1 |
| 5a0cd1cf-61b3-3d9b-bc0b-252efd6ed2d1 | -10.818 | -50.9073 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e4a2f545-d985-3cd1-b9a7-f241b39c331c | -3.3311 | -59.8101 | 2026-09-19 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 165.2 |
| caf60f92-e1ea-3fc5-9f6b-fcbc44e841d7 | -10.5481 | -51.3156 | 2026-09-19 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 2bba5f35-ad3d-3d12-9571-79732d027992 | -10.8282 | -50.1601 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 511f2a78-3bb1-38ca-9f08-dce63268546f | -3.331 | -59.8292 | 2026-09-19 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 24a7bab4-4d7f-3898-9a72-96eae95a0864 | -11.9112 | -50.1016 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 212.9 |
| e6012fca-2748-35ef-b31c-a5debe531ea7 | -11.4524 | -50.2624 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c0bb31c4-c748-38fc-9ed5-93f86032a1d1 | -11.3433 | -44.0376 | 2026-09-19 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 5200af06-d24b-3a6c-9c01-d02202e3f699 | -10.5667 | -51.3349 | 2026-09-19 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b340223f-ce41-30eb-b4c4-be396f48d8f0 | -3.3183 | -57.8677 | 2026-09-19 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 44e81c76-6d04-38a1-b7ed-6dc8c89f7d3c | -6.1838 | -47.5258 | 2026-09-19 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 037c7173-885a-3383-bd39-c62c1b3610ca | -6.1836 | -47.5477 | 2026-09-19 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| c85a87fe-3309-3b2e-ab08-36cf4e7b4e99 | -10.932 | -50.8742 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c396ca8a-2081-34d2-9fc6-fa18cfe4adf3 | -12.5036 | -50.0291 | 2026-09-19 16:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 453.7 |
| 0b157365-7bc6-3461-9a59-0fc670a0d8e7 | -7.7844 | -44.8669 | 2026-09-19 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| bfde3d01-5543-3998-8aaa-74122998fdfa | -3.4003 | -61.2898 | 2026-09-19 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b825211e-eef5-3a8d-8556-034fd2a5aad4 | -9.0355 | -48.7487 | 2026-09-19 16:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 625ffd1a-2d7d-358e-a064-76b3cd79e5fb | -11.4715 | -50.2603 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 6626e9c0-daf2-3036-a163-a57185d0fd0b | -3.6077 | -59.0577 | 2026-09-19 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| dc1c92c1-103c-3de6-bb23-5e2bc785c385 | -12.0089 | -49.939 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0b0e56d6-cdd8-38b9-b91b-dbc04f38be18 | -3.7311 | -60.6208 | 2026-09-19 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 2c5c1a86-caa7-3b39-a93d-a1a177db77d0 | -10.809 | -50.1836 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3f81497e-9815-3b85-bc2c-ebfacbc46b0b | -3.1514 | -58.644 | 2026-09-19 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 27032eaf-5f01-3864-89d9-ed15adfa12b3 | -7.8601 | -44.8366 | 2026-09-19 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 0cbc6249-1a6c-3a4f-9b6a-ab7e2457a5d4 | -8.8639 | -45.937 | 2026-09-19 16:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 64e416fd-2de2-30b5-aaaf-47521c0d9aa8 | -2.9157 | -57.7983 | 2026-09-19 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 64af7842-7ba7-3f22-8784-527c333b9787 | -10.8469 | -50.1795 | 2026-09-19 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 222.3 |
| 95120847-1f4d-3613-82c2-d65381001c85 | -7.7118 | -44.6451 | 2026-09-19 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 368.6 |
| 44d32813-bd2d-364c-b316-afa66313d008 | -12.5032 | -50.0508 | 2026-09-19 16:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 358.0 |
| f7fba8b4-6930-3042-90f9-0af34ff8e699 | -10.7994 | -50.8881 | 2026-09-19 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 95c642b5-328d-35e9-aa62-0c7247a911db | -12.6037 | -50.9405 | 2026-09-19 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| f92c8778-7479-357f-8b7e-c6a102ce12e0 | -11.9306 | -50.0778 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| a908d104-2c89-3b58-868b-fbfb3fc7c166 | -2.8975 | -57.7793 | 2026-09-19 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 8ae0a667-f497-362e-8e7e-2a98a80174d7 | -11.9303 | -50.0993 | 2026-09-19 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 00f8981d-1188-356b-a25d-5afd06f73872 | -12.1093 | -50.8499 | 2026-09-19 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| cc7f3ae7-4824-3096-9bce-020ebc2cad09 | -3.3637 | -61.3282 | 2026-09-19 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| f031c0da-0716-3eec-b0d7-6e2d2cab4c6a | -12.2688 | -49.1907 | 2026-09-19 16:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 1c254459-1974-3fdb-8067-7e61c6247946 | -12.0082 | -49.9822 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| fb359c46-6293-38cb-8379-0dcc6505ae2a | -9.0355 | -48.7487 | 2026-09-19 16:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 5d2762c6-c53f-3135-8649-266dfd619de3 | -10.6705 | -50.6251 | 2026-09-19 16:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a751daeb-a274-330a-9da8-c019fc705ae7 | -11.8556 | -50.0006 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 5bee719b-3276-37cc-a3b2-382be01f041c | -12.0086 | -49.9606 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 1601bd06-2945-3340-9c48-6cddc956c1a3 | -10.8469 | -50.1795 | 2026-09-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 262.1 |
| 021e609b-1469-358b-a299-4a3f3284cb28 | -10.6189 | -50.2466 | 2026-09-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| e07e4ce8-f2bd-35bf-b341-859df001faaa | -5.6596 | -43.3906 | 2026-09-19 16:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d83abff9-16f3-372a-8c65-0e4417e5457c | -12.0277 | -49.9583 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 24e6d2c3-2d6f-3c79-aad8-9ce24873f327 | -7.7844 | -44.8669 | 2026-09-19 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| cb626b05-b0f3-3021-bc17-37bb8b26a89b | -10.7994 | -50.8881 | 2026-09-19 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |


[Clique aqui para ver as próximas entradas](README126.md)
