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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a16b06-06b9-390a-a5fe-e4c4d3c9c0fd | -17.47543 | -50.22044 | 2026-05-12 04:42:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fde4e75-31f6-3b0a-afcc-54305095884d | -11.2839 | -55.7866 | 2026-05-12 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 725e6273-46ef-3aca-bae4-9d7465ebe959 | -12.85332 | -43.75957 | 2026-05-12 04:42:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5aeb29f4-8309-3ef7-8810-cfcf937659a2 | -11.95191 | -47.89267 | 2026-05-12 04:42:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c15a8eb8-9139-3c6e-a91f-ad2f9ac3d81d | -14.55152 | -58.79546 | 2026-05-12 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36bca0c1-9881-3436-b98d-9d081f4fe274 | -12.60056 | -49.02885 | 2026-05-12 04:42:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119b4852-ddce-3f92-8f02-273b0e02db52 | -12.54095 | -57.22424 | 2026-05-12 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91b99913-6969-3936-a717-3c365174fe37 | -14.71342 | -48.89852 | 2026-05-12 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abd4f507-5058-3eb4-9a17-cd3b0087751b | -10.55554 | -56.32652 | 2026-05-12 04:42:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0b6a9b6-3916-34f4-82cd-3f51d9ec4210 | -11.74002 | -54.25128 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b3351f7-cc9d-3a74-a389-e7c0630a1b21 | -13.11217 | -51.72304 | 2026-05-12 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4116fc0c-92b3-313f-bea3-9b38c310e6fa | -14.10723 | -45.28608 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5697cc5d-eeca-389a-a7b5-2feed2322e2f | -12.40588 | -46.76072 | 2026-05-12 04:42:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c654fcc4-01a2-3ed5-8ed0-0aac3def7749 | -12.65226 | -47.09649 | 2026-05-12 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28fb33a8-5950-3524-8500-84dc5e272632 | -13.15403 | -56.81569 | 2026-05-12 04:42:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d300647-458f-32b3-8194-a1332f794e65 | -11.95733 | -54.6683 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7d671eb-58eb-34b4-97bf-46fe5163b7e9 | -11.29763 | -54.0221 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16e26781-177e-36bd-b94a-d11476bbe8ba | -13.11549 | -51.72359 | 2026-05-12 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 696552d7-f7c0-32d4-abc3-be96509f8f96 | -12.8579 | -43.76023 | 2026-05-12 04:42:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab60d2a2-c90c-3b97-afb3-6da53b196ae5 | -14.14994 | -52.88676 | 2026-05-12 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad0772e4-2c75-3da2-90ef-933bcfe6156a | -11.95788 | -54.68759 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0fb9d42-7a4c-390a-a02a-606711e531b1 | -11.95411 | -54.68689 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fb22282-67f9-36b7-b3b6-8d762737edf1 | -13.17874 | -52.70129 | 2026-05-12 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d14c137-027a-319f-ba70-871ba76bf9d9 | -11.73633 | -54.25063 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 701dccf2-a363-3983-b9f3-b0969a94883c | -11.99839 | -47.77153 | 2026-05-12 04:42:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6027db37-b3eb-3c2c-886a-81d50e6a981a | -14.14654 | -52.8862 | 2026-05-12 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93464dd8-c8e6-3f5f-a272-6b48aedc18d9 | -12.61469 | -44.19057 | 2026-05-12 04:42:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7e43f58-35d8-3329-9d1b-9f25ca90a391 | -11.29396 | -54.02147 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcd1148c-03fd-3e85-954c-a1e54f4d77b3 | -13.18431 | -52.70996 | 2026-05-12 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afdf2e5e-218c-3174-96da-6cf79a64c2c7 | -13.68646 | -44.29135 | 2026-05-12 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1df490d8-fc84-3ce0-b374-6829b156fd9b | -12.34975 | -50.03098 | 2026-05-12 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b56adfac-467f-3a0e-bbca-14cdfe9ed8d3 | -15.88232 | -43.09819 | 2026-05-12 04:42:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3977d15e-8a1d-3ece-a68e-6d1be139c4a0 | -11.95492 | -54.68221 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4252176a-44ae-36d4-ab4f-6e2700b00a9a | -14.14933 | -52.89051 | 2026-05-12 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d4a5a39-967c-34ce-90b5-3ae7245085f3 | -11.95813 | -54.66368 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 872900aa-0220-3499-a6c2-6ec2cab7594b | -11.95949 | -54.67828 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9471e83-633a-3ec0-9347-99960826c181 | -13.89809 | -48.73248 | 2026-05-12 04:42:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55c7bf97-bb75-3a47-9225-7d5f00fb44f5 | -13.31346 | -43.55384 | 2026-05-12 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0033c6ba-b7a7-3e1c-b856-ac91db614eed | -12.35307 | -50.03151 | 2026-05-12 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d64255fe-8bf9-352b-a4b3-3d6f9637c26c | -14.15501 | -45.41611 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d72575b-2c0e-3e30-8281-bf6b360b8ba4 | -11.28327 | -55.79028 | 2026-05-12 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15e92ed4-94d5-34f0-b3f2-7534fab8e57b | -15.87766 | -43.09462 | 2026-05-12 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b7e6472-0ae7-370d-9b1c-bcb4640ff14f | -11.95357 | -54.66761 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0ac8712-0929-3552-b16a-f9673612b7c6 | -11.95653 | -54.67293 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58836ebc-986d-36f2-a967-6c08228b9fda | -13.36688 | -43.20314 | 2026-05-12 04:42:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c3e35eb-a607-385e-87db-6719fa169918 | -14.15815 | -45.42456 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 858d164c-226e-3deb-8373-ed390f9dc918 | -11.30497 | -54.02336 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| addd52ed-1a07-375d-80e6-58a8f679765f | -13.11882 | -51.72414 | 2026-05-12 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ad89b2-f694-3dae-ac80-67ef1d56800b | -14.55249 | -58.79026 | 2026-05-12 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e36a2c8-bb11-305f-b5a9-4713462acac2 | -11.74078 | -54.24681 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c591c2ef-c195-318b-8696-989b539ab2d6 | -13.37167 | -43.20381 | 2026-05-12 04:42:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b2995a8-5f61-326c-83e4-9b5451cc9120 | -14.15273 | -52.89107 | 2026-05-12 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82078530-3bd0-3d20-9735-2ef0bff1742f | -11.95573 | -54.67756 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74c87202-f46b-3bc8-86e6-35f014ddf5df | -14.10249 | -45.28946 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aacd855d-19f7-3838-a157-a23834ab940f | -10.55483 | -56.33062 | 2026-05-12 04:42:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| efa785e2-c0e9-362b-af15-9465326a6cb6 | -11.30054 | -54.02716 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba59620-1944-3796-adb1-a468e646809a | -14.1401 | -45.33381 | 2026-05-12 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9d0c3f7-7a27-379c-9997-04f1c6ef71d5 | -12.99721 | -54.68224 | 2026-05-12 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb15843e-72e3-3f39-872c-b783adb7ac24 | -11.95868 | -54.68293 | 2026-05-12 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9c6bf80-9d9c-38c6-b874-882bc1297958 | -11.29321 | -54.02589 | 2026-05-12 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7656184-a8d8-3516-92b3-8b6ced9f7ac7 | -18.48471 | -51.70782 | 2026-05-12 04:44:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff28551d-0de5-33f0-8071-3446b953d018 | -19.41672 | -44.34301 | 2026-05-12 04:44:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| def2dada-f6c6-3e0b-9dba-ee0fe47636a7 | -23.54978 | -55.45277 | 2026-05-12 04:44:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 27d0ae9a-024a-3f7c-b625-3025d97bccf7 | -20.1341 | -50.492 | 2026-05-12 04:44:00 | NOAA-21 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69795f80-79d2-3fc3-ad40-5a97792c538a | -22.61349 | -51.25408 | 2026-05-12 04:44:00 | NOAA-21 | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| d743267b-91b5-33f3-bffd-c24d615ac9ad | -20.13696 | -50.49652 | 2026-05-12 04:44:00 | NOAA-21 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ba29b23-9dad-3955-afcb-0ab4bc70c459 | -22.60952 | -51.25745 | 2026-05-12 04:44:00 | NOAA-21 | NANTES | SÃO PAULO | Brasil | 3532157 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8787a1ae-e67b-36d1-9ca4-4449835bd38e | -19.11018 | -50.86773 | 2026-05-12 04:44:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 825b9e14-1222-351f-b8ec-886f40221071 | -20.13353 | -50.49595 | 2026-05-12 04:44:00 | NOAA-21 | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 881d7264-ada9-38d8-be4b-d0ac8dbf3443 | -18.13148 | -49.09599 | 2026-05-12 04:44:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1a4e995-5964-3101-9de8-005ab0aad977 | -18.32605 | -51.07467 | 2026-05-12 04:44:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8773d3ff-4af7-3f1c-b876-219dd06c14cd | -19.165 | -54.24149 | 2026-05-12 04:44:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b27108a5-45c4-3836-b249-aece4cdfa1a8 | -19.72215 | -54.65261 | 2026-05-12 04:44:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82b91f53-3118-3119-ab98-b757418c6cdb | -21.33436 | -47.08213 | 2026-05-12 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73ff584c-0c17-3f14-bb95-4fea119fb92d | -21.33484 | -47.07806 | 2026-05-12 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3fe2bf-435e-3ba7-8c12-e554bd9bfa47 | -23.5491 | -55.45679 | 2026-05-12 04:44:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d139d7ab-1318-3d82-9560-e6ba5024e993 | -19.91813 | -54.74177 | 2026-05-12 04:44:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b76deb9-c3c2-3316-8bc8-91812dc27d8d | -20.81692 | -45.18279 | 2026-05-12 04:44:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| baa6ae47-bd4d-31ff-a8e8-73eb17a5e63a | -21.28607 | -48.60185 | 2026-05-12 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7237d55-04c5-352c-9bd1-bd1828133cba | -27.88495 | -48.63025 | 2026-05-12 04:46:00 | NOAA-21 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5486d29a-6914-3515-a847-51f9ed94290f | -11.95303 | -54.66461 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5386227d-14e7-3cb7-9e4d-b8d1ab33ee60 | -11.29913 | -54.02138 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebe7f57b-011e-33db-8e1e-eee2bc1a98f4 | -10.63698 | -48.0088 | 2026-05-12 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d6ee5a3-dbcb-36a5-a95c-1176edf45b51 | -11.95242 | -54.66863 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80bc75ac-7624-38c6-b68d-23a9929e7e04 | -13.18306 | -52.707 | 2026-05-12 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e601264-ab8a-3588-86e4-b2925958582a | -11.74126 | -54.24813 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3611777-59bb-3903-b06d-6e6e693eae8b | -11.95211 | -54.66725 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfaf7d8b-afae-3d61-9654-0ea05e8a9098 | -10.13104 | -47.92835 | 2026-05-12 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44a1614b-b791-3d82-82e2-ace51a725d9c | -13.66714 | -52.1979 | 2026-05-12 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1cc722c-adfa-3750-8a64-4ae41227864d | -11.30273 | -54.02192 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bb20be-cfac-3d51-8e73-cf3e532f2149 | -11.05902 | -52.49019 | 2026-05-12 05:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b781c3d3-637e-3d74-9c91-89dec4df5c31 | -11.95623 | -54.68829 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23b6d9db-bf5a-300d-9cad-8de7cdef8287 | -9.64427 | -42.95636 | 2026-05-12 05:14:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78467731-ced7-364e-a3d3-2397ed6f0f03 | -11.98209 | -46.78867 | 2026-05-12 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06d33e65-560b-374a-8939-91f0379730dd | -11.00271 | -46.48907 | 2026-05-12 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eba4af2-5d93-3f1d-a792-c026f8f38540 | -10.55335 | -56.32795 | 2026-05-12 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e181071-e034-3e5d-b13f-2a0656449e40 | -9.45349 | -47.82474 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8166cb0a-32b0-3062-97d4-a68454c7c436 | -12.8588 | -43.75903 | 2026-05-12 05:14:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f138d475-fece-3562-b99a-ae07b73b93e9 | -11.73706 | -54.25173 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ac3dbe7-749a-36e3-842c-f8e40da3167d | -11.2907 | -54.0286 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
