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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92e25e68-d35c-31d1-af1b-cabbdf7d3393 | -3.6215 | -60.566 | 2026-09-07 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3568bee7-2b73-39d7-a9fa-2c324a846baa | -4.1102 | -49.0675 | 2026-09-07 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 7ebffcfa-9f3b-3e57-8892-8e10e2be5dfe | -6.9475 | -59.7414 | 2026-09-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| fffcd023-4b3b-34ab-83f7-78dbb8c47c77 | -6.0004 | -57.6884 | 2026-09-07 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 237b40f3-5b46-3282-b0ce-cebe37d721cc | -6.9659 | -59.7599 | 2026-09-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 02be47f5-b661-396c-bb25-5428d4243585 | -2.9024 | -50.4423 | 2026-09-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| dd391a5c-863e-3549-8860-75ce6c3d38e6 | -2.8654 | -50.4643 | 2026-09-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 20ed324f-a380-31ba-ab32-ac8687dcc2da | -6.6514 | -59.945 | 2026-09-07 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 31bf9602-eef6-31eb-ad3a-485279b6ebd7 | -3.1279 | -60.6509 | 2026-09-07 00:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 60664e92-49df-32b7-8ffc-ddb7c546f947 | -6.6513 | -59.9642 | 2026-09-07 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| f7fe592c-f21f-32df-9b2e-5bacdd074f7b | -2.9645 | -48.7036 | 2026-09-07 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 218d0460-0914-3bd9-b386-5e4e7db453c7 | -6.6699 | -59.9251 | 2026-09-07 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| fb93a3a1-6b97-3546-b094-43ea5fb0aacf | -3.1462 | -60.6506 | 2026-09-07 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 5387f6b1-5878-322e-8241-dd0c77d4f96c | -6.9474 | -59.7607 | 2026-09-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6b533788-9bf5-3268-ac19-100414a818ed | -9.7519 | -43.4143 | 2026-09-07 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ed7e5442-cd4a-336e-a241-7af523ea495d | -2.6388 | -46.7597 | 2026-09-07 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| cb6b2d9f-bb7d-3b47-8021-4ab440f3dc89 | -2.6387 | -46.7817 | 2026-09-07 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 5914505d-628c-3b2d-b8d2-bfc71b4a6e43 | -9.7328 | -43.4168 | 2026-09-07 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| e83ef1b4-7efe-37a1-bd99-304406e4ca93 | -6.6697 | -59.9635 | 2026-09-07 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8467c527-f2a0-3844-a9fa-f0b55826a833 | -7.0603 | -56.4827 | 2026-09-07 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 01a4dbd0-6de8-38c6-a894-288014b77b4b | -3.1461 | -60.6696 | 2026-09-07 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 4ff9919b-1982-34e2-aefa-189d1bb28294 | -15.9589 | -41.7481 | 2026-09-07 00:00:00 | GOES-19 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| f099d458-a541-31b4-9878-0eb9aa0be496 | -2.6202 | -46.7822 | 2026-09-07 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3b31312c-10f1-3eab-a421-e518ddfa1ea7 | -11.1994 | -44.6179 | 2026-09-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 414.4 |
| 45a4a2e3-cc57-3ef4-a8ec-e80b8d795e0e | -2.8839 | -50.4428 | 2026-09-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 249.4 |
| 1fbf04de-c6d3-3501-83ba-363ade5218cf | -2.8839 | -50.4638 | 2026-09-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| b3128613-e0fc-35c0-ae42-1c198e6c775d | -9.7332 | -43.3932 | 2026-09-07 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 170.2 |
| 892bc4d3-4449-3402-86a4-f07e0cd5d0bf | -6.6698 | -59.9443 | 2026-09-07 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6dc4268f-cd4a-3ad2-93c5-b30599f939f6 | -7.0605 | -56.4629 | 2026-09-07 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 97c07370-6a07-33ff-b7bf-f8220dddecc3 | -9.7138 | -43.4192 | 2026-09-07 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 6f735a9a-9c00-370b-bec8-456619cec1ad | -6.0002 | -57.7079 | 2026-09-07 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 9a963978-d3d3-35e0-ab9d-ab9b4ab988a6 | -6.966 | -59.7407 | 2026-09-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a53a4d7f-f0e4-3f72-a4b8-0b6f2a0c1da0 | -15.9788 | -41.7435 | 2026-09-07 00:00:00 | GOES-19 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| 4e9586da-d9cc-3e35-948e-c6f2d1e6ca23 | -4.2056 | -48.5706 | 2026-09-07 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3ab195a2-6b68-3b91-a25b-4bf4cde0b1d5 | -5.3646 | -56.0249 | 2026-09-07 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 29784da1-bb0f-300c-af6d-4700e04ad64a | -2.8655 | -50.4434 | 2026-09-07 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 2bfed03c-68f2-3c16-aeb7-06f4e6e44a95 | -4.0917 | -49.0683 | 2026-09-07 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 958ad210-268e-3544-900d-47d9170a6ee3 | -11.199 | -44.6412 | 2026-09-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 38d5540e-0df3-3b23-9be4-accc3ec5627e | -9.7522 | -43.3907 | 2026-09-07 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 47d0a330-8f2b-314c-8bc3-b2fc26645d8b | -13.2287 | -61.7355 | 2026-09-07 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 31153683-ce1b-35e3-a1a8-2ac1aa0e5038 | -13.2477 | -61.7342 | 2026-09-07 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 22de3b66-95fa-31e7-a222-f01838ece69c | -13.2286 | -61.7549 | 2026-09-07 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c0eeb75b-11e8-3907-9151-3080d365f60c | -11.1803 | -44.6207 | 2026-09-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 634152dd-5a14-3e8c-9ba5-75349b27fb36 | -13.2477 | -61.7342 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f3b2f013-2e8b-3f0b-b153-c418a87f05c9 | -13.2096 | -61.7561 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c3056423-0a04-3501-8d12-4ba622cc5e19 | -13.2097 | -61.7367 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0b095af8-ea55-357d-b9ad-122a2762dc32 | -11.1799 | -44.6439 | 2026-09-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 9567f421-56f7-306b-a999-117441b05168 | -3.6033 | -60.5664 | 2026-09-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 32ad7861-963c-332a-913c-767df1a4ff26 | -6.6698 | -59.9443 | 2026-09-07 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 4015a851-d30b-31f0-aed5-431842897965 | -11.199 | -44.6412 | 2026-09-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 74558b26-69c7-3730-95b4-572855af5475 | -11.1803 | -44.6207 | 2026-09-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 1aa2469f-173a-3aab-a9b8-12910568f01c | -6.055 | -57.8032 | 2026-09-07 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 61ee5f6d-dd17-367e-a9bc-7f6f2ccf80e4 | -11.1994 | -44.6179 | 2026-09-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 250.4 |
| affaf653-4e2a-3e56-a071-6e53a95c8b28 | -5.9819 | -57.6892 | 2026-09-07 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 65334c15-d6d0-35c5-af8e-b1371876868b | -9.4968 | -40.2839 | 2026-09-07 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.6 |
| c881bf1b-4463-34e7-a51d-ff0ab5a85dee | -13.2286 | -61.7549 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 7c0c0d6e-8664-3d86-a496-236d8568c8c5 | -9.7519 | -43.4143 | 2026-09-07 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c0133fc5-8c80-374e-a762-ebbbfa9fdecd | -6.9475 | -59.7414 | 2026-09-07 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8d9476b7-b8cc-32bb-a8e6-458577b8da84 | -3.6215 | -60.566 | 2026-09-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 847d531a-8aae-3c14-8fb4-a9fa21f45858 | -2.8655 | -50.4434 | 2026-09-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| c5bf3659-35e5-303c-97f6-2b510ecb017b | -3.1461 | -60.6696 | 2026-09-07 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 33850638-6724-3a38-85a2-f51603e7eb3f | -2.6202 | -46.7822 | 2026-09-07 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 83208cc3-d09a-3ab4-a52b-413fa591bd44 | -9.7522 | -43.3907 | 2026-09-07 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 9402e981-4cfe-3191-96dc-c3de9efdfa2d | -3.1462 | -60.6317 | 2026-09-07 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6edcb2b0-19b0-3525-8900-26933da4948f | -3.1462 | -60.6506 | 2026-09-07 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 1d1d4856-9e3c-387f-971d-1785a7312414 | -6.6699 | -59.9251 | 2026-09-07 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 49fb73e2-2dbf-3624-b2c9-c4d5e3711597 | -4.1102 | -49.0675 | 2026-09-07 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 35543d3b-a4bf-3215-b6d8-7436ae54e085 | -2.9645 | -48.7036 | 2026-09-07 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f6faffd3-168a-38b1-b702-37a9a65ea093 | -4.1103 | -49.0461 | 2026-09-07 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c1ed7106-d0a8-3146-94b3-3a870ed39a2b | -2.6388 | -46.7597 | 2026-09-07 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| bb41ffe1-465b-353b-b5ea-f22063b73f3e | -6.6513 | -59.9642 | 2026-09-07 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.7 |
| ed26442e-462d-39cd-8075-f82f4bcaba59 | -9.7332 | -43.3932 | 2026-09-07 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 208.7 |
| 0723376e-dd58-3aa1-9065-d9bf0bf9fb79 | -2.6387 | -46.7817 | 2026-09-07 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| c2d08ce0-f3cd-3744-b0bb-1e7359aa63ed | -2.8839 | -50.4638 | 2026-09-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| d273b81e-49bc-3796-b4bf-9bddb8ad8dc8 | -9.7328 | -43.4168 | 2026-09-07 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 2bf27112-09e9-3772-abb0-a4ba6e3bbc72 | -7.0603 | -56.4827 | 2026-09-07 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8e45abd0-2f70-3930-a163-f82aaa915d4a | -6.6514 | -59.945 | 2026-09-07 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| aed80915-af7b-3d75-88f6-9487c8885ea9 | -2.6203 | -46.7602 | 2026-09-07 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 688e1ca4-31ec-3f4f-b6b3-854e957deb6c | -2.8654 | -50.4643 | 2026-09-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c5abfef1-71b8-3d63-bd0c-1a65ba0ce8a6 | -2.8839 | -50.4428 | 2026-09-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 410.7 |
| 119329b3-b515-37d5-aad8-59dbadd17bd7 | -4.2242 | -48.5697 | 2026-09-07 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 92a88233-b641-3a1b-8d46-9ed990d3afd5 | -13.2476 | -61.7536 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8ee06d99-6860-31e9-a716-9e5fd5faec02 | -6.9474 | -59.7607 | 2026-09-07 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 17678566-ba38-338a-8340-cc3e9048284d | -7.0605 | -56.4629 | 2026-09-07 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1da3d6ee-d1ab-34fa-a5bb-e96ee19a6ce1 | -7.1156 | -56.5194 | 2026-09-07 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 98a93ef7-4c45-30a0-9557-ec25c5c8d153 | -6.0002 | -57.7079 | 2026-09-07 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 9f2aefd7-5c41-317c-997c-4ef5c90b3888 | -2.884 | -50.4219 | 2026-09-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5fa50f5d-0bd1-39a0-8aa7-c4ae10940f12 | -6.0004 | -57.6884 | 2026-09-07 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| cb60f800-f51a-3a11-bc94-0fc1a9c47d43 | -13.2287 | -61.7355 | 2026-09-07 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 31c04bfa-9c91-36ff-8122-e4ff5f0da1e2 | -11.18 | -44.62 | 2026-09-07 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9f906b6-3085-3e2a-9a8d-fe8f42aa7f7d | -9.74 | -43.43 | 2026-09-07 00:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca3ca6f0-c89f-36cc-b03e-269529e2500c | -9.74 | -43.38 | 2026-09-07 00:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| af5eea37-a84d-3441-a849-4aa693e24b87 | -2.88 | -50.45 | 2026-09-07 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e8f793-04a6-3763-af81-b197c4ba9cb9 | -6.6698 | -59.9443 | 2026-09-07 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3051dd1d-a588-3820-89c3-da5c2faa5097 | -2.8655 | -50.4434 | 2026-09-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 3fe034e9-81d5-305e-be1e-8bc3a68c6570 | -6.6699 | -59.9251 | 2026-09-07 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e8132840-1543-33a2-84d8-9efcffb80115 | -2.884 | -50.4219 | 2026-09-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 42840904-9c53-3008-bc7a-661652b4c856 | -11.0514 | -44.3369 | 2026-09-07 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 03e3382c-e094-3fc1-9421-eee2d31b2db6 | -3.1462 | -60.6317 | 2026-09-07 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 248ff677-8acc-38a8-b028-a478a6679f01 | -11.1803 | -44.6207 | 2026-09-07 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |


[Clique aqui para ver as próximas entradas](README2.md)
