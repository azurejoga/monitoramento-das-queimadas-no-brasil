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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce6977a4-d6e8-31e3-b84a-4fb9e1622633 | -1.2914 | -54.556 | 2024-11-06 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3daba0b-7a7e-3dbc-8ad3-dd91adb53258 | -3.2921 | -53.1134 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6119328-9fc3-33d5-b023-5a70b2e06fee | -1.503 | -53.498001 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ccdb8e5-798a-3a37-967e-9b177daaa395 | -2.7575 | -53.211102 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd67948-166b-39fa-9d35-cac42063a9cb | -2.8445 | -49.476002 | 2024-11-06 00:54:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4616d92b-97b7-3fcc-b86e-6b77bfe0cc1c | -3.0376 | -53.263401 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c186b162-88b6-3b23-ba90-1538c9850c57 | -6.4932 | -47.492699 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b945882-60a2-36b5-88bf-cee7dcbf0f40 | -2.1509 | -53.669899 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e27df8-70fa-3061-adbf-9fe82688f455 | -2.9196 | -51.044701 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6131c76c-5c0a-3251-a709-b4d8cff5a8c7 | -6.4885 | -47.473301 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 846a3bdf-c087-3079-93e8-8e4b202d9f98 | -2.3876 | -46.559299 | 2024-11-06 00:54:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8321cbd4-4786-359f-b759-f28a1d236082 | -2.8242 | -52.917 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6556e9c-5805-354a-be86-7be70c5f991a | -3.2937 | -53.120201 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db07e7a-653a-33e8-af47-11d3b73b9c72 | -3.3234 | -50.071602 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74012ef7-fda5-3774-a095-0948077e144c | -3.9561 | -48.1465 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa708b33-831d-35ef-8f16-dd6b0f4c4abf | -3.745 | -50.065498 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a318ace-cfa4-3c31-8eee-9a6dac7ece46 | -2.8636 | -51.786098 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c2e1c02-c292-3ed8-9518-74a6258ae3eb | -3.9681 | -48.153801 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce19d8f-de7b-3174-b9e3-1953d8e4e305 | -5.3148 | -43.070499 | 2024-11-06 00:54:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faa15182-b95d-3b0e-bc85-1b7d6f058f5e | 3.6184 | -51.3022 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d6b6d2bb-11d1-3d28-b9fe-cdaa6f33b98e | -6.1048 | -43.980999 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce745348-6d9a-36ab-888d-92fac241fb0e | -3.0215 | -53.418201 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b1f6bd-e311-34c9-b21a-39ecb19b288f | -4.5622 | -48.0061 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65767b74-15bd-30c2-94ac-ddb9e5d03ff0 | -1.064 | -53.653198 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a19991-93e5-3c29-94da-206daa966c8c | -3.0363 | -54.205601 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5f486f-1ccd-38f3-9345-0db57a9d9426 | -3.1408 | -51.1987 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950189fa-4e61-307f-a904-46394221e3a1 | -4.2186 | -53.558701 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768f46db-73ea-313e-bf62-30a49f85ba33 | -23.947701 | -54.046299 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7de644a-0556-3fcf-b0ac-16fcee986af9 | -2.8467 | -51.354801 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e55b50e9-2c06-3538-8a99-fad4cebbd2e3 | -3.4933 | -52.101101 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d1aa05d-c89e-3ca3-95a1-be5b13bf68fe | -1.5555 | -54.268101 | 2024-11-06 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 897eca8b-3673-386b-84cf-b43bb4acaf47 | -3.0827 | -50.946899 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d64d6c2-8b3d-3276-b77b-a81780791853 | -10.396 | -48.926701 | 2024-11-06 00:54:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33a46c50-b0d3-3222-8ded-c29f28d00c30 | -2.9442 | -51.061901 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8748fa4b-0b69-32c3-937e-2acb435cb674 | -6.1339 | -43.9739 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f36a7a0-b2dd-33ff-8f06-935e0e1f9097 | -5.6689 | -45.949001 | 2024-11-06 00:54:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e538c2c-9c61-3fec-b1d8-1817a5d601a5 | -3.335 | -50.077202 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7acea9-81df-342e-ae09-d22803d60807 | -3.327 | -50.0872 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ae9f72-ff96-3682-a2e0-e356ddc61cee | -2.674 | -51.814098 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19def675-6bf3-3e58-a792-33095ad9b58b | -3.5923 | -58.582199 | 2024-11-06 00:54:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c45c08de-90eb-3485-8136-8e06bc4634b5 | -6.1104 | -43.961899 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8338659-23a5-3db7-a680-336d5e73d05a | -2.1493 | -53.662998 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cac18ea-36d4-37ab-b0d3-a7e54bfd604e | -2.0712 | -47.0494 | 2024-11-06 00:54:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d1f0cc6-167c-34fe-9e1c-e5c0edb5769c | -2.8062 | -52.928299 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4234e2-f7ac-3d1c-97f2-8b4bdcb5e836 | -2.849 | -51.767502 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb47dbf4-8f70-3dee-a185-5b64aec7c9c7 | -3.5331 | -52.994999 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92b702b-2d10-3418-88c8-121f0aa208ab | -4.5502 | -47.998699 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa1ed8a-3b85-3919-9277-bec4f15e353c | -1.088 | -48.2136 | 2024-11-06 00:54:00 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b1a74f-38f4-36ec-9bc1-16b7f2986401 | 3.5294 | -51.240299 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd2d9b5-a0d0-3a0d-a981-ed8f109c424c | -3.6675 | -50.220299 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5742b7a-2d05-3b83-9260-35dccd79ae7f | -3.1194 | -51.105701 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d72124f-690a-3fef-ac50-14d25a71794d | -2.7259 | -54.155602 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2975f160-c8e8-3317-aa63-76d3536cb899 | -3.0844 | -50.954201 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab646e15-b120-33d4-ab37-0b2f6583f709 | -2.5469 | -54.003601 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f4e5169-b78f-33fd-b9c4-300264c18fcb | -2.8353 | -51.349899 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed5cbf41-2609-3eed-935d-ae3e22d6b3cb | -3.5979 | -51.569698 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 240b0630-28aa-3b8e-8c59-ef52ed7f4cb4 | -6.1063 | -43.945 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccaa1a42-1192-3ca7-b282-caa8fc74b005 | -2.9539 | -54.793999 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6214d5d5-10e6-34ec-9ad2-de1afe189866 | -2.398 | -46.167999 | 2024-11-06 00:54:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0cd2c2c-9eea-3542-8787-ff06ddc816a3 | -2.5763 | -53.997101 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8b96b9-d9a8-32ab-bde2-52b54b7a2de1 | -23.938 | -54.048302 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27ea1f9f-544f-307b-8fbf-7d1b3d3a705b | -1.9062 | -52.153702 | 2024-11-06 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e7e198-d37f-330e-b285-7e1a716ccfb9 | -4.233 | -48.534599 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe5b98a0-4ebd-3d8b-b76d-4f77bff9dc98 | -4.56 | -47.996498 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7321c9-331e-32ba-a4c9-879514c9f2ed | -2.9773 | -53.269699 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd635538-65fe-3cce-87b9-360805966c24 | -2.167 | -53.695202 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bae0c9cb-45c2-395c-bb69-9e7dce20d93f | -6.4945 | -44.6861 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2066278b-c008-3f58-9cd2-2adbadad65e9 | -1.3339 | -54.606201 | 2024-11-06 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 238fe4c7-0f04-3932-9bca-4f70b200d7d4 | -5.233 | -48.138699 | 2024-11-06 00:54:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae940ff-b802-3a80-9454-14e3c876e79d | -2.9344 | -51.064098 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79201735-23df-3852-93c1-f2abef2325ba | -5.551 | -43.694099 | 2024-11-06 00:54:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10889e5d-d1c8-371f-9ada-c5e3a99e7eea | -3.0278 | -53.265598 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41672225-a83b-34e7-b50c-b1109fc81edc | -3.0701 | -52.504601 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c05b78c4-19c8-3606-9e31-25c5d61771ea | -4.0639 | -50.0172 | 2024-11-06 00:54:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1869e0b-dac4-38a8-8909-1c2aed58bb42 | -3.7367 | -53.389099 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57100970-0642-3741-b35e-989b99ada60e | -3.0105 | -54.0924 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c62420-158f-3090-bc00-6a97fcaefd8c | -2.7243 | -54.148499 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea3ffb93-4917-3a71-8923-2aca73d1ca28 | -3.7196 | -49.425301 | 2024-11-06 00:54:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b56a7a-9a8f-34dc-8ba2-40283d3a12eb | -4.0581 | -46.922199 | 2024-11-06 00:54:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aebd85a7-8f9c-3496-a06d-95ad1086a6c4 | -0.3555 | -51.421902 | 2024-11-06 00:54:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5c925a33-a461-3151-8de9-010c84c3de54 | -9.5987 | -49.537201 | 2024-11-06 00:54:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df9d1157-e84e-32b5-b049-a20b74d89ab7 | -2.7474 | -54.1138 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5c3784-4be1-31d4-8be4-0a694a5f3eab | -4.0608 | -46.933601 | 2024-11-06 00:54:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c863ad2b-ed5d-3247-afae-03399d796c26 | -9.8918 | -42.0979 | 2024-11-06 00:54:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5681e4ce-813c-322b-8400-d4d111eb5a3c | -2.9425 | -51.054699 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b90e8d-c01c-3c44-b5a5-049e5234622b | -3.9936 | -43.242298 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90acac81-4379-373d-aae2-36270c700a67 | -1.3519 | -51.942101 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176eea6b-002f-3ced-8256-5e093161bc24 | -2.6702 | -52.515301 | 2024-11-06 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8bab117-13b7-3435-9b8a-70d9ae88fce4 | -4.1387 | -43.584801 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 858eb13c-6bd1-3608-8fb9-6693574ced0e | -2.5835 | -51.331699 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfe42fe-2582-3c8b-bdcf-fba34a19b298 | -6.9353 | -47.788502 | 2024-11-06 00:54:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3159c57a-89bf-3dc7-9f51-fba2a3c1eb26 | -6.4811 | -44.673698 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 155515a5-3bd7-3cbc-8138-50cb97fa78a9 | -3.0837 | -54.504002 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e37ac17-2f03-3a25-b3a6-401e9f7e995e | -2.9441 | -54.7962 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ccc68e-1ba1-3f80-bf27-356f54e2daae | -3.118 | -54.247299 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e18f1fa-57ce-39d4-bfab-ed8b8764a349 | -2.7823 | -52.869202 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c57d1434-6e17-34e7-a956-910b59adf8de | 3.5196 | -51.238098 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a5347fec-383d-3403-8195-2a557e9dc043 | -2.8392 | -51.769699 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf9533d-b0c9-3e31-9699-959e82297815 | -4.078 | -53.937199 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c775ea1-83eb-38a4-923c-632e175ab993 | -1.5539 | -54.261101 | 2024-11-06 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
