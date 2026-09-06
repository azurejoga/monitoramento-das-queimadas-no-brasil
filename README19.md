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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18035653-b556-311d-aa7f-ec7ea442d080 | -4.67499 | -55.63317 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f6eab83-7aee-32db-bc9a-c377a9ce1c40 | -5.33499 | -56.0228 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17149cc5-59e3-38f3-a033-74998d9c703c | -5.25652 | -59.97935 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db047514-96fc-3a27-a3ac-ccfc7ab29f14 | -3.55347 | -48.18262 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1652075e-20e6-3902-bfd9-e24d4a07219d | -3.14085 | -60.63576 | 2026-09-06 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12c75298-ed6a-3b34-9b1f-dc0f259c2a5e | -3.77886 | -58.85347 | 2026-09-06 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef730372-cefe-3bb0-a0a1-9fb3363a1e21 | -5.92546 | -47.89201 | 2026-09-06 04:46:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6effcfea-d478-314f-b9bc-5305edff0479 | -11.28973 | -45.10781 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ec3df25-1909-3d4a-95b2-e78a86343cea | -6.06944 | -57.80009 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f8b3c9a-e2bc-3e68-a46b-52a55c822e16 | -3.62766 | -54.60974 | 2026-09-06 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 636df6da-5e20-3b60-86a4-94d7272105ec | -5.14558 | -55.95391 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8ae0b51-c3c6-3a3d-ae8f-73c24fc5815c | -3.81078 | -55.89293 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f73cdb70-2d2f-31b0-a74c-63061a148ca8 | -10.70564 | -45.90262 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c76a0a12-58db-326e-bda4-25d662169c1b | -4.66538 | -55.6422 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1df19357-7804-3345-bd31-26a45e9341fa | -5.36785 | -56.02459 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 011d30bd-cf3d-39cc-ba46-137eec0c0edc | -5.35518 | -56.02611 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dcf763eb-89bc-368d-a441-c75627b3f9d1 | -5.6592 | -60.23892 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0952b3-2aa9-3cab-a81a-d3e57650d300 | -7.10058 | -56.51471 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87452378-f35c-3697-b70d-19e0062e04d2 | -4.64049 | -48.63755 | 2026-09-06 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6632b0af-8483-3677-9aa3-e46e8e262b5f | -4.04338 | -52.09011 | 2026-09-06 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb31cc10-c24c-3a9c-8fbe-36d3d201db4c | -7.89802 | -47.69547 | 2026-09-06 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 813dc8ba-e849-3f91-adb9-d0da5d418d36 | -6.87821 | -41.04858 | 2026-09-06 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4edb8617-8afe-31c4-9140-fcc0f3707464 | -3.41398 | -54.77578 | 2026-09-06 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be675f34-521e-34a8-9419-4941d1fd24e8 | -5.14327 | -55.96808 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 17b4cc95-d66c-310c-af36-f86c1d8c7cc5 | -6.33174 | -43.35266 | 2026-09-06 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bf98711-efbd-33a5-9081-c3348a8ac5f1 | -5.35114 | -56.02542 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a7c805-67c3-31f8-917a-56c9e3f5cf49 | -6.18497 | -40.87755 | 2026-09-06 04:46:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bf733e2b-2cc8-3988-a16c-7155e79e82a9 | -3.76889 | -61.76585 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c1e573c-63a2-3294-a50d-f1781b3a698b | -3.78891 | -58.85507 | 2026-09-06 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d010ce7-5646-363c-a1ff-adceeccbd3bd | -6.50837 | -58.29316 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8503943-1a55-3152-a915-3214929b32ee | -6.05961 | -57.79126 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 31b09089-d15b-34c9-8a34-104723b792db | -4.35269 | -56.28991 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f98cd889-ba0a-3ae4-a0c3-52bdb5f63a8f | -4.6784 | -55.63733 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0822287d-7dc1-38c3-808d-7970707a09e1 | -3.7921 | -55.87872 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38197d50-fd4c-3261-b9ea-9eeecd243225 | -4.1156 | -49.09016 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f95629e3-f65b-3690-bd04-a9856b469291 | -4.92302 | -55.80957 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 069d79ad-3c02-34bf-a9dc-e1ef61c582de | -5.85254 | -52.04753 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc5e996b-05b6-314b-9e72-366d82723fc6 | -6.0612 | -57.79421 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ff0b6c5-a037-3620-9526-68f4921232a5 | -8.50456 | -54.64787 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 943d2f7c-0fb4-3434-907b-fbea75ddd40c | -3.76811 | -61.77048 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81bc71d9-9164-3d25-921c-af522e8bc6c4 | -5.04351 | -44.46535 | 2026-09-06 04:46:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddfe4b28-598e-3ef5-ae20-f10cb8c8c5a8 | -6.44178 | -58.15649 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebf65b87-fbe6-3bcb-8f8b-bbdbd95e3d0f | -4.81383 | -49.38818 | 2026-09-06 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2bc7ca5e-234d-36d1-9ccf-2f098e8433e4 | -5.59436 | -60.24477 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b75a381b-cb73-3eb8-8f04-65aa01c56803 | -4.66761 | -55.62833 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df8630cd-1673-3057-845e-61f96289fed8 | -4.91846 | -55.81231 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5770373-0a94-313f-81a0-9a2722937d4f | -5.3546 | -56.02966 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ee39f3d-bc1a-3bd8-946e-6fb7e4cbc229 | -4.66705 | -55.63181 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0541f20f-65df-3e13-bb18-a697373f8bca | -4.55904 | -55.03889 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dce3416-7e69-38a0-889c-4ba54edfb1ef | -6.00054 | -57.78532 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ade2c09-919d-3700-8029-640228639cf3 | -5.36036 | -56.0197 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c56538f-5f59-3ce6-8042-3d2242f3d58a | -3.76955 | -61.76823 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c7587be-060c-35f0-b8c4-ce272a67924f | -5.36498 | -56.04233 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f66170e-1bbc-3204-b09e-e51d44b12b69 | -4.11332 | -49.08244 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3c992a5-aabb-3c2a-be27-93133b867432 | -5.15307 | -55.95875 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aff10443-8654-3ca9-bcc3-5e23cfed2eaf | -5.36671 | -56.03168 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9f73cfe5-af00-319c-a217-ed4b0f3e713e | -4.69204 | -56.09833 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de57d0a8-bbe0-3aba-a66d-dfd1ab3b43a8 | -5.35344 | -56.03677 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b3da182-9e75-3eae-b5d1-e15d70aa4eab | -3.42106 | -58.31346 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4866b242-d356-3714-92af-3f907e7da69a | -5.25699 | -59.98185 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0729182-f3d9-3874-92bc-2afd0d6a7798 | -9.57453 | -40.35596 | 2026-09-06 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 05b84955-0ce4-3876-b418-6d890ec91663 | -5.17128 | -56.05472 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300d87ae-b75d-303f-ac71-b73a5b4841ad | -6.06787 | -57.79712 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23a82a0f-2ee9-3ae1-bad6-bb525cd3696e | -11.28847 | -45.70213 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 474dc79d-51a7-3c42-b0da-d3f1acb7474e | -5.15193 | -55.96581 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 60fc22fc-5d48-3fc5-b208-601a0a457afc | -5.33729 | -56.03408 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0da427a-f316-3ebf-a107-147d6abb8158 | -5.34249 | -56.02763 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1bd4c5-442d-3c2a-919c-8b9f9ea80499 | -7.37264 | -47.0216 | 2026-09-06 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 46f4d601-9512-3432-ae3b-7e60c1dd1477 | -6.51301 | -58.29375 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd828f61-3e69-3027-920b-751aebf4649c | -5.34191 | -56.03118 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd339ce-e156-3eb5-a6aa-42d22fbfe4cb | -5.97382 | -57.68213 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84852da7-0ab9-399c-b711-34a450b5a6d0 | -5.35402 | -56.03322 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f48e0189-6ca4-3271-a7c9-642a0a4e2b8d | -5.3569 | -56.041 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ce3c181-bb99-3c1d-8e25-a56f2cbdea03 | -7.27726 | -55.14784 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53d16d0-02c2-39c4-89f8-8e8123923b35 | -5.17068 | -56.0583 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 190d4173-b5ba-33e7-a49f-72a89efd8931 | -3.81488 | -55.89359 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aea94a78-3528-39fe-a27f-1d5cb7fefcbd | -4.35144 | -48.96971 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc8935d-c3a8-318f-b394-1fee759df255 | -7.44735 | -49.72718 | 2026-09-06 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 705c6a57-05a8-33c6-b887-6d5d75a47140 | -7.73146 | -44.30827 | 2026-09-06 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aea1252-aef6-324f-8f07-53c88b888464 | -11.29036 | -45.10288 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba3ac4a8-524e-31d1-ae1f-7d3ad3eb9d8e | -6.94891 | -59.76168 | 2026-09-06 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b57148f-898a-3077-ac90-31456b898ffa | -6.84235 | -59.42722 | 2026-09-06 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb1b96e7-8a74-3602-826c-276bfed49fe7 | -5.13642 | -60.36613 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a18de3ea-036c-3ab8-a2db-5e48acaf7620 | -4.11671 | -49.08295 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07154774-0b71-3498-8b26-c02b1f88d4e6 | -6.06199 | -57.78968 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a5f5dc3-6851-35ea-b9ea-e28788388c11 | -6.40173 | -51.25866 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fe4288a-4e35-3633-a3c2-52bddf332436 | -3.15358 | -59.14606 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be112a21-0c4c-3572-b005-5e0da990a27a | -3.79559 | -55.88304 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e199239a-aa3d-3bb1-8d10-fce7fcdf77ab | -5.50561 | -44.02332 | 2026-09-06 04:46:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daad64cf-cd2b-36fe-9d46-c80ff313fe5c | -4.5564 | -55.04081 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fd04ff1-75da-35ab-934a-692664a21b0c | -6.12948 | -57.74546 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16d3dc23-ca85-3b8f-a3b6-cb30998a6cc9 | -11.29447 | -45.70008 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f31f3cf0-bfe2-3a35-b59e-4ec9427112a8 | -6.94995 | -59.75582 | 2026-09-06 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecedc000-b4f2-3b8c-afef-f8bfa31496ef | -5.36152 | -56.03811 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5639a4d3-f306-3d47-9f89-6ae6aaf8b42c | -5.25223 | -59.9778 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfa5841e-f1c7-34cb-bd80-9f16955e6af7 | -6.06571 | -57.79488 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac3970e4-51ac-382d-869b-d4c5cc4637c9 | -4.36887 | -47.7809 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd30df4c-5e1b-3d88-81fe-5b973bd741be | -3.38901 | -59.41415 | 2026-09-06 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f02f5824-a03d-3277-86e6-a187de82b82c | -4.36593 | -47.77628 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| b67a8d23-eb4d-30b1-bc09-eca17ba9bf34 | -6.87311 | -55.61062 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README20.md)
