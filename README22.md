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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50dba669-b1ca-3d57-8c01-1a0be2f79218 | -9.17583 | -58.06578 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6177d63-6a9b-31e4-a4a8-d097242cbcfe | -9.20387 | -58.04896 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21f44181-2ef0-34ca-b097-a1ae30b04407 | -10.12735 | -52.09311 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d9233ea-d21f-324d-bdac-7aa30d077263 | -12.52137 | -48.28372 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1d8584f-bf30-3eb2-9ded-c7e26ad5739c | -4.35097 | -47.76299 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02ba0560-8f10-34e6-a490-459cef33e023 | -4.35011 | -47.76865 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca1638c2-6723-3079-8ea1-0b39d497bfb1 | -3.25391 | -50.81994 | 2026-07-02 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d94baa-4291-325b-a1d6-0e3018e21055 | -12.51368 | -48.28958 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2559c8df-3ce4-3466-a37f-ad05d3f66b27 | -4.01111 | -48.05808 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6abdf30c-ea23-3fe7-a7fb-b34dc3865370 | -10.12204 | -52.09232 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f27bd922-7481-38b9-82ec-113a619bdb52 | -11.36287 | -55.43215 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98642519-a132-3739-a4cf-ec4c3a42fdee | -10.12779 | -52.08973 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f01c24f-612a-366f-9c00-e91c5efff427 | -11.3591 | -55.42741 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2455def-bb5e-301d-a323-de19efd43061 | -10.12692 | -52.09648 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5578c92-b055-336c-8758-454462daf332 | -11.35855 | -55.43155 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4129ae61-9161-3e86-a215-37775c00ef51 | -4.35017 | -47.76857 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1c51fd2-7386-3bc7-a0ef-dd1aa1b45ba3 | -11.41609 | -56.06337 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f45883b6-d32a-3ed8-9536-f192b83e89e4 | -9.18897 | -58.0509 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 099b4dc7-ad0f-31b5-b85c-8f79f65f0da0 | -12.50746 | -48.28194 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c41abb4-7000-3a71-a12c-de7683082025 | -11.36774 | -55.42858 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abbb6002-74df-3d5a-819a-05aaad19b9e8 | -11.85252 | -48.24792 | 2026-07-02 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b250ff24-44ec-3ad6-9f38-2eafb512427d | -10.13181 | -52.10061 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f118238c-a1cb-37e0-8d77-1278e72c3ad5 | -11.42022 | -56.06402 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1547ba0-6c50-3277-b118-f31f2e78564f | -4.00482 | -48.05667 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c2f943a4-d532-37e5-96e5-957891ab6706 | -9.19254 | -58.05146 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0163f67-ee3c-324d-9eb9-3a81c9a90fb2 | -9.2003 | -58.04842 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f30a18cd-2d36-3fc8-b2b3-c6cd8123be74 | -11.4443 | -55.91862 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad4290e0-eeca-330a-b3e2-e846f943de0e | -11.42953 | -56.05774 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5c73c56-9e03-3385-a720-f09bec6f6975 | -4.00415 | -48.06144 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68db83dd-aab3-3132-a37f-cee8c73fa091 | -12.51441 | -48.28291 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 430f12fe-669d-3e52-ac83-bd14da026775 | -11.36397 | -55.42385 | 2026-07-02 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42215008-d45a-31f2-99fb-fbc4bce638be | -5.12501 | -49.33019 | 2026-07-02 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9f9d9d9-e64a-3639-831a-8c6c921c8d50 | -11.04834 | -56.93073 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db34d041-63d3-3585-85bb-2ff164943135 | -10.12649 | -52.09983 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be840fd7-d5a3-3e09-a982-c62d9bd3ae0d | -8.65638 | -49.71579 | 2026-07-02 05:23:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9211a03d-7ea9-3fc4-ba4a-729f87c889ef | -11.85322 | -48.24152 | 2026-07-02 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| be1a667d-abec-3ed6-95ee-23f65dbbfafb | -4.94858 | -48.24363 | 2026-07-02 05:23:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 783aab23-f96b-350a-868a-bcd2f4da6280 | -11.41971 | -56.06778 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a42d0658-d398-3d25-9124-eb4676d5523c | -12.52761 | -48.29123 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 609e1d0f-94b1-3720-a74f-a660e740b7c0 | -12.52697 | -48.28931 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3efa733f-2e1f-3696-8c58-b6a928b2f502 | -9.0238 | -59.53664 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 860a48c1-ed11-3db3-956e-f3b41bae0c3d | -9.20091 | -58.04428 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0380f19a-4b4b-3629-aff2-66331948b6cb | -12.51305 | -48.28756 | 2026-07-02 05:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 20ce05fb-41fe-385c-91ba-816f480a02ff | -11.44377 | -55.92249 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 843b6816-773a-36ed-8aba-471bd7d76803 | -4.01041 | -48.06309 | 2026-07-02 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 67af8fa6-c2cb-35fb-b5f0-2c823867ec75 | -10.82099 | -58.01857 | 2026-07-02 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8266a10c-962f-3f88-b526-5996e9cae82f | -9.1854 | -58.05036 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ee9496-2894-3ff7-ab83-4f3f57fdccd3 | -10.13138 | -52.10396 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9d298c5-75a2-3c09-a8bb-1b46942d784b | -9.19193 | -58.0556 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a533300-2701-3f1e-8e79-12ce49a7f3bc | -8.87763 | -50.1849 | 2026-07-02 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616b6440-b9eb-36c9-beed-0e43d5b00eea | -11.4316 | -56.07335 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a1e5d1c-6925-35d1-b127-cedb82a9da3b | -9.02717 | -59.53716 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96bff4a6-223d-3047-af22-9c97130a57a1 | -10.66776 | -54.51936 | 2026-07-02 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eaed7cf-997d-3ebf-9df8-b26fe2269bd8 | -3.51459 | -48.03464 | 2026-07-02 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e3004a9f-de0f-31cf-ab48-75accb53121c | -11.42385 | -56.0684 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc5b826c-0a2a-3792-bfdf-4bede83d722d | -11.42177 | -56.05268 | 2026-07-02 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63382ab2-5f63-395b-9115-d2b74599877f | -9.60027 | -56.92756 | 2026-07-02 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77bab8f-d0b6-33cc-b84a-0dca84783d30 | -9.17644 | -58.06166 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f9cd4b5-6272-334d-8759-01a01942c8a7 | -10.12247 | -52.08893 | 2026-07-02 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92bf5ae-af24-392b-a530-80ec69f5b9a1 | -9.02326 | -59.54027 | 2026-07-02 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1995246-101f-3a5b-aeb7-bc83c89bc369 | -10.08143 | -60.49592 | 2026-07-02 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79fa45fb-400a-3724-8343-407e77f4578b | -8.87707 | -50.1893 | 2026-07-02 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d99f4b01-16b5-38f7-8268-f30cd46543ac | -3.50757 | -48.03856 | 2026-07-02 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71673393-0b85-3a44-be7e-3ad6f5d88840 | -10.69623 | -49.6088 | 2026-07-02 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8172a50b-fe8b-3c86-8700-a1f03701104b | -9.75452 | -47.88114 | 2026-07-02 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ce7f5e1-f12b-3ef9-8066-d5f427269174 | -9.26165 | -57.85778 | 2026-07-02 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b3a68c1-47cc-359d-8ec4-deeb87518463 | -8.65695 | -49.7112 | 2026-07-02 05:23:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70898b8f-b604-3240-82d5-b440f314e899 | -19.50959 | -52.73886 | 2026-07-02 05:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c615394-44b5-3f4b-a7cb-53ae5314b63d | -8.71273 | -48.33942 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b67e357a-4029-3df9-829b-eeb6ef32693a | -8.49554 | -47.19822 | 2026-07-02 05:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 40ff030d-b3e0-3f9c-acb0-14a173721759 | -11.61287 | -60.41463 | 2026-07-02 05:25:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 44645600-f509-3137-8ae2-05a3fd475dec | -14.1754 | -52.87795 | 2026-07-02 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58820504-d27c-33af-ae73-c96df68745bb | -14.15859 | -52.88276 | 2026-07-02 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b71f901d-67dd-3f11-b3eb-0f2b75f15dba | -14.159 | -52.87918 | 2026-07-02 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94683c42-cf12-3a46-838e-ad0a2620cbc5 | -19.50463 | -52.72989 | 2026-07-02 05:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 003670c8-f5ff-383b-887a-23a32a80f99e | -11.80666 | -57.00734 | 2026-07-02 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ffeb6eda-ad02-3d50-aefe-31c3d32ec13c | -11.63688 | -59.0219 | 2026-07-02 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cc94c7b-ae4d-342c-b4a6-e88014d1d233 | -11.9098 | -57.38255 | 2026-07-02 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e879213-abd8-352a-a37d-c1a0ee93a903 | -11.62694 | -59.01636 | 2026-07-02 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 994bc960-f27c-30f2-a9a0-8cca94fccfa1 | -13.65325 | -60.62498 | 2026-07-02 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d7494d2-0b22-34bf-8851-6b74fa566a1c | -11.79628 | -56.99554 | 2026-07-02 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b023af29-d709-325a-a358-f49f4f2d3d36 | -11.7956 | -57.00056 | 2026-07-02 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 57680dd4-61a4-32d1-b7ae-97ba0992ef1a | -12.54371 | -57.17896 | 2026-07-02 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae15bae-9506-3130-a920-6736ff000d89 | -11.62987 | -59.02085 | 2026-07-02 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3b97718-2ef4-33ea-83d5-d054e1463915 | -8.65522 | -49.71758 | 2026-07-02 05:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 299a4ee9-042b-38f6-8a28-5cac91c997df | -8.50263 | -47.19904 | 2026-07-02 05:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e8578516-7b0d-339e-b6bc-280e17003849 | -6.42686 | -55.79853 | 2026-07-02 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 929f98b2-1679-3597-a822-87f666a6866f | -11.63453 | -59.01346 | 2026-07-02 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b97274d5-0dca-3c44-ab35-1f8437114416 | -12.15279 | -57.22259 | 2026-07-02 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1cd1da5-282e-3ee9-a6cc-e181cf4924a1 | -8.71631 | -48.34513 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 293817b2-7fdd-3961-9b29-77af895be858 | -11.63044 | -59.01688 | 2026-07-02 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e31e6943-1118-32b0-9cf1-db94c44ca6c3 | -8.71705 | -48.33893 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d7d77307-7881-364f-ad29-64e0202764b6 | -12.14821 | -57.22695 | 2026-07-02 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd48d3db-4cdb-33da-be79-c76322df694d | -16.36015 | -56.66151 | 2026-07-02 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e8ffee99-f975-30db-a9e6-eac298eaf82c | -7.9118 | -48.24593 | 2026-07-02 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6de21c5-3b81-3c4f-831e-61a5dd3505d6 | -12.21986 | -56.56459 | 2026-07-02 05:25:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c3ee44-9d92-36fc-8c9f-8604a0e4e222 | -8.71939 | -48.34019 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05749606-fc93-3cdb-bc87-54bacb1edd84 | -19.50422 | -52.73415 | 2026-07-02 05:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 134b4249-1f3c-32c5-b696-0b32cb810f8d | -8.7186 | -48.34639 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7fe4b39f-5986-32e9-84c0-86b40bdab626 | -8.65581 | -49.71301 | 2026-07-02 05:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README23.md)
