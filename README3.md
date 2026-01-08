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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afa69a4b-8fc9-3922-b4f3-d62bab27a64c | -4.2763 | -43.77874 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ccf97189-f05d-3159-9404-c4b5dcd83276 | -7.5675 | -46.48139 | 2026-01-08 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3b0c619-332f-3071-bc75-19945a51e813 | -5.04125 | -40.85992 | 2026-01-08 03:53:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fc6c81d5-24c0-34bd-b970-9995bca01faa | -5.28101 | -45.83297 | 2026-01-08 03:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| febcd3cc-c923-317e-903f-2fce5e06e49f | -4.28016 | -43.78476 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9a3f16-952d-3f96-8280-661e534d1264 | -4.27241 | -43.77293 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a32a26ef-5e58-3de1-a22e-360bf3f64bdf | -4.26207 | -43.7764 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc8fdd35-d98a-3c6c-8ac2-917b7119f5af | -5.56288 | -45.45781 | 2026-01-08 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e4df620-d0a1-3cc4-9d7f-617aa0d2483b | -4.26682 | -43.77716 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41d2e17f-5dc8-3d4c-af71-dfcc4facf9fc | -6.34034 | -43.37931 | 2026-01-08 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bb852d0-80eb-3110-808b-8c16a27e4a99 | -4.26853 | -43.76708 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aaec458f-c2d5-30b9-88f2-f7d44b05c7b3 | -7.56212 | -46.4804 | 2026-01-08 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e161b1-2df9-3f9a-a109-30bd680309eb | -4.27326 | -43.76793 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0e8c9ebf-26c1-3361-9162-5d96e8086c0d | -4.26594 | -43.7823 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 353dac75-25c2-3ce3-81e3-b8905af81bf5 | -10.17679 | -39.05136 | 2026-01-08 03:53:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 042e7b5f-ffef-34fa-a23a-4e9a8032e1c9 | -3.70887 | -46.97927 | 2026-01-08 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c416e04b-4272-3f23-91b0-33a093111a2d | -3.86934 | -42.51294 | 2026-01-08 03:53:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28991b64-3c31-3b7e-823d-d54f2aa1bafa | -4.28361 | -43.76434 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae57892c-f189-32ff-aeba-db09004a940b | -5.04048 | -40.86471 | 2026-01-08 03:53:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0f9334c2-713d-3c1a-b7f6-1c793ffacbed | -9.34256 | -40.46699 | 2026-01-08 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 07eff578-5ecc-3fd4-bbfa-4fd77d8d9cbf | -4.28576 | -43.7805 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 396d72e4-3248-39ff-adc3-396a3e7e513f | -4.51566 | -43.69486 | 2026-01-08 03:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23901fca-8a8a-3c79-af62-82d9065dee50 | -4.28274 | -43.76949 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ac66d7d-f47b-3b94-b7cb-3f21aa074dde | -6.34481 | -43.38004 | 2026-01-08 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73978c8d-51ca-3617-a14c-2e404ff51173 | -8.69267 | -39.58522 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02d24099-c1b8-355e-a348-f9092040c47d | -7.56688 | -46.48478 | 2026-01-08 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 068a8b46-a7b8-3e73-9925-0d2f6111ef94 | -5.04286 | -43.26349 | 2026-01-08 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c5edef1-b431-3d9b-b39c-526f65dca6bd | -6.34408 | -43.38438 | 2026-01-08 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c687ee37-d083-36d5-9a35-af315ea8901b | -6.28037 | -39.88557 | 2026-01-08 03:53:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b84cee80-15eb-3cc3-bd81-c1f43223ed11 | -5.58314 | -43.75347 | 2026-01-08 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b0f7f06-05b4-3a2c-9409-96d15f771c0c | -5.28642 | -45.83363 | 2026-01-08 03:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a51998cd-1a86-3ea9-997d-9ab6acee69c7 | -6.07959 | -37.31288 | 2026-01-08 03:53:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3924c089-6ec2-3088-88d0-5722daf78dd3 | -7.75273 | -41.39392 | 2026-01-08 03:53:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea91287a-7e8d-346b-810f-c90b2a37d2fe | -3.73531 | -44.55342 | 2026-01-08 03:53:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd9e00c7-ff70-32e1-8953-b87945277ed9 | -10.1439 | -36.20848 | 2026-01-08 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f80f1b2-0cbf-3137-b23e-efdf41b030dd | -4.96974 | -42.75958 | 2026-01-08 03:53:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3338ee6-a7d0-3c29-888e-29215d9348b2 | -4.27371 | -43.79401 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da8eafa9-a50e-33de-8873-0cf54f2fc68a | -4.28189 | -43.77456 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f67e7806-f6e7-3da3-af09-dcdeaa1bcdb8 | -10.14446 | -36.20481 | 2026-01-08 03:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2cdcab5-e0c3-30cd-872f-5a9e2b4dcb58 | -4.96588 | -40.58403 | 2026-01-08 03:53:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 08467ddd-0721-32c4-9f6d-df70f3669ffe | -5.5918 | -37.27846 | 2026-01-08 03:53:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf5f6f49-b655-34ee-874b-b49f6289ff17 | -4.27069 | -43.78308 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31a599ff-c2b9-3c34-8b0f-55891a7e0996 | -4.2849 | -43.78559 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41dfb0c9-d09b-33d7-b637-d22e025eb0fc | -3.87441 | -42.50947 | 2026-01-08 03:53:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e5d412e-5007-3263-a75a-5bbda2f80ca4 | -9.64446 | -42.95292 | 2026-01-08 03:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61fc449c-139e-37df-81a7-d2e7209408d1 | -6.56486 | -35.24192 | 2026-01-08 03:53:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d2d20062-d23c-319e-802c-8f7462614405 | -5.79583 | -42.68589 | 2026-01-08 03:53:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aeb52844-7442-3362-be5a-cfd31a1e5925 | -7.82135 | -38.47084 | 2026-01-08 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4facd848-1f34-3c7e-8909-e53eb719bba0 | -6.6669 | -35.12141 | 2026-01-08 03:53:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 083509c3-79de-3844-9c2c-098d44428b2c | -4.27413 | -43.76284 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c506f62a-c96d-3191-8cd5-22ce3735c581 | -4.27887 | -43.76357 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6822b1a3-eee1-34b3-997c-48592c0e661a | -7.56475 | -45.62688 | 2026-01-08 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62d69b64-a018-3f25-b2a3-1aa553174d51 | -4.28406 | -43.79059 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757adb5f-a349-31fe-a867-2d23c9e0479d | -9.64382 | -42.95662 | 2026-01-08 03:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf8fc385-3552-386c-a7b4-c92dd250e1a8 | -5.32525 | -37.59217 | 2026-01-08 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db86b320-df82-314f-a174-2d95762c9570 | -4.27157 | -43.7779 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8c893649-39e7-3950-a007-315cb0d1b21b | -6.09525 | -40.31243 | 2026-01-08 03:53:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 782a27e8-4fae-3dd0-aa15-631559d4e3cc | -5.79154 | -42.68519 | 2026-01-08 03:53:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51b802eb-bf53-3e6b-98d4-5a70f87cebff | -5.04434 | -40.86534 | 2026-01-08 03:53:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a6358628-6913-3d51-a62f-b1f65c9475ed | -9.34107 | -40.46547 | 2026-01-08 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 55a90743-10d0-3e72-9f4d-1d6bc356e2f9 | -4.51151 | -43.494 | 2026-01-08 03:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c118c382-bcd0-3270-b350-2ecb669c831d | -5.59513 | -37.27899 | 2026-01-08 03:53:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7ff7b82-0232-358c-affa-c994c414e279 | -6.06883 | -39.18378 | 2026-01-08 03:53:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f23268c7-0fee-3ec1-a75b-9c262fb71ec0 | -9.64856 | -42.95366 | 2026-01-08 03:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cd832159-7c69-3f56-8143-763e149664de | -5.56283 | -45.45802 | 2026-01-08 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e6cfb11-6c3b-3da1-ac60-3f0fc16b1ba9 | -3.92186 | -45.58316 | 2026-01-08 03:53:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ed41988-2b39-35ca-80af-6dc5dcf49e48 | -7.71128 | -38.05133 | 2026-01-08 03:53:00 | NPP-375D | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2b2f7526-718c-3417-9082-93b5be04ce5c | -3.87372 | -42.51366 | 2026-01-08 03:53:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c75d05f1-8777-352d-aa3c-4f9339583ced | -5.63857 | -35.23228 | 2026-01-08 03:53:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac87bf45-0161-339e-8b00-62de55eb25ec | -5.53928 | -38.19675 | 2026-01-08 03:53:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc379a07-e5af-324b-baa1-ad92d846c9c5 | -9.07057 | -39.92319 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f2e61643-df34-33dd-9441-4bdcbb4f554d | -4.26768 | -43.77208 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 01550c88-9589-374f-a8da-ccb58c1cb595 | -4.28747 | -43.77034 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b602b02f-d00f-386f-8a07-7d2abdeccbe8 | -4.26422 | -43.79239 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b77f08e0-0fcd-3d01-a869-cdb01089f9d7 | -6.28396 | -39.88621 | 2026-01-08 03:53:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f558e498-2a3f-3223-8883-4adfd422f434 | -4.60274 | -45.99378 | 2026-01-08 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42738fb2-0c73-3200-909b-a4c36edb90a7 | -5.287 | -45.83035 | 2026-01-08 03:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 823c53d9-2a34-3c8e-a945-914a2ec03896 | -4.28662 | -43.77542 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c4fdb897-09d1-3ea8-ba60-96eb24b4145f | -7.56812 | -46.478 | 2026-01-08 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0c4a79-cf13-38be-8156-2476805dff3b | -4.87556 | -42.73287 | 2026-01-08 03:53:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c55d6e-3c49-36c3-9bcb-1e687918d8c5 | -8.81944 | -39.82708 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ead8af73-1507-3b8f-a8fd-01a8cdf42ed7 | -5.74836 | -45.10937 | 2026-01-08 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 069a6cd0-0d99-350c-aa53-91564014adb7 | -5.17617 | -37.76022 | 2026-01-08 03:53:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e1f031bd-173b-3ec5-ba78-4b38db9e6445 | -4.59723 | -45.99297 | 2026-01-08 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91baf276-545b-3f90-b3c1-bd087af2d37c | -5.32469 | -37.5957 | 2026-01-08 03:53:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 270342f8-45f8-3b15-a8de-508e7891794e | -8.58947 | -39.44373 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce2b76cb-890c-3857-ae0a-2ad19bb401fe | -3.70293 | -46.97829 | 2026-01-08 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98f3235f-b23a-3609-a868-526ebbb10dae | -5.04037 | -42.50002 | 2026-01-08 03:53:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58ad14d0-a313-3e82-a98e-3eac5c5cd318 | -5.03834 | -43.26273 | 2026-01-08 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25423f14-bd62-38ee-b514-bcb312779316 | -4.25645 | -43.78074 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9286d973-3fe0-33ee-bbea-c55ddbd41dc6 | -5.04565 | -40.86269 | 2026-01-08 03:53:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 55181c37-a7de-33ac-97f4-8a546c4dad23 | -4.27931 | -43.7898 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2a4477-8aec-3fbf-b120-193c619b556d | -4.26981 | -43.78825 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b73ca0-9709-370a-a5a1-6cb76cf83063 | -6.56544 | -35.2382 | 2026-01-08 03:53:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd6c0904-2c8c-3a38-bde6-cf0ec5a24fe5 | -5.04511 | -40.86058 | 2026-01-08 03:53:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 092f71a6-c801-3ab0-8577-a6a7586cae54 | -4.26119 | -43.78155 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70ee80b7-470c-3b1d-8ced-3304f0f7edb1 | -5.24474 | -37.50299 | 2026-01-08 03:53:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f8a51d00-c33f-3401-8b37-bb05038f2f7f | -4.27715 | -43.77372 | 2026-01-08 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0dbc522e-afa4-37c3-9d29-da645e44bd94 | -8.68859 | -39.58846 | 2026-01-08 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b90498f-08a5-30ee-9d60-cefe19c673c4 | -6.58824 | -44.62307 | 2026-01-08 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README4.md)
