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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbcb8595-754a-33a5-93df-6b29791d32ed | -14.15896 | -45.16793 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11696892-3b7f-3c19-bb37-4bb7c7033adb | -10.85317 | -50.19409 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cdcd351-ee2b-3521-8ee6-4714ca77b341 | -12.35008 | -50.70704 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ef1eb7d-1de3-3824-93de-3c0e82df6fce | -10.87059 | -54.10076 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12b57d53-f99b-34a3-a17a-762a810a1aec | -12.41557 | -45.05017 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7012d6ce-2b96-3be2-ae8e-1bde7afd44a0 | -10.89209 | -50.87711 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85c8541d-c7c9-3a23-8e7d-29c46f43716d | -13.6268 | -48.31328 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa9d325e-eff7-36c4-9226-d2a18ebf0f35 | -11.33968 | -43.4129 | 2026-09-19 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46f880d7-ec9b-3a33-bdd6-1ad6b4ff6c2a | -12.70206 | -45.95476 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df30a95b-cae4-33bc-8a7d-cf59c002a00f | -12.85911 | -46.33312 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b23d9a2e-e928-3f09-8234-08bfbff71bea | -11.44119 | -51.46061 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b3dfc9d-c5d2-3a8a-b94d-61cacad0e277 | -12.85212 | -44.39193 | 2026-09-19 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 31b3ad94-b96c-355d-ab95-ca71419d2844 | -11.33753 | -47.35049 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b818dd8-257d-3b7a-9dbb-ba10d8d8bf68 | -12.57703 | -47.08827 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ba2aad0-1a0c-30c4-a00d-7b44c2975637 | -14.15027 | -45.21161 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9a162e7-698f-3e24-9913-c708047bb598 | -11.11777 | -45.29804 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99b200be-1fc3-382e-a4b6-9a58fec621eb | -10.79371 | -46.65673 | 2026-09-19 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9bfba95-f459-3f0a-a060-64d0e9ff2b52 | -11.80508 | -46.83938 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 447f0130-a329-3d8e-9b63-d8e9a33921fa | -12.12644 | -46.98063 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02d78c76-e922-3073-8cca-c199c47570aa | -14.94972 | -49.92561 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e5d623e7-ee19-38bd-8096-8ce1318e0aae | -10.93358 | -53.96081 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 635b8143-2d77-326e-a835-6d4f56e7d435 | -12.74495 | -47.01752 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef589040-cf6e-3438-b7e1-5d31375f6572 | -14.79822 | -48.58166 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77ee258d-7938-3cf6-95ba-465bf449f0ca | -12.99887 | -46.97667 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51ccd7e3-237d-36f3-8666-56f1268f1ed6 | -11.1156 | -45.28797 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ec441b8-6c86-3695-921d-5d484f0b94f4 | -11.06013 | -49.772 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0e8b07-893b-380c-af13-de3dfb024c2d | -13.73794 | -48.80295 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9006e28e-dfd3-336a-a484-bdc440f7dddb | -10.87187 | -54.09457 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12aa10b5-5e86-3a30-bcb3-7cc1d8a0a1ad | -11.11858 | -45.29331 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 368c9d4e-a4a6-3806-abbb-ed138b1fdbbf | -12.69221 | -45.94298 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15ad9a12-4138-3f92-ac79-02e4d402f13f | -10.70553 | -50.2605 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e4f7636-757b-3219-8ae3-d2d88e5dfb0f | -14.17697 | -48.75572 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bcd1ed0-296c-3b59-b3e9-ed2fd57cfae8 | -16.88362 | -50.57589 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4cf5033b-0e1d-3119-afc4-6d9d386c422a | -11.94491 | -50.12241 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 673c6ea2-b090-3929-b890-f86468c34586 | -11.48679 | -45.73158 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 176c67d1-6aa8-333c-a4d8-1fc55185a361 | -11.05948 | -49.76689 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1ba1998-d44d-3bee-9177-190ec46434ce | -10.83313 | -50.91835 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae520497-a2f0-3715-9bbe-3bfecd1bf8f3 | -14.67483 | -46.66109 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 612b6b85-5278-3cbb-ab07-fb859b495de1 | -10.83145 | -50.92558 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f44d4b63-65dc-3037-889c-a16e511ae603 | -12.54181 | -47.09459 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aeb7674e-f8f2-3f74-95d1-a6d66d8709f0 | -11.83761 | -46.8389 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9113b25-ab96-3935-91d0-48a143760184 | -14.68531 | -46.64737 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e364c7cb-a7e4-3422-b7a5-5c55a96790bb | -11.80691 | -46.84449 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f12eb4a-7eb7-35f7-b7da-4e189b74bd03 | -13.74352 | -48.79793 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2de7ae1-6828-3af5-b59c-d4810b63d06c | -13.61369 | -46.93439 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c18e4450-6e82-33ba-8adb-b6bf63696bf2 | -13.0083 | -46.9709 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 49d33102-c24e-3deb-b128-c1a69bd7b1d6 | -10.79925 | -50.88556 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a39c40-1e9f-304d-a626-9c0ef0d4ab0b | -10.99838 | -48.32585 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 325943fa-1663-39dc-a470-6a3b81bc2981 | -14.92552 | -49.92318 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 42dfc619-75ba-30ee-9618-34218a85cb49 | -13.88049 | -48.60668 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e58446a5-5238-32cf-83bb-8dc1819827ff | -16.07358 | -52.25238 | 2026-09-19 04:04:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17304ff9-5f97-3f9a-8e77-9fc2ea4054e8 | -16.8874 | -50.57804 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8b5a47b4-7c23-3a2e-9d5e-62a575f6c843 | -16.88848 | -50.57265 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c18b0c25-8c12-314c-99f1-907f7343fde2 | -12.74085 | -47.01679 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57fd5d7e-a864-39c3-8858-02b25f0af786 | -11.47001 | -47.65249 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc36166c-20b2-3f4f-a460-a8506b322b99 | -12.35135 | -50.70039 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ac181bf-538f-3a55-982c-865af862f9f0 | -12.14849 | -46.9764 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 783d33d1-2f9a-31a7-b24b-778121404fe5 | -11.87501 | -47.61388 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 732ebac6-4ec0-3bcc-836c-1eee1d2d0942 | -14.67094 | -46.66039 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0dd4bd45-ede7-3cc4-8a9e-ef0fc80a711a | -14.15388 | -45.21226 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9563d3c-0b19-32ca-8c35-fa75e2a88bd0 | -11.7707 | -47.43704 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbe15244-faca-3641-a34a-faeeb71859ca | -11.44456 | -51.47333 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3da6ee55-60aa-31f1-8fbc-eac1ec714372 | -12.59813 | -50.88104 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a093dd0-27e8-3394-aa81-4068ed74f5dd | -16.80349 | -46.98467 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 811f0cae-a56e-3910-b08b-81b6723584f1 | -14.78862 | -48.58451 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 272a58ec-5e89-3cad-8f14-def608a3378f | -14.81969 | -48.56354 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b50632e-05c2-3d1b-b6f2-a84f5287fee3 | -10.55694 | -51.31435 | 2026-09-19 04:04:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20099e5f-48db-34ca-b868-e3352822b613 | -12.6919 | -45.96789 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e025af25-cdec-38fe-aadd-13b9ffae43e6 | -11.07008 | -48.31997 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2e323481-e6ce-3916-beb3-1e106a75838f | -12.16046 | -47.0051 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 636fdc27-7b92-3f6c-aedc-915d42b969e1 | -12.69604 | -45.94371 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e0ebd5a-7a9c-3335-84c0-db77794175a2 | -12.59159 | -49.10487 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 320bfe73-87e4-37b7-9c05-94474ea6d22d | -10.83102 | -50.92922 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5363e8-369f-3c91-b25d-80d10a888d90 | -11.02134 | -54.1264 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| acfa8b5d-e1ea-3259-862d-075632822d64 | -15.99336 | -46.7438 | 2026-09-19 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f85fa213-a22c-3655-903b-4ed1a50ae971 | -14.66594 | -46.6624 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cef6bf9a-acdc-3650-8a6b-d8ebfd32edd3 | -16.79967 | -46.98393 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 02312a96-b7db-39e5-9298-a585acab7159 | -13.68135 | -48.57999 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3458aec6-d803-395b-b7b8-2dcf2d4070f1 | -11.47736 | -45.74017 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a1fefe05-50d7-3c9b-af89-fba7fdfa8215 | -12.5963 | -49.10577 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 855e0020-4676-332f-aacf-189b3796d07d | -13.61492 | -46.92734 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aca1b846-4170-372d-b78c-137c06340875 | -13.01007 | -46.93757 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 328fceff-2676-3c49-9e2a-071e2a0a5b2a | -10.8005 | -46.64225 | 2026-09-19 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b241d59-02a2-3c96-b54e-363055f17c3b | -15.88081 | -49.89676 | 2026-09-19 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 196f8e69-3c87-3c3d-9e13-852f981af2c7 | -14.15244 | -45.22086 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19eb5b4c-838f-3e00-b9ef-4d06d854d641 | -15.57846 | -56.54135 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bb3fb965-5644-3742-b458-0d4480ea4f15 | -10.83454 | -50.91113 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 446359c2-daab-35fd-ac77-8ef6ec0eda72 | -11.08281 | -48.30177 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 12029741-ba9d-3391-9d29-729d425e11a2 | -13.61001 | -48.30587 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbd0276e-cef0-31c8-9d50-bf627a567171 | -10.83173 | -50.9256 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9e795a7-a601-35be-aa34-0b51658820d5 | -10.91977 | -48.41873 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f0a23ca-0d64-325d-af03-686ac2a895dd | -11.12534 | -45.29929 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82b219ca-3515-348f-a846-48ebee1fac75 | -17.24434 | -46.72219 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a485249-76a7-3558-ac3f-2271a3f37385 | -15.5868 | -56.55743 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bb5b4978-ccee-3ab7-b653-c7eac686a63a | -16.88738 | -50.58221 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 75c13fa5-bb4e-3ebc-a9a7-464ab84b3cf4 | -10.88759 | -54.06571 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e39f72c-9231-3da3-b2e8-46e495a32731 | -14.79906 | -48.57714 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d68367b3-be85-3e6b-a7a9-0f033773c013 | -11.3735 | -44.04446 | 2026-09-19 04:04:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| def3ecbc-40ab-38d3-86ca-6582edebc7cd | -12.12442 | -46.99192 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c86a222-e44e-3c7c-8341-f8cc3872a487 | -10.84392 | -50.18562 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
