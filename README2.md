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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55e748c9-ce5e-3c27-87a4-1fb62b4d8dd8 | -7.7439 | -44.18003 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df721336-e2ad-377c-a2e8-bb2efa241ae9 | -3.50624 | -48.03959 | 2026-06-29 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bb1a1f4-a15e-3773-a400-d760a49bb52c | -4.7718 | -46.3913 | 2026-06-29 03:51:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 23829998-bdc6-3207-97ac-0f2332e2e64a | -6.6928 | -39.20516 | 2026-06-29 03:51:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d866efc-47da-35b1-92a8-dad98dad3b37 | -7.74899 | -44.17967 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1855e825-7a90-30c8-b87f-de2c2fa583dd | -7.30821 | -46.29207 | 2026-06-29 03:51:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db7c5546-f368-3c36-ac2e-663a3c038a3c | -7.55594 | -43.76941 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d27169d-9273-3811-9d1c-87da49b1b624 | -4.84088 | -42.92775 | 2026-06-29 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb46bbb7-fb67-3ccf-a622-dab9192fa863 | -4.76615 | -46.39064 | 2026-06-29 03:51:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 61ca6fe5-6f00-3b07-a7fb-02b4baf8bd14 | -7.74845 | -44.18105 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0616afef-951b-3bce-8a9f-7b44aa5b95a9 | -3.51349 | -48.03524 | 2026-06-29 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dea740a-10c3-3099-b066-e8afab3030c2 | -10.83009 | -49.12925 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83a9f70f-3a86-389a-b595-82db843a7a22 | -10.32217 | -50.1804 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 913ed8f7-4735-3000-a7bc-5f5604ce5f41 | -10.71834 | -50.24687 | 2026-06-29 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e8de1b5-c35b-3662-b5e4-93fb21343c38 | -13.70607 | -47.84967 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e0955a9-74f5-30c4-911e-a52865baf8a6 | -10.7182 | -50.24957 | 2026-06-29 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46524517-861e-389b-9d4a-8cf9d23aa2a0 | -11.15313 | -49.18584 | 2026-06-29 03:53:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa9d51d-fdaa-3986-893f-0f769baa0e26 | -10.4661 | -46.58369 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59697c78-ad71-3723-8f1d-404cbef0b73d | -10.82915 | -49.13392 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a17ccea-1fae-335d-8096-8e9f9c74d3c5 | -8.21722 | -47.10196 | 2026-06-29 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 006031fa-0b0e-3b04-b66d-384ec263de9f | -10.32971 | -50.1763 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c71290ce-311b-38da-9ae3-5627050c99a7 | -10.97977 | -49.55312 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a9d0ed3-ff1c-3127-82b6-c1a82d1cd6a3 | -9.68673 | -47.6954 | 2026-06-29 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0f2d374-736d-302b-ba29-0d0f9cefcad6 | -12.52296 | -48.29119 | 2026-06-29 03:53:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 645378f4-32e2-381d-b8a5-a6a23102e2ae | -10.33081 | -50.17082 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08d2f571-db26-3b74-b413-f584ed7bfd32 | -10.33724 | -50.17219 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0893064f-6b1b-3d96-a194-09a7a1cff232 | -11.48432 | -47.4141 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c632e7cc-47cf-3e09-aede-76cf00b702d9 | -13.85642 | -44.75128 | 2026-06-29 03:53:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81b9eeb7-edcc-322b-998e-8671dec8ebcd | -10.97878 | -49.55805 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2249c016-936c-3a52-b985-15e08e1d90ae | -11.15433 | -49.18942 | 2026-06-29 03:53:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34573353-47f5-3e82-a9fb-b817542600a8 | -9.68973 | -47.69811 | 2026-06-29 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4718c92-0322-38cc-b98d-554f2581aec9 | -8.21653 | -47.10564 | 2026-06-29 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89abc8fb-fec5-3d71-81af-6cf07efdb407 | -10.47306 | -46.57507 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15748d94-e4e3-3c88-8c61-adf0488a016c | -12.37092 | -47.44279 | 2026-06-29 03:53:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e701af-77d7-3e5b-b003-b7ba33e300f6 | -11.47843 | -47.43232 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1823679-9df8-36fb-85d3-985f5547826a | -10.71192 | -50.24548 | 2026-06-29 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 660113c5-8c0a-33a7-b9dd-206e1807a404 | -10.20892 | -46.50724 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| eab66b5a-5bb5-304e-8301-37805900647d | -11.48528 | -47.42564 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30a5f55-e299-3526-88ee-ab22cb7c3df5 | -11.64541 | -48.52986 | 2026-06-29 03:53:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 883d8398-5f05-3e63-80e7-578e035226c7 | -13.94443 | -47.32639 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b67021b7-e7b7-310d-b959-bcb304e0148a | -11.15226 | -49.19038 | 2026-06-29 03:53:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b471fa0-b58a-36fe-b9f0-7d2d1badfb28 | -12.51743 | -48.29004 | 2026-06-29 03:53:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdb5be20-110e-32b6-84a4-3e249b9884b6 | -9.22086 | -46.64648 | 2026-06-29 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c14297cc-7500-3f67-9a58-2f766fbd7fc1 | -10.32108 | -50.18583 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5fc3630c-08ec-3952-a2ec-1b2803315625 | -10.46724 | -46.5777 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d42259-2c19-3181-9b61-f95613a0cc61 | -11.91801 | -43.39685 | 2026-06-29 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 096a0db8-0eed-3dd9-bd9e-9e4f6e34c924 | -10.32327 | -50.17494 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49ff2ca3-4adf-3665-89bf-d1f889bcaaf1 | -11.48189 | -47.41462 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0cafba2-957b-3e0f-8416-ac009d509af7 | -10.46667 | -46.5807 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e50cdea1-a37c-3d6f-993d-cc57734a06c3 | -11.15341 | -49.194 | 2026-06-29 03:53:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15670bbc-15d0-3185-afb6-c2d9b6194d61 | -11.15137 | -49.195 | 2026-06-29 03:53:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f94e2ef3-8c67-3621-9332-22d0f608e59c | -13.945 | -47.32345 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c039b814-4f40-3626-b5b2-66daeab47005 | -13.70932 | -47.86095 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef10abdc-0ba9-3edc-a5df-74f2c9b3122c | -13.70481 | -47.856 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d950b5a-d6de-32fe-8642-286a06028d18 | -10.45975 | -46.58908 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 453c69e5-ed2d-385c-8e41-38b3385cfd22 | -10.33834 | -50.16671 | 2026-06-29 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0080a8ea-209f-32ce-bff1-f38dce5e6c62 | -10.48107 | -47.10401 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f908eeb-b2a2-3f43-93aa-5dfcf530dbd0 | -11.63969 | -48.52874 | 2026-06-29 03:53:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4af527f-900e-323e-99e8-721150d4ab88 | -10.48628 | -47.10564 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a53d14cf-a18d-3638-9edc-efebe3e36db7 | -10.82725 | -49.1363 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 522d0ac2-fd2b-3e25-9ebd-dab9401110bc | -11.48374 | -47.41718 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fe47448-18db-3f8d-8781-fa4f1a865147 | -11.48446 | -47.42982 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcf2c8e1-6419-3817-872f-046d2f03bc09 | -12.5167 | -48.29373 | 2026-06-29 03:53:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebcfc6dc-b919-31c5-8ada-0cd7d6d00bca | -10.52938 | -48.15939 | 2026-06-29 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb765355-4281-3c36-8e2c-d1c760e1f76f | -10.82312 | -49.13281 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3638c87-86f9-364f-a961-ae8656f2463a | -9.69047 | -47.69429 | 2026-06-29 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28be53d7-d128-3819-b70a-365f1956e29d | -10.21522 | -46.50188 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c94d1e55-2a5f-39a7-b499-7727e0991109 | -12.52222 | -48.29491 | 2026-06-29 03:53:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31e4118c-e88d-3a32-afdd-eaea4b413478 | -11.48612 | -47.42133 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50465969-a686-3b8b-9577-38dd6f4e2fc7 | -11.48863 | -47.42054 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c22275-c07c-39e0-b730-b3419c7dd395 | -10.82816 | -49.1316 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c8c3db5-c928-3186-8cf8-0680c0c07b81 | -9.22145 | -46.64326 | 2026-06-29 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0865befb-6629-3e48-bebe-45e13669edc4 | -10.9778 | -49.56297 | 2026-06-29 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4760d8e1-8cbe-3ff4-9892-da9fe206850f | -11.48675 | -47.41806 | 2026-06-29 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3941b8f-274c-3a3d-8e56-fd30eb9bd58e | -10.71177 | -50.24821 | 2026-06-29 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4407ca2d-898f-3e26-9fb4-b3f531c8a7e6 | -13.70994 | -47.85781 | 2026-06-29 03:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b050a17-c86c-3985-8121-dcaeda5d6fad | -10.53014 | -48.15546 | 2026-06-29 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eac77f84-8633-3eab-8a9d-54182f265824 | -10.21465 | -46.505 | 2026-06-29 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47c0ed56-e0b0-3f44-84e4-123820975473 | -20.3293 | -42.30747 | 2026-06-29 03:55:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f8626379-2eef-3022-8e88-0d5df6b32e71 | -20.89892 | -41.91109 | 2026-06-29 03:55:00 | NOAA-20 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eef33168-8595-3a44-a9cb-f530a6bc0e53 | -17.70809 | -46.77278 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8534aa65-6e8c-36d8-99f4-cd470eab6ee7 | -19.81071 | -42.87341 | 2026-06-29 03:55:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 103210fb-792d-38e5-9843-992dfe135b04 | -17.61088 | -46.68878 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76985754-f760-338f-8b35-6e53b79f7662 | -17.61542 | -46.68974 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5a97af-609a-3b8a-9be8-fe7e42919dbd | -19.91587 | -42.32257 | 2026-06-29 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 683233eb-048a-354d-8ced-1d7cc811bb81 | -15.11831 | -46.48934 | 2026-06-29 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8691d4e8-0925-3b7f-9c20-8042a0483028 | -20.30722 | -42.67347 | 2026-06-29 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d629f8b8-e606-37b6-9d73-e2b0662968a9 | -19.81352 | -42.87823 | 2026-06-29 03:55:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5614a079-cb0c-358c-b28b-4e75f49639ac | -17.70712 | -46.77765 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5b7edc1-36d9-3377-9dd9-0163e76ae272 | -19.81424 | -42.87408 | 2026-06-29 03:55:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 736d1067-0c90-3a75-86c7-37df2a54f696 | -17.61447 | -46.69457 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2515a3f-8fde-3bf7-910d-2c4ac4d683ea | -15.11935 | -46.4918 | 2026-06-29 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b028eab-6bdb-36a0-9fab-c1579a18ba5a | -20.0757 | -40.65637 | 2026-06-29 03:55:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 53dc6e28-0425-3f8a-b27d-2020995610c9 | -16.78509 | -48.76284 | 2026-06-29 03:55:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9da9e67-c30a-311f-8054-b1a3cd435f2c | -21.4725 | -41.26668 | 2026-06-29 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f3018686-c4d5-33e3-87c8-ea82a2788851 | -17.70254 | -46.77681 | 2026-06-29 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f80db13-52e0-3e15-846c-7f63f64019fb | -18.80114 | -44.55856 | 2026-06-29 03:55:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ae59de4-f5dd-35f4-87cf-b35c13d5568a | -4.84719 | -42.92809 | 2026-06-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3706cfd1-29e9-3135-bb06-b1a5115a879b | -3.71489 | -47.1674 | 2026-06-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fa2c775-d469-343b-93f8-0a8c25701af4 | -4.3369 | -48.66613 | 2026-06-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
