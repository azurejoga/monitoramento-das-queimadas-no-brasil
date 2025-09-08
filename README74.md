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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50413a63-f89f-3b29-a494-0ff9e2618924 | -11.90177 | -46.65141 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a93a8cd-f3f8-3d37-9e8e-afbc39595ca4 | -15.00641 | -48.14492 | 2025-09-08 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7d09123-ebc5-3255-984c-760bb3fd7945 | -15.24511 | -52.38154 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf1a0773-1284-3095-8971-3c8570883fd1 | -9.44753 | -61.81905 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6aa40bde-1b2a-32d3-9a79-b80efd8f4721 | -15.22892 | -52.3462 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d39c31d6-a981-3d00-b4e8-45b83c8b07bf | -11.18691 | -55.05217 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e692643f-f46e-3754-9025-0e0e453bc560 | -11.69655 | -54.54837 | 2025-09-08 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28bd3180-fc38-3c70-af01-f562ac4bfda0 | -12.9515 | -54.78769 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca89190-83b1-33f4-b813-7fd1628cfc6a | -12.63443 | -56.97924 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4e52afd-9486-3298-87da-ab4aa62d5c74 | -16.91088 | -45.82578 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1f78793-f787-31b2-9f82-fe214fb62631 | -13.89734 | -53.98239 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4804e17e-32f8-392b-83ce-f58bc00ee2ac | -14.87634 | -55.81873 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52da8fbe-a598-3efd-a871-1994882c38e8 | -9.38778 | -62.33651 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd629a8-5bd7-31b6-bd64-5bdf5bc9a340 | -16.95535 | -45.76488 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36ac04d1-524f-3761-abc6-0b1d95b08a94 | -12.94101 | -54.7896 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a10ab87-3c1e-3739-b67b-3be559dd676f | -12.94493 | -54.76484 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3794d61b-ddef-3cf7-9ea9-909d67dcf7a7 | -15.8331 | -52.29063 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 910ea04a-1347-368f-9bbf-037b7cc9e574 | -12.93439 | -54.78852 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33edadb5-9c6d-3120-b253-b46792a4dcf6 | -12.95043 | -54.77301 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd6c0f4a-acaa-3960-b7a3-227f6db8c906 | -15.51466 | -52.78795 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81d4c7d1-7dc4-344a-8f03-17851389ac0c | -11.21841 | -55.00573 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cebf6d70-a8fe-367f-a256-86fabe87118e | -15.75812 | -56.42566 | 2025-09-08 04:53:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1c7729b-c583-32e7-8a34-9c4c64a15352 | -11.98098 | -50.39623 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4632cc3e-03d1-34c6-bf2e-5092bf0bd577 | -11.90757 | -64.967 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b11b542d-ee64-35da-b95c-589a8ffe86a7 | -14.50082 | -48.80967 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8cf51f8-6936-3954-b50f-83b89feb62b1 | -11.11296 | -52.04479 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad2ff952-2e9a-3237-b8c0-45599dc8a7a2 | -15.7432 | -53.57834 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f72e2b9f-6466-3c9b-b6cf-1e0d985cbf66 | -11.38798 | -50.41132 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03b34083-2a1c-33ea-a605-c09ed38591b8 | -11.89746 | -64.98765 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0560027c-f694-3343-80ae-1eab946edcc3 | -12.19421 | -53.91302 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 783ab589-01de-3156-9d02-e3b87c4b496a | -10.14709 | -61.13647 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3780b5a4-efe6-3820-a9e4-1beff46038ea | -15.73761 | -53.56982 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a456eb-3e9e-3c13-ab31-08e9c5921a47 | -12.00019 | -47.7773 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1c0694f8-ade9-3118-a5f5-4af68e53fac1 | -13.83164 | -46.24398 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3eea0f0-3fbf-34f5-b746-d92322bcddd3 | -15.74937 | -53.53753 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea5e1a59-16c1-3fad-88be-7756aa2e2055 | -11.61306 | -47.14553 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df039f37-703b-3b41-9a02-6fdf894c5907 | -14.51546 | -48.7959 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8edebf9d-4e73-3f9b-9673-4cc8d7c2a5fa | -11.63946 | -46.63063 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d67ee7e-77d5-3fd8-8c49-1220bfc1943f | -14.29703 | -44.87902 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3454fdab-ce21-3e9b-8702-f6334f5b582c | -15.75273 | -53.53809 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5a6b879-c2f8-3ece-8b69-374c255bec08 | -15.23819 | -52.35588 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe69609f-4e54-3f6f-84e2-bf28d5bff1a3 | -12.61963 | -56.98087 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 85d7e93b-7543-325a-a853-958c40eb7974 | -11.87648 | -50.95958 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d363c20b-3a28-387a-84c0-29a2959d419b | -12.016 | -50.381 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8129ddc-86c0-3698-be55-92d50e89a0de | -13.51311 | -50.80826 | 2025-09-08 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84263ab3-bc0b-3042-a33a-363dd9b804d2 | -12.94768 | -54.76892 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2ea5786-0f70-3172-97f8-ed267011f82f | -11.11129 | -52.05597 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2722a256-b88c-371e-bc87-06cedf753911 | -12.93938 | -54.77844 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21092cf6-a13e-37ea-bebf-490f0bff4714 | -13.64786 | -43.80542 | 2025-09-08 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5f69f825-3afa-3588-a0ab-18e89f4553f3 | -16.43848 | -49.28184 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b151741-1cd7-368c-b18d-dcbc5d303ec3 | -11.38306 | -50.41948 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3bcc6744-6146-3827-b3eb-d0585934fe62 | -10.88179 | -55.71659 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4a7a8f1-0900-3795-b090-b27a4bdb41e8 | -13.81265 | -46.27505 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e36abc2-8cc2-3bf8-9e96-3b46cb331c75 | -15.25138 | -53.79611 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0789eb3d-e219-3cd9-bd09-cc69f11c0e16 | -11.38735 | -50.41568 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 392c9b1c-13d6-3fec-bf4c-2a1a62b263e1 | -17.16855 | -44.44096 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d42fff-24fe-3e84-805d-2eb65aa34f82 | -12.82347 | -52.93459 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a3dcb61-220d-367e-b3d3-fc4ebddd67d2 | -16.91238 | -45.81198 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0910f8e5-7cef-36f3-959e-9c26c4e69d05 | -10.15082 | -61.14269 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e2cc637-ab9b-32e6-b4f9-a9090b0c09a9 | -12.89666 | -47.99424 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c9fa89e7-20c4-35e3-8f80-9807438ad2db | -12.80786 | -52.94703 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abf63538-7eda-3e43-89d7-b2d92d5d42f2 | -14.8781 | -55.80787 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4090897b-6ae5-309d-af2c-9d31f1559b64 | -14.71266 | -60.25163 | 2025-09-08 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5091137-6875-317e-8c82-5a74b8b2cb44 | -17.36895 | -49.24511 | 2025-09-08 04:53:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb15e9aa-6ac2-3741-9ca0-b9592dd2e3a0 | -12.8205 | -52.88566 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e7b3ba31-ac3d-3efe-af1e-5e8b9b1b8956 | -11.86427 | -51.06765 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f51ec980-70b2-3b9e-a5e2-57adbcb5ea44 | -14.53967 | -53.15233 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a49fc5a-c031-3f05-b16d-e7879e5db4c5 | -12.83229 | -52.89872 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4843b56-e353-31f8-b226-2d58527f86ef | -11.59366 | -52.20118 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0917fc0a-e28b-32b6-8dd5-e6ac2549efd4 | -20.59983 | -47.84298 | 2025-09-08 04:55:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d78374f4-6ae7-3316-989f-3236a0cc5dd5 | -19.82596 | -47.27513 | 2025-09-08 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef4943fc-0725-352a-9db1-a52a1e87207b | -18.02213 | -47.11924 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9503b94a-dcb0-370a-9402-71a6ea3f9839 | -20.9528 | -48.45621 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 86a3898f-4fef-34c4-b08c-7a31814b1602 | -18.42759 | -48.79063 | 2025-09-08 04:55:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf005871-e7ec-39f3-bf9b-9d416d947c22 | -18.02415 | -47.11295 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 658a79ec-ac3a-3311-a338-d912c8e814bf | -23.18554 | -47.24792 | 2025-09-08 04:55:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e65f0a81-d31a-3a88-93d1-62977fec58f9 | -19.35245 | -44.5218 | 2025-09-08 04:55:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a002c0d0-e778-30a5-a6dd-d6676160e625 | -17.42759 | -50.22391 | 2025-09-08 04:55:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fc71897-018d-33c4-993d-554d018ffffd | -22.142 | -54.87145 | 2025-09-08 04:55:00 | NOAA-21 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0013010a-2b04-3d67-bb0b-3adb48e787ae | -22.46825 | -52.10395 | 2025-09-08 04:55:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7d6d1ce4-2382-33b4-93bd-4d1ac9995ba6 | -22.56948 | -54.91724 | 2025-09-08 04:55:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 12562979-5dde-3ecf-8886-e201d61b7dd9 | -19.20771 | -43.72957 | 2025-09-08 04:55:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ca566f4-f9e0-346f-99b4-970bf3fd3854 | -20.951 | -48.45423 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30e1f929-2f6a-3881-b96c-54c89ae5bcc3 | -22.6913 | -46.92184 | 2025-09-08 04:55:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3a9e098f-aa56-36df-b4e4-8330720adc12 | -20.92845 | -45.27114 | 2025-09-08 04:55:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ea7bdcb3-6a8b-37f5-8ec2-542c4b6c3469 | -18.02291 | -47.11261 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 78a2c524-c368-318b-8bbe-9ff15687e7a3 | -20.95041 | -48.45939 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 601d940a-0a74-337e-b55a-361ecf1ec5e8 | -17.5823 | -49.79403 | 2025-09-08 04:55:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b0e98d5-d599-3b6f-92da-92dc6c53d24a | -18.04594 | -47.09756 | 2025-09-08 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6121c368-9d9e-3867-a914-f5320a9cde91 | -20.95696 | -48.46195 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4dd98457-38bb-3675-a3d9-a6cd660a7df6 | -19.87186 | -46.15089 | 2025-09-08 04:55:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f08bb453-b0a4-3d93-a755-9b64a1d273c2 | -19.73056 | -47.89676 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c9b13f2-4f22-3ab9-b0bc-522c28dfe65c | -20.95983 | -48.46052 | 2025-09-08 04:55:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2289ac23-38c8-3663-bcd7-a03300ed37b3 | -17.5818 | -49.79787 | 2025-09-08 04:55:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dda982e2-2d34-3dbd-80d6-f2543e6e5081 | -17.63846 | -52.57997 | 2025-09-08 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24f53263-90f2-3ded-bc01-41daef79400f | -20.1022 | -51.10579 | 2025-09-08 04:55:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd87787-7af5-3f2a-8bc6-e93f7c1f1d45 | -18.24092 | -46.62409 | 2025-09-08 04:55:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46b3d415-561d-31d2-bfb4-3b12446a2f17 | -18.95792 | -46.79873 | 2025-09-08 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fad546e-71d7-37a7-85fa-e62a767397ca | -17.76459 | -48.60987 | 2025-09-08 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86df3e9b-76c6-31f9-81f7-bec77fde6100 | -19.52735 | -47.8878 | 2025-09-08 04:55:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README75.md)
