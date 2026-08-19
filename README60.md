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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3832a2b-f1d4-3c01-bd89-bfe81330b8e6 | -6.08983 | -57.91264 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 65989ef3-f32a-397e-baae-575ce1d19864 | -6.35657 | -54.90583 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6562c49c-f6b5-3cd7-8376-883f8ab54dff | -6.0166 | -57.8459 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db1a36f9-2139-3a95-9a78-a773c871a67e | -6.10522 | -57.85818 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79724161-42ff-3e30-b458-d2562e640004 | -5.50015 | -60.12824 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 233cc96e-61ef-3652-8588-d906941a7835 | -6.09101 | -57.90475 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74b13238-c0e0-3f0d-8787-a9390aec8a82 | -6.09042 | -57.9087 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4177bf8-b9b3-38e0-8242-f16a69e91cca | -6.00661 | -57.84028 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49a8738e-82aa-341e-af70-baebdcf40e49 | -14.21265 | -52.91399 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 049dcfe8-183e-352f-ac89-063ca230254f | -11.21166 | -54.00552 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84909a61-955c-3ddb-b1b8-04c3ebf20ad4 | -11.22129 | -54.00691 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b9e2a42-e8ae-32db-9e73-5503e5e52506 | -6.02337 | -50.20247 | 2026-08-19 05:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dbb8cef0-fcc4-3712-a7a2-d9ca34969193 | -12.74839 | -59.75546 | 2026-08-19 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79839dc1-f437-3d1a-a803-4533b60ed5b8 | -6.08924 | -57.9166 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7ec4ce6e-2e87-3661-b0c8-e1be26a74117 | -11.92181 | -55.91584 | 2026-08-19 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5998016-c8e6-35fa-a0e9-1e3adc3e0e12 | -14.15363 | -52.92841 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e405eae-238a-3bec-9b93-f300685b78dc | -4.46366 | -55.45626 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7ccfbe9-caf1-3f7f-8d73-20f16a0f760d | -6.27214 | -55.97125 | 2026-08-19 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4516ce1-6f64-31a2-8c68-ecbbbfc11b4a | -15.78274 | -55.5582 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9199dce-a698-3642-951e-8951c859c972 | -6.00774 | -57.85674 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d24875e7-e903-3600-8ec9-8df929da4462 | -6.02374 | -57.82261 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff48ce3-96e3-3d58-a0f8-c2ee3b93d9fc | -6.34928 | -54.89666 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6963b85-244c-3a5e-b363-9f3983199f56 | -11.6373 | -54.52902 | 2026-08-19 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11ba0657-2264-3731-9649-c77ad1138f8a | -6.12452 | -57.70522 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80e35203-4a50-3aaa-b5a8-0c803aff2fbd | -9.5493 | -63.5254 | 2026-08-19 05:25:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7078bc54-6416-319c-968b-46c9cb0c2f29 | -16.26123 | -57.67312 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f6155cdb-a31c-3163-a0cb-c13edd1a0458 | -11.22258 | -55.06572 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1c75859-456a-3ce2-aef9-59e192156331 | -11.69948 | -54.56325 | 2026-08-19 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ed3f6ba-9bcf-3b59-8c91-18ba979481f0 | -6.10344 | -57.87003 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dfb8529-9f7a-380d-a037-dcade33d0f23 | -6.12626 | -57.71792 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efe8f2c5-843b-3960-9b3a-38cab3e36813 | -11.32221 | -55.23199 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbee043b-9ca7-3e75-83fe-7e6be17b5d2e | -6.10077 | -57.71815 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd7761e7-eaf3-3fe4-9094-a698ab7ccaa0 | -6.44958 | -52.72607 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b27d58f3-a05f-3c86-b78b-4b4d48a68093 | -6.00248 | -57.84376 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2aaad2d-85b6-3901-b3fc-8d303724cb62 | -6.27606 | -55.97191 | 2026-08-19 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa72bd72-c136-3cab-9f36-2844f1343788 | -13.47267 | -51.789 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a5efc54-1b98-347c-8d95-036ac1fabc38 | -12.12874 | -57.20707 | 2026-08-19 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ef73cbe-8732-31fc-aaac-32dfb3447a2d | -4.78762 | -62.92047 | 2026-08-19 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4707dde8-87a6-366b-845c-8921540cff57 | -14.15493 | -52.93974 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a5a5a333-6594-3707-af80-755ebfafca3e | -14.15318 | -52.93215 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae521b66-8d85-3cf7-af3a-71312c361689 | -5.91928 | -49.26292 | 2026-08-19 05:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3c434b7f-4ab4-3b9c-a037-22d199f9152a | -11.22921 | -55.08501 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 150405f9-45db-3db7-8443-83b72f7796e5 | -6.14286 | -57.872 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93bd4c59-1ffc-3318-8935-5b86df0c2087 | -10.94024 | -57.17878 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42ddb7f2-a641-3326-9ced-7da3edaa914e | -15.78174 | -55.56015 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22a2ebe0-b8d6-30c5-b602-679ce59638a1 | -5.49684 | -60.12773 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3259b5d9-b844-3021-aa0d-236bb40e60dd | -15.28206 | -56.49855 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee002efb-8da1-3894-9a4c-3891acb156e1 | -6.40651 | -54.95113 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44bc3cbc-bec4-31b9-a9e8-e57b86b7c586 | -6.00008 | -57.85966 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 934d86ad-6324-3810-9dd0-b7093d4c8e03 | -6.34222 | -54.91558 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a7b8c0e-e7c3-3d6d-aa64-fec543f13aa1 | -16.32372 | -55.38174 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46df550e-5abc-3610-8507-b42437ab4213 | -6.4431 | -52.73645 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc1fb0f-0e0a-3518-a6b8-dfd0764761a0 | -15.88882 | -55.56889 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6874bb4-ba59-3329-900c-65d110ddd87a | -5.43487 | -48.41855 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5fd27e3d-77c6-3df0-a18d-11ce22063807 | -6.10487 | -57.73944 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb1b5a7b-78cd-3220-b572-b9214cb0432e | -4.45847 | -55.45686 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0c5d9a5-c99c-3f98-8bf9-b2426a1d6f26 | -6.13873 | -57.87541 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f63d5187-2a5c-3324-903a-41eabeee1ad3 | -14.15732 | -52.94339 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26ed8652-fc40-3c07-9be5-b46b7e38a1ac | -11.71709 | -54.63237 | 2026-08-19 05:25:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0df2da7-80ad-3a29-9249-de794f4dd6b5 | -6.13933 | -57.87146 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3991f725-19b3-3686-9a41-6b0ce7f64117 | -10.49773 | -59.61214 | 2026-08-19 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5195c2-bee7-3c31-a045-389976ac196c | -6.34588 | -54.92007 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b5a7c0e-0aea-3ae6-8ff8-af18e4e4667c | -16.26163 | -57.66688 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2977eae7-0cbd-300c-8541-3be4da77123f | -15.7708 | -55.57839 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 199b2065-1932-31d2-b6cd-71792b24e39d | -6.39357 | -51.75034 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029351c5-931f-3eed-b8ba-a79dfafe5eee | -14.14992 | -52.93564 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bca0a4da-a6f5-3aff-a57d-c9f1526525ba | -6.02262 | -57.80605 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9042758-e29d-3c8f-b860-0b27208dd6ed | -14.1523 | -52.93956 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c90fa19-7739-35f4-96b0-0dd6172f9d7a | -6.09815 | -57.85711 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f64ad6b1-413f-3e29-baf1-b3a25804a4b0 | -11.22885 | -55.05262 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 916b18ee-101f-3950-a825-7efa068a8269 | -15.87611 | -55.55769 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b4bd085-4978-3d3b-9863-6e22918744fa | -5.49631 | -60.13118 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0c107b4-2761-33da-b340-ab64f3371b5f | -4.28111 | -60.85543 | 2026-08-19 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5cd0a92-be47-353a-bcff-9fd21c8be012 | -15.23422 | -57.66014 | 2026-08-19 05:25:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 509ef2a2-d09e-3089-aa67-c4ea76e72b7a | -15.25672 | -56.49069 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96718f8c-a589-3f11-bc15-e465a87fc65a | -10.94064 | -57.11813 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e736d92d-1cdb-352a-89cc-80d220c13c74 | -6.09756 | -57.8611 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b91712-8171-377a-8102-c9cae82e7822 | -15.3225 | -56.45765 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7fa471ad-21c5-3181-a7b5-f2a6b9237160 | -6.08689 | -57.90818 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 391897c4-8403-3d1d-b0e5-0071c9b34a5f | -16.23081 | -59.95971 | 2026-08-19 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1293e78c-68b0-36d2-bf87-d21fbceb0919 | -16.24499 | -57.66793 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cc112c56-3228-3fa5-b723-ea93aa761c7f | -16.25764 | -57.66894 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| af042a00-bb4a-3d86-9aa8-15d73b3cc7bc | -4.46683 | -55.462 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd57163c-c07f-3bfc-906d-14fc75afe6c4 | -11.22979 | -55.08052 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c981faf-60ef-3e62-92d5-764c05a22299 | -15.76994 | -55.58023 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18f076f1-c2d4-35af-bc86-0ca3e7dd0451 | -6.11907 | -57.7416 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aca5d657-5fe2-34a0-8076-7fdab92908a0 | -6.09394 | -57.90923 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62936bca-d5a5-39d0-aea7-a102fc59ae29 | -14.21807 | -52.91462 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f25d765-96b5-3972-9cfe-38e250146732 | -15.77558 | -55.57232 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbae6906-7c51-3aaf-972a-fde04ab8996e | -6.44545 | -52.71981 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e0d429-e84e-3e60-b339-ee2c0a645522 | -15.32303 | -56.45354 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f919112-a3aa-346a-b0e4-6ecd66d81841 | -11.2206 | -54.01223 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8538cdb1-ad61-3e6c-9bc1-02bbdda2b99f | -6.10462 | -57.86215 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d094ad0-6e38-3a74-b095-5133b31fdf67 | -6.12331 | -57.71333 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cf8fdbf-f98b-3cdb-ab21-040d599aa89b | -6.10403 | -57.86609 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be950b21-acdb-3436-86af-a25291f7aae7 | -16.74309 | -50.22379 | 2026-08-19 05:25:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1266266-6a79-37f3-b790-d8a04ec38a03 | -6.147 | -57.8686 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23ab9905-f82a-349d-87a8-a6a6f8b1249a | -6.01306 | -57.84542 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b33be7c-37d8-3446-8846-d69b9294a754 | -11.22252 | -55.08104 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97741e5e-7c40-359a-ad93-99af3b490702 | -11.64198 | -54.52967 | 2026-08-19 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README61.md)
