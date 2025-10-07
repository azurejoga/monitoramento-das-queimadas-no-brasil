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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b258011-ad1b-33b2-b4cf-3e56dd6d70f9 | -13.29868 | -48.05196 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89293768-7a84-30f1-afe4-2f58beb05340 | -10.61971 | -49.06087 | 2025-10-07 04:38:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fac116c-0d26-3314-bb51-eb81ec28277d | -11.64427 | -46.87747 | 2025-10-07 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c974f2f-33f9-3baf-8f74-f44c7be7d951 | -15.36213 | -47.32304 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f32ce60-fbab-3494-b920-64eae9878585 | -12.976 | -46.77947 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9613a653-8b75-3b9d-8eff-29491c2ae819 | -11.04997 | -50.90995 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32a06bc9-9edc-3f83-977a-1368299aa3f8 | -10.88077 | -51.03073 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 517d148d-4875-3f6c-9eff-d648b1ca33c7 | -14.65478 | -48.37225 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cf0686f-8f61-348d-b1a0-4804597dd4b2 | -10.38758 | -50.30881 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a4ffe2d-c952-36d2-999e-69ae1c990875 | -15.51452 | -46.8427 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5a1c7b0-0d26-3565-82ad-0c7f940dcedf | -11.15826 | -47.75485 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 493ef3c6-f25e-333b-8f78-da8de478bd05 | -11.83853 | -44.91291 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69f48f69-f8c7-307b-8c15-4202998e0a93 | -16.11561 | -48.94287 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c98e3e14-babe-35c0-8a32-99a638b5feae | -11.38197 | -54.35115 | 2025-10-07 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2d62e0-c4d2-3db0-ab80-70eb99b9870d | -12.2421 | -47.01954 | 2025-10-07 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b921f686-3c9b-3bb7-a39c-fcae7d6a95ba | -15.27498 | -46.33692 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9651075a-0064-3c29-83d0-2c9394bc0239 | -12.54554 | -48.14133 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fbb29ca-0615-3d15-ae5a-b29875cfd22d | -10.91285 | -47.67548 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75683ba7-d3f5-3e25-9a25-8c1d206f26b1 | -13.08791 | -47.8112 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de3ef4a4-090b-3a8f-9403-db43ccb3b7f3 | -10.80494 | -48.5932 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72a14c61-1caa-3093-bd12-c346dd6c8e05 | -15.97993 | -50.85082 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc60547e-f273-3ebb-b647-f7a0fdc47f54 | -14.83082 | -52.93015 | 2025-10-07 04:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c6fe2e2-2761-3028-a51c-87cf2e11ffb3 | -13.77781 | -43.94199 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71108df6-4aa0-3d9d-bf9e-ecb86a0356ff | -10.74179 | -50.4915 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5f436b3d-2fc6-3c7d-ba81-da9ee739cafd | -11.2475 | -50.28483 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 786fec36-5eb0-3054-bea5-28b31293dca0 | -14.90697 | -46.85342 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7a02d3-ec65-334a-b8da-499b9be49b93 | -13.7113 | -48.08881 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b383061a-8b33-35b0-ae80-02310fe32ba2 | -18.28418 | -45.45851 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a2e8fb7c-f147-350f-bbbf-a388dd4cd0ff | -12.72678 | -47.94055 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01d69a36-13ee-3ed8-b2ad-bd277cee3b81 | -13.2246 | -51.68966 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a404235-ce74-3c2b-b816-8b9261b07ecb | -11.23025 | -47.76583 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f79902b3-165b-3d78-8647-661dd5a35054 | -10.4333 | -50.3277 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 11a83882-5ab0-3309-aace-29c6356f1f39 | -12.39757 | -51.13583 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db897581-d36b-3fc6-983d-14ee549734a9 | -14.92117 | -51.45014 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6540d44-c303-3f88-adc7-1351e108f05e | -14.6576 | -48.37652 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39485dee-ec36-3ea1-99dd-a55a9eb50ee4 | -10.07059 | -50.51566 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf5bdd0a-e127-3df1-9992-249a2d110416 | -10.74644 | -49.70883 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d09fc27a-4dff-31a1-b403-8910fd06ed55 | -14.72599 | -46.01149 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 686107e6-6e0e-32f3-852c-24c93d4be86e | -14.75402 | -46.0296 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89061ad7-69e6-32da-9916-ea94dc1845d3 | -12.24034 | -47.85859 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56a834fe-b1f6-36a0-8d2b-181f4d76799d | -14.6497 | -48.35995 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d77dd7-2c83-3ed7-adb6-d6104b1cdf26 | -12.24428 | -47.85547 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8244f1a-51d6-3a49-a378-5adc26d2139d | -16.28744 | -50.97802 | 2025-10-07 04:38:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33918a9e-cf43-3194-82ce-6fd94a9d784d | -11.0337 | -50.92276 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 34eb9770-3a16-3d9d-85b1-98bacaa32217 | -13.25234 | -48.05979 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e01d9d1c-6256-33ca-bc18-3533f9f4c70b | -13.26086 | -47.79538 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8a9007b-a55e-3fb1-917e-4421b515ec6c | -15.19285 | -56.82459 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d72ec48-ce3e-39d8-85d4-c3bf54b099aa | -14.64858 | -48.36735 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c998bc98-ad0c-3362-a77e-b2f5105f6b3e | -15.58893 | -52.55885 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1a2ad52d-a81d-39df-8854-579e979ba26a | -13.23295 | -48.45728 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf4cc82a-cc0b-380b-a953-032e2b1b04af | -12.81174 | -50.52436 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c1aa90a-2930-32d0-9821-842caf209cd6 | -14.93969 | -46.81135 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c41f2d7-83ea-30e3-9010-30672184a3a6 | -15.58963 | -52.55475 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6921f6f3-24ca-3861-bf34-5d9aaf368ad0 | -13.50189 | -43.66689 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9a2e1216-2ca2-30ae-96da-cb647dcae765 | -10.58463 | -51.47123 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7ec53a21-67b0-398b-8dec-af7b2540b0ce | -9.38318 | -59.42378 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb538978-9ca7-3774-9dd9-c487a6783316 | -11.94506 | -51.47747 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72988ca9-0d25-3c1d-ac25-95e3eb278645 | -12.93767 | -46.79412 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e0fe350-ecaa-338d-a5cc-aa4a3d87fbbe | -13.64128 | -47.28529 | 2025-10-07 04:38:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b54e02cf-4ce9-3f08-b5f6-403366256363 | -10.45016 | -50.41741 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9b99fa34-521c-3f07-9ef4-ea8252676ef2 | -14.6144 | -52.48983 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 356c7e80-fec4-3159-8ee9-b92ac6a0e58e | -17.75044 | -50.37343 | 2025-10-07 04:38:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65306bfd-1ee3-3c81-bd8f-a6c30ff48fbf | -13.33703 | -47.5677 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfbb9aef-eff6-38c2-9bfb-ca10f7a7bf83 | -12.23967 | -43.77229 | 2025-10-07 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11a8db9d-7d7d-3a51-b87c-6db66c25ff89 | -11.95047 | -51.46655 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae1be713-7e15-3945-ae84-d92d95488071 | -13.94545 | -48.17542 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 462ed6aa-890c-3c35-b1d6-672185b5d1ed | -13.02658 | -51.02812 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d75ee65-aa8f-3f4a-ac42-17ab0d9aba0d | -14.72972 | -46.0121 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8451285e-030b-31c7-9fba-fa89fdc0821c | -15.99814 | -50.951 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b16f235-a0f1-34d5-9062-73b81490576a | -15.7922 | -43.6536 | 2025-10-07 04:38:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc010e12-f4fc-3952-99d1-0f1ce639e0d7 | -16.28685 | -50.98164 | 2025-10-07 04:38:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0290bc43-3207-3b73-bb5d-451b00cff0ee | -18.44788 | -42.61445 | 2025-10-07 04:38:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d2c4da7-d6b3-35f0-86a1-613636487de1 | -13.72457 | -43.85913 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3f80fd0-2394-3b9a-8271-dea1f5855423 | -10.12521 | -52.34925 | 2025-10-07 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c10ff1db-cb97-348f-a6d5-5c8e8973a1de | -14.7341 | -46.00813 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cb7468-7a46-360f-8666-4f8e97da8706 | -13.09259 | -48.00911 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fa0db45-0943-3962-b33b-3c0a90af9ca8 | -11.94832 | -46.43565 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a618e7db-347f-3da1-8dfe-efda0d3a4429 | -10.32834 | -51.23153 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7dd03e57-8b17-3b7a-8dba-bb2befda48a6 | -12.97246 | -46.77893 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65708da8-d7e9-3682-a89e-034ffb646af4 | -14.63918 | -52.51557 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c1dfdc8-805b-33de-b645-59a4edeaaefd | -16.27345 | -48.68155 | 2025-10-07 04:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7890943-b245-30b3-a106-bd73e366e66e | -12.38414 | -51.11026 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb36d6f3-cbde-3eb2-ad82-e1fc04b1358d | -14.81144 | -44.89435 | 2025-10-07 04:38:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77fb1bb8-fd7a-36bf-98fe-dcf3013cbb9c | -15.4465 | -49.10214 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f960cd2d-673f-32d1-9fa8-79aad35083b1 | -13.37097 | -48.03699 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d3381a4-6b03-3c7d-ab6a-129122e87a16 | -15.0942 | -46.64068 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c7d1159-9b41-3c00-bfb3-fc72b2d42b6a | -13.39017 | -47.58871 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe7a3fe8-7da4-34ac-88c5-4b9015c766e2 | -16.2957 | -50.99072 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f5ef302-44c5-3649-ae01-836ab9c33f6d | -11.16832 | -47.73438 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a4b9eb8-1f50-3b27-abcf-2b7ac30f1889 | -13.34387 | -47.56906 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ae7d783-ff22-3822-acd3-0d974b33419f | -11.1585 | -47.95435 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3c52005-feb7-303e-b125-d6502536b4c4 | -12.90844 | -54.73819 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eca2c548-9bec-3dd0-abfc-9ecdb4305ca6 | -15.61213 | -52.57138 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb06920b-5642-35f4-9dd8-d3fa26779e68 | -12.46172 | -48.00527 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 226d75fa-940f-3d9d-a777-27ab9448a748 | -11.13274 | -47.21681 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9d308a0-86f1-310c-aeab-66fcf925e195 | -15.51515 | -46.83831 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f7c9b66-0473-3175-9872-62361500451b | -10.3412 | -54.18821 | 2025-10-07 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6512db3-172f-3eb6-9469-522459fa0e07 | -12.23919 | -43.77583 | 2025-10-07 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc65e879-45c1-38c3-84af-a27beba042ae | -10.43211 | -50.33504 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a14b5bc-4a55-397f-a6bc-0bda2cbc42a0 | -12.94507 | -54.7223 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
