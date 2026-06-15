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
| beb2daaf-e2c3-3717-964d-b3ffc75c4f6b | -10.1599 | -56.60026 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41b9333d-5acc-326d-8e19-36a381a1a490 | -10.54226 | -53.72498 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fc1224e-354d-37e5-bfe1-5e04e87d772c | -10.7742 | -54.10331 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9db265e-6b50-37bb-8a96-c3d3ed84dfdf | -10.1592 | -56.60444 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dbe6039-0e4f-3a73-8adf-2b11227edda6 | -10.28919 | -47.59772 | 2026-06-15 04:55:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5489512-a248-34cf-b105-b505aad56397 | -6.15981 | -48.48508 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3c6e1e8-a70d-3062-a293-afd0d85606f2 | -6.11918 | -48.50159 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3b01e5-66b5-3920-a1ff-54fac590a650 | -11.71789 | -54.49287 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef91847-9c05-308e-8ff8-1dd524232e3a | -10.83927 | -53.73688 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d7ca99b-3eb6-3312-a11d-9aa69707c627 | -11.51229 | -56.12332 | 2026-06-15 04:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12eef0b0-c9b4-34eb-a77f-cfe4ce83f796 | -8.43219 | -54.72463 | 2026-06-15 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 299df944-2075-3f58-bdbf-aeec2e59a260 | -8.88797 | -48.50561 | 2026-06-15 04:55:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1209fd57-50e9-3e6b-89ab-3898a007d15c | -10.53951 | -53.72095 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ad2416c-145d-35be-8dc7-c6eadf73e314 | -11.02408 | -44.69197 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55980c9f-2179-3f46-96b0-475154ed2958 | -13.54465 | -47.85067 | 2026-06-15 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5795a352-14ed-3b8c-9360-d21fc5fd226c | -10.15204 | -56.60317 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 249c8446-bb9c-3761-85a3-4866ecab1a33 | -9.27044 | -50.66118 | 2026-06-15 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9658f96d-29fa-3ebd-bb5f-3bee810223db | -8.22111 | -55.09743 | 2026-06-15 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e85e871-f04f-38e2-8d08-7c9bfcf4272f | -13.81003 | -43.65202 | 2026-06-15 04:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fd66b70-39cf-3511-9bd6-600578055de4 | -10.80388 | -54.17301 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd40850-9deb-3b14-8059-73dbe9e03449 | -8.43408 | -51.54903 | 2026-06-15 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f355ee89-2080-34e0-83d5-932905f3933a | -11.34525 | -51.3994 | 2026-06-15 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c71fe31c-4861-3444-93f1-37b724379748 | -8.06773 | -47.18346 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c041611f-cad2-3218-ac47-6d45e12dea5e | -8.19365 | -46.75502 | 2026-06-15 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f768fc3-0149-38a6-8a47-f5e0265aaed0 | -7.91966 | -48.25238 | 2026-06-15 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b20400ec-065b-3da9-8db6-e2cbd9d55abb | -7.91571 | -48.25176 | 2026-06-15 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d38a266-8a0c-342f-9436-065515db8a5e | -10.90228 | -54.13175 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65240f5e-da53-35ad-a239-58793aa72e74 | -11.82546 | -51.62062 | 2026-06-15 04:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea65f4e-3465-31cb-908c-34a80701c1cc | -6.1626 | -48.46621 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24863bc9-e989-32a8-8db1-c4b104fb391b | -11.26635 | -53.95693 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c87c78-608a-3c96-be4e-a42bad8ffb28 | -11.02449 | -44.68869 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8043e2b7-093a-3d2a-804a-ee2f18e78c5e | -10.15632 | -56.59963 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2b0ebe6-3f14-3296-8251-c934bda40f01 | -11.02891 | -44.69605 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72200090-ddc3-3b96-b94b-062ebafe696a | -6.16601 | -48.49577 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd3dbdaa-94da-3f4c-ab61-7cbd568843af | -10.83707 | -53.72935 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37b47adf-555f-379a-aa62-8f9b8a488fe6 | -12.73511 | -46.29134 | 2026-06-15 04:55:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74e2cfc0-fdeb-3a16-842e-ea60cb322df2 | -7.91709 | -48.25015 | 2026-06-15 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72be3975-6991-3a4b-bb6a-a83a349d9911 | -10.55413 | -56.34462 | 2026-06-15 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69dfdeb2-a73b-34b6-8140-a7f31d060607 | -10.83045 | -53.72828 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b64ff6b-86d2-32b7-8519-88f72e037a20 | -9.26692 | -50.66063 | 2026-06-15 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4c98d4b-da38-31f4-9e67-797ffe82aad3 | -12.71833 | -54.20568 | 2026-06-15 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6e7732a-b880-30f4-950b-2025d815749b | -11.71902 | -54.48579 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31b9d64-968a-3b20-9f0d-64ee16efac1e | -8.09973 | -46.06748 | 2026-06-15 04:55:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178f736a-b639-3f43-82d1-fb626acb152b | -10.90503 | -54.1358 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 480447cb-b04b-3104-a0d0-6f1f524561f6 | -10.80057 | -54.17247 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96798fbb-61e4-3d6f-8af1-779b6135f4e9 | -11.26854 | -53.96447 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72648b53-851a-31bf-b24e-02c76dde46fd | -6.15744 | -48.47479 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10e7a34d-95d9-3e46-86cf-5cf9cf88c3c8 | -8.43746 | -51.54956 | 2026-06-15 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c915b7ae-1f64-327c-ac9a-0dbb088393df | -6.72579 | -44.37597 | 2026-06-15 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6cd0799-d855-368e-a6cb-576cfa669eab | -8.43259 | -54.72808 | 2026-06-15 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fe0664a-e7ec-32e4-96b7-79ab80df1c02 | -11.34333 | -51.39819 | 2026-06-15 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d1c894-8afe-39cc-8ba8-da23ca728f84 | -8.08106 | -47.08211 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa5d9655-c41f-378a-81b6-fd93b2ac8a4a | -8.38861 | -47.47131 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6315936-2f83-3528-ace3-871e373b2940 | -10.83265 | -53.73581 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f316be0-f0fb-3d0a-9605-2e51a2407c44 | -11.73078 | -49.04465 | 2026-06-15 04:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3fc53eb-b321-33c8-94f4-d934cef2a54d | -10.83596 | -53.73634 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd87e99-73d8-32d4-9f9b-55a38f8d9773 | -6.7254 | -44.37873 | 2026-06-15 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7093b5e-ca86-308a-a549-1f47cc7bbb6e | -10.53345 | -53.71638 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95569fb8-05c4-3741-8a37-03ee2224f935 | -10.84258 | -53.73742 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d43bb2-6356-3a4f-8812-c12ca2e1fb64 | -11.31403 | -54.46635 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58aa47d8-2cb5-33ef-8717-98654140cd7b | -7.32431 | -48.87059 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60713ce-70bb-3c78-a713-73480b96a13d | -10.77364 | -54.10682 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 610aa5ee-1b79-3f27-9c6e-89521f825456 | -8.18927 | -46.75437 | 2026-06-15 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15f9c6c1-de4d-3711-9246-98821e79c916 | -6.15812 | -48.47012 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de0f840d-4923-3751-b4ee-e7b0e5c290a7 | -11.26579 | -53.96043 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b49077a-8b0b-3fe7-91fb-e0e7947ca5b6 | -8.83499 | -49.53135 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96efbf80-26f4-3f34-bc63-2ecb57bb07a2 | -12.73031 | -46.29032 | 2026-06-15 04:55:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4c34ae7-1ea0-3190-a49b-3827678488ae | -11.26966 | -53.95746 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8974cb-15bd-35ad-8ed1-db41c65dc331 | -8.43319 | -54.72443 | 2026-06-15 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58eeafcc-ffff-3538-8952-302c409f7e70 | -6.16978 | -48.4966 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32efc8e6-f633-394a-9d65-2b458b2c1168 | -8.38426 | -46.49538 | 2026-06-15 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f310dcf-07df-32cf-ae73-ce227a37edde | -11.02933 | -44.69277 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8bdf590-d2fb-3ba0-bbdb-01e604a1134e | -8.6852 | -47.83635 | 2026-06-15 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b411f03a-475d-3845-bf6d-c042787fed8e | -12.71558 | -54.20161 | 2026-06-15 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f09825-4ae1-3e82-be80-401cad3c4d5a | -8.19742 | -46.75995 | 2026-06-15 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa9d8f8c-daa0-3fa1-af4b-9f1d68590d53 | -10.8321 | -53.7393 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bad539b0-d852-37f4-8319-89a2d167576a | -10.80715 | -54.17382 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0001b1e-3761-3a3a-8613-d764b94b3311 | -7.31916 | -48.87926 | 2026-06-15 04:55:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14ae6197-6264-359e-8d1b-45b4d4443c46 | -6.1629 | -48.49055 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a30fa0-c572-3f5e-a0fe-8825d7d1bb70 | -10.534 | -53.71288 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12450e1c-89f7-3f13-9eb3-52959824bf9c | -8.96623 | -46.9101 | 2026-06-15 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5e1d57b-3659-3736-bb58-58fae8f4b0ee | -8.88403 | -48.50501 | 2026-06-15 04:55:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d96d1d40-3827-395d-a642-7fd33c197a12 | -10.57277 | -57.31451 | 2026-06-15 04:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c4b8f65-cdee-32b3-8edb-f1be57796821 | -8.06829 | -47.1797 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f0c7f9f-f210-367a-abe4-50f982661205 | -11.71845 | -54.48933 | 2026-06-15 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13dfef16-1e84-3720-ad0b-3c8c7b450bec | -11.02975 | -44.68948 | 2026-06-15 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3a47eabf-4455-39e6-a6e0-6bce55dc6c6b | -10.80659 | -54.17733 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc23c1b6-2421-34d9-b049-768f9d0e3ccc | -10.83763 | -53.72585 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d7f0522-2990-3a24-bfcb-1bded80fced9 | -6.15912 | -48.48979 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46e5e2df-5d91-3e1f-9b8c-151b7dbbc53f | -8.19304 | -46.75928 | 2026-06-15 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec6be4b5-90b3-34ea-b82a-42be5fd48cda | -11.06449 | -52.45125 | 2026-06-15 04:55:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbc80f9e-5ca4-39ae-91c3-7a6062fc7eef | -6.11754 | -48.48682 | 2026-06-15 04:55:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a4a171-ce99-387e-991c-01f9e5656f74 | -11.78693 | -54.01688 | 2026-06-15 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c70fc63-2957-362c-baac-801c90bed84a | -13.50958 | -47.84476 | 2026-06-15 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 538d0846-5160-3b6d-a800-8dff11b3f599 | -8.07131 | -47.18298 | 2026-06-15 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff65600-e02b-3a79-b9a8-9912b49f529c | -10.83376 | -53.72881 | 2026-06-15 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4d66756-5810-3509-ab92-2867922c6a3c | -13.50896 | -47.84941 | 2026-06-15 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7bcdde7-132c-3e28-bb45-7fe0e0295cff | -8.4316 | -54.72828 | 2026-06-15 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ed84abee-dea9-3c60-a024-310802dbc212 | -8.98436 | -48.09438 | 2026-06-15 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaed2bc1-54d8-35d7-8ebb-4cf937c88778 | -11.51164 | -56.12719 | 2026-06-15 04:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
