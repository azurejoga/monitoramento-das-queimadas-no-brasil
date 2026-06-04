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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b2434cf-c8a3-3a1f-86cf-f6ebc0c0446a | -9.51838 | -50.2625 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95e29cac-772f-35ae-9724-a5271170b7c2 | -9.37028 | -50.54146 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb4b5c07-8fe8-308d-baa0-7831106747e0 | -5.45957 | -37.72206 | 2026-06-04 04:08:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2071e330-1d4c-3f47-8c37-85c67e5ac65c | -9.53266 | -47.75379 | 2026-06-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7aed351-51e4-358b-a73c-949d7e2eec32 | -10.00655 | -46.55533 | 2026-06-04 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21eb8099-ae04-3a82-90df-4b86637ba449 | -8.29516 | -48.23948 | 2026-06-04 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b356d302-ac9a-3e32-8e44-4e00788f6939 | -9.37532 | -50.54237 | 2026-06-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc695e7f-e292-360a-9bd4-6f415feb6e45 | -6.39728 | -44.84165 | 2026-06-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c758d2eb-17fb-303d-bfbc-ffa7c9472584 | -9.46774 | -46.0573 | 2026-06-04 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cce9df4-7797-33bb-b826-1fe4b81ff72d | -9.68464 | -47.04839 | 2026-06-04 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4310b513-eb2e-30b0-99ef-1431614d03b1 | -9.2238 | -46.67657 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b30fe0d7-dcf7-36b0-8bad-2cf07caae5a0 | -8.06671 | -46.20095 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f3dc14a-2a53-34ac-87ca-7ec0b2e5beb8 | -9.53089 | -47.75414 | 2026-06-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f7293c6-e0b4-30ac-80b2-4471b4665eba | -8.0723 | -46.19138 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8283f9-788e-3b88-9c6c-bae02ce91e61 | -10.00493 | -46.56489 | 2026-06-04 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ed427e0-4252-3344-9e62-e4e64eaa5be3 | -9.92314 | -48.00545 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 391d7d34-1ccf-3863-915d-304bfad0b160 | -9.93292 | -48.00236 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 956f77ac-7319-315f-a7c6-8d1cf2b113db | -8.57941 | -45.99862 | 2026-06-04 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61241ede-40ac-30de-858e-698ac8f99fdf | -8.07313 | -46.18647 | 2026-06-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476ee2e7-1a54-3f93-8da5-5a8d8f7ebf49 | -9.89622 | -47.86053 | 2026-06-04 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32015c39-ef47-390c-81f1-016dd1de67d5 | -11.5499 | -52.7867 | 2026-06-04 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 04ea2da5-3c06-3481-b5db-cb9dc67bca3e | -12.2138 | -57.2688 | 2026-06-04 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 81bb38b0-99b4-3ba5-beb8-60c87fc45d96 | -12.2136 | -57.2888 | 2026-06-04 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.0 |
| f7384d3a-ef92-3eff-8cd6-27f1109e1a4a | -12.2327 | -57.2672 | 2026-06-04 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 45fed612-b242-363d-bc38-a5e1289fdb14 | -12.2325 | -57.2872 | 2026-06-04 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 0fcc91a4-7460-3131-9103-1d13f1da2b41 | -10.3839 | -49.4554 | 2026-06-04 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 23c5333d-5fc7-39d7-b0ea-0ad0e647cdb5 | -10.6148 | -46.70596 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e231b7d-ba1e-337e-9327-9d5b4fe9a611 | -12.02584 | -45.87054 | 2026-06-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72a11e9f-4775-3b90-9b21-0604c8458048 | -15.33334 | -42.33643 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e303fdd9-5f98-391e-95eb-89a708283459 | -14.7853 | -50.63969 | 2026-06-04 04:10:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa811152-abd8-3e9b-81aa-742cdbb803c0 | -10.61314 | -46.71561 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1504454a-b762-3608-8e42-2ba8b8418d9e | -11.55047 | -52.78799 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ee5d034e-2f91-36e7-b6ae-0b861ab3d0d7 | -17.63684 | -45.16385 | 2026-06-04 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e137fe1-d035-31b2-8639-d0ac6163887a | -15.33722 | -42.33335 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 365e50c7-66cd-3776-8e15-1cac8f23b4cd | -15.43601 | -46.33339 | 2026-06-04 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fed307a-7340-307d-8912-16c82e8165c7 | -10.55231 | -46.6174 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 45001a23-dd2e-3638-8217-b18ca09d1ce4 | -14.08568 | -53.38962 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 033851e8-ee19-3d80-80bd-2bb1dacd89f5 | -11.7959 | -42.63811 | 2026-06-04 04:10:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9fb17918-192b-3547-ab3d-413e3f168962 | -14.29448 | -49.14433 | 2026-06-04 04:10:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 539118be-1568-384f-b141-90d509bc2f36 | -12.17862 | -54.54139 | 2026-06-04 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51602193-5c1d-31eb-995a-d38a3fd0bd0d | -14.29376 | -49.14835 | 2026-06-04 04:10:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d3b0072-6f45-3dc1-80dc-b1f31168a3cc | -11.55343 | -52.78487 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 48bc5f0d-7de1-3842-9fc4-cc7e020a86a0 | -14.07533 | -53.38348 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9960ae7-456b-3e81-8ad6-7d49b9a654e0 | -14.06666 | -53.39774 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcb64613-a48a-3b51-9043-a2009b126a44 | -15.33668 | -42.33697 | 2026-06-04 04:10:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c35b7644-0877-3653-a309-ccdc24b80b49 | -10.84423 | -53.75029 | 2026-06-04 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4b94f96-8d32-3ee1-baa1-8a45b9af07cc | -11.54146 | -52.78668 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68128890-326e-316c-92a5-3d0738e481a7 | -12.56198 | -48.3501 | 2026-06-04 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86357532-535a-3eb5-9b4e-e323e08488ad | -12.73863 | -54.19366 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9914e36f-170f-3bd6-93e5-1c22a33808e9 | -11.54635 | -52.79156 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 59010ecf-d117-3c62-a997-21f806b848ed | -11.26416 | -53.97019 | 2026-06-04 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c6988c7-690b-30e4-91e2-5ef9e4691d3e | -14.77159 | -52.67251 | 2026-06-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3e56145-e7d3-3dee-8509-14b96df3c4ce | -10.56592 | -46.62983 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4871681c-f8f3-3b9d-b0ac-50110590bf50 | -16.74465 | -49.93614 | 2026-06-04 04:10:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5470a441-5811-3d10-93b9-e3c24e4109cc | -11.78695 | -52.51303 | 2026-06-04 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d90145b-9880-3147-b583-2da1cf1cfd6c | -10.38916 | -49.44219 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5871a330-e97b-3b18-b8f5-386a227e6e6e | -14.44604 | -48.90376 | 2026-06-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a249de3-1976-3c4d-819d-85fb8f75e96d | -11.27024 | -53.97128 | 2026-06-04 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 611dc8e1-3a03-3d03-84c3-0471a39d0a52 | -11.94981 | -46.75092 | 2026-06-04 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caa67fcd-dd01-3fef-81d9-1c64ed929edb | -11.62701 | -55.18951 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 674e8896-9f2c-334d-8d68-742ae4537a55 | -11.762 | -47.07412 | 2026-06-04 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf7d62f-40b1-3272-9290-d4669caf1cba | -11.2589 | -48.35865 | 2026-06-04 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07ad8b35-13dd-34da-bf63-bcd28f7340f0 | -12.02425 | -45.86959 | 2026-06-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e562fc3-4920-337b-b65d-6c6623b57cbb | -11.62725 | -55.18779 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8dee9b8b-957b-3a48-9db9-95ec9072488e | -16.5861 | -45.88562 | 2026-06-04 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfc1f750-fa57-38cb-889a-5dd076ad98cc | -11.39409 | -47.81792 | 2026-06-04 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e008dac-dd3f-3ef7-8ac0-662881cc97f8 | -11.55123 | -52.78412 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7af4bdf0-c1a6-3983-a7d2-180ca1e8d924 | -10.84939 | -53.75591 | 2026-06-04 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d98b040d-6511-3b88-a4bc-7d4b73bfdd91 | -10.39376 | -49.44302 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8784f3c-d165-38b3-805f-b28a313c5978 | -11.54709 | -52.78764 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 731b0c53-5fba-3850-96be-c2d51c69979c | -10.54853 | -46.61658 | 2026-06-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c4085191-8af8-3472-9cc9-ccc0e2cfa683 | -11.63373 | -55.18912 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 392a8c74-a206-34ce-abaa-2aaddac92999 | -12.02653 | -45.86633 | 2026-06-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf2c2523-cf47-3edf-9160-f77c2239e899 | -11.54408 | -52.79086 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 65e44675-4803-3000-9832-916fe7901c86 | -14.44537 | -48.90759 | 2026-06-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7a8bbea-7a49-3bec-8e3c-b4d324d781d2 | -11.63487 | -55.18355 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| beac7452-75b9-3adb-8ecb-daf9aacf9faa | -14.04538 | -46.34269 | 2026-06-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f720112-0900-3025-a1bd-8c5cd410d920 | -11.5497 | -52.79188 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9918b6b8-fe77-370f-a666-e8efbb6abf5b | -12.53758 | -43.80157 | 2026-06-04 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2562d1be-57c0-3cf9-8608-8fc729b375c5 | -14.04969 | -46.33909 | 2026-06-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 606e1107-ca58-3a28-b529-2ea51bfbf69b | -14.04609 | -46.33849 | 2026-06-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb33525f-3dcd-3fd3-b255-73ae81881838 | -13.51513 | -54.31316 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9316816a-73d9-3e6c-9c0f-4aafce9e53fd | -14.78988 | -50.64065 | 2026-06-04 04:10:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84730166-e76c-3185-9792-834a4ecc3d58 | -14.44804 | -48.90462 | 2026-06-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72d9de6d-11a5-3ab4-a49a-718364de0b13 | -10.6397 | -49.72896 | 2026-06-04 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c88b761-7a93-37a6-991b-1fa823b4c431 | -14.29493 | -49.14351 | 2026-06-04 04:10:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a2d758f-2fd6-361a-b84a-fa5b9d059568 | -10.38456 | -49.44142 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fafc8fe6-539e-3287-b784-4a2331badd94 | -17.50171 | -46.44253 | 2026-06-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaad63d3-bd8c-3b1e-9670-98393a4f4d99 | -14.07934 | -53.39233 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 10c2219f-e055-3248-b81b-6f8c03ff0899 | -12.73771 | -54.19822 | 2026-06-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ba41e97-3cfe-3a88-828a-171afcb1f909 | -14.29419 | -49.14752 | 2026-06-04 04:10:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85edbdd9-a17d-3278-b270-a9b0b4cabba3 | -11.95496 | -49.54379 | 2026-06-04 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25117014-c8d3-314f-bf8e-5204fb54a519 | -13.05165 | -44.18618 | 2026-06-04 04:10:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16b6dc59-16a9-328c-9ce4-108aa6c0aafb | -10.99092 | -47.05332 | 2026-06-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e536b8-ead5-3ea7-a35d-09a14e49f30c | -10.3883 | -49.44703 | 2026-06-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b394b53c-5f13-3f36-95de-62f3a1e6ff38 | -11.54485 | -52.78694 | 2026-06-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 96c79bc7-2292-3344-b770-fabfd3d3c989 | -11.6284 | -55.18219 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 79be722c-7dc6-3666-8bb1-57c09de1f600 | -14.04896 | -46.34332 | 2026-06-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11d7a9dd-d4cb-3242-b2b0-c1023be07fd1 | -11.62078 | -55.18644 | 2026-06-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec0f1f44-7c80-31e1-8966-7df9923e25d1 | -11.25959 | -48.35466 | 2026-06-04 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
