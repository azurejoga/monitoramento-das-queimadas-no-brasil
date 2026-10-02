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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bb4037d-2e67-3454-bfc0-e289f172e36d | -13.86775 | -43.63589 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd33c629-bf11-3ef4-9e26-81ae73a60563 | -13.86687 | -43.64169 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 384c3c24-9862-34fa-a181-dcd41b0f293f | -11.7611 | -43.58027 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c3180ab1-bd77-3cbb-87bb-4a561bc5c9b3 | -10.78304 | -53.76823 | 2026-10-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f7cf377-8805-3a9b-af82-eb92677ca73c | -11.40513 | -43.40704 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2027ea8a-7b2c-3c29-beda-f300864d02c7 | -11.76418 | -43.57145 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d64fc65-a4b2-33cd-b587-9f6fbef57271 | -9.88506 | -50.17689 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4c5d644-1a0a-35c6-92a3-665f25b52fb6 | -11.2465 | -45.20523 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd1c12a2-c57a-30fd-b216-793b3ae8034f | -11.46164 | -43.42512 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cdd4707-c4a2-3b68-b817-fc7ecb88f2df | -11.65945 | -43.59882 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7f870a66-cbe5-39c4-a049-454c9f51a493 | -9.2125 | -57.71975 | 2026-10-02 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4411c2b-ca96-3301-a046-370a162ba96b | -9.80384 | -48.18753 | 2026-10-02 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83feb99f-46f5-392a-aed7-2c172c91555f | -12.91511 | -44.82021 | 2026-10-02 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cca17d05-1dcf-3e51-8ac7-027deb5b8100 | -11.75059 | -43.44667 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33fdab45-f1fa-3669-be12-a10d66cf5a28 | -13.86093 | -43.63525 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0893fbb5-bb45-3497-8634-207ae54ca9cc | -9.7877 | -44.8042 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e538336d-4d48-3d31-b7b6-0d909adf5555 | -11.46313 | -43.42759 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0e52ced-b200-32c5-9eba-4f5beef27a76 | -11.6447 | -43.55918 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92f23cc9-1295-3536-83a0-23ceba75947d | -11.79143 | -43.5593 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4940a2c7-0821-3b8f-bbc0-612d30e44ad8 | -9.84326 | -44.83785 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 716f6a59-af69-3646-935c-aa2539ab392c | -12.66605 | -45.097 | 2026-10-02 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e76bc00b-f639-3078-918e-2fafe329beea | -11.46895 | -43.43383 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79f338e9-a6bf-3b06-8205-ad68706a78f0 | -9.74689 | -53.87754 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b57dd86-1bd2-3b7a-9f72-3e0353d802ef | -11.46373 | -43.42221 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e950af95-0464-3323-9051-95f5ccb81b7d | -11.73714 | -43.45025 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ad22081-53d5-3d2f-96c4-7e725ba24d26 | -15.31028 | -42.76934 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f37171be-c3ea-30d4-b994-d4184172acb7 | -10.26677 | -49.6659 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69d2946a-1a7a-330c-821d-2a6feff5c32e | -10.8309 | -51.09295 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6c412fd5-1227-3314-8f0d-a609a326d105 | -13.55722 | -53.18743 | 2026-10-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d4253b0-74cb-31c9-bb30-20b66d1e6e79 | -8.33375 | -55.27745 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc43231a-3424-38da-b4c7-3d5d4d9d4023 | -11.71969 | -43.43155 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8600717-0340-3466-a6f5-caf25d5d6b9a | -8.30819 | -54.71971 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe974339-aeb1-3ce6-abc6-34950349c07f | -11.14148 | -44.60842 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34cd26fa-0cf3-34e4-aa62-131ce07f1333 | -11.68755 | -43.60157 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be2c1fe8-076c-3741-b78e-8d2386c1da25 | -11.76973 | -43.57988 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0efdf741-0cc1-33d5-ac8e-f57aeec2f12e | -15.31861 | -42.7559 | 2026-10-02 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8952941c-3fff-3359-8e15-56b5a680a923 | -13.34377 | -43.85407 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d86b180-1038-314a-a6e1-cf3c35da2d41 | -13.33445 | -43.86159 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbf5c96f-672b-3abe-9681-cc768305d1ed | -10.25321 | -49.67184 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3bfe627-4363-35b3-a532-367250eeb601 | -9.7757 | -44.80649 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a81120cd-8e77-3749-93fd-cc0349b29b17 | -13.86745 | -43.63601 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa44a781-d3db-3a4b-ba82-46f04c802e9d | -13.86062 | -43.64079 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af7dad63-15bd-3829-8a2e-9e7b9084d58e | -11.79635 | -43.57335 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80e3a83b-2f59-37ee-b186-1fc5d1d8d5a0 | -8.54713 | -54.56179 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e27b3cc7-7b16-39e6-b469-493c25bbbe19 | -11.74853 | -43.57707 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b16f2b5f-81b0-3104-b158-1a1fbf6ef0ad | -11.75701 | -43.44754 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52326bab-215d-369f-bc39-64cb9fe0388a | -11.6558 | -43.59681 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e62b2b8c-7207-32fc-9fcb-c27d6cdd5c1e | -15.31719 | -42.77056 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 5adb2e26-30e9-3dbe-8bef-8e06d5aca15f | -13.5531 | -53.19099 | 2026-10-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07719f42-2a2c-3e9d-bd19-e83085e603fd | -11.74449 | -43.57395 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 053d7f0e-cd8b-3693-8ebe-0a38c5868df9 | -8.30327 | -54.72958 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d229b226-5896-38e9-9244-54827334a121 | -11.47446 | -43.42679 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b8d4c84-8b5b-350a-8cea-e1362a786ef3 | -9.79195 | -53.82919 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78b98b16-7b4e-3ccf-b541-ece91c6518cb | -11.69452 | -43.59702 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dbeef7b-be32-3664-946b-70509abd6123 | -10.26312 | -49.66143 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29846ed4-8d16-36dc-9bd4-a7dd75db0fbd | -11.24706 | -45.20076 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f702e1a3-b0c7-308b-b5e7-7ae1d2884441 | -11.66723 | -43.61016 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6189b8a1-f9d0-3f27-ae90-faced4abbc6c | -8.55043 | -54.56231 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a863abbf-c4b4-3d1f-a800-366665ed41dd | -9.88555 | -50.17336 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c4d93d2-f075-3852-bf62-d8ae8076cf53 | -9.82507 | -44.84315 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e30cad49-6430-3ae0-9a30-2cc3eb7379c3 | -12.32662 | -46.38013 | 2026-10-02 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ab3cfb6-e8a5-38b4-8227-ec70c0a60fbf | -11.24335 | -45.19992 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c00ddeb2-2564-39ab-acc8-3c23fafbdfc4 | -15.30938 | -42.77847 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| cd1cd81f-076f-34f7-b1c1-be90a2b650c0 | -12.18092 | -57.10679 | 2026-10-02 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20fc00af-3b72-3d65-b99b-2e0b75e0a029 | -10.40489 | -53.7816 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e854c268-699a-319c-be8b-6c5aa67dd9e2 | -11.75487 | -43.57815 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 07be3afd-e0d1-3499-a9b5-382881fd2604 | -11.75018 | -43.58114 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 18aae86b-fe6f-3d01-b886-c75fc2a36c51 | -11.15876 | -44.61523 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f1b2a850-736d-3194-a4c1-29710352f914 | -11.14097 | -44.61274 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b9680cd-be25-363a-aaa0-b86bc1bc3379 | -11.6531 | -43.5979 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b648b7f-eb01-330d-8568-856e30d56b3f | -11.77438 | -43.57742 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5472c44-3f95-3ae1-8393-d00a349a8845 | -11.23769 | -45.2295 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87c48686-3896-3799-b4cb-98acd7a325cc | -11.73581 | -43.5751 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d80e963e-52f1-3520-a5fa-24e62d436526 | -15.30893 | -42.77892 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 267.2 |
| b42bd4dd-c82e-3c8f-9bef-5ff9587fb0cd | -12.91562 | -44.81557 | 2026-10-02 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 791cf1bb-3f4b-32cc-ab80-33ded90677d6 | -9.33738 | -50.99221 | 2026-10-02 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 264db33b-1c13-3207-a24e-5ae841e516db | -13.86653 | -43.64719 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 53862acb-192d-3c1f-ad16-96cc02f6cbe2 | -10.94042 | -68.72478 | 2026-10-02 04:59:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61568ca0-0446-3aba-af3b-eacb594f691b | -10.43532 | -53.84262 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fcb5b63-5d47-305a-85a7-f3d088083c77 | -9.81127 | -44.81244 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df03d910-587c-32a0-be59-45b09481cd46 | -10.05621 | -53.12175 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3eadd72-d887-30f7-a74d-7af6c73cdce2 | -9.82687 | -44.81844 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ebe925f-bc60-30fe-9ed1-ad690155c5ab | -11.71326 | -43.43069 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ad9f4a-d74e-3b82-af28-2ff66c1719e4 | -10.25067 | -49.67708 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eae98dc3-2f93-3a2a-bfbe-caad16a4781f | -11.77672 | -43.57522 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5eb9777-bae6-3c30-8979-f07891b672ae | -11.76914 | -43.58523 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a6fc1850-db57-327b-8158-10e7694c8c58 | -11.1523 | -44.61889 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 837e9fa6-e806-3ea0-957d-8ddc11e3943c | -9.64973 | -54.3384 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e22965ae-31ee-312d-95e5-c3985bca7640 | -15.32329 | -42.77994 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 306.0 |
| f7de2cf3-eec7-3e67-811c-f48d8bfbe161 | -10.80796 | -49.33748 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cb411df3-d2a6-3f7d-80c4-ebd615c26263 | -11.46615 | -43.44202 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a52fb02-0929-34f8-a362-9df7b4117a45 | -9.82848 | -44.81535 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ffd87ff-dab9-308b-822e-981b13ba89ba | -12.52855 | -43.09837 | 2026-10-02 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6c36198b-a15d-35f3-88d4-9fd8954df1a5 | -11.65816 | -43.60983 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9a68e5a8-0faa-3ca0-8621-f049f6a702dc | -8.50524 | -54.94287 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b0c32c2-da0f-3f45-98b1-b7279fab3128 | -11.77296 | -43.55051 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6c318e-5b9f-3154-a8e2-0990c97375e5 | -11.66032 | -43.6143 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c531248d-23ec-3028-8bb8-d3e63514fd7c | -8.29007 | -54.72751 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04e9dd4-41da-334b-afde-763fbb7df4d9 | -15.30976 | -42.76984 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b92578ab-ce47-3e97-bb56-0244d4e89049 | -11.76739 | -43.58182 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README69.md)
