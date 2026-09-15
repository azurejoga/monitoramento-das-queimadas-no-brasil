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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e013320c-4903-306d-90ac-3cd02041407e | -17.621 | -47.2375 | 2026-09-15 01:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ce90dc3d-4bc5-3e2a-b9e4-dd816b348866 | -11.1207 | -50.9179 | 2026-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 682300fe-c589-3f70-b12e-df18ced949a4 | -7.244 | -46.1603 | 2026-09-15 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 514317a4-4e3e-3e3a-b767-8c7ac83d11a7 | -18.1714 | -51.7466 | 2026-09-15 02:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 20a19b5b-c24d-3a27-86bf-284587806234 | -3.7462 | -61.7552 | 2026-09-15 02:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| a3c2aa77-df05-39e3-b46f-65037b17ed18 | -3.552 | -53.9934 | 2026-09-15 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 488bfeb8-cf7d-326b-b6ec-d7f39ab9b3ba | -11.884 | -43.8142 | 2026-09-15 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 19d6f23e-4a61-3589-8cd7-4fa46f7e9806 | -18.1709 | -51.7685 | 2026-09-15 02:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| df3fe0b5-79ac-3760-94c0-9bab7599ff4a | -10.9039 | -51.5539 | 2026-09-15 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 654beef8-467f-3657-8a52-3fbd3390296d | -10.7916 | -46.2298 | 2026-09-15 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5dc206c8-92dd-365e-89d8-4147858c6353 | -3.552 | -53.9733 | 2026-09-15 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8181fde0-3c28-3e85-a133-3f9efaaa22b7 | -11.8836 | -43.8378 | 2026-09-15 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1edb5c85-89e8-3848-b6f2-32023d2e75c6 | -6.1109 | -57.684 | 2026-09-15 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| c8c29546-d3e9-3500-8b01-d2883b86f479 | -4.6774 | -42.0951 | 2026-09-15 02:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 065fa62e-7822-363b-8d57-199a9f3ea90c | -3.5336 | -53.9939 | 2026-09-15 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bca5d736-17d4-3493-a059-9abc222a3744 | -16.2335 | -50.1218 | 2026-09-15 02:00:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b5c7c785-d73f-3c02-9332-674321d4d60d | -6.6953 | -58.6903 | 2026-09-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3cf33f3d-82fa-3a0a-91d0-f0c1e3c0ac06 | -2.9025 | -50.4214 | 2026-09-15 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b82151e1-f6c1-34b1-99c1-3582157fe9a5 | -10.885 | -51.5558 | 2026-09-15 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 483e1e40-32ec-3918-8acc-c6fe55b17497 | -18.1714 | -51.7466 | 2026-09-15 02:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 9de323c2-d11e-3d44-bd85-eccb9e039f6b | -17.6204 | -47.2607 | 2026-09-15 02:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0976764d-33a3-3068-94fd-2d2df1de37b7 | -9.4139 | -50.1103 | 2026-09-15 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 54caa067-987c-35a8-918c-b74ed60e732e | -3.7462 | -61.7552 | 2026-09-15 02:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| af8364c3-f20e-3b27-923f-8ebc4cca20a6 | -10.885 | -51.5558 | 2026-09-15 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6b167f9d-194c-31e1-adf6-d2701da7ecc0 | -3.7463 | -61.7363 | 2026-09-15 02:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a4aede83-1574-3755-a414-92a849854f0a | -3.1816 | -61.1235 | 2026-09-15 02:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 47ef4a49-a448-3ce7-8832-df789a637ebb | -13.287 | -51.2832 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| b56ff3c7-03ee-3ece-85b8-6260c76d01c3 | -14.2046 | -47.4265 | 2026-09-15 02:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4b23af47-caea-39d2-a3e0-aa5d41432733 | -9.3577 | -50.0943 | 2026-09-15 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| eeb6161e-889d-33e8-93c0-f5b44fe26087 | -3.5336 | -53.9939 | 2026-09-15 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 786017c4-20ae-33ca-b386-112537d5a89a | -10.9039 | -51.5539 | 2026-09-15 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7c2fa02b-220e-38a8-9729-b058ea81b192 | -13.3059 | -51.3022 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6f225662-7b44-3976-ae35-bce6494623d7 | -6.8446 | -55.5611 | 2026-09-15 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| d6096e8b-322b-337a-976a-8965969c6c27 | -13.2486 | -51.288 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 296ed043-234e-3396-9780-711e8e52557b | -13.2678 | -51.2856 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| e720fa6d-3b7b-3d35-aae1-3256c3a61b8e | -2.9025 | -50.4214 | 2026-09-15 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ba2a007b-f98c-35b2-83fa-937eae384619 | -6.1109 | -57.684 | 2026-09-15 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 5634b262-f669-3776-91ac-c6ac697943ab | -11.9033 | -43.8112 | 2026-09-15 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6cb7b2d0-8699-3b1d-9254-56ff1bd9492d | -11.884 | -43.8142 | 2026-09-15 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 96254af3-8fa9-333d-aba0-5c34ae45c5ad | -18.1709 | -51.7685 | 2026-09-15 02:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2669f2d5-3bbc-34fa-84cc-1065565840d6 | -9.4328 | -50.1086 | 2026-09-15 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7d88535f-5992-3952-9a8d-95a82ad4deba | -13.2681 | -51.2642 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 67148ad7-785d-3c48-85a5-95455417669c | -13.3062 | -51.2808 | 2026-09-15 02:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b4dc25c6-7357-36ef-ad41-d6d5f4ce0846 | -11.1207 | -50.9179 | 2026-09-15 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| aa6d9e73-0af4-3ad2-adbb-28e8e50803d3 | -3.552 | -53.9934 | 2026-09-15 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ecf54ee5-5b48-3539-be17-63ae3de94a08 | -13.2681 | -51.2642 | 2026-09-15 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4f83c622-ff76-3c60-932a-13a45666e26e | -3.728 | -61.7367 | 2026-09-15 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 31a46c09-9d2d-3d37-b662-c536f28d2d0b | -11.8836 | -43.8378 | 2026-09-15 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3df414c8-fdc6-3808-a885-b81d0db167c9 | -2.6783 | -57.5893 | 2026-09-15 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 40575522-c3c6-31fb-b48f-175d7c20d805 | -13.2678 | -51.2856 | 2026-09-15 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 6e7dc518-42ea-3be7-920c-261926543d50 | -3.1816 | -61.1235 | 2026-09-15 02:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8a6c77de-d23d-3ccd-845b-bbfb61eefd9f | -10.7916 | -46.2298 | 2026-09-15 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bc346af3-9a6f-3bca-a4a1-6251adb4dcef | -18.1714 | -51.7466 | 2026-09-15 02:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| eea30038-493c-3b9a-ab3b-b3525ec6f832 | -3.7462 | -61.7552 | 2026-09-15 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a6d29875-ff04-3218-8e14-70f78651d6ab | -3.728 | -61.7555 | 2026-09-15 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 35836bc8-4aba-3038-b405-6adc1d1c8b79 | -11.884 | -43.8142 | 2026-09-15 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 546c188d-11ff-3acf-a5a3-24656ab9c372 | -10.7726 | -46.2322 | 2026-09-15 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 17c3ef32-cb18-36b1-b9e3-1f9737d70109 | -3.7463 | -61.7363 | 2026-09-15 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8e1b62be-794e-3ddd-ad5a-29334f831604 | -2.6966 | -57.5889 | 2026-09-15 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d7797922-8f33-3c6b-aa5a-d069839841c7 | -9.4139 | -50.1103 | 2026-09-15 02:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c27791da-0328-39b0-bc9c-18325570a03b | -3.5336 | -53.9939 | 2026-09-15 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 245e9876-0b22-30d4-bcf4-b86cf614ced2 | -3.552 | -53.9934 | 2026-09-15 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 1fadcb72-e854-356a-99d0-7358b9b86b94 | -13.5722 | -51.4391 | 2026-09-15 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8a3288aa-bde8-3246-a434-ba18964f0696 | -3.552 | -53.9733 | 2026-09-15 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 35b4c3e9-741c-379a-8150-5db791c31e1a | -18.1709 | -51.7685 | 2026-09-15 02:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6156261b-1aee-3cfd-8077-c2052cae3f2a | -4.115 | -60.6886 | 2026-09-15 02:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2646c734-c412-3c1c-b0b7-ac507982e58e | -13.2678 | -51.2856 | 2026-09-15 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 66d358a0-83d7-349d-84ad-0c92a5e0bef3 | -9.376 | -50.1352 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5424bbad-086b-398d-898b-1cdbfd44e798 | -9.3572 | -50.137 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| a444ed60-336c-33c6-a7cd-1165612f4b90 | -7.244 | -46.1603 | 2026-09-15 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| da337b34-357c-3b45-8922-be9d96373eec | -13.3059 | -51.3022 | 2026-09-15 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 87d1d3da-4f2b-3bbf-b7c8-7d7f927aa2bf | -3.552 | -53.9934 | 2026-09-15 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 49781460-cc16-3403-9756-f9edd9bd4d60 | -2.6966 | -57.5889 | 2026-09-15 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c3e070ee-8e0d-3ef7-ad18-bde2ae3052cc | -18.1709 | -51.7685 | 2026-09-15 02:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 43d5f4d1-d2ca-3aca-bb2a-2b7397350c6d | -3.728 | -61.7555 | 2026-09-15 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e84db08e-1e18-380c-8a02-edf187bffb2f | -6.6768 | -58.6911 | 2026-09-15 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| cf57e712-30c0-394d-9b68-6da8d0d740a3 | -3.5336 | -53.9939 | 2026-09-15 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3295e798-8eb0-3913-bb8d-e36ea6fac05f | -9.3575 | -50.1156 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| dcdc7c17-851e-3b7d-a3a0-4048c877deee | -13.287 | -51.2832 | 2026-09-15 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 9a867e8e-3617-36a6-83f1-d883a6804bdc | -2.6783 | -57.5893 | 2026-09-15 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 80e739a4-dced-3b7f-9fab-83756b061753 | -6.6952 | -58.7097 | 2026-09-15 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a1c12604-9674-34e2-9c62-ac0387b591fe | -9.3577 | -50.0943 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d5b476ed-a4ee-3d08-abfd-d8697ab342d1 | -3.7463 | -61.7363 | 2026-09-15 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d518458d-92c3-3d04-b0d3-4e51188988cb | -3.728 | -61.7367 | 2026-09-15 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bdc145a3-74a3-30cf-a833-c1e53d19eb03 | -13.3062 | -51.2808 | 2026-09-15 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 1e8ceb48-db91-3339-b151-8b8e2990a150 | -10.792 | -46.2071 | 2026-09-15 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b4f9b50a-67a1-3d3c-92f8-d74812d726e7 | -10.7916 | -46.2298 | 2026-09-15 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| b754cdec-f678-31ed-98ca-c293477f9a52 | -9.3567 | -50.1796 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| dc15715c-38a2-3ea8-8636-dc5bdee8a256 | -6.6953 | -58.6903 | 2026-09-15 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 75501e92-a727-3224-8a58-e738538c24f7 | -3.7462 | -61.7552 | 2026-09-15 02:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8021a11b-039e-3d99-a8df-071a1e770439 | -11.8836 | -43.8378 | 2026-09-15 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a4292945-0b1f-37c4-a0ed-c1bbca101a44 | -13.2867 | -51.3046 | 2026-09-15 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| bdb7018b-98c7-343d-8fd8-df736c36b38a | -11.884 | -43.8142 | 2026-09-15 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 0afd3765-3840-31a9-b1c7-856bf9ed290d | -9.3569 | -50.1583 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 02c4668c-1669-3178-b159-fa45086eace4 | -3.552 | -53.9733 | 2026-09-15 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 89e8cf37-bfb7-3a24-b9b9-8a04557c8b12 | -9.4139 | -50.1103 | 2026-09-15 02:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| cb5c3bc9-7999-3292-973f-9ce9eecac817 | -18.1714 | -51.7466 | 2026-09-15 02:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 2e6de167-2d1e-3e0a-8626-0b87d7566809 | -2.9025 | -50.4214 | 2026-09-15 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 656ce012-6770-315c-8a1d-f831e8d80fbf | -18.1714 | -51.7466 | 2026-09-15 02:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 3d25ac00-e855-3496-bdbb-8850d022a46a | -2.6966 | -57.5889 | 2026-09-15 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |


[Clique aqui para ver as próximas entradas](README16.md)
