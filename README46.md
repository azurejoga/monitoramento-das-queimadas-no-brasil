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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30af6a17-02d7-3d98-84cb-b8a55af2b6eb | -11.71307 | -45.39854 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa79e3c-66cc-3871-9390-41dbf76a2c6e | -14.92569 | -46.86249 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d750f0e-97ef-3454-a949-78370c207bb9 | -14.69907 | -45.17657 | 2025-10-06 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bab9b16-38c8-3adc-aafa-74c22c07ba60 | -9.22886 | -51.83722 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4efda517-d8fe-32f8-a3d5-97c88b5b9912 | -11.64463 | -47.74297 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c5d9483-483d-3ced-913a-f20c469049ac | -9.37463 | -45.90912 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bba043e5-0c2f-3c72-92c1-6c56b69335bb | -13.65817 | -47.28665 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37018a88-408a-3a9c-b0e3-9f7e865ba7f9 | -11.84127 | -45.05727 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75641a83-afd8-3b59-ad46-b2bfd8e511c4 | -13.2887 | -48.0883 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36a0bbd3-4a77-3a0e-90e8-dd865bbfb107 | -12.70765 | -45.8496 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 976a6866-d655-36bd-a607-5bc9c2f9caec | -11.0722 | -47.9195 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18350ed1-6d22-3a72-a66d-f65707ff2852 | -10.4818 | -49.08766 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d6607f-c449-3915-9cd8-54688e519744 | -15.36055 | -48.00088 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c2108ce-bc68-33e6-a832-500a02a796a2 | -15.58888 | -52.53317 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1de7e7cc-f29f-3860-a379-6f21334c76de | -9.31783 | -50.42775 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a29571-5e2c-3e17-9037-8e7a26b3fdef | -14.73867 | -54.63852 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd73281a-930c-3439-9e70-dc5043021eb0 | -15.7331 | -48.40541 | 2025-10-06 04:27:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d4e29de-eca7-3fde-8da8-7c400decd190 | -13.24663 | -48.46147 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc3e22a-1e9b-301a-98af-13c970336a5b | -11.57736 | -46.77722 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2f80a38-2e1a-3dd0-bba3-f69551fc4020 | -12.48621 | -45.54831 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cecca09-2a2a-3ac3-ac6b-f39e5037b52e | -13.27358 | -47.17815 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccab1c01-dd93-348a-bc8a-69cc58bd2340 | -11.51096 | -54.45963 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 614b8d93-22b5-3445-8dd9-9ac1b1fb966b | -14.67983 | -48.39425 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e1a240f-c799-33aa-a3f8-54b5fa616e46 | -14.69539 | -48.29514 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 853f7820-86b5-3d4b-a8ed-f8a610aff0bb | -14.61963 | -52.50267 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| aea629f9-db79-3596-aeb4-2a1b5d8795ce | -13.08429 | -47.83089 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53147b16-b3f1-3786-98cd-61d2d27fd198 | -13.26154 | -47.23421 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d62f07d9-4dec-34e0-9432-4d69073fdf35 | -11.46528 | -51.51398 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a3c15db-e2b9-3154-abd6-94c78798b9b6 | -11.5312 | -47.68533 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a86fddd7-45c3-3ed5-9bc9-333c0eb1f40b | -11.80582 | -45.1285 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1cfb709-abd2-394f-9d32-36c1e94627fa | -10.80937 | -48.81988 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df9971a8-69d9-353a-b45c-418c4f5c1de1 | -15.67785 | -46.28213 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e76b3600-d454-3232-89d4-d5ab0f7d05fe | -13.35637 | -47.56876 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 865ac09f-06e8-31fc-8f92-47a97158c287 | -10.62016 | -48.66252 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03ad19d5-2de5-3115-b48f-0eeb4255fc39 | -14.55509 | -46.66509 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d42e08a9-fab9-30a3-a384-2e0d936c09c6 | -11.87583 | -57.8214 | 2025-10-06 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40107682-cf49-36df-9f7e-9dde460f593a | -13.27935 | -47.58109 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 694707ba-d492-3c14-8f2d-232ac3b19ab5 | -9.2356 | -51.82143 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 375cb691-8817-32ad-8f42-c94291cdca9c | -11.44749 | -43.48909 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20dff3ea-ef91-3825-8a0b-18b4bbcb48ec | -9.41828 | -47.89563 | 2025-10-06 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 367d60f2-45e3-3012-b449-d2ecf19ce74e | -15.2202 | -56.82922 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09368457-148c-3aa3-8972-1ef391ff07da | -12.44646 | -45.51162 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 110b0b11-8bf1-389d-83b4-ef22eb1d0650 | -15.37156 | -47.9954 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32ac3b2c-b4c1-3960-81a0-24773e9ad37e | -14.94105 | -47.14127 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8374160-794c-341a-a779-3ce20c1c69d6 | -14.68368 | -48.39125 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b949f36e-64c9-3fbf-bbb2-dabe92687a34 | -14.71015 | -48.35201 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6990b328-fa34-3a5a-8de7-2a3642c1cb28 | -12.25601 | -49.20137 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a9b8e53-b115-3f0a-a448-031d5647d2ce | -15.60233 | -52.54484 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d22c1843-bb9f-3c46-a028-089055ef286b | -11.29525 | -48.23072 | 2025-10-06 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 539672cc-5764-3561-93f8-41bbbe6acfd5 | -14.61035 | -52.51075 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58205d8e-a9e7-3eb5-abc1-00022f2a9e30 | -15.99396 | -50.93017 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 20f79ee0-8c1e-3278-add0-2eab3739af14 | -12.38896 | -51.09476 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4612f8-885f-3e04-88ab-a7e779250184 | -13.26208 | -47.23068 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fddd58d9-74ba-32d4-8b05-7cc571a8b8a9 | -15.74397 | -46.26014 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82f1fbbe-95a9-3d34-8ade-2a32af3b00e4 | -16.63661 | -44.55477 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffe325d1-7cf2-3b69-a453-ed40ef336748 | -11.0043 | -51.15183 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3be4ccc-7529-3f16-a8ab-6899661c50d7 | -13.26752 | -47.19541 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69377470-4e61-309e-9f16-0b3621e2726b | -15.93667 | -48.60387 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f28dce14-f2ce-305a-8845-03a06681c758 | -15.17109 | -45.76881 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ebb2235-352f-31e4-8a89-a5f2f5fd581b | -9.33705 | -54.5264 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec64629f-baa1-3f0b-bf18-ce977a005df3 | -9.96075 | -43.77639 | 2025-10-06 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09229580-2eb2-32b3-be67-0439ed9ba756 | -14.31526 | -45.85466 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04bfc466-42f9-3d8f-ad06-f79a3901f7d2 | -16.02729 | -51.0509 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 456f8467-6ddb-305b-87cc-84dbba76d6d3 | -14.64143 | -48.33707 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 299d5349-e936-3e86-a78d-1f4faab2bb6e | -9.9623 | -48.75297 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acb586a2-3c55-34e8-9136-9559739abdcc | -13.081 | -47.93843 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62080a0b-8c11-3d4b-bdab-876059549e35 | -11.8395 | -45.06921 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f28aeda3-1083-3428-b4b3-b93a7310a5d5 | -14.63181 | -52.54494 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7a3729d-8d09-3292-bcda-06c5be86180f | -10.62322 | -46.34785 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18362090-e66e-3d6a-a6f2-a7395772d60b | -11.54979 | -47.04296 | 2025-10-06 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13ebb50d-77d6-3d47-8838-ce4e1d812119 | -11.51632 | -54.45583 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbba134b-070e-397c-8b0b-fce62c69ed7a | -15.8776 | -46.25656 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc0c0bee-5c0c-38bc-a683-7e5a00786857 | -13.73813 | -48.06452 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 323cc20a-3f06-3c44-9058-e91785b0bfb8 | -13.60365 | -48.69939 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de054026-6dbd-3635-ab57-34fd1a0735cd | -13.38815 | -43.59281 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e2834a3-5cbf-3a00-805f-a579262735d5 | -16.05521 | -51.00222 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1d54b7c-052e-30f7-a44e-5444ed6ee913 | -12.90229 | -47.29243 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32ea473b-2320-331b-ab05-0b3abe5958b8 | -14.56125 | -46.64711 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22f38102-ecb2-3eaf-adae-0a9ff0e0139a | -13.55737 | -47.23414 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1becfef3-ea63-386f-96cb-b50dff3e8990 | -11.49202 | -45.047 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52682326-88dd-3e5e-a3ef-7ae1fd414abf | -10.94094 | -54.26831 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a23862-c805-31e9-8b81-e1664df95758 | -15.99114 | -50.92575 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14123e81-69ab-3272-a6ef-10d805a94595 | -11.00445 | -51.16366 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86709cf6-02e8-3c12-b011-3297b57cc421 | -15.66848 | -47.56671 | 2025-10-06 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470c049e-d1ed-3a9c-bc58-c2a443f58af6 | -9.95892 | -48.75243 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48fcee5f-cadd-3f4c-b1d9-9d3fff4ea625 | -15.53298 | -46.86224 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa7d5a5c-3c82-3932-8e7c-fa367e9668f9 | -14.91222 | -46.83763 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06a04ec2-b09a-3fef-b1a5-02d5f60274f8 | -13.28378 | -47.6179 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acd8e520-a2a6-3089-92ad-6e31e4f97f2e | -10.62555 | -45.00688 | 2025-10-06 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 435960be-4524-36f5-b795-91f8c929d165 | -14.61863 | -48.13369 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 75124a01-06f2-3e75-bb74-93195894b006 | -16.23845 | -49.65828 | 2025-10-06 04:27:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3550505f-139e-3d75-ae69-866dc58f4dd6 | -11.70692 | -45.41738 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9935fd-096d-3478-947a-3de97d103656 | -12.32988 | -45.37552 | 2025-10-06 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18c065ba-bc15-3f60-a899-252af589d61d | -10.58384 | -51.59641 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 244ea534-de89-3874-9a43-4a3231e7ae2a | -15.20716 | -56.81313 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77884154-b9bd-324c-8450-18e47caac20a | -12.48221 | -45.55159 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f0c0273-4f79-3282-94a8-4de5deed2a9b | -12.45127 | -45.54686 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7540a025-f24d-3a40-bba9-370716633c81 | -12.71452 | -46.87745 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2483feae-b062-3db4-8e29-9404bdca52bc | -14.66613 | -48.3738 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ccca030-7569-3fb3-ad2e-d02419ec41da | -15.29072 | -46.31878 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
