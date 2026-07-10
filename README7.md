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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4cfb3e3-f0d6-32d9-97b0-349e0bb39280 | -11.48878 | -52.92305 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8977a36-9fbc-3841-a267-d18aeed00cf4 | -7.72787 | -44.56182 | 2026-07-10 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7944c27-8ac5-353e-99a9-12a36a4c84a9 | -9.18932 | -58.06607 | 2026-07-10 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dec4d60-42ff-3d76-a260-8b6fefe4ddd4 | -12.356 | -47.41562 | 2026-07-10 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2688f27f-3e8f-3bb8-b0e8-0a5bf726e5f0 | -8.13568 | -47.87034 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09da21a8-d6b8-330a-9cca-bdac672577b4 | -7.90834 | -55.42843 | 2026-07-10 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cc5f316-79fc-33ef-8c8c-65729ec581e2 | -13.37155 | -54.36905 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2402369-d3ae-327e-b7e7-fd5aa6259888 | -10.26336 | -46.38647 | 2026-07-10 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3fc7273-e4ee-3d28-9a75-bc272124b659 | -10.69394 | -49.60968 | 2026-07-10 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c3d057f-34b6-3d21-ac8b-f852e0b3e88f | -11.27705 | -55.79587 | 2026-07-10 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61b93fcf-0281-3cfb-b553-74308b34f770 | -13.30047 | -54.34026 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7749a632-02e4-3ca6-976b-c4d64386b523 | -9.49535 | -48.75119 | 2026-07-10 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5c1034e-c792-38ff-b7ac-e9da290be457 | -10.12764 | -50.19116 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc4974bc-a7a1-30aa-98c1-089649531db6 | -13.76111 | -46.27565 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1af839d9-c75a-3fd4-8365-c6ae836c381f | -12.35204 | -47.41882 | 2026-07-10 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3817aaaa-17bf-3294-b862-ddf3ef9c584e | -10.15463 | -50.19555 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e9fc686-ada4-3ea7-a018-3ff3284fa27d | -12.49526 | -43.77493 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87bc4ed6-5483-3777-81a9-89b19e8c14b2 | -12.1699 | -59.76125 | 2026-07-10 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5080c5f-b46e-39b3-bd05-b9b5a35e990c | -13.3682 | -54.36478 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd0554c4-ad7f-3ac0-a7a4-8249fea930e4 | -12.44812 | -49.44781 | 2026-07-10 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b48774f-d796-3a96-91e9-76f30b772b47 | -12.45465 | -49.57876 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 812fdf82-5a91-363f-9868-79bb5c9b9653 | -10.16092 | -50.17786 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d79ac5d2-f96d-3a08-ad58-397547c09664 | -7.9025 | -48.05658 | 2026-07-10 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b03fed-d054-3357-aa1f-fcb2baa3ff40 | -10.83586 | -49.3795 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53064cc5-98d5-39cc-a016-decce5c107ed | -12.49627 | -43.76741 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 82d8af01-3641-37ce-a096-083f8e60e8e7 | -10.12545 | -50.18331 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72db80ca-1cf2-3856-8944-0b4edbf9b0d8 | -13.31059 | -54.34333 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61a691a9-3028-39d1-90d7-a2a494dd9d26 | -8.72372 | -47.83102 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727850ef-482b-3174-986c-91bd5747fed6 | -8.12089 | -47.59412 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c880c5-3547-314e-be96-6984faf23836 | -10.37949 | -52.15614 | 2026-07-10 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fa6eeee-9418-3088-a93a-eb7b77d8be15 | -13.3563 | -54.36261 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1221740b-d97d-31f5-90f8-e6e59c61db08 | -11.83975 | -48.23987 | 2026-07-10 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88b54b24-aea5-3aaa-b301-917dfacfe916 | -13.76711 | -46.31106 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5813275e-14fd-3f19-b1dd-193b42f55933 | -13.2983 | -54.32919 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c992b9a3-4e8d-3962-908e-366e28954f50 | -13.3749 | -54.37331 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 728baa18-f94b-39b7-aecf-fdc14c026134 | -13.76229 | -46.26735 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50503a49-97a1-309c-a194-7861ddabbe1d | -12.49937 | -43.7755 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db4395d8-6860-38ff-8b30-2d4710005804 | -10.16779 | -50.15656 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ed521f9-a5b4-3ebc-a6c1-2cc9641559c3 | -10.60557 | -46.5619 | 2026-07-10 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3471bc2d-66dd-3eeb-a961-cef441973b99 | -11.27418 | -55.78587 | 2026-07-10 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c485a423-b408-3d23-a12d-61407e5282cd | -6.42366 | -55.79284 | 2026-07-10 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 064aaa90-de0a-36e3-9183-3fafe91211ab | -11.87533 | -47.67308 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afb85f77-b366-3135-8f44-57631fff77cc | -8.13514 | -47.87381 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bacf5fd-5f93-3809-9175-027f8ad9ce89 | -10.8331 | -49.37545 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1046c023-b9a1-3ce8-bfab-caef17b84458 | -11.49332 | -52.91911 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e26432-2562-3f25-8d48-a9963da7c5bc | -10.13102 | -50.19171 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d5034f4-1a4a-31aa-8474-9c6c6e17da38 | -7.18602 | -46.54943 | 2026-07-10 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75ea94f5-1a8d-38dc-9990-e33aec42dfa3 | -10.6945 | -49.60615 | 2026-07-10 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7a7509d-6b34-3110-8f53-4f3f9073d108 | -12.45355 | -49.5858 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e252c47b-9976-3080-a110-846187ef84cb | -8.03179 | -47.42237 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4d033ba-fc30-37d5-a75a-2f3305a4e6a7 | -13.31257 | -43.72162 | 2026-07-10 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5b2acbf-9a63-3326-a718-a9ab70afb29d | -12.45741 | -49.58282 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19b385f1-283e-3959-9f45-7de1371a8f95 | -12.35261 | -47.4151 | 2026-07-10 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e39e1a7-15ba-348a-b4fa-3d05246fc9fb | -8.52522 | -54.75786 | 2026-07-10 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bff62a3d-647e-3bf5-b8b2-ae854345bc1a | -8.03788 | -47.42691 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fac331a7-efae-373b-b07f-a118be98b06b | -11.32699 | -54.47107 | 2026-07-10 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324f1d8e-6122-3b57-bf53-a658fb137ae2 | -8.12854 | -47.87277 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7020f9e-b52d-3122-9848-8c6381940706 | -9.26232 | -47.28855 | 2026-07-10 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21b02914-6a9c-3709-87b8-7af017ef8cfe | -12.16415 | -59.76007 | 2026-07-10 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa984cb8-a4a4-3435-a973-6f377e43d1f5 | -8.72265 | -47.83799 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b43de4-f74c-3af5-888b-85216323cea5 | -11.87814 | -47.67723 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 203de459-64a8-3c9d-92ed-e4cd16009588 | -13.36026 | -54.36335 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e73edfb4-922f-38ad-b432-b9ead2519851 | -11.87924 | -47.66998 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2edcc036-c91e-328a-ab6f-7206b139096c | -10.98365 | -49.39302 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ad50c9a-bbf9-37ce-aa1e-958549feca6a | -13.31118 | -54.34935 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6ea169f-0cee-3be9-9d8b-eebdea9b119f | -12.49678 | -43.76367 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97866b0d-9c84-35d4-b0ff-19631db42518 | -8.11573 | -47.09692 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 627ddd88-9a3e-34a9-990d-6ac4cebb8a80 | -9.56066 | -48.67962 | 2026-07-10 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db2d179f-9ab1-365c-bc0d-931bbb03ea2b | -8.50668 | -48.0673 | 2026-07-10 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21b7b505-6e30-31da-853b-7c75bc3058a4 | -13.36298 | -54.37116 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 530e0334-7697-312b-80ed-91ad82001029 | -8.50721 | -48.06383 | 2026-07-10 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 819abdbf-c5d4-348d-a721-767172b5a58e | -13.2971 | -54.33609 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f0ab50-5945-35fd-8f7c-6df8ebc188d2 | -10.13336 | -50.17712 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f721b55-4fae-3179-8c0e-41a6e5174eb3 | -10.40664 | -49.44705 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88994f91-3fca-35ac-aad1-899f958d436e | -11.87869 | -47.67361 | 2026-07-10 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea6b0ddb-4e11-3fc4-af30-dd4886ac24a9 | -13.27228 | -45.15128 | 2026-07-10 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f8ef5be-1d47-3df6-8e78-bf67ec996928 | -6.58693 | -51.69854 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84a24e41-a9fb-3f03-9d61-92d139748d99 | -10.84747 | -45.04176 | 2026-07-10 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6f983e1-a7ce-3c63-a1b8-4ec0050ea58f | -10.84812 | -45.03728 | 2026-07-10 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbe02207-00da-3b71-b24d-ecfbf5a51e59 | -8.0412 | -47.42741 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff391fe-dd8d-3d01-9a15-fd0cfd546a09 | -13.36696 | -54.37188 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae78ca95-c679-332a-a62c-cd98b143e1d6 | -13.7659 | -46.26775 | 2026-07-10 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3db1e4-7f78-3688-9d92-a01cfd3cc1ca | -10.15741 | -50.19975 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab1fd9fc-bb22-3c2d-8ba3-71165d4e53c4 | -10.98696 | -49.39356 | 2026-07-10 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54f1f637-f89c-3f80-9284-d4b7c8385253 | -13.37217 | -54.36551 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6dfc4e-65b9-3d99-bd11-f6c6639d2a58 | -11.27336 | -55.79046 | 2026-07-10 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fb1b41d-57a1-36d4-9483-abd6ed2def97 | -12.16334 | -59.76425 | 2026-07-10 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e6c5d30-6989-321e-9ece-68e75057cd42 | -13.37428 | -54.37685 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6510f539-73ee-33f0-b037-27ef735ebd9b | -12.49988 | -43.77175 | 2026-07-10 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f4c6948-1d81-36bf-b780-193d33e3f3e8 | -11.47696 | -52.91843 | 2026-07-10 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a9c1d66-b6a4-374e-b9de-1fe98e52afbf | -8.71988 | -47.83398 | 2026-07-10 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fcfbd4b-02cf-3ee9-a8bd-b06bd03c6ecc | -8.04066 | -47.43091 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c13b216c-e9a8-3db1-a44c-f68cf2ba5c1a | -13.36633 | -54.37543 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1089bbb8-4d9c-3db1-b99a-7d22fe56e9e1 | -8.03842 | -47.42341 | 2026-07-10 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85435cb1-34f6-3208-bef0-a3ac17e4ce98 | -13.3703 | -54.37614 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69f69916-da7f-32c8-bbf9-e62489efa8b0 | -9.16358 | -50.89259 | 2026-07-10 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a58ac3db-c595-3fa5-bcf3-1ea5ec0cad68 | -13.30996 | -54.34679 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d5ae989-da3a-3a66-b8dc-e508bebc6c9f | -12.4508 | -49.58174 | 2026-07-10 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d00a366-f68f-37cc-92fa-0ec5186fe934 | -13.30444 | -54.34097 | 2026-07-10 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3afdfddb-a8aa-37ce-b661-3c8cfd5622b0 | -10.12882 | -50.18386 | 2026-07-10 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
