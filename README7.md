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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cafe3091-63d4-3960-b367-4bafb1f4c9f3 | -4.76779 | -41.79572 | 2026-06-23 04:04:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0c4869f-c3b1-32fb-8f6e-c22e339145ef | -2.48221 | -47.08379 | 2026-06-23 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c52510f-8d95-3eff-9669-e81d852b797e | -5.82483 | -45.05489 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91666fb1-6b6c-3667-a113-f81bb2dbdf14 | -6.18652 | -44.86189 | 2026-06-23 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5db584b-4250-37f6-84ef-b43ca880009d | -5.82769 | -45.06285 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 838fffbd-1a60-3553-87bc-0f6c129ccebc | -4.35282 | -47.7654 | 2026-06-23 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 428428d6-9dfd-31aa-9808-6039a326b92d | -5.94014 | -43.46439 | 2026-06-23 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cbfb8e12-1800-3567-abdb-7db114495b0e | -5.81899 | -45.06488 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de1f3b84-8cb3-3353-a6ce-7c5741f05fee | -6.99818 | -42.89521 | 2026-06-23 04:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9fb14992-a662-38cf-82f4-85b0c83d383d | -4.98392 | -37.23359 | 2026-06-23 04:04:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20c122ee-afdf-32a3-a0a8-ef5c5658f355 | -5.82137 | -45.05052 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f6e3b08-a2ab-3e14-877e-821a2d4fac59 | -6.99339 | -42.76904 | 2026-06-23 04:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ba9ee46-7d34-3105-b6dc-2928c1e6c7b8 | -6.36476 | -43.59447 | 2026-06-23 04:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9773a2a-54bc-308c-9f8a-e9018948fba9 | -6.6335 | -38.72593 | 2026-06-23 04:04:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34ec45ed-db5b-35c0-8c0d-718844b1014f | -3.5146 | -48.03374 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d485c264-9d02-388c-935d-fc2ab3e4dc86 | -3.51309 | -48.03455 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd66ae8-2784-360f-a01a-a3f1a455765d | -3.51202 | -48.04102 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0cd3377-de13-3b25-882d-d29e9f312ef6 | -6.99627 | -42.77359 | 2026-06-23 04:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3200eafc-84d8-3060-a04d-1a6f06f06715 | -6.99563 | -42.77756 | 2026-06-23 04:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91ecb683-2815-3e41-bc34-26ff63c4dfd0 | -3.86754 | -42.96467 | 2026-06-23 04:04:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1c48d012-465e-3f0a-a523-4d61dcb38a50 | -6.40079 | -38.84629 | 2026-06-23 04:04:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db54e380-d27d-30ff-bfec-ae720b5259a6 | -3.86824 | -42.96034 | 2026-06-23 04:04:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 38b5dca7-493c-3959-b4fd-6d6bf9067758 | -5.81959 | -45.06127 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66961681-6b88-36ed-b705-580ec497dcd8 | -3.5089 | -48.03601 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8c276c1-1386-3255-a251-865e9944b843 | -6.50229 | -42.22243 | 2026-06-23 04:04:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5092e4cb-d705-315c-b492-b2c05f2654e3 | -3.51351 | -48.04013 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db37b28d-775e-3850-8ba7-f760f11b2c31 | -4.05404 | -43.24839 | 2026-06-23 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e458ce1-2ba3-3106-b121-8358d6d21ab2 | -5.82828 | -45.05925 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23c77deb-20e6-32c3-9cd0-791cf15175f1 | -6.22504 | -48.45236 | 2026-06-23 04:04:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fe5398b-3e10-3a74-9e85-2c04f458fb43 | -3.09868 | -39.92122 | 2026-06-23 04:04:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04a303bf-6bf4-3a2b-b117-0af632554af2 | -5.82423 | -45.05847 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ff0a586-6028-3879-9eda-44ff4ffe0d6d | -6.24735 | -48.52137 | 2026-06-23 04:04:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b6c7b85-4108-3eda-96d2-ff3af43299b0 | -6.99612 | -42.77661 | 2026-06-23 04:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3bcfb2d-030d-3e2d-beae-df6d105c85cf | -6.39891 | -44.18474 | 2026-06-23 04:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27583fa3-6d97-38ec-84a9-cd253b923522 | -5.81778 | -45.07216 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0927417d-d709-372a-8a89-9b949c38067c | -5.80105 | -43.78694 | 2026-06-23 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9308cbf9-8481-3a26-bd19-a12692748d9b | -5.58661 | -46.3748 | 2026-06-23 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f33b770-6487-3cff-8232-7cbb8d6d6522 | -3.5079 | -48.03379 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bd34506-50b4-3cdd-a242-8064707ce764 | -6.99392 | -42.7681 | 2026-06-23 04:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0d52e87-9098-3c0b-ab81-1f4f17bfa209 | -4.35331 | -47.76254 | 2026-06-23 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0992040f-a2b0-3e85-a2d7-c7adc306a0a1 | -5.82888 | -45.05564 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1f80d47-f83a-3753-9817-268fb6b7a897 | -4.3478 | -47.76462 | 2026-06-23 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cda0d3e-7f7c-3630-af8c-8b6147f364f3 | -3.09923 | -39.91776 | 2026-06-23 04:04:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 364c46d5-2adc-3c27-a234-5953c3054c8d | -5.8003 | -43.79149 | 2026-06-23 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de952e44-cc0f-301e-a053-8c0ce79080dc | -5.82709 | -45.06647 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf3dc174-a544-3108-9238-b6a44bdefe65 | -6.25194 | -48.52514 | 2026-06-23 04:04:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94de8309-edf5-3619-9b90-d1d5a73e7159 | -5.81718 | -45.0758 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89113641-b5f6-35a2-9736-a813f9f0dd67 | -3.5074 | -48.03683 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3968c301-b496-396f-bfe7-d90c458954d5 | -6.50697 | -42.21539 | 2026-06-23 04:04:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7dbfed58-60de-3dd3-8c9f-07482f02b8e3 | -3.67255 | -48.99089 | 2026-06-23 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c22b7636-946d-3e51-9321-80299b27b5e5 | -5.82018 | -45.05769 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5868fe9c-7ab9-38ce-acaf-3f6ee24c8cf9 | -3.51257 | -48.03767 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eca456d8-4780-3b19-89af-8f693c8cca5a | -5.82244 | -45.06931 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3576f4f2-45c6-377b-9978-c571ec534d31 | -6.18878 | -44.87309 | 2026-06-23 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad571190-2cad-3a47-8f18-87b69303f5cd | -5.82364 | -45.06206 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bba03074-b811-38f3-9aac-244735df94ae | -6.25243 | -48.52243 | 2026-06-23 04:04:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f25afdc9-5e4a-3615-888e-128572095713 | -3.67191 | -48.99454 | 2026-06-23 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0c37236-1cd7-3452-9f71-29901507a8d7 | -6.99398 | -42.89861 | 2026-06-23 04:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9bacc4ef-8bfa-3d3c-8b51-6c4216dff819 | -3.50834 | -48.03922 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21330ae4-e6e0-3331-95a5-c7dce4e79753 | -4.51241 | -40.58459 | 2026-06-23 04:04:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 717793c6-d66c-3f43-93ac-d775534748e3 | -4.45314 | -48.0237 | 2026-06-23 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edaa1e68-58ee-31c2-a866-125ced87688f | -5.82304 | -45.06567 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6d6a41e-064b-3720-b30b-8d638602cc58 | -3.67181 | -48.99395 | 2026-06-23 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 962ddf78-7487-31b0-8248-ca089b78b8c1 | -6.2255 | -48.44974 | 2026-06-23 04:04:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 505db999-07f1-3ff2-a147-77bb0499e80a | -6.57695 | -44.56661 | 2026-06-23 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddf85cf5-6c91-340d-932d-0cc94ad9aafe | -5.82078 | -45.05412 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e10d760-c1f3-34a8-992f-2d67b5ae0819 | -4.45365 | -48.02072 | 2026-06-23 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931e24f4-ead7-3e80-9d60-ecbc2c22b4b5 | -3.50686 | -48.04013 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d062e704-b48f-314d-a226-e84c9f831889 | -5.93941 | -43.46876 | 2026-06-23 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 12fa4856-975f-3d2e-add2-6ddbde1f9478 | -3.51407 | -48.03683 | 2026-06-23 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aecc3358-5727-38db-96ce-201126a96330 | -6.18936 | -44.86958 | 2026-06-23 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a15f4e74-28e8-38de-a6b6-af8c951eb160 | -6.62286 | -43.93425 | 2026-06-23 04:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fdb0aa9-9e82-3e30-b076-9aedce155be3 | -8.12612 | -47.89245 | 2026-06-23 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e085d35-a58c-39e5-bca0-86edab7e1a8c | -11.28073 | -43.33832 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c0f6346-92a2-3959-9f35-2752d5a66b2a | -12.85375 | -44.36116 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fed27b65-23c1-3ce0-909f-0303a3d8a3f0 | -12.86298 | -44.37124 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc90f579-077f-3a8e-8133-80909d25a073 | -9.22449 | -45.33193 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d857d7ee-0262-3535-bca1-7a98a7069701 | -9.77682 | -48.97941 | 2026-06-23 04:06:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6660b871-4e08-397b-9bc2-bc6417f59265 | -12.87284 | -44.35613 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc51034b-d9c0-396e-a262-299e48f2f63c | -11.04612 | -52.46304 | 2026-06-23 04:06:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f9e1b86-eb69-329a-b533-82fd2331d0ed | -10.53907 | -47.71635 | 2026-06-23 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43f210af-e6cd-39ef-b6ed-854268033328 | -12.86722 | -44.36778 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b93274fa-0c89-3645-a705-772b91015b24 | -12.87353 | -44.35205 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 493654fa-5fa3-353f-b20c-635d7b44a3de | -9.36788 | -50.54034 | 2026-06-23 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2999db1-2826-3a8f-877c-f7b4ba926e54 | -12.45505 | -46.52399 | 2026-06-23 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63fe8a98-cb96-319f-a8a0-b2641d017662 | -12.8743 | -44.36905 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad9a4141-730c-30bc-9f3d-20869461399b | -11.81532 | -47.34146 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df96fb2b-b2ac-370e-84e5-75c5a353ee4c | -9.21294 | -47.92932 | 2026-06-23 04:06:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76fde740-5e96-38c8-a9e7-9c5bce01a2ee | -9.21578 | -45.33555 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 408ae4a8-ebec-3d00-a8bb-f25a0266b42a | -9.21971 | -45.33625 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 533e1090-5334-3bdc-85d1-11083971b934 | -12.8693 | -44.35549 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2d2dd7d8-03e7-3e82-bbdc-dbea88e61167 | -12.8502 | -44.36053 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 16b83199-11b6-3cb5-8bff-4897f8f4e62f | -12.03055 | -47.80324 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eb6a8e0-a267-3d31-ba3e-e0a518b27dee | -11.80247 | -47.3391 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ad248f4-e2d7-3e9e-b302-9ed322b0fb79 | -12.50623 | -48.27222 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 612c4bfc-b7db-310d-b6ab-d84a96fa0ac5 | -7.72419 | -44.56675 | 2026-06-23 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10f359ac-f0e8-323a-acc4-3855f0d60ff8 | -11.83646 | -47.07804 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8719dc-9fbf-347c-aa68-cf38c5f8c0e9 | -11.30919 | -54.72432 | 2026-06-23 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5629006b-ce1d-31e7-a29b-23c45d484e12 | -10.53987 | -47.7119 | 2026-06-23 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08a81bd6-7bda-3dc9-849a-121a02c1cd42 | -10.88468 | -49.54465 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)
