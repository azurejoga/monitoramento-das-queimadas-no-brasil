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
| bd21fe2a-d425-35c1-bd99-49eb43e40882 | -9.29905 | -45.49253 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b4f85b9-249e-3905-b286-276054ef1072 | -11.47949 | -47.40217 | 2026-05-23 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d824f475-97bb-3790-af4c-a544bc305ccf | -7.64851 | -45.30022 | 2026-05-23 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c1d79cb-64a8-379c-9cbf-acc324d92460 | -11.00669 | -46.81584 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9550fe1c-b579-3ea4-8880-53f0d28305cd | -11.54731 | -56.93923 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dafe19ee-a33f-3ff2-a1b4-b5c0f385ab29 | -9.29844 | -45.49661 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c189b967-237d-3741-90da-6f4715dd0e43 | -10.91457 | -54.11515 | 2026-05-23 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 544ea8b8-aa4a-31e3-aef2-c449d57b6b6a | -11.05686 | -46.83127 | 2026-05-23 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22fcb337-32ca-33b8-b7c2-c4636e3a351e | -6.85206 | -48.73709 | 2026-05-23 04:34:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6849d930-ca47-3c5f-b099-af00409a3d92 | -8.43481 | -51.5546 | 2026-05-23 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d28ec3cd-0ec1-3284-8b2b-ffc9c6582b94 | -11.44242 | -52.92784 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55a89017-dbda-3fd0-9619-4d6efb37cc75 | -10.79835 | -49.41124 | 2026-05-23 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41f4e299-2b78-3e4e-9dce-d72466678fed | -8.43844 | -51.55519 | 2026-05-23 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 105c9c88-0d1c-3c39-9478-bd5984dd1047 | -11.92626 | -43.87036 | 2026-05-23 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b77d17df-84be-3f50-b959-6d7048a8a2e3 | -9.29488 | -45.49609 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca64a5cf-d5fb-3707-a18a-01186e5d5fd8 | -11.6141 | -47.90351 | 2026-05-23 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfaf51e4-8148-3463-89ee-5951fb7b76c1 | -8.73924 | -50.24056 | 2026-05-23 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2739db6a-6823-3ee6-b1f9-710b328ec3ce | -11.45072 | -52.92452 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cd9b8603-4239-30f6-9694-393cf4c079e3 | -11.05857 | -46.81993 | 2026-05-23 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fd2d4f5-c0dd-3893-ae9c-bc482015c392 | -11.07853 | -46.68734 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54fed070-a1f2-363f-9b60-9877d8bd9c4e | -10.91734 | -54.12332 | 2026-05-23 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d9dfc2-3421-35ef-a32d-4f64528e6398 | -11.55365 | -56.9429 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dcd2a79-5af4-32e9-b60e-39cb9b1946ba | -6.39 | -44.17141 | 2026-05-23 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 735e53d8-04b6-3f3f-9c1b-a997dfa955c1 | -11.00724 | -46.8121 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d82d9eb-cd8f-3cb0-82b6-f9161407a239 | -11.61007 | -55.33438 | 2026-05-23 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cc6593e-ddf6-392b-adfe-71a0dbaac9ab | -7.55161 | -42.64714 | 2026-05-23 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8d3dcff-4998-3b35-b330-d922f3bb5d59 | -7.36389 | -43.8654 | 2026-05-23 04:34:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d960d81-13c0-30f9-8ef7-3e1f09a07507 | -11.84705 | -43.96806 | 2026-05-23 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f4ef49f-9e8c-3766-bb96-08056c194d02 | -9.21886 | -48.59387 | 2026-05-23 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ce9183c-c90e-32e7-8324-c57412c3d894 | -11.05515 | -46.84262 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa84918-2a34-36c4-8895-c4f7ecbc7f46 | -10.59828 | -53.47327 | 2026-05-23 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2098706-39b9-3aec-9e9a-019e5a5ac34f | -7.05038 | -45.06384 | 2026-05-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cac399e3-ac59-351e-927d-6d4c4e0eaa5b | -9.95144 | -52.42203 | 2026-05-23 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86512cd0-b64e-3122-bcc4-000102b6d8ef | -11.61744 | -47.90403 | 2026-05-23 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 663588a5-a63c-3a18-8cb8-f98890431ca4 | -11.29651 | -47.57517 | 2026-05-23 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d14a32-7541-3884-bdaa-176a0d444b91 | -11.55749 | -56.94946 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6a070ab-07a1-3a31-84ec-1c7407a4bcb5 | -7.30026 | -47.06232 | 2026-05-23 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46929a69-9a9a-376d-aa5a-ef4274300c11 | -8.52486 | -54.7721 | 2026-05-23 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9976d7d-465e-3731-ad01-2eb3289861fa | -11.56185 | -56.94217 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6f3941e-cabc-35fd-bd2d-29ace769eb4b | -11.48287 | -47.40268 | 2026-05-23 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8bba7d75-2831-3ae9-a6ac-a1d56da746d1 | -7.21811 | -46.91229 | 2026-05-23 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f226e30-a2f9-3f1a-a928-5a670ee25bde | -10.48408 | -42.41366 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| eca8c0c4-373a-3084-a440-9eb96d7bb72a | -10.64981 | -49.72475 | 2026-05-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3295211f-42c7-3685-b84c-29de1dbdd89f | -9.45002 | -50.84586 | 2026-05-23 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e9154a-fef1-3b70-8c36-0845db590c9b | -9.28838 | -45.49096 | 2026-05-23 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20e49637-d302-323a-bb7b-afed36ebd20c | -6.39369 | -44.17198 | 2026-05-23 04:34:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d80ea4a-4fee-3486-a06f-f1407af7a72b | -11.55607 | -56.32771 | 2026-05-23 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e65d3e-bdb0-30cf-ac9c-f369aa4b248c | -9.65127 | -47.26981 | 2026-05-23 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba94608-5417-37d0-8d57-6576d937ee9a | -7.92732 | -47.82372 | 2026-05-23 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4db814-13be-3ed1-9fd9-cc37d318092c | -12.05882 | -45.26981 | 2026-05-23 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8cd435-05c6-3fd2-89e9-c616dc66f125 | -11.44994 | -52.92914 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8f8813f2-50a3-329b-a027-4f759539ce61 | -11.01178 | -46.80514 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 449b5ac5-035a-383e-8c5b-b89548760df0 | -10.65257 | -49.72884 | 2026-05-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ba63549-ddf5-326f-b190-6190df1392bd | -11.55264 | -56.94847 | 2026-05-23 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b255aeee-256a-3b14-9cad-5dd054ddd464 | -10.66148 | -48.26361 | 2026-05-23 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54293096-8222-3610-86a3-a916fc776b67 | -11.18022 | -55.91943 | 2026-05-23 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6f5e1128-2709-31e8-b6b3-76c115ca9692 | -11.46733 | -52.91787 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aaf5b82-26b7-3341-9dee-26530b3a97a6 | -10.48525 | -42.40516 | 2026-05-23 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ea55851b-d68a-31c1-b02f-30b53830b223 | -11.05457 | -46.79995 | 2026-05-23 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a696f3c2-7f46-3c53-a6d1-3988c47468ac | -11.35213 | -51.41239 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78dab9fd-bcc4-3537-97a3-3841512654d3 | -11.70806 | -54.62953 | 2026-05-23 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e8905be-c160-39c4-a3b0-96046f72e186 | -11.43866 | -52.9272 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2eaa3ed-5f86-34aa-9971-9766c242d22d | -10.7121 | -56.24479 | 2026-05-23 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8848fd64-6cbb-36ff-939d-84d4caab27d4 | -7.92402 | -47.82321 | 2026-05-23 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e54b809a-5683-36c1-925d-df6138d2ca8c | -11.18479 | -55.92026 | 2026-05-23 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5a35990d-af94-393d-9a13-37d130efd1b7 | -11.3132 | -47.55555 | 2026-05-23 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 625a2965-c5c2-3039-b852-31eb677be0a8 | -7.64792 | -45.30421 | 2026-05-23 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a0a6346-fd6c-3005-af06-38e12f088932 | -10.87571 | -49.39481 | 2026-05-23 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c457a84-0f21-34ba-bf33-49e5af9f0fd5 | -11.84753 | -43.96452 | 2026-05-23 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 932917d5-362e-3703-a080-c292e3c936d6 | -12.299 | -47.91494 | 2026-05-23 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abe69e82-50de-3732-8e78-14697e30d449 | -7.13351 | -44.06839 | 2026-05-23 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2483c7e4-eb5e-3728-bdfc-a52a7aabe55a | -11.45448 | -52.92517 | 2026-05-23 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 714e55ca-cad5-3373-b8ce-1f19c1c6c693 | -7.01143 | -45.0085 | 2026-05-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d45608-2bac-3453-af88-a1387d2f6042 | -9.55131 | -48.66496 | 2026-05-23 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 691d2a29-b67c-3a6e-99cb-f4ff44100505 | -11.05906 | -46.69988 | 2026-05-23 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a7e873-d0a8-36a7-ab95-7f6f790af8bf | -6.84873 | -48.73656 | 2026-05-23 04:34:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 299df294-f296-3813-940b-b91d495ec4aa | -8.0295 | -46.44955 | 2026-05-23 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df8da9d0-2776-3aeb-baa8-585dd2bc355b | -7.13541 | -44.07133 | 2026-05-23 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ce79d28-617e-3467-8585-81bb5120dd4c | -11.95018 | -57.03928 | 2026-05-23 04:36:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e3380d2-bcdc-39fc-b182-701e09ae89a0 | -12.17082 | -56.45332 | 2026-05-23 04:36:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef58b905-5392-3d16-9f8b-f2f2c715ec1c | -16.33526 | -52.77417 | 2026-05-23 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de6ed84d-532f-3f08-a5b8-c97f6ec9b698 | -11.79416 | -57.35334 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e8eac7-ab3a-3b25-aa90-f25445cb6363 | -16.33471 | -52.7744 | 2026-05-23 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59f8c6ee-9254-36da-b980-013cf9d5e1a2 | -11.79468 | -57.35049 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001ab795-74bc-3bf1-adae-84c8a37f7b3a | -11.79309 | -57.35917 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 178fd621-2c22-3e2a-8a78-8fe3bdba32db | -16.49182 | -45.91263 | 2026-05-23 04:36:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67835cfc-b98d-33d6-b808-d2d91739b371 | -11.79255 | -57.36209 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60c36ee0-3773-36f7-9bd5-321ba165bac2 | -11.79362 | -57.35625 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6be45302-888c-3198-8565-cafcb3d4d05d | -12.17172 | -56.44836 | 2026-05-23 04:36:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b24ea0b-43d0-303a-99e3-01867adfcccc | -16.6386 | -46.87083 | 2026-05-23 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cace23dc-1698-3f87-b20a-a62bc19b7d8b | -14.30367 | -49.24974 | 2026-05-23 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4fd999f-4b8b-3413-9312-b0ae642a91cd | -11.78916 | -57.35252 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c52b91-788c-31e5-96ac-1b0f55b7ff42 | -12.4123 | -54.19912 | 2026-05-23 04:36:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 298fa4f6-b7c0-3e77-b3bd-faf4cfbfcccc | -11.79754 | -57.36298 | 2026-05-23 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f541fc33-046f-3702-bbf8-9e77dc02e9da | -21.49283 | -48.64144 | 2026-05-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeb05e07-f5d1-3cbc-95e7-8c3135228947 | -21.52376 | -48.62503 | 2026-05-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be9c17f5-77bf-3ffe-a5c5-6e23ebd741bc | -20.76595 | -48.56843 | 2026-05-23 04:38:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71396163-5a47-3e6b-8231-08f42ad5d171 | -21.52085 | -48.62027 | 2026-05-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae08d0eb-15ee-392c-8060-82d832ca0097 | -21.49224 | -48.6456 | 2026-05-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3b58cc2-8f1b-3c73-8c31-a8c4ddc97946 | -21.52026 | -48.62448 | 2026-05-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)
