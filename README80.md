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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4545fa4e-b4b2-3367-aa73-d1d3c99cdf48 | -9.72098 | -48.15593 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4447845b-a7d5-3acc-963a-46480c693c04 | -6.61523 | -50.06183 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 314da7b0-937f-3e90-95f3-a9c9847097c7 | -11.01392 | -54.12494 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 992dd489-b3b8-3d87-bcf1-0f358a7b14e9 | -10.83931 | -50.94073 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49e11dfb-00a6-3f1a-a08c-b6f2eb367a29 | -11.71282 | -54.5518 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 361bc317-e254-381d-aed5-3ffe1976cde9 | -13.01397 | -46.91684 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3d4fe05-a75c-376a-83ad-91d61996a6be | -8.78113 | -48.66798 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1051357f-3acd-315e-8389-2702b39b67fe | -5.83553 | -53.55581 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 150de233-9de4-36c7-bdd1-84367a4af2d8 | -11.65806 | -43.42133 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b870f8f4-4399-3a00-b3d8-be435e8cce68 | -10.88098 | -54.07539 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1482e617-940e-3c7d-be92-52aee58b51f8 | -11.37395 | -51.40292 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 057de8f2-0e3b-3759-a44c-35e08dc99c91 | -11.08107 | -48.3138 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dba6fbcb-0f7f-3ac6-a2d5-73729b1326d4 | -5.85548 | -52.0751 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b50663-e890-392f-aa2c-df30a7289fa3 | -8.60978 | -54.60833 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e07f52a-eda2-3c82-9584-531bedd474cb | -7.43561 | -44.74314 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a878724-bfce-3598-a349-513a4781db44 | -12.5739 | -47.08345 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac24a206-d4a2-3260-a41c-dfd4af172813 | -10.60542 | -46.52479 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 037daede-0d3c-332b-9706-3db9237084d9 | -9.73232 | -46.08342 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee7d3c9e-1b30-3912-960c-d68ef2c3dfa2 | -10.59406 | -51.90597 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa460dbe-7c9f-3d8d-82c6-749be8e1969c | -6.79872 | -47.82192 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6db5e2c3-51f6-3156-9d4c-c182ca0006a4 | -10.88058 | -53.98437 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3a2b3fe-780b-3bb9-957c-70d10e104161 | -8.6342 | -47.61663 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5072bda-8531-37a7-8748-671912c89151 | -11.29258 | -54.04588 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fbdd010-7a8a-3c6c-a311-e494e5a922b9 | -9.23621 | -46.23424 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 006403f8-501e-37b0-9306-2d01a82ad652 | -7.57636 | -44.89808 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33c50d92-0fc6-3772-a6f9-a94acab62249 | -10.96109 | -57.19801 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48e8d732-f7e0-3a63-a438-bcb48064d041 | -11.9039 | -47.63303 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e9970b7-2cc1-3890-b721-03279f0dadeb | -11.48011 | -47.79436 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd6d7e47-c864-3169-9d22-752e1636fa3f | -9.02518 | -48.75675 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b06d360-ce78-3ad5-8c4e-e6b1cdff880d | -12.87754 | -51.00507 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b8eb10d-9cf8-3ddd-b73b-1a978fdd7803 | -11.27822 | -54.12658 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9c66549-83ca-31a7-b7b8-a66882ba2861 | -10.39008 | -51.86848 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97c97c4a-7baa-3774-8d60-510a187f85fa | -6.99342 | -45.67635 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6d39563-ee5a-3628-b2b3-8afd28cecd32 | -11.94322 | -55.92738 | 2026-09-20 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c365f6eb-f613-30de-b353-120c91e394e8 | -11.48289 | -47.77617 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e299fe77-2187-392a-94f1-01b3c60cc434 | -7.42825 | -44.74199 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b40e01dc-d245-38f7-a41f-c797a91ec63b | -8.14947 | -54.80869 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dea5b22-1d17-3920-8c44-e5c1c21e202b | -13.20952 | -51.75836 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aea4f7e-cd4f-3f15-9a34-5c705a4a2151 | -11.7156 | -54.55988 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d79f4268-4228-3082-b6de-a8107670aef2 | -11.85267 | -47.66747 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9b4de49-0f8f-3832-876b-1b18c8c92d28 | -11.63385 | -47.76941 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e1a6b8f-7f6c-3256-8c0d-f3fe1b6c628f | -9.69568 | -48.33887 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e80d987-f67c-362c-aa88-1a044e2b3bd1 | -10.39347 | -48.90956 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d02f5c7-5779-39a4-a766-6eb2e366340a | -11.12002 | -47.71685 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1809452-0085-3b78-89fa-8a4d0e72c388 | -10.09474 | -48.41365 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90822002-cc0a-3502-ae55-ec995b70fe49 | -11.23769 | -48.37863 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a8fd6a8-3b24-33cd-9d3f-3838911b55b6 | -5.83721 | -53.52097 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea56ea11-beef-339c-af43-1e6a1167b962 | -6.61806 | -50.06611 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d7ee5c9-2fc4-3e0a-b61d-5fae83f5f7a4 | -12.47436 | -50.05033 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1fb49f5c-e125-3ac0-aae1-c3dfe86fcc34 | -12.5227 | -50.0437 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29ba7eff-95da-3efd-8d3a-d6e55fd08698 | -7.88247 | -44.84631 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b48b9721-3daa-3ad2-bf9c-210cfa7e4923 | -10.11395 | -45.56186 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2dd09d2-f92a-37ef-8a22-0d43baeae383 | -10.56971 | -46.5484 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d50a0ed-f844-3107-9c7a-e0d28f12bc0a | -12.64147 | -50.92754 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea971b9b-820a-320a-81ae-d148416662f0 | -13.25124 | -51.74184 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609f8b3c-0597-32ff-8a8f-175d8b220e29 | -12.15548 | -47.03001 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8d3a252-225b-3d99-a298-84d2aa738bcc | -5.86161 | -53.52905 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b56e9ea1-5769-311b-88c4-9864cd3fc703 | -12.15143 | -47.03337 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 118526e5-8ac9-3d3b-a3fb-ce0a90767a9c | -10.8717 | -57.14992 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fa1093-3bf7-30f4-a554-73a07217eb35 | -9.83065 | -46.44038 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 040687c1-4cd8-3c77-b726-70d97e196a5c | -13.72948 | -48.78583 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e15e1825-cd90-33b8-8fbc-efde739ddba8 | -7.36037 | -44.86883 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 881fccee-97b1-313e-875f-06a0ab1ea63a | -7.55161 | -45.42792 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d95b19ed-3629-3b16-a081-0b50b6bb9346 | -7.56962 | -45.40568 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19bd8f01-231f-3d0b-ae57-77b38bb63c25 | -7.16921 | -47.45196 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 484485a4-f648-3cbf-b09a-aba663661f5e | -9.24099 | -46.17887 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d4c5337-cddf-3751-a8d1-0d36e5f30231 | -9.26038 | -45.95386 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ba766d9-2668-3254-a450-fcf3b55ff516 | -11.04169 | -48.30367 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6372c171-e2cb-3450-b4c9-8611e0d62479 | -10.07161 | -45.67213 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90e32c9f-56cf-3c14-b185-4b94232da816 | -7.63808 | -55.06642 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0be615c7-385e-3d6c-b977-7a96144d512c | -11.7637 | -47.44833 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cdbdb60-08f6-3ac9-8cdd-2550075741bf | -8.76899 | -48.70163 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bf18e45-5cf7-332f-a533-2fdd62922988 | -10.28302 | -50.23956 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b0b07ce1-c019-3786-8bf0-9030ae36073c | -9.02574 | -48.77464 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4adcd1f9-fc7c-3903-afb7-6d1da1516b01 | -8.75796 | -48.66426 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed86ea3c-3f7c-3403-b2cf-c87ca7ec9b95 | -7.4373 | -44.75681 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9780f801-15ad-3629-ac06-fe72caa9bb8d | -7.58848 | -46.73546 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6494ca6-063f-3ed6-92ae-6c689fb1e99c | -5.85262 | -53.53139 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 766f71b8-c8a1-389c-b531-e98c0f1adf63 | -11.475 | -47.75992 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b74ef7ae-d831-3779-b7cc-c211f5dbc08d | -8.92782 | -50.91436 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51a7b516-ecfb-3bfc-a0e5-8cf4fe1c8cb8 | -11.20606 | -54.08151 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 858dc187-c9c5-37b0-a194-6e61908c8d9c | -8.05376 | -46.28101 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 492ea327-cda1-38e2-9684-8ab837cff2fb | -13.31747 | -51.78423 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da71e79b-8b57-3f32-b070-b86db595719e | -10.66124 | -48.69793 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b611e63c-d8a8-36ab-b1fb-5914f7235f94 | -10.92751 | -53.94998 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 77e92ec1-40e2-360c-a79f-038be64fd482 | -11.45234 | -45.37082 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb1006b0-2df0-3485-8f83-6fee53c757c4 | -9.96745 | -46.5595 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e057b5bd-99a3-34c2-ac25-8066e31fbd16 | -7.53613 | -45.43387 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 66a2dcf6-9aec-31e9-a848-77c1deeffd7c | -10.87753 | -53.97847 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa0f51c-3db4-3ba1-bcae-776d4509477f | -11.63723 | -47.76993 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b94a081a-ad4b-3f4a-b9b6-44cf2ec4e93f | -10.26827 | -50.26681 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 997c3471-07fc-31bf-964d-986b4bcd2e59 | -7.28286 | -45.5535 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7503580-2826-3003-a97e-ccf8bb5b249e | -10.41284 | -48.93804 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf68c7b2-0f21-38c7-87ea-62461602e430 | -10.09198 | -48.43119 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70802708-d268-3886-971b-be370cf7a17c | -5.84324 | -53.56112 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73ea6980-51d0-376d-b172-31ad34d8eba3 | -11.41898 | -51.46518 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d14dc57e-9a4e-3b2d-a58a-b63afc015d15 | -10.46748 | -51.27746 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ecbe254-ecac-3a28-9bfc-455dd8bc1c48 | -8.16641 | -54.76339 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d99fabe-fac3-36ac-9d38-3136d874225e | -9.6951 | -48.32092 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd824afc-2133-31e6-8978-170eea692520 | -11.83738 | -47.63095 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README81.md)
