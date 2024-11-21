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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f383a4f-718b-360a-8ee6-954ebb603e27 | -5.10343 | -43.16784 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 378c9abd-63be-3042-965a-2224afec5233 | -3.28219 | -48.79844 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c10df2d-94a1-37f6-a1bd-eadd881b8b86 | -1.45469 | -52.66541 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277dd46c-8590-3126-897b-6f43eebce822 | -3.07123 | -49.20446 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 71fd52d4-6a08-3bcd-b107-add6b880393a | -3.59725 | -43.63705 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f7d8234-8ffc-3ee3-824e-a9919a1e2355 | -2.71493 | -46.08918 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b40a0da0-7cc4-3297-bd48-46c44e3aaa1e | -3.08028 | -49.21177 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e70a6fcf-a4cd-30ee-89c7-376160f1b7f2 | -3.29899 | -50.36443 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f79f9f3c-2fcc-3b66-bf24-8e760bc5c554 | -3.00724 | -51.3131 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a754f70d-b89c-3531-b24a-3244af088273 | -3.80244 | -52.22065 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 655020af-0ef2-3a90-abeb-866773db0342 | -5.11022 | -43.16889 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0e7e296c-3c30-342b-9ab7-69e3cde30e7e | -3.28913 | -49.19403 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bdd83df-a814-35dd-b24f-d1711b1a6e5c | -4.74692 | -45.41463 | 2024-11-21 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d02db5-8098-34e9-acc7-c7500cd0c320 | -2.33761 | -53.93158 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b1ba4a77-f835-3154-9cd1-334409c164f8 | -1.27045 | -51.60663 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3bbf0c69-7276-3cd4-8571-b28dcdfbb176 | -3.59437 | -43.6326 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa77d3c5-9aaa-3019-ba4b-38d617d4478a | -4.36813 | -46.09453 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9305afe1-3900-3d1b-add6-27c80904019e | -1.95321 | -46.25671 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b0603b-5036-34c6-b3aa-7e8b8ac9e117 | -2.59822 | -46.18986 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dcd0fc6-003d-3c6d-9979-4e29d0369e3a | -3.30492 | -50.36196 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67ec757d-89ed-3f7f-afec-ccba022227be | -6.64899 | -41.99235 | 2024-11-21 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b8aff80e-3573-33e2-9ce5-d117e85f4a66 | -4.04275 | -46.37264 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26f69e99-02e6-37ea-9224-6d2441b90f4b | -6.06977 | -44.15023 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c7b4011-ae67-329f-9da6-0a57d14f522f | -2.657 | -46.54892 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1c0110a-b8f6-398a-8d5e-f5bad022a024 | -2.84255 | -46.68923 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9534e076-375a-3718-be6b-5e56fd0e48ef | -4.96025 | -49.84238 | 2024-11-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b24361-28f4-3b6e-b2d2-c71c44569401 | -3.49564 | -50.44436 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7011cab-18a5-355f-ae4d-24ef5742835f | -4.77004 | -44.49454 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a29c782a-6a3f-344e-83f2-d7c5aae2f524 | -3.67646 | -45.24089 | 2024-11-21 04:08:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fb4285b0-8024-35b9-b6fa-9b5208cb7cb4 | -3.40013 | -49.78505 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61d9f5a3-3a6b-3dcb-aba9-eaedb1f206df | -2.92221 | -53.07183 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| caeeb074-1cdd-332d-a3c0-ad295cd0f01a | -4.38964 | -47.77335 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a13fda0-e325-3948-90de-28eb38363703 | -2.66682 | -46.23447 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1da1c482-d01d-334b-94c6-2d34cbd7cc3f | -3.46922 | -50.01388 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9b998abe-4f84-3e0a-8cd2-c418c977cc58 | -6.33405 | -41.9178 | 2024-11-21 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0dd121f0-07a8-395a-8c49-9fb2e6dce681 | -4.24269 | -49.08489 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af15331b-6967-3a10-962f-e3c732673bc0 | -2.62626 | -48.0645 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 724e385c-85cf-32f7-94b6-bc7b96a8e287 | 0.14056 | -51.09806 | 2024-11-21 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b1ba9fa-16aa-34ea-8c81-8e0145336f44 | -1.7437 | -52.05957 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 412fe678-fb64-3851-8d08-cedc1d5d913c | -1.54588 | -47.21469 | 2024-11-21 04:08:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5492451-ce94-3481-b136-787c8604e374 | -4.145 | -43.27963 | 2024-11-21 04:08:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd19c6ae-44f4-3e99-ab29-b9e0a7cf1630 | -6.21368 | -46.15793 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b20a588-8994-3010-9e92-00627b0ddc6f | -2.76725 | -52.11486 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f524d192-5f23-3045-9e8d-0133a925cd8f | -3.81318 | -47.79872 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6d331bc1-83ed-3d00-b421-642ce84dfd00 | -3.84565 | -50.69453 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2e4f9d9-f6db-3707-9c82-c9c06d1bff28 | -3.88874 | -46.65589 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 494a9fa7-5f09-34c3-8c39-2a110984f873 | -2.83538 | -46.6801 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca5d514b-ca07-3ca9-9bd2-3fd60e2b75aa | -4.35357 | -45.88801 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6075ea5-cf7e-3197-92a0-39ad715cf14c | -3.27833 | -50.52562 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f256ceeb-dbbe-3578-bb46-e0270ad8d510 | -3.37776 | -52.45838 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 926fc686-0a36-3eb9-8f6b-e6ff85481c41 | -2.64053 | -45.76423 | 2024-11-21 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff7a301-30fe-3ce1-8a17-d7af09fa24f2 | -3.26669 | -45.37129 | 2024-11-21 04:08:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da171049-c2ca-3826-96a3-1f77823a1810 | -1.70408 | -46.23373 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0965f9d4-0e82-32c5-be76-2d2d0f5e26f9 | -5.24101 | -42.63737 | 2024-11-21 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7892aa84-ab32-39c3-bc62-2a43fb022b2c | -4.4877 | -48.11057 | 2024-11-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a99ee41a-9b34-3d17-8bc9-9242eb5e54ae | -2.89187 | -48.27663 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4882e542-2d7d-3aa9-a16d-dcf75c3b1290 | -1.13891 | -51.67862 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b02e0a-501b-33ab-8753-120b11369d13 | -5.46365 | -43.26886 | 2024-11-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33f0ac70-a394-3d7c-ac48-3176da745898 | -4.76961 | -46.44746 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c2db1eb-5cf7-30eb-a9dc-d6d049696e26 | -3.75737 | -52.41134 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8e04811-e679-3a93-bd67-73c25f456b9d | -5.11882 | -46.18025 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59c3ab4f-85c9-3dee-8692-6f653a832584 | -3.49725 | -50.4482 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3fd1fa4-a173-3612-a2b9-eb03249df92a | -5.45195 | -43.23323 | 2024-11-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8039d810-c03f-3bf8-8a17-eed3a04306df | -4.48064 | -44.75704 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 639465ea-67b6-3cc8-a39e-169bad927209 | -6.11746 | -42.51666 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cba0fb6f-d7ce-3ffb-a9f9-20f9dd8a4ef5 | -3.12833 | -45.44773 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0bf2b8f-f3f5-3f58-b021-3ab5f837846a | -3.10365 | -49.44683 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b03b9f-4449-36b5-8eee-6473b2d69585 | -5.27141 | -44.37229 | 2024-11-21 04:08:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b266808-bfaa-3f7b-9a17-bcfd85aa04fd | -2.93551 | -49.43124 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 314a72ad-b4f9-3098-a17f-e36e1d29f6a4 | -1.05229 | -51.74302 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aad0e2be-ac9a-3f85-9abb-7981621d8326 | -5.52014 | -43.66196 | 2024-11-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05f568ab-fb10-316c-ab4b-6cf4aed349c4 | -2.65964 | -46.14711 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b92aa82f-8b44-326e-adac-eb0470f8de6c | -1.20123 | -53.6827 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2fe02631-64d6-3188-9c53-c47ba60d621f | -3.80701 | -42.54719 | 2024-11-21 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e3947ed-010f-3eb2-bfec-9b8cfbcb4f36 | -3.2941 | -49.19489 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 71469840-a7dc-3584-8fbb-fa79bb9d8ca9 | -1.46024 | -52.67175 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72e772ab-e0b5-3e45-a001-c64ea5c3c18c | -3.01643 | -51.0115 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e98ffb38-f652-3cdb-b363-0e275dc8e86b | -5.45646 | -44.82275 | 2024-11-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f687d76-c03f-319b-a8b4-15493adc2c0b | -3.34482 | -51.64817 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d49def9f-891e-38a9-be29-9db2961f67ff | -3.18008 | -54.3189 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1909b544-16f7-301b-8b2c-96cb2cf69e38 | -3.41955 | -50.252 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5296f203-646f-3c7b-9395-b872de42d5e9 | -2.92989 | -49.12478 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f882539e-f05c-3eb3-87de-ca9d53258543 | -4.95007 | -46.72412 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f51eaa2-404b-391c-b475-c1e701d1ee05 | -2.63012 | -48.07009 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a8bcecfa-12af-3237-9982-d1e8a7e0f977 | -3.29457 | -49.19205 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| da35dc0e-17b9-3624-a6a1-934f041ac1ab | -2.60997 | -54.53695 | 2024-11-21 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce19d87f-4d1c-381a-9ce4-da24d34150de | -3.78323 | -44.06225 | 2024-11-21 04:08:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50a100d5-9f45-3ce7-b18a-7aba29f3dc7a | -5.43005 | -45.34021 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40138068-d90a-3d58-a28f-ab6f2b234f89 | -3.96061 | -46.72483 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81ab4328-84b4-38d5-b4ea-e112fa76022d | -5.24172 | -36.18555 | 2024-11-21 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7d91003-0851-33e0-a209-9cb172b572fe | -2.16812 | -51.97046 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08a09c26-011c-3560-9cc6-1a853b151f23 | -2.6777 | -46.23975 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c01e785b-6c5e-3ad5-a26b-5c5c4663660e | -3.49442 | -48.22539 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ffa9b87-3c1a-3b51-9f64-0b3fa7f3a0e8 | -5.43814 | -42.83237 | 2024-11-21 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3ca6855-69ff-3eef-9b99-ea8fa73b352d | -2.01097 | -54.5244 | 2024-11-21 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9478fcdb-abb8-3e56-9af9-49be17e83fb5 | -2.69703 | -46.25043 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 681735d5-3118-3a33-9360-ff15c3e9bfe5 | -4.01088 | -47.97196 | 2024-11-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8697100-4007-37cf-84aa-416b111a8b94 | -2.61996 | -51.80088 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b537a600-3efc-3957-9864-84de95ed70ba | -3.63941 | -50.21612 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4a2a73-6146-37b0-9ab9-29ef46dcd986 | -2.80591 | -51.77043 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
