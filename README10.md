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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a8255b0-92a7-3209-b935-185c74d19a1f | -11.98401 | -57.1949 | 2025-06-16 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef6f5198-23c1-3bf2-ad38-e94d9c5ec37d | -11.01085 | -55.06285 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 851d4f78-e76d-38db-af45-f8b5965a46a9 | -8.74876 | -47.17281 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2005825-3b17-39b1-b274-cdc5662e919d | -12.48638 | -58.46891 | 2025-06-16 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0089d938-367e-37e2-a9f1-5e5b489bca9e | -10.07288 | -52.74142 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 693012fa-f639-3600-85c8-86a4415d2f51 | -8.74156 | -47.17721 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31cef39d-827b-3d3e-83bd-a39eb2279057 | -10.07209 | -52.74332 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39511465-036f-37af-a5ae-4b3c2b067f75 | -10.99939 | -55.05752 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 400fb30a-cf98-31d6-8365-0f61ebf29bff | -12.52433 | -57.22699 | 2025-06-16 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2588c7b-4e23-39d6-8c1a-c74d6b473033 | -11.00485 | -55.0763 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70a1d87-d98e-321f-9216-2402ae114b5a | -10.07668 | -52.74402 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe4c5c42-b5ba-3bdd-885d-4bc12f6d51b3 | -11.00438 | -55.05107 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 92e1cdeb-3aaf-3436-bbdf-6b23a7de0af3 | -12.4932 | -58.47001 | 2025-06-16 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b512f4e6-7eb5-38cb-8071-d901a49089fa | -10.22702 | -54.2979 | 2025-06-16 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ec21c4b8-a5aa-3168-82ad-fde806223511 | -12.05122 | -48.0759 | 2025-06-16 05:16:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2a19ef-b21f-3ca6-9ac7-b1644d273b33 | -8.74888 | -47.16997 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbb7b347-2b2e-3cbb-944a-4f796dd92b40 | -12.05202 | -48.08147 | 2025-06-16 05:16:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4842347e-e515-38fd-b50d-e58d80ef99ef | -11.00137 | -55.07221 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fe6dd4-3266-337d-a797-e80afa27629d | -12.02874 | -57.09083 | 2025-06-16 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae5f29af-4641-3cc3-a50d-0e0b13bd552d | -12.72564 | -46.27539 | 2025-06-16 05:16:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7b04824-89b1-319e-ae3f-bdab357fcdc6 | -11.1379 | -53.91359 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0114a79-a9ea-3586-8237-71b02ce89676 | -7.64299 | -48.31888 | 2025-06-16 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da76e6f8-f7f2-3df3-8ab4-9baecf661992 | -12.48621 | -58.46949 | 2025-06-16 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| daa63129-4ae7-3615-9127-4f1fde035bc5 | -10.85474 | -53.78377 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29fe4b35-cd1d-371e-b535-f0cd27947a0c | -10.22756 | -54.29405 | 2025-06-16 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d15ec0b-db8f-3deb-9e93-132f8bc314d3 | -10.56381 | -52.0153 | 2025-06-16 05:16:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dde00cc8-3f55-3625-9ba9-b742695e323d | -12.08727 | -52.57725 | 2025-06-16 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fdfd5fb-2082-3f4d-9240-df77d1eda3c6 | -11.00187 | -55.0687 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e42c4c55-8edf-3b15-83c4-c3a191f0e20b | -11.00934 | -55.07335 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3a6eed5-68bf-3fe9-8d9f-09e5069045dd | -10.28805 | -67.42342 | 2025-06-16 05:16:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac6af612-d247-3445-b00a-d25a5658aec8 | -12.05701 | -48.082 | 2025-06-16 05:16:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 598a5068-ed7d-3313-8ce9-c91bcf38c050 | -11.00736 | -55.05875 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8b54f865-5950-3f67-96c4-997ecab4ab55 | -11.00834 | -55.08034 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e44734-f9f5-3a8e-a1d1-dc0a03b41dc7 | -11.14312 | -53.93964 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f6b1d023-8713-3244-af51-80b6ba47bceb | -7.6457 | -48.31701 | 2025-06-16 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 461122a6-5a1b-3c4e-baba-cefc7ab9d54b | -7.64359 | -48.31442 | 2025-06-16 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 424b39fa-8863-3d90-9f35-957177fb47e7 | -11.00337 | -55.05816 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dedb06f9-9653-3db3-9d40-1031517d434e | -11.01135 | -55.05933 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 49508036-6c8a-3e33-81d9-5cc14ce064be | -11.00435 | -55.07979 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44ff4642-737a-3433-a352-8f37c66a82d4 | -9.46249 | -57.84649 | 2025-06-16 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e532e329-7506-3f5c-8942-37e10b38f058 | -11.00772 | -55.08467 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fe3eea3-590b-33ff-8320-70c1c192c778 | -11.00837 | -55.05167 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d5b7eb01-2fd6-306a-8c6c-4ae8b5466a4c | -11.00984 | -55.06985 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52340bf2-01d2-36be-8933-6df6d5a26452 | -10.09574 | -52.74179 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 41a4c6bf-8f19-3f9a-b398-a173ee7b4523 | -10.92859 | -56.83289 | 2025-06-16 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f5dff8-7661-302a-8d4f-4fd6afb81bd0 | -11.00237 | -55.06518 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4eb8ff75-f180-3e77-a091-7e5ad66b856e | -12.48979 | -58.46946 | 2025-06-16 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b650b70-79e1-312c-80e1-c464964a4b35 | -10.84664 | -53.77846 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88b40970-a92a-3146-9ab2-217490284fa3 | -11.00287 | -55.06167 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cab5853-153d-3ad1-a358-d228c1535a2b | -11.00686 | -55.06227 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a4dbdba-3958-33db-8836-f0f763d3b929 | -9.3608 | -56.8611 | 2025-06-16 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9225f3d-2819-3f61-8850-8db62c5a9812 | -11.00387 | -55.05464 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed087587-025f-3350-b019-56e942698082 | -11.00585 | -55.06929 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 995be07c-803c-344e-865b-cab22a28bccf | -10.84721 | -53.77431 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c7ee799-f819-34c9-b4e0-2b785c74dad5 | -12.7251 | -46.28046 | 2025-06-16 05:16:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb586507-cadd-3da7-b5a7-d73f2321fff0 | -10.85098 | -53.77905 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95958465-f16e-3dcb-8cd7-ffb9ad153bc4 | -13.92069 | -54.62799 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0755ef4a-8477-378b-b896-c49d7826ff12 | -14.54391 | -59.87114 | 2025-06-16 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 805761af-770b-335e-8e82-274973f202d7 | -12.44432 | -63.68768 | 2025-06-16 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe99ed14-d0e1-3fbf-bb86-a591951589b3 | -14.02662 | -55.12345 | 2025-06-16 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28ab6329-8950-390e-ab92-12139718399f | -14.54336 | -59.87474 | 2025-06-16 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81983a66-f952-3b9d-876e-452afcccad75 | -15.4072 | -47.84918 | 2025-06-16 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64baf00e-3974-3ea3-9075-33fda247418a | -14.82984 | -48.45372 | 2025-06-16 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e42a628-389c-3658-bc9d-8ddb3c0e73e3 | -14.54446 | -59.86757 | 2025-06-16 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02c016ba-60c3-3afe-83c5-402bffe0660d | -14.8299 | -48.45296 | 2025-06-16 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9b2afe7-f8da-3e5e-badb-14bb078d67a1 | -13.91322 | -54.61842 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6654c599-0ffc-3cef-b47e-bb888a975d4d | -14.02609 | -55.12734 | 2025-06-16 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cc0e741-75f8-37a4-9815-a074e6da0679 | -13.91642 | -54.6273 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3546407-57df-3784-9628-97cead43d68d | -13.91216 | -54.62661 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d2c8eca-211b-3058-8b98-19b78233eeae | -13.91589 | -54.6314 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 382e7588-c021-357c-bbfd-8b9cb685aa02 | -13.91696 | -54.62321 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 941dd23e-f07a-3408-8f4f-76637892c7b0 | -14.03076 | -55.12406 | 2025-06-16 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb649aee-691f-317b-9029-bde52e5d1370 | -16.29224 | -52.93605 | 2025-06-16 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb769db8-79e4-3129-9b87-faed55fce449 | -13.91269 | -54.62249 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80558a39-f376-358a-8c2a-5c45177da577 | -13.28957 | -57.07346 | 2025-06-16 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c19471b-1667-372d-b474-f868873137c8 | -13.92016 | -54.63207 | 2025-06-16 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7a399b2-140b-3e8e-99a7-f3c54723c159 | -14.0313 | -55.12016 | 2025-06-16 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 148baeb3-a754-345b-925b-5ba08fec008f | -23.02981 | -54.83625 | 2025-06-16 05:21:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| b92a24ac-5f0e-3a37-ab32-61cb49e8bb57 | -23.03459 | -54.83679 | 2025-06-16 05:21:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 846bd5b9-a6db-3f92-956d-ad6476baedd0 | -11.0115 | -55.0561 | 2025-06-16 05:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9beea638-6c74-3dd1-a7f9-8b167126118e | -11.0115 | -55.0561 | 2025-06-16 05:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3c722b22-f8d2-3273-8bc6-be8fc2a6c7dd | -11.0115 | -55.0561 | 2025-06-16 05:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5b8da964-caef-32da-a9fd-ec1f87851d5b | -11.0115 | -55.0561 | 2025-06-16 06:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8a7bc57a-7a9f-318a-9c7e-692aab9e816a | -10.29151 | -67.42323 | 2025-06-16 06:08:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93ee6430-1095-38e1-bf58-40e5d53bfbac | -11.0115 | -55.0561 | 2025-06-16 06:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d45cce7c-0b02-30e9-99b2-76ae18d52b55 | -10.08931 | -52.74641 | 2025-06-16 06:31:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e5995d6e-0475-3159-9f25-1cb889e2db81 | -10.09182 | -52.7274 | 2025-06-16 06:31:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b941c367-f4b4-36f1-a3b1-1a172908901b | -11.00249 | -55.06692 | 2025-06-16 06:33:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6d23263d-fbe3-3a27-9d86-6c19e846f7f0 | -10.99761 | -55.0596 | 2025-06-16 06:33:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ee41e543-f401-38bd-9c31-b32edf381a98 | -11.14334 | -53.9353 | 2025-06-16 06:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9f69be32-dac4-3228-8d3d-becbf2f73c14 | -10.99938 | -55.04615 | 2025-06-16 06:33:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f0baa910-86e2-3751-b65d-a70a75484f82 | -11.00999 | -55.04773 | 2025-06-16 06:33:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 3f62f735-c0fb-3f4d-a021-0054f2dcbf50 | -11.13604 | -53.92734 | 2025-06-16 06:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cd7169bf-6bdf-3019-99bb-e5b0837289ab | -11.00821 | -55.06115 | 2025-06-16 06:33:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0134777e-3a18-356d-9d4e-4f586b82abfe | -11.00435 | -55.05359 | 2025-06-16 06:33:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c263cf7a-aa0a-3b97-8000-71212b16dc22 | -11.1339 | -53.94331 | 2025-06-16 06:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d183a0f8-b349-3ef0-83b7-379a0024b7f7 | -11.00644 | -55.07444 | 2025-06-16 06:33:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 647745d8-e617-3d7b-8f57-196bd145cc30 | -6.67208 | -43.19522 | 2025-06-16 12:04:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 5cfde8be-b56c-3038-9e0f-d97fb3449f99 | -7.22656 | -44.73789 | 2025-06-16 12:04:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ac2ffe69-7611-3f91-98c6-2c0be4bd60f4 | -5.85077 | -43.63802 | 2025-06-16 12:04:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |


[Clique aqui para ver as próximas entradas](README11.md)
