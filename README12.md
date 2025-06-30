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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0dfaa5e-0127-3a98-86d3-f7149d67adfb | -10.86982 | -53.76998 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dabf4f71-3e88-301d-8524-dea94db65de6 | -12.10168 | -54.67093 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc268a4-f81e-3e49-b817-5fdd2a16c5d9 | -9.24385 | -58.7367 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e3a249c-49fd-3ed6-8593-5c183254d617 | -12.61738 | -54.21514 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 90410536-3ba9-3bb0-b12b-6c05abc46576 | -9.08739 | -59.4922 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a4d44b4-77ad-3f0a-b9a4-84905f755c02 | -14.86948 | -54.80697 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 860ff1cc-4171-312f-bbcd-f8d5a691708e | -12.46548 | -58.56848 | 2025-06-30 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c452a7-a42c-3401-8082-e901bde998ea | -9.71142 | -56.18161 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a447302-b47c-3957-ad89-d7566aa4abbc | -11.20423 | -55.91382 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e964110-5f58-3f47-8015-a82c8c349dcb | -12.07355 | -48.45493 | 2025-06-30 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4b2dd47-7fe8-38f4-8a48-8a580df50090 | -10.5559 | -52.04211 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bdec60ac-a2a3-3bf2-a66e-d41f61cea927 | -9.25797 | -58.75853 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ff392d3-a055-3fd9-9cef-f931c9c25bd7 | -10.55264 | -52.03634 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 375abffa-88bc-32b5-9729-abf505afee68 | -10.85182 | -53.74147 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 044c6136-070f-3ee8-a796-5f3770a2756a | -10.87703 | -53.77102 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ed74819-daa9-3143-b102-1335866def13 | -11.2026 | -55.92459 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8436e9a3-d3e6-35d0-b451-d4ae878c6213 | -9.08618 | -59.49499 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b45c47d-5d34-3f13-af38-d38a03a91d5b | -10.85413 | -53.73947 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 304ae152-b50b-38e8-bfa3-56cfc45a221c | -10.79733 | -44.24436 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 73b82e84-2a5e-3a10-a721-0e20d198fca8 | -12.10985 | -54.66409 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c419891e-1991-345d-9cfe-5d78875af391 | -10.85664 | -53.73354 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d434185-da4f-3651-a3d1-a0a34105fc7f | -10.55964 | -52.05183 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38829831-d9b6-3543-a513-b4aea91a7f52 | -12.62097 | -54.21568 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ce92fc2-d16a-38b4-8c1a-44c20f7c8eea | -10.87584 | -53.75373 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6b59d5e-4a8e-3884-8e4e-632176d0f5fb | -11.07735 | -54.4586 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cc8904d-a2db-311c-8902-937596f458dc | -10.65585 | -44.48495 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ec2387b-3f53-3575-8a1c-8325e4ed4722 | -11.20757 | -55.91434 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a99d5ce-bf52-37b9-ba6d-12bb2d7985b5 | -10.35478 | -57.50475 | 2025-06-30 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd2991c3-16c9-39c2-b583-3d4c073b8e82 | -9.24012 | -58.75954 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a76565a-c90f-3f72-ac97-257b0d962b8f | -9.79641 | -55.96233 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 129a1311-deed-3c28-87b3-d85b8cc334ae | -12.62692 | -54.22512 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b88bd89b-9ab4-3cb9-9dcf-2464493ca037 | -13.58292 | -54.28641 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6423ef7-541a-3f3e-b97f-7baa4e91ecd6 | -12.60636 | -57.87701 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c9f3364-4433-3e15-b987-7c7dc5ab90c1 | -10.80199 | -44.24352 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 7e722487-d03f-3e64-9860-7ec8a8c38090 | -9.23572 | -58.74316 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 664349b6-9bde-365d-a902-67077ee2d42f | -9.47409 | -57.83854 | 2025-06-30 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e64b50d4-7207-3ead-b45c-d7d741c2ebfb | -12.62298 | -54.21497 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6cd5bc0c-ac61-3130-a3d6-704505587543 | -10.86685 | -53.73941 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1cac48a-08d1-3a5f-8aca-55e9eabc1a8d | -10.13145 | -57.77339 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74917275-0593-3b42-8db9-c8cd12353034 | -12.62815 | -54.21679 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d84f2689-d38b-3572-a6e1-6f6dfd0f89df | -10.85543 | -53.74202 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e08afb3d-86b9-3965-8340-b93ca3074d08 | -10.85782 | -53.75106 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4269f56-d4f1-3a1a-9598-6c75aa9d3c58 | -10.30479 | -57.04492 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa93c88d-2b0a-31a6-9773-c8488db8d77e | -10.87163 | -53.75739 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c0437e-d287-39ef-a8f5-588e53da8e67 | -10.12483 | -57.77532 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95bcc6c1-dc15-3e5b-9355-5a35a718a28e | -10.30094 | -57.04788 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa20d004-c9e5-331c-a984-a254da091626 | -11.27811 | -52.46697 | 2025-06-30 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09081df7-0251-3700-b348-fec6d88a3848 | -10.86024 | -53.73408 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf22f24-aa18-3480-b262-1d14dbe43ca0 | -10.30039 | -57.05136 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1adef7b6-6954-3ba8-9b5d-4065e3e289ce | -12.62272 | -54.22873 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213b1be2-1fcb-342b-8b68-eaa1616757ad | -13.43185 | -47.82938 | 2025-06-30 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da96a870-bc62-3218-98b4-c3169315913a | -10.22935 | -54.29642 | 2025-06-30 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af341b16-905f-3c0c-af85-cedb902d2c35 | -10.86324 | -53.73886 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2c37292-a042-3279-9305-a221e5871ea5 | -10.87945 | -53.75425 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a120aec3-1bd5-3094-a54c-21cbddcdb454 | -9.08673 | -59.4963 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33aa03ab-b85e-373c-a75b-fd4f8cc6bff3 | -12.20061 | -49.63636 | 2025-06-30 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc7722f6-0591-3767-bbdc-9b36eefd3711 | -9.23729 | -58.75517 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f24fea96-5da3-312f-9368-5fd8f1769df1 | -9.23352 | -58.73501 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b92a4a-10e1-3f45-b8c4-a0e10f8aecea | -11.19701 | -55.91635 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b996caee-c3b2-3360-a134-0ae407578174 | -9.22821 | -58.74586 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bf2845d-3430-374f-bc58-2387b35ab779 | -11.19367 | -55.91581 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 791a06f4-7d26-3cfa-9999-19cde6a113a5 | -12.63317 | -54.2208 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddcd3b00-508f-3102-ab88-779e1f4c3efe | -9.24041 | -58.73613 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0be68938-baa7-3afa-918e-fe3af9231fe5 | -11.20594 | -55.92511 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11709e78-36c6-3034-a52d-08cf80c87e8f | -10.85482 | -53.74627 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae17a4ea-0b04-3389-98f4-e5cbe1239df1 | -12.09469 | -54.66985 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07a106f9-9b68-3634-81b5-d455eafd72ae | -9.25108 | -58.75739 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0565434c-0ff2-305c-8ef1-a9fd1e31116c | -11.07385 | -54.45809 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ea3489-3d58-3dd2-bced-b6c0f1be8028 | -10.85964 | -53.73832 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16f221bc-fd7f-3085-8c1f-bc2dbeba8867 | -9.49158 | -56.08641 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82422a03-c3dd-36ca-9130-61da76ee1b4d | -11.21261 | -55.92614 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71466db3-a5b6-399f-8abe-ddc3a8116e98 | -12.61353 | -57.87456 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e136958-5993-30c2-bd03-a365a27cbd5e | -10.87403 | -53.76631 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73f9eedf-6b64-3aef-9d01-6ea1bde15a63 | -10.2966 | -57.1401 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f35762a-801f-3fb2-b88e-77cb1cb407a5 | -13.08571 | -54.84763 | 2025-06-30 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17ba007a-0927-32b0-99e8-6d2d280a31ee | -9.24949 | -58.74542 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63863574-097f-3813-aa4f-251f681cba0e | -13.08163 | -54.85108 | 2025-06-30 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12ca6114-1d68-361a-98b3-ae50b8d105cf | -10.79664 | -44.25017 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 713f9796-3ceb-3d0f-8c98-6b475b2ec8b3 | -9.70427 | -56.18406 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8226e2a3-2445-3b5c-a353-6dc958bf94e0 | -9.22945 | -58.73825 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a5ac5b0-11ea-3808-82bc-a9f7dcd49d17 | -13.01207 | -53.41566 | 2025-06-30 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d96f4c0-d3b5-3cc8-8968-79d832882f62 | -13.47316 | -56.85659 | 2025-06-30 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfdf7007-43b6-3c84-8e57-a61cd40e3675 | -10.87103 | -53.76159 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b0341a6-e441-3fa3-9793-2706eae5033f | -10.55123 | -52.04668 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79556e1c-e58e-340d-a1ac-8f41a8ba01fc | -12.10058 | -54.58131 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ff3b2db-4614-3925-a679-f67d75c0887d | -9.08975 | -59.49556 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd5eb691-935b-3127-9d70-403a13fa7f86 | -10.86203 | -53.74736 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31d7c121-b0b4-3511-891b-61dd421c08ea | -10.79801 | -44.23859 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 16604832-919d-3298-bfcd-789a04c1b043 | -9.22883 | -58.74206 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d55e107b-7ae4-305c-8c32-f1c833d8315b | -10.55246 | -52.04554 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e62c9c90-5711-3715-851e-3213fae6da01 | -12.62898 | -54.22444 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 29e8ea27-0975-3596-9e12-efa7b0e3b941 | -10.81162 | -55.86018 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7e9dfa7-c1e9-3899-a24f-f7a10cfa7ef6 | -12.62631 | -54.22928 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b337a94-7db3-3ea4-8210-ad1f6a1a7b80 | -12.19649 | -49.63056 | 2025-06-30 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff6e1bf2-8c2c-36e8-9ff2-c4e11efe1b28 | -10.29654 | -57.05432 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b55b7c41-bbc6-3fd9-96ff-f959c3e0363b | -9.24825 | -58.75302 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6251fc43-ad22-3b2e-9bad-f38a0db34f8d | -12.63139 | -54.23332 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11510a55-6b8a-31ca-a779-1f3f5dcaae80 | -9.24763 | -58.75682 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbd3990e-95da-354c-8ee7-3fd8033b97dc | -10.86563 | -53.7479 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e9f4551-87ed-3929-a056-87f8a412a81d | -14.02883 | -54.49361 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README13.md)
